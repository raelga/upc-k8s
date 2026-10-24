# Proposta Universitària — Postgrau en Platform Engineering i DevOps amb Kubernetes

---

## Resum de la proposta (màxim 250 paraules)

Aquest postgrau forma enginyers capaços de dissenyar, implementar i operar plataformes internes de desenvolupament (IDP) basades en Kubernetes a escala empresarial. El programa integra els fonaments de DevOps amb les pràctiques avançades de Platform Engineering, cobrint el cicle complet: des de la infraestructura cloud i la programació per a automatització fins als fluxos GitOps, l'observabilitat distribuïda i la gestió multicluster en entorns productius.

Amb 90 hores lectives equivalents a 12 crèdits ECTS, impartides en modalitat *live online*, l'estudi s'estructura en sis mòduls i un projecte final que progressen des dels fonaments (DevOps, programació assistida per IA en Go/Python/Bash, xarxes, Git i cloud computing amb AWS, Azure i GCP) fins a les capacitats avançades de plataforma (operators personalitzats, hosted control planes, serverless i desplegaments multi-cloud). El nucli del programa és Kubernetes, amb 30 hores dedicades a l'arquitectura, els building blocks, l'emmagatzematge, el networking, l'autenticació, la construcció d'un clúster component a component i la seva operació en producció.

El programa incorpora les eines de l'ecosistema CNCF més demandades per la indústria: Terraform, Helm, ArgoCD, Prometheus, Grafana, OpenTelemetry, Istio, Traefik, HashiCorp Vault, External Secrets Operator, Crossplane, Tekton i KEDA, entre d'altres. L'enfocament és eminentment pràctic: cada sessió combina teoria, demos en viu i laboratoris guiats sobre entorns reals multi-cloud.

El perfil de sortida capacita per exercir com a Platform Engineer, Site Reliability Engineer (SRE) o Kubernetes Architect, amb cobertura directa de certificacions oficials com CKA, CKAD, CKS, Terraform Associate i Vault Associate.

---

## Competència o altres informacions (màxim 250 paraules)

### Programes formatius similars

A nivell internacional existeixen programes comparables, encara que la majoria se centren exclusivament en Kubernetes sense cobrir el cicle complet de Platform Engineering:

- **Linux Foundation — Kubernetes Certifications (CKA/CKAD/CKS):** Certificacions de referència que validen competències tècniques en Kubernetes. El nostre programa cobreix directament el temari de les tres certificacions dins dels mòduls M3, M4 i M5.
- **CNCF — Platform Engineering Maturity Model:** Marc de referència publicat per la CNCF que defineix els nivells de maduresa en Platform Engineering. El nostre programa s'alinea amb aquest model, des del nivell provisional fins a l'optimitzat.
- **KubeCon + CloudNativeCon:** La conferència de referència de l'ecosistema cloud native, amb més de 12.000 assistents, evidencia la demanda creixent de professionals especialitzats en Kubernetes i Platform Engineering.

### Documents i informes de referència

- L'informe *State of Kubernetes 2025* de Datadog reporta que el 65% de les organitzacions operen Kubernetes en producció, amb un creixement anual del 20%.
- L'*Accelerate State of DevOps Report 2024* (Google/DORA) confirma que les organitzacions amb pràctiques DevOps madures despleguen 208 vegades més freqüentment.
- L'informe de Gartner *Platform Engineering Will Transform Software Development by 2027* projecta que el 80% de les organitzacions d'enginyeria tindran equips de plataforma.

### Pàgines web de referència

- https://kubernetes.io — Documentació oficial de Kubernetes
- https://www.cncf.io — Cloud Native Computing Foundation
- https://landscape.cncf.io — CNCF Cloud Native Landscape
- https://tag-app-delivery.cncf.io/whitepapers/platforms/ — CNCF Platform Engineering Whitepaper
- https://platformengineering.org — Platform Engineering Community
- https://dora.dev — DORA Metrics i State of DevOps Reports
- https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/ — Certificació CKA
- https://learn.hashicorp.com — Tutorials Terraform i Vault

---

## Continguts de l'estudi (màxim 6 punts)

1. **Fonaments DevOps, Platform Engineering i programació per a infraestructura.** Contextualització del moviment DevOps i la seva evolució cap a Platform Engineering. Competències de programació en Bash, Python i Go orientades a l'automatització d'infraestructura, desenvolupament de CLIs i construcció de controladors per a Kubernetes.

2. **Cloud Computing multi-proveïdor i Infraestructura com a Codi.** Recursos fonamentals d'AWS, Azure i GCP (computació, xarxes, emmagatzematge, identitat i serveis gestionats). Terraform com a eina central de provisionament declaratiu multi-cloud: HCL, state management, mòduls, testing i CI/CD. Xarxes, DNS i CDNs amb Cloudflare. Control de versions avançat amb Git.

3. **Contenidors i Kubernetes Core.** Ecosistema OCI: construcció d'imatges, runtimes, registres i seguretat. Arquitectura completa de Kubernetes: control plane, building blocks (workloads, configuració, scheduling), emmagatzematge (PV/PVC, CSI), networking (Services, Ingress, Gateway API, CNI, Network Policies), autenticació (RBAC, OIDC, admission controllers) i construcció d'un clúster component a component.

4. **Kubernetes en producció i ecosistema Cloud Native.** Operació de clústers gestionats (EKS, GKE, AKS) i altres entorns. Application bundles (Helm, Kustomize). Infraestructura declarativa dins de Kubernetes: ExternalDNS, cert-manager i Crossplane. Gestió de secrets amb HashiCorp Vault i External Secrets Operator.

5. **Observabilitat, GitOps, CI/CD i networking avançat.** Stack d'observabilitat complet: Prometheus, Grafana (Loki, Tempo, Mimir), OpenTelemetry. GitOps amb ArgoCD i Prow. Pipelines amb Tekton. Networking avançat amb Traefik i Istio (service mesh). Estratègies de desplegament (canary, blue/green) amb Argo Rollouts. Escalat de workloads (HPA, VPA, KEDA, Karpenter).

6. **Platform Engineering avançat: operators, serverless i multi-cluster.** Construcció d'operators personalitzats amb Kubebuilder/Operator SDK. Gestió del cicle de vida de clústers amb Cluster API. Serverless amb Knative. Hosted Control Planes (HyperShift, vCluster, Kamaji). Gestió i desplegament multi-cluster (Istio multicluster, Cilium Cluster Mesh, Submariner) i multi-cloud amb Crossplane. Disaster Recovery amb Velero.

---

## Objectius del procés d'aprenentatge (màxim 6 punts)

1. **Comprendre i aplicar els principis de DevOps i Platform Engineering** per dissenyar Internal Developer Platforms (IDP) que millorin la Developer Experience, establint golden paths, mètriques DORA i estructures organitzatives basades en Team Topologies. L'estudiant serà capaç de definir l'estratègia de plataforma d'una organització.

2. **Dominar la infraestructura cloud multi-proveïdor i la seva gestió declarativa** aprovisionant i operant recursos en AWS, Azure i GCP mitjançant Terraform, amb bones pràctiques de state management, modularització, testing i CI/CD. L'estudiant podrà dissenyar i mantenir infraestructura multi-cloud de forma automatitzada i auditable.

3. **Dissenyar, desplegar i operar clústers Kubernetes en entorns de producció,** comprenent en profunditat l'arquitectura (control plane i data plane), els objectes fonamentals (workloads, storage, networking, RBAC), i les particularitats de cada proveïdor cloud (EKS, GKE, AKS). L'estudiant serà capaç de construir un clúster des de zero i operar-ne de gestionats.

4. **Implementar estratègies completes de gestió de secrets, seguretat i observabilitat** desplegant HashiCorp Vault i External Secrets Operator per a la gestió centralitzada de credencials, i un stack d'observabilitat complet (Prometheus, Grafana, Loki, Tempo, OpenTelemetry) per a la monitorització, alerting i troubleshooting de plataformes distribuïdes.

5. **Establir fluxos de lliurament continu basats en GitOps i networking avançat,** implementant ArgoCD per a la reconciliació declarativa, Tekton per a pipelines CI/CD, i service meshes (Istio, Traefik) per a la gestió avançada del trànsit. L'estudiant sabrà configurar estratègies de desplegament progressiu (canary, blue/green) amb rollback automàtic basat en mètriques.

6. **Construir i operar plataformes avançades multi-cluster i multi-cloud,** desenvolupant operators personalitzats amb Operator Framework, gestionant el cicle de vida de clústers i orquestrant desplegaments distribuïts. L'estudiant podrà dissenyar arquitectures de Disaster Recovery amb Velero i estratègies de failover cross-region.
