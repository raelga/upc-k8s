# Posgrado en Platform Engineering y DevOps con Kubernetes — edición 2026–2027

UPC School · Curso 305300 · Live online · Castellano · 12 ECTS.

**30 sesiones de 3 horas (90h)**, martes y jueves de 18:00 a 21:00, zona horaria **Europe/Madrid**. Inicio: **03/11/2026**. Fin: **18/03/2027**, con presentación y defensa del Trabajo Final. Las 29 clases de contenido terminan el **11/03/2027**; el desarrollo del proyecto es trabajo autónomo y el **16/03 no hay clase**.

[Syllabus detallado](syllabus-detallado.md) · [Calendario](calendario.md).

## Distribución

| Bloque | Sesiones | Horas | ECTS | Docencia |
|---|---|---:|---:|---|
| M1 · Fundamentos DevOps, Platform Engineering y Programación para Infraestructura | 1 (1) | 3h | 1.5 | René Serral |
| M2 · Cloud Computing Multicloud e Infraestructura como Código | 2–4 (3) | 9h | 1 | Rael Garcia |
| M3 · Contenedores y Kubernetes Core. Ecosistema OCI | 5–10 (6) | 18h | 2 | Rael Garcia |
| M4 · Kubernetes en Producción y Ecosistema Cloud Native | 11–15 (5) | 15h | 2 | Rael Garcia |
| M5 · Observabilidad, GitOps, CI/CD y Networking Avanzado | 16–24 (9) | 27h | 2 | David Girón, Rael Garcia |
| M6 · Platform Engineering Avanzado: Operators, Serverless y Multi-Cluster | 25–29 (5) | 15h | 2 | Marc Catrisse |
| PF · Trabajo Final | 30 (1) | 3h | 1.5 | René Serral y Rael Garcia |
| **Total** | **30** | **90h** | **12** | |

## Docencia

| Docente | Clases de contenido | Horas de contenido | Presentación TFG |
|---|---:|---:|---|
| René Serral | 1 | 3h | Sesión 30, junto a Rael Garcia (3h) |
| Rael Garcia | 17 | 51h | Sesión 30, junto a René Serral (3h) |
| David Girón | 6 | 18h | — |
| Marc Catrisse | 5 | 15h | — |

La sesión conjunta del TFG suma 3h al curso, aunque cuenta como 3h de participación para cada uno de sus dos docentes.

## Metodología y prerrequisitos

Dirigido a perfiles junior con conocimientos básicos de Linux, redes y scripting. Las clases cloud introducen los recursos que se utilizarán para desplegar Kubernetes: identidad, instancias, redes, balanceadores y almacenamiento, seguidos de su aprovisionamiento como código. Python se practica progresivamente en proveedores; Bash en pipelines; Go en el ejemplo de operator. La IA apoya la escritura/adaptación de código, cuya ejecución y resultados se verifican.

Una aplicación Python de dos servicios conecta Kubernetes, observabilidad, CI/GitOps, entrega y escalado. Laboratorios guiados con configuraciones preparadas; permisos, cuotas y costes comprobados; limpieza de recursos al finalizar. EKS/kOps se explican durante su despliegue con un entorno de respaldo disponible. M6 combina conceptos, comparación y demostraciones; operators tiene una clase completa. Los secretos se entregan mediante mecanismos externos y no se guardan en repositorios ni en el estado de Terraform.

## M1 · Formación transversal y créditos

M1 combina **3h propias y 6h integradas**: 9h de contenido incluidas en las 90h del curso. Los 1,5 ECTS incluyen además trabajo autónomo evaluable de adaptación de scripts entre proveedores, validaciones y modificación del ejemplo de Go.

| Sesión | Contenido transversal M1 | Horas incluidas |
|---|---|---:|
| 1 · Fundamentos de DevOps y Platform Engineering | Fundamentos DevOps, cultura, plataformas y métricas | 3h |
| 2 · AWS: fundamentos y aprovisionamiento como código | Python para consultar recursos; generación y revisión de código con IA | 1h |
| 3 · Azure: fundamentos y aprovisionamiento como código | Adaptación de scripts, configuración y tratamiento de resultados | 1h |
| 4 · GCP: fundamentos y aprovisionamiento como código | Reutilización de la automatización y comparación de implementaciones | 1h |
| 19 · Automatización de pipelines: scripting, Tekton y Trivy | Bash/Python, errores, validaciones y ejecución automatizada | 1,5h |
| 25 · Desarrollo de operators: Go y Kubebuilder/Operator SDK | Go aplicado y lectura/modificación del controlador | 1,5h |

Las horas compartidas no se suman de nuevo al total. La docencia corresponde al profesor de cada clase.

## Sesiones

| # | Bloque | Sesión | Docente |
|---:|---|---|---|
| 1 | M1 | Fundamentos de DevOps y Platform Engineering | René Serral |
| 2 | M2 + M1 | AWS: fundamentos y aprovisionamiento como código | Rael Garcia |
| 3 | M2 + M1 | Azure: fundamentos y aprovisionamiento como código | Rael Garcia |
| 4 | M2 + M1 | GCP: fundamentos y aprovisionamiento como código | Rael Garcia |
| 5 | M3 | Contenedores y ecosistema OCI: imágenes, runtimes y registros | Rael Garcia |
| 6 | M3 | Arquitectura de Kubernetes: API, autenticación y permisos | Rael Garcia |
| 7 | M3 | Aplicaciones en Kubernetes: workloads, configuración y recursos | Rael Garcia |
| 8 | M3 | Persistencia en Kubernetes: almacenamiento y aplicaciones con estado | Rael Garcia |
| 9 | M3 | Networking en Kubernetes: comunicación y exposición de servicios | Rael Garcia |
| 10 | M3 | Construcción de un clúster Kubernetes componente a componente | Rael Garcia |
| 11 | M4 | Kubernetes en AWS: EKS y clústeres autogestionados con kOps | Rael Garcia |
| 12 | M4 | Kubernetes en Azure y GCP: AKS y GKE | Rael Garcia |
| 13 | M4 | Configuración y empaquetado de aplicaciones: Kustomize y Helm | Rael Garcia |
| 14 | M4 | Infraestructura declarativa: DNS, certificados y recursos cloud | Rael Garcia |
| 15 | M4 | Gestión de secretos externos: Vault y External Secrets Operator | Rael Garcia |
| 16 | M5 | Métricas y alertas: Prometheus, PromQL y Alertmanager | David Girón |
| 17 | M5 | Dashboards y logs: Grafana, Loki y Alloy | David Girón |
| 18 | M5 | Trazas distribuidas y correlación: OpenTelemetry y Tempo | David Girón |
| 19 | M5 + M1 | Automatización de pipelines: scripting, Tekton y Trivy | Rael Garcia |
| 20 | M5 | Colaboración y validación de cambios: Git y Prow | Rael Garcia |
| 21 | M5 | Despliegue declarativo y reconciliación: GitOps con ArgoCD | Rael Garcia |
| 22 | M5 | Entrada de tráfico y service mesh: Traefik e Istio | David Girón |
| 23 | M5 | Entrega progresiva: canary y blue/green con Argo Rollouts | David Girón |
| 24 | M5 | Escalado de aplicaciones y nodos: HPA, VPA, KEDA y Karpenter | David Girón |
| 25 | M6 + M1 | Desarrollo de operators: Go y Kubebuilder/Operator SDK | Marc Catrisse |
| 26 | M6 | Políticas de admisión y recuperación: OPA/Gatekeeper y Velero | Marc Catrisse |
| 27 | M6 | Gestión de clústeres: Cluster API y Hosted Control Planes | Marc Catrisse |
| 28 | M6 | Serverless en Kubernetes: Knative y Virtual Kubelet | Marc Catrisse |
| 29 | M6 | Conectividad multi-cluster: Istio, Cilium Cluster Mesh y Submariner | Marc Catrisse |
| 30 | PF | Presentación y defensa del Trabajo Final | René Serral y Rael Garcia |

## Trabajo Final

Construcción progresiva de una plataforma a partir de las prácticas: IaC en un proveedor, aplicación Kubernetes, Helm/Kustomize, CI con escaneo, ArgoCD, DNS/TLS, secretos externos, métricas/logs/trazas, seguridad y escalado.

**Entregables:** repositorio reproducible, memoria de arquitectura y decisiones técnicas, runbooks, demo funcional con diagnóstico/recuperación y defensa oral. La evaluación considera funcionalidad, reproducibilidad, seguridad, observabilidad, justificación de decisiones, costes, documentación y defensa. Las ampliaciones avanzadas no son obligatorias.

**Presentación y defensa:** sesión 30, **18/03/2027, 18:00–21:00**, con **René Serral y Rael Garcia**, incluida en las 90h. Desarrollo y consolidación mediante trabajo autónomo durante el curso. La última clase de contenido es el 11/03 y el 16/03 queda libre para finalizar el proyecto.
