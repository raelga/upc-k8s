# Posgrado en Platform Engineering y DevOps con Kubernetes

> Conviértete en Platform Engineer: especialízate en Kubernetes y despliega la nueva generación de plataformas cloud.

> 📄 **Este documento** es la vista **resumida** del programa (títulos, calendario y tecnologías).
> Para el desarrollo sesión a sesión, con laboratorios, objetivos y evaluación por módulo,
> consulta el [**roadmap detallado**](roadmap-postgrado-kubernetes-detallado.md).

## Estructura General

| Dato               | Detalle                                               |
|--------------------|-------------------------------------------------------|
| Titulación         | Diploma de experto en Platform Engineering y DevOps con Kubernetes (UPC) |
| Modalidad          | Live online                                           |
| Duración           | 5 meses                                               |
| Inicio de clases   | 03/11/2026                                            |
| Fin de clases      | 18/03/2027                                            |
| Horario            | Martes y jueves, 18:00 a 21:00 (3h por sesión)        |
| Horas lectivas     | 90h                                                   |
| Créditos           | 12 ECTS                                               |
| Estructura         | 6 módulos + Proyecto Final                            |
| Idioma             | Español                                               |
| Dirección académica| Rael Garcia Arnes · René Serral Gracià               |
| Requisitos previos | Conocimientos básicos de Linux, redes y scripting     |

---

## Distribución de Créditos y Horas

| #   | Módulo                                                                       | ECTS  | Horas  |
|-----|------------------------------------------------------------------------------|-------|--------|
| M1  | Fundamentos DevOps, Platform Engineering y Programación para Infraestructura  | 1.5   | 12h    |
| M2  | Cloud Computing Multicloud e Infraestructura como Código                      | 1     | 12h    |
| M3  | Contenedores y Kubernetes Core. Ecosistema OCI                               | 2     | 15h    |
| M4  | Kubernetes en Producción y Ecosistema Cloud Native                          | 2     | 15h    |
| M5  | Observabilidad, GitOps, CI/CD y Networking Avanzado                          | 2     | 15h    |
| M6  | Platform Engineering Avanzado: Operators, Serverless y Multi-Cluster         | 2     | 15h    |
| PF  | Proyecto Final                                                               | 1.5   | 6h     |
|     | **Total**                                                                    | **12**|**90h** |

El programa es eminentemente práctico: cada módulo combina teoría, demos en vivo y laboratorios guiados sobre entornos reales multi-cloud.

---

## Calendario de Sesiones

**30 sesiones de 3h** (martes y jueves, 18:00–21:00), del **03/11/2026** al **18/03/2027**. El calendario sigue el mismo criterio de días no lectivos que el calendario académico oficial de la UPC-FIB: festivo de La Immaculada (8 dic), vacaciones de Navidad (24, 29 y 31 dic 2026, 5 ene 2027) y festivo UPC (9 feb 2027). Las últimas fechas de la ventana oficial (9, 11, 16 y 18 mar 2027) quedan como reserva/recuperación. Consulta el [**calendario completo**](calendario.md) o `Calendario_Postgrado_Kubernetes.xlsx` (hoja *Calendario*).

| Módulo | Sesiones | Fechas                          |
|--------|----------|---------------------------------|
| M1     | 1–4      | 03/11/2026 – 12/11/2026         |
| M2     | 5–8      | 17/11/2026 – 26/11/2026         |
| M3     | 9–13     | 01/12/2026 – 17/12/2026         |
| M4     | 14–18    | 22/12/2026 – 19/01/2027         |
| M5     | 19–23    | 21/01/2027 – 04/02/2027         |
| M6     | 24–28    | 11/02/2027 – 25/02/2027         |
| PF     | 29–30    | 02/03/2027 – 04/03/2027         |

---

## M1 — Fundamentos DevOps, Platform Engineering y Programación para Infraestructura (1.5 ECTS · 12h)

**Descripción:** Contextualización del movimiento DevOps y su evolución hacia Platform Engineering. Competencias de programación asistidas por inteligencia artificial en Bash, Python y Go orientadas a la automatización de infraestructura, desarrollo de CLIs y construcción de controladores para Kubernetes.

### Fundamentos de DevOps y Platform Engineering
- Historia y principios DevOps: de Waterfall a Agile a DevOps. Cultura, automatización, medición y compartición (CALMS)
- Prácticas clave: CI/CD, Infrastructure as Code, Monitoring, Incident Management, Blameless Postmortems
- El problema de escala de DevOps: de equipos pequeños a grandes organizaciones de ingeniería
- Platform Engineering: definición, diferencias con DevOps y SRE, y casos de adopción real
- Internal Developer Platforms (IDP): concepto, golden paths, ciclo de vida y Developer Experience (DevEx)
- Team Topologies: stream-aligned, enabling, platform teams y complicated subsystem teams
- Métricas de éxito: DORA metrics (Deployment Frequency, Lead Time, MTTR, Change Failure Rate) y framework SPACE
- Backstage como portal de desarrollo interno: plugins, TechDocs y Software Catalog
- El rol del Platform Engineer: responsabilidades, skills T-shaped y evolución de carrera

### Programación para Infraestructura: Bash, Python y Go (asistida por IA)
- Programación asistida por IA: copilots y asistentes para scripting, refactorización y generación de tests
- Bash scripting avanzado: variables, estructuras de control, funciones, arrays y manejo de errores
- Automatización de sistema: gestión de procesos, pipes, redirecciones, grep/sed/awk/jq/yq, cron y Makefiles
- Python para DevOps: scripting, SDKs cloud (boto3, azure-sdk, google-cloud) y manejo de APIs REST
- Python: manipulación de YAML/JSON/TOML, Jinja2 templating, CLIs con Click/Typer y testing con pytest
- Go: sintaxis, tipos, structs, interfaces, goroutines, channels y manejo de errores idiomático
- Go para infraestructura: desarrollo de CLIs con cobra/viper y cliente Kubernetes (client-go)
- Patrones de desarrollo de controladores y operators en Go: reconciliation loop e informers
- Testing en Go: unit tests, table-driven tests, mocks con testify e integración con CI
- Herramientas de desarrollo: Makefile, direnv, pre-commit hooks y linters (golangci-lint, ruff)

---

## M2 — Cloud Computing Multicloud e Infraestructura como Código (1 ECTS · 12h)

**Descripción:** Recursos fundamentales de AWS, Azure y GCP (computación, redes, almacenamiento, identidad y servicios gestionados). Terraform como herramienta central de aprovisionamiento declarativo multi-cloud: HCL, gestión del estado, módulos, testing y CI/CD. Redes, DNS y CDNs con Cloudflare. Control de versiones avanzado con Git.

### Redes, DNS y CDN con Cloudflare
- Revisión de fundamentos TCP/IP, UDP, TLS 1.3/mTLS, HTTP/2 y HTTP/3 (QUIC)
- DNS: resolución recursiva e iterativa, registros (A, AAAA, CNAME, TXT, SRV, NS), TTL y propagación
- DNS avanzado: DNSSEC, DNS-over-HTTPS, split-horizon DNS y service discovery basado en DNS
- CDN: arquitectura, edge caching, routing geográfico, invalidación y cache-control headers
- Cloudflare: DNS authoritative, Cloudflare Tunnel, Workers, WAF, DDoS protection y R2
- Certificados TLS: PKI, cadena de confianza, ACME protocol y automatización con Let's Encrypt
- Load balancing: algoritmos, health checks, session persistence y global load balancing

### Control de Versiones Avanzado con Git
- Arquitectura interna de Git: objects (blob, tree, commit, tag), refs, packfiles, reflog y garbage collection
- Estrategias de branching: Git Flow, GitHub Flow, trunk-based development y comparativa práctica
- Rebases interactivos: squash, fixup, reword, edit y reordenación de commits
- Resolución de conflictos: estrategias de merge (recursive, ort), rerere, git mergetool y best practices
- Gestión de ramas: naming conventions, branch protection rules, CODEOWNERS y cleanup automático
- Pull Requests y code review: merge strategies (merge, squash, rebase), signed commits y draft PRs
- Git hooks: pre-commit, commit-msg, post-merge y automatización con pre-commit framework
- Monorepos: estrategias, herramientas (Nx, Turborepo) y gestión de dependencias
- Operaciones avanzadas: git bisect, git worktree, submodules, subtrees y sparse-checkout

### Cloud Computing: AWS, Azure y GCP
- AWS · IAM: users, roles, policies, OIDC federation, IRSA y AWS SSO
- AWS · Computación: EC2 (instance types, AMIs, user-data), Auto Scaling Groups, Lambda
- AWS · Redes: VPC, subnets públicas/privadas, Security Groups, ALB/NLB, Route 53 y PrivateLink
- AWS · Almacenamiento: S3 (lifecycle, versioning), EBS, EFS y ECR
- AWS · Servicios gestionados: RDS, DynamoDB, SQS, CloudWatch y Secrets Manager
- Azure · IAM: Entra ID, Managed Identities, RBAC y Azure Key Vault
- Azure · Computación: VMs, VMSS, Azure Functions y Azure Container Apps
- Azure · Redes: VNet, subnets, NSG, Load Balancer, Application Gateway y Azure DNS
- Azure · Almacenamiento: Blob Storage, Azure Files, Managed Disks y ACR
- Azure · Servicios gestionados: Azure SQL, Cosmos DB, Service Bus y Azure Monitor
- GCP · IAM: Service Accounts, Workload Identity, org policies y Cloud Audit Logs
- GCP · Computación: Compute Engine, Cloud Functions y Cloud Run
- GCP · Redes: VPC, Firewall Rules, Cloud NAT, Cloud Load Balancing y Cloud DNS
- GCP · Almacenamiento: Cloud Storage, Persistent Disk y Artifact Registry
- GCP · Servicios gestionados: Cloud SQL, Firestore, Pub/Sub y Cloud Monitoring
- Comparativa multi-cloud: estrategias de portabilidad, vendor lock-in y abstracción de recursos

### Infraestructura como Código con Terraform
- Fundamentos de IaC: filosofía declarativa vs imperativa, idempotencia y drift detection
- HCL: sintaxis, tipos de datos, expresiones, funciones y meta-argumentos (count, for_each, depends_on)
- Providers: configuración, autenticación y uso de los providers de AWS, Azure y GCP
- State management: local vs remote state, state locking, backends (S3, GCS, Azure Blob) y workspaces
- Módulos: diseño, versionado, registro público y privado, composición y reusabilidad
- Patrones avanzados: for_each, dynamic blocks, moved blocks, import y workspaces
- Terraform en CI/CD: plan/apply automatizado, Atlantis y GitHub Actions
- Testing de infraestructura: terraform test, tflint, checkov, tfsec y políticas con OPA/Conftest
- Alternativas complementarias: OpenTofu, Pulumi y CDKTF

---

## M3 — Contenedores y Kubernetes Core. Ecosistema OCI (2 ECTS · 15h)

**Descripción:** Ecosistema OCI: construcción de imágenes, runtimes, registros y seguridad. Arquitectura completa de Kubernetes: plano de control, bloques fundamentales (workloads, configuración, scheduling), almacenamiento (PV/PVC, CSI), networking (Services, Ingress, Gateway API, CNI, Network Policies), autenticación (RBAC, OIDC, admission controllers) y construcción de un clúster componente a componente.

### Contenedores y Ecosistema OCI
- Arquitectura de contenedores: Linux namespaces, cgroups v2, UnionFS y el modelo de capas OCI
- Dockerfile avanzado: multi-stage builds, BuildKit, cache optimization y distroless/scratch images
- Container runtimes: Docker, containerd, CRI-O, runc, gVisor y la interfaz CRI de Kubernetes
- Docker Compose: definición de servicios multi-contenedor, redes, volúmenes y profiles
- Registros de imágenes: Docker Hub, GHCR, ECR, ACR, GAR y Harbor como registro privado
- Seguridad de imágenes: CVE scanning con Trivy/Grype, image signing con Cosign y generación de SBOM
- Builds in-cluster: kaniko, buildah y Paketo Buildpacks para entornos sin Docker daemon
- Optimización: reducción de tamaño, gestión de capas, secrets en build time y multi-platform builds
- OCI Artifacts: almacenamiento de Helm charts, políticas OPA y otros artefactos en registros OCI

### Kubernetes Core: Arquitectura y Building Blocks
- Introducción · Control Plane: kube-apiserver, etcd, kube-scheduler, controller-manager, cloud-controller-manager
- Introducción · Data Plane: kubelet, kube-proxy, container runtime y comunicación entre nodos
- Clusters locales · kind (Kubernetes in Docker): configuración multi-nodo, networking y uso en CI
- Building Blocks · Pods: ciclo de vida, init containers, sidecar pattern y ephemeral containers
- Building Blocks · Workloads: Deployment, StatefulSet, DaemonSet, Job, CronJob y ReplicaSet
- Building Blocks · Configuración: ConfigMap, Secret (tipos, encriptación at rest), env vars y volúmenes
- Building Blocks · Namespace, Labels, Selectors, Annotations, Finalizers y OwnerReferences
- Building Blocks · Scheduling: node/pod affinity, taints, tolerations, topology spread y priority classes
- Building Blocks · Resource management: requests, limits, LimitRange, ResourceQuota y QoS classes
- Almacenamiento · PersistentVolume, PersistentVolumeClaim, StorageClass y dynamic provisioning
- Almacenamiento · CSI: arquitectura, drivers (EBS, Azure Disk, GCE PD), volume snapshots y Velero
- Networking · Services: ClusterIP, NodePort, LoadBalancer, ExternalName, Headless y EndpointSlices
- Networking · Ingress: controllers, IngressClass, Gateway API (HTTPRoute, GRPCRoute)
- Networking · CNI: Calico, Cilium, Flannel. NetworkPolicy y microsegmentación de tráfico
- Networking · DNS interno: CoreDNS, resolución de servicios y customización de zonas
- Autenticación · RBAC: ServiceAccounts, Roles, ClusterRoles, Bindings y principio de mínimo privilegio
- Autenticación · certificados X.509, OIDC, webhook auth y bound SA tokens
- Autenticación · Admission controllers: validating/mutating webhooks, OPA Gatekeeper y Kyverno
- Autenticación · Pod Security Admission (PSA) y Pod Security Standards
- Cluster desde cero · etcd, kube-apiserver, scheduler, controller-manager, kubelet, kube-proxy: configuración manual, PKI y TLS bootstrapping

---

## M4 — Kubernetes en Producción y Ecosistema Cloud Native (2 ECTS · 15h)

**Descripción:** Operación de clústeres gestionados (EKS, GKE, AKS) y otros entornos. Application bundles (Helm, Kustomize). Infraestructura declarativa dentro de Kubernetes: ExternalDNS, cert-manager y Crossplane. Gestión de secretos con HashiCorp Vault y External Secrets Operator.

### Kubernetes en Producción: clústeres gestionados multi-cloud
- EKS (AWS): arquitectura, node groups (managed, self-managed, Fargate), eksctl
- EKS Add-ons: AWS Load Balancer Controller, EBS/EFS CSI, VPC CNI, ExternalDNS
- EKS Seguridad: IRSA, EKS Pod Identity, KMS encryption y audit logging
- GKE: Standard vs Autopilot, node pools, Workload Identity y VPC-native networking
- GKE Add-ons: Cloud Operations, Config Connector, GKE Gateway y Fleet Management
- AKS: arquitectura, AAD/Entra ID integration, Managed Identities y Azure CNI
- AKS Add-ons: Azure Monitor, CSI drivers (Disk/Files/Blob), AGIC y Azure Policy
- AKS Seguridad: Workload Identity, Azure Key Vault CSI Provider y Defender for Containers
- Otros clouds: OVHcloud, DigitalOcean DOKS, Scaleway, Linode LKE y Hetzner
- On-premises: k3s, k0s, Rancher, Tanzu y OpenShift
- Aprovisionamiento IaC: Terraform modules para EKS, GKE y AKS
- Comparativa multi-cloud: feature matrix, managed vs self-managed, pricing y criterios de selección

### Application Bundles e Infraestructura Declarativa
- Helm: charts, templates, values, hooks, repositorios, helm-secrets y helm-diff
- Kustomize: bases, overlays, patches, generators y transformers. Helm + Kustomize
- Patrón Operator: CRDs, controller loop, Operator Lifecycle Manager, niveles de madurez
- Operators de referencia: cert-manager, Prometheus Operator, Strimzi, Crossplane
- ExternalDNS: providers (Route53, CloudDNS, Cloudflare), anotaciones y políticas de sync
- cert-manager: Issuers, ClusterIssuers, Let's Encrypt, ACME DNS-01/HTTP-01, renovación automática
- Crossplane: Providers, Managed Resources, Compositions, XRDs. Comparativa con Terraform
- Crossplane avanzado: Composition Functions, EnvironmentConfigs, integración con ArgoCD

### Gestión de Secretos: Vault y External Secrets
- Vault · Arquitectura: server, agents, backends de almacenamiento y alta disponibilidad
- Vault · Auth methods en Kubernetes: Kubernetes Auth, JWT/OIDC, AppRole y cloud IAM
- Vault · Secrets Engines: KV v1/v2, Dynamic Secrets (database, AWS, Azure), PKI y Transit
- Vault · Vault Agent: auto-auth, template rendering, sidecar injection. Vault Secrets Operator (VSO)
- Vault · Políticas (HCL), namespaces, auditing y disaster recovery con Raft integrated storage
- Vault · Operaciones: inicialización, unseal, auto-unseal con KMS (AWS, Azure, GCP)
- External Secrets · Arquitectura: ExternalSecret, SecretStore, ClusterSecretStore y refresh intervals
- External Secrets · Providers: AWS Secrets Manager, Azure Key Vault, GCP Secret Manager y Vault
- External Secrets · Patrones avanzados: secret templating, generators y pushSecret. Integración con GitOps
- Secret Management · Sealed Secrets, SOPS y comparativa de patrones por madurez

---

## M5 — Observabilidad, GitOps, CI/CD y Networking Avanzado (2 ECTS · 15h)

**Descripción:** Stack de observabilidad completo: Prometheus, Grafana (Loki, Tempo, Mimir), OpenTelemetry. GitOps con ArgoCD y Prow. Pipelines con Tekton. Networking avanzado con Traefik e Istio (service mesh). Estrategias de despliegue (canary, blue/green) con Argo Rollouts. Escalado de workloads (HPA, VPA, KEDA, Karpenter).

### Observabilidad
- Los tres pilares: métricas, logs, trazas. Correlación entre señales
- Prometheus: arquitectura, scraping, PromQL, service discovery, Alertmanager
- Prometheus Operator: ServiceMonitor, PodMonitor, recording rules, alerting rules. Thanos para HA
- Grafana: datasources, dashboards, variables, alerting. Grafana as Code (grafonnet, Terraform)
- Grafana stack: Loki (logs), Tempo (trazas), Mimir (métricas), Alloy (collector)
- OpenTelemetry: especificación OTLP, Collector pipelines, auto-instrumentación en Kubernetes
- Stack completo: Prometheus + Grafana + Loki + Tempo + OTel Collector integrados

### GitOps y Pipelines CI/CD
- Principios GitOps: declarativo, versionado, automatizado, reconciliado. Pull vs Push model
- ArgoCD: Applications, AppProjects, ApplicationSets, sync policies, waves, hooks y RBAC
- ArgoCD avanzado: multi-tenancy, SSO, App of Apps, ApplicationSet generators y notifications
- ArgoCD Image Updater y Argo Rollouts: patrones de Progressive Delivery con análisis automático
- Prow: arquitectura CI nativa en Kubernetes, plugins, Tide, Deck dashboard y ProwJobs
- Tekton: Tasks, Pipelines, PipelineRuns, Workspaces, Triggers y Tekton Chains
- Integración Tekton + ArgoCD para workflows CI/CD end-to-end en Kubernetes

### Networking Avanzado (Service Mesh)
- Traefik: IngressRoute CRDs, middlewares, TLS automático, dashboard y métricas
- Traefik avanzado: TCP/UDP routing, rate limiting, circuit breaker, canary con TraefikService
- Istio: arquitectura (Istiod + Envoy sidecars), mTLS automático y observabilidad integrada
- Istio traffic: VirtualServices, DestinationRules, Gateways, traffic shifting, fault injection
- Istio seguridad: AuthorizationPolicies, PeerAuthentication, circuit breaking, Kiali
- Ambient Mesh (Istio): modo sin sidecar, ztunnel, waypoints y migración

### Entrega Progresiva y Escalado
- Estrategias: rolling update, blue/green, canary, A/B testing y trade-offs
- Argo Rollouts: canary con análisis automatizado, blue-green, integración Istio/Traefik + Prometheus
- Progressive delivery: Feature flags (Flagger/OpenFeature), métricas como gates, rollback automático
- HPA: métricas CPU/memory, custom metrics (Prometheus Adapter), scaling behavior
- VPA: modos (Off/Initial/Auto), recomendaciones y limitaciones
- KEDA: ScaledObject, ScaledJob, triggers (Kafka, SQS, Prometheus, cron) y cooldown
- Cluster Autoscaler vs Karpenter: node pools, scale-from-zero, cost optimization

---

## M6 — Platform Engineering Avanzado: Operators, Serverless y Multi-Cluster (2 ECTS · 15h)

**Descripción:** Construcción de operators personalizados con Kubebuilder/Operator SDK. Gestión del ciclo de vida de clústeres con Cluster API. Serverless con Knative. Hosted Control Planes (HyperShift, vCluster, Kamaji). Gestión y despliegue multi-cluster (Istio multicluster, Cilium Cluster Mesh, Submariner) y multi-cloud con Crossplane. Disaster Recovery con Velero.

### Construcción de Operators
- Operator SDK (Go): scaffolding, CRD design, controller implementation y webhooks
- kubebuilder: reconciliation patterns, finalizers, status conditions y API versioning
- Operadores de producción: leader election, metrics, testing (envtest) y OLM

### Gestión de Clústeres y Serverless
- Cluster API (CAPI): arquitectura, providers (AWS/Azure/GCP), lifecycle y upgrades
- Rancher Fleet y ArgoCD ApplicationSets para gestión de flotas de clusters
- Upgrade strategies: rolling upgrades, ventanas de mantenimiento y node drain
- Knative Serving: auto-scaling a cero, revision routing y traffic splitting
- Virtual Kubelet: nodos virtuales con Fargate, ACI y Cloud Run

### Hosted Control Planes
- HyperShift (Red Hat): arquitectura, hosted clusters y node pools
- vCluster: clusters virtuales ligeros, sincronización y multi-tenancy
- Kamaji: tenant control planes, datastores y gestión de flota

### Multi-cluster y Multi-cloud
- Arquitecturas: hub-and-spoke, peer-to-peer, federación
- Open Cluster Management (OCM), Rancher MCM y ArgoCD multicluster
- Istio multicluster (primary-remote, multi-primary)
- Cilium Cluster Mesh: tunneling, shared services y network policies globales
- Submariner: cross-cluster networking, service discovery y globalnet
- Crossplane como plano de control universal, políticas OPA y ESO multi-cloud
- Disaster Recovery: Velero, replicación de estado, RPO/RTO y failover automático

---

## PF — Proyecto Final (1.5 ECTS · 6h)

**Descripción:** Diseño, implementación y defensa de una plataforma interna de desarrollo (IDP) end-to-end que integre las competencias del programa.

- Aprovisionamiento de la infraestructura base con Terraform sobre uno o varios proveedores cloud
- Despliegue y configuración de un clúster Kubernetes gestionado
- Flujo GitOps con ArgoCD para el ciclo de vida de las aplicaciones de plataforma
- Gestión de secretos con Vault y/o External Secrets Operator
- Stack de observabilidad (métricas, logs, trazas) y alerting
- Entrega progresiva (canary o blue/green) con rollback automático basado en métricas
- Documentación, golden paths y defensa del proyecto

---

## Certificaciones Oficiales Alineadas

| Certificación                                   | Cobertura en el programa        |
|-------------------------------------------------|---------------------------------|
| CKA — Certified Kubernetes Administrator         | Módulos M3 y M4                 |
| CKAD — Certified Kubernetes Application Developer | Módulos M3 y M5                 |
| CKS — Certified Kubernetes Security Specialist    | Módulos M3 y M4                 |
| HashiCorp Vault Associate                        | Módulo M4                       |
| HashiCorp Terraform Associate                    | Módulo M2                       |
| AWS / Azure / GCP Associate Cloud                | Módulo M2                       |
| KCNA — Kubernetes and Cloud Native Associate     | Cobertura completa del programa |
| CGOA — GitOps Certified (Linux Foundation)       | Módulos M5 y M6                 |

---

## Herramientas y Tecnologías

| Categoría            | Tecnologías                                                  |
|----------------------|--------------------------------------------------------------|
| Lenguajes            | Go, Python, Bash                                             |
| Contenedores         | Docker, containerd, BuildKit, kaniko, Cosign, Syft          |
| Kubernetes local     | kind, minikube, k3d, k3s                                     |
| IaC                  | Terraform, OpenTofu, Crossplane, ExternalDNS, cert-manager  |
| Secret Management    | HashiCorp Vault, External Secrets Operator, Sealed Secrets, SOPS |
| GitOps               | ArgoCD, Prow, Argo Rollouts, Argo Image Updater             |
| Pipelines CI/CD      | Tekton + Chains, GitHub Actions                             |
| Observabilidad       | Prometheus, Grafana, Loki, Tempo, OpenTelemetry Collector   |
| Networking           | Traefik, Istio (+ Ambient), Cilium, Calico, CoreDNS         |
| Seguridad            | OPA/Gatekeeper, Kyverno, Trivy, Cosign, SBOM                |
| App Bundles          | Helm 3, Kustomize, Operator SDK, kubebuilder                |
| Scaling              | HPA, VPA, KEDA, Karpenter, Cluster Autoscaler               |
| Serverless           | Knative Serving, Virtual Kubelet, KEDA                      |
| Hosted Ctrl Planes   | HyperShift, Kamaji, vCluster                                |
| Multi-cluster        | Cluster API, Rancher Fleet, OCM, Cilium Cluster Mesh, Submariner |
| Developer Portal     | Backstage                                                   |
| Cloud                | AWS (EKS), Azure (AKS), GCP (GKE)                           |
