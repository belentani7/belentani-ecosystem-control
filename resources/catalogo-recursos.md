# Biblioteca curada de recursos

> Esta selección no pretende ser exhaustiva: se priorizaron recursos primarios y mantenidos que responden a las tecnologías y riesgos observados en el inventario. Cada adopción debe evaluarse por proyecto y licencia.

| Área | Recurso | Uso previsto |
|---|---|---|
| Seguridad de secretos | [GitHub Secret Scanning](https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning) | Detectar, investigar y remediar exposición de credenciales, incluidos hallazgos históricos. |
| Seguridad de secretos | [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) | Definir inventario, propietario, mínimo privilegio, rotación, revocación y expiración de secretos. |
| Cadena de suministro | [Dependabot security updates](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-security-updates) | Recibir actualizaciones de seguridad para dependencias vulnerables una vez activados el grafo y las alertas. |
| Cadena de suministro | [OpenSSF Scorecard](https://openssf.org/projects/scorecard/) | Evaluar controles de seguridad y riesgos de proyectos abiertos y dependencias críticas. |
| Cadena de suministro | [SLSA](https://slsa.dev/) | Madurar procedencia de builds, integridad de artefactos y controles de cadena de suministro. |
| Seguridad de CI/CD | [OWASP GitHub Actions Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GitHub_Actions_Security_Cheat_Sheet.html) | Revisar permisos, fijación de acciones por SHA, secretos y entradas no confiables en workflows. |
| IA responsable | [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | Estructurar la gestión de riesgos de sistemas de IA con una referencia institucional. |
| IA responsable | [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) | Revisar riesgos específicos de aplicaciones con modelos de lenguaje y agentes. |
| Accesibilidad | [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Usar criterios de accesibilidad verificables para experiencias web y creativas. |
| Pruebas web | [Playwright](https://playwright.dev/) | Añadir pruebas de recorrido crítico y comprobación de despliegues antes de anunciar enlaces públicos. |
| Frontend | [React documentation](https://react.dev/) | Referencia primaria para los proyectos React identificados. |
| Frontend | [Next.js documentation](https://nextjs.org/docs) | Referencia primaria para las aplicaciones Next.js identificadas. |
| Frontend | [Vite documentation](https://vite.dev/guide/) | Referencia primaria para los proyectos Vite identificados. |
| Diseño de interfaz | [Tailwind CSS documentation](https://tailwindcss.com/docs) | Referencia primaria para la capa de estilos repetida en el inventario. |
| Operaciones | [GitHub repository templates](https://docs.github.com/repositories/creating-and-managing-repositories/creating-a-template-repository) | Estandarizar arranque de proyectos, estructura, documentación y políticas comunes. |
| Limpieza de historial | [GitHub: Removing sensitive data from a repository](https://docs.github.com/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) | Planificar, solo después de rotar secretos, una limpieza coordinada de historial si es necesaria. |

## Criterio de incorporación

Los recursos se registran como **referencias**, no como copias de código de terceros. Antes de adoptar un repositorio externo, se debe revisar la licencia, el mantenimiento, las dependencias y el encaje con la arquitectura. OpenSSF Scorecard está diseñado precisamente para ayudar a evaluar riesgos de proyectos de código abierto y sus dependencias.[4]

## Referencias

[3] [GitHub Docs — Secret scanning](https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning)

[4] [OpenSSF — Scorecard](https://openssf.org/projects/scorecard/)

[5] [GitHub Docs — Dependabot security updates](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-security-updates)

[6] [OWASP — Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
