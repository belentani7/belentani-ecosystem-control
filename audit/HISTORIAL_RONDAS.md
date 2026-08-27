# Historial de rondas de auditoría

> Registro acumulativo. Cada ronda añade archivos y commits nuevos; las entregas anteriores se mantienen como evidencia histórica.

| Ronda | Fecha | Alcance | Entregables añadidos | Conservación |
|---|---|---|---|---|
| 1 | 2026-08-27 | Inventario de repositorios, análisis técnico, presencia pública, seguridad y recursos. | Informes `01` a `06`, inventario estructurado, manifiesto de fuentes, biblioteca de recursos y paquete inicial. | Línea base preservada en el commit `6705476`. |
| 2 | 2026-08-27 | Comparación incremental, detección del proyecto privado `uaol-machine-realm`, revisión de cobertura de seguridad y comprobación HTTP de puntos públicos. | Informe `07`, carpeta `data/ronda-2/`, referencia de fuente UAOL, estado de segunda ronda y paquete versionado. | Añadición exclusiva; no se reemplazan archivos de la Ronda 1. |

## Regla para rondas futuras

Toda ronda posterior debe partir de la rama `main` actualizada, crear una carpeta o informe con identificador de ronda, conservar los archivos anteriores, verificar que el diff no contenga eliminaciones y publicar un paquete nuevo en Drive en lugar de reemplazar los paquetes ya cargados.
