# Postgrado Universitario en Kubernetes y Platform Engineering

## Estructura General

| Dato               | Detalle                                               |
|--------------------|-------------------------------------------------------|
| Modalidad          | Semipresencial / Online                               |
| Duración           | 20 semanas                                            |
| Horas lectivas     | 140h (40 sesiones de 3.5h)                            |
| Dedicación semanal | 7h/semana (2 sesiones)                                |
| Módulos            | 12 módulos                                            |
| Formato de sesión  | Bloques de 3.5h (teoría + demo + lab guiado)          |
| Requisitos previos | Conocimientos básicos de Linux, redes y scripting     |

---

## Distribución de Horas

| #   | Módulo                                                           | Sesiones | Horas  |
|-----|------------------------------------------------------------------|----------|--------|
| M01 | Fundamentos de DevOps y Platform Engineering                     | 1        | 3.5h   |
| M02 | Programación para DevOps: Go, Python y Bash                     | 2        | 7h     |
| M03 | Redes, DNS y CDN con Cloudflare                                 | 1        | 3.5h   |
| M04 | Control de Versiones Avanzado con Git                            | 1        | 3.5h   |
| M05 | Cloud Computing: AWS, Azure y GCP                               | 3        | 10.5h  |
| M06 | Infraestructura como Código con Terraform                       | 2        | 7h     |
| M07 | Contenedores y Ecosistema OCI                                   | 2        | 7h     |
| M08 | Kubernetes Core: Arquitectura y Building Blocks                 | 8        | 28h    |
| M09 | Kubernetes en Producción: Multi-cloud                           | 2        | 7h     |
| M10 | Ecosistema Cloud Native: Bundles, IaC, Secrets y Observabilidad | 7        | 24.5h  |
| M11 | GitOps, Pipelines y Networking Avanzado                         | 6        | 21h    |
| M12 | Platform Engineering Avanzado: Operators y Multi-cluster        | 5        | 17.5h  |
|     | **Total**                                                        | **40**   |**140h**|

---

## BLOQUE I — Fundamentos y Cultura DevOps

### M01 — Fundamentos de DevOps y Platform Engineering (3.5h · 1 sesión)

**Objetivo:** Contextualización histórica, filosófica y organizativa del movimiento DevOps y su evolución hacia Platform Engineering.

| Sesión | Título | Contenido |
|--------|--------|-----------|
| 1 | DevOps y Platform Engineering | Historia DevOps: Waterfall, Agile, DevOps. CALMS. Prácticas clave: CI/CD, IaC, Monitoring, Blameless Postmortems. Platform Engineering: IDP, golden paths, DevEx. Team Topologies. DORA metrics. Backstage como portal interno. |

**Temario detallado:**
- Historia y principios DevOps: cultura, automatización, medición y compartición (CALMS)
- Prácticas clave: CI/CD, Infrastructure as Code, Monitoring, Incident Management, Blameless Postmortems
- El problema de escala de DevOps: de equipos pequeños a grandes organizaciones
- Platform Engineering: definición, diferencias con DevOps y SRE
- Internal Developer Platforms (IDP): concepto, golden paths, ciclo de vida y Developer Experience (DevEx)
- Team Topologies: stream-aligned, enabling, platform teams y complicated subsystem teams
- Métricas de éxito: DORA metrics y framework SPACE
- Backstage como portal de desarrollo interno
- El rol del Platform Engineer: responsabilidades y evolución de carrera

---

### M02 — Programación para DevOps: Go, Python y Bash (7h · 2 sesiones)

**Objetivo:** Bases de programación orientadas a la automatización de infraestructura y desarrollo de herramientas de plataforma.

| Sesión | Título | Contenido |
|--------|--------|-----------|
| 2 | Bash y Python para DevOps | Bash: variables, control de flujo, funciones, pipes, grep/sed/awk/jq. Python: scripting, SDKs cloud, CLIs con Click/Typer, pytest, ruff. |
| 3 | Go para Cloud Native | Fundamentos Go: tipos, structs, interfaces, goroutines, channels. CLIs con cobra/viper, client-go, controller-runtime. Testing y golangci-lint. |

**Temario detallado:**
- Bash scripting avanzado: variables, estructuras de control, funciones, arrays y manejo de errores
- Automatización: pipes, redirecciones, grep/sed/awk/jq/yq, cron y Makefiles
- Python para DevOps: scripting, SDKs cloud (boto3, azure-sdk, google-cloud), APIs REST
- Python: YAML/JSON/TOML, CLIs con Click/Typer y testing con pytest
- Go: sintaxis, tipos, structs, interfaces, goroutines, channels
- Go para infraestructura: CLIs con cobra/viper, client-go, controller-runtime
- Patrones de desarrollo de controladores y operators en Go
- Testing en Go: unit tests, table-driven tests, mocks con testify
- Herramientas: Makefile, direnv, pre-commit hooks, linters (golangci-lint, ruff)

---

### M03 — Redes, DNS y CDN con Cloudflare (3.5h · 1 sesión)

**Objetivo:** Fundamentos de red aplicados a entornos cloud y distribuidos, con Cloudflare como plataforma de referencia.

| Sesión | Título | Contenido |
|--------|--------|-----------|
| 4 | DNS, CDNs y Cloudflare | TCP/IP, DNS en profundidad (registros, resolución, DNSSEC). CDNs: edge caching, anycast. Cloudflare: DNS autoritativo, proxy, WAF, Workers, R2, Tunnels. TLS y ACME. |

**Temario detallado:**
- Revisión de fundamentos TCP/IP, UDP, TLS 1.3/mTLS, HTTP/2 y HTTP/3 (QUIC)
- DNS: resolución recursiva e iterativa, registros (A, AAAA, CNAME, TXT, SRV, NS), TTL
- DNS avanzado: DNSSEC, DNS-over-HTTPS, split-horizon DNS, service discovery
- CDN: arquitectura, edge caching, routing geográfico, invalidación
- Cloudflare: DNS authoritative, Tunnel, Workers, WAF, DDoS protection, R2
- Certificados TLS: PKI, cadena de confianza, ACME protocol, Let's Encrypt
- Load balancing: algoritmos, health checks, session persistence

---

## BLOQUE II — Infraestructura y Colaboración

### M04 — Control de Versiones Avanzado con Git (3.5h · 1 sesión)

**Objetivo:** Dominio profundo de Git como herramienta colaborativa en equipos de alto rendimiento.

| Sesión | Título | Contenido |
|--------|--------|-----------|
| 5 | Git avanzado | Internals de Git: objects, DAG, reflog. Flujos: Git Flow, GitHub Flow, trunk-based. Rebase interactivo, resolución de conflictos, CODEOWNERS, hooks, monorepos. |

**Temario detallado:**
- Arquitectura interna: objects (blob, tree, commit, tag), refs, packfiles, reflog
- Estrategias de branching: Git Flow, GitHub Flow, trunk-based development
- Rebases interactivos: squash, fixup, reword, edit y reordenación
- Resolución de conflictos: estrategias de merge (recursive, ort), rerere
- Gestión de ramas: naming conventions, branch protection, CODEOWNERS
- Pull Requests y code review: merge strategies, signed commits
- Git hooks: pre-commit, commit-msg, pre-commit framework
- Monorepos: estrategias, herramientas (Nx, Turborepo)
- Operaciones avanzadas: git bisect, git worktree, submodules, subtrees

---

## BLOQUE III — Cloud Computing

### M05 — Cloud Computing: AWS, Azure y GCP (10.5h · 3 sesiones)

**Objetivo:** Introducción práctica a los tres grandes proveedores cloud con foco en los recursos necesarios para Kubernetes.

| Sesión | Título | Contenido |
|--------|--------|-----------|
| 6 | Introducción a AWS | IAM (users, roles, policies, OIDC). EC2, ASG, Lambda. VPC, subnets, SG, ALB. S3, EBS, EFS, ECR. RDS, DynamoDB, SQS, CloudWatch. |
| 7 | Introducción a Azure | Entra ID, Managed Identities, RBAC. VMs, VMSS, Azure Functions. VNet, NSG, Load Balancer. Blob Storage, Azure Files, ACR. Azure SQL, Cosmos DB. |
| 8 | Introducción a GCP y comparativa | Service Accounts, Workload Identity. Compute Engine, Cloud Functions, Cloud Run. VPC, Cloud NAT, Cloud LB. Cloud Storage, Artifact Registry. Comparativa multi-cloud. |

**Temario detallado:**
- AWS: IAM, EC2, ASG, Lambda, VPC, subnets, SG, ALB/NLB, Route 53, S3, EBS, EFS, ECR, RDS, DynamoDB, SQS, CloudWatch, Secrets Manager
- Azure: Entra ID, Managed Identities, VMs, VMSS, Azure Functions, VNet, NSG, Load Balancer, Application Gateway, Blob Storage, Azure Files, ACR, Azure SQL, Cosmos DB, Service Bus, Azure Monitor
- GCP: Service Accounts, Workload Identity, Compute Engine, Cloud Functions, Cloud Run, VPC, Cloud NAT, Cloud LB, Cloud DNS, Cloud Storage, Artifact Registry, Cloud SQL, Firestore, Pub/Sub, Cloud Monitoring
- Comparativa multi-cloud: portabilidad, vendor lock-in, abstracción de recursos

---

### M06 — Infraestructura como Código con Terraform (7h · 2 sesiones)

**Objetivo:** Diseño y operación de infraestructura declarativa multi-cloud con Terraform.

| Sesión | Título | Contenido |
|--------|--------|-----------|
| 9 | Terraform: fundamentos y state | IaC declarativa. HCL, providers, resources, data sources, variables, outputs. State: local vs remote, locking, backends. Módulos: estructura, versionado, registry. |
| 10 | Terraform: avanzado y CI/CD | for_each, dynamic blocks, moved blocks, import, workspaces. CI/CD: Atlantis, GitHub Actions. Testing: tflint, checkov, OPA. OpenTofu. |

**Temario detallado:**
- Fundamentos de IaC: declarativa vs imperativa, idempotencia, drift detection
- HCL: sintaxis, tipos, expresiones, funciones, count, for_each, depends_on
- Providers: configuración y autenticación AWS, Azure, GCP
- State: local vs remote, locking, backends (S3, GCS, Azure Blob), workspaces
- Módulos: diseño, versionado, registro público y privado, composición
- Patrones avanzados: for_each, dynamic blocks, moved blocks, import
- CI/CD: plan/apply automatizado, Atlantis, GitHub Actions
- Testing: terraform test, tflint, checkov, tfsec, OPA/Conftest
- Alternativas: OpenTofu, Pulumi, CDKTF

---

## BLOQUE IV — Contenedores

### M07 — Contenedores y Ecosistema OCI (7h · 2 sesiones)

**Objetivo:** Dominio del ecosistema de contenedores: desde la construcción de imágenes hasta seguridad y registros.

| Sesión | Título | Contenido |
|--------|--------|-----------|
| 11 | Contenedores: fundamentos y Docker | Namespaces, cgroups, OCI. Dockerfile: multi-stage, BuildKit, cache. Runtimes: containerd, CRI-O, gVisor. Docker Compose. Podman. |
| 12 | Imágenes: seguridad, registries y builds | Imágenes: distroless, scratch, alpine. Scanning: Trivy, Grype, Cosign, SBOM. Registries: Harbor, ECR, ACR, GAR. Kaniko, Buildpacks. OCI Artifacts. |

**Temario detallado:**
- Arquitectura: Linux namespaces, cgroups v2, UnionFS, modelo de capas OCI
- Dockerfile avanzado: multi-stage builds, BuildKit, cache optimization, distroless/scratch
- Container runtimes: Docker, containerd, CRI-O, runc, gVisor, CRI de Kubernetes
- Docker Compose: servicios multi-contenedor, redes, volúmenes, profiles
- Registros: Docker Hub, GHCR, ECR, ACR, GAR, Harbor
- Seguridad: CVE scanning con Trivy/Grype, image signing con Cosign, SBOM
- Builds in-cluster: kaniko, buildah, Paketo Buildpacks
- Optimización: reducción de tamaño, secrets en build time, multi-platform builds
- OCI Artifacts: Helm charts, políticas OPA en registros OCI

---

## BLOQUE V — Kubernetes Core

### M08 — Kubernetes Core: Arquitectura y Building Blocks (28h · 8 sesiones)

**Objetivo:** Estudio exhaustivo de la arquitectura de Kubernetes y sus objetos fundamentales.

| Sesión | Título | Contenido |
|--------|--------|-----------|
| 13 | Introducción y arquitectura | Historia, CNCF. Control plane: API server, etcd, scheduler, controller-manager. Data plane: kubelet, kube-proxy, CRI. Clusters locales con kind. |
| 14 | Building Blocks: Workloads | Pod anatomy, ciclo de vida. ReplicaSet, Deployment (rolling update, rollback). DaemonSet, StatefulSet, Job, CronJob. Init containers, sidecar. |
| 15 | Building Blocks: Configuración y organización | ConfigMap, Secret, ServiceAccount. Namespaces, Labels, Selectors, Annotations, Finalizers, OwnerReferences. ResourceQuotas, LimitRanges. |
| 16 | Almacenamiento en Kubernetes | PV, PVC, StorageClass, dynamic provisioning. CSI drivers (EBS, Azure Disk, GCE PD). EmptyDir, hostPath, volume snapshots, expansion, cloning. Velero. |
| 17 | Aplicaciones en Kubernetes | Probes (liveness, readiness, startup). Scheduling: affinity/anti-affinity, taints, tolerations, topology spread. Requests, limits, QoS, PriorityClasses, PDBs. |
| 18 | Networking en Kubernetes | Modelo de red, CNI (Calico, Cilium, Flannel). Services: ClusterIP, NodePort, LoadBalancer, Headless. Ingress, Gateway API. Network Policies. CoreDNS. |
| 19 | Autenticación y autorización | RBAC: Role, ClusterRole, Bindings, ServiceAccounts. Auth: X.509, OIDC, webhook, SA tokens. Admission controllers: Gatekeeper, Kyverno. PSA. |
| 20 | Cluster componente a componente | Kubernetes "the hard way": etcd, API server, scheduler, controller-manager. kubelet, containerd, kube-proxy, TLS bootstrapping. PKI, kubeadm. Debugging. |

**Temario detallado:**
- Control Plane: kube-apiserver, etcd, kube-scheduler, controller-manager, cloud-controller-manager
- Data Plane: kubelet, kube-proxy, container runtime, comunicación entre nodos
- Clusters locales: kind (multi-nodo, networking, CI), minikube, k3d
- Pods: ciclo de vida, init containers, sidecar pattern, ephemeral containers
- Workloads: Deployment, StatefulSet, DaemonSet, Job, CronJob, ReplicaSet
- Configuración: ConfigMap, Secret (encriptación at rest), env vars, volúmenes
- Scheduling: node/pod affinity, taints, tolerations, topology spread, priority classes
- Resource management: requests, limits, LimitRange, ResourceQuota, QoS
- Almacenamiento: PV, PVC, StorageClass, CSI drivers, volume snapshots, Velero
- Aplicaciones: Probes, rolling updates, rollbacks, PDBs, Reloader
- Services: ClusterIP, NodePort, LoadBalancer, ExternalName, Headless, EndpointSlices
- Ingress: controllers, IngressClass, Gateway API (HTTPRoute, GRPCRoute)
- CNI: Calico, Cilium, Flannel. NetworkPolicy, microsegmentación
- DNS: CoreDNS, resolución de servicios, customización de zonas
- RBAC: ServiceAccounts, Roles, ClusterRoles, Bindings, mínimo privilegio
- Autenticación: X.509, OIDC, webhook auth, bound SA tokens
- Admission controllers: validating/mutating webhooks, OPA Gatekeeper, Kyverno
- Pod Security Admission (PSA) y Pod Security Standards
- Cluster desde cero: etcd, API server, scheduler, controller-manager, kubelet, PKI, kubeadm, debugging

---

## BLOQUE VI — Kubernetes en Cloud

### M09 — Kubernetes en Producción: Multi-cloud (7h · 2 sesiones)

**Objetivo:** Despliegue y operación de Kubernetes gestionado en los principales proveedores cloud y otros entornos.

| Sesión | Título | Contenido |
|--------|--------|-----------|
| 21 | Kubernetes en AWS (EKS) y GCP (GKE) | EKS: arquitectura, node groups, Fargate, IRSA, EBS CSI, ALB Controller, VPC CNI. GKE: Autopilot vs Standard, Workload Identity, GKE Gateway, Fleet Management. |
| 22 | Kubernetes en Azure (AKS) y otros | AKS: node pools, Workload Identity, Azure CNI, AGIC, Defender. Otros: DOKS, LKE, OVHcloud, k3s, Talos. Terraform IaC. Comparativa. |

**Temario detallado:**
- EKS: arquitectura, node groups (managed, self-managed, Fargate), eksctl, IRSA, EKS Pod Identity
- EKS Add-ons: AWS LB Controller, EBS/EFS CSI, VPC CNI, ExternalDNS
- GKE: Standard vs Autopilot, node pools, Workload Identity, VPC-native networking
- GKE Add-ons: Cloud Operations, Config Connector, GKE Gateway, Fleet Management
- AKS: arquitectura, Entra ID, Managed Identities, Azure CNI
- AKS Add-ons: Azure Monitor, CSI drivers, AGIC, Azure Policy, Defender
- Otros clouds: DOKS, OKE, LKE, OVHcloud, Scaleway, Hetzner
- On-premises: k3s, k0s, Rancher, Tanzu, OpenShift
- Aprovisionamiento IaC: Terraform modules para EKS, GKE, AKS
- Comparativa: feature matrix, pricing, managed vs self-managed

---

## BLOQUE VII — Ecosistema Cloud Native

### M10 — Ecosistema Cloud Native: Bundles, IaC, Secrets y Observabilidad (24.5h · 7 sesiones)

**Objetivo:** Herramientas del ecosistema CNCF para gestionar application bundles, infraestructura declarativa, secretos y observabilidad.

| Sesión | Título | Contenido |
|--------|--------|-----------|
| 23 | Application Bundles y Operators Overview | Helm: charts, templates, values, hooks. Kustomize: overlays, patches, generators. Helm + Kustomize. Patrón Operator, CRDs, OLM, operators de referencia. |
| 24 | InfraAsCode: ExternalDNS, cert-manager y Crossplane | ExternalDNS: providers, sincronización. cert-manager: Issuers, Let's Encrypt, ACME. Crossplane: Providers, Compositions, XRDs. Crossplane vs Terraform. |
| 25 | Vault: fundamentos y Kubernetes | Vault: arquitectura, seal/unseal, HA. Auth: K8s Auth, OIDC, AppRole. Secret engines: KV, Dynamic Secrets, PKI, Transit. Vault Agent y VSO. |
| 26 | External Secrets y Secret Management | ESO: SecretStore, ExternalSecret, providers. Templating, generators, pushSecret. Sealed Secrets, SOPS. Vault + ESO combinados. |
| 27 | Prometheus y Alertmanager | Tres pilares de observabilidad. Prometheus: arquitectura, PromQL, service discovery. Prometheus Operator. Recording/alerting rules. Thanos HA. |
| 28 | Grafana, Loki, Tempo y stack completo | Grafana: dashboards, alerting, Grafana as Code. Loki (logs), Tempo (trazas), Mimir (métricas), Alloy (collector). |
| 29 | OpenTelemetry y observabilidad end-to-end | OTel: especificación OTLP, SDK, Collector pipelines. Auto-instrumentación en K8s. Lab: métricas, trazas, logs y dashboards. |

**Temario detallado:**
- Helm: charts, templates, values, hooks, repositorios, helm-secrets, helm-diff
- Kustomize: bases, overlays, patches, generators, transformers. Helm + Kustomize
- Patrón Operator: CRDs, controller loop, OLM, niveles de madurez
- ExternalDNS: providers (Route53, CloudDNS, Cloudflare), sincronización
- cert-manager: Issuers, ClusterIssuers, Let's Encrypt, ACME DNS-01/HTTP-01
- Crossplane: Providers, Managed Resources, Compositions, XRDs, Composition Functions
- Vault: arquitectura, auth methods, secret engines (KV, Dynamic, PKI, Transit), Agent, VSO
- External Secrets Operator: SecretStore, ExternalSecret, providers, templating
- Sealed Secrets, SOPS, comparativa de patrones
- Prometheus: arquitectura, scraping, PromQL, Alertmanager, Prometheus Operator, Thanos
- Grafana: datasources, dashboards, alerting, Grafana as Code. Loki, Tempo, Mimir, Alloy
- OpenTelemetry: especificación OTLP, Collector, auto-instrumentación

---

## BLOQUE VIII — GitOps, CI/CD y Networking

### M11 — GitOps, Pipelines y Networking Avanzado (21h · 6 sesiones)

**Objetivo:** Herramientas que conforman el ecosistema moderno de entrega continua y networking avanzado en Kubernetes.

| Sesión | Título | Contenido |
|--------|--------|-----------|
| 30 | GitOps: principios y ArgoCD | Principios GitOps: pull vs push. ArgoCD: Application, ApplicationSet, Projects, sync policies, RBAC. App of Apps, SSO, notifications. |
| 31 | Prow, Tekton y pipelines CI/CD | Prow: plugins, Tide, Deck, ProwJobs. Tekton: Tasks, Pipelines, Triggers, Tekton Chains. Integración Tekton + ArgoCD. |
| 32 | Networking: Traefik | Traefik: IngressRoute CRD, middlewares (rate limiting, auth), TLS automático. TCP/UDP routing, canary, métricas, dashboard. |
| 33 | Networking: Istio | Service mesh: Istiod, Envoy sidecar, Ambient mode. VirtualService, DestinationRule, Gateway, traffic shifting, fault injection. mTLS, AuthorizationPolicy, Kiali. |
| 34 | Estrategias de despliegue y Progressive Delivery | Rolling, blue/green, canary, A/B. Argo Rollouts: canary + Prometheus. Progressive delivery: Flagger, OpenFeature, rollback automático. |
| 35 | Scaling de workloads y clusters | HPA: CPU/memory, custom metrics. VPA: modos y limitaciones. KEDA: event-driven, triggers. Cluster Autoscaler vs Karpenter, cost optimization. |

**Temario detallado:**
- GitOps: principios, pull vs push model
- ArgoCD: Applications, AppProjects, ApplicationSets, sync policies, RBAC, SSO, notifications
- ArgoCD Image Updater, Argo Rollouts, Progressive Delivery
- Prow: CI nativa en Kubernetes, plugins, Tide, Deck, ProwJobs
- Tekton: Tasks, Pipelines, PipelineRuns, Workspaces, Triggers, Tekton Chains
- Traefik: IngressRoute CRDs, middlewares, TLS, TCP/UDP routing, canary
- Istio: arquitectura, mTLS, VirtualServices, DestinationRules, Gateways, AuthorizationPolicies
- Istio Ambient Mesh: ztunnel, waypoints, migración desde sidecar
- Estrategias de despliegue: rolling, blue/green, canary, A/B
- Argo Rollouts: canary con análisis automatizado, integración Istio/Traefik + Prometheus
- Progressive delivery: Flagger, OpenFeature, métricas como gates
- HPA, VPA, KEDA, Cluster Autoscaler, Karpenter

---

## BLOQUE IX — Platform Engineering Avanzado

### M12 — Platform Engineering Avanzado: Operators y Multi-cluster (17.5h · 5 sesiones)

**Objetivo:** Capacidades avanzadas de plataforma: construcción de operators, hosted control planes, serverless y despliegues multi-cluster/multi-cloud.

| Sesión | Título | Contenido |
|--------|--------|-----------|
| 36 | Building Kubernetes Operators | CRD design, API versioning. Kubebuilder/Operator SDK: scaffolding, controller-runtime, reconciliation loop. Testing con envtest, OLM. |
| 37 | Cluster Management y Serverless | Cluster API: providers, ClusterClass. Rancher Fleet. Knative Serving, Virtual Kubelet (Fargate, ACI). Upgrade strategies. |
| 38 | Hosted Control Planes | HyperShift: arquitectura, hosted clusters. vCluster: clusters virtuales, multi-tenancy. Kamaji: tenant control planes. Comparativa. |
| 39 | Multi-cluster management y deployments | Arquitecturas: hub-spoke, federación. OCM, Rancher MCM, ArgoCD multicluster. Istio multicluster, Cilium Cluster Mesh, Submariner. |
| 40 | Multi-cloud deployments y Disaster Recovery | Crossplane multi-cloud, OPA policies, ESO multi-cloud. Velero backup/restore, RPO/RTO, failover cross-region/cross-cloud. |

**Temario detallado:**
- Operator SDK (Go): scaffolding, CRD design, controller implementation, webhooks
- kubebuilder: reconciliation patterns, finalizers, status conditions, API versioning
- Operadores de producción: leader election, metrics, testing (envtest), OLM
- Cluster API (CAPI): arquitectura, providers, lifecycle, upgrades automáticos
- Rancher Fleet, ArgoCD ApplicationSets para gestión de flotas
- Knative Serving: auto-scaling a cero, revision routing, traffic splitting
- Virtual Kubelet: nodos virtuales con Fargate, ACI, Cloud Run
- HyperShift, vCluster, Kamaji: hosted control planes y comparativa
- Multi-cluster: hub-and-spoke, OCM, Rancher MCM, ArgoCD multicluster
- Istio multicluster, Cilium Cluster Mesh, Submariner
- Multi-cloud: Crossplane, OPA policies, ESO multi-cloud
- Disaster Recovery: Velero, replicación de estado, RPO/RTO, failover

---

## Calendario Semanal (20 semanas · 7h/semana)

| Semana | Sesión A (3.5h) | Sesión B (3.5h) | Módulo |
|--------|-----------------|-----------------|--------|
| 1 | S01: DevOps y Platform Engineering | S02: Bash y Python | M01 + M02 |
| 2 | S03: Go para Cloud Native | S04: DNS, CDNs y Cloudflare | M02 + M03 |
| 3 | S05: Git avanzado | S06: Introducción a AWS | M04 + M05 |
| 4 | S07: Introducción a Azure | S08: Introducción a GCP | M05 |
| 5 | S09: Terraform fundamentos | S10: Terraform avanzado | M06 |
| 6 | S11: Contenedores fundamentos | S12: Imágenes y seguridad | M07 |
| 7 | S13: Arquitectura Kubernetes | S14: Building Blocks: Workloads | M08 |
| 8 | S15: Configuración y organización | S16: Almacenamiento | M08 |
| 9 | S17: Aplicaciones | S18: Networking | M08 |
| 10 | S19: Autenticación y autorización | S20: Cluster componente a componente | M08 |
| 11 | S21: EKS y GKE | S22: AKS y otros | M09 |
| 12 | S23: Application Bundles y Operators | S24: ExternalDNS, cert-manager, Crossplane | M10 |
| 13 | S25: Vault fundamentos y K8s | S26: External Secrets | M10 |
| 14 | S27: Prometheus y Alertmanager | S28: Grafana, Loki, Tempo | M10 |
| 15 | S29: OpenTelemetry end-to-end | S30: GitOps y ArgoCD | M10 + M11 |
| 16 | S31: Prow, Tekton y CI/CD | S32: Networking: Traefik | M11 |
| 17 | S33: Networking: Istio | S34: Deployment strategies | M11 |
| 18 | S35: Scaling | S36: Building Operators | M11 + M12 |
| 19 | S37: Cluster Management y Serverless | S38: Hosted Control Planes | M12 |
| 20 | S39: Multi-cluster management | S40: Multi-cloud y DR | M12 |

---

## Certificaciones Oficiales Alineadas

| Certificación | Cobertura |
|---------------|-----------|
| CKA — Certified Kubernetes Administrator | Módulos M08 y M09 |
| CKAD — Certified Kubernetes Application Dev. | Módulos M07, M08 y M11 |
| CKS — Certified Kubernetes Security Specialist | Módulos M08, M09 y M10 |
| HashiCorp Vault Associate | Módulo M10 |
| HashiCorp Terraform Associate | Módulo M06 |
| AWS / Azure / GCP Associate Cloud | Módulo M05 |
| KCNA — Kubernetes and Cloud Native Associate | Cobertura completa |
| GitOps Certified (CGOA — Linux Foundation) | Módulos M11 y M12 |

---

## Herramientas y Tecnologías

| Categoría | Tecnologías |
|-----------|-------------|
| Lenguajes | Go, Python, Bash |
| Contenedores | Docker, containerd, BuildKit, kaniko, Cosign, Syft |
| Kubernetes local | kind, minikube, k3d, k3s |
| IaC | Terraform, OpenTofu, Crossplane, ExternalDNS, cert-manager |
| Secret Management | HashiCorp Vault, External Secrets Operator, Sealed Secrets, SOPS |
| GitOps | ArgoCD, Prow, Argo Rollouts, Argo Image Updater |
| Pipelines CI/CD | Tekton + Chains, GitHub Actions |
| Observabilidad | Prometheus, Grafana, Loki, Tempo, OpenTelemetry Collector |
| Networking | Traefik, Istio (+ Ambient), Cilium, Calico, CoreDNS |
| Seguridad | OPA/Gatekeeper, Kyverno, Trivy, Cosign, SBOM |
| App Bundles | Helm 3, Kustomize, Operator SDK, kubebuilder |
| Scaling | HPA, VPA, KEDA, Karpenter, Cluster Autoscaler |
| Serverless | Knative Serving, Virtual Kubelet, KEDA |
| Hosted Control Planes | HyperShift, Kamaji, vCluster |
| Multi-cluster | Cluster API, Rancher Fleet, OCM, Cilium Cluster Mesh, Submariner |
| Developer Portal | Backstage |
| Cloud | AWS (EKS), Azure (AKS), GCP (GKE) |

---

## Bibliografía y Recursos de Referencia

| Recurso | Tipo |
|---------|------|
| *Kubernetes in Action, 2nd Ed.* — Marko Lukša | Libro |
| *The Phoenix Project* — Kim, Behr, Spafford | Libro |
| *Team Topologies* — Skelton, Pais | Libro |
| *Terraform: Up & Running, 3rd Ed.* — Yevgeniy Brikman | Libro |
| *Programming Kubernetes* — Hausenblas, Schimanski | Libro |
| *Istio in Action* — Posta, Maloku | Libro |
| *Observability Engineering* — Majors, Fong-Jones, Miranda | Libro |
| *Cloud Native DevOps with Kubernetes* — Arundel, Domingus | Libro |
| kubernetes.io/docs | Documentación oficial |
| cncf.io/projects | Landscape CNCF |
| learn.hashicorp.com | Tutoriales Terraform/Vault |
| prometheus.io/docs | Documentación Prometheus |
| argoproj.github.io | Documentación Argo (CD, Rollouts, Workflows) |
