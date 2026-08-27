# Informe ejecutivo de ecosistema

## Síntesis

La auditoría inventarió **65 repositorios propios** de la cuenta `belentani7`: 63 públicos y 2 privados. Se identificó una cartera activa, con **686 contribuciones visibles** en los últimos doce meses consultados y una concentración tecnológica en React, Next.js, Vite, Tailwind CSS y GitHub Actions. El perfil comunica con claridad la unión entre sistemas de IA, Trust & Safety, desarrollo full-stack y tecnología creativa.[1]

La señal estratégica dominante es un ecosistema deliberadamente multidisciplinar: productos y experiencias web, automatización/agentes, validación y evidencia, y obra creativa/audiovisual. La oportunidad no consiste en crear más repositorios independientes, sino en explicitar una arquitectura de portfolio, estándares compartidos y rutas de publicación que conecten esas líneas.

| Dimensión | Evidencia observada | Lectura |
|---|---|---|
| Base técnica | React (28), Next.js (24), Vite (22) y Tailwind (27) aparecen de forma recurrente. | Es viable definir una plantilla técnica transversal y reducir divergencia operativa. |
| Entrega y automatización | GitHub Actions aparece en 40 repositorios. | La superficie de CI/CD es significativa; conviene homogeneizar permisos, secretos y validaciones. |
| Documentación | 50 repositorios contienen README. | Existe una buena base, pero quedan proyectos que necesitan una ficha mínima para ser navegables y mantenibles. |
| Proyectos de alto potencial | OmniAgent aborda enrutamiento de tareas de IA; ProofMesh propone auditoría evidence-first; Duck Unified presenta una suite de creación, gestión y análisis. | Son pilares diferenciables que deberían recibir casos de estudio, demo verificable y hoja de ruta explícita. |

## Arquitectura de portfolio propuesta

| Dominio | Función | Proyectos representativos | Resultado público recomendado |
|---|---|---|---|
| **NOIACORE / IA y agentes** | Sistemas de IA, enrutamiento, herramientas y orquestación. | `omniagent`, `local-agent`, `llm-vfx-orchestrator`, `comfyui-json-compiler`. | Casos de uso, criterios de seguridad, límites y demostraciones reproducibles. |
| **Trust & Safety / evidencia** | Auditoría de cambios, trazabilidad y validación. | `proofmesh`, `oss-compass`, `evidence-ledger`, `pbr-validator`. | Método, evidencias, evaluación honesta de madurez y documentación técnica. |
| **Duck / Creative technology** | Experiencias visuales, música, audiovisual y herramientas de estudio. | `duck-unified-master`, `duck-studio-suite`, `duck-music-lab`, `Duck-Omega`. | Demos estables, galerías con contexto técnico y una ruta clara a cada producto. |
| **Humano / comunidad** | Proyectos de impacto, educación o experiencias personales. | `ManosAbiertas`, `Cruzando-el-charco`, `Belentani.cv-ai`, `entrenador-jorge-bcn`. | Objetivo, alcance, datos tratados, responsables y puntos de contacto. |
| **Identidad Belentani** | Portfolio, obra, narrativa y dirección creativa. | `Belentani`, `belentaniexperience`, `judas-experience`, `belentani7`. | Página puente entre oferta profesional de IA/T&S y universo creativo. |

## Presencia pública

La presencia verificada se distribuye entre GitHub, que opera como hub técnico y de enlaces, y `belentani.es`, que presenta una identidad artística y tecnológica distintiva.[1] [2] El perfil enlaza a un portfolio desplegado, dominios propios y una página profesional de LinkedIn. Sin embargo, la consistencia de enlace necesita atención: `belentani.eu` mostró una página de aparcamiento, la experiencia BuildAI no entregó contenido en la comprobación automatizada y `belentani.vercel.app` mostró texto/código en vez de un portfolio renderizado. Estas señales justifican una revisión de producción antes de concentrar tráfico hacia esos destinos.

## Prioridades

| Prioridad | Horizonte | Acción | Resultado esperado |
|---|---|---|---|
| P0 | Inmediata | Tratar los `.env` versionados como posibles exposiciones: inventariar, verificar vigencia, revocar/rotar cuando corresponda y bloquear nuevas inclusiones. | Se reducen los riesgos de credenciales reutilizadas y la propagación a nuevos repositorios. |
| P0 | Inmediata | Revisar `belentani.vercel.app`, el artefacto desplegado y las cabeceras; retirar/reestructurar el despliegue si publica código no previsto. | El portfolio vuelve a entregar una experiencia intencional y no expone detalles técnicos innecesarios. |
| P1 | 7 días | Definir el portfolio canónico y redirigir o retirar dominios/enlaces degradados. | Una ruta pública coherente desde GitHub a producto, portfolio y contacto. |
| P1 | 14 días | Establecer plantilla de repositorio y ficha mínima: propósito, estado, demo, seguridad, licencia, datos, contacto y próximos pasos. | La cartera queda navegable y seleccionable para clientes, colaboradores o comunidad. |
| P2 | 30 días | Activar una línea de seguridad y mantenimiento para repositorios priorizados: dependencias, workflows, pruebas de despliegue y Scorecard. | Señales objetivas de calidad y menor deuda de mantenimiento. |

## Referencias

[1] [Perfil público de GitHub de belentani7](https://github.com/belentani7)

[2] [Sitio oficial belentani.es](https://belentani.es/)

[3] [GitHub Docs — Secret scanning](https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning)

[4] [OpenSSF — Scorecard](https://openssf.org/projects/scorecard/)
