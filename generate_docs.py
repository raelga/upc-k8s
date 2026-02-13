#!/usr/bin/env python3
"""Generate the Postgrado Kubernetes .docx and .xlsx files."""

from docx import Document
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import os

# ============================================================
# DATA: 40 sessions, 3.5h each, 140h total
# ============================================================

MODULES = [
    {
        "id": "M01",
        "title": "Fundamentos de DevOps y Platform Engineering",
        "hours": 3.5,
        "sessions": 1,
        "block": "BLOQUE I",
        "block_title": "Fundamentos y Cultura DevOps",
        "description": (
            "Contextualización histórica, filosófica y organizativa del movimiento DevOps "
            "y su evolución hacia Platform Engineering como disciplina."
        ),
        "topics": [
            "Historia y principios DevOps: de Waterfall a Agile a DevOps. Cultura, automatización, medición y compartición (CALMS)",
            "Prácticas clave: CI/CD, Infrastructure as Code, Monitoring, Incident Management, Blameless Postmortems",
            "El problema de escala de DevOps: de equipos pequeños a grandes organizaciones de ingeniería",
            "Platform Engineering: definición, diferencias con DevOps y SRE, y casos de adopción real",
            "Internal Developer Platforms (IDP): concepto, golden paths, ciclo de vida y Developer Experience (DevEx)",
            "Team Topologies: stream-aligned, enabling, platform teams y complicated subsystem teams",
            "Métricas de éxito: DORA metrics (Deployment Frequency, Lead Time, MTTR, Change Failure Rate) y framework SPACE",
            "Backstage como portal de desarrollo interno: plugins, TechDocs y Software Catalog",
            "El rol del Platform Engineer: responsabilidades, skills T-shaped y evolución de carrera",
        ],
        "session_detail": [
            ("Sesión 1", "DevOps y Platform Engineering", "3.5h",
             "Historia DevOps, CALMS, prácticas CI/CD e IaC. Platform Engineering: IDP, golden paths, "
             "Team Topologies, DORA metrics. Backstage como portal interno."),
        ],
    },
    {
        "id": "M02",
        "title": "Programación para DevOps: Go, Python y Bash",
        "hours": 7,
        "sessions": 2,
        "block": None,
        "description": (
            "Bases de programación orientadas a la automatización de infraestructura "
            "y desarrollo de herramientas de plataforma."
        ),
        "topics": [
            "Bash scripting avanzado: variables, estructuras de control, funciones, arrays y manejo de errores",
            "Automatización de sistema: gestión de procesos, pipes, redirecciones, grep/sed/awk/jq/yq, cron y Makefiles",
            "Python para DevOps: scripting, SDKs cloud (boto3, azure-sdk, google-cloud) y manejo de APIs REST",
            "Python: manipulación de YAML/JSON/TOML, Jinja2 templating, CLIs con Click/Typer y testing con pytest",
            "Go: sintaxis, tipos, structs, interfaces, goroutines, channels y manejo de errores idiomático",
            "Go para infraestructura: desarrollo de CLIs con cobra/viper y cliente Kubernetes (client-go)",
            "Patrones de desarrollo de controladores y operators en Go: reconciliation loop e informers",
            "Testing en Go: unit tests, table-driven tests, mocks con testify e integración con CI",
            "Herramientas de desarrollo: Makefile, direnv, pre-commit hooks y linters (golangci-lint, ruff)",
        ],
        "session_detail": [
            ("Sesión 2", "Bash y Python para DevOps", "3.5h",
             "Bash: variables, control de flujo, funciones, pipes, grep/sed/awk/jq. "
             "Python: scripting, SDKs cloud, CLIs con Click/Typer, pytest, ruff."),
            ("Sesión 3", "Go para Cloud Native", "3.5h",
             "Fundamentos Go: tipos, structs, interfaces, goroutines, channels. "
             "CLIs con cobra/viper, client-go, controller-runtime. Testing y golangci-lint."),
        ],
    },
    {
        "id": "M03",
        "title": "Redes, DNS y CDN con Cloudflare",
        "hours": 3.5,
        "sessions": 1,
        "block": None,
        "description": (
            "Fundamentos de red aplicados a entornos cloud y distribuidos, "
            "con Cloudflare como plataforma de referencia."
        ),
        "topics": [
            "Revisión de fundamentos TCP/IP, UDP, TLS 1.3/mTLS, HTTP/2 y HTTP/3 (QUIC)",
            "DNS: resolución recursiva e iterativa, registros (A, AAAA, CNAME, TXT, SRV, NS), TTL y propagación",
            "DNS avanzado: DNSSEC, DNS-over-HTTPS, split-horizon DNS y service discovery basado en DNS",
            "CDN: arquitectura, edge caching, routing geográfico, invalidación y cache-control headers",
            "Cloudflare: DNS authoritative, Cloudflare Tunnel, Workers, WAF, DDoS protection y R2",
            "Certificados TLS: PKI, cadena de confianza, ACME protocol y automatización con Let's Encrypt",
            "Load balancing: algoritmos, health checks, session persistence y global load balancing",
        ],
        "session_detail": [
            ("Sesión 4", "DNS, CDNs y Cloudflare", "3.5h",
             "TCP/IP, DNS en profundidad (registros, resolución, DNSSEC). CDNs: edge caching, anycast. "
             "Cloudflare: DNS autoritativo, proxy, WAF, Workers, R2, Tunnels. TLS y ACME."),
        ],
    },
    {
        "id": "M04",
        "title": "Control de Versiones Avanzado con Git",
        "hours": 3.5,
        "sessions": 1,
        "block": "BLOQUE II",
        "block_title": "Infraestructura y Colaboración",
        "description": (
            "Dominio profundo de Git como herramienta colaborativa "
            "en equipos de alto rendimiento."
        ),
        "topics": [
            "Arquitectura interna de Git: objects (blob, tree, commit, tag), refs, packfiles, reflog y garbage collection",
            "Estrategias de branching: Git Flow, GitHub Flow, trunk-based development y comparativa práctica",
            "Rebases interactivos: squash, fixup, reword, edit y reordenación de commits",
            "Resolución de conflictos: estrategias de merge (recursive, ort), rerere, git mergetool y best practices",
            "Gestión de ramas: naming conventions, branch protection rules, CODEOWNERS y cleanup automático",
            "Pull Requests y code review: merge strategies (merge, squash, rebase), signed commits y draft PRs",
            "Git hooks: pre-commit, commit-msg, post-merge y automatización con pre-commit framework",
            "Monorepos: estrategias, herramientas (Nx, Turborepo) y gestión de dependencias",
            "Operaciones avanzadas: git bisect, git worktree, submodules, subtrees y sparse-checkout",
        ],
        "session_detail": [
            ("Sesión 5", "Git avanzado", "3.5h",
             "Internals de Git: objects, DAG, reflog. Flujos: Git Flow, GitHub Flow, trunk-based. "
             "Rebase interactivo, resolución de conflictos, CODEOWNERS, hooks, monorepos."),
        ],
    },
    {
        "id": "M05",
        "title": "Cloud Computing: AWS, Azure y GCP",
        "hours": 10.5,
        "sessions": 3,
        "block": "BLOQUE III",
        "block_title": "Cloud Computing",
        "description": (
            "Introducción práctica a los tres grandes proveedores cloud con foco en los recursos "
            "necesarios para Kubernetes."
        ),
        "topics": [
            "AWS · IAM: users, roles, policies, OIDC federation, IRSA y AWS SSO",
            "AWS · Computación: EC2 (instance types, AMIs, user-data), Auto Scaling Groups, Lambda",
            "AWS · Redes: VPC, subnets públicas/privadas, Security Groups, ALB/NLB, Route 53 y PrivateLink",
            "AWS · Almacenamiento: S3 (lifecycle, versioning), EBS, EFS y ECR",
            "AWS · Servicios gestionados: RDS, DynamoDB, SQS, CloudWatch y Secrets Manager",
            "AZURE · IAM: Entra ID, Managed Identities, RBAC y Azure Key Vault",
            "AZURE · Computación: VMs, VMSS, Azure Functions y Azure Container Apps",
            "AZURE · Redes: VNet, subnets, NSG, Load Balancer, Application Gateway y Azure DNS",
            "AZURE · Almacenamiento: Blob Storage, Azure Files, Managed Disks y ACR",
            "AZURE · Servicios gestionados: Azure SQL, Cosmos DB, Service Bus y Azure Monitor",
            "GCP · IAM: Service Accounts, Workload Identity, org policies y Cloud Audit Logs",
            "GCP · Computación: Compute Engine, Cloud Functions y Cloud Run",
            "GCP · Redes: VPC, Firewall Rules, Cloud NAT, Cloud Load Balancing y Cloud DNS",
            "GCP · Almacenamiento: Cloud Storage, Persistent Disk y Artifact Registry",
            "GCP · Servicios gestionados: Cloud SQL, Firestore, Pub/Sub y Cloud Monitoring",
            "Comparativa multi-cloud: estrategias de portabilidad, vendor lock-in y abstracción de recursos",
        ],
        "session_detail": [
            ("Sesión 6", "Introducción a AWS", "3.5h",
             "IAM (users, roles, policies, OIDC). EC2, ASG, Lambda. VPC, subnets, SG, ALB. "
             "S3, EBS, EFS, ECR. RDS, DynamoDB, SQS, CloudWatch."),
            ("Sesión 7", "Introducción a Azure", "3.5h",
             "Entra ID, Managed Identities, RBAC. VMs, VMSS, Azure Functions. "
             "VNet, NSG, Load Balancer. Blob Storage, Azure Files, ACR. Azure SQL, Cosmos DB."),
            ("Sesión 8", "Introducción a GCP y comparativa multi-cloud", "3.5h",
             "Service Accounts, Workload Identity. Compute Engine, Cloud Functions, Cloud Run. "
             "VPC, Cloud NAT, Cloud LB. Cloud Storage, Artifact Registry. Cloud SQL, Pub/Sub. Comparativa."),
        ],
    },
    {
        "id": "M06",
        "title": "Infraestructura como Código con Terraform",
        "hours": 7,
        "sessions": 2,
        "block": None,
        "description": (
            "Diseño y operación de infraestructura declarativa multi-cloud con Terraform."
        ),
        "topics": [
            "Fundamentos de IaC: filosofía declarativa vs imperativa, idempotencia y drift detection",
            "HCL: sintaxis, tipos de datos, expresiones, funciones y meta-argumentos (count, for_each, depends_on)",
            "Providers: configuración, autenticación y uso de los providers de AWS, Azure y GCP",
            "State management: local vs remote state, state locking, backends (S3, GCS, Azure Blob) y workspaces",
            "Módulos: diseño, versionado, registro público y privado, composición y reusabilidad",
            "Patrones avanzados: for_each, dynamic blocks, moved blocks, import y workspaces",
            "Terraform en CI/CD: plan/apply automatizado, Atlantis y GitHub Actions",
            "Testing de infraestructura: terraform test, tflint, checkov, tfsec y políticas con OPA/Conftest",
            "Alternativas complementarias: OpenTofu, Pulumi y CDKTF",
        ],
        "session_detail": [
            ("Sesión 9", "Terraform: fundamentos y state", "3.5h",
             "IaC declarativa. HCL, providers, resources, data sources, variables, outputs. "
             "State: local vs remote, locking, backends. Módulos: estructura, versionado, registry."),
            ("Sesión 10", "Terraform: avanzado y CI/CD", "3.5h",
             "for_each, dynamic blocks, moved blocks, import, workspaces. "
             "CI/CD: Atlantis, GitHub Actions. Testing: tflint, checkov, OPA. OpenTofu."),
        ],
    },
    {
        "id": "M07",
        "title": "Contenedores y Ecosistema OCI",
        "hours": 7,
        "sessions": 2,
        "block": "BLOQUE IV",
        "block_title": "Contenedores",
        "description": (
            "Dominio del ecosistema de contenedores: desde la construcción de imágenes "
            "hasta seguridad y registros."
        ),
        "topics": [
            "Arquitectura de contenedores: Linux namespaces, cgroups v2, UnionFS y el modelo de capas OCI",
            "Dockerfile avanzado: multi-stage builds, BuildKit, cache optimization y distroless/scratch images",
            "Container runtimes: Docker, containerd, CRI-O, runc, gVisor y la interfaz CRI de Kubernetes",
            "Docker Compose: definición de servicios multi-contenedor, redes, volúmenes y profiles",
            "Registros de imágenes: Docker Hub, GHCR, ECR, ACR, GAR y Harbor como registro privado",
            "Seguridad de imágenes: CVE scanning con Trivy/Grype, image signing con Cosign y generación de SBOM",
            "Builds in-cluster: kaniko, buildah y Paketo Buildpacks para entornos sin Docker daemon",
            "Optimización: reducción de tamaño, gestión de capas, secrets en build time y multi-platform builds",
            "OCI Artifacts: almacenamiento de Helm charts, políticas OPA y otros artefactos en registros OCI",
        ],
        "session_detail": [
            ("Sesión 11", "Contenedores: fundamentos y Docker", "3.5h",
             "Namespaces, cgroups, OCI. Dockerfile: multi-stage, BuildKit, cache. "
             "Runtimes: containerd, CRI-O, gVisor. Docker Compose. Podman."),
            ("Sesión 12", "Imágenes: seguridad, registries y builds", "3.5h",
             "Imágenes: distroless, scratch, alpine. Scanning: Trivy, Grype, Cosign, SBOM. "
             "Registries: Harbor, ECR, ACR, GAR. Kaniko, Buildpacks. OCI Artifacts."),
        ],
    },
    {
        "id": "M08",
        "title": "Kubernetes Core: Arquitectura y Building Blocks",
        "hours": 28,
        "sessions": 8,
        "block": "BLOQUE V",
        "block_title": "Kubernetes Core",
        "description": (
            "Estudio exhaustivo de la arquitectura de Kubernetes y sus objetos fundamentales."
        ),
        "topics": [
            "INTRODUCCIÓN · Control Plane: kube-apiserver, etcd, kube-scheduler, controller-manager, cloud-controller-manager",
            "INTRODUCCIÓN · Data Plane: kubelet, kube-proxy, container runtime y comunicación entre nodos",
            "CLUSTERS LOCALES · kind (Kubernetes in Docker): configuración multi-nodo, networking y uso en CI",
            "BUILDING BLOCKS · Pods: ciclo de vida, init containers, sidecar pattern y ephemeral containers",
            "BUILDING BLOCKS · Workloads: Deployment, StatefulSet, DaemonSet, Job, CronJob y ReplicaSet",
            "BUILDING BLOCKS · Configuración: ConfigMap, Secret (tipos, encriptación at rest), env vars y volúmenes",
            "BUILDING BLOCKS · Namespace, Labels, Selectors, Annotations, Finalizers y OwnerReferences",
            "BUILDING BLOCKS · Scheduling: node/pod affinity, taints, tolerations, topology spread y priority classes",
            "BUILDING BLOCKS · Resource management: requests, limits, LimitRange, ResourceQuota y QoS classes",
            "ALMACENAMIENTO · PersistentVolume, PersistentVolumeClaim, StorageClass y dynamic provisioning",
            "ALMACENAMIENTO · CSI: arquitectura, drivers (EBS, Azure Disk, GCE PD), volume snapshots y Velero",
            "ALMACENAMIENTO · Patrones: ReadWriteOnce vs ReadWriteMany, StatefulSet storage y volume cloning",
            "APLICACIONES · Probes (liveness/readiness/startup), init containers, sidecar containers y PodDisruptionBudgets",
            "APLICACIONES · Scheduling avanzado: node selectors, affinity/anti-affinity, topology spread constraints",
            "APLICACIONES · Rolling updates, rollbacks y ConfigMap/Secret reloading con Reloader",
            "NETWORKING · Services: ClusterIP, NodePort, LoadBalancer, ExternalName, Headless y EndpointSlices",
            "NETWORKING · Ingress: controllers, IngressClass, Gateway API (HTTPRoute, GRPCRoute)",
            "NETWORKING · CNI: Calico, Cilium, Flannel. NetworkPolicy y microsegmentación de tráfico",
            "NETWORKING · DNS interno: CoreDNS, resolución de servicios y customización de zonas",
            "AUTENTICACIÓN · RBAC: ServiceAccounts, Roles, ClusterRoles, Bindings y principio de mínimo privilegio",
            "AUTENTICACIÓN · Autenticación: certificados X.509, OIDC, webhook auth y bound SA tokens",
            "AUTENTICACIÓN · Admission controllers: validating/mutating webhooks, OPA Gatekeeper y Kyverno",
            "AUTENTICACIÓN · Pod Security Admission (PSA) y Pod Security Standards",
            "CLUSTER DESDE CERO · etcd: operaciones, snapshots, restore, clustering TLS y monitorización",
            "CLUSTER DESDE CERO · kube-apiserver, scheduler, controller-manager: configuración manual y flags",
            "CLUSTER DESDE CERO · kubelet, container runtime, kube-proxy: configuración y TLS bootstrapping",
            "CLUSTER DESDE CERO · PKI del cluster: generación de certificados con cfssl/openssl y rotación",
            "CLUSTER DESDE CERO · kubeadm bajo el capó, debugging: logs, kubectl debug, ephemeral containers",
        ],
        "session_detail": [
            ("Sesión 13", "Introducción y arquitectura de Kubernetes", "3.5h",
             "Historia, CNCF. Control plane: API server, etcd, scheduler, controller-manager. "
             "Data plane: kubelet, kube-proxy, CRI. Clusters locales con kind: multi-nodo, port mappings."),
            ("Sesión 14", "Building Blocks: Workloads", "3.5h",
             "Pod anatomy, ciclo de vida. ReplicaSet, Deployment (rolling update, rollback). "
             "DaemonSet, StatefulSet, Job, CronJob. Init containers, sidecar pattern."),
            ("Sesión 15", "Building Blocks: Configuración y organización", "3.5h",
             "ConfigMap, Secret (tipos, encriptación at rest). ServiceAccount. Namespaces, Labels, "
             "Selectors, Annotations, Finalizers, OwnerReferences. ResourceQuotas, LimitRanges."),
            ("Sesión 16", "Almacenamiento en Kubernetes", "3.5h",
             "PV, PVC, StorageClass, dynamic provisioning. CSI drivers (EBS, Azure Disk, GCE PD). "
             "EmptyDir, hostPath, volume snapshots, expansion, cloning. Velero backup."),
            ("Sesión 17", "Aplicaciones en Kubernetes", "3.5h",
             "Probes (liveness, readiness, startup). Scheduling: affinity/anti-affinity, taints, "
             "tolerations, topology spread. Requests, limits, QoS, PriorityClasses, PDBs. Reloader."),
            ("Sesión 18", "Networking en Kubernetes", "3.5h",
             "Modelo de red, CNI (Calico, Cilium, Flannel). Services: ClusterIP, NodePort, LoadBalancer, "
             "Headless, EndpointSlices. Ingress controllers, Gateway API. Network Policies. CoreDNS."),
            ("Sesión 19", "Autenticación y autorización", "3.5h",
             "RBAC: Role, ClusterRole, RoleBinding, ClusterRoleBinding, ServiceAccounts. "
             "Auth: X.509, OIDC, webhook, bound SA tokens. Admission controllers: Gatekeeper, Kyverno. PSA."),
            ("Sesión 20", "Cluster Kubernetes componente a componente", "3.5h",
             "Kubernetes 'the hard way': etcd manual, kube-apiserver, scheduler, controller-manager. "
             "kubelet, containerd, kube-proxy, TLS bootstrapping. PKI, cfssl. kubeadm. Debugging."),
        ],
    },
    {
        "id": "M09",
        "title": "Kubernetes en Producción: Multi-cloud",
        "hours": 7,
        "sessions": 2,
        "block": "BLOQUE VI",
        "block_title": "Kubernetes en Cloud",
        "description": (
            "Despliegue y operación de Kubernetes gestionado en los principales proveedores cloud "
            "y otros entornos."
        ),
        "topics": [
            "EKS (AWS): arquitectura, node groups (managed, self-managed, Fargate), eksctl",
            "EKS Add-ons: AWS Load Balancer Controller, EBS/EFS CSI, VPC CNI, ExternalDNS",
            "EKS Seguridad: IRSA, EKS Pod Identity, KMS encryption y audit logging",
            "GKE: Standard vs Autopilot, node pools, Workload Identity y VPC-native networking",
            "GKE Add-ons: Cloud Operations, Config Connector, GKE Gateway y Fleet Management",
            "AKS: arquitectura, AAD/Entra ID integration, Managed Identities y Azure CNI",
            "AKS Add-ons: Azure Monitor, CSI drivers (Disk/Files/Blob), AGIC y Azure Policy",
            "AKS Seguridad: Workload Identity, Azure Key Vault CSI Provider y Defender for Containers",
            "Otros clouds: OVHcloud, DigitalOcean DOKS, Scaleway, Linode LKE y Hetzner",
            "On-premises: k3s, k0s, Rancher, Tanzu y OpenShift",
            "Aprovisionamiento IaC: Terraform modules para EKS, GKE y AKS",
            "Comparativa multi-cloud: feature matrix, managed vs self-managed, pricing y criterios de selección",
        ],
        "session_detail": [
            ("Sesión 21", "Kubernetes en AWS (EKS) y GCP (GKE)", "3.5h",
             "EKS: arquitectura, node groups, Fargate, IRSA, EBS CSI, ALB Controller, VPC CNI. "
             "GKE: Autopilot vs Standard, Workload Identity, GKE Gateway, Fleet Management."),
            ("Sesión 22", "Kubernetes en Azure (AKS) y otros entornos", "3.5h",
             "AKS: node pools, Workload Identity, Azure CNI, AGIC. Defender for Containers. "
             "Otros: DOKS, LKE, OVHcloud, k3s, Talos. Terraform IaC para los tres. Comparativa."),
        ],
    },
    {
        "id": "M10",
        "title": "Ecosistema Cloud Native: Bundles, IaC, Secrets y Observabilidad",
        "hours": 24.5,
        "sessions": 7,
        "block": "BLOQUE VII",
        "block_title": "Ecosistema Cloud Native",
        "description": (
            "Herramientas del ecosistema CNCF para gestionar application bundles, infraestructura declarativa, "
            "secretos y observabilidad en Kubernetes."
        ),
        "topics": [
            "APPLICATION BUNDLES · Helm: charts, templates, values, hooks, repositorios, helm-secrets y helm-diff",
            "APPLICATION BUNDLES · Kustomize: bases, overlays, patches, generators y transformers. Helm + Kustomize",
            "OPERATORS OVERVIEW · Patrón Operator: CRDs, controller loop, Operator Lifecycle Manager, niveles de madurez",
            "OPERATORS OVERVIEW · Operators de referencia: cert-manager, Prometheus Operator, Strimzi, Crossplane",
            "INFRA AS CODE · ExternalDNS: providers (Route53, CloudDNS, Cloudflare), anotaciones y políticas de sync",
            "INFRA AS CODE · cert-manager: Issuers, ClusterIssuers, Let's Encrypt, ACME DNS-01/HTTP-01, renovación automática",
            "INFRA AS CODE · Crossplane: Providers, Managed Resources, Compositions, XRDs. Comparativa con Terraform",
            "INFRA AS CODE · Crossplane avanzado: Composition Functions, EnvironmentConfigs, integración con ArgoCD",
            "VAULT · Arquitectura: server, agents, backends de almacenamiento y alta disponibilidad",
            "VAULT · Auth methods en Kubernetes: Kubernetes Auth, JWT/OIDC, AppRole y cloud IAM",
            "VAULT · Secrets Engines: KV v1/v2, Dynamic Secrets (database, AWS, Azure), PKI y Transit",
            "VAULT · Vault Agent: auto-auth, template rendering, sidecar injection. Vault Secrets Operator (VSO)",
            "VAULT · Políticas (HCL), namespaces, auditing y disaster recovery con Raft integrated storage",
            "VAULT · Operaciones: inicialización, unseal, auto-unseal con KMS (AWS, Azure, GCP)",
            "EXTERNAL SECRETS · Arquitectura: ExternalSecret, SecretStore, ClusterSecretStore y refresh intervals",
            "EXTERNAL SECRETS · Providers: AWS Secrets Manager, Azure Key Vault, GCP Secret Manager y Vault",
            "EXTERNAL SECRETS · Patrones avanzados: secret templating, generators y pushSecret",
            "EXTERNAL SECRETS · Integración con GitOps: ArgoCD + ESO y gestión del ciclo de vida",
            "SECRET MANAGEMENT · Sealed Secrets, SOPS, comparativa de patrones por madurez",
            "OBSERVABILIDAD · Los tres pilares: métricas, logs, trazas. Correlación entre señales",
            "OBSERVABILIDAD · Prometheus: arquitectura, scraping, PromQL, service discovery, Alertmanager",
            "OBSERVABILIDAD · Prometheus Operator: ServiceMonitor, PodMonitor, recording rules, alerting rules. Thanos para HA",
            "OBSERVABILIDAD · Grafana: datasources, dashboards, variables, alerting. Grafana as Code (grafonnet, Terraform)",
            "OBSERVABILIDAD · Grafana stack: Loki (logs), Tempo (trazas), Mimir (métricas), Alloy (collector)",
            "OBSERVABILIDAD · OpenTelemetry: especificación OTLP, Collector pipelines, auto-instrumentación en Kubernetes",
            "OBSERVABILIDAD · Stack completo: Prometheus + Grafana + Loki + Tempo + OTel Collector integrados",
        ],
        "session_detail": [
            ("Sesión 23", "Application Bundles y Operators Overview", "3.5h",
             "Helm: charts, templates, values, hooks, repositorios. Kustomize: overlays, patches, generators. "
             "Helm + Kustomize. Patrón Operator, CRDs, controller loop, OLM, operators de referencia."),
            ("Sesión 24", "InfraAsCode: ExternalDNS, cert-manager y Crossplane", "3.5h",
             "ExternalDNS: providers, sincronización DNS. cert-manager: Issuers, Let's Encrypt, ACME. "
             "Crossplane: Providers, Managed Resources, Compositions, XRDs. Crossplane vs Terraform."),
            ("Sesión 25", "Vault: fundamentos y Kubernetes", "3.5h",
             "Vault: arquitectura, seal/unseal, storage backends, HA. Auth methods: K8s Auth, OIDC, AppRole. "
             "Secret engines: KV, Dynamic Secrets, PKI, Transit. Vault Agent y VSO en Kubernetes."),
            ("Sesión 26", "External Secrets y Secret Management", "3.5h",
             "ESO: SecretStore, ExternalSecret, providers (Vault, AWS SM, Azure KV, GCP SM). "
             "Templating, generators, pushSecret. Sealed Secrets, SOPS. Vault + ESO combinados. ArgoCD + ESO."),
            ("Sesión 27", "Prometheus y Alertmanager", "3.5h",
             "Tres pilares de observabilidad. Prometheus: arquitectura, scraping, PromQL, service discovery. "
             "Prometheus Operator: ServiceMonitor, PodMonitor. Recording rules, alerting rules. Thanos HA."),
            ("Sesión 28", "Grafana, Loki, Tempo y stack completo", "3.5h",
             "Grafana: datasources, dashboards, variables, alerting, Grafana as Code. "
             "Loki (logs), Tempo (trazas), Mimir (métricas), Alloy (collector). Stack integrado."),
            ("Sesión 29", "OpenTelemetry y observabilidad end-to-end", "3.5h",
             "OTel: especificación OTLP, SDK, Collector (receivers, processors, exporters). "
             "Auto-instrumentación en K8s. Lab: instrumentar aplicación con métricas, trazas, logs y dashboards."),
        ],
    },
    {
        "id": "M11",
        "title": "GitOps, Pipelines y Networking Avanzado",
        "hours": 21,
        "sessions": 6,
        "block": "BLOQUE VIII",
        "block_title": "GitOps, CI/CD y Networking",
        "description": (
            "Herramientas que conforman el ecosistema moderno de entrega continua "
            "y networking avanzado en Kubernetes."
        ),
        "topics": [
            "GITOPS · Principios GitOps: declarativo, versionado, automatizado, reconciliado. Pull vs Push model",
            "GITOPS · ArgoCD: Applications, AppProjects, ApplicationSets, sync policies, waves, hooks y RBAC",
            "GITOPS · ArgoCD avanzado: multi-tenancy, SSO, App of Apps, ApplicationSet generators y notifications",
            "GITOPS · ArgoCD Image Updater y Argo Rollouts: patrones de Progressive Delivery con análisis automático",
            "GITOPS · Prow: arquitectura CI nativa en Kubernetes, plugins, Tide, Deck dashboard y ProwJobs",
            "PIPELINES · Tekton: Tasks, Pipelines, PipelineRuns, Workspaces, Triggers y Tekton Chains",
            "PIPELINES · Integración Tekton + ArgoCD para workflows CI/CD end-to-end en Kubernetes",
            "NETWORKING · Traefik: IngressRoute CRDs, middlewares, TLS automático, dashboard y métricas",
            "NETWORKING · Traefik avanzado: TCP/UDP routing, rate limiting, circuit breaker, canary con TraefikService",
            "NETWORKING · Istio: arquitectura (Istiod + Envoy sidecars), mTLS automático y observabilidad integrada",
            "NETWORKING · Istio traffic: VirtualServices, DestinationRules, Gateways, traffic shifting, fault injection",
            "NETWORKING · Istio seguridad: AuthorizationPolicies, PeerAuthentication, circuit breaking, Kiali",
            "NETWORKING · Ambient Mesh (Istio): modo sin sidecar, ztunnel, waypoints y migración",
            "DEPLOYMENT · Estrategias: rolling update, blue/green, canary, A/B testing y trade-offs",
            "DEPLOYMENT · Argo Rollouts: canary con análisis automatizado, blue-green, integración Istio/Traefik + Prometheus",
            "DEPLOYMENT · Progressive delivery: Feature flags (Flagger/OpenFeature), métricas como gates, rollback automático",
            "SCALING · HPA: métricas CPU/memory, custom metrics (Prometheus Adapter), scaling behavior",
            "SCALING · VPA: modos (Off/Initial/Auto), recomendaciones y limitaciones",
            "SCALING · KEDA: ScaledObject, ScaledJob, triggers (Kafka, SQS, Prometheus, cron) y cooldown",
            "SCALING · Cluster Autoscaler vs Karpenter: node pools, scale-from-zero, cost optimization",
        ],
        "session_detail": [
            ("Sesión 30", "GitOps: principios y ArgoCD", "3.5h",
             "Principios GitOps: pull vs push. ArgoCD: arquitectura, Application, ApplicationSet, Projects, "
             "sync policies, waves, hooks, RBAC. App of Apps, SSO, notifications."),
            ("Sesión 31", "Prow, Tekton y pipelines CI/CD", "3.5h",
             "Prow: arquitectura, plugins, Tide, Deck, ProwJobs. "
             "Tekton: Tasks, Pipelines, Triggers, Workspaces, Tekton Chains. Integración Tekton + ArgoCD."),
            ("Sesión 32", "Networking: Traefik", "3.5h",
             "Traefik: IngressRoute CRD, middlewares (rate limiting, auth, headers), TLS automático. "
             "TCP/UDP routing, canary con TraefikService, métricas, trazas, dashboard."),
            ("Sesión 33", "Networking: Istio", "3.5h",
             "Service mesh: Istiod, Envoy sidecar, Ambient mode (ztunnel). "
             "VirtualService, DestinationRule, Gateway, traffic shifting, fault injection, circuit breaker. "
             "mTLS, AuthorizationPolicy, Kiali."),
            ("Sesión 34", "Estrategias de despliegue y Progressive Delivery", "3.5h",
             "Rolling, blue/green, canary, A/B. Argo Rollouts: canary con análisis Prometheus, blue-green. "
             "Progressive delivery: Flagger, OpenFeature, métricas como gates, rollback automático."),
            ("Sesión 35", "Scaling de workloads y clusters", "3.5h",
             "HPA: CPU/memory, custom metrics con Prometheus Adapter. VPA: modos y limitaciones. "
             "KEDA: event-driven, ScaledObject, triggers. Cluster Autoscaler vs Karpenter, cost optimization."),
        ],
    },
    {
        "id": "M12",
        "title": "Platform Engineering Avanzado: Operators, Serverless y Multi-cluster",
        "hours": 17.5,
        "sessions": 5,
        "block": "BLOQUE IX",
        "block_title": "Platform Engineering Avanzado",
        "description": (
            "Capacidades avanzadas de plataforma: construcción de operators, hosted control planes, "
            "serverless y despliegues multi-cluster/multi-cloud."
        ),
        "topics": [
            "BUILDING OPERATORS · Operator SDK (Go): scaffolding, CRD design, controller implementation y webhooks",
            "BUILDING OPERATORS · kubebuilder: reconciliation patterns, finalizers, status conditions y API versioning",
            "BUILDING OPERATORS · Operadores de producción: leader election, metrics, testing (envtest) y OLM",
            "CLUSTER MANAGEMENT · Cluster API (CAPI): arquitectura, providers (AWS/Azure/GCP), lifecycle y upgrades",
            "CLUSTER MANAGEMENT · Rancher Fleet y ArgoCD ApplicationSets para gestión de flotas de clusters",
            "CLUSTER MANAGEMENT · Upgrade strategies: rolling upgrades, ventanas de mantenimiento y node drain",
            "SERVERLESS · Knative Serving: auto-scaling a cero, revision routing y traffic splitting",
            "SERVERLESS · Virtual Kubelet: nodos virtuales con Fargate, ACI y Cloud Run",
            "HOSTED CONTROL PLANES · HyperShift (Red Hat): arquitectura, hosted clusters y node pools",
            "HOSTED CONTROL PLANES · vCluster: clusters virtuales ligeros, sincronización y multi-tenancy",
            "HOSTED CONTROL PLANES · Kamaji: tenant control planes, datastores y gestión de flota",
            "MULTI-CLUSTER MANAGEMENT · Arquitecturas: hub-and-spoke, peer-to-peer, federación",
            "MULTI-CLUSTER MANAGEMENT · Open Cluster Management (OCM), Rancher MCM y ArgoCD multicluster",
            "MULTI-CLUSTER DEPLOYMENTS · Istio multicluster (primary-remote, multi-primary)",
            "MULTI-CLUSTER DEPLOYMENTS · Cilium Cluster Mesh: tunneling, shared services y network policies globales",
            "MULTI-CLUSTER DEPLOYMENTS · Submariner: cross-cluster networking, service discovery y globalnet",
            "MULTI-CLOUD DEPLOYMENTS · Crossplane como plano de control universal, políticas OPA y ESO multi-cloud",
            "MULTI-CLOUD DEPLOYMENTS · Disaster Recovery: Velero, replicación de estado, RPO/RTO y failover automático",
        ],
        "session_detail": [
            ("Sesión 36", "Building Kubernetes Operators", "3.5h",
             "CRD design, API versioning, status subresource. Kubebuilder/Operator SDK: scaffolding, "
             "controller-runtime, reconciliation loop, predicates. Testing con envtest, OLM."),
            ("Sesión 37", "Cluster Management y Serverless", "3.5h",
             "Cluster API (CAPI): providers, ClusterClass, lifecycle. Rancher Fleet. "
             "Serverless: Knative Serving, Virtual Kubelet (Fargate, ACI). Upgrade strategies."),
            ("Sesión 38", "Hosted Control Planes", "3.5h",
             "HyperShift: arquitectura, hosted clusters. vCluster: clusters virtuales, multi-tenancy. "
             "Kamaji: tenant control planes, datastores. Comparativa de trade-offs."),
            ("Sesión 39", "Multi-cluster management y deployments", "3.5h",
             "Arquitecturas multi-cluster: hub-spoke, federación. OCM, Rancher MCM, ArgoCD multicluster. "
             "Istio multicluster, Cilium Cluster Mesh, Submariner."),
            ("Sesión 40", "Multi-cloud deployments y Disaster Recovery", "3.5h",
             "Crossplane multi-cloud, OPA policies, ESO multi-cloud. "
             "Velero backup/restore, replicación de estado, RPO/RTO, failover cross-region/cross-cloud. "
             "Proyecto Final: presentación de requisitos."),
        ],
    },
]

# ============================================================
# HELPER FUNCTIONS
# ============================================================

# Colors
COLOR_PRIMARY = RGBColor(0x1A, 0x56, 0xDB)  # Blue
COLOR_DARK = RGBColor(0x1F, 0x2A, 0x37)      # Dark gray
COLOR_MEDIUM = RGBColor(0x4B, 0x55, 0x63)     # Medium gray
COLOR_LIGHT_BG = "E8F0FE"                      # Light blue bg
COLOR_WHITE = "FFFFFF"
COLOR_HEADER_BG = "1A56DB"


def set_cell_shading(cell, color_hex):
    """Set background color of a table cell."""
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)


def add_table_borders(table):
    """Add borders to all cells in the table."""
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else parse_xml(f'<w:tblPr {nsdecls("w")}/>')
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        '  <w:top w:val="single" w:sz="4" w:space="0" w:color="D1D5DB"/>'
        '  <w:left w:val="single" w:sz="4" w:space="0" w:color="D1D5DB"/>'
        '  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="D1D5DB"/>'
        '  <w:right w:val="single" w:sz="4" w:space="0" w:color="D1D5DB"/>'
        '  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="D1D5DB"/>'
        '  <w:insideV w:val="single" w:sz="4" w:space="0" w:color="D1D5DB"/>'
        '</w:tblBorders>'
    )
    tblPr.append(borders)


def set_paragraph_spacing(paragraph, before=0, after=0):
    """Set paragraph spacing."""
    pPr = paragraph._p.get_or_add_pPr()
    spacing = parse_xml(
        f'<w:spacing {nsdecls("w")} w:before="{before}" w:after="{after}"/>'
    )
    pPr.append(spacing)


# ============================================================
# GENERATE DOCX
# ============================================================

def generate_docx():
    doc = Document()

    # -- Page setup --
    section = doc.sections[0]
    section.page_width = Cm(21)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)

    # -- Default font --
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(10)
    font.color.rgb = COLOR_DARK

    # ---- TITLE PAGE ----
    for _ in range(6):
        doc.add_paragraph("")

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("POSTGRADO UNIVERSITARIO")
    run.font.size = Pt(14)
    run.font.color.rgb = COLOR_MEDIUM
    run.font.name = 'Calibri'

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Kubernetes &\nPlatform Engineering")
    run.font.size = Pt(28)
    run.font.bold = True
    run.font.color.rgb = COLOR_PRIMARY
    run.font.name = 'Calibri'

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("De DevOps a Plataformas Internas de Desarrollo a Escala")
    run.font.size = Pt(12)
    run.font.italic = True
    run.font.color.rgb = COLOR_MEDIUM
    run.font.name = 'Calibri'

    doc.add_page_break()

    # ---- DESCRIPTION ----
    h = doc.add_heading("Descripción del Programa", level=1)
    h.runs[0].font.color.rgb = COLOR_PRIMARY

    doc.add_paragraph(
        "Este postgrado forma ingenieros y arquitectos capaces de diseñar, implementar y operar "
        "plataformas internas de desarrollo sobre Kubernetes a escala empresarial. El programa "
        "integra los fundamentos de DevOps con las prácticas avanzadas de Platform Engineering, "
        "cubriendo el ciclo completo: desde la infraestructura cloud y la gestión de secretos "
        "hasta los flujos GitOps, la observabilidad distribuida y la gestión multicluster en "
        "entornos productivos de alta exigencia."
    )

    # ---- STRUCTURE SUMMARY TABLE ----
    h = doc.add_heading("Estructura del Programa", level=2)
    h.runs[0].font.color.rgb = COLOR_PRIMARY

    table = doc.add_table(rows=1, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    add_table_borders(table)
    data = [("12", "Módulos"), ("140h", "Horas lectivas"), ("3", "Clouds"), ("35+", "Herramientas")]
    row = table.rows[0]
    for i, (val, label) in enumerate(data):
        cell = row.cells[i]
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(val)
        run.font.size = Pt(18)
        run.font.bold = True
        run.font.color.rgb = COLOR_PRIMARY
        p2 = cell.add_paragraph()
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run2 = p2.add_run(label)
        run2.font.size = Pt(9)
        run2.font.color.rgb = COLOR_MEDIUM
        set_cell_shading(cell, COLOR_LIGHT_BG)

    doc.add_paragraph("")

    # -- Profile tables --
    for label, text in [
        ("Perfil de ingreso recomendado",
         "Ingenieros de software o sistemas con experiencia en desarrollo o administración de "
         "sistemas Linux. Se valorará conocimiento básico de redes TCP/IP, scripting y algún "
         "proveedor cloud. No se requiere experiencia previa en Kubernetes."),
        ("Perfil de egreso",
         "Al finalizar, el estudiante estará capacitado para diseñar y operar Internal Developer "
         "Platforms (IDP) basadas en Kubernetes, implementar estrategias GitOps con gestión avanzada "
         "de secretos, gestionar despliegues multicloud y multicluster con Hosted Control Planes, "
         "construir Operators personalizados y liderar la transformación de equipos hacia Platform Engineering."),
    ]:
        table = doc.add_table(rows=1, cols=1)
        add_table_borders(table)
        cell = table.rows[0].cells[0]
        p = cell.paragraphs[0]
        run = p.add_run(f"◆  {label}")
        run.font.bold = True
        run.font.size = Pt(10)
        run.font.color.rgb = COLOR_PRIMARY
        p2 = cell.add_paragraph()
        run2 = p2.add_run(text)
        run2.font.size = Pt(10)
        set_cell_shading(cell, COLOR_LIGHT_BG)
        doc.add_paragraph("")

    # ---- MODULE SUMMARY TABLE ----
    doc.add_paragraph("")
    table = doc.add_table(rows=len(MODULES) + 1, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    add_table_borders(table)

    # Header
    hdr = table.rows[0]
    for i, txt in enumerate(["Módulo", "Título"]):
        cell = hdr.cells[i]
        p = cell.paragraphs[0]
        run = p.add_run(txt)
        run.font.bold = True
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        set_cell_shading(cell, COLOR_HEADER_BG)

    for ri, mod in enumerate(MODULES, 1):
        row = table.rows[ri]
        cell0 = row.cells[0]
        p0 = cell0.paragraphs[0]
        run0 = p0.add_run(f"{mod['id']} · {mod['hours']:.0f}h")
        run0.font.bold = True
        run0.font.size = Pt(10)
        run0.font.color.rgb = COLOR_PRIMARY

        cell1 = row.cells[1]
        p1 = cell1.paragraphs[0]
        run1 = p1.add_run(mod['title'])
        run1.font.size = Pt(10)

        if ri % 2 == 0:
            set_cell_shading(cell0, COLOR_LIGHT_BG)
            set_cell_shading(cell1, COLOR_LIGHT_BG)

    # Set column widths
    for row in table.rows:
        row.cells[0].width = Cm(3.5)
        row.cells[1].width = Cm(12.5)

    doc.add_page_break()

    # ---- DETAILED MODULES ----
    current_block = None
    for mod in MODULES:
        # Block header
        if mod.get("block") and mod["block"] != current_block:
            current_block = mod["block"]

            table = doc.add_table(rows=1, cols=1)
            add_table_borders(table)
            cell = table.rows[0].cells[0]
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(f"{mod['block']}")
            run.font.bold = True
            run.font.size = Pt(11)
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            p2 = cell.add_paragraph()
            p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run2 = p2.add_run(mod.get("block_title", ""))
            run2.font.size = Pt(13)
            run2.font.bold = True
            run2.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            set_cell_shading(cell, COLOR_HEADER_BG)
            doc.add_paragraph("")

        # Module detail table
        # Build topics string
        topics_lines = []
        for t in mod["topics"]:
            topics_lines.append(f"›  {t}")
        topics_str = "\n".join(topics_lines)

        table = doc.add_table(rows=1, cols=1)
        add_table_borders(table)
        cell = table.rows[0].cells[0]

        # Module header line
        p = cell.paragraphs[0]
        run = p.add_run(f"{mod['id']} | {mod['hours']:.0f}h")
        run.font.bold = True
        run.font.size = Pt(11)
        run.font.color.rgb = COLOR_PRIMARY

        run2 = p.add_run(f"    {mod['title']}")
        run2.font.bold = True
        run2.font.size = Pt(11)
        run2.font.color.rgb = COLOR_DARK

        # Description
        p2 = cell.add_paragraph()
        run3 = p2.add_run(mod['description'])
        run3.font.size = Pt(10)
        run3.font.italic = True
        run3.font.color.rgb = COLOR_MEDIUM

        # Topics
        for topic in mod["topics"]:
            p3 = cell.add_paragraph()
            run4 = p3.add_run(f"›  {topic}")
            run4.font.size = Pt(9)
            run4.font.color.rgb = COLOR_DARK
            set_paragraph_spacing(p3, before=20, after=20)

        doc.add_paragraph("")

        # Session breakdown table
        if mod["session_detail"]:
            sess_table = doc.add_table(rows=len(mod["session_detail"]) + 1, cols=4)
            sess_table.alignment = WD_TABLE_ALIGNMENT.CENTER
            add_table_borders(sess_table)

            # Header
            hdr = sess_table.rows[0]
            for i, txt in enumerate(["#", "Título", "Duración", "Contenido"]):
                cell_h = hdr.cells[i]
                p_h = cell_h.paragraphs[0]
                run_h = p_h.add_run(txt)
                run_h.font.bold = True
                run_h.font.size = Pt(9)
                run_h.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                set_cell_shading(cell_h, COLOR_HEADER_BG)

            for si, (sess_num, sess_title, sess_dur, sess_content) in enumerate(mod["session_detail"], 1):
                row = sess_table.rows[si]
                for ci, val in enumerate([sess_num, sess_title, sess_dur, sess_content]):
                    cell_s = row.cells[ci]
                    p_s = cell_s.paragraphs[0]
                    run_s = p_s.add_run(val)
                    run_s.font.size = Pt(9)
                    if ci == 0:
                        run_s.font.bold = True
                        run_s.font.color.rgb = COLOR_PRIMARY
                    if si % 2 == 0:
                        set_cell_shading(cell_s, COLOR_LIGHT_BG)

            # Column widths
            for row in sess_table.rows:
                row.cells[0].width = Cm(2)
                row.cells[1].width = Cm(4)
                row.cells[2].width = Cm(1.5)
                row.cells[3].width = Cm(8.5)

        doc.add_paragraph("")

    # ---- CERTIFICATIONS ----
    doc.add_page_break()
    h = doc.add_heading("Competencias y Certificaciones", level=1)
    h.runs[0].font.color.rgb = COLOR_PRIMARY

    doc.add_paragraph(
        "Al finalizar el programa, el estudiante habrá adquirido las competencias técnicas y "
        "organizativas para desempeñarse como Platform Engineer, Site Reliability Engineer (SRE) "
        "o Kubernetes Architect en organizaciones de cualquier tamaño y sector."
    )

    h2 = doc.add_heading("Certificaciones Oficiales Alineadas", level=2)
    h2.runs[0].font.color.rgb = COLOR_PRIMARY

    certs = [
        ("CKA — Certified Kubernetes Administrator", "Cobertura directa: módulos M08 y M09"),
        ("CKAD — Certified Kubernetes Application Dev.", "Cobertura directa: módulos M07, M08 y M11"),
        ("CKS — Certified Kubernetes Security Specialist", "Cobertura directa: módulos M08, M09 y M10"),
        ("HashiCorp Vault Associate", "Cobertura directa: módulo M10"),
        ("HashiCorp Terraform Associate", "Cobertura directa: módulo M06"),
        ("AWS / Azure / GCP Associate Cloud", "Cobertura directa: módulo M05"),
        ("KCNA — Kubernetes and Cloud Native Associate", "Cobertura completa del programa"),
        ("GitOps Certified (CGOA — Linux Foundation)", "Cobertura directa: módulos M11 y M12"),
    ]

    cert_table = doc.add_table(rows=len(certs) + 1, cols=2)
    cert_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    add_table_borders(cert_table)

    hdr = cert_table.rows[0]
    for i, txt in enumerate(["Certificación", "Cobertura en el programa"]):
        cell = hdr.cells[i]
        p = cell.paragraphs[0]
        run = p.add_run(txt)
        run.font.bold = True
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        set_cell_shading(cell, COLOR_HEADER_BG)

    for ri, (cert, coverage) in enumerate(certs, 1):
        row = cert_table.rows[ri]
        for ci, val in enumerate([cert, coverage]):
            cell = row.cells[ci]
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.size = Pt(9)
            if ci == 0:
                run.font.bold = True
            if ri % 2 == 0:
                set_cell_shading(cell, COLOR_LIGHT_BG)

    # ---- TECHNOLOGIES TABLE ----
    doc.add_paragraph("")
    h2 = doc.add_heading("Herramientas y Tecnologías", level=2)
    h2.runs[0].font.color.rgb = COLOR_PRIMARY

    techs = [
        ("Lenguajes", "Go, Python, Bash"),
        ("Contenedores", "Docker, containerd, BuildKit, kaniko, Cosign, Syft"),
        ("Kubernetes local", "kind, minikube, k3d, k3s"),
        ("IaC", "Terraform, OpenTofu, Crossplane, ExternalDNS, cert-manager"),
        ("Secret Management", "HashiCorp Vault, External Secrets Operator, Sealed Secrets, SOPS"),
        ("GitOps", "ArgoCD, Prow, Argo Rollouts, Argo Image Updater"),
        ("Pipelines CI/CD", "Tekton + Chains, GitHub Actions"),
        ("Observabilidad", "Prometheus, Grafana, Loki, Tempo, OpenTelemetry Collector"),
        ("Networking", "Traefik, Istio (+ Ambient), Cilium, Calico, CoreDNS"),
        ("Seguridad", "OPA/Gatekeeper, Kyverno, Trivy, Cosign, SBOM"),
        ("App Bundles", "Helm 3, Kustomize, Operator SDK, kubebuilder"),
        ("Scaling", "HPA, VPA, KEDA, Karpenter, Cluster Autoscaler"),
        ("Serverless", "Knative Serving, Virtual Kubelet, KEDA"),
        ("Hosted Ctrl Planes", "HyperShift, Kamaji, vCluster"),
        ("Multi-cluster", "Cluster API, Rancher Fleet, OCM, Cilium Cluster Mesh, Submariner"),
        ("Developer Portal", "Backstage"),
        ("Cloud", "AWS (EKS), Azure (AKS), GCP (GKE)"),
    ]

    tech_table = doc.add_table(rows=len(techs) + 1, cols=2)
    tech_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    add_table_borders(tech_table)

    hdr = tech_table.rows[0]
    for i, txt in enumerate(["Categoría", "Tecnologías"]):
        cell = hdr.cells[i]
        p = cell.paragraphs[0]
        run = p.add_run(txt)
        run.font.bold = True
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        set_cell_shading(cell, COLOR_HEADER_BG)

    for ri, (cat, tech) in enumerate(techs, 1):
        row = tech_table.rows[ri]
        for ci, val in enumerate([cat, tech]):
            cell = row.cells[ci]
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.size = Pt(9)
            if ci == 0:
                run.font.bold = True
                run.font.color.rgb = COLOR_PRIMARY
            if ri % 2 == 0:
                set_cell_shading(cell, COLOR_LIGHT_BG)

    for row in tech_table.rows:
        row.cells[0].width = Cm(3.5)
        row.cells[1].width = Cm(12.5)

    # ---- SAVE ----
    path = os.path.join(os.path.dirname(__file__), "Postgrado_Kubernetes_Platform_Engineering.docx")
    doc.save(path)
    print(f"DOCX saved: {path}")
    return path


# ============================================================
# GENERATE XLSX — Weekly Calendar
# ============================================================

def generate_xlsx():
    wb = Workbook()
    ws = wb.active
    ws.title = "Calendario Semanal"

    # Styles
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="1A56DB", end_color="1A56DB", fill_type="solid")
    alt_fill = PatternFill(start_color="E8F0FE", end_color="E8F0FE", fill_type="solid")
    module_font = Font(name="Calibri", size=10, bold=True, color="1A56DB")
    normal_font = Font(name="Calibri", size=10, color="1F2A37")
    center_align = Alignment(horizontal="center", vertical="center", wrap_text=True)
    left_align = Alignment(horizontal="left", vertical="center", wrap_text=True)
    thin_border = Border(
        left=Side(style="thin", color="D1D5DB"),
        right=Side(style="thin", color="D1D5DB"),
        top=Side(style="thin", color="D1D5DB"),
        bottom=Side(style="thin", color="D1D5DB"),
    )

    # Build session list in order
    sessions = []
    for mod in MODULES:
        for sess in mod["session_detail"]:
            sessions.append({
                "module_id": mod["id"],
                "module_title": mod["title"],
                "block": mod.get("block", ""),
                "block_title": mod.get("block_title", ""),
                "session_num": sess[0],
                "session_title": sess[1],
                "duration": sess[2],
                "content": sess[3],
            })

    # Headers
    headers = [
        "Semana", "Fecha orientativa", "Día",
        "Sesión", "Módulo", "Título de la sesión",
        "Duración", "Contenido principal",
        "Horas semana", "Horas acumuladas"
    ]

    for ci, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=ci, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = center_align
        cell.border = thin_border

    # Fill data: 2 sessions per week, 7h/week
    row_num = 2
    cumulative_hours = 0

    for week in range(1, 21):  # 20 weeks
        sess_idx_1 = (week - 1) * 2
        sess_idx_2 = (week - 1) * 2 + 1

        week_sessions = []
        if sess_idx_1 < len(sessions):
            week_sessions.append(sessions[sess_idx_1])
        if sess_idx_2 < len(sessions):
            week_sessions.append(sessions[sess_idx_2])

        week_hours = len(week_sessions) * 3.5
        cumulative_hours += week_hours

        for si, sess in enumerate(week_sessions):
            day_label = "Día 1" if si == 0 else "Día 2"
            is_alt = week % 2 == 0

            values = [
                f"Semana {week}",
                "",  # fecha orientativa (blank)
                day_label,
                sess["session_num"],
                f"{sess['module_id']} — {sess['module_title']}",
                sess["session_title"],
                sess["duration"],
                sess["content"],
                f"{week_hours:.0f}h" if si == 0 else "",
                f"{cumulative_hours:.0f}h" if si == 0 else "",
            ]

            for ci, val in enumerate(values, 1):
                cell = ws.cell(row=row_num, column=ci, value=val)
                cell.font = normal_font
                cell.alignment = left_align if ci >= 5 else center_align
                cell.border = thin_border
                if ci == 4 or ci == 5:
                    cell.font = module_font
                if is_alt:
                    cell.fill = alt_fill

            row_num += 1

    # Summary row
    row_num += 1
    ws.cell(row=row_num, column=1, value="TOTAL").font = Font(name="Calibri", size=11, bold=True, color="1A56DB")
    ws.cell(row=row_num, column=7, value="140h").font = Font(name="Calibri", size=11, bold=True, color="1A56DB")
    ws.cell(row=row_num, column=9, value="7h/sem").font = Font(name="Calibri", size=11, bold=True, color="1A56DB")
    ws.cell(row=row_num, column=10, value="140h").font = Font(name="Calibri", size=11, bold=True, color="1A56DB")
    for ci in range(1, 11):
        ws.cell(row=row_num, column=ci).border = thin_border

    # Column widths
    widths = [10, 14, 8, 10, 38, 30, 9, 60, 10, 12]
    for ci, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(ci)].width = w

    # ---- Sheet 2: Module summary ----
    ws2 = wb.create_sheet("Resumen por Módulo")

    headers2 = ["Módulo", "Título", "Horas", "Sesiones", "Bloque"]
    for ci, header in enumerate(headers2, 1):
        cell = ws2.cell(row=1, column=ci, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = center_align
        cell.border = thin_border

    for ri, mod in enumerate(MODULES, 2):
        vals = [
            mod["id"],
            mod["title"],
            f"{mod['hours']:.0f}h",
            mod["sessions"],
            mod.get("block_title", mod.get("block", "")),
        ]
        is_alt = ri % 2 == 0
        for ci, val in enumerate(vals, 1):
            cell = ws2.cell(row=ri, column=ci, value=val)
            cell.font = module_font if ci == 1 else normal_font
            cell.alignment = center_align if ci in (1, 3, 4) else left_align
            cell.border = thin_border
            if is_alt:
                cell.fill = alt_fill

    # Total row
    total_row = len(MODULES) + 2
    ws2.cell(row=total_row, column=1, value="TOTAL").font = Font(name="Calibri", size=11, bold=True, color="1A56DB")
    ws2.cell(row=total_row, column=3, value="140h").font = Font(name="Calibri", size=11, bold=True, color="1A56DB")
    ws2.cell(row=total_row, column=4, value=40).font = Font(name="Calibri", size=11, bold=True, color="1A56DB")
    for ci in range(1, 6):
        ws2.cell(row=total_row, column=ci).border = thin_border

    widths2 = [8, 45, 8, 10, 25]
    for ci, w in enumerate(widths2, 1):
        ws2.column_dimensions[get_column_letter(ci)].width = w

    # ---- Sheet 3: Session detail ----
    ws3 = wb.create_sheet("Detalle de Sesiones")

    headers3 = ["Sesión", "Módulo", "Título", "Duración", "Contenido detallado"]
    for ci, header in enumerate(headers3, 1):
        cell = ws3.cell(row=1, column=ci, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = center_align
        cell.border = thin_border

    for ri, sess in enumerate(sessions, 2):
        vals = [
            sess["session_num"],
            sess["module_id"],
            sess["session_title"],
            sess["duration"],
            sess["content"],
        ]
        is_alt = ri % 2 == 0
        for ci, val in enumerate(vals, 1):
            cell = ws3.cell(row=ri, column=ci, value=val)
            cell.font = normal_font
            cell.alignment = left_align
            cell.border = thin_border
            if ci in (1, 2):
                cell.font = module_font
                cell.alignment = center_align
            if is_alt:
                cell.fill = alt_fill

    widths3 = [12, 8, 32, 9, 70]
    for ci, w in enumerate(widths3, 1):
        ws3.column_dimensions[get_column_letter(ci)].width = w

    path = os.path.join(os.path.dirname(__file__), "Calendario_Postgrado_Kubernetes.xlsx")
    wb.save(path)
    print(f"XLSX saved: {path}")
    return path


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    generate_docx()
    generate_xlsx()
    print("Done!")
