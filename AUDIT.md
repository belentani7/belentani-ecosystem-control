# Informe de Auditoría: belentani-ecosystem-control

Fecha: 2026-08-27
Stack detectado: Repositorio de gobernanza/inventario (Markdown, Python, shell, GitHub Actions)
Commits analizados: 1 (08a5421)
Veredicto: sano

## Lo mejor del repo (mínimo 3)

1. **Filosofía de conservación impecable.** El repositorio documenta explícitamente que cada ronda incremental añade archivos sin reemplazar los anteriores (`audit/HISTORIAL_RONDAS.md`), lo que preserva la evidencia histórica y evita pérdida de datos.
2. **Política de secretos disciplinada y bien ejecutada.** No hay `.env`, `.pem`, `.key` ni credenciales versionadas. La regla "documentar variables por propósito, no por valor" (`docs/03-plan-seguridad.md`) se respeta en todo el repo, y los repositorios con `.env` detectados quedan excluidos deliberadamente de los submódulos.
3. **Organización clara y navegable.** Mapa de contenidos en `README.md`, manifiesto de entrega, CSV/JSON coherentes (66 filas = 65 repos + cabecera), separación limpia entre docs, data, resources, scripts y sources, y un pipeline CI mínimo (`validate.yml`) que valida el inventario.

Complemento: la trazabilidad es excelente — 60 submódulos con commit auditado fijado en `.gitmodules`, referencias por URL en `sources/repositorios.csv`, y un script reproducible (`clone-sources.sh`) que clona selectivamente.

## Hallazgos CRÍTICOS (archivo:línea)

Ninguno. No se detectaron secretos reales versionados, RCE, inyección SQL, ni bugs que rompan build. El código presente (`scripts/analizar_ronda_2.py`) es sintácticamente válido y la lógica de comparación de inventarios es correcta.

## Hallazgos ALTOS

Ninguno. No hay funcionalidad rota ni dependencias con CVE conocidos (no se gestiona ningún paquete de aplicación).

## Hallazgos MEDIOS

- `data/ronda-2/uaol_alertas_codigo.json`, `uaol_alertas_dependencias.json`, `uaol_alertas_secretos.json`: contienen códigos de escape ANSI (salida coloreada de `gh`/curl) y, por tanto, **no son JSON válido** a pesar de llevar extensión `.json`. `json.load()` falla en los tres. Es un problema de calidad de datos, no de seguridad (el contenido es un mensaje de error de API, sin secretos). **No modificado**: estos archivos son artefactos de evidencia de la Ronda 2 y la filosofía del repo es preservar la evidencia tal cual. Se recomienda regenerarlos con `--no-color` o docinarlas como `.txt` en rondas futuras.

## Hallazgos BAJOS

- El CI (`validate.yml`) solo valida `data/catalogo_proyectos.json`; los `.json` de `data/ronda-2/` quedan fuera de la validación automatizada, lo que impidió detectar el problema ANSI. Ampliar la validación a `data/**/*.json` detectaría regresiones.

## Añadido por el auditor

- `AUDIT.md` (este informe).

## Próximos pasos recomendados

1. Regenerar los tres `uaol_alertas_*.json` sin color ANSI (o renombrarlos) para que el inventario de seguridad sea parseable por herramientas automáticas.
2. Ampliar el workflow de validación a todos los JSON de `data/` (por ejemplo `python3 -m json.tool data/ronda-2/*.json`) para capturar este tipo de regresión.
3. Avanzar los P0 del plan de seguridad (rotación/revocación de los `.env` versionados y revisión de `belentani.vercel.app`), que ya están correctamente documentados en `docs/03-plan-seguridad.md`.

## No tocado (pero anotado)

- Los 60 submódulos referenciados permanecen sin inicializar en el clon (estado `-` en `git submodule status`); es el comportamiento esperado de un repo de control y no requirió acción.
- No se modificó ningún archivo de evidencia de la Ronda 1 ni de la Ronda 2.
