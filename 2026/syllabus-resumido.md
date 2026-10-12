# Posgrado en Platform Engineering y DevOps con Kubernetes — edición 2026–2027

UPC School · Curso 305300 · Live online · Castellano.

**Versión de trabajo consolidada con los acuerdos del curso.** 30 sesiones lectivas de 3 horas (90h), martes y jueves de 18:00 a 21:00, zona horaria **Europe/Madrid**. Ventana del curso: 03/11/2026–18/03/2027. El Proyecto Final tiene actividades propias fuera de las 30 sesiones y 90 horas, conforme al criterio acordado. Se conservan como referencia los 12 ECTS publicados, incluido PF; no se recalculan proporcionalmente con este reparto interno.

Referencia oficial: https://upcschool.upc.edu/esp/estudis/formacio/curs/305300/platform-engineering-devops-kubernetes/. El contenido oficial se ha contrastado con la transcripción aportada por el usuario; no se dispone de una descarga verificada de la página.

M6 sigue provisional, con enfoque de visión general y demostraciones; docente UPC por confirmar. La asignación Traefik/Istio completa corresponde a David. René y Rael son las denominaciones docentes acordadas; no se inventan nombres completos para David ni para el profesor UPC.

Enlaces: [syllabus detallado](syllabus-detallado.md) · [calendario](calendario.md).

## Distribución

| Bloque | Sesiones | Horas lectivas | ECTS publicados | Docencia |
|---|---:|---:|---:|---|
| M1 · Fundamentos DevOps, Platform Engineering y Programación para Infraestructura | 1–1 (1) | 3h | 1.5 | René |
| M2 · Cloud Computing Multicloud e Infraestructura como Código | 2–4 (3) | 9h | 1 | Rael |
| M3 · Contenedores y Kubernetes Core. Ecosistema OCI | 5–11 (7) | 21h | 2 | Rael |
| M4 · Kubernetes en Producción y Ecosistema Cloud Native | 12–16 (5) | 15h | 2 | Rael |
| M5 · Observabilidad, GitOps, CI/CD y Networking Avanzado | 17–25 (9) | 27h | 2 | David, Rael |
| M6 · Platform Engineering Avanzado: Operators, Serverless y Multi-Cluster | 26–30 (5) | 15h | 2 | Profesor UPC — por confirmar |
| PF · Proyecto Final | Fuera de las 30 | Fuera de las 90h; referencia publicada 6h | 1.5 | Por confirmar |
| **Total lectivo** | **30** | **90h** | **12 ECTS, incluido PF** | |

## Carga docente

| Docente | Sesiones lectivas | Horas |
|---|---:|---:|
| René | 1 | 3h |
| Rael | 18 | 54h |
| David | 6 | 18h |
| Profesor UPC — por confirmar | 5 | 15h |

Tutoría, consolidación y defensa del Proyecto Final no están asignadas todavía.

## Enfoque docente y prerrequisitos

Perfil junior: Linux, redes y scripting básicos según el contexto del repositorio; requisitos de acceso oficiales pendientes de verificar. No se exige experiencia cloud previa en esta planificación. Una misma aplicación Python con dos servicios conecta cloud, Kubernetes, observabilidad, CI y GitOps. Bash se practica en Tekton; Python aparece progresivamente en proveedores y automatización; Go se usa para comprender el operator. La IA ayuda a escribir/adaptar código que debe revisarse y verificarse.

Laboratorios guiados con manifiestos/configuraciones preparados. Antes de clase se comprueban cuentas, permisos, cuotas, dominios y costes. Se preservan estados reutilizables; para despliegues lentos, especialmente EKS/kOps, se explican conceptos durante la espera y se dispone de un entorno alternativo preparado. Cada práctica cloud incluye limpieza. Secretos y credenciales no se guardan en repositorios, logs ni estado Terraform; crear el contenedor del secreto no implica cargar su valor mediante IaC.

Semáforo: 🟢 alcance cómodo; 🟡 ajustado con material preparado. No mide dificultad de la herramienta ni garantiza tiempo de despliegue. Las amarillas de M6 suponen demostraciones, no implementaciones completas.

## Sesiones

| # | Bloque | Sesión | Docente | Carga |
|---:|---|---|---|:---:|
| 1 | M1 | DevOps y Platform Engineering | René | 🟢 |
| 2 | M2 | AWS, Terraform y Python | Rael | 🟡 |
| 3 | M2 | Azure, Terraform y automatización Python | Rael | 🟡 |
| 4 | M2 | GCP, estado remoto y comparación de IaC | Rael | 🟡 |
| 5 | M3 | Contenedores y ecosistema OCI | Rael | 🟡 |
| 6 | M3 | Arquitectura, API, kind, autenticación y RBAC | Rael | 🟡 |
| 7 | M3 | Workloads, configuración y recursos | Rael | 🟡 |
| 8 | M3 | Persistencia, CSI y StatefulSets | Rael | 🟡 |
| 9 | M3 | Networking y exposición de aplicaciones | Rael | 🟡 |
| 10 | M3 | Clúster componente a componente | Rael | 🟡 |
| 11 | M3 | Seguridad de imágenes y políticas de admisión | Rael | 🟡 |
| 12 | M4 | EKS y kOps en AWS | Rael | 🟡 |
| 13 | M4 | AKS y GKE | Rael | 🟡 |
| 14 | M4 | Kustomize y Helm | Rael | 🟡 |
| 15 | M4 | DNS y HTTPS con Cloudflare, ExternalDNS y cert-manager | Rael | 🟢 |
| 16 | M4 | Secretos externos: Vault y External Secrets Operator | Rael | 🟡 |
| 17 | M5 | Prometheus, PromQL y Alertmanager | David | 🟡 |
| 18 | M5 | Grafana, Loki y Alloy | David | 🟡 |
| 19 | M5 | OpenTelemetry, Collector, Tempo y correlación | David | 🟡 |
| 20 | M5 | Scripting y pipelines con Tekton | Rael | 🟡 |
| 21 | M5 | Git y Prow: colaboración y validaciones | Rael | 🟡 |
| 22 | M5 | GitOps con ArgoCD | Rael | 🟡 |
| 23 | M5 | Traefik e Istio | David | 🟡 |
| 24 | M5 | Entrega progresiva con Argo Rollouts | David | 🟡 |
| 25 | M5 | Escalado con HPA, VPA, KEDA y Karpenter | David | 🟡 |
| 26 | M6 | Operators con Go y Kubebuilder/Operator SDK | Profesor UPC — por confirmar | 🟡 |
| 27 | M6 | Cluster API y Hosted Control Planes | Profesor UPC — por confirmar | 🟡 |
| 28 | M6 | Knative y serverless | Profesor UPC — por confirmar | 🟢 |
| 29 | M6 | Multi-cluster: Istio, Cilium y Submariner | Profesor UPC — por confirmar | 🟡 |
| 30 | M6 | Crossplane y recuperación con Velero | Profesor UPC — por confirmar | 🟡 |

## Proyecto Final — fuera del cómputo lectivo

Construcción incremental de una plataforma con el material de las prácticas; no se empieza desde cero al acabar las clases. Infraestructura IaC en un proveedor, aplicación en Kubernetes, configuración Helm/Kustomize, CI, ArgoCD, DNS/TLS, secretos externos, observabilidad, seguridad, entrega progresiva y escalado.

Entregables propuestos, basados en el roadmap previo: repositorio reproducible, memoria de arquitectura/decisiones y runbooks, demo end-to-end con fallo/diagnóstico/recuperación y defensa oral. Firmas/SBOM y multi-cluster no se convierten en requisitos obligatorios si se tratan solo como extras o demostraciones.

Criterios para cerrar con el equipo docente: funcionalidad, reproducibilidad, seguridad, observabilidad, justificación de decisiones, limpieza/costes, documentación y defensa. No se fijan pesos nuevos ni tamaño de equipos. Tutoría/tribunal pendientes de asignación.

Actividades propuestas: **09/03/2027 consolidación** y **11/03/2027 presentación/defensa**, 18:00–21:00; no cuentan como sesiones 31/32 ni añaden horas al total lectivo. Fechas de PF por confirmar según organización y número de equipos. 16/03 y 18/03 quedan como reserva/recuperación.

## Cobertura oficial y decisiones pendientes

Este reparto conserva las tecnologías nombradas oficialmente, pero cuatro alcances requieren cierre docente; no se consideran extras prescindibles:

- **Git avanzado:** sesión 21. Se ha acordado práctica de colaboración básica; decidir qué parte avanzada (por ejemplo rebase, conflictos o protección de ramas) cubrir sin volver a un catálogo de operaciones.
- **Testing y CI/CD de Terraform:** vincular ejemplos de M2 con sesión 20; concretar las comprobaciones y el tiempo, sin afirmar que el pipeline de imágenes ya cubre IaC.
- **Cloudflare CDN:** DNS/ExternalDNS/ACME se cubren en sesión 15; falta concretar el ejemplo o explicación de CDN.
- **OIDC:** introducción en sesión 6 y contexto de identidad cloud; configuración práctica y profundidad pendientes.

Admission controllers sí tienen espacio en sesión 11. Vault y ESO permanecen explícitos en sesión 16; Secrets Manager es alternativa, no sustitución. Crossplane se concentra en sesión 30 con referencia desde M4. Mimir se introduce en sesión 17. Alloy se conserva por decisión expresa; no se incluye Snyk. OCM y Rancher no forman parte del reparto actual. La distribución de M6 y su profesor UPC requieren confirmación; las fechas reflejan la propuesta actual y no disponibilidad individual verificada.

