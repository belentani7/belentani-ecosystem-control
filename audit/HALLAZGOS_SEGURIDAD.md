# Hallazgos de seguridad y tratamiento

| Hallazgo | Severidad orientativa | Tratamiento en este repositorio | Siguiente decisión |
|---|---|---|---|
| `.env` versionados en tres repositorios públicos. | Alta hasta validar vigencia y alcance. | No se copian ni referencian como submódulos; solo se registra el estado sin valores. | Triage, rotación/revocación si procede, prevención y evaluación de limpieza de historial. |
| Posibles patrones de credenciales en documentación o código. | Informativa / requiere triage. | No se han transcrito valores; las coincidencias en documentación de terceros no se interpretan como secreto activo. | Revisar alertas y escaneos del proveedor, centrando la investigación en rutas propias. |
| Portfolio Vercel no renderizado y con texto/código visible. | Alta de configuración/exposición potencial. | Se documenta como observación; no se copian fragmentos de respuesta. | Revisar despliegue, build, routing, cabeceras y secretos de plataforma. |
