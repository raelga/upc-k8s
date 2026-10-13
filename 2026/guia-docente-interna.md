# Guía interna de cobertura y concentración · 2026–2027

Documento de preparación docente. Reúne los mínimos de contenido de la descripción del programa y el alcance práctico de cada clase; no forma parte del syllabus para el alumnado.

Fuente: descripción de asignaturas transcrita de https://upcschool.upc.edu/esp/estudis/formacio/curs/305300/platform-engineering-devops-kubernetes/. Las listas son una distribución docente de esa descripción, no citas literales ni requisitos de instalar todas las herramientas. Los contenidos pueden cambiar de bloque sin perder su cobertura.

**🟢 Cómoda · 🟡 Ajustada con ejemplos preparados · 🔴 Requiere reducir alcance o ampliar tiempo.** El color depende del alcance de práctica previsto. Una mención introductoria y un laboratorio completo no equivalen a la misma profundidad.

30 clases / 90h, incluida la defensa. M1: 9h de contenido propio/transversal, sin duplicarlas en el cómputo.

## Comprobaciones de cobertura prioritarias

- **Git avanzado:** incluir un ejemplo profesional en sesión 20; PR/commits básicos no bastan por sí solos.
- **Terraform:** HCL, estado y módulos en proveedores; testing y CI/CD conectados con sesión 19. No confundir CI de imágenes con validación de IaC.
- **Cloudflare:** además de DNS/ACME, cubrir redes y explicar CDN en sesión 14.
- **OIDC:** incluirlo expresamente en sesión 6; no limitar toda autenticación a certificados/tokens.
- **Go e IA:** mantenerlos en el ejemplo de operators y sus evidencias de trabajo transversal M1.

## 01 · Fundamentos de DevOps y Platform Engineering

**Bloque:** M1 · **Docente:** René · **Concentración:** 🟢

**Cobertura mínima:**

- Contextualización de DevOps y su evolución hacia Platform Engineering.
- Presentar la programación asistida por IA como práctica transversal del curso.

**Condición para mantener la concentración:** Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva.

**Ampliación:** Implantación completa de Backstage y diseño organizativo en profundidad.

## 02 · AWS: fundamentos y aprovisionamiento como código

**Bloque:** M2 · **Docente:** Rael · **Concentración:** 🟡

**Cobertura mínima:**

- Recursos fundamentales AWS: computación, redes, almacenamiento, identidad y servicios gestionados.
- Aprovisionamiento declarativo con Terraform: HCL y recursos.
- Automatización con Python asistida por IA; contenido transversal de M1.

**Implementación / alcance docente:** Python/CLI para comprobaciones; no sustituir recursos cloud por un catálogo de sintaxis.

**Condición para mantener la concentración:** Un ejemplo cloud pequeño, Python preparado y explicación durante aprovisionamiento.

**Ampliación:** Curso completo de HCL/boto3; diseño autónomo desde cero; catálogo exhaustivo de bases de datos, mensajería y serverless.

## 03 · Azure: fundamentos y aprovisionamiento como código

**Bloque:** M2 · **Docente:** Rael · **Concentración:** 🟡

**Cobertura mínima:**

- Recursos fundamentales Azure: computación, redes, almacenamiento, identidad y servicios gestionados.
- Terraform: parametrización y uso de módulos.
- Adaptación de automatización Python asistida por IA; contenido transversal de M1.

**Condición para mantener la concentración:** Reutilizar el patrón AWS; evitar enseñar el SDK completo.

**Ampliación:** SDK Azure completo; diseño avanzado de módulos; catálogo exhaustivo de servicios gestionados.

## 04 · GCP: fundamentos y aprovisionamiento como código

**Bloque:** M2 · **Docente:** Rael · **Concentración:** 🟡

**Cobertura mínima:**

- Recursos fundamentales GCP: computación, redes, almacenamiento, identidad y servicios gestionados.
- Terraform: gestión del estado y comparación del aprovisionamiento multicloud.
- Automatización con Python; contenido transversal de M1.

**Implementación / alcance docente:** Pulumi/OpenTofu son comparaciones complementarias; no están nombrados en la descripción publicada.

**Condición para mantener la concentración:** Reutilizar patrón y estado; Pulumi breve.

**Ampliación:** Laboratorio propio de Pulumi; SDK completo; módulos propios avanzados.

## 05 · Contenedores y ecosistema OCI: imágenes, runtimes y registros

**Bloque:** M3 · **Docente:** Rael · **Concentración:** 🟡

**Cobertura mínima:**

- Ecosistema OCI: construcción de imágenes, runtimes, registros y seguridad.

**Implementación / alcance docente:** Los productos concretos de build/runtime/escaneo son elecciones del laboratorio.

**Condición para mantener la concentración:** Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva.

**Ampliación:** Catálogo de runtimes alternativos y builds in-cluster; firma/SBOM como extras, escaneo se concreta en el pipeline Tekton.

## 06 · Arquitectura de Kubernetes: API, autenticación y permisos

**Bloque:** M3 · **Docente:** Rael · **Concentración:** 🟡

**Cobertura mínima:**

- Arquitectura Kubernetes: plano de control y relación con los nodos.
- Autenticación/autorización: RBAC y OIDC.

**Implementación / alcance docente:** kind es el entorno local elegido; el requisito es explicar arquitectura, RBAC y OIDC.

**Condición para mantener la concentración:** Seguir una petición kubectl; no repetir el montaje manual.

**Ampliación:** Integración OIDC avanzada; el montaje interno se aborda en la sesión de clúster desde cero.

## 07 · Aplicaciones en Kubernetes: workloads, configuración y recursos

**Bloque:** M3 · **Docente:** Rael · **Concentración:** 🟡

**Cobertura mínima:**

- Workloads, configuración y scheduling como bloques fundamentales de Kubernetes.

**Condición para mantener la concentración:** Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva.

**Ampliación:** Catálogo exhaustivo de controladores y scheduling avanzado.

## 08 · Persistencia en Kubernetes: almacenamiento y aplicaciones con estado

**Bloque:** M3 · **Docente:** Rael · **Concentración:** 🟡

**Cobertura mínima:**

- Almacenamiento Kubernetes: PV/PVC y CSI.

**Condición para mantener la concentración:** Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva.

**Ampliación:** Snapshots/cloning avanzados; comparación exhaustiva de drivers y afinidad avanzada.

## 09 · Networking en Kubernetes: comunicación y exposición de servicios

**Bloque:** M3 · **Docente:** Rael · **Concentración:** 🟡

**Cobertura mínima:**

- Networking Kubernetes: Services, Ingress, Gateway API, CNI y Network Policies.

**Implementación / alcance docente:** CoreDNS y el CNI preparado permiten enseñar el recorrido sin comparar todos los productos.

**Condición para mantener la concentración:** CNI/controlador preparados; un recorrido y pocas políticas.

**Ampliación:** Instalación/comparación de múltiples CNI; catálogo completo de rutas; networking avanzado se desarrolla con Traefik/Istio.

## 10 · Construcción de un clúster Kubernetes componente a componente

**Bloque:** M3 · **Docente:** Rael · **Concentración:** 🟡

**Cobertura mínima:**

- Construcción de un clúster Kubernetes componente a componente.

**Condición para mantener la concentración:** Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva.

**Ampliación:** Kubernetes the hard way completo sin ayudas; operación HA y recuperación avanzada.

## 11 · Kubernetes en AWS: EKS y clústeres autogestionados con kOps

**Bloque:** M4 · **Docente:** Rael · **Concentración:** 🟡

**Cobertura mínima:**

- Operación de EKS y de otros entornos Kubernetes.

**Implementación / alcance docente:** kOps es el ejemplo de entorno autogestionado; la web no exige kOps por nombre.

**Condición para mantener la concentración:** Permisos y cuotas comprobados; despliegues solapados y clústeres de respaldo.

**Ampliación:** Dos despliegues diseñados autónomamente; operación avanzada practicada en profundidad.

## 12 · Kubernetes en Azure y GCP: AKS y GKE

**Bloque:** M4 · **Docente:** Rael · **Concentración:** 🟡

**Cobertura mínima:**

- Operación de AKS y GKE.

**Condición para mantener la concentración:** Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva.

**Ampliación:** Instalaciones completas independientes y catálogo de add-ons de ambos proveedores.

## 13 · Configuración y empaquetado de aplicaciones: Kustomize y Helm

**Bloque:** M4 · **Docente:** Rael · **Concentración:** 🟡

**Cobertura mínima:**

- Application bundles: Helm y Kustomize.

**Condición para mantener la concentración:** Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva.

**Ampliación:** Creación de charts complejos desde cero y catálogo de plugins.

## 14 · Infraestructura declarativa: DNS, certificados y recursos cloud

**Bloque:** M4 · **Docente:** Rael · **Concentración:** 🟢

**Cobertura mínima:**

- Redes/DNS/CDN con Cloudflare, en conexión con los fundamentos cloud y la exposición de la aplicación.
- Infraestructura declarativa: ExternalDNS, cert-manager y Crossplane.

**Implementación / alcance docente:** Cloudflare cubre DNS y ACME; dedicar también un ejemplo/explicación a CDN. Crossplane introductorio, sin Compositions complejas.

**Condición para mantener la concentración:** DNS/certificados como práctica principal; Crossplane como demo breve. La cobertura CDN añade presión: limitarla a un ejemplo concreto.

**Ampliación:** DNSSEC/DoH, operación DNS avanzada, Crossplane Compositions/XRDs avanzados y Composition Functions.

## 15 · Gestión de secretos externos: Vault y External Secrets Operator

**Bloque:** M4 · **Docente:** Rael · **Concentración:** 🟡

**Cobertura mínima:**

- Gestión de secretos con HashiCorp Vault y External Secrets Operator.

**Implementación / alcance docente:** AWS Secrets Manager/ASCP son alternativas complementarias; no sustituyen Vault y ESO.

**Condición para mantener la concentración:** Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva.

**Ampliación:** HA/auto-unseal y operación Vault en producción; implantación completa de todos los backends; no exponer valores sensibles en Terraform state.

## 16 · Métricas y alertas: Prometheus, PromQL y Alertmanager

**Bloque:** M5 · **Docente:** David · **Concentración:** 🟡

**Cobertura mínima:**

- Prometheus y Grafana como parte del stack de observabilidad.
- Mimir: explicar su función en el almacenamiento de métricas.

**Implementación / alcance docente:** PromQL, Alertmanager y Operator desarrollan la práctica de métricas; Mimir permanece introductorio.

**Condición para mantener la concentración:** Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva.

**Ampliación:** HA/federación y operación Mimir; reparto orientativo 20/30/40/25/55/10 min para métricas/recogida/PromQL/alertas/lab/cierre.

## 17 · Dashboards y logs: Grafana, Loki y Alloy

**Bloque:** M5 · **Docente:** David · **Concentración:** 🟡

**Cobertura mínima:**

- Grafana y Loki para visualización y logs.

**Implementación / alcance docente:** Alloy es el recolector elegido, no una obligación explícita de la web.

**Condición para mantener la concentración:** Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva.

**Ampliación:** Grafana as Code y operación avanzada de Loki; no enseñar todas las capacidades de Alloy.

## 18 · Trazas distribuidas y correlación: OpenTelemetry y Tempo

**Bloque:** M5 · **Docente:** David · **Concentración:** 🟡

**Cobertura mínima:**

- OpenTelemetry y Tempo como parte del stack de observabilidad completo.

**Implementación / alcance docente:** Collector y correlación son el enfoque de práctica; no desarrollar un curso completo de SDK.

**Condición para mantener la concentración:** Dos servicios preparados, instrumentación automática, trace ID y enlaces comprobados.

**Ampliación:** SDK en profundidad, instrumentación manual completa, sampling avanzado y operación productiva de Collector/Tempo.

## 19 · Automatización de pipelines: scripting, Tekton y Trivy

**Bloque:** M5 · **Docente:** Rael · **Concentración:** 🟡

**Cobertura mínima:**

- Programación Bash asistida por IA aplicada a automatización, con Python cuando corresponda; contenido M1.
- Pipelines con Tekton.
- Testing y CI/CD de Terraform: conectar las prácticas IaC con comprobaciones automatizadas.
- Seguridad de imágenes: aplicación práctica en el pipeline.

**Implementación / alcance docente:** Trivy es la herramienta elegida para escaneo; no está nombrada en la web. El pipeline de imágenes no cubre por sí solo testing/CI de Terraform.

**Condición para mantener la concentración:** Tareas preparadas; reservar tiempo para escaneo y comprobaciones IaC.

**Ampliación:** Curso completo de Bash/Python; Triggers/Chains avanzados y attestations.

## 20 · Colaboración y validación de cambios: Git y Prow

**Bloque:** M5 · **Docente:** Rael · **Concentración:** 🟡

**Cobertura mínima:**

- Control de versiones avanzado con Git.
- GitOps/colaboración con Prow: situar su función junto al flujo GitOps y CI.

**Implementación / alcance docente:** No dar Git avanzado por cubierto únicamente con commit/PR; incluir una operación profesional preparada, sin curso de internals.

**Condición para mantener la concentración:** Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva.

**Ampliación:** Instalación completa de Prow; internals/monorepos/operaciones Git avanzadas.

## 21 · Despliegue declarativo y reconciliación: GitOps con ArgoCD

**Bloque:** M5 · **Docente:** Rael · **Concentración:** 🟡

**Cobertura mínima:**

- GitOps con ArgoCD.

**Condición para mantener la concentración:** Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva.

**Ampliación:** ApplicationSets avanzado, multi-tenancy, SSO y catálogo completo de hooks/waves.

## 22 · Entrada de tráfico y service mesh: Traefik e Istio

**Bloque:** M5 · **Docente:** David · **Concentración:** 🟡

**Cobertura mínima:**

- Networking avanzado con Traefik e Istio, incluyendo service mesh.

**Condición para mantener la concentración:** Componentes preparados; entrada/mTLS como práctica, sin catálogo de routing.

**Ampliación:** Instalación desde cero, catálogo de middlewares, TCP/UDP, tuning Envoy y Ambient Mesh profundo.

## 23 · Entrega progresiva: canary y blue/green con Argo Rollouts

**Bloque:** M5 · **Docente:** David · **Concentración:** 🟡

**Cobertura mínima:**

- Canary y blue/green con Argo Rollouts.

**Condición para mantener la concentración:** Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva.

**Ampliación:** Feature flags/Flagger/OpenFeature y estrategias avanzadas; no repetir instalación de networking.

## 24 · Escalado de aplicaciones y nodos: HPA, VPA, KEDA y Karpenter

**Bloque:** M5 · **Docente:** David · **Concentración:** 🟡

**Cobertura mínima:**

- Escalado de workloads con HPA, VPA, KEDA y Karpenter.

**Condición para mantener la concentración:** HPA como lab; VPA recomendaciones y demos KEDA/Karpenter sin competir por el mismo workload.

**Ampliación:** Catálogo triggers, métricas complejas, tuning, políticas Spot/capacidad y optimización profunda de costes; evitar controladores compitiendo.

## 25 · Desarrollo de operators: Go y Kubebuilder/Operator SDK

**Bloque:** M6 · **Docente:** Profesor UPC · **Concentración:** 🟡

**Cobertura mínima:**

- Construcción de operators personalizados con Kubebuilder/Operator SDK.
- Go aplicado a construcción de controladores; programación asistida por IA como parte transversal de M1.

**Implementación / alcance docente:** La clase completa se reserva a operators; Go se aprende leyendo/modificando el ejemplo.

**Condición para mantener la concentración:** Ejemplo de operator preparado; no añadir Crossplane.

**Ampliación:** Curso Go, Cobra/Viper, concurrencia avanzada y operator desarrollado desde cero.

## 26 · Políticas de admisión y recuperación: OPA/Gatekeeper y Velero

**Bloque:** M6 · **Docente:** Profesor UPC · **Concentración:** 🟡

**Cobertura mínima:**

- Admission controllers como contenido de autenticación/control de Kubernetes.
- Disaster Recovery con Velero.

**Implementación / alcance docente:** OPA/Gatekeeper es la implementación elegida para admisión; la web no exige ese motor por nombre. Kyverno/PSA son alternativas o ampliaciones.

**Condición para mantener la concentración:** Una política y una restauración preparadas; no enseñar Rego ni DR completos.

**Ampliación:** Políticas Rego complejas, catálogo de políticas, recuperación productiva avanzada, firmas y attestations.

## 27 · Gestión de clústeres: Cluster API y Hosted Control Planes

**Bloque:** M6 · **Docente:** Profesor UPC · **Concentración:** 🟡

**Cobertura mínima:**

- Gestión del ciclo de vida de clústeres con Cluster API.
- Hosted Control Planes: HyperShift, vCluster y Kamaji.

**Condición para mantener la concentración:** Visión general y demos; no instalar cuatro plataformas.

**Ampliación:** Instalación de todos los productos y operación avanzada.

## 28 · Serverless en Kubernetes: Knative y Virtual Kubelet

**Bloque:** M6 · **Docente:** Profesor UPC · **Concentración:** 🟢

**Cobertura mínima:**

- Serverless con Knative.

**Implementación / alcance docente:** Virtual Kubelet está incluido por diseño del curso, además del Knative nombrado en la web.

**Condición para mantener la concentración:** Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva.

**Ampliación:** Knative Eventing avanzado, plataforma serverless completa y desarrollo de providers Virtual Kubelet.

## 29 · Conectividad multi-cluster: Istio, Cilium Cluster Mesh y Submariner

**Bloque:** M6 · **Docente:** Profesor UPC · **Concentración:** 🟡

**Cobertura mínima:**

- Gestión/despliegue multi-cluster: Istio multicluster, Cilium Cluster Mesh y Submariner.

**Condición para mantener la concentración:** Comparación y ejemplo entre clústeres, no desplegar tres redes desde cero.

**Ampliación:** Desplegar las tres soluciones desde cero.

## 30 · Presentación y defensa del Trabajo Final

**Bloque:** PF · **Docente:** René y Rael · **Concentración:** 🟡

**Cobertura mínima:**

- Proyecto Final: presentación y defensa del trabajo integrador. La web nombra Proyecto Final; formato/defensa es el diseño docente del curso.

**Implementación / alcance docente:** Una sesión dentro de las 30/90h, impartida por René y Rael; trabajo autónomo previo.

**Condición para mantener la concentración:** Ajustar duración de demos y preguntas al número de equipos.

**Ampliación:** Ampliaciones voluntarias del proyecto; las tecnologías de profundización no son requisitos obligatorios.
