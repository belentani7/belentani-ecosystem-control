# Fuentes y submódulos

Este repositorio unifica los proyectos mediante **referencias Git reproducibles**, no copiando sus árboles de código ni historial dentro de un monorepo artificial. El enfoque evita duplicación, mantiene la trazabilidad hacia el origen y permite clonar cada fuente de forma selectiva.

| Estado | Cantidad | Tratamiento |
|---|---:|---|
| Submódulos referenciados | 59 | Están registrados en `.gitmodules` con el commit auditado. Para descargarlos: `git submodule update --init --recursive`. |
| Pendientes de revisión de seguridad | 3 | Permanecen en el manifiesto, sin submódulo, porque se detectó un `.env` versionado. No deben incorporarse hasta revisar, revocar/rotar lo necesario y definir la corrección de historial. |

## Política de fuentes externas

Los enlaces a repositorios o herramientas de terceros se conservan en `../resources/catalogo-recursos.md` como referencias. No se vendorizan ni se clonan automáticamente: antes de incorporar código externo se deben comprobar licencia, mantenimiento, seguridad, compatibilidad y necesidad real.

## Uso

```bash
git clone --recurse-submodules <URL_DEL_REPOSITORIO_DE_CONTROL>
cd belentani-ecosystem-control
# Para inicializar módulos pendientes después de un clon sin --recurse-submodules:
git submodule update --init --recursive
```

> Los repositorios marcados como `pendiente_revision_seguridad` se han excluido deliberadamente de los submódulos para no propagar configuraciones potencialmente sensibles.
