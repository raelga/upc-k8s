# Posgrado en Platform Engineering y DevOps con Kubernetes — edición 2026–2027

UPC School · Curso 305300 · Live online · Castellano · 12 ECTS.

El programa se desarrolla en **30 sesiones lectivas de 3 horas (90h)**, los martes y jueves de 18:00 a 21:00, en la zona horaria **Europe/Madrid**. El curso comienza el 03/11/2026 y finaliza el 18/03/2027. El Proyecto Final cuenta con actividades de consolidación y defensa adicionales a las 90 horas lectivas.

Enlaces: [syllabus detallado](syllabus-detallado.md) · [calendario](calendario.md).

## Distribución

| Bloque | Sesiones | Horas lectivas | ECTS | Docencia |
|---|---:|---:|---:|---|
| M1 · Fundamentos DevOps, Platform Engineering y Programación para Infraestructura | 1 (1) | 3h | 1.5 | René |
| M2 · Cloud Computing Multicloud e Infraestructura como Código | 2–4 (3) | 9h | 1 | Rael |
| M3 · Contenedores y Kubernetes Core. Ecosistema OCI | 5–11 (7) | 21h | 2 | Rael |
| M4 · Kubernetes en Producción y Ecosistema Cloud Native | 12–16 (5) | 15h | 2 | Rael |
| M5 · Observabilidad, GitOps, CI/CD y Networking Avanzado | 17–25 (9) | 27h | 2 | David, Rael |
| M6 · Platform Engineering Avanzado: Operators, Serverless y Multi-Cluster | 26–30 (5) | 15h | 2 | Profesor UPC |
| PF · Proyecto Final | Fuera de las 30 | 6h adicionales | 1.5 | — |
| **Total lectivo** | **30** | **90h** | **12 ECTS, incluido PF** | |

## Carga docente

| Docente | Sesiones lectivas | Horas |
|---|---:|---:|
| René | 1 | 3h |
| Rael | 18 | 54h |
| David | 6 | 18h |
| Profesor UPC | 5 | 15h |

## Enfoque docente y prerrequisitos

Dirigido a perfiles junior con conocimientos básicos de Linux, redes y scripting. Las sesiones de proveedores introducen los fundamentos cloud. Una misma aplicación Python con dos servicios conecta cloud, Kubernetes, observabilidad, CI y GitOps. Bash se practica en Tekton; Python aparece progresivamente en proveedores y automatización; Go se usa para comprender el operator. La IA ayuda a escribir/adaptar código que debe revisarse y verificarse.

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
| 26 | M6 | Operators con Go y Kubebuilder/Operator SDK | Profesor UPC | 🟡 |
| 27 | M6 | Cluster API y Hosted Control Planes | Profesor UPC | 🟡 |
| 28 | M6 | Knative y serverless | Profesor UPC | 🟢 |
| 29 | M6 | Multi-cluster: Istio, Cilium y Submariner | Profesor UPC | 🟡 |
| 30 | M6 | Crossplane y recuperación con Velero | Profesor UPC | 🟡 |

## Proyecto Final

El proyecto integra progresivamente los resultados de las prácticas: infraestructura IaC en un proveedor, aplicación en Kubernetes, configuración con Helm/Kustomize, CI, ArgoCD, DNS/TLS, secretos externos, observabilidad, seguridad, entrega progresiva y escalado.

**Entregables:** repositorio reproducible, memoria de arquitectura y decisiones técnicas, runbooks, demostración end-to-end con un escenario de fallo, diagnóstico y recuperación, y defensa oral.

**Evaluación:** funcionalidad, reproducibilidad, seguridad, observabilidad, justificación de decisiones, control de costes, documentación y defensa. Las tecnologías tratadas como ampliación, como firmas/SBOM y configuraciones multi-cluster avanzadas, son opcionales en el proyecto.

**Consolidación:** 09/03/2027, 18:00–21:00. **Presentación y defensa:** 11/03/2027, 18:00–21:00. Ambas actividades se realizan fuera de las 30 sesiones lectivas. El 16/03 y el 18/03 se reservan para recuperación.
