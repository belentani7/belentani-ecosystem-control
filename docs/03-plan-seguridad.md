# Plan de seguridad y continuidad

## Hallazgo de prioridad alta

La revisión de nombres de archivos detectó tres archivos `.env` **versionados** en repositorios públicos: `duck-lab`, `tender-words-connect` y `abrazo-tender-words`. La auditoría no revela sus valores ni afirma que cada variable sea una credencial activa. Sin embargo, por el tipo de configuración detectada —conexiones de base de datos, servicios de terceros y claves de publicación— deben tratarse como exposición potencial hasta completar su verificación.

> GitHub indica que el análisis de secretos examina el historial Git completo y las ramas, y recomienda rotar una credencial cuando se detecta una filtración.[3]

| Fase | Acción segura | Propietario sugerido | Evidencia de cierre |
|---|---|---|---|
| 0. Contención | No copiar los tres repositorios como submódulos ni volver a distribuir sus `.env`. Registrar las variables por propósito, no por valor. | Responsable técnico | Manifiesto actualizado y ningún archivo de entorno incluido en el repositorio de control. |
| 1. Triage | Identificar qué variables corresponden a servicios activos, caducados, de prueba o vacíos. Revisar registros de acceso cuando el proveedor lo permita. | Responsable de cada servicio | Inventario de secretos con estado, propietario y fecha de revisión. |
| 2. Rotación/revocación | Rotar o revocar las credenciales activas; actualizar secretos del entorno de despliegue y confirmar funcionamiento. | Responsable técnico y de plataforma | Prueba de producción controlada con nuevas credenciales. |
| 3. Prevención | Eliminar `.env` de seguimiento, conservar solo `.env.example` sin valores reales, activar reglas de pre-commit y políticas de CI. | Mantenedores | Pull request con pruebas y política documentada. |
| 4. Historial | Evaluar limpieza de historial **solo después** de rotar. Coordinar fuerzas, clones y despliegues para evitar reintroducción. | Responsable Git | Registro de procedimiento y verificación posterior de escaneo. |

## Controles transversales

| Control | Aplicación | Justificación |
|---|---|---|
| Secret scanning | Verificar alertas de los repositorios públicos y habilitar la cobertura disponible. | GitHub informa que el escaneo cubre credenciales codificadas en ramas e historial.[3] |
| Dependabot | Activar grafo de dependencias, alertas y actualizaciones de seguridad en los proyectos con paquetes. | Reduce el tiempo de reacción ante vulnerabilidades de dependencias.[5] |
| Scorecard | Ejecutar evaluación de los repositorios públicos prioritarios antes de promoverlos como productos de referencia. | Ofrece comprobaciones automatizadas para riesgos de proyectos y dependencias abiertos.[4] |
| Permisos de Actions | Usar `permissions: read-all` como punto de partida y elevar permisos por trabajo con justificación documentada; fijar acciones externas por SHA cuando el riesgo lo requiera. | Reduce la superficie de CI/CD y favorece trazabilidad. |
| Despliegues | Añadir smoke tests de URL, comprobación de tipo de contenido y ruta de rollback antes de actualizar perfiles/enlaces. | Evita publicar páginas aparcadas, experiencias en blanco o artefactos de desarrollo. |
| Backups | Cifrar, limitar acceso y probar restauración de respaldos que contengan configuración o datos sensibles. | OWASP recomienda gobernar el ciclo de vida y verificar procedimientos de copia/restauración.[6] |

## Protección de la presencia pública

El comportamiento observado en `belentani.vercel.app` se debe investigar de forma prioritaria. Confirmar el proyecto Vercel asociado, el comando de build, el directorio de salida, el routing, el contenido de la respuesta y cualquier configuración que pueda publicar fuentes o artefactos erróneos. Hasta su corrección, no debe ser el enlace principal de perfil.

## Referencias

[3] [GitHub Docs — Secret scanning](https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning)

[4] [OpenSSF — Scorecard](https://openssf.org/projects/scorecard/)

[5] [GitHub Docs — Dependabot security updates](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-security-updates)

[6] [OWASP — Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
