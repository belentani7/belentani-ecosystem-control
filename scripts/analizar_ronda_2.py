#!/usr/bin/env python3
"""Compara el inventario base con la segunda ronda sin modificar archivos previos."""
from __future__ import annotations

import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/home/ubuntu/belentani-ecosystem-control-r2')
BASELINE = json.loads((ROOT / 'data' / 'catalogo_proyectos.json').read_text(encoding='utf-8'))
CURRENT = json.loads((ROOT / 'data' / 'ronda-2' / 'repositorios_actuales.json').read_text(encoding='utf-8'))
OUT_JSON = ROOT / 'data' / 'ronda-2' / 'comparacion.json'
OUT_MD = ROOT / 'data' / 'ronda-2' / 'comparacion.md'


def old_normalized(item: dict) -> dict:
    return {
        'repositorio': item['repositorio'],
        'url': item['url'],
        'privado': item['visibilidad'] == 'privado',
        'archivado': bool(item['archivado']),
        'ultimo_push': item.get('ultimo_push') or '',
        'actualizado': item.get('actualizado') or '',
        'lenguaje': item.get('lenguaje_principal') or 'Sin lenguaje',
        'tamano_kb': int(item.get('tamano_kb') or 0),
    }


def current_normalized(item: dict) -> dict:
    return {
        'repositorio': item['nameWithOwner'],
        'url': item['url'],
        'privado': bool(item['isPrivate']),
        'archivado': bool(item['isArchived']),
        'ultimo_push': item.get('pushedAt') or '',
        'actualizado': item.get('updatedAt') or '',
        'lenguaje': (item.get('primaryLanguage') or {}).get('name') or 'Sin lenguaje',
        'tamano_kb': int(item.get('diskUsage') or 0),
    }


def main() -> None:
    old = {item['repositorio']: old_normalized(item) for item in BASELINE['repositorios']}
    new = {item['nameWithOwner']: current_normalized(item) for item in CURRENT}
    altas = sorted(set(new) - set(old))
    desaparecidos = sorted(set(old) - set(new))
    comunes = sorted(set(new) & set(old))
    cambios = []
    for key in comunes:
        before, after = old[key], new[key]
        changed = {}
        for field in ('privado', 'archivado', 'ultimo_push', 'actualizado', 'lenguaje', 'tamano_kb'):
            if before[field] != after[field]:
                changed[field] = {'antes': before[field], 'ahora': after[field]}
        if changed:
            cambios.append({'repositorio': key, 'url': after['url'], 'cambios': changed})
    changes_by_type = Counter(field for item in cambios for field in item['cambios'])
    summary = {
        'generado_utc': datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        'linea_base_repositorios': len(old),
        'ronda_2_repositorios': len(new),
        'altas': [new[key] for key in altas],
        'desaparecidos': [old[key] for key in desaparecidos],
        'cambios_en_repositorios_existentes': cambios,
        'conteo_cambios_por_campo': dict(changes_by_type),
        'totales_actuales': {
            'publicos': sum(not item['privado'] for item in new.values()),
            'privados': sum(item['privado'] for item in new.values()),
            'archivados': sum(item['archivado'] for item in new.values()),
            'lenguajes': dict(Counter(item['lenguaje'] for item in new.values()).most_common()),
        },
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    lines = [
        '# Comparación de inventario — Ronda 2',
        '',
        '> Comparación incremental. La línea base permanece intacta en `data/catalogo_proyectos.json`; este archivo únicamente registra observaciones nuevas.',
        '',
        '## Cobertura',
        '',
        '| Indicador | Línea base | Ronda 2 |',
        '|---|---:|---:|',
        f"| Repositorios propios accesibles | {len(old)} | {len(new)} |",
        f"| Repositorios públicos | {sum(not x['privado'] for x in old.values())} | {summary['totales_actuales']['publicos']} |",
        f"| Repositorios privados | {sum(x['privado'] for x in old.values())} | {summary['totales_actuales']['privados']} |",
        f"| Repositorios archivados | {sum(x['archivado'] for x in old.values())} | {summary['totales_actuales']['archivados']} |",
        '',
        '## Altas identificadas',
        '',
    ]
    if altas:
        lines.extend(['| Repositorio | Visibilidad | Creado | Referencia |', '|---|---|---|---|'])
        for key in altas:
            item = new[key]
            lines.append(f"| {key} | {'privado' if item['privado'] else 'público'} | {item['actualizado'][:10] or '—'} | [GitHub]({item['url']}) |")
    else:
        lines.append('No se identificaron repositorios nuevos frente a la línea base.')
    lines.extend(['', '## Cambios observados en repositorios existentes', ''])
    if cambios:
        lines.extend(['| Repositorio | Tipo de cambio |', '|---|---|'])
        for item in cambios:
            keys = ', '.join(item['cambios'])
            lines.append(f"| [{item['repositorio']}]({item['url']}) | {keys} |")
    else:
        lines.append('No se identificaron cambios de metadatos frente a la línea base en la ventana de revisión.')
    if desaparecidos:
        lines.extend(['', '## Entradas ausentes respecto a la línea base', '', '| Repositorio | Último estado conocido |', '|---|---|'])
        for item in summary['desaparecidos']:
            lines.append(f"| {item['repositorio']} | {'privado' if item['privado'] else 'público'} |")
    lines.extend(['', '## Nota metodológica', '', 'Las diferencias de tamaño de GitHub y de marcas de actualización pueden responder a indexación de plataforma, cambios de metadatos o actividad real. Las altas se registran como observación y no se incorporan automáticamente como submódulos hasta una revisión de seguridad y documentación.'])
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
