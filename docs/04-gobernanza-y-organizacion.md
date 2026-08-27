# Gobernanza y organización del ecosistema

## Principio operativo

La organización debe separar **identidad y narrativa**, **productos activos**, **investigación/experimentos** y **archivos o backups**, evitando que el nombre de un repositorio sea la única fuente de estado. Cada proyecto debe tener un único dueño operativo, un objetivo de publicación y una decisión explícita: mantener, consolidar, archivar o retirar.

| Nivel | Propósito | Cadencia | Artefacto mínimo |
|---|---|---|---|
| Ecosistema | Priorizar líneas de trabajo y coherencia pública. | Mensual | Portfolio roadmap y mapa de enlaces. |
| Producto | Decidir objetivo, público, métricas y estado de entrega. | Quincenal | Ficha de producto y tablero de prioridades. |
| Repositorio | Mantener calidad técnica, documentación, licencias y seguridad. | Por pull request / mensual | README, SECURITY, licencia, cambios y CI. |
| Experimento | Aprender sin promesa de producción. | Al cierre del experimento | Hipótesis, resultado, decisión de promover o archivar. |

## Convenciones recomendadas

| Elemento | Convención |
|---|---|
| Estado | `active`, `incubating`, `maintenance`, `archived`, `superseded`. |
| README | Propósito, audiencia, estado, demo, stack, inicio, seguridad/datos, licencia, contacto y siguientes pasos. |
| Repositorios de backup | Mantenerlos privados o etiquetados explícitamente como históricos; no presentarlos como producto actual. |
| Demos | URL canónica, fecha de verificación, responsable y prueba de humo. |
| Dependencias | Gestor y lockfile definidos; actualizaciones revisadas por riesgo y no por volumen. |
| Decisiones | Documentos breves en `docs/decisions/ADR-XXXX.md` para decisiones de arquitectura o producto que afecten a varias líneas. |

## Flujo de promoción

```text
Idea o experimento
  -> ficha mínima + hipótesis
  -> revisión de seguridad, licencia y viabilidad
  -> repositorio activo con plantilla común
  -> demo y pruebas de despliegue
  -> inclusión en portfolio y proyectos fijados
  -> mantenimiento, consolidación o archivo
```

## Selección de proyectos para el escaparate

Se recomienda limitar el escaparate principal a seis proyectos, uno o dos por dominio estratégico. El criterio debe equilibrar utilidad demostrable, estabilidad de despliegue, claridad de documentación, diferenciación y seguridad. Los demás repositorios pueden seguir siendo públicos o accesibles, pero deben residir en colecciones temáticas, no competir por ser portada.
