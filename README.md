# Belentani Ecosystem Control

> Repositorio privado de inventario, gobernanza, priorización y acceso reproducible a proyectos del ecosistema Belentani/NOIACORE. Generado el 2026-08-27T05:07:59+00:00.

El objetivo es convertir una cartera heterogénea de proyectos web, IA, Trust & Safety y tecnología creativa en un sistema navegable. El repositorio contiene análisis, planes de trabajo, referencias a recursos y submódulos Git; no aloja copias masivas de los repositorios originales ni archivos de entorno.

## Mapa de contenidos

| Ruta | Contenido |
|---|---|
| [`docs/01-informe-ejecutivo.md`](docs/01-informe-ejecutivo.md) | Lectura estratégica, presencia pública y prioridades. |
| [`docs/02-inventario-proyectos.md`](docs/02-inventario-proyectos.md) | Catálogo de los 65 repositorios propios analizados. |
| [`docs/03-plan-seguridad.md`](docs/03-plan-seguridad.md) | Acciones prioritarias de secretos, despliegues y cadena de suministro. |
| [`docs/04-gobernanza-y-organizacion.md`](docs/04-gobernanza-y-organizacion.md) | Estructura operativa, decisiones y flujos de trabajo. |
| [`docs/05-presencia-online.md`](docs/05-presencia-online.md) | Auditoría de los puntos públicos verificables. |
| [`docs/06-tramites-y-operacion.md`](docs/06-tramites-y-operacion.md) | Listas de comprobación de dominio, marca, derechos, privacidad y publicación. |
| [`sources/`](sources/README.md) | Manifiesto y submódulos de los repositorios fuente. |
| [`resources/`](resources/catalogo-recursos.md) | Biblioteca curada de recursos primarios. |
| [`data/`](data/README.md) | Exportaciones estructuradas de inventario. |

## Resultado de la auditoría

| Indicador | Resultado |
|---|---:|
| Repositorios propios inventariados | 65 |
| Públicos / privados | 63 / 2 |
| Repositorios con README | 50 |
| Repositorios con GitHub Actions detectado | 40 |
| Contribuciones visibles en 12 meses | 686 |
| Submódulos incluidos | 59 |
| Repositorios retenidos por revisión de seguridad | 3 |

## Regla de seguridad

> **No incorporar secretos, archivos `.env` reales, claves privadas, tokens ni backups de credenciales.** Las configuraciones se documentan por nombre de variable y propósito; los valores permanecen en un gestor de secretos o en el entorno de ejecución.

## Recuperar fuentes

El repositorio puede clonarse con submódulos. Para obtener únicamente las fuentes aprobadas en una carpeta independiente, use `scripts/clone-sources.sh`. Las fuentes con configuraciones de entorno versionadas quedan excluidas hasta su revisión de seguridad.

## Límites

Este repositorio no sustituye controles de acceso, auditorías de código en profundidad, asesoramiento jurídico, ni la rotación real de credenciales. Tampoco atribuye presencia a perfiles externos cuando no fue posible verificar su titularidad o contenido público.

## Segunda ronda incremental

La **Ronda 2** se conserva como una adición versionada, sin reemplazar los entregables anteriores. El informe, datos de comparación y estados de verificación se encuentran en [`docs/07-ronda-2-incremental.md`](docs/07-ronda-2-incremental.md) y [`data/ronda-2/`](data/ronda-2/) Esta ronda incorpora la detección y evaluación inicial de `uaol-machine-realm`, registrada como plataforma privada de simulación operacional con límites explícitos frente al control físico.

| Entrega incremental | Ubicación |
|---|---|
| Informe de segunda ronda | [`docs/07-ronda-2-incremental.md`](docs/07-ronda-2-incremental.md) |
| Comparación de inventarios | [`data/ronda-2/comparacion.md`](data/ronda-2/comparacion.md) |
| Estados HTTP de puntos públicos | [`data/ronda-2/estado_puntos_publicos.txt`](data/ronda-2/estado_puntos_publicos.txt) |
| Referencia de UAOL | [`sources/uaol-machine-realm`](sources/uaol-machine-realm) |
