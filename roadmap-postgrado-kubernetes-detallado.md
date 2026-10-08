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
| M1 · Fundamentos DevOps, PE y Programación | 1.5 | 6h  | 1–2   | 03/11 → 05/11/2026 |
| M2 · Cloud Multicloud e IaC                | 1   | 12h | 3–6   | 10/11 → 19/11/2026 |
| M3 · Contenedores y Kubernetes Core (OCI)  | 2   | 15h | 7–11  | 24/11 → 10/12/2026 |
| M4 · Kubernetes en Producción y Cloud Native | 2 | 15h | 12–16 | 15/12/2026 → 12/01/2027 |
| M5 · Observabilidad, GitOps, CI/CD y Networking | 2 | 18h | 17–22 | 14/01 → 02/02/2027 |
| M6 · Platform Engineering Avanzado         | 2   | 18h | 23–28 | 04/02 → 25/02/2027 |
| PF · Proyecto Final                        | 1.5 | 6h  | 29–30 | 02/03 → 04/03/2027 |
| **Total**                                  | **12** | **90h** | **30** | |

> **Rebalanceo interno (sin alterar ECTS oficiales ni el total de 90h/30 sesiones):**
> M1 pasa de 4 a 2 sesiones (Go se traslada a M6, justo antes de construir operators,
> aprendizaje just-in-time). Las 2 sesiones liberadas se reparten: +1 en M5 (se divide
> la observabilidad en 3 sesiones — métricas, logs, trazas+correlación — en vez de 2) y
> +1 en M6 (nueva sesión de Go). Los ECTS por módulo se mantienen como en la ficha
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

### Sesión 1 — DevOps y Platform Engineering (Martes 03/11/2026)

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

**1 ECTS · 12h · Sesiones 3–6 · 10/11/2026 → 19/11/2026**

**Objetivo.** Comprender los recursos fundamentales de AWS, Azure y GCP y aprovisionarlos de
forma declarativa, auditable y reutilizable con Terraform, sobre una base sólida de redes/DNS
y control de versiones avanzado.

**Competencias de entrada.** M1. Nociones de redes TCP/IP y una cuenta en al menos un cloud.

### Sesión 3 — Redes, DNS y CDN con Cloudflare (Martes 10/11/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 3.1 | Modelo TCP/IP | Repaso de capas, TCP/UDP, TLS 1.3/mTLS, HTTP/2 y HTTP/3 (QUIC), gRPC. |
| 3.2 | DNS en profundidad | Jerarquía, registros (A, AAAA, CNAME, TXT, SRV, NS), resolución recursiva vs iterativa, TTL. |
| 3.3 | DNS avanzado | DNSSEC, DNS-over-HTTPS, split-horizon, service discovery basado en DNS. |
| 3.4 | CDN y Cloudflare | Edge caching, anycast, invalidación. DNS autoritativo, WAF, Workers, R2, Zero Trust Tunnels. TLS/ACME. |

**🧪 Lab.** Configurar un dominio en Cloudflare: DNS, reglas WAF, un Worker edge-side y un
Tunnel hacia un servicio local. Verificar TLS automático.

### Sesión 4 — Control de versiones avanzado con Git (Jueves 12/11/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 4.1 | Internals de Git | Objetos (blob, tree, commit, tag), DAG, refs, reflog, packfiles, GC. |
| 4.2 | Flujos de colaboración | Git Flow, GitHub Flow, trunk-based development. Pros y contras. |
| 4.3 | Operativa avanzada | Rebase interactivo (squash, fixup, autosquash), cherry-pick, bisect, worktree, resolución de conflictos (ort, rerere). |
| 4.4 | Colaboración a escala | Branch protection, CODEOWNERS, signed commits, hooks (pre-commit), monorepos. |

**🧪 Lab.** Sobre un repo con historia "sucia": limpiar con rebase interactivo, configurar
branch protection + CODEOWNERS + pre-commit hooks y documentar la estrategia de branching.

### Sesión 5 — Cloud Computing: AWS, Azure y GCP (Martes 17/11/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 5.1 | Identidad | AWS IAM/IRSA · Azure Entra ID/Managed Identities · GCP IAM/Workload Identity. |
| 5.2 | Computación | EC2/ASG/Lambda · VMs/VMSS/Functions · Compute Engine/Cloud Run. |
| 5.3 | Redes | VPC/SG/ALB/Route53 · VNet/NSG/App Gateway/Azure DNS · VPC/Cloud NAT/Cloud LB/Cloud DNS. |
| 5.4 | Almacenamiento y gestionados | S3/EBS/ECR/RDS · Blob/Files/ACR/Azure SQL · GCS/Artifact Registry/Cloud SQL. Comparativa y vendor lock-in. |

**🧪 Lab.** Desplegar manualmente (consola/CLI) una VPC con subredes públicas/privadas y una
VM accesible en uno de los tres clouds; documentar el equivalente en los otros dos.

### Sesión 6 — Infraestructura como Código con Terraform (Jueves 19/11/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 6.1 | Fundamentos IaC | Declarativo vs imperativo, idempotencia, drift detection. |
| 6.2 | HCL y providers | Sintaxis, expresiones, funciones, meta-argumentos (count, for_each, depends_on). Providers AWS/Azure/GCP. |
| 6.3 | State y módulos | Local vs remote state, locking, backends (S3/GCS/Azure Blob), workspaces. Diseño y versionado de módulos. |
| 6.4 | Avanzado y CI/CD | dynamic blocks, moved, import. plan/apply automatizado (Atlantis, GitHub Actions). Testing: tflint, checkov, OPA/Conftest. OpenTofu. |

**🧪 Lab.** Reescribir la infraestructura del Lab 5 como módulo Terraform reutilizable, con
remote state y un pipeline `plan` en CI que ejecute `tflint`/`checkov`.

**Evaluación del módulo.** Entrega de los 4 labs (50%) + un módulo Terraform multi-cloud
reutilizable con state remoto y validación en CI (50%).

**Bibliografía.** *Terraform: Up & Running* (Brikman) · docs de AWS/Azure/GCP well-architected
· documentación de Cloudflare y de Git (Pro Git, Chacon & Straub).

---

## M3 — Contenedores y Kubernetes Core. Ecosistema OCI

**2 ECTS · 15h · Sesiones 7–11 · 24/11/2026 → 10/12/2026**

**Objetivo.** Dominar el ecosistema de contenedores (OCI) y la arquitectura de Kubernetes,
construyendo y operando sus objetos fundamentales, hasta levantar un clúster componente a
componente.

**Competencias de entrada.** M1–M2. Familiaridad con Linux (namespaces, procesos) y Docker básico.

### Sesión 7 — Contenedores y ecosistema OCI (Martes 24/11/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 7.1 | Arquitectura de contenedores | Linux namespaces, cgroups v2, UnionFS, modelo de capas OCI. |
| 7.2 | Build de imágenes | Dockerfile avanzado, multi-stage, BuildKit, cache, distroless/scratch, multi-platform. |
| 7.3 | Runtimes y registros | Docker, containerd, CRI-O, runc, gVisor, CRI. Docker Hub, GHCR, ECR/ACR/GAR, Harbor. |
| 7.4 | Seguridad de la cadena | CVE scanning (Trivy/Grype), firma (Cosign), SBOM. Builds in-cluster (kaniko, buildah). OCI Artifacts. |

**🧪 Lab.** Construir una imagen multi-stage distroless, escanearla con Trivy, firmarla con
Cosign y generar su SBOM; publicarla en un registro privado (Harbor/GHCR).

### Sesión 8 — Kubernetes: arquitectura y clusters locales (Jueves 26/11/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 8.1 | Control plane | kube-apiserver, etcd, kube-scheduler, controller-manager, cloud-controller-manager. |
| 8.2 | Data plane | kubelet, kube-proxy, container runtime, comunicación entre nodos. |
| 8.3 | API y objetos | Modelo declarativo, API groups, CRUD con kubectl, dry-run, server-side apply. |
| 8.4 | Clusters locales | kind (Kubernetes in Docker): multi-nodo, port mappings, uso en CI. |

**🧪 Lab.** Levantar un clúster multi-nodo con kind, inspeccionar los componentes del control
plane y desplegar la imagen firmada del Lab 7.

### Sesión 9 — Building Blocks: workloads, configuración y scheduling (Martes 01/12/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 9.1 | Pods y workloads | Ciclo de vida, init/sidecar/ephemeral containers. Deployment, StatefulSet, DaemonSet, Job, CronJob, ReplicaSet. |
| 9.2 | Configuración | ConfigMap, Secret (tipos, encriptación at rest), env vars, volúmenes. Reloader. |
| 9.3 | Organización | Namespaces, Labels, Selectors, Annotations, Finalizers, OwnerReferences. |
| 9.4 | Scheduling y recursos | Affinity/anti-affinity, taints/tolerations, topology spread, PriorityClasses. requests/limits, LimitRange, ResourceQuota, QoS, PDB. |

**🧪 Lab.** Desplegar una app multi-componente (Deployment + StatefulSet) con ConfigMaps,
Secrets, probes, requests/limits y reglas de scheduling; provocar un reschedule y observarlo.

### Sesión 10 — Almacenamiento y networking en Kubernetes (Jueves 03/12/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 10.1 | Almacenamiento | PV, PVC, StorageClass, dynamic provisioning. CSI (EBS, Azure Disk, GCE PD), snapshots, cloning. |
| 10.2 | Services | ClusterIP, NodePort, LoadBalancer, ExternalName, Headless, EndpointSlices. |
| 10.3 | Ingress y Gateway API | Ingress controllers, IngressClass, Gateway API (HTTPRoute, GRPCRoute). |
| 10.4 | CNI y DNS | Calico, Cilium, Flannel. NetworkPolicy y microsegmentación. CoreDNS. |

**🧪 Lab.** Exponer la app del Lab 9 vía Ingress/Gateway API con almacenamiento persistente
(PVC) y aplicar NetworkPolicies de mínimo privilegio entre componentes.

### Sesión 11 — Autenticación, RBAC y clúster componente a componente (Jueves 10/12/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 11.1 | RBAC | ServiceAccounts, Roles, ClusterRoles, Bindings, mínimo privilegio. |
| 11.2 | Autenticación y admisión | X.509, OIDC, webhook auth, bound SA tokens. Admission controllers, OPA Gatekeeper, Kyverno, PSA. |
| 11.3 | Cluster desde cero (I) | etcd (operaciones, snapshots, TLS), kube-apiserver, scheduler, controller-manager: configuración manual y flags. |
| 11.4 | Cluster desde cero (II) | kubelet, containerd, kube-proxy, TLS bootstrapping. PKI con cfssl/openssl. kubeadm bajo el capó. Debugging. |

**🧪 Lab.** "Kubernetes the hard way" reducido: arrancar los componentes del control plane con
certificados propios y unir un nodo; validar con un Pod de prueba. Definir RBAC de mínimo
privilegio para un equipo.

**Evaluación del módulo.** Labs 7–11 (40%) + prueba práctica: desplegar y exponer de forma
segura una aplicación en Kubernetes partiendo de una imagen firmada (60%). Cobertura de CKAD/CKS.

**Bibliografía.** *Kubernetes in Action* (Lukša) · *Programming Kubernetes* (Hausenblas,
Schimanski) · Kubernetes docs · CKA/CKAD/CKS curricula (CNCF/Linux Foundation).

---

## M4 — Kubernetes en Producción y Ecosistema Cloud Native

**2 ECTS · 15h · Sesiones 12–16 · 15/12/2026 → 12/01/2027**

**Objetivo.** Operar Kubernetes gestionado en los grandes clouds y desplegar el ecosistema
cloud native imprescindible: application bundles, infraestructura declarativa y gestión de
secretos.

**Competencias de entrada.** M3. Acceso a al menos un cloud provider.

### Sesión 12 — Kubernetes gestionado: EKS, GKE y AKS (Martes 15/12/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 12.1 | EKS | Node groups (managed/self-managed/Fargate), eksctl, IRSA/Pod Identity, add-ons (ALB Controller, EBS/EFS CSI, VPC CNI), KMS/audit. |
| 12.2 | GKE | Standard vs Autopilot, Workload Identity, VPC-native, Config Connector, GKE Gateway, Fleet. |
| 12.3 | AKS | Entra ID, Managed Identities, Azure CNI, Azure Monitor, CSI, AGIC, Azure Policy, Defender for Containers. |
| 12.4 | Comparativa | Feature matrix, managed vs self-managed, pricing y criterios de selección. |

**🧪 Lab.** Provisionar un clúster gestionado (EKS/GKE/AKS) con Terraform, habilitar Workload
Identity/IRSA y desplegar una app con un LoadBalancer/Ingress cloud-native.

### Sesión 13 — Otros entornos y aprovisionamiento IaC multi-cloud (Jueves 17/12/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 13.1 | Otros clouds | OVHcloud, DigitalOcean DOKS, Linode LKE, Scaleway, Hetzner. |
| 13.2 | On-premises / edge | k3s, k0s, Rancher, Talos, OpenShift. |
| 13.3 | IaC de clústeres | Módulos Terraform para EKS/GKE/AKS; parametrización y entornos. |
| 13.4 | Día 2 | Upgrades, node pools, backups y consideraciones de coste. |

**🧪 Lab.** Levantar un clúster ligero (k3s/Talos) y compararlo operativamente con el
gestionado del Lab 12 (arranque, upgrades, add-ons).

### Sesión 14 — Application bundles: Kustomize, Helm y su ecosistema (Martes 22/12/2026)

| # | Tema | Contenido |
|---|------|-----------|
| 14.1 | Kustomize | Bases, overlays, patches, generators, transformers. 2 ejemplos prácticos (dev/prod). |
| 14.2 | Helm | Charts, templates, values, hooks. El catálogo de Helm (Artifact Hub) como ecosistema de distribución. |
| 14.3 | Helm + Kustomize | helm-secrets, helm-diff. Combinar Helm (render) con overlays Kustomize por entorno. |
| 14.4 | Caso real: charts que despliegan operators | Ejemplo con el chart de kube-prometheus-stack / Grafana Operator: un chart puede instalar un Operator + sus CRDs. *Se profundizará en el patrón Operator en la Sesión 24.* |

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

### Sesión 15 — Infraestructura declarativa: ExternalDNS, cert-manager y Crossplane (Jueves 07/01/2027)

| # | Tema | Contenido |
|---|------|-----------|
| 15.1 | ExternalDNS | Providers (Route53, CloudDNS, Cloudflare), anotaciones, políticas de sync. |
| 15.2 | cert-manager | Issuers/ClusterIssuers, Let's Encrypt, ACME DNS-01/HTTP-01, renovación automática. |
| 15.3 | Crossplane | Providers, Managed Resources, Compositions, XRDs. Comparativa con Terraform. |
| 15.4 | Crossplane avanzado | Composition Functions, EnvironmentConfigs, integración con ArgoCD. |

**🧪 Lab.** Automatizar DNS + TLS de la app (ExternalDNS + cert-manager) y aprovisionar un
recurso cloud (p.ej. bucket) desde Kubernetes con Crossplane.

### Sesión 16 — Gestión de secretos: Vault y External Secrets (Martes 12/01/2027)

| # | Tema | Contenido |
|---|------|-----------|
| 16.1 | Vault: arquitectura | Server/agents, storage backends, HA, seal/unseal, auto-unseal con KMS. |
| 16.2 | Vault: auth y engines | Kubernetes Auth, JWT/OIDC, AppRole. KV v1/v2, Dynamic Secrets, PKI, Transit. Vault Agent, VSO. |
| 16.3 | External Secrets | ExternalSecret, SecretStore/ClusterSecretStore, providers (AWS SM, Azure KV, GCP SM, Vault), templating, pushSecret. |
| 16.4 | Otros patrones | Sealed Secrets, SOPS. Comparativa por madurez e integración con GitOps. |

**🧪 Lab.** Desplegar Vault en el clúster, configurar Kubernetes Auth y un secret dinámico, y
consumirlo desde la app mediante External Secrets Operator.

**Evaluación del módulo.** Labs 12–16 (40%) + entrega intermedia del Proyecto Final: clúster
gestionado con app empaquetada (Helm/Kustomize), DNS+TLS automáticos y secretos gestionados (60%).

**Bibliografía.** Docs de EKS/GKE/AKS · Helm & Kustomize docs · cert-manager/ExternalDNS/
Crossplane docs · HashiCorp Vault Associate curriculum · External Secrets Operator docs.

---

## M5 — Observabilidad, GitOps, CI/CD y Networking Avanzado

**2 ECTS · 15h · Sesiones 19–23 · 28/01/2027 → 11/02/2027**

**Objetivo.** Instrumentar plataformas con observabilidad completa, entregar de forma
declarativa con GitOps y pipelines, y gobernar el tráfico con service mesh y estrategias de
despliegue progresivo y escalado.

**Competencias de entrada.** M3–M4. App desplegable en un clúster gestionado.

### Sesión 19 — Observabilidad (I): Prometheus y Alertmanager (Jueves 28/01/2027)

| # | Tema | Contenido |
|---|------|-----------|
| 19.1 | Los tres pilares | Métricas, logs, trazas y su correlación. |
| 19.2 | Prometheus | Arquitectura, scraping, PromQL, service discovery. |
| 19.3 | Prometheus Operator | ServiceMonitor, PodMonitor, recording/alerting rules. Thanos para HA. |
| 19.4 | Alerting | Alertmanager: routing, silencing, inhibición, receptores. |

**🧪 Lab.** Instrumentar la app, desplegar kube-prometheus-stack, escribir consultas PromQL y
definir una alerta con enrutado en Alertmanager.

### Sesión 20 — Observabilidad (II): Grafana stack y OpenTelemetry (Martes 02/02/2027)

| # | Tema | Contenido |
|---|------|-----------|
| 20.1 | Grafana | Datasources, dashboards, variables, alerting. Grafana as Code (grafonnet/Terraform). |
| 20.2 | Grafana stack | Loki (logs), Tempo (trazas), Mimir (métricas), Alloy (collector). |
| 20.3 | OpenTelemetry | Especificación OTLP, SDK, Collector (receivers/processors/exporters), auto-instrumentación. |
| 20.4 | End-to-end | Correlación métricas ↔ logs ↔ trazas en un mismo dashboard. |

**🧪 Lab.** Añadir logs (Loki) y trazas (Tempo/OTel) a la app y construir un dashboard que
correlacione las tres señales; provocar un fallo y diagnosticarlo.

### Sesión 21 — GitOps y pipelines CI/CD (Jueves 04/02/2027)

| # | Tema | Contenido |
|---|------|-----------|
| 21.1 | Principios GitOps | Declarativo, versionado, automatizado, reconciliado. Pull vs push. |
| 21.2 | ArgoCD | Applications, AppProjects, ApplicationSets, sync policies, waves, hooks, RBAC, App of Apps, SSO. |
| 21.3 | Prow | CI nativo en Kubernetes: plugins, Tide, Deck, ProwJobs. |
| 21.4 | Tekton | Tasks, Pipelines, PipelineRuns, Workspaces, Triggers, Chains. Integración Tekton + ArgoCD. |

**🧪 Lab.** Poner la plataforma bajo ArgoCD (App of Apps) y construir un pipeline Tekton
build→test→scan→deploy que actualice el repo GitOps.

### Sesión 22 — Networking avanzado: Traefik e Istio (Martes 09/02/2027)

| # | Tema | Contenido |
|---|------|-----------|
| 22.1 | Traefik | IngressRoute CRDs, middlewares, TLS automático, TCP/UDP, rate limiting, dashboard. |
| 22.2 | Istio: arquitectura | Istiod + Envoy sidecars, mTLS automático, observabilidad integrada, Kiali. |
| 22.3 | Istio: tráfico | VirtualServices, DestinationRules, Gateways, traffic shifting, fault injection. |
| 22.4 | Istio: seguridad y Ambient | AuthorizationPolicies, PeerAuthentication, circuit breaking. Ambient Mesh (ztunnel, waypoints). |

**🧪 Lab.** Inyectar la app en un service mesh (Istio), habilitar mTLS estricto, aplicar una
AuthorizationPolicy y hacer traffic shifting entre dos versiones.

### Sesión 23 — Entrega progresiva y escalado (Jueves 11/02/2027)

| # | Tema | Contenido |
|---|------|-----------|
| 23.1 | Estrategias | Rolling, blue/green, canary, A/B y trade-offs. |
| 23.2 | Argo Rollouts | Canary con análisis automatizado (Prometheus), blue-green, integración Istio/Traefik. |
| 23.3 | Progressive delivery | Feature flags (Flagger/OpenFeature), métricas como gates, rollback automático. |
| 23.4 | Escalado | HPA (custom metrics), VPA, KEDA (event-driven), Cluster Autoscaler vs Karpenter. |

**🧪 Lab.** Configurar un despliegue canary con Argo Rollouts y análisis basado en métricas
Prometheus, con rollback automático al degradarse el SLO; añadir un HPA y un ScaledObject KEDA.

**Evaluación del módulo.** Labs 19–23 (40%) + entrega del Proyecto: plataforma bajo GitOps con
observabilidad, service mesh y despliegue progresivo funcionando (60%). Cobertura de CGOA.

**Bibliografía.** Prometheus/Grafana/OpenTelemetry docs · *Observability Engineering*
(Majors et al.) · ArgoCD/Tekton docs · Istio docs · Argo Rollouts/KEDA docs.

---

## M6 — Platform Engineering Avanzado: Operators, Serverless y Multi-Cluster

**2 ECTS · 15h · Sesiones 24–28 · 16/02/2027 → 02/03/2027**

**Objetivo.** Extender Kubernetes con operators propios y operar plataformas avanzadas:
gestión del ciclo de vida de clústeres, serverless, hosted control planes y arquitecturas
multi-cluster/multi-cloud con disaster recovery.

**Competencias de entrada.** M3–M5 y programación en Go (M1).

### Sesión 24 — Construcción de Operators (Martes 16/02/2027)

| # | Tema | Contenido |
|---|------|-----------|
| 24.1 | Diseño de API | CRD design, API versioning, status subresource, conditions. |
| 24.2 | Kubebuilder/Operator SDK | Scaffolding, controller-runtime, reconciliation loop, predicates, webhooks. |
| 24.3 | Finalizers y estado | Finalizers, owner references, gestión de errores y requeue. |
| 24.4 | Operators de producción | Leader election, métricas, testing con envtest, empaquetado con OLM. |

**🧪 Lab.** Construir un operator sencillo (p.ej. que reconcilie un recurso `Website`) con
kubebuilder, con status conditions, finalizer y tests envtest.

### Sesión 25 — Gestión de clústeres y serverless (Jueves 18/02/2027)

| # | Tema | Contenido |
|---|------|-----------|
| 25.1 | Cluster API (CAPI) | Arquitectura, providers (AWS/Azure/GCP), ClusterClass, lifecycle, upgrades. |
| 25.2 | Gestión de flotas | Rancher Fleet, ArgoCD ApplicationSets. Upgrade strategies, node drain. |
| 25.3 | Serverless: Knative | Serving, auto-scaling a cero, revisions, traffic splitting. |
| 25.4 | Virtual Kubelet | Nodos virtuales con Fargate, ACI, Cloud Run. |

**🧪 Lab.** Crear un clúster con Cluster API declarativamente y desplegar un servicio Knative
que escale a cero y reciba tráfico dividido entre revisiones.

### Sesión 26 — Hosted Control Planes (Martes 23/02/2027)

| # | Tema | Contenido |
|---|------|-----------|
| 26.1 | HyperShift | Arquitectura, hosted clusters, node pools. |
| 26.2 | vCluster | Clusters virtuales ligeros, sincronización, multi-tenancy. |
| 26.3 | Kamaji | Tenant control planes, datastores, gestión de flota. |
| 26.4 | Trade-offs | Aislamiento, coste, densidad y casos de uso. |

**🧪 Lab.** Desplegar vClusters como entornos aislados por equipo sobre un mismo host cluster
y comparar el aislamiento frente a namespaces.

### Sesión 27 — Multi-cluster (Jueves 25/02/2027)

| # | Tema | Contenido |
|---|------|-----------|
| 27.1 | Arquitecturas | Hub-and-spoke, peer-to-peer, federación. |
| 27.2 | Gestión | Open Cluster Management (OCM), Rancher MCM, ArgoCD multicluster. |
| 27.3 | Mesh multi-cluster | Istio multicluster (primary-remote, multi-primary), Cilium Cluster Mesh. |
| 27.4 | Conectividad | Submariner: cross-cluster networking, service discovery, globalnet. |

**🧪 Lab.** Conectar dos clústeres con Cilium Cluster Mesh (o Submariner) y exponer un servicio
compartido cross-cluster con failover.

### Sesión 28 — Multi-cloud y Disaster Recovery (Martes 02/03/2027)

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

**1.5 ECTS · 6h · Sesiones 29–30 · 04/03/2027 → 09/03/2027**

**Objetivo.** Diseñar, implementar y defender una Internal Developer Platform (IDP) end-to-end
sobre Kubernetes que integre las competencias del programa. El proyecto se construye de forma
incremental a lo largo de los módulos (entregas intermedias en M4 y M5) y se consolida y
defiende en estas dos sesiones.

### Sesión 29 — Desarrollo y consolidación (Jueves 04/03/2027)

Sesión de taller: integración final de componentes, revisión de arquitectura con la dirección
académica, hardening y preparación de la demo.

### Sesión 30 — Presentación y defensa (Martes 09/03/2027)

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
