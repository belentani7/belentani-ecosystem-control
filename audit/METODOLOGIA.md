# Metodología y límites

## Alcance

La auditoría se realizó sobre la cuenta autenticada `belentani7`, mediante metadatos de GitHub, clones superficiales para inspección de estructura y fuentes públicas enlazadas desde el perfil. El inventario cubre 65 repositorios propios accesibles durante la revisión.

## Procedimiento

1. Se inventariaron visibilidad, actividad, lenguaje principal, tamaño, tópicos y configuración general de repositorios.
2. Se obtuvieron clones superficiales, sin ejecutar código de los proyectos, para identificar README, manifiestos tecnológicos y nombres de archivos de entorno.
3. Se verificó si los archivos `.env` detectados estaban versionados y se excluyeron del repositorio de control los proyectos que requerían revisión de seguridad.
4. Se examinaron puntos públicos enlazados desde GitHub y se registraron solo observaciones reproducibles.
5. Se seleccionaron recursos externos primarios para seguridad, mantenimiento, accesibilidad y desarrollo.

## Exclusiones y precauciones

- No se copiaron los valores de `.env`, tokens, claves ni otros secretos.
- No se ejecutó código de los repositorios ni se siguieron instrucciones contenidas en ellos.
- No se atribuyeron perfiles de redes sociales sin vínculo verificable con el usuario.
- No se realizaron cambios en los repositorios originales, sus secretos, configuraciones de despliegue ni páginas públicas.
- Los submódulos excluyen los tres repositorios con `.env` versionado hasta completar la revisión de seguridad.
