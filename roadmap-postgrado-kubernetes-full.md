# Postgrado Universitario en Kubernetes y Cloud Native Engineering

> **Nota:** Este documento es una **visión expandida y aspiracional** (60 ECTS / 1500h,
> formato máster de 2 semestres). **No** corresponde al programa publicado por la UPC.
> El programa oficial es de **90h lectivas / 12 ECTS** (6 módulos + Proyecto Final,
> *live online*, martes y jueves 18:00–21:00, 03/11/2026 → 18/03/2027) y su temario
> vigente está en [`roadmap-postgrado-kubernetes.md`](roadmap-postgrado-kubernetes.md).
> Se conserva aquí como material de referencia y posible base para futuras ediciones ampliadas.
> Página publicada: https://upcschool.upc.edu/esp/estudis/formacio/curs/305300/postgrau-platform-engineering-devops-kubernetes/

## Estructura General

| Dato               | Detalle                                      |
|---------------------|----------------------------------------------|
| Modalidad           | Semipresencial / Online                      |
| Duración            | 12 meses (2 semestres)                       |
| Créditos ECTS       | 60                                           |
| Módulos             | 12 módulos + Proyecto Final                  |
| Horas totales       | 1500h (600h lectivas + 900h trabajo autónomo)|
| Requisitos previos  | Grado en Informática o experiencia equivalente|

---

## Semestre 1: Fundamentos y Cloud Computing

---

### Módulo 1 — Cultura y Metodología DevOps (4 ECTS)

**Objetivo:** Comprender el paradigma DevOps y la disciplina emergente de Platform Engineering como marco conceptual del postgrado.

| # | Tema | Contenido |
|---|------|-----------|
| 1.1 | Historia y motivación | Del modelo Waterfall a Agile, del Agile a DevOps. Los muros entre Dev y Ops. |
| 1.2 | Principios DevOps | CALMS (Culture, Automation, Lean, Measurement, Sharing). Los tres caminos (The Phoenix Project). |
| 1.3 | Prácticas clave | CI/CD, Infrastructure as Code, Monitoring, Incident Management, Blameless Postmortems. |
| 1.4 | Platform Engineering | Qué es una Internal Developer Platform (IDP). Golden paths. Developer Experience (DevEx). |
| 1.5 | Roles y organizaciones | SRE vs DevOps vs Platform Engineer. Team Topologies aplicadas. |
| 1.6 | Métricas | DORA metrics (Deployment Frequency, Lead Time, MTTR, Change Failure Rate). |

**Práctica:** Diseñar la propuesta de IDP para una empresa ficticia, identificando golden paths, equipos y métricas objetivo.

---

### Módulo 2 — Programación para DevOps (6 ECTS)

**Objetivo:** Dotar al alumno de las competencias de programación necesarias para automatizar, extender y operar infraestructura.

#### Bloque A — Bash (2 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 2.1 | Fundamentos de shell | Variables, control de flujo, funciones, exit codes. |
| 2.2 | Procesamiento de texto | grep, sed, awk, jq, yq. Pipes y redirecciones. |
| 2.3 | Scripting avanzado | Traps, señales, subshells, process substitution. |
| 2.4 | Automatización | Cron, systemd timers, scripts de bootstrap, Makefiles. |

**Práctica:** Crear un toolkit de scripts Bash para provisionar y validar un entorno de desarrollo local.

#### Bloque B — Python (2 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 2.5 | Python para infraestructura | Tipos, estructuras de datos, módulos, entornos virtuales. |
| 2.6 | Librerías clave | requests, boto3, google-cloud-*, azure-sdk, paramiko. |
| 2.7 | CLI tools | Click / Typer para construir herramientas de línea de comandos. |
| 2.8 | Testing y calidad | pytest, linting (ruff), type checking (mypy). |

**Práctica:** Desarrollar una CLI en Python que inventaríe recursos cloud en múltiples proveedores.

#### Bloque C — Go (2 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 2.9  | Fundamentos de Go | Tipos, structs, interfaces, goroutines, channels. |
| 2.10 | Go para Cloud Native | HTTP servers, client-go, controller-runtime. |
| 2.11 | Tooling | go test, go vet, golangci-lint, goreleaser. |
| 2.12 | Patrones comunes | CLI con cobra, configuración con viper, logging estructurado. |

**Práctica:** Construir una herramienta CLI en Go que interactúe con la API de Kubernetes.

---

### Módulo 3 — Redes: DNS y CDNs (3 ECTS)

**Objetivo:** Reforzar los conceptos de red imprescindibles para operar servicios en la nube.

| # | Tema | Contenido |
|---|------|-----------|
| 3.1 | Modelo TCP/IP | Repaso de capas, protocolos clave (TCP, UDP, HTTP/1.1, HTTP/2, HTTP/3, gRPC). |
| 3.2 | DNS en profundidad | Jerarquía DNS, tipos de registro (A, AAAA, CNAME, MX, TXT, SRV, NS). Resolución recursiva vs iterativa. TTLs. |
| 3.3 | DNS avanzado | DNSSEC, DNS-over-HTTPS, split-horizon DNS, service discovery basado en DNS. |
| 3.4 | CDNs: conceptos | Caché en el edge, invalidación, origin shield, anycast. |
| 3.5 | Cloudflare | DNS autoritativo, proxy y WAF, Workers, R2, Zero Trust tunnels, Argo Smart Routing. |
| 3.6 | Integración con Kubernetes | ExternalDNS como adelanto, cert-manager y DNS-01 challenge. |

**Práctica:** Configurar un dominio en Cloudflare con DNS, WAF rules, Page Rules y un Worker edge-side.

---

### Módulo 4 — Control de Versiones con Git (3 ECTS)

**Objetivo:** Dominar Git como herramienta fundamental para la colaboración y la entrega continua.

| # | Tema | Contenido |
|---|------|-----------|
| 4.1 | Internals de Git | Objetos (blob, tree, commit, tag), DAG, reflog, packfiles. |
| 4.2 | Flujos de colaboración | Git Flow, GitHub Flow, Trunk-Based Development. Pros y contras. |
| 4.3 | Operativa diaria | Staging area, stash, cherry-pick, bisect. |
| 4.4 | Rebase | Interactive rebase, fixup, autosquash. Rebase vs merge: cuándo usar cada uno. |
| 4.5 | Resolución de conflictos | Estrategias de merge (recursive, ort), rerere, herramientas visuales (meld, difftool). |
| 4.6 | Gestión de ramas | Protección de ramas, CODEOWNERS, signed commits, hooks (pre-commit, commit-msg). |
| 4.7 | Monorepos y submódulos | Git submodules, git subtree, herramientas monorepo (nx, turborepo). |

**Práctica:** Simular un ciclo completo de desarrollo en equipo: feature branches, code review, resolución de conflictos, rebase interactivo y release tagging.

---

### Módulo 5 — Cloud Computing: Azure, AWS y GCP (8 ECTS)

**Objetivo:** Conocer los recursos fundamentales de los tres grandes proveedores cloud.

#### Bloque A — Introducción a AWS (3 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 5.1 | Conceptos base | Regiones, AZs, ARNs, IAM (users, roles, policies, OIDC federation). |
| 5.2 | Cómputo | EC2 (instance types, AMIs, user-data), Auto Scaling Groups, Lambda. |
| 5.3 | Almacenamiento | S3 (buckets, lifecycle, versioning), EBS, EFS. |
| 5.4 | Networking | VPC, subnets, route tables, IGW, NAT Gateway, Security Groups, NACLs. |
| 5.5 | Servicios gestionados | RDS, DynamoDB, SQS, SNS, CloudWatch, Route 53. |
| 5.6 | Contenedores en AWS | ECR, ECS (Fargate), introducción a EKS. |

#### Bloque B — Introducción a Azure (3 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 5.7  | Conceptos base | Subscriptions, Resource Groups, RBAC, Azure AD / Entra ID. |
| 5.8  | Cómputo | Virtual Machines, VM Scale Sets, Azure Functions. |
| 5.9  | Almacenamiento | Blob Storage, Azure Files, Managed Disks. |
| 5.10 | Networking | VNets, Subnets, NSGs, Azure Load Balancer, Application Gateway. |
| 5.11 | Servicios gestionados | Azure SQL, Cosmos DB, Service Bus, Azure Monitor. |
| 5.12 | Contenedores en Azure | ACR, ACI, introducción a AKS. |

#### Bloque C — Introducción a GCP (2 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 5.13 | Conceptos base | Projects, folders, organizations, IAM, service accounts. |
| 5.14 | Cómputo y almacenamiento | Compute Engine, Cloud Functions, Cloud Storage, Persistent Disks. |
| 5.15 | Networking | VPC, firewall rules, Cloud NAT, Cloud Load Balancing. |
| 5.16 | Servicios gestionados | Cloud SQL, Firestore, Pub/Sub, Cloud Monitoring, Cloud DNS. |
| 5.17 | Contenedores en GCP | Artifact Registry, Cloud Run, introducción a GKE. |

**Práctica:** Desplegar la misma aplicación web de referencia (3-tier) en los tres proveedores usando sus respectivas consolas y CLIs.

---

### Módulo 6 — Infraestructura como Código con Terraform (5 ECTS)

**Objetivo:** Dominar Terraform como herramienta central de aprovisionamiento multi-cloud.

| # | Tema | Contenido |
|---|------|-----------|
| 6.1 | Fundamentos | HCL, providers, resources, data sources, variables, outputs. |
| 6.2 | State | Local vs remote state, state locking, backends (S3, GCS, Azure Blob). |
| 6.3 | Módulos | Estructura de módulos, registry público, módulos internos, versionado. |
| 6.4 | Patrones avanzados | for_each, dynamic blocks, moved blocks, import, workspaces. |
| 6.5 | Testing y calidad | terraform validate, tflint, checkov, OPA/Conftest, terraform test. |
| 6.6 | CI/CD para Terraform | Atlantis, Terraform Cloud/Enterprise, GitHub Actions pipelines. |
| 6.7 | Multi-cloud con Terraform | Proveedores AWS + Azure + GCP en el mismo proyecto, gestión de providers. |
| 6.8 | OpenTofu | Contexto del fork, diferencias y compatibilidad. |

**Práctica:** Crear módulos Terraform reutilizables para aprovisionar la infraestructura base (VPC/VNet, subnets, IAM) en AWS, Azure y GCP. Pipeline CI/CD con validación automática.

---

## Semestre 2: Contenedores, Kubernetes y Ecosistema Cloud Native

---

### Módulo 7 — Contenedores (4 ECTS)

**Objetivo:** Comprender la tecnología de contenedores como base para Kubernetes.

| # | Tema | Contenido |
|---|------|-----------|
| 7.1 | Fundamentos Linux | Namespaces, cgroups, capabilities, seccomp, chroot. |
| 7.2 | Docker | Dockerfile, multi-stage builds, layer caching, build args, .dockerignore. |
| 7.3 | Imágenes | OCI image spec, distroless, scratch, alpine. Scanning con trivy/grype. |
| 7.4 | Container runtimes | containerd, CRI-O, runc, gVisor, Kata Containers. |
| 7.5 | Registries | Docker Hub, Harbor, cloud registries (ECR, ACR, GAR). |
| 7.6 | Buildkit y alternativas | Buildx, Kaniko, ko (para Go), Buildpacks. |
| 7.7 | Compose y entornos locales | Docker Compose para desarrollo, Podman como alternativa. |

**Práctica:** Containerizar una aplicación multi-servicio (frontend + API + worker + DB), optimizar imágenes, escanear vulnerabilidades y publicar en un registry.

---

### Módulo 8 — Kubernetes Core (10 ECTS)

**Objetivo:** Dominar los conceptos fundamentales y la arquitectura de Kubernetes.

#### Bloque A — Fundamentos (3 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 8.1 | Introducción y arquitectura | Historia, CNCF, arquitectura: control plane (API server, etcd, scheduler, controller-manager) y data plane (kubelet, kube-proxy, container runtime). |
| 8.2 | Clusters locales con kind | Instalación, configuración multi-nodo, port mappings, integración con registries locales. |
| 8.3 | Building blocks: Workloads | Pod, ReplicaSet, Deployment, DaemonSet, StatefulSet, Job, CronJob. |
| 8.4 | Building blocks: Config | ConfigMap, Secret, ServiceAccount, ResourceQuotas, LimitRanges. |
| 8.5 | Building blocks: Otros | Namespace, Labels, Selectors, Annotations, Finalizers, OwnerReferences. |

#### Bloque B — Almacenamiento (1 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 8.6 | Modelo de storage | PersistentVolume, PersistentVolumeClaim, StorageClass. |
| 8.7 | CSI drivers | Concepto, drivers comunes (EBS CSI, Azure Disk, GCE PD). |
| 8.8 | Patrones | EmptyDir, hostPath, volume snapshots, volume expansion, volume cloning. |

#### Bloque C — Aplicaciones (1 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 8.9  | Lifecycle | Probes (liveness, readiness, startup), init containers, sidecar containers. |
| 8.10 | Scheduling | Node selectors, affinity/anti-affinity, taints and tolerations, topology spread. |
| 8.11 | Gestión de recursos | Requests, limits, QoS classes, PriorityClasses, Pod Disruption Budgets. |

#### Bloque D — Networking (2 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 8.12 | Modelo de red | Pod networking, CNI plugins (Calico, Cilium, Flannel), Pod CIDR. |
| 8.13 | Services | ClusterIP, NodePort, LoadBalancer, ExternalName, Headless Services. |
| 8.14 | Ingress y Gateway API | Ingress controllers, IngressClass, Gateway API (HTTPRoute, GRPCRoute). |
| 8.15 | Network Policies | Ingress/egress rules, default deny, herramientas de visualización. |
| 8.16 | DNS interno | CoreDNS, resolución de servicios, custom DNS entries, stub domains. |

#### Bloque E — Autenticación y Autorización (1 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 8.17 | Authentication | X.509 certificates, OIDC, webhook token auth, service account tokens (bound). |
| 8.18 | Authorization | RBAC (Role, ClusterRole, RoleBinding, ClusterRoleBinding), ABAC, webhook. |
| 8.19 | Admission controllers | Validating, mutating, OPA Gatekeeper, Kyverno. |

#### Bloque F — Cluster local componente a componente (2 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 8.20 | Construir un cluster desde cero | Levantar etcd manualmente, configurar kube-apiserver, scheduler, controller-manager. |
| 8.21 | Nodos worker | Configurar kubelet, container runtime, kube-proxy. |
| 8.22 | Certificados | PKI del cluster, generación y rotación de certificados con cfssl/openssl. |
| 8.23 | Bootstrapping | kubeadm bajo el capó, token-based discovery, TLS bootstrapping. |
| 8.24 | Debugging del cluster | Logs de componentes, audit logging, kubectl debug, ephemeral containers. |

**Práctica del módulo:** (1) Desplegar la aplicación multi-servicio del Módulo 7 en kind con storage, networking, RBAC y policies. (2) Construir un cluster Kubernetes "the hard way" componente a componente.

---

### Módulo 9 — Kubernetes en Cloud Providers (4 ECTS)

**Objetivo:** Operar clústeres Kubernetes gestionados en los principales proveedores cloud y entender las diferencias.

| # | Tema | Contenido |
|---|------|-----------|
| 9.1 | EKS (AWS) | Arquitectura EKS, node groups (managed, self-managed, Fargate), IRSA, EBS CSI, ALB Ingress Controller, VPC CNI. |
| 9.2 | GKE (GCP) | Arquitectura GKE, Autopilot vs Standard, Workload Identity, GCE PD CSI, Gateway API nativo, Config Connector. |
| 9.3 | AKS (Azure) | Arquitectura AKS, node pools, Workload Identity, Azure Disk/File CSI, AGIC, Azure CNI overlay. |
| 9.4 | Otros clouds | DOKS (DigitalOcean), OKE (Oracle), LKE (Linode/Akamai), OVHcloud Kubernetes. Clusters en bare metal con Talos/Flatcar. |
| 9.5 | Aprovisionamiento IaC | Terraform modules para EKS, GKE y AKS. Comparativa de configuraciones. |
| 9.6 | Comparativa cross-cloud | Tabla de equivalencias: networking, storage, identity, add-ons. Trade-offs entre proveedores. |

**Práctica:** Aprovisionar clusters EKS, GKE y AKS con Terraform y desplegar la misma aplicación en los tres, comparando comportamiento, rendimiento y coste.

---

### Módulo 10 — Ecosistema Cloud Native: IaC, Secrets y Observabilidad (8 ECTS)

**Objetivo:** Integrar las herramientas del ecosistema CNCF para gestionar infraestructura, secretos y observabilidad de forma declarativa.

#### Bloque A — Application Bundles y Operators (1 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 10.1 | Helm | Charts, values, templates, hooks, repositorios, helm-secrets. |
| 10.2 | Kustomize | Overlays, patches, components, generators. Helm + Kustomize. |
| 10.3 | Kubernetes Operators overview | Patrón operator, CRDs, controller loop, Operator Hub, niveles de madurez. |

#### Bloque B — Infraestructura declarativa en Kubernetes (2 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 10.4 | ExternalDNS | Arquitectura, providers soportados (Cloudflare, Route53, Cloud DNS), sincronización automática de registros DNS. |
| 10.5 | cert-manager y Let's Encrypt | Issuers, ClusterIssuers, ACME protocol, DNS-01 vs HTTP-01 challenges, renovación automática. |
| 10.6 | Crossplane | Arquitectura, Providers, Managed Resources, Compositions, XRDs. Comparativa con Terraform. |
| 10.7 | Crossplane avanzado | Composition Functions, EnvironmentConfigs, Usage tracking, integración con ArgoCD. |

#### Bloque C — Secret Management (1.5 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 10.8 | HashiCorp Vault | Arquitectura (seal/unseal, storage backend), secret engines (KV, PKI, AWS, database). Auth methods. |
| 10.9 | Vault en Kubernetes | Vault Agent Injector, CSI driver, Vault Secrets Operator. HA deployment. |
| 10.10 | External Secrets Operator | Arquitectura, SecretStore, ClusterSecretStore, ExternalSecret. Providers: Vault, AWS SM, Azure KV, GCP SM. |
| 10.11 | Estrategias combinadas | Vault como backend central + ESO como sincronizador. Rotación automática de secretos. |

#### Bloque D — Observabilidad (3.5 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 10.12 | Los tres pilares | Métricas, logs, trazas. Correlación entre señales. |
| 10.13 | Prometheus | Arquitectura (server, alertmanager, pushgateway), PromQL, service discovery, ServiceMonitor/PodMonitor con Prometheus Operator. |
| 10.14 | Prometheus avanzado | Recording rules, alerting rules, Thanos/Cortex para long-term storage y HA, federation. |
| 10.15 | Grafana | Datasources, dashboards (JSON model), variables, alerting, Grafana as Code (grafonnet, Terraform provider). |
| 10.16 | Grafana stack | Loki (logs), Tempo (trazas), Mimir (métricas), Alloy (collector). |
| 10.17 | OpenTelemetry | Especificación, SDK, OpenTelemetry Collector (receivers, processors, exporters), auto-instrumentación en Kubernetes. |
| 10.18 | Observabilidad end-to-end | Instrumentar la aplicación de referencia: métricas custom, trazas distribuidas, logs estructurados, dashboards y alertas. |

**Práctica:** Desplegar el stack completo de observabilidad (Prometheus + Grafana + Loki + Tempo + OTel Collector), configurar ExternalDNS + cert-manager + Vault + ESO, y demostrar el flujo completo desde código hasta dashboards.

---

### Módulo 11 — GitOps, CI/CD y Networking Avanzado (7 ECTS)

**Objetivo:** Implementar pipelines de entrega continua y networking avanzado siguiendo principios GitOps.

#### Bloque A — GitOps (2.5 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 11.1 | Principios GitOps | Declarativo, versionado, automatizado, reconciliado. Pull vs Push model. |
| 11.2 | ArgoCD | Arquitectura, Application, ApplicationSet, Projects, sync policies, waves, hooks. |
| 11.3 | ArgoCD avanzado | Multi-tenancy, SSO/RBAC, App of Apps, ApplicationSet generators, notifications. |
| 11.4 | Prow | Arquitectura, plugins, Tide (merge automation), Deck (dashboard), ProwJobs. Uso en el ecosistema Kubernetes. |
| 11.5 | Tekton | Pipelines, Tasks, TaskRuns, PipelineRuns, Triggers, Results, Workspaces. Tekton Chains para supply chain security. |

#### Bloque B — Networking Avanzado (2 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 11.6 | Traefik | IngressRoute CRD, middleware (rate limiting, auth, headers), Let's Encrypt integration, dashboard. |
| 11.7 | Traefik avanzado | TCP/UDP routing, canary con TraefikService, métricas y trazas, Traefik Hub. |
| 11.8 | Istio: fundamentos | Service mesh, arquitectura (istiod, Envoy sidecar), Ambient mode (ztunnel). |
| 11.9 | Istio: traffic management | VirtualService, DestinationRule, Gateway, traffic shifting, fault injection, circuit breaker. |
| 11.10 | Istio: seguridad y observabilidad | mTLS automático, AuthorizationPolicy, PeerAuthentication, Kiali, telemetría integrada. |

#### Bloque C — Deployment Strategies (1.5 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 11.11 | Estrategias de despliegue | Rolling update, blue/green, canary, A/B testing. Comparativa de trade-offs. |
| 11.12 | Argo Rollouts | Rollout resource, canary con análisis automatizado, blue-green, integración con Istio/Traefik y Prometheus. |
| 11.13 | Progressive delivery | Feature flags (Flagger), métricas de negocio como gates, rollback automático. |

#### Bloque D — Scaling (1 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 11.14 | Horizontal Pod Autoscaler | Métricas CPU/memory, custom metrics (Prometheus Adapter), scaling behavior. |
| 11.15 | Vertical Pod Autoscaler | Modes (Off, Initial, Auto), recomendaciones, limitaciones. |
| 11.16 | Cluster Autoscaler | Arquitectura, node pools, scale-from-zero, over-provisioning. |
| 11.17 | KEDA | Event-driven autoscaling, ScaledObject, ScaledJob, scalers (Kafka, SQS, Prometheus, cron). |

**Práctica:** Implementar un pipeline GitOps completo: Tekton build → imagen a registry → ArgoCD sync → canary deploy con Argo Rollouts + Istio + análisis Prometheus → auto-rollback.

---

### Módulo 12 — Kubernetes Avanzado y Multi-Cluster (5 ECTS)

**Objetivo:** Abordar los patrones avanzados de operación, extensión y gestión multi-cluster/multi-cloud.

#### Bloque A — Operators (1.5 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 12.1 | Diseño de operators | CRD design, API versioning, status subresource, printer columns. |
| 12.2 | Kubebuilder / Operator SDK | Scaffolding, controller-runtime, reconciliation loop, predicates, indexers. |
| 12.3 | Testing y operativa | envtest, e2e testing, OLM (Operator Lifecycle Manager), publicación en OperatorHub. |

#### Bloque B — Cluster Management (1 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 12.4 | Cluster lifecycle | Cluster API (CAPI), providers (AWS, Azure, GCP, vSphere), ClusterClass. |
| 12.5 | Serverless Kubernetes | AWS Fargate en EKS, GKE Autopilot, Azure Container Apps, Virtual Kubelet. |
| 12.6 | Hosted Control Planes | Concepto, HyperShift (OpenShift), vCluster, Kamaji, EKS Anywhere. |

#### Bloque C — Multi-Cluster y Multi-Cloud (2.5 ECTS)

| # | Tema | Contenido |
|---|------|-----------|
| 12.7 | Multi-cluster management | Cluster API fleet, Rancher, GKE Fleet, ArgoCD multi-cluster, Karmada. |
| 12.8 | Multi-cluster deployments | Federación de workloads, Submariner para networking cross-cluster, Liqo. |
| 12.9 | Multi-cloud deployments | Patrones de abstracción, Crossplane como plano de control universal, policy engines para consistencia. |
| 12.10 | Service mesh multi-cluster | Istio multi-cluster (primary-remote, multi-primary), Cilium Cluster Mesh. |
| 12.11 | Observabilidad multi-cluster | Thanos para métricas federadas, Grafana Cloud, OpenTelemetry Collector como gateway centralizado. |
| 12.12 | Disaster recovery | Velero backup/restore, etcd backup strategies, RPO/RTO planning, failover automatizado cross-region/cross-cloud. |

**Práctica:** Desplegar una arquitectura multi-cluster (2 proveedores cloud), con networking cross-cluster (Submariner o Cilium Mesh), federación de workloads, observabilidad centralizada y failover automático.

---

## Proyecto Final de Postgrado (6 ECTS)

### Descripción

Diseño, implementación y defensa de una plataforma cloud native completa que integre los conocimientos adquiridos a lo largo del postgrado.

### Requisitos mínimos

| Área | Requisito |
|------|-----------|
| Infraestructura | Aprovisionada con Terraform en al menos 2 cloud providers |
| Kubernetes | Clusters gestionados (EKS/GKE/AKS) con configuración production-ready |
| GitOps | ArgoCD gestionando todos los manifiestos del cluster |
| CI/CD | Pipeline completo con Tekton (build, test, scan, deploy) |
| Networking | Ingress/Gateway API + service mesh + ExternalDNS + TLS automático |
| Secretos | Vault + External Secrets Operator |
| Observabilidad | Stack completo (métricas, logs, trazas) con dashboards y alertas |
| Seguridad | RBAC, Network Policies, Admission Policies, image scanning |
| Scaling | Al menos HPA + Cluster Autoscaler configurados |
| Documentación | Arquitectura, decisiones técnicas (ADRs), runbooks operacionales |

### Entregables

1. **Repositorio Git** con todo el código (IaC, manifiestos, configuración, pipelines)
2. **Memoria técnica** (30-50 páginas): arquitectura, decisiones, diagrama de componentes, lecciones aprendidas
3. **Demo en vivo** (30 min): despliegue end-to-end, escenario de fallo y recuperación, observabilidad
4. **Defensa oral** (15 min): preguntas del tribunal

---

## Mapa de Dependencias entre Módulos

```
M1 (DevOps) ──────────────────────────────────────────────────┐
M2 (Programación) ─────────────────────────────────┐          │
M3 (DNS/CDN) ──────────────────────────────┐       │          │
M4 (Git) ──────────────────────────────┐   │       │          │
M5 (Cloud Providers) ──────────┐       │   │       │          │
M6 (Terraform) ─────────┐      │       │   │       │          │
                         ▼      ▼       ▼   ▼       ▼          ▼
                      M7 (Contenedores)                        │
                         │                                     │
                         ▼                                     │
                      M8 (K8s Core) ◄──────────────────────────┘
                         │
                    ┌────┼────┐
                    ▼    ▼    ▼
                  M9   M10   M11
                 (Cloud)(Eco) (GitOps)
                    │    │     │
                    └────┼─────┘
                         ▼
                  M12 (Avanzado)
                         │
                         ▼
                  Proyecto Final
```

---

## Bibliografía y Recursos de Referencia

| Recurso | Tipo |
|---------|------|
| *Kubernetes in Action* — Marko Lukša | Libro |
| *The Phoenix Project* — Kim, Behr, Spafford | Libro |
| *Team Topologies* — Skelton, Pais | Libro |
| *Terraform: Up & Running* — Yevgeniy Brikman | Libro |
| *Programming Kubernetes* — Hausenblas, Schimanski | Libro |
| *Istio in Action* — Posta, Maloku | Libro |
| *Observability Engineering* — Majors, Fong-Jones, Miranda | Libro |
| *Cloud Native DevOps with Kubernetes* — Arundel, Domingus | Libro |
| kubernetes.io/docs | Documentación oficial |
| cncf.io/projects | Landscape CNCF |
| learn.hashicorp.com | Tutoriales Terraform/Vault |
| prometheus.io/docs | Documentación Prometheus |
| argoproj.github.io | Documentación Argo (CD, Rollouts, Workflows) |
