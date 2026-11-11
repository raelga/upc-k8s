# Posgrado en Platform Engineering y DevOps con Kubernetes — edición 2026–2027

UPC School · Curso 305300 · Live online · Castellano · 12 ECTS.

**30 sesiones de 3 horas (90h)**, martes y jueves de 18:00 a 21:00, zona horaria **Europe/Madrid**. Inicio: **03/11/2026**. Fin: **18/03/2027**, con presentación y defensa del Trabajo Final. Las 29 clases de contenido terminan el **11/03/2027**; el desarrollo del proyecto es trabajo autónomo y el **16/03 no hay clase**.

[Syllabus detallado](syllabus-detallado.md) · [Calendario](calendario.md).

## Distribución

| Bloque | Sesiones | Horas | ECTS | Docencia |
|---|---|---:|---:|---|
| M1 · Fundamentos DevOps, Platform Engineering y Programación para Infraestructura | 1 (1) | 3h | 1.5 | René Serral<br>Rael Garcia |
| M2 · Cloud Computing Multicloud e Infraestructura como Código | 2–3 (2) | 6h | 1 | Rael Garcia |
| M3 · Contenedores y Kubernetes Core. Ecosistema OCI | 4–10 (7) | 21h | 2 | Rael Garcia |
| M4 · Kubernetes en Producción y Ecosistema Cloud Native | 11–13, 15–16 (5) | 15h | 2 | Rael Garcia |
| M5 · Observabilidad, GitOps, CI/CD y Networking Avanzado | 17–25 (9) | 27h | 2 | David Girón, Rael Garcia |
| M6 · Platform Engineering Avanzado: Operators, Serverless y Multi-Cluster | 14, 26–29 (5) | 15h | 2 | Rael Garcia, Marc Catrisse |
| PF · Trabajo Final | 30 (1) | 3h | 1.5 | René Serral<br>Rael Garcia |
| **Total** | **30** | **90h** | **12** | |

## Docencia

| Docente | Clases de contenido | Horas de contenido | Presentación TFG |
|---|---:|---:|---|
| René Serral | 1 | 3h | Sesión 30, junto a Rael Garcia (3h) |
| Rael Garcia | 19 | 57h | Sesión 30, junto a René Serral (3h) |
| David Girón | 6 | 18h | — |
| Marc Catrisse | 4 | 12h | — |

Las sesiones 1 y 30 son compartidas por René Serral y Rael Garcia. Cada una suma 3h al curso, aunque cuenta como 3h de participación para cada docente; las horas de participación docente no se suman para calcular las 90h del curso.

## Metodología y prerrequisitos

Dirigido a perfiles junior con conocimientos básicos de Linux, redes y scripting. Dos sesiones de contenedores preparan la ejecución de la aplicación en el entorno Academy validado antes de Kubernetes. AWS concentra el laboratorio guiado principal de IaC; Azure y GCP se trabajan mediante comparaciones y demostraciones preparadas, no mediante dos despliegues completos del alumnado. Se introducen identidad, redes, cómputo, almacenamiento y registros, y su aprovisionamiento como código. Python se practica en la validación de servicios y en proveedores; Bash en pipelines; Go en el ejemplo de operator. La IA apoya la escritura/adaptación de código, cuya ejecución y resultados se verifican.

Una aplicación Python de dos servicios conecta contenedores, Kubernetes, observabilidad, CI/GitOps, entrega y escalado. Laboratorios guiados con configuraciones preparadas; permisos, cuotas y costes comprobados; limpieza de recursos al finalizar. Se utiliza un clúster EKS preparado en networking y se comparan demostraciones preparadas de AKS y GKE. M6 combina conceptos, comparación y demostraciones; operators tiene una clase completa. Los secretos se entregan mediante mecanismos externos y no se guardan en repositorios ni en el estado de Terraform.

La sesión 1 incluye, dentro de sus 3h de M1 y con docencia compartida, una presentación guiada de AWS Academy y del ciclo de trabajo del laboratorio asignado, sin asumir un tipo concreto de laboratorio. Se requiere invitación y acceso al curso; el docente comprueba previamente el entorno real, sus permisos, cuotas y límites. Se distinguen contenidos del curso y entorno de laboratorio, acceso temporal a la consola, estado del laboratorio y operaciones de inicio, parada y finalización disponibles; persistencia y limpieza se rigen por sus instrucciones, sin garantías universales de conservación ni de gasto. Al finalizar la sesión 1, o como prerrequisito antes de la 4, el docente valida el entorno Academy para contenedores: runtime disponible o instalado cuando esté permitido, acceso al registro y restricciones del laboratorio. Las sesiones 4–5 se ejecutan en ese entorno preparado, no en un entorno local independiente. Las sesiones 2–3 de cloud e IaC preceden a ambas sesiones de contenedores.

**Primeras sesiones:** El 05/11 se practica el estado de Terraform y EC2 en AWS Academy. El 10/11 se sigue la [evolución de WordPress](https://github.com/raelga/kubernetes-talks/tree/main/course/infra/labs/aws/02-wordpress): MariaDB local, RDS, módulos, estados independientes, Auto Scaling, AMI versionadas y archivos multimedia en S3.

## Costes y control del consumo cloud

AWS reserva 15–20 minutos en la sesión 2 para facturación, filtros, presupuestos/alertas y limpieza. Las sesiones 11 y 12 dedican respectivamente 15–20 minutos a Azure Cost Management y GCP Cloud Billing; se explican el retraso de la facturación y que los presupuestos no detienen el gasto.

En AKS y GKE se retoma el coste de control plane, nodos, balanceadores, discos y tráfico.

## M1 · Formación transversal y créditos

M1 combina **3h propias y 6h integradas**: 9h de contenido incluidas en las 90h del curso. Los 1,5 ECTS incluyen además trabajo autónomo evaluable de adaptación de scripts entre proveedores, validaciones y modificación del ejemplo de Go.

| Sesión | Contenido transversal M1 | Horas incluidas |
|---|---|---:|
| 1 · Fundamentos de DevOps y Platform Engineering | DevOps, SRE y Platform Engineering; SLI/SLO/SLA e introducción a Terraform | 3h |
| 2 · AWS: fundamentos y aprovisionamiento como código | Python para consultar recursos; generación y revisión de código con IA | 1h |
| 3 · AWS WordPress: de EC2 con estado a instancias reemplazables | Adaptación de scripts, configuración y comparación entre proveedores | 1h |
| 5 · Contenedores II: redes, volúmenes, Compose y diagnóstico | Validación Python de los servicios y revisión de código con IA | 1h |
| 14 · Desarrollo de operators: Go y Kubebuilder/Operator SDK | Go aplicado y lectura/modificación del controlador | 1,5h |
| 17 · Automatización de pipelines: scripting, Tekton y Trivy | Bash/Python, errores, validaciones y ejecución automatizada | 1,5h |

Las horas compartidas no se suman de nuevo al total. La docencia corresponde al profesor de cada clase.

## Sesiones

| # | Bloque | Sesión | Docente |
|---:|---|---|---|
| 1 | M1 | Fundamentos de DevOps y Platform Engineering | René Serral<br>Rael Garcia |
| 2 | M2 + M1 | AWS: fundamentos y aprovisionamiento como código | Rael Garcia |
| 3 | M2 + M1 | AWS WordPress: de EC2 con estado a instancias reemplazables | Rael Garcia |
| 4 | M3 | Contenedores I: imágenes, ejecución y registros | Rael Garcia |
| 5 | M3 + M1 | Contenedores II: redes, volúmenes, Compose y diagnóstico | Rael Garcia |
| 6 | M3 | Arquitectura de Kubernetes: API, autenticación y permisos | Rael Garcia |
| 7 | M3 | Aplicaciones en Kubernetes: workloads, configuración y recursos | Rael Garcia |
| 8 | M3 | Persistencia en Kubernetes: almacenamiento y aplicaciones con estado | Rael Garcia |
| 9 | M3 | Networking en Kubernetes: comunicación y exposición de servicios | Rael Garcia |
| 10 | M3 | Construcción de un clúster Kubernetes componente a componente | Rael Garcia |
| 11 | M4 | Kubernetes en Azure: AKS | Rael Garcia |
| 12 | M4 | Kubernetes en GCP: GKE | Rael Garcia |
| 13 | M4 | Configuración y empaquetado de aplicaciones: Kustomize y Helm | Rael Garcia |
| 14 | M6 + M1 | Desarrollo de operators: Go y Kubebuilder/Operator SDK | Rael Garcia |
| 15 | M4 | Infraestructura declarativa: DNS, certificados y recursos cloud | Rael Garcia |
| 16 | M4 | Gestión de secretos externos: Vault y External Secrets Operator | Rael Garcia |
| 17 | M5 + M1 | Automatización de pipelines: scripting, Tekton y Trivy | Rael Garcia |
| 18 | M5 | Colaboración y validación de cambios: Git y Prow | Rael Garcia |
| 19 | M5 | Despliegue declarativo y reconciliación: GitOps con ArgoCD | Rael Garcia |
| 20 | M5 | Métricas y alertas: Prometheus, PromQL y Alertmanager | David Girón |
| 21 | M5 | Dashboards y logs: Grafana, Loki y Alloy | David Girón |
| 22 | M5 | Trazas distribuidas y correlación: OpenTelemetry y Tempo | David Girón |
| 23 | M5 | Entrada de tráfico y service mesh: Traefik e Istio | David Girón |
| 24 | M5 | Entrega progresiva: canary y blue/green con Argo Rollouts | David Girón |
| 25 | M5 | Escalado de aplicaciones y nodos: HPA, VPA, KEDA y Karpenter | David Girón |
| 26 | M6 | Políticas de admisión y recuperación: OPA/Gatekeeper y Velero | Marc Catrisse |
| 27 | M6 | Gestión de clústeres: Cluster API y Hosted Control Planes | Marc Catrisse |
| 28 | M6 | Serverless en Kubernetes: Knative y Virtual Kubelet | Marc Catrisse |
| 29 | M6 | Conectividad multi-cluster: Istio, Cilium Cluster Mesh y Submariner | Marc Catrisse |
| 30 | PF | Presentación y defensa del Trabajo Final | René Serral<br>Rael Garcia |

## Trabajo Final

Construcción progresiva de una plataforma a partir de las prácticas: IaC en un proveedor, aplicación Kubernetes, Helm/Kustomize, CI con escaneo, ArgoCD, DNS/TLS, secretos externos, métricas/logs/trazas, seguridad y escalado.

**Entregables:** repositorio reproducible, memoria de arquitectura y decisiones técnicas, runbooks, demo funcional con diagnóstico/recuperación y defensa oral. La evaluación considera funcionalidad, reproducibilidad, seguridad, observabilidad, justificación de decisiones, costes, documentación y defensa. Las ampliaciones avanzadas no son obligatorias.

**Presentación y defensa:** sesión 30, **18/03/2027, 18:00–21:00**, con **René Serral y Rael Garcia**, incluida en las 90h. Desarrollo y consolidación mediante trabajo autónomo durante el curso. La última clase de contenido es el 11/03 y el 16/03 queda libre para finalizar el proyecto.

La sesión de operators de M6 se imparte después de Kustomize y Helm; el resto de M6 continúa al final del programa.
