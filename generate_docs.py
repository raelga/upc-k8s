#!/usr/bin/env python3
"""Generate the Posgrado Platform Engineering & DevOps con Kubernetes .docx and .xlsx files.

Structure matches the published UPC program (curso 305300):
90 horas lectivas / 12 ECTS / Live online / 6 módulos + Proyecto Final.
"""

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
# PROGRAM FACTS (published UPC program 305300)
# ============================================================

PROGRAM = {
    "title": "Posgrado en Platform Engineering y DevOps con Kubernetes",
    "titulacion": "Diploma de experto en Platform Engineering y DevOps con Kubernetes (UPC)",
    "tagline": "Conviértete en Platform Engineer: especialízate en Kubernetes y despliega la nueva generación de plataformas cloud.",
    "hours": "90h",
    "ects": "12",
    "modalidad": "Live online",
    "idioma": "Español",
    "duracion": "5 meses",
    "edicion": "1ª edición",
    "direccion": "Rael Garcia Arnes · René Serral Gracià",
    "url": "https://upcschool.upc.edu/esp/estudis/formacio/curs/305300/postgrau-platform-engineering-devops-kubernetes/",
    "inicio": "03/11/2026",
    "fin": "18/03/2027",
    "horario": "Martes y jueves, 18:00 a 21:00 (3h por sesión)",
}

# Class schedule: sessions run Tue/Thu 18:00-21:00 from inicio to fin.
# Non-teaching dates aligned with the official UPC FIB academic calendar (festius + vacances):
# La Immaculada (8 Dec), Christmas break (24, 29, 31 Dec 2026; 5 Jan 2027), and 9 Feb 2027 (festiu UPC).
# 90h / 3h = 30 sessions; the remaining Tue/Thu slots act as buffer/recuperación.
SCHEDULE_START = (2026, 11, 3)
SCHEDULE_END = (2027, 3, 18)
SESSION_HOURS = 3
NON_TEACHING = {
    (2026, 12, 8): "Festivo: La Immaculada",
    (2026, 12, 24): "Vacaciones de Navidad",
    (2026, 12, 29): "Vacaciones de Navidad",
    (2026, 12, 31): "Vacaciones de Navidad",
    (2027, 1, 5): "Vacaciones de Navidad",
    (2027, 2, 9): "Festivo UPC",
}

# ============================================================
# DATA: 6 modules + Proyecto Final, 90h / 12 ECTS total
# Each module aggregates units from the original detailed roadmap.
# ============================================================

MODULES = [
    {
        "id": "M1",
        "title": "Fundamentos DevOps, Platform Engineering y Programación para Infraestructura",
        "ects": "1.5",
        "hours": 6,
        "sessions": [
            "Fundamentos de DevOps y Platform Engineering (CALMS, IDP, Team Topologies, DORA)",
            "Bash y Python para DevOps, asistidos por IA",
        ],
        "description": (
            "Contextualización del movimiento DevOps y su evolución hacia Platform Engineering. "
            "Competencias de programación asistidas por inteligencia artificial en Bash y Python "
            "orientadas a la automatización de infraestructura y desarrollo de CLIs. Go se introduce "
            "más adelante (M6), en el contexto de construcción de controladores para Kubernetes."
        ),
        "units": [
            {
                "title": "Fundamentos de DevOps y Platform Engineering",
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
            },
            {
                "title": "Bash y Python para DevOps (asistida por IA)",
                "topics": [
                    "Programación asistida por IA: copilots y asistentes para scripting, refactorización y generación de tests",
                    "Bash scripting: variables, estructuras de control, funciones, arrays y manejo de errores",
                    "Automatización de sistema: pipes, redirecciones, grep/sed/awk/jq/yq, cron y Makefiles",
                    "Python para DevOps: scripting, SDKs cloud (boto3, azure-sdk, google-cloud) y manejo de APIs REST",
                    "Python: manipulación de YAML/JSON/TOML, Jinja2 templating, CLIs con Click/Typer y testing con pytest",
                    "Calidad de código: linting con ruff, type checking con mypy, pre-commit hooks",
                ],
            },
        ],
    },
    {'id': 'M2',
     'title': 'Cloud Computing Multicloud e Infraestructura como Código',
     'ects': '1',
     'hours': 9,
     'sessions': ['AWS y fundamentos de Terraform/OpenTofu',
                  'Azure e IaC: equivalencias y módulos',
                  'GCP e IaC: estado y comparativa multicloud'],
     'description': 'Infraestructura cloud básica con Terraform/OpenTofu integrado en tres sesiones. AWS como '
                    'caso principal; Azure y GCP como transferencia del mismo patrón, con ejemplos preparados. '
                    'Identidad, redes, máquinas virtuales y almacenamiento. Comparación breve con Pulumi, sin '
                    'laboratorio propio. Kubernetes gestionado y su aprovisionamiento se abordan en M4.',
     'units': [{'title': 'AWS y fundamentos de Terraform/OpenTofu',
                'topics': ['AWS: IAM, regiones y zonas, VPC, subredes, Security Groups, EC2 y S3; contexto de '
                           'ECR',
                           'Fundamentos IaC: declarativo, idempotencia y drift; Terraform/OpenTofu, HCL, '
                           'provider y recursos',
                           'Caso práctico común: red, máquina virtual y almacenamiento; init, plan, apply y '
                           'destroy; permisos y control de costes']},
               {'title': 'Azure e IaC: equivalencias y módulos',
                'topics': ['Azure: Entra ID, suscripciones, grupos de recursos, Managed Identities, VNet, NSG, '
                           'máquinas virtuales y Blob Storage; contexto de ACR',
                           'Transferencia del caso AWS a Azure con configuración preparada: equivalencias y '
                           'diferencias',
                           'Terraform/OpenTofu: variables, outputs y uso de módulos existentes; sin diseño '
                           'avanzado de módulos propios']},
               {'title': 'GCP e IaC: estado y comparativa multicloud',
                'topics': ['GCP: proyectos, cuentas de servicio, IAM, VPC, firewall, Compute Engine y Cloud '
                           'Storage; contexto de Artifact Registry',
                           'Transferencia del mismo caso a GCP con configuración preparada; comparación de '
                           'identidad, redes, permisos y portabilidad',
                           'Terraform/OpenTofu: estado local y remoto, locking según backend y protección del '
                           'estado y de las credenciales',
                           'Pulumi: comparación de 10–15 minutos de HCL frente a Python/Go con un ejemplo '
                           'equivalente pequeño; también requiere gestión de estado; sin instalación ni '
                           'laboratorio propio']}]},
    {
        "id": "M3",
        "title": "Contenedores y Kubernetes Core. Ecosistema OCI",
        "ects": "2",
        "hours": 15,
        "sessions": [
            "Contenedores y ecosistema OCI: imágenes, runtimes y seguridad",
            "Kubernetes: arquitectura, control plane y clusters locales (kind)",
            "Building Blocks: workloads, configuración y scheduling",
            "Almacenamiento y networking en Kubernetes",
            "Autenticación, RBAC y clúster componente a componente",
        ],
        "description": (
            "Ecosistema OCI: construcción de imágenes, runtimes, registros y seguridad. Arquitectura "
            "completa de Kubernetes: plano de control, bloques fundamentales (workloads, configuración, "
            "scheduling), almacenamiento (PV/PVC, CSI), networking (Services, Ingress, Gateway API, CNI, "
            "Network Policies), autenticación (RBAC, OIDC, admission controllers) y construcción de un "
            "clúster componente a componente."
        ),
        "units": [
            {
                "title": "Contenedores y Ecosistema OCI",
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
            },
            {
                "title": "Kubernetes Core: Arquitectura y Building Blocks",
                "topics": [
                    "Introducción · Control Plane: kube-apiserver, etcd, kube-scheduler, controller-manager, cloud-controller-manager",
                    "Introducción · Data Plane: kubelet, kube-proxy, container runtime y comunicación entre nodos",
                    "Clusters locales · kind (Kubernetes in Docker): configuración multi-nodo, networking y uso en CI",
                    "Building Blocks · Pods: ciclo de vida, init containers, sidecar pattern y ephemeral containers",
                    "Building Blocks · Workloads: Deployment, StatefulSet, DaemonSet, Job, CronJob y ReplicaSet",
                    "Building Blocks · Configuración: ConfigMap, Secret (tipos, encriptación at rest), env vars y volúmenes",
                    "Building Blocks · Namespace, Labels, Selectors, Annotations, Finalizers y OwnerReferences",
                    "Building Blocks · Scheduling: node/pod affinity, taints, tolerations, topology spread y priority classes",
                    "Building Blocks · Resource management: requests, limits, LimitRange, ResourceQuota y QoS classes",
                    "Almacenamiento · PersistentVolume, PersistentVolumeClaim, StorageClass, dynamic provisioning y CSI (EBS, Azure Disk, GCE PD)",
                    "Networking · Services (ClusterIP, NodePort, LoadBalancer, Headless), Ingress, Gateway API, CNI (Calico, Cilium) y NetworkPolicy",
                    "Networking · DNS interno: CoreDNS, resolución de servicios y customización de zonas",
                    "Autenticación · RBAC: ServiceAccounts, Roles, ClusterRoles, Bindings y principio de mínimo privilegio",
                    "Autenticación · certificados X.509, OIDC, webhook auth, bound SA tokens y admission controllers (Gatekeeper, Kyverno, PSA)",
                    "Cluster desde cero · etcd, kube-apiserver, scheduler, controller-manager, kubelet, kube-proxy: configuración manual, PKI y TLS bootstrapping",
                ],
            },
        ],
    },
    {
        "id": "M4",
        "title": "Kubernetes en Producción y Ecosistema Cloud Native",
        "ects": "2",
        "hours": 15,
        "sessions": [
            "Kubernetes gestionado: EKS, GKE y AKS",
            "Otros entornos y aprovisionamiento IaC multi-cloud",
            "Application bundles: Kustomize, Helm y su ecosistema",
            "Infraestructura declarativa: ExternalDNS, cert-manager y Crossplane",
            "Gestión de secretos: Vault y External Secrets Operator",
        ],
        "description": (
            "Operación de clústeres gestionados (EKS, GKE, AKS) y otros entornos. Application bundles "
            "(Helm, Kustomize). Infraestructura declarativa dentro de Kubernetes: ExternalDNS, "
            "cert-manager y Crossplane. Gestión de secretos con HashiCorp Vault y External Secrets Operator."
        ),
        "units": [
            {
                "title": "Kubernetes en Producción: clústeres gestionados multi-cloud",
                "topics": [
                    "EKS (AWS): arquitectura, node groups (managed, self-managed, Fargate), eksctl",
                    "EKS Add-ons: AWS Load Balancer Controller, EBS/EFS CSI, VPC CNI, ExternalDNS",
                    "EKS Seguridad: IRSA, EKS Pod Identity, KMS encryption y audit logging",
                    "GKE: Standard vs Autopilot, node pools, Workload Identity y VPC-native networking",
                    "GKE Add-ons: Cloud Operations, Config Connector, GKE Gateway y Fleet Management",
                    "AKS: arquitectura, AAD/Entra ID integration, Managed Identities y Azure CNI",
                    "AKS Add-ons: Azure Monitor, CSI drivers (Disk/Files/Blob), AGIC y Azure Policy",
                    "AKS Seguridad: Workload Identity, Azure Key Vault CSI Provider y Defender for Containers",
                    "Otros entornos: OVHcloud, DigitalOcean DOKS, Linode LKE, on-premises (k3s, k0s, Rancher, OpenShift)",
                    "Aprovisionamiento IaC: Terraform modules para EKS, GKE y AKS. Comparativa multi-cloud",
                ],
            },
            {
                "title": "Application Bundles e Infraestructura Declarativa",
                "topics": [
                    "Kustomize: bases, overlays, patches, generators y transformers. 2 ejemplos prácticos (dev/prod)",
                    "Helm: charts, templates, values, hooks. El catálogo de Helm (Artifact Hub) como ecosistema de distribución",
                    "Helm + Kustomize: helm-secrets, helm-diff. Combinar render de Helm con overlays Kustomize por entorno",
                    "Caso real: charts que despliegan operators (kube-prometheus-stack, Grafana Operator). Se profundiza en la Sesión 24",
                    "ExternalDNS: providers (Route53, CloudDNS, Cloudflare), anotaciones y políticas de sync",
                    "cert-manager: Issuers, ClusterIssuers, Let's Encrypt, ACME DNS-01/HTTP-01, renovación automática",
                    "Crossplane: Providers, Managed Resources, Compositions, XRDs. Comparativa con Terraform",
                    "Crossplane avanzado: Composition Functions, EnvironmentConfigs, integración con ArgoCD",
                ],
            },
            {
                "title": "Gestión de Secretos: Vault y External Secrets",
                "topics": [
                    "Vault · Arquitectura: server, agents, backends de almacenamiento y alta disponibilidad",
                    "Vault · Auth methods en Kubernetes: Kubernetes Auth, JWT/OIDC, AppRole y cloud IAM",
                    "Vault · Secrets Engines: KV v1/v2, Dynamic Secrets (database, AWS, Azure), PKI y Transit",
                    "Vault · Vault Agent: auto-auth, template rendering, sidecar injection. Vault Secrets Operator (VSO)",
                    "Vault · Políticas (HCL), namespaces, auditing, DR con Raft y auto-unseal con KMS (AWS, Azure, GCP)",
                    "External Secrets · ExternalSecret, SecretStore, ClusterSecretStore y refresh intervals",
                    "External Secrets · Providers: AWS Secrets Manager, Azure Key Vault, GCP Secret Manager y Vault",
                    "External Secrets · Patrones avanzados: secret templating, generators, pushSecret e integración con GitOps",
                    "Secret Management · Sealed Secrets, SOPS y comparativa de patrones por madurez",
                ],
            },
        ],
    },
    {
        "id": "M5",
        "title": "Observabilidad, GitOps, CI/CD y Networking Avanzado",
        "ects": "2",
        "hours": 18,
        "sessions": [
            "Observabilidad (I): Prometheus, PromQL y Alertmanager",
            "Observabilidad (II): Grafana y Loki (logs)",
            "Observabilidad (III): OpenTelemetry, Tempo y correlación",
            "GitOps y pipelines CI/CD: ArgoCD, Prow y Tekton",
            "Networking avanzado: Traefik e Istio (service mesh)",
            "Entrega progresiva y escalado: Argo Rollouts, HPA/VPA, KEDA, Karpenter",
        ],
        "description": (
            "Stack de observabilidad completo: Prometheus, Grafana (Loki, Tempo, Mimir), OpenTelemetry, "
            "repartido en 3 sesiones (métricas, logs, trazas+correlación) para un ritmo sostenible. "
            "GitOps con ArgoCD y Prow. Pipelines con Tekton. Networking avanzado con Traefik e Istio "
            "(service mesh). Estrategias de despliegue (canary, blue/green) con Argo Rollouts. Escalado de "
            "workloads (HPA, VPA, KEDA, Karpenter)."
        ),
        "units": [
            {
                "title": "Observabilidad (I): Métricas",
                "topics": [
                    "Los tres pilares: métricas, logs, trazas. Correlación entre señales",
                    "Prometheus: arquitectura, scraping, PromQL, service discovery, Alertmanager",
                    "Prometheus Operator: ServiceMonitor, PodMonitor, recording rules, alerting rules. Thanos para HA",
                ],
            },
            {
                "title": "Observabilidad (II): Grafana y Logs",
                "topics": [
                    "Grafana: datasources, dashboards, variables, alerting. Grafana as Code (grafonnet, Terraform)",
                    "Loki: arquitectura, LogQL (mismo modelo mental que PromQL), labels vs indexación de texto completo",
                    "Promtail: recolección de logs de los Pods y envío a Loki",
                    "Grafana Explore: consulta y filtrado de logs por label en tiempo real",
                ],
            },
            {
                "title": "Observabilidad (III): OpenTelemetry, Tempo y Correlación",
                "topics": [
                    "OpenTelemetry: especificación OTLP, SDK, auto-instrumentación de la app sin tocar código",
                    "OpenTelemetry Collector: pipeline de receivers, processors y exporters",
                    "Tempo: backend de trazas distribuidas, trace ID, spans, integración con Grafana",
                    "Mimir: métricas a escala/federadas (mención breve, complementa Prometheus de la Sesión 19)",
                    "Correlación end-to-end: exemplars, salto métrica→traza→logs en un mismo dashboard",
                ],
            },
            {
                "title": "GitOps y Pipelines CI/CD",
                "topics": [
                    "Principios GitOps: declarativo, versionado, automatizado, reconciliado. Pull vs Push model",
                    "ArgoCD: Applications, AppProjects, ApplicationSets, sync policies, waves, hooks y RBAC",
                    "ArgoCD avanzado: multi-tenancy, SSO, App of Apps, ApplicationSet generators y notifications",
                    "ArgoCD Image Updater y Argo Rollouts: patrones de Progressive Delivery con análisis automático",
                    "Prow: arquitectura CI nativa en Kubernetes, plugins, Tide, Deck dashboard y ProwJobs",
                    "Tekton: Tasks, Pipelines, PipelineRuns, Workspaces, Triggers y Tekton Chains",
                    "Integración Tekton + ArgoCD para workflows CI/CD end-to-end en Kubernetes",
                ],
            },
            {
                "title": "Networking Avanzado (Service Mesh)",
                "topics": [
                    "Traefik: IngressRoute CRDs, middlewares, TLS automático, dashboard y métricas",
                    "Traefik avanzado: TCP/UDP routing, rate limiting, circuit breaker, canary con TraefikService",
                    "Istio: arquitectura (Istiod + Envoy sidecars), mTLS automático y observabilidad integrada",
                    "Istio traffic: VirtualServices, DestinationRules, Gateways, traffic shifting, fault injection",
                    "Istio seguridad: AuthorizationPolicies, PeerAuthentication, circuit breaking, Kiali",
                    "Ambient Mesh (Istio): modo sin sidecar, ztunnel, waypoints y migración",
                ],
            },
            {
                "title": "Entrega Progresiva y Escalado",
                "topics": [
                    "Estrategias: rolling update, blue/green, canary, A/B testing y trade-offs",
                    "Argo Rollouts: canary con análisis automatizado, blue-green, integración Istio/Traefik + Prometheus",
                    "Progressive delivery: Feature flags (Flagger/OpenFeature), métricas como gates, rollback automático",
                    "HPA: métricas CPU/memory, custom metrics (Prometheus Adapter), scaling behavior",
                    "VPA: modos (Off/Initial/Auto), recomendaciones y limitaciones",
                    "KEDA: ScaledObject, ScaledJob, triggers (Kafka, SQS, Prometheus, cron) y cooldown",
                    "Cluster Autoscaler vs Karpenter: node pools, scale-from-zero, cost optimization",
                ],
            },
        ],
    },
    {
        "id": "M6",
        "title": "Platform Engineering Avanzado: Operators, Serverless y Multi-Cluster",
        "ects": "2",
        "hours": 18,
        "sessions": [
            "Go: de cero a controlador de Kubernetes",
            "Construcción de Operators con Kubebuilder/Operator SDK",
            "Gestión de clústeres (Cluster API) y serverless (Knative)",
            "Hosted Control Planes: HyperShift, vCluster y Kamaji",
            "Multi-cluster: OCM, Istio multicluster y Cilium Cluster Mesh",
            "Multi-cloud con Crossplane y Disaster Recovery con Velero",
        ],
        "description": (
            "Go desde cero hasta cliente de la API de Kubernetes, como base para construir operators "
            "personalizados con Kubebuilder/Operator SDK. Gestión del ciclo de vida de clústeres con "
            "Cluster API. Serverless con Knative. Hosted Control Planes (HyperShift, vCluster, Kamaji). "
            "Gestión y despliegue multi-cluster (Istio multicluster, Cilium Cluster Mesh, Submariner) y "
            "multi-cloud con Crossplane. Disaster Recovery con Velero."
        ),
        "units": [
            {
                "title": "Go: de cero a controlador de Kubernetes",
                "topics": [
                    "Fundamentos de Go: tipos, structs, interfaces, goroutines, channels, manejo de errores idiomático",
                    "client-go: clientset, kubeconfig, serialización, listar/filtrar/crear recursos de la API",
                    "controller-runtime: reconciliation loop, informers, predicates (fundamentos, sin construir el operator todavía)",
                    "CLIs y tooling: cobra/viper, logging estructurado, go test, mocks con testify, golangci-lint",
                ],
            },
            {
                "title": "Construcción de Operators",
                "topics": [
                    "Operator SDK (Go): scaffolding, CRD design, controller implementation y webhooks",
                    "kubebuilder: reconciliation patterns, finalizers, status conditions y API versioning",
                    "Operadores de producción: leader election, metrics, testing (envtest) y OLM",
                ],
            },
            {
                "title": "Gestión de Clústeres y Serverless",
                "topics": [
                    "Cluster API (CAPI): arquitectura, providers (AWS/Azure/GCP), lifecycle y upgrades",
                    "Rancher Fleet y ArgoCD ApplicationSets para gestión de flotas de clusters",
                    "Upgrade strategies: rolling upgrades, ventanas de mantenimiento y node drain",
                    "Knative Serving: auto-scaling a cero, revision routing y traffic splitting",
                    "Virtual Kubelet: nodos virtuales con Fargate, ACI y Cloud Run",
                ],
            },
            {
                "title": "Hosted Control Planes",
                "topics": [
                    "HyperShift (Red Hat): arquitectura, hosted clusters y node pools",
                    "vCluster: clusters virtuales ligeros, sincronización y multi-tenancy",
                    "Kamaji: tenant control planes, datastores y gestión de flota",
                ],
            },
            {
                "title": "Multi-cluster y Multi-cloud",
                "topics": [
                    "Arquitecturas: hub-and-spoke, peer-to-peer, federación",
                    "Open Cluster Management (OCM), Rancher MCM y ArgoCD multicluster",
                    "Istio multicluster (primary-remote, multi-primary)",
                    "Cilium Cluster Mesh: tunneling, shared services y network policies globales",
                    "Submariner: cross-cluster networking, service discovery y globalnet",
                    "Crossplane como plano de control universal, políticas OPA y ESO multi-cloud",
                    "Disaster Recovery: Velero, replicación de estado, RPO/RTO y failover automático",
                ],
            },
        ],
    },
    {
        "id": "PF",
        "title": "Proyecto Final",
        "ects": "1.5",
        "hours": 6,
        "sessions": [
            "Proyecto Final: desarrollo de la plataforma (IDP)",
            "Proyecto Final: presentación y defensa",
        ],
        "description": (
            "Diseño, implementación y defensa de una plataforma interna de desarrollo (IDP) end-to-end "
            "que integre las competencias del programa."
        ),
        "units": [
            {
                "title": "Plataforma Interna de Desarrollo end-to-end",
                "topics": [
                    "Aprovisionamiento de la infraestructura base con Terraform sobre uno o varios proveedores cloud",
                    "Despliegue y configuración de un clúster Kubernetes gestionado",
                    "Flujo GitOps con ArgoCD para el ciclo de vida de las aplicaciones de plataforma",
                    "Gestión de secretos con Vault y/o External Secrets Operator",
                    "Stack de observabilidad (métricas, logs, trazas) y alerting",
                    "Entrega progresiva (canary o blue/green) con rollback automático basado en métricas",
                    "Documentación, golden paths y defensa del proyecto",
                ],
            },
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


def module_hours(mod):
    return mod["hours"]


def build_calendar():
    """Return (sessions, buffer) where sessions is a list of dicts with the 30
    dated class sessions (Tue/Thu) mapped to modules, and buffer is the list of
    remaining Tue/Thu dates (recuperación) up to the official end date."""
    from datetime import date, timedelta

    start = date(*SCHEDULE_START)
    end = date(*SCHEDULE_END)
    non_teaching = {date(*k): v for k, v in NON_TEACHING.items()}

    teaching_dates = []
    d = start
    while d <= end:
        if d.weekday() in (1, 3) and d not in non_teaching:  # Tue=1, Thu=3
            teaching_dates.append(d)
        d += timedelta(days=1)

    # Flatten module sessions in order
    flat = []
    for mod in MODULES:
        for si, theme in enumerate(mod["sessions"], 1):
            flat.append((mod, si, theme))

    n = len(flat)  # expected 30
    dias = {1: "Martes", 3: "Jueves"}
    sessions = []
    acc = 0
    for idx, (mod, si, theme) in enumerate(flat):
        dt = teaching_dates[idx]
        acc += SESSION_HOURS
        sessions.append({
            "n": idx + 1,
            "date": dt,
            "day": dias[dt.weekday()],
            "module_id": mod["id"],
            "module_title": mod["title"],
            "theme": theme,
            "acc_hours": acc,
        })
    buffer = teaching_dates[n:]
    return sessions, buffer


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
    run = p.add_run("POSGRADO")
    run.font.size = Pt(14)
    run.font.color.rgb = COLOR_MEDIUM
    run.font.name = 'Calibri'

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Platform Engineering & DevOps\ncon Kubernetes")
    run.font.size = Pt(28)
    run.font.bold = True
    run.font.color.rgb = COLOR_PRIMARY
    run.font.name = 'Calibri'

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(PROGRAM["tagline"])
    run.font.size = Pt(12)
    run.font.italic = True
    run.font.color.rgb = COLOR_MEDIUM
    run.font.name = 'Calibri'

    doc.add_page_break()

    # ---- DESCRIPTION ----
    h = doc.add_heading("Descripción del Programa", level=1)
    h.runs[0].font.color.rgb = COLOR_PRIMARY

    doc.add_paragraph(
        "Este posgrado forma ingenieros capaces de diseñar, implementar y operar plataformas internas "
        "de desarrollo (IDP) sobre Kubernetes a escala empresarial. El programa integra los fundamentos "
        "de DevOps con las prácticas avanzadas de Platform Engineering, cubriendo el ciclo completo: "
        "desde la infraestructura cloud y la programación para automatización hasta los flujos GitOps, "
        "la observabilidad distribuida y la gestión multicluster en entornos productivos."
    )

    # ---- STRUCTURE SUMMARY TABLE ----
    h = doc.add_heading("Estructura del Programa", level=2)
    h.runs[0].font.color.rgb = COLOR_PRIMARY

    table = doc.add_table(rows=1, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    add_table_borders(table)
    data = [
        (PROGRAM["hours"], "Horas lectivas"),
        (PROGRAM["ects"], "ECTS"),
        ("6 + PF", "Módulos + Proyecto"),
        ("3", "Clouds"),
    ]
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

    # -- Program facts table --
    facts = [
        ("Titulación", PROGRAM["titulacion"]),
        ("Modalidad", PROGRAM["modalidad"]),
        ("Idioma", PROGRAM["idioma"]),
        ("Duración", PROGRAM["duracion"]),
        ("Dirección académica", PROGRAM["direccion"]),
    ]
    fact_table = doc.add_table(rows=len(facts), cols=2)
    fact_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    add_table_borders(fact_table)
    for ri, (k, v) in enumerate(facts):
        c0 = fact_table.rows[ri].cells[0]
        r0 = c0.paragraphs[0].add_run(k)
        r0.font.bold = True
        r0.font.size = Pt(9)
        r0.font.color.rgb = COLOR_PRIMARY
        c1 = fact_table.rows[ri].cells[1]
        r1 = c1.paragraphs[0].add_run(v)
        r1.font.size = Pt(9)
        if ri % 2 == 0:
            set_cell_shading(c0, COLOR_LIGHT_BG)
            set_cell_shading(c1, COLOR_LIGHT_BG)
    for r in fact_table.rows:
        r.cells[0].width = Cm(4.5)
        r.cells[1].width = Cm(11.5)

    doc.add_paragraph("")

    # -- Profile tables --
    for label, text in [
        ("Perfil de ingreso recomendado",
         "Profesionales con experiencia inicial en IT (software o sistemas) que quieren construir una "
         "base sólida en DevOps y Kubernetes con enfoque práctico. Se valorará conocimiento básico de "
         "redes TCP/IP, scripting y algún proveedor cloud. No se requiere experiencia previa en Kubernetes."),
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
    table = doc.add_table(rows=len(MODULES) + 2, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    add_table_borders(table)

    # Header
    hdr = table.rows[0]
    for i, txt in enumerate(["Módulo", "ECTS · Horas", "Título"]):
        cell = hdr.cells[i]
        p = cell.paragraphs[0]
        run = p.add_run(txt)
        run.font.bold = True
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        set_cell_shading(cell, COLOR_HEADER_BG)

    for ri, mod in enumerate(MODULES, 1):
        row = table.rows[ri]
        c0 = row.cells[0]
        r0 = c0.paragraphs[0].add_run(mod["id"])
        r0.font.bold = True
        r0.font.size = Pt(10)
        r0.font.color.rgb = COLOR_PRIMARY

        c1 = row.cells[1]
        r1 = c1.paragraphs[0].add_run(f"{mod['ects']} ECTS · {mod['hours']}h")
        r1.font.size = Pt(10)

        c2 = row.cells[2]
        r2 = c2.paragraphs[0].add_run(mod["title"])
        r2.font.size = Pt(10)

        if ri % 2 == 0:
            for c in (c0, c1, c2):
                set_cell_shading(c, COLOR_LIGHT_BG)

    # Total row
    total_row = table.rows[len(MODULES) + 1]
    rt0 = total_row.cells[0].paragraphs[0].add_run("TOTAL")
    rt0.font.bold = True
    rt0.font.color.rgb = COLOR_PRIMARY
    rt1 = total_row.cells[1].paragraphs[0].add_run(f"{PROGRAM['ects']} ECTS · {PROGRAM['hours']}")
    rt1.font.bold = True
    rt1.font.color.rgb = COLOR_PRIMARY

    for row in table.rows:
        row.cells[0].width = Cm(2.0)
        row.cells[1].width = Cm(3.5)
        row.cells[2].width = Cm(10.5)

    doc.add_page_break()

    # ---- DETAILED MODULES ----
    for mod in MODULES:
        table = doc.add_table(rows=1, cols=1)
        add_table_borders(table)
        cell = table.rows[0].cells[0]

        # Module header line
        p = cell.paragraphs[0]
        run = p.add_run(f"{mod['id']} | {mod['ects']} ECTS · {mod['hours']}h")
        run.font.bold = True
        run.font.size = Pt(11)
        run.font.color.rgb = COLOR_PRIMARY

        run2 = p.add_run(f"    {mod['title']}")
        run2.font.bold = True
        run2.font.size = Pt(11)
        run2.font.color.rgb = COLOR_DARK

        # Description
        p2 = cell.add_paragraph()
        run3 = p2.add_run(mod["description"])
        run3.font.size = Pt(10)
        run3.font.italic = True
        run3.font.color.rgb = COLOR_MEDIUM

        # Units with topics
        for unit in mod["units"]:
            pu = cell.add_paragraph()
            run_u = pu.add_run(f"▸ {unit['title']}")
            run_u.font.bold = True
            run_u.font.size = Pt(10)
            run_u.font.color.rgb = COLOR_PRIMARY
            set_paragraph_spacing(pu, before=40, after=20)
            for topic in unit["topics"]:
                p3 = cell.add_paragraph()
                run4 = p3.add_run(f"     ›  {topic}")
                run4.font.size = Pt(9)
                run4.font.color.rgb = COLOR_DARK
                set_paragraph_spacing(p3, before=10, after=10)

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
        ("CKA — Certified Kubernetes Administrator", "Cobertura directa: módulos M3 y M4"),
        ("CKAD — Certified Kubernetes Application Dev.", "Cobertura directa: módulos M3 y M5"),
        ("CKS — Certified Kubernetes Security Specialist", "Cobertura directa: módulos M3 y M4"),
        ("HashiCorp Vault Associate", "Cobertura directa: módulo M4"),
        ("HashiCorp Terraform Associate", "Cobertura directa: módulo M2"),
        ("AWS / Azure / GCP Associate Cloud", "Cobertura directa: módulo M2"),
        ("KCNA — Kubernetes and Cloud Native Associate", "Cobertura completa del programa"),
        ("GitOps Certified (CGOA — Linux Foundation)", "Cobertura directa: módulos M5 y M6"),
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
# GENERATE XLSX
# ============================================================

def generate_xlsx():
    wb = Workbook()

    # Styles
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="1A56DB", end_color="1A56DB", fill_type="solid")
    alt_fill = PatternFill(start_color="E8F0FE", end_color="E8F0FE", fill_type="solid")
    module_font = Font(name="Calibri", size=10, bold=True, color="1A56DB")
    normal_font = Font(name="Calibri", size=10, color="1F2A37")
    total_font = Font(name="Calibri", size=11, bold=True, color="1A56DB")
    center_align = Alignment(horizontal="center", vertical="center", wrap_text=True)
    left_align = Alignment(horizontal="left", vertical="center", wrap_text=True)
    thin_border = Border(
        left=Side(style="thin", color="D1D5DB"),
        right=Side(style="thin", color="D1D5DB"),
        top=Side(style="thin", color="D1D5DB"),
        bottom=Side(style="thin", color="D1D5DB"),
    )

    # ---- Sheet 1: Programa ----
    ws1 = wb.active
    ws1.title = "Programa"
    ws1.cell(row=1, column=1, value="Dato").font = header_font
    ws1.cell(row=1, column=1).fill = header_fill
    ws1.cell(row=1, column=1).alignment = center_align
    ws1.cell(row=1, column=1).border = thin_border
    ws1.cell(row=1, column=2, value="Detalle").font = header_font
    ws1.cell(row=1, column=2).fill = header_fill
    ws1.cell(row=1, column=2).alignment = center_align
    ws1.cell(row=1, column=2).border = thin_border

    facts = [
        ("Título", PROGRAM["title"]),
        ("Titulación", PROGRAM["titulacion"]),
        ("Horas lectivas", PROGRAM["hours"]),
        ("Créditos", f"{PROGRAM['ects']} ECTS"),
        ("Modalidad", PROGRAM["modalidad"]),
        ("Idioma", PROGRAM["idioma"]),
        ("Duración", PROGRAM["duracion"]),
        ("Edición", PROGRAM["edicion"]),
        ("Inicio de clases", PROGRAM["inicio"]),
        ("Fin de clases", PROGRAM["fin"]),
        ("Horario", PROGRAM["horario"]),
        ("Dirección académica", PROGRAM["direccion"]),
        ("Estructura", "6 módulos + Proyecto Final"),
        ("Referencia", PROGRAM["url"]),
    ]
    for ri, (k, v) in enumerate(facts, 2):
        c0 = ws1.cell(row=ri, column=1, value=k)
        c0.font = module_font
        c0.alignment = left_align
        c0.border = thin_border
        c1 = ws1.cell(row=ri, column=2, value=v)
        c1.font = normal_font
        c1.alignment = left_align
        c1.border = thin_border
        if ri % 2 == 0:
            c0.fill = alt_fill
            c1.fill = alt_fill
    ws1.column_dimensions["A"].width = 22
    ws1.column_dimensions["B"].width = 75

    # ---- Sheet 2: Calendario (dated sessions) ----
    wsc = wb.create_sheet("Calendario")
    sessions, buffer = build_calendar()
    headers_c = ["Sesión", "Fecha", "Día", "Horario", "Módulo", "Tema de la sesión", "Duración", "Horas acum."]
    for ci, header in enumerate(headers_c, 1):
        cell = wsc.cell(row=1, column=ci, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = center_align
        cell.border = thin_border

    row_num = 2
    for s in sessions:
        vals = [
            s["n"],
            s["date"].strftime("%d/%m/%Y"),
            s["day"],
            "18:00–21:00",
            s["module_id"],
            s["theme"],
            f"{SESSION_HOURS}h",
            f"{s['acc_hours']}h",
        ]
        is_alt = row_num % 2 == 0
        for ci, val in enumerate(vals, 1):
            cell = wsc.cell(row=row_num, column=ci, value=val)
            cell.font = module_font if ci in (1, 5) else normal_font
            cell.alignment = left_align if ci == 6 else center_align
            cell.border = thin_border
            if is_alt:
                cell.fill = alt_fill
        row_num += 1

    # Buffer / recuperación rows
    for bd in buffer:
        dias = {1: "Martes", 3: "Jueves"}
        vals = ["—", bd.strftime("%d/%m/%Y"), dias[bd.weekday()], "18:00–21:00",
                "—", "Reserva / recuperación", f"{SESSION_HOURS}h", ""]
        for ci, val in enumerate(vals, 1):
            cell = wsc.cell(row=row_num, column=ci, value=val)
            cell.font = normal_font
            cell.alignment = left_align if ci == 6 else center_align
            cell.border = thin_border
        row_num += 1

    # Total row
    wsc.cell(row=row_num, column=1, value="TOTAL").font = total_font
    wsc.cell(row=row_num, column=6, value=f"{len(sessions)} sesiones").font = total_font
    wsc.cell(row=row_num, column=8, value=PROGRAM["hours"]).font = total_font
    for ci in range(1, 9):
        wsc.cell(row=row_num, column=ci).border = thin_border

    widths_c = [8, 12, 9, 12, 9, 62, 9, 11]
    for ci, w in enumerate(widths_c, 1):
        wsc.column_dimensions[get_column_letter(ci)].width = w

    # ---- Sheet 3: Módulos ----
    ws2 = wb.create_sheet("Módulos")
    headers2 = ["Módulo", "Título", "ECTS", "Horas", "Unidades / contenidos"]
    for ci, header in enumerate(headers2, 1):
        cell = ws2.cell(row=1, column=ci, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = center_align
        cell.border = thin_border

    for ri, mod in enumerate(MODULES, 2):
        units = " · ".join(u["title"] for u in mod["units"])
        vals = [mod["id"], mod["title"], mod["ects"], f"{mod['hours']}h", units]
        is_alt = ri % 2 == 0
        for ci, val in enumerate(vals, 1):
            cell = ws2.cell(row=ri, column=ci, value=val)
            cell.font = module_font if ci == 1 else normal_font
            cell.alignment = center_align if ci in (1, 3, 4) else left_align
            cell.border = thin_border
            if is_alt:
                cell.fill = alt_fill

    total_row = len(MODULES) + 2
    ws2.cell(row=total_row, column=1, value="TOTAL").font = total_font
    ws2.cell(row=total_row, column=3, value=PROGRAM["ects"]).font = total_font
    ws2.cell(row=total_row, column=4, value=PROGRAM["hours"]).font = total_font
    for ci in range(1, 6):
        ws2.cell(row=total_row, column=ci).border = thin_border
        ws2.cell(row=total_row, column=ci).alignment = center_align if ci in (1, 3, 4) else left_align

    widths2 = [10, 52, 8, 8, 60]
    for ci, w in enumerate(widths2, 1):
        ws2.column_dimensions[get_column_letter(ci)].width = w

    # ---- Sheet 3: Contenidos detallados ----
    ws3 = wb.create_sheet("Contenidos detallados")
    headers3 = ["Módulo", "Unidad", "Contenido"]
    for ci, header in enumerate(headers3, 1):
        cell = ws3.cell(row=1, column=ci, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = center_align
        cell.border = thin_border

    row_num = 2
    for mi, mod in enumerate(MODULES):
        for unit in mod["units"]:
            for topic in unit["topics"]:
                is_alt = mi % 2 == 1
                vals = [mod["id"], unit["title"], topic]
                for ci, val in enumerate(vals, 1):
                    cell = ws3.cell(row=row_num, column=ci, value=val)
                    cell.font = module_font if ci == 1 else normal_font
                    cell.alignment = center_align if ci == 1 else left_align
                    cell.border = thin_border
                    if is_alt:
                        cell.fill = alt_fill
                row_num += 1

    widths3 = [10, 42, 95]
    for ci, w in enumerate(widths3, 1):
        ws3.column_dimensions[get_column_letter(ci)].width = w

    path = os.path.join(os.path.dirname(__file__), "Calendario_Postgrado_Kubernetes.xlsx")
    wb.save(path)
    print(f"XLSX saved: {path}")
    return path


def generate_calendar_md():
    """Generate the public Markdown calendar from the canonical schedule data."""
    sessions, buffer = build_calendar()
    lines = [
        "# Calendario",
        "",
        f"**{PROGRAM['title']}** · {PROGRAM['edicion']} · {PROGRAM['modalidad']}",
        "",
        (
            f"**{len(sessions)} sesiones de {SESSION_HOURS}h** · "
            f"{PROGRAM['inicio']}–{PROGRAM['fin']} · {PROGRAM['horario']}"
        ),
        "",
        (
            "> Las columnas de profesorado quedan pendientes de completar cuando se cierre "
            "la asignación docente."
        ),
        "",
        "| Semana | Fecha | Día | Sesión | Título | Asignatura | Horario | Profesor/a 1 | Profesor/a 2 |",
        "| ------ | ----- | --- | ------ | ------ | ---------- | ------- | ------------ | ------------ |",
    ]

    for session in sessions:
        lines.append(
            "| {week} | {date} | {day} | {number} | {title} | {module} · {module_title} | "
            "18:00–21:00 |  |  |".format(
                week=session["date"].isocalendar().week,
                date=session["date"].strftime("%d/%m/%Y"),
                day=session["day"],
                number=session["n"],
                title=session["theme"],
                module=session["module_id"],
                module_title=session["module_title"],
            )
        )

    for date in buffer:
        day = {1: "Martes", 3: "Jueves"}[date.weekday()]
        lines.append(
            f"| {date.isocalendar().week} | {date.strftime('%d/%m/%Y')} | {day} | — | "
            "Reserva / recuperación | — | 18:00–21:00 |  |  |"
        )

    lines.extend([
        "",
        "## Fechas no lectivas",
        "",
        "| Fecha | Motivo |",
        "| ----- | ------ |",
    ])
    for date_tuple, reason in sorted(NON_TEACHING.items()):
        from datetime import date

        date_value = date(*date_tuple)
        lines.append(f"| {date_value.strftime('%d/%m/%Y')} | {reason} |")

    lines.extend([
        "",
        (
            "El desarrollo de cada sesión, incluidos objetivos, contenidos y laboratorios, "
            "está disponible en el "
            "[roadmap detallado](roadmap-postgrado-kubernetes-detallado.md)."
        ),
        "",
    ])

    path = os.path.join(os.path.dirname(__file__), "calendario.md")
    with open(path, "w", encoding="utf-8") as calendar_file:
        calendar_file.write("\n".join(lines))
    print(f"Markdown calendar saved: {path}")
    return path


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    generate_docx()
    generate_xlsx()
    generate_calendar_md()
    print("Done!")
