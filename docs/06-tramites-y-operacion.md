# Listas de comprobación operativas

> Estas listas son de gestión y no constituyen asesoramiento jurídico, fiscal, laboral ni de protección de datos. Para decisiones vinculantes, debe revisarlas un profesional competente en la jurisdicción aplicable.

## Dominio y publicación

| Paso | Evidencia a conservar | Estado inicial |
|---|---|---|
| Definir dominio canónico por marca/producto. | Decisión registrada y mapa de redirecciones. | Pendiente de consolidación. |
| Configurar redirecciones 301 desde dominios alternativos o retirar enlaces no activos. | Prueba de respuesta HTTP y fecha de verificación. | `belentani.eu` requiere decisión. |
| Verificar TLS, cabeceras básicas, robots y mapa del sitio. | Captura de configuración y comprobación automatizada. | Pendiente. |
| Probar las rutas públicas antes de anunciarlas. | Registro de smoke test y responsable. | Recomendado para BuildAI/Vercel. |

## Derechos, marca y activos creativos

| Paso | Evidencia a conservar |
|---|---|
| Inventariar nombre, logotipos, música, visuales, textos, modelos, prompts y software por obra/proyecto. | Registro de activos con titularidad, licencia, fecha y ubicación. |
| Distinguir activos propios, de clientes, con licencia comercial y de código abierto. | Matriz de derechos y restricciones de publicación. |
| Documentar contribuciones de colaboradores y permisos de uso de imagen/voz cuando aplique. | Contratos, autorizaciones o términos aceptados. |
| Añadir licencia explícita a cada repositorio y un aviso de terceros cuando sea necesario. | Archivo `LICENSE` y `NOTICE` revisados. |

## Datos y servicios

| Paso | Evidencia a conservar |
|---|---|
| Identificar qué proyectos procesan datos personales, analítica, pagos o cuentas de usuario. | Registro de tratamiento por proyecto. |
| Documentar proveedores, regiones, roles de acceso y periodos de retención. | Inventario de proveedores y evaluación proporcional. |
| Preparar textos de privacidad, cookies, términos y contacto de soporte antes de publicar servicios que los requieran. | Versionado de políticas y fecha de entrada en vigor. |
| Separar entornos de desarrollo, prueba y producción; revocar accesos al cerrar un proyecto. | Matriz de acceso y registro de baja. |

## Operación de software

Antes de declarar un proyecto «production-ready», debe existir una descripción de servicio, responsable, soporte, procedimiento de rollback, gestión de secretos, copias/restauración probadas, monitorización proporcional y un proceso de reporte de vulnerabilidades.
