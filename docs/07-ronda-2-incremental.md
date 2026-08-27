# Ronda 2 — revisión incremental

> **Principio de conservación:** este documento añade evidencia y recomendaciones a la primera ronda. No sustituye ni elimina el inventario, informes, manifiestos o paquetes ya publicados.

## Resultado comparativo

La segunda consulta de GitHub identifica **67 repositorios propios accesibles**, frente a 65 en la línea base. No se registran bajas. Las dos incorporaciones observadas son el propio repositorio privado de control creado en la primera ronda y el nuevo repositorio privado `uaol-machine-realm`.

| Indicador | Línea base | Ronda 2 | Variación |
|---|---:|---:|---:|
| Repositorios propios accesibles | 65 | 67 | +2 |
| Públicos | 63 | 63 | 0 |
| Privados | 2 | 4 | +2 |
| Archivados | 2 | 2 | 0 |
| Repositorios ausentes de la línea base | 0 | 0 | 0 |
| Cambios de metadatos en repositorios existentes | — | 1 | Tamaño informado por GitHub |

Los datos estructurados de la comparación se conservan en [`data/ronda-2/comparacion.json`](../data/ronda-2/comparacion.json) y su vista legible en [`data/ronda-2/comparacion.md`](../data/ronda-2/comparacion.md). El inventario de la primera ronda sigue disponible sin modificación en [`data/catalogo_proyectos.json`](../data/catalogo_proyectos.json).

## Proyecto nuevo: UAOL–Máquina Realm

`uaol-machine-realm` se presenta como una plataforma persistente de operaciones con agentes y gemelo digital, basada en React, TypeScript, Vite, Express, tRPC, Drizzle, MySQL y un gateway local. La documentación declara explícitamente un límite importante: la versión auditada funciona sobre un **gemelo digital determinista** y no controla hardware, redes industriales, navegadores ni herramientas personales reales.[1]

| Área | Evidencia declarada | Lectura de segunda ronda |
|---|---|---|
| Límite operativo | No hay adaptador físico; los protocolos industriales se emulan sin abrir sockets industriales. | La separación entre simulación y operación física está documentada y debe mantenerse como bloqueo técnico, no solo como aviso de interfaz. |
| Seguridad de acceso | OAuth, sesiones, roles, auditoría, confirmaciones, rate limits y token de gateway hasheado. | Es una base razonable de diseño; requiere pruebas de autorización, registros revisables y una política de emisión/rotación de credenciales del gateway. |
| Resiliencia | Cola idempotente, arrendamiento, outbox local y reintentos. | Deben probarse condiciones de red, duplicación de órdenes, caducidad, revocación y recuperación antes de cualquier operación de mayor criticidad. |
| Documentación | Seis documentos operativos detectados, además de guía específica del gateway. | El proyecto está mejor preparado para madurar que un experimento sin documentación; conviene conservar una matriz de requisitos de producción. |
| Configuración | Solo se detectó `gateway-local/.env.gateway.example`; no hay `.env` real en el clon superficial. | No se identificó un archivo de entorno real para incluir o excluir. Los valores siguen sin inspeccionarse ni copiarse. |

> **Límite de seguridad:** ningún portal web, agente o gateway debe sustituir controles de seguridad funcional ni mecanismos independientes de parada de emergencia. La transición desde simulación requiere autorización operativa, segmentación de red, adaptadores específicos, pruebas en banco y aceptación documentada.[1]

## Cobertura de seguridad observada

La comprobación no invasiva del nuevo repositorio no encontró rutas con patrones convencionales de claves en los archivos analizados, pero no equivale a una certificación de ausencia de secretos. Los endpoints de GitHub devolvieron que Dependabot y Code Scanning no están habilitados; Secret Scanning no era accesible con el contexto de integración de esta revisión. Por tanto, se debe interpretar como **cobertura no disponible**, no como resultado limpio.

| Control | Estado observado | Acción incremental recomendada |
|---|---|---|
| Archivos de entorno reales | No detectados en el clon superficial. | Mantener solo ejemplos sin valores, bloquear `.env` mediante `.gitignore` y pre-commit. |
| Patrones convencionales de credenciales | Sin coincidencias de ruta en la revisión local. | Activar escaneos de proveedor y revisar alertas antes de publicar o conectar servicios. |
| Dependabot | Deshabilitado. | Activar grafo de dependencias, alertas y actualizaciones de seguridad.[2] |
| Code Scanning | Deshabilitado. | Definir análisis estático orientado a TypeScript/Node y revisar los resultados antes de despliegues. |
| Secret Scanning | No accesible mediante esta revisión. | Confirmar elegibilidad y alertas en la configuración de seguridad del repositorio; revisar el historial si se habilita.[3] |
| Workflows de GitHub Actions | No se detectaron workflows en el clon. | Cuando se añada CI, fijar permisos mínimos, validar dependencias y separar secretos por entorno. |

## Segunda verificación de presencia pública

La comprobación de cabeceras mantiene disponibles los puntos de entrada principales, aunque no elimina los hallazgos cualitativos anteriores.

| Punto | Resultado HTTP observado | Situación acumulada | Acción |
|---|---|---|---|
| `github.com/belentani7` | 200, HTML | Hub técnico accesible. | Mantener como entrada de evidencias técnicas y proyectos seleccionados. |
| `belentani.es` | 200, HTML | Sitio principal creativo accesible. | Enlazar de forma clara hacia los casos de IA y Trust & Safety. |
| `belentani.eu` | 200, HTML | Sigue respondiendo como dominio aparcado. | Redirigir, publicar o retirar del conjunto de enlaces oficiales. |
| Experiencia BuildAI | 200, HTML | Disponible a nivel HTTP; la primera revisión no obtuvo contenido útil renderizado. | Verificar el recorrido completo en un navegador de usuario y añadir monitorización. |
| `belentani.vercel.app` | 200, `application/javascript` | Persiste una respuesta de JavaScript, coherente con el hallazgo previo de contenido no presentado como portfolio. | Prioridad alta: revisar proyecto, artefacto, rutas, cabeceras y exposición de fuentes antes de promover el enlace. |

## Prioridades añadidas

| Prioridad | Acción nueva | Criterio de cierre |
|---|---|---|
| P0 | Incorporar `uaol-machine-realm` al registro del ecosistema como proyecto privado de simulación, no como controlador industrial. | Ficha de estado que especifique «gemelo digital», responsable, entornos y límites operativos. |
| P0 | Confirmar y habilitar una cobertura de alertas proporcional para UAOL: dependencias, análisis de código y secretos cuando la plataforma lo permita. | Panel de seguridad revisado, responsables asignados y evidencias de alertas/cierre. |
| P0 | Mantener el modo físico bloqueado hasta completar autorización, pruebas y aceptación fuera del entorno de simulación. | Matriz de requisitos firmada por responsables operativos y de seguridad; no basta con una declaración en README. |
| P1 | Añadir una prueba de humo de despliegue que falle si un portfolio responde como JavaScript o texto no renderizado. | Registro de despliegue con comprobación de ruta, tipo de contenido y señal visual o funcional. |
| P1 | Actualizar el portfolio canónico y corregir enlaces a dominios aparcados o demos degradadas. | Revisión manual de los enlaces del perfil y monitorización periódica. |

## Garantías de conservación

Esta ronda no modifica los repositorios fuente auditados, no rota credenciales, no cambia despliegues y no elimina archivos de las entregas anteriores. El nuevo informe, los datos de comparación y las referencias de UAOL se añaden mediante un commit nuevo; la entrega de Drive se publica como un paquete con nombre de ronda distinto, junto con su suma de verificación.

## Referencias

[1] [`uaol-machine-realm` — README](../sources/uaol-machine-realm/README.md)

[2] [GitHub Docs — Dependabot security updates](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-security-updates)

[3] [GitHub Docs — Secret scanning](https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning)
