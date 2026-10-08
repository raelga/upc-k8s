# Roadmap Detallado — Posgrado en Platform Engineering y DevOps con Kubernetes

> **Versión in-depth** del programa publicado por la UPC (90h lectivas / 12 ECTS).
> Para la vista resumida (títulos, calendario y tecnologías) consulta
> [`roadmap-postgrado-kubernetes.md`](roadmap-postgrado-kubernetes.md).
> Este documento desarrolla, sesión a sesión, el temario, los laboratorios y la
> evaluación de los 6 módulos + Proyecto Final.
> Página publicada: https://upcschool.upc.edu/esp/estudis/formacio/curs/305300/postgrau-platform-engineering-devops-kubernetes/

## Ficha del programa

| Dato                | Detalle                                                        |
|---------------------|----------------------------------------------------------------|
| Titulación          | Diploma de experto en Platform Engineering y DevOps con Kubernetes (UPC) |
| Créditos            | 12 ECTS · 90h lectivas                                         |
| Modalidad           | Live online · Español                                          |
| Calendario          | 30 sesiones de 3h · Martes y jueves 18:00–21:00                |
| Fechas              | 03/11/2026 → 18/03/2027                                        |
| Dirección académica | Rael Garcia Arnes · René Serral Gracià                        |
| Perfil de entrada   | Profesionales IT con base en Linux, redes y scripting          |
| Perfil de egreso    | Platform Engineer · SRE · Kubernetes Architect                 |

**Cómo leer este documento.** Cada módulo abre con su **objetivo**, las **competencias de
entrada** y su ubicación en el calendario. Cada **sesión** (3h) incluye una tabla de temas,
un **🧪 laboratorio** guiado y una estimación de trabajo autónomo recomendado. Cada módulo
cierra con sus **criterios de evaluación** y **bibliografía**.

---

## Mapa de módulos y sesiones

| Módulo | ECTS | Horas | Sesiones | Fechas                    |
|--------|------|-------|----------|---------------------------|
| M1 · Fundamentos DevOps, PE y Programación | 1.5 | 6h  | 1–2 | 03/11/2026 → 05/11/2026 |
| M2 · Cloud Multicloud e IaC                | 1   | 9h | 3–5 | 10/11/2026 → 17/11/2026 |
| M3 · Contenedores y Kubernetes Core (OCI)  | 2   | 15h | 6–10 | 19/11/2026 → 03/12/2026 |
| M4 · Kubernetes en Producción y Cloud Native | 2 | 15h | 11–15 | 10/12/2026 → 07/01/2027 |
| M5 · Observabilidad, GitOps, CI/CD y Networking | 2 | 21h | 16–22 | 12/01/2027 → 02/02/2027 |
| M6 · Platform Engineering Avanzado         | 2   | 18h | 23–28 | 04/02/2027 → 25/02/2027 |
| PF · Proyecto Final                        | 1.5 | 6h  | 29–30 | 02/03/2027 → 04/03/2027 |
| **Total**                                  | **12** | **90h** | **30** | |

> **Rebalanceo interno (sin alterar ECTS oficiales ni el total de 90h/30 sesiones):**
> M1 pasa de 4 a 2 sesiones (Go se traslada a M6, justo antes de construir operators,
> aprendizaje just-in-time). Las 2 sesiones liberadas se reparten: +1 en M5 (se divide
> la observabilidad en 3 sesiones — métricas, logs, trazas+correlación — en vez de 2) y
> +1 en M6 (nueva sesión de Go). Además, M2 integra IaC en tres sesiones cloud y libera una sesión para separar ArgoCD de Prow/Tekton en M5. Los ECTS por módulo se mantienen como en la ficha
> oficial de la UPC; solo cambia la distribución interna de horas/sesiones.
>
> Festivos y no lectivos: **La Immaculada (8 dic 2026)** y **vacaciones de Navidad
> (24, 29 y 31 dic 2026, 5 ene 2027)**, más el **festivo UPC del 9 feb 2027**. Las fechas
> 9, 11, 16 y 18 de marzo de 2027 quedan como **reserva/recuperación**.

---

## M1 — Fundamentos DevOps, Platform Engineering y Programación para Infraestructura

**1.5 ECTS · 6h · Sesiones 1–2 · 03/11/2026 → 05/11/2026**

**Objetivo.** Situar el movimiento DevOps y su evolución hacia Platform Engineering, y dotar
al estudiante de las competencias de programación (Bash, Python) —potenciadas por
asistentes de IA— necesarias para automatizar infraestructura. *Go se introduce más adelante,
en la Sesión 23 (M6), en el contexto de construir un controlador de Kubernetes.*

**Competencias de entrada.** Manejo básico de línea de comandos Linux, nociones de
programación y de control de versiones.

### Sesión 1 — Fundamentos de DevOps y Platform Engineering (CALMS, IDP, Team Topologies, DORA) (Martes 03/11/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 1.1 | Historia y motivación | De Waterfall a Agile, de Agile a DevOps. Los muros entre Dev y Ops. Los tres caminos (The Phoenix Project). |
| 1.2 | Principios DevOps | CALMS: Culture, Automation, Lean, Measurement, Sharing. |
| 1.3 | Prácticas clave | CI/CD, Infrastructure as Code, Monitoring, Incident Management, Blameless Postmortems. |
| 1.4 | Platform Engineering | Internal Developer Platforms (IDP), golden paths, Developer Experience (DevEx). |
| 1.5 | Organización | SRE vs DevOps vs Platform Engineer. Team Topologies (stream-aligned, enabling, platform, complicated-subsystem). |
| 1.6 | Métricas | DORA (Deployment Frequency, Lead Time, MTTR, Change Failure Rate) y framework SPACE. Backstage como portal. |

**🧪 Lab.** Diseñar la propuesta de IDP para una empresa ficticia: identificar golden paths,
topología de equipos y métricas DORA objetivo. Entregable: diagrama + una página de decisiones.

*Trabajo autónomo sugerido: 2h (lectura The Phoenix Project / Team Topologies).*

### Sesión 2 — Bash y Python para DevOps, asistidos por IA (Jueves 05/11/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 2.1 | Programación asistida por IA | Copilots/asistentes para scripting, refactor y generación de tests. Buenas prácticas y revisión crítica (transversal a Bash y Python). |
| 2.2 | Bash | Variables, control de flujo, funciones, arrays, manejo de errores. grep/sed/awk/jq/yq. cron/systemd timers, Makefiles. |
| 2.3 | Python para DevOps | Tipos, entornos virtuales. SDKs cloud (boto3, google-cloud-*, azure-sdk). Manejo de APIs REST. |
| 2.4 | Python: datos y calidad | YAML/JSON/TOML, Jinja2. CLIs con Click/Typer. Testing con pytest, linting con ruff, type checking con mypy. |

**🧪 Lab.** Toolkit de automatización: scripts Bash (aprovisionamiento/validación de un entorno
local, con `make` targets) + una CLI Python que los orquesta e inventaría recursos cloud,
exportando a JSON/tabla, con tests `pytest`.

**Evaluación del módulo.** Entrega de los 2 labs (40%) + propuesta de IDP de la Sesión 1 como
mini-proyecto evaluable (60%). Se valora la calidad del código, la idempotencia y la claridad
de las decisiones.

**Bibliografía.** *The Phoenix Project* (Kim, Behr, Spafford) · *Team Topologies* (Skelton,
Pais) · *The DevOps Handbook* · docs oficiales de Bash y Python.

---

## M2 — Cloud Computing Multicloud e Infraestructura como Código

**1 ECTS · 9h · Sesiones 3–5 · 10/11/2026 → 17/11/2026**

**Objetivo.** Infraestructura cloud básica con Terraform/OpenTofu integrado en tres sesiones. AWS como caso principal; Azure y GCP como transferencia del mismo patrón, con ejemplos preparados. Identidad, redes, máquinas virtuales y almacenamiento. Comparación breve con Pulumi, sin laboratorio propio. Kubernetes gestionado y su aprovisionamiento se abordan en M4.

**Competencias de entrada.** M1; Linux, redes y scripting básicos. Cuentas de laboratorio con permisos y límites de coste definidos.

### Sesión 3 — AWS y fundamentos de Terraform/OpenTofu (Martes 10/11/2026)

- AWS: IAM, regiones y zonas, VPC, subredes, Security Groups, EC2 y S3; contexto de ECR
- Fundamentos IaC: declarativo, idempotencia y drift; Terraform/OpenTofu, HCL, provider y recursos
- Caso práctico común: red, máquina virtual y almacenamiento; init, plan, apply y destroy; permisos y control de costes

**🧪 Lab.** Aplicar el caso común de red, máquina virtual y almacenamiento, comprobar permisos y conectividad y destruir los recursos al terminar. En AWS se introduce el flujo; en Azure y GCP se parte de ejemplos preparados para comparar diferencias. No se despliega Kubernetes en este módulo.

### Sesión 4 — Azure e IaC: equivalencias y módulos (Jueves 12/11/2026)

- Azure: Entra ID, suscripciones, grupos de recursos, Managed Identities, VNet, NSG, máquinas virtuales y Blob Storage; contexto de ACR
- Transferencia del caso AWS a Azure con configuración preparada: equivalencias y diferencias
- Terraform/OpenTofu: variables, outputs y uso de módulos existentes; sin diseño avanzado de módulos propios

**🧪 Lab.** Aplicar el caso común de red, máquina virtual y almacenamiento, comprobar permisos y conectividad y destruir los recursos al terminar. En AWS se introduce el flujo; en Azure y GCP se parte de ejemplos preparados para comparar diferencias. No se despliega Kubernetes en este módulo.

### Sesión 5 — GCP e IaC: estado y comparativa multicloud (Martes 17/11/2026)

- GCP: proyectos, cuentas de servicio, IAM, VPC, firewall, Compute Engine y Cloud Storage; contexto de Artifact Registry
- Transferencia del mismo caso a GCP con configuración preparada; comparación de identidad, redes, permisos y portabilidad
- Terraform/OpenTofu: estado local y remoto, locking según backend y protección del estado y de las credenciales
- Pulumi: comparación de 10–15 minutos de HCL frente a Python/Go con un ejemplo equivalente pequeño; también requiere gestión de estado; sin instalación ni laboratorio propio

**🧪 Lab.** Aplicar el caso común de red, máquina virtual y almacenamiento, comprobar permisos y conectividad y destruir los recursos al terminar. En AWS se introduce el flujo; en Azure y GCP se parte de ejemplos preparados para comparar diferencias. No se despliega Kubernetes en este módulo.

**Evaluación del módulo.** Caso AWS reproducible y comparación razonada con Azure y GCP; se valora el uso de variables, outputs, módulos existentes, estado y limpieza de recursos. No se exige diseñar módulos propios ni dominar tres clouds.

**Bibliografía.** Documentación oficial de AWS, Azure, GCP, Terraform y OpenTofu; Pulumi como referencia comparativa.

---

## M3 — Contenedores y Kubernetes Core. Ecosistema OCI

**2 ECTS · 15h · Sesiones 6–10 · 19/11/2026 → 03/12/2026**

**Objetivo.** Dominar el ecosistema de contenedores (OCI) y la arquitectura de Kubernetes,
construyendo y operando sus objetos fundamentales, hasta levantar un clúster componente a
componente.

**Competencias de entrada.** M1–M2. Familiaridad con Linux (namespaces, procesos) y Docker básico.

### Sesión 6 — Contenedores y ecosistema OCI: imágenes, runtimes y seguridad (Jueves 19/11/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 6.1 | Arquitectura de contenedores | Linux namespaces, cgroups v2, UnionFS, modelo de capas OCI. |
| 6.2 | Build de imágenes | Dockerfile avanzado, multi-stage, BuildKit, cache, distroless/scratch, multi-platform. |
| 6.3 | Runtimes y registros | Docker, containerd, CRI-O, runc, gVisor, CRI. Docker Hub, GHCR, ECR/ACR/GAR, Harbor. |
| 6.4 | Seguridad de la cadena | CVE scanning (Trivy/Grype), firma (Cosign), SBOM. Builds in-cluster (kaniko, buildah). OCI Artifacts. |

**🧪 Lab.** Construir una imagen multi-stage distroless, escanearla con Trivy, firmarla con
Cosign y generar su SBOM; publicarla en un registro privado (Harbor/GHCR).

### Sesión 7 — Kubernetes: arquitectura, control plane y clusters locales (kind) (Martes 24/11/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 7.1 | Control plane | kube-apiserver, etcd, kube-scheduler, controller-manager, cloud-controller-manager. |
| 7.2 | Data plane | kubelet, kube-proxy, container runtime, comunicación entre nodos. |
| 7.3 | API y objetos | Modelo declarativo, API groups, CRUD con kubectl, dry-run, server-side apply. |
| 7.4 | Clusters locales | kind (Kubernetes in Docker): multi-nodo, port mappings, uso en CI. |

**🧪 Lab.** Levantar un clúster multi-nodo con kind, inspeccionar los componentes del control
plane y desplegar la imagen firmada del Lab 7.

### Sesión 8 — Building Blocks: workloads, configuración y scheduling (Jueves 26/11/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 8.1 | Pods y workloads | Ciclo de vida, init/sidecar/ephemeral containers. Deployment, StatefulSet, DaemonSet, Job, CronJob, ReplicaSet. |
| 8.2 | Configuración | ConfigMap, Secret (tipos, encriptación at rest), env vars, volúmenes. Reloader. |
| 8.3 | Organización | Namespaces, Labels, Selectors, Annotations, Finalizers, OwnerReferences. |
| 8.4 | Scheduling y recursos | Affinity/anti-affinity, taints/tolerations, topology spread, PriorityClasses. requests/limits, LimitRange, ResourceQuota, QoS, PDB. |

**🧪 Lab.** Desplegar una app multi-componente (Deployment + StatefulSet) con ConfigMaps,
Secrets, probes, requests/limits y reglas de scheduling; provocar un reschedule y observarlo.

### Sesión 9 — Almacenamiento y networking en Kubernetes (Martes 01/12/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 9.1 | Almacenamiento | PV, PVC, StorageClass, dynamic provisioning. CSI (EBS, Azure Disk, GCE PD), snapshots, cloning. |
| 9.2 | Services | ClusterIP, NodePort, LoadBalancer, ExternalName, Headless, EndpointSlices. |
| 9.3 | Ingress y Gateway API | Ingress controllers, IngressClass, Gateway API (HTTPRoute, GRPCRoute). |
| 9.4 | CNI y DNS | Calico, Cilium, Flannel. NetworkPolicy y microsegmentación. CoreDNS. |

**🧪 Lab.** Exponer la app del Lab 9 vía Ingress/Gateway API con almacenamiento persistente
(PVC) y aplicar NetworkPolicies de mínimo privilegio entre componentes.

### Sesión 10 — Autenticación, RBAC y clúster componente a componente (Jueves 03/12/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 10.1 | RBAC | ServiceAccounts, Roles, ClusterRoles, Bindings, mínimo privilegio. |
| 10.2 | Autenticación y admisión | X.509, OIDC, webhook auth, bound SA tokens. Admission controllers, OPA Gatekeeper, Kyverno, PSA. |
| 10.3 | Cluster desde cero (I) | etcd (operaciones, snapshots, TLS), kube-apiserver, scheduler, controller-manager: configuración manual y flags. |
| 10.4 | Cluster desde cero (II) | kubelet, containerd, kube-proxy, TLS bootstrapping. PKI con cfssl/openssl. kubeadm bajo el capó. Debugging. |

**🧪 Lab.** "Kubernetes the hard way" reducido: arrancar los componentes del control plane con
certificados propios y unir un nodo; validar con un Pod de prueba. Definir RBAC de mínimo
privilegio para un equipo.

**Evaluación del módulo.** Labs 6–10 (40%) + prueba práctica: desplegar y exponer de forma
segura una aplicación en Kubernetes partiendo de una imagen firmada (60%). Cobertura de CKAD/CKS.

**Bibliografía.** *Kubernetes in Action* (Lukša) · *Programming Kubernetes* (Hausenblas,
Schimanski) · Kubernetes docs · CKA/CKAD/CKS curricula (CNCF/Linux Foundation).

---

## M4 — Kubernetes en Producción y Ecosistema Cloud Native

**2 ECTS · 15h · Sesiones 11–15 · 10/12/2026 → 07/01/2027**

**Objetivo.** Operar Kubernetes gestionado en los grandes clouds y desplegar el ecosistema
cloud native imprescindible: application bundles, infraestructura declarativa y gestión de
secretos.

**Competencias de entrada.** M3. Acceso a al menos un cloud provider.

### Sesión 11 — Kubernetes gestionado: EKS, GKE y AKS (Jueves 10/12/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 11.1 | EKS | Node groups (managed/self-managed/Fargate), eksctl, IRSA/Pod Identity, add-ons (ALB Controller, EBS/EFS CSI, VPC CNI), KMS/audit. |
| 11.2 | GKE | Standard vs Autopilot, Workload Identity, VPC-native, Config Connector, GKE Gateway, Fleet. |
| 11.3 | AKS | Entra ID, Managed Identities, Azure CNI, Azure Monitor, CSI, AGIC, Azure Policy, Defender for Containers. |
| 11.4 | Comparativa | Feature matrix, managed vs self-managed, pricing y criterios de selección. |

**🧪 Lab.** Provisionar un clúster gestionado (EKS/GKE/AKS) con Terraform, habilitar Workload
Identity/IRSA y desplegar una app con un LoadBalancer/Ingress cloud-native.

### Sesión 12 — Otros entornos y aprovisionamiento IaC multi-cloud (Martes 15/12/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 12.1 | Otros clouds | OVHcloud, DigitalOcean DOKS, Linode LKE, Scaleway, Hetzner. |
| 12.2 | On-premises / edge | k3s, k0s, Rancher, Talos, OpenShift. |
| 12.3 | IaC de clústeres | Módulos Terraform para EKS/GKE/AKS; parametrización y entornos. |
| 12.4 | Día 2 | Upgrades, node pools, backups y consideraciones de coste. |

**🧪 Lab.** Levantar un clúster ligero (k3s/Talos) y compararlo operativamente con el
gestionado del Lab 12 (arranque, upgrades, add-ons).

### Sesión 13 — Application bundles: Kustomize, Helm y su ecosistema (Jueves 17/12/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 13.1 | Kustomize | Bases, overlays, patches, generators, transformers. 2 ejemplos prácticos (dev/prod). |
| 13.2 | Helm | Charts, templates, values, hooks. El catálogo de Helm (Artifact Hub) como ecosistema de distribución. |
| 13.3 | Helm + Kustomize | helm-secrets, helm-diff. Combinar Helm (render) con overlays Kustomize por entorno. |
| 13.4 | Caso real: charts que despliegan operators | Ejemplo con el chart de kube-prometheus-stack / Grafana Operator: un chart puede instalar un Operator + sus CRDs. *Se profundizará en el patrón Operator en la Sesión 24.* |

**Guion de sesión (180 min, enfocado a concepto → cómo se implementa):**

| Bloque | Tiempo | Formato | Contenido |
|---|---|---|---|
| 1. Kustomize | 35 min | Concepto (10') + demo en vivo (25') | Overlay = parche, no plantilla, sin templating. `base/` + `overlays/dev` y `overlays/prod` (patchesStrategicMerge o JSON6902), `kustomize build`, `kubectl apply -k`, un `configMapGenerator`. Mensaje clave: "YAML puro + parches, cero magia". |
| 2. Helm | 45 min | Concepto (10') + demo en vivo (35') | Empaquetar y distribuir con lógica (`if`, `range`) y versión. Estructura de un chart (`Chart.yaml`, `values.yaml`, `templates/`), `helm install`/`upgrade`/`template` (comparar el render con Kustomize), Artifact Hub como catálogo e instalar un chart real (p. ej. `bitnami/nginx`). Mensaje clave: "plantilla con lógica + versión + catálogo". |
| 3. Helm + Kustomize combinados | 25 min | Concepto (5') + demo (20') | Patrón de producción: chart de terceros sin tocar + Kustomize sobre su output. `helm template chart/ > rendered.yaml` + overlay de entorno. Mención breve (sin demo) de `helm-diff`/`helm-secrets`. |
| 4. Caso real: chart que instala un operator | 15 min | Demo pasiva (sin hands-on) | `helm install kube-prometheus-stack` y mostrar que instala CRDs + un controller. Cierre: "esto es un Operator; cómo se construye uno se ve en la Sesión 24". |
| 5. Lab guiado | 50 min | Hands-on con checkpoints | 0–15': chart básico funcionando en `dev`. 15–35': overlay `prod` con Kustomize sobre el render. 35–50': deploy en 2 namespaces + verificación + dudas. |

*10 min de buffer/preguntas repartidos entre bloques.*

**🧪 Lab.** Empaquetar la app del proyecto como Helm chart parametrizado con overlays Kustomize
por entorno (dev/prod) y desplegarla en dos namespaces.

### Sesión 14 — Infraestructura declarativa: ExternalDNS, cert-manager y Crossplane (Martes 22/12/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 14.1 | ExternalDNS | Providers (Route53, CloudDNS, Cloudflare), anotaciones, políticas de sync. |
| 14.2 | cert-manager | Issuers/ClusterIssuers, Let's Encrypt, ACME DNS-01/HTTP-01, renovación automática. |
| 14.3 | Crossplane | Providers, Managed Resources, Compositions, XRDs. Comparativa con Terraform. |
| 14.4 | Crossplane avanzado | Composition Functions, EnvironmentConfigs, integración con ArgoCD. |

**🧪 Lab.** Automatizar DNS + TLS de la app (ExternalDNS + cert-manager) y aprovisionar un
recurso cloud (p.ej. bucket) desde Kubernetes con Crossplane.

### Sesión 15 — Gestión de secretos: Vault y External Secrets Operator (Jueves 07/01/2027)

| # | Tema | Contenido |
|---|------|-----------|
| 15.1 | Vault: arquitectura | Server/agents, storage backends, HA, seal/unseal, auto-unseal con KMS. |
| 15.2 | Vault: auth y engines | Kubernetes Auth, JWT/OIDC, AppRole. KV v1/v2, Dynamic Secrets, PKI, Transit. Vault Agent, VSO. |
| 15.3 | External Secrets | ExternalSecret, SecretStore/ClusterSecretStore, providers (AWS SM, Azure KV, GCP SM, Vault), templating, pushSecret. |
| 15.4 | Otros patrones | Sealed Secrets, SOPS. Comparativa por madurez e integración con GitOps. |

**🧪 Lab.** Desplegar Vault en el clúster, configurar Kubernetes Auth y un secret dinámico, y
consumirlo desde la app mediante External Secrets Operator.

**Evaluación del módulo.** Labs 11–15 (40%) + entrega intermedia del Proyecto Final: clúster
gestionado con app empaquetada (Helm/Kustomize), DNS+TLS automáticos y secretos gestionados (60%).

**Bibliografía.** Docs de EKS/GKE/AKS · Helm & Kustomize docs · cert-manager/ExternalDNS/
Crossplane docs · HashiCorp Vault Associate curriculum · External Secrets Operator docs.

---

## M5 — Observabilidad, GitOps, CI/CD y Networking Avanzado

**2 ECTS · 21h · Sesiones 16–22 · 12/01/2027 → 02/02/2027**

**Objetivo.** Instrumentar la plataforma, introducir Git en el flujo GitOps con ArgoCD y automatizar validaciones con Prow/Tekton; gestionar tráfico y entrega progresiva.

**Competencias de entrada.** M3–M4; aplicación desplegable en Kubernetes. Git se introduce aquí con alcance básico.

### Sesión 16 — Observabilidad (I): Prometheus, PromQL y Alertmanager (Martes 12/01/2027)

- Los tres pilares: métricas, logs, trazas. Correlación entre señales
- Prometheus: arquitectura, scraping, PromQL, service discovery, Alertmanager
- Prometheus Operator: ServiceMonitor, PodMonitor, recording rules, alerting rules. Thanos para HA

**🧪 Lab.** Instrumentar la aplicación, desplegar kube-prometheus-stack, escribir consultas PromQL y una alerta.

### Sesión 17 — Observabilidad (II): Grafana y Loki (logs) (Jueves 14/01/2027)

- Grafana: datasources, dashboards, variables, alerting. Grafana as Code (grafonnet, Terraform)
- Loki: arquitectura, LogQL (mismo modelo mental que PromQL), labels vs indexación de texto completo
- Promtail: recolección de logs de los Pods y envío a Loki
- Grafana Explore: consulta y filtrado de logs por label en tiempo real

**🧪 Lab.** Recoger logs en Loki y consultarlos desde Grafana Explore.

### Sesión 18 — Observabilidad (III): OpenTelemetry, Tempo y correlación (Martes 19/01/2027)

- OpenTelemetry: especificación OTLP, SDK, auto-instrumentación de la app sin tocar código
- OpenTelemetry Collector: pipeline de receivers, processors y exporters
- Tempo: backend de trazas distribuidas, trace ID, spans, integración con Grafana
- Mimir: métricas a escala/federadas (mención breve, complementa la sesión de Prometheus)
- Correlación end-to-end: exemplars, salto métrica→traza→logs en un mismo dashboard

**🧪 Lab.** Instrumentar trazas con OpenTelemetry y Tempo y correlacionar métricas, trazas y logs.

### Sesión 19 — Git y GitOps con ArgoCD (Jueves 21/01/2027)

- Git para el repositorio de manifiestos: ramas, commits, PR, revisión y conflictos sencillos; sin Git avanzado
- Principios GitOps: declarativo, versionado, automatizado, reconciliado. Pull vs Push model
- ArgoCD: Applications, AppProjects, ApplicationSets, sync policies, waves, hooks y RBAC
- ArgoCD avanzado: multi-tenancy, SSO, App of Apps, ApplicationSet generators y notifications
- Práctica: modificar un manifiesto, revisar el PR, sincronizar con ArgoCD y observar la reconciliación

**🧪 Lab.** Modificar un manifiesto mediante PR y observar sincronización y reconciliación en ArgoCD.

### Sesión 20 — Pipelines CI/CD: Prow y Tekton (Martes 26/01/2027)

- Git aplicado a CI: cambios y PR como disparadores de validaciones y pipelines
- Prow: arquitectura CI nativa en Kubernetes, plugins, Tide, Deck dashboard y ProwJobs
- Tekton: Tasks, Pipelines, PipelineRuns, Workspaces, Triggers y Tekton Chains
- Integración Tekton + ArgoCD para workflows CI/CD end-to-end en Kubernetes

**🧪 Lab.** Validar un PR con Prow y ejecutar un pipeline Tekton build → test → scan que actualice el repositorio GitOps.

### Sesión 21 — Networking avanzado: Traefik e Istio (service mesh) (Jueves 28/01/2027)

- Traefik: IngressRoute CRDs, middlewares, TLS automático, dashboard y métricas
- Traefik avanzado: TCP/UDP routing, rate limiting, circuit breaker, canary con TraefikService
- Istio: arquitectura (Istiod + Envoy sidecars), mTLS automático y observabilidad integrada
- Istio traffic: VirtualServices, DestinationRules, Gateways, traffic shifting, fault injection
- Istio seguridad: AuthorizationPolicies, PeerAuthentication, circuit breaking, Kiali
- Ambient Mesh (Istio): modo sin sidecar, ztunnel, waypoints y migración

**🧪 Lab.** Habilitar mTLS, aplicar una AuthorizationPolicy y practicar traffic shifting con Istio.

### Sesión 22 — Entrega progresiva y escalado: Argo Rollouts, HPA/VPA, KEDA, Karpenter (Martes 02/02/2027)

- Estrategias: rolling update, blue/green, canary, A/B testing y trade-offs
- Argo Rollouts: canary con análisis automatizado, blue-green, integración Istio/Traefik + Prometheus
- Progressive delivery: Feature flags (Flagger/OpenFeature), métricas como gates, rollback automático
- HPA: métricas CPU/memory, custom metrics (Prometheus Adapter), scaling behavior
- VPA: modos (Off/Initial/Auto), recomendaciones y limitaciones
- KEDA: ScaledObject, ScaledJob, triggers (Kafka, SQS, Prometheus, cron) y cooldown
- Cluster Autoscaler vs Karpenter: node pools, scale-from-zero, cost optimization

**🧪 Lab.** Configurar un canary con Argo Rollouts, análisis de métricas y rollback; añadir HPA y KEDA.

**Evaluación del módulo.** Labs 16–22 (40%) + plataforma bajo GitOps con observabilidad, service mesh y entrega progresiva (60%).

**Bibliografía.** Documentación oficial de Prometheus, Grafana, OpenTelemetry, Git, ArgoCD, Prow, Tekton, Istio, Argo Rollouts y KEDA.

---

## M6 — Platform Engineering Avanzado: Operators, Serverless y Multi-Cluster

**2 ECTS · 18h · Sesiones 23–28 · 04/02/2027 → 25/02/2027**

**Objetivo.** Extender Kubernetes con operators propios y operar plataformas avanzadas:
gestión del ciclo de vida de clústeres, serverless, hosted control planes y arquitecturas
multi-cluster/multi-cloud con disaster recovery.

**Competencias de entrada.** M3–M5 y programación básica de M1; Go se introduce al inicio de M6.

### Sesión 23 — Go: de cero a controlador de Kubernetes (Jueves 04/02/2027)

- Fundamentos de Go: tipos, structs, interfaces, goroutines, channels, manejo de errores idiomático
- client-go: clientset, kubeconfig, serialización, listar/filtrar/crear recursos de la API
- controller-runtime: reconciliation loop, informers, predicates (fundamentos, sin construir el operator todavía)
- CLIs y tooling: cobra/viper, logging estructurado, go test, mocks con testify, golangci-lint

### Sesión 24 — Construcción de Operators con Kubebuilder/Operator SDK (Jueves 11/02/2027)

| # | Tema | Contenido |
|---|------|-----------|
| 24.1 | Diseño de API | CRD design, API versioning, status subresource, conditions. |
| 24.2 | Kubebuilder/Operator SDK | Scaffolding, controller-runtime, reconciliation loop, predicates, webhooks. |
| 24.3 | Finalizers y estado | Finalizers, owner references, gestión de errores y requeue. |
| 24.4 | Operators de producción | Leader election, métricas, testing con envtest, empaquetado con OLM. |

**🧪 Lab.** Construir un operator sencillo (p.ej. que reconcilie un recurso `Website`) con
kubebuilder, con status conditions, finalizer y tests envtest.

### Sesión 25 — Gestión de clústeres (Cluster API) y serverless (Knative) (Martes 16/02/2027)

| # | Tema | Contenido |
|---|------|-----------|
| 25.1 | Cluster API (CAPI) | Arquitectura, providers (AWS/Azure/GCP), ClusterClass, lifecycle, upgrades. |
| 25.2 | Gestión de flotas | Rancher Fleet, ArgoCD ApplicationSets. Upgrade strategies, node drain. |
| 25.3 | Serverless: Knative | Serving, auto-scaling a cero, revisions, traffic splitting. |
| 25.4 | Virtual Kubelet | Nodos virtuales con Fargate, ACI, Cloud Run. |

**🧪 Lab.** Crear un clúster con Cluster API declarativamente y desplegar un servicio Knative
que escale a cero y reciba tráfico dividido entre revisiones.

### Sesión 26 — Hosted Control Planes: HyperShift, vCluster y Kamaji (Jueves 18/02/2027)

| # | Tema | Contenido |
|---|------|-----------|
| 26.1 | HyperShift | Arquitectura, hosted clusters, node pools. |
| 26.2 | vCluster | Clusters virtuales ligeros, sincronización, multi-tenancy. |
| 26.3 | Kamaji | Tenant control planes, datastores, gestión de flota. |
| 26.4 | Trade-offs | Aislamiento, coste, densidad y casos de uso. |

**🧪 Lab.** Desplegar vClusters como entornos aislados por equipo sobre un mismo host cluster
y comparar el aislamiento frente a namespaces.

### Sesión 27 — Multi-cluster: OCM, Istio multicluster y Cilium Cluster Mesh (Martes 23/02/2027)

| # | Tema | Contenido |
|---|------|-----------|
| 27.1 | Arquitecturas | Hub-and-spoke, peer-to-peer, federación. |
| 27.2 | Gestión | Open Cluster Management (OCM), Rancher MCM, ArgoCD multicluster. |
| 27.3 | Mesh multi-cluster | Istio multicluster (primary-remote, multi-primary), Cilium Cluster Mesh. |
| 27.4 | Conectividad | Submariner: cross-cluster networking, service discovery, globalnet. |

**🧪 Lab.** Conectar dos clústeres con Cilium Cluster Mesh (o Submariner) y exponer un servicio
compartido cross-cluster con failover.

### Sesión 28 — Multi-cloud con Crossplane y Disaster Recovery con Velero (Jueves 25/02/2027)

| # | Tema | Contenido |
|---|------|-----------|
| 28.1 | Multi-cloud con Crossplane | Plano de control universal, políticas OPA, ESO multi-cloud. |
| 28.2 | Backup/restore | Velero: backups programados, restore selectivo, migración entre clústeres. |
| 28.3 | Estrategia DR | RPO/RTO, replicación de estado, etcd backup, failover cross-region/cross-cloud. |
| 28.4 | Observabilidad global | Thanos/Mimir federados, OTel Collector como gateway. |

**🧪 Lab.** Configurar backups Velero de la plataforma y ejecutar un restore en otro clúster;
documentar el RPO/RTO alcanzado.

**Evaluación del módulo.** Labs 24–28 (40%) + operator propio funcional y una capacidad
avanzada (multi-cluster o DR) integrada en el Proyecto (60%).

**Bibliografía.** *Programming Kubernetes* (Hausenblas, Schimanski) · kubebuilder book ·
Cluster API/Knative docs · vCluster/HyperShift/Kamaji docs · Velero docs.

---

## PF — Proyecto Final

**1.5 ECTS · 6h · Sesiones 29–30 · 02/03/2027 → 04/03/2027**

**Objetivo.** Diseñar, implementar y defender una Internal Developer Platform (IDP) end-to-end
sobre Kubernetes que integre las competencias del programa. El proyecto se construye de forma
incremental a lo largo de los módulos (entregas intermedias en M4 y M5) y se consolida y
defiende en estas dos sesiones.

### Sesión 29 — Proyecto Final: desarrollo de la plataforma (IDP) (Martes 02/03/2027)

Sesión de taller: integración final de componentes, revisión de arquitectura con la dirección
académica, hardening y preparación de la demo.

### Sesión 30 — Proyecto Final: presentación y defensa (Jueves 04/03/2027)

Demo en vivo (despliegue end-to-end + escenario de fallo y recuperación + observabilidad) y
defensa oral ante tribunal.

### Requisitos mínimos

| Área | Requisito |
|------|-----------|
| Infraestructura | Aprovisionada con Terraform en al menos 1 cloud provider (2 recomendado) |
| Kubernetes | Clúster gestionado (EKS/GKE/AKS) con configuración production-ready |
| GitOps | ArgoCD gestionando los manifiestos de la plataforma |
| CI/CD | Pipeline (Tekton u otro) con build, test, scan y deploy |
| Networking | Ingress/Gateway API + TLS automático + (opcional) service mesh |
| Secretos | Vault y/o External Secrets Operator |
| Observabilidad | Métricas, logs y trazas con dashboards y alertas |
| Seguridad | RBAC, Network Policies, admission policies, image scanning/firma |
| Entrega y escalado | Estrategia progresiva (canary/blue-green) + autoscaling (HPA/KEDA) |
| Documentación | Arquitectura, decisiones técnicas (ADRs) y runbooks |

### Entregables

1. **Repositorio Git** con todo el código (IaC, manifiestos, configuración, pipelines).
2. **Memoria técnica** (arquitectura, decisiones, diagrama de componentes, lecciones aprendidas).
3. **Demo en vivo**: despliegue end-to-end, escenario de fallo y recuperación, observabilidad.
4. **Defensa oral** ante el tribunal.

### Criterios de evaluación

Funcionalidad end-to-end (30%) · Calidad de ingeniería y seguridad (25%) · Observabilidad y
operabilidad / día-2 (15%) · Documentación y ADRs (15%) · Defensa (15%).

---

## Mapa de dependencias entre módulos

```
M1 (DevOps + Programación) ─────────────────────────────┐
M2 (Cloud + IaC) ───────────────────────────────┐       │
                                                 ▼       ▼
                                        M3 (Contenedores + K8s Core)
                                                 │
                                                 ▼
                                        M4 (Producción + Cloud Native)
                                                 │
                                         ┌───────┴───────┐
                                         ▼               ▼
                                   M5 (Obs/GitOps)   M6 (PE Avanzado)
                                         │               │
                                         └───────┬───────┘
                                                 ▼
                                          PF (Proyecto Final)
```

---

## Certificaciones alineadas

| Certificación | Módulos |
|---------------|---------|
| CKA — Certified Kubernetes Administrator | M3, M4 |
| CKAD — Certified Kubernetes Application Developer | M3, M5 |
| CKS — Certified Kubernetes Security Specialist | M3, M4 |
| HashiCorp Vault Associate | M4 |
| HashiCorp Terraform Associate | M2 |
| AWS/Azure/GCP Associate Cloud | M2 |
| KCNA — Kubernetes and Cloud Native Associate | Todo el programa |
| CGOA — GitOps Certified | M5, M6 |

---

## Anexo — Visión ampliada (60 ECTS / 1500h)

> Material de referencia **no vinculante**: una hipotética edición extendida en formato máster
> (2 semestres, 60 ECTS, 1500h = 600h lectivas + 900h de trabajo autónomo) que profundiza cada
> módulo del programa publicado. Se conserva como base para futuras ediciones. El desarrollo
> original y completo de esta visión está disponible en el historial de git (fichero previo
> `roadmap-postgrado-kubernetes-full.md`).

| # | Módulo (visión 60 ECTS) | ECTS | Se corresponde con |
|---|--------------------------|------|--------------------|
| 1 | Cultura y Metodología DevOps | 4 | M1 |
| 2 | Programación para DevOps (Bash/Python/Go) | 6 | M1 |
| 3 | Redes: DNS y CDNs | 3 | M2 |
| 4 | Control de Versiones con Git | 3 | M2 |
| 5 | Cloud Computing: AWS/Azure/GCP | 8 | M2 |
| 6 | Infraestructura como Código con Terraform | 5 | M2 |
| 7 | Contenedores | 4 | M3 |
| 8 | Kubernetes Core | 10 | M3 |
| 9 | Kubernetes en Cloud Providers | 4 | M4 |
| 10 | Ecosistema Cloud Native (IaC, Secrets, Observabilidad) | 8 | M4, M5 |
| 11 | GitOps, CI/CD y Networking Avanzado | 7 | M5 |
| 12 | Kubernetes Avanzado y Multi-Cluster | 5 | M6 |
| PF | Proyecto Final de Postgrado | 6 | PF |
| | **Total** | **60** | |

En esta visión, cada ECTS lectivo se acompaña de ~1,5× de trabajo autónomo (prácticas
extendidas, lecturas y un proyecto de mayor alcance con memoria de 30–50 páginas y defensa
ante tribunal).
