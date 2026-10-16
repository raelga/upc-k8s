# Posgrado en Platform Engineering y DevOps con Kubernetes — edición 2026–2027

UPC School · Curso 305300 · Live online · Castellano · 12 ECTS.

**30 sesiones de 3 horas (90h)**, martes y jueves de 18:00 a 21:00, zona horaria **Europe/Madrid**. Inicio: **03/11/2026**. Fin: **18/03/2027**, con presentación y defensa del Trabajo Final. Las 29 clases de contenido terminan el **11/03/2027**; el desarrollo del proyecto es trabajo autónomo y el **16/03 no hay clase**.

[Syllabus resumido](syllabus-resumido.md) · [Calendario](calendario.md).

## Metodología y prerrequisitos

Dirigido a perfiles junior con conocimientos básicos de Linux, redes y scripting. Las clases cloud introducen los recursos que se utilizarán para desplegar Kubernetes: identidad, instancias, redes, balanceadores y almacenamiento, seguidos de su aprovisionamiento como código. Python se practica progresivamente en proveedores; Bash en pipelines; Go en el ejemplo de operator. La IA apoya la escritura/adaptación de código, cuya ejecución y resultados se verifican.

Una aplicación Python de dos servicios conecta Kubernetes, observabilidad, CI/GitOps, entrega y escalado. Laboratorios guiados con configuraciones preparadas; permisos, cuotas y costes comprobados; limpieza de recursos al finalizar. EKS/kOps se explican durante su despliegue con un entorno de respaldo disponible. M6 combina conceptos, comparación y demostraciones; operators tiene una clase completa. Los secretos se entregan mediante mecanismos externos y no se guardan en repositorios ni en el estado de Terraform.

## M1 · Formación transversal y créditos

M1 combina **3h propias y 6h integradas**: 9h de contenido incluidas en las 90h del curso. Los 1,5 ECTS incluyen además trabajo autónomo evaluable de adaptación de scripts entre proveedores, validaciones y modificación del ejemplo de Go.

| Sesión | Contenido transversal M1 | Horas incluidas |
|---|---|---:|
| 1 · Fundamentos de DevOps y Platform Engineering | Fundamentos DevOps, cultura, plataformas y métricas | 3h |
| 2 · AWS: fundamentos y aprovisionamiento como código | Python para consultar recursos; generación y revisión de código con IA | 1h |
| 3 · Azure: fundamentos y aprovisionamiento como código | Adaptación de scripts, configuración y tratamiento de resultados | 1h |
| 4 · GCP: fundamentos y aprovisionamiento como código | Reutilización de la automatización y comparación de implementaciones | 1h |
| 19 · Automatización de pipelines: scripting, Tekton y Trivy | Bash/Python, errores, validaciones y ejecución automatizada | 1,5h |
| 25 · Desarrollo de operators: Go y Kubebuilder/Operator SDK | Go aplicado y lectura/modificación del controlador | 1,5h |

Las horas compartidas no se suman de nuevo al total. La docencia corresponde al profesor de cada clase.

## M1 · Fundamentos DevOps, Platform Engineering y Programación para Infraestructura

1 sesión · 3h · 1.5 ECTS.

### Sesión 1 · Fundamentos de DevOps y Platform Engineering

**Fecha:** 03/11/2026 · 18:00–21:00 · **Docente:** René Serral.

**Contenido de M1:** Fundamentos DevOps, cultura, plataformas y métricas. **Dedicación:** 3h incluidas en esta clase.

**Objetivo:** Relacionar DevOps, SRE y Platform Engineering con necesidades de una organización.

**Contenido principal:**

- CALMS y prácticas DevOps.
- IDP, golden paths y experiencia de desarrollo.
- Team Topologies y métricas DORA.

**Práctica / evidencia:** Propuesta breve de plataforma para una empresa: usuarios, capacidades y criterios de éxito.

**Ampliación:** Implantación completa de Backstage y diseño organizativo en profundidad.

## M2 · Cloud Computing Multicloud e Infraestructura como Código

3 sesiones · 9h · 1 ECTS.

### Sesión 2 · AWS: fundamentos y aprovisionamiento como código

**Fecha:** 05/11/2026 · 18:00–21:00 · **Docente:** Rael Garcia.

**Contenido de M1:** Python para consultar recursos; generación y revisión de código con IA. **Dedicación:** 1h incluidas en esta clase.

**Objetivo:** Entender una infraestructura AWS pequeña y verificar su funcionamiento mediante código.

**Contenido principal:**

- IAM, regiones y zonas.
- VPC, subredes, Security Groups, EC2 y S3, contexto de ECR.
- HCL, provider, recursos, variables y plan/apply/destroy.
- Consulta Python preparada e IA para adaptar código.

**Práctica / evidencia:** Lanzar el ejemplo preparado, explicar mientras se despliega, modificar una variable, consultar recursos y verificar limpieza.

**Ampliación:** Curso completo de HCL/boto3; diseño autónomo desde cero; catálogo exhaustivo de bases de datos, mensajería y serverless.

### Sesión 3 · Azure: fundamentos y aprovisionamiento como código

**Fecha:** 10/11/2026 · 18:00–21:00 · **Docente:** Rael Garcia.

**Contenido de M1:** Adaptación de scripts, configuración y tratamiento de resultados. **Dedicación:** 1h incluidas en esta clase.

**Objetivo:** Transferir el patrón de AWS a Azure y reconocer diferencias de identidad y red.

**Contenido principal:**

- Entra ID, suscripciones, grupos de recursos y Managed Identities.
- VNet, NSG, VM y Blob Storage, contexto de ACR.
- Variables, outputs y módulos existentes.
- Adaptación del script Python.

**Práctica / evidencia:** Reproducir el caso común con configuración preparada y explicar equivalencias y diferencias.

**Ampliación:** SDK Azure completo; diseño avanzado de módulos; catálogo exhaustivo de servicios gestionados.

### Sesión 4 · GCP: fundamentos y aprovisionamiento como código

**Fecha:** 12/11/2026 · 18:00–21:00 · **Docente:** Rael Garcia.

**Contenido de M1:** Reutilización de la automatización y comparación de implementaciones. **Dedicación:** 1h incluidas en esta clase.

**Objetivo:** Aplicar el caso común en GCP y comparar proveedores y formas de definir infraestructura.

**Contenido principal:**

- Proyectos, cuentas de servicio e IAM.
- VPC, firewall, Compute Engine y Cloud Storage, contexto de Artifact Registry.
- Estado local/remoto, permisos y locking según backend.
- Pulumi con Python frente a HCL durante 10–15 minutos.

**Práctica / evidencia:** Adaptar el caso preparado, consultar recursos y comparar identidad, red, estado y portabilidad.

**Ampliación:** Laboratorio propio de Pulumi; SDK completo; módulos propios avanzados.

## M3 · Contenedores y Kubernetes Core. Ecosistema OCI

6 sesiones · 18h · 2 ECTS.

### Sesión 5 · Contenedores y ecosistema OCI: imágenes, runtimes y registros

**Fecha:** 17/11/2026 · 18:00–21:00 · **Docente:** Rael Garcia.

**Objetivo:** Construir, ejecutar y publicar una imagen entendiendo aislamiento y runtime.

**Contenido principal:**

- Namespaces, cgroups y capas OCI.
- Dockerfile y build multi-stage.
- Docker/containerd/CRI-O y CRI.
- Registros e higiene de imágenes.

**Práctica / evidencia:** Construir una imagen pequeña y ejecutar/publicar la aplicación que servirá de hilo conductor.

**Ampliación:** Catálogo de runtimes alternativos y builds in-cluster; firma/SBOM como extras, escaneo se concreta en el pipeline Tekton.

### Sesión 6 · Arquitectura de Kubernetes: API, autenticación y permisos

**Fecha:** 19/11/2026 · 18:00–21:00 · **Docente:** Rael Garcia.

**Objetivo:** Seguir una petición kubectl y distinguir autenticación de autorización.

**Contenido principal:**

- Control plane y nodos.
- API, etcd, reconciliación y ejecución de Pods.
- Kubeconfig, certificados, tokens y ServiceAccounts.
- Role/RoleBinding.
- OIDC y admisión conceptual.

**Práctica / evidencia:** Levantar kind, localizar componentes y comprobar una operación permitida y otra denegada.

**Ampliación:** Integración OIDC avanzada; el montaje interno se aborda en la sesión de clúster desde cero.

### Sesión 7 · Aplicaciones en Kubernetes: workloads, configuración y recursos

**Fecha:** 24/11/2026 · 18:00–21:00 · **Docente:** Rael Garcia.

**Objetivo:** Desplegar una aplicación y gestionar su configuración y ciclo de vida.

**Contenido principal:**

- Pods, Deployments, Jobs y CronJobs.
- ConfigMap/Secret.
- Probes.
- Requests/limits y scheduling básico.
- Namespaces, labels y selectors.

**Práctica / evidencia:** Modificar configuración, observar probes, actualizar la aplicación y comprobar asignación de recursos.

**Ampliación:** Catálogo exhaustivo de controladores y scheduling avanzado.

### Sesión 8 · Persistencia en Kubernetes: almacenamiento y aplicaciones con estado

**Fecha:** 26/11/2026 · 18:00–21:00 · **Docente:** Rael Garcia.

**Objetivo:** Mantener datos y comprender las necesidades de workloads con estado.

**Contenido principal:**

- Volúmenes, PV/PVC, StorageClass y aprovisionamiento dinámico.
- Función de CSI.
- StatefulSet.
- Afinidad y restricciones de ubicación relevantes para almacenamiento.

**Práctica / evidencia:** Añadir persistencia, recrear un Pod y verificar datos y comportamiento del workload.

**Ampliación:** Snapshots/cloning avanzados; comparación exhaustiva de drivers y afinidad avanzada.

### Sesión 9 · Networking en Kubernetes: comunicación y exposición de servicios

**Fecha:** 01/12/2026 · 18:00–21:00 · **Docente:** Rael Garcia.

**Objetivo:** Seguir tráfico entre Pods, descubrir servicios y exponer la aplicación.

**Contenido principal:**

- CNI en Pod→Pod.
- Services y CoreDNS.
- Ejemplo Gateway API y relación con Ingress.
- NetworkPolicy.

**Práctica / evidencia:** Con CNI/controlador preparados, exponer la aplicación, bloquear tráfico y permitir solo conexiones necesarias.

**Ampliación:** Instalación/comparación de múltiples CNI; catálogo completo de rutas; networking avanzado se desarrolla con Traefik/Istio.

### Sesión 10 · Construcción de un clúster Kubernetes componente a componente

**Fecha:** 03/12/2026 · 18:00–21:00 · **Docente:** Rael Garcia.

**Objetivo:** Comprender cómo se ensamblan y autentican los componentes de Kubernetes.

**Contenido principal:**

- PKI, etcd, kube-apiserver, scheduler y controller-manager.
- Kubelet, runtime y kube-proxy.
- Unión de un nodo y TLS bootstrapping.

**Práctica / evidencia:** Arrancar un clúster reducido con material preparado, unir un nodo y ejecutar un Pod.

**Ampliación:** Kubernetes the hard way completo sin ayudas; operación HA y recuperación avanzada.

## M4 · Kubernetes en Producción y Ecosistema Cloud Native

5 sesiones · 15h · 2 ECTS.

### Sesión 11 · Kubernetes en AWS: EKS y clústeres autogestionados con kOps

**Fecha:** 10/12/2026 · 18:00–21:00 · **Docente:** Rael Garcia.

**Objetivo:** Comparar Kubernetes gestionado y autogestionado sobre la misma base AWS.

**Contenido principal:**

- Terraform para lanzar EKS.
- KOps con configuración preparada.
- Control plane, red, identidad y nodos.
- Responsabilidades, upgrades, disponibilidad, costes y recuperación.

**Práctica / evidencia:** Explicar durante ambos despliegues, solapar esperas, desplegar la misma aplicación y comparar; comprobar permisos y disponer de clústeres de respaldo.

**Ampliación:** Dos despliegues diseñados autónomamente; operación avanzada practicada en profundidad.

### Sesión 12 · Kubernetes en Azure y GCP: AKS y GKE

**Fecha:** 15/12/2026 · 18:00–21:00 · **Docente:** Rael Garcia.

**Objetivo:** Aplicar la comparación de operación cloud a Azure y GCP.

**Contenido principal:**

- Identidad de workloads.
- Networking.
- Pools de nodos.
- Actualizaciones y responsabilidad operativa.
- GKE Standard/Autopilot y opciones de AKS.

**Práctica / evidencia:** Demostración preparada de los mismos requisitos y comparación razonada con EKS.

**Ampliación:** Instalaciones completas independientes y catálogo de add-ons de ambos proveedores.

### Sesión 13 · Configuración y empaquetado de aplicaciones: Kustomize y Helm

**Fecha:** 17/12/2026 · 18:00–21:00 · **Docente:** Rael Garcia.

**Objetivo:** Adaptar manifiestos y usar paquetes existentes.

**Contenido principal:**

- Bases, overlays y patches.
- Charts, values, templates y releases.
- Uso combinado de render Helm y Kustomize.
- Chart que instala un operator.

**Práctica / evidencia:** Adaptar la aplicación a dos entornos e instalar/configurar un chart, distinguiendo chart, operator y recursos gestionados.

**Ampliación:** Creación de charts complejos desde cero y catálogo de plugins.

### Sesión 14 · Infraestructura declarativa: DNS, certificados y recursos cloud

**Fecha:** 12/01/2027 · 18:00–21:00 · **Docente:** Rael Garcia.

**Objetivo:** Gestionar DNS, certificados y un recurso cloud mediante controladores declarativos.

**Contenido principal:**

- Registros DNS, resolución y TTL.
- Cloudflare como provider.
- ExternalDNS.
- Issuer/ClusterIssuer y ACME DNS-01.
- Protección del token.
- Crossplane: provider, managed resource y reconciliación; comparación breve con Terraform.

**Práctica / evidencia:** Publicar DNS y verificar HTTPS con ExternalDNS/cert-manager sobre Cloudflare; demostrar con configuración preparada un recurso cloud gestionado por Crossplane.

**Ampliación:** DNSSEC/DoH, operación DNS avanzada, Crossplane Compositions/XRDs avanzados y Composition Functions.

### Sesión 15 · Gestión de secretos externos: Vault y External Secrets Operator

**Fecha:** 14/01/2027 · 18:00–21:00 · **Docente:** Rael Garcia.

**Objetivo:** Separar secretos de manifiestos y aplicar identidad y permisos de acceso.

**Contenido principal:**

- Vault y ESO explícitos del programa.
- Despliegue guiado mediante Helm, operator como opción sin fijar uno.
- Autenticación Kubernetes y política básica.
- SecretStore/ExternalSecret.
- AWS Secrets Manager como alternativa y entrega CSI frente a Secret.

**Práctica / evidencia:** Aplicación consume secreto externo, modificarlo y comprobar sincronización y comportamiento de la aplicación.

**Ampliación:** HA/auto-unseal y operación Vault en producción; implantación completa de todos los backends; no exponer valores sensibles en Terraform state.

## M5 · Observabilidad, GitOps, CI/CD y Networking Avanzado

9 sesiones · 27h · 2 ECTS.

### Sesión 16 · Métricas y alertas: Prometheus, PromQL y Alertmanager

**Fecha:** 19/01/2027 · 18:00–21:00 · **Docente:** David Girón.

**Objetivo:** Detectar fallos mediante métricas y definir cuándo alertar.

**Contenido principal:**

- Contadores/histogramas, labels/cardinalidad.
- Scraping/exporters.
- Operator, ServiceMonitor/PodMonitor.
- Tasas, errores, latencia y agregación.
- Reglas, routing y silencios.
- Introducción Mimir.

**Práctica / evidencia:** kube-prometheus-stack preparado, conectar la app, provocar errores/carga, consultar y comprobar una alerta.

**Ampliación:** HA/federación y operación Mimir; reparto orientativo 20/30/40/25/55/10 min para métricas/recogida/PromQL/alertas/lab/cierre.

### Sesión 17 · Dashboards y logs: Grafana, Loki y Alloy

**Fecha:** 21/01/2027 · 18:00–21:00 · **Docente:** David Girón.

**Objetivo:** Pasar de un síntoma en métricas a mensajes que explican el fallo.

**Contenido principal:**

- Datasources, paneles y variables.
- Dashboard de tráfico/errores/latencia.
- Labels frente a campos de logs.
- Alloy para logs de Pods.
- LogQL, Explore y JSON.

**Práctica / evidencia:** Provocar fallo, detectarlo en el dashboard y localizar logs del mismo intervalo con configuración guiada de Alloy.

**Ampliación:** Grafana as Code y operación avanzada de Loki; no enseñar todas las capacidades de Alloy.

### Sesión 18 · Trazas distribuidas y correlación: OpenTelemetry y Tempo

**Fecha:** 26/01/2027 · 18:00–21:00 · **Docente:** David Girón.

**Objetivo:** Localizar dónde se atasca una petición entre servicios.

**Contenido principal:**

- Spans, contexto y propagación.
- Instrumentación automática.
- Receivers/processors/exporters.
- Tempo/Grafana.
- Trace ID en logs, enlaces y exemplars cuando proceda.

**Práctica / evidencia:** Dos servicios preparados, provocar latencia y recorrer métrica→traza→logs; Collector para trazas y Alloy para logs.

**Ampliación:** SDK en profundidad, instrumentación manual completa, sampling avanzado y operación productiva de Collector/Tempo.

**Preparación:** trace ID en logs, propagación entre servicios y enlaces Grafana comprobados. Alloy y Collector tienen capacidades solapadas; el reparto logs/trazas facilita la continuidad del laboratorio.

### Sesión 19 · Automatización de pipelines: scripting, Tekton y Trivy

**Fecha:** 28/01/2027 · 18:00–21:00 · **Docente:** Rael Garcia.

**Contenido de M1:** Bash/Python, errores, validaciones y ejecución automatizada. **Dedicación:** 1,5h incluidas en esta clase.

**Objetivo:** Automatizar tareas verificables y construir una imagen mediante pipeline.

**Contenido principal:**

- Git mínimo.
- Bash para CLI, errores y resultados, jq.
- Python cuando aporte valor.
- Asistencia de IA y revisión.
- Tasks, Pipelines, PipelineRuns y Workspaces.
- Trivy en CI.
- Escaneo Trivy: interpretación de resultados, umbral de fallo y bloqueo de publicación.

**Práctica / evidencia:** Conectar tareas preparadas build → test → scan → publicación; provocar un fallo de Trivy, interpretar el resultado, corregir la imagen y repetir el pipeline.

**Ampliación:** Curso completo de Bash/Python; Triggers/Chains avanzados y attestations.

**Continuidad:** Git mínimo antes de ejecutar pipelines; colaboración mediante PR en la sesión posterior. Puente Prow/Tekton preparado: no asumir integración automática universal.

### Sesión 20 · Colaboración y validación de cambios: Git y Prow

**Fecha:** 02/02/2027 · 18:00–21:00 · **Docente:** Rael Garcia.

**Objetivo:** Conectar un cambio revisado con las comprobaciones conocidas de CI.

**Contenido principal:**

- Ramas, commits, PR, revisión y conflictos sencillos.
- ProwJobs, plugins, Tide y Deck como visión operativa.
- Relación con pipeline Tekton.

**Práctica / evidencia:** Prow preparado, abrir un PR, observar validaciones y resolver un fallo antes del merge.

**Ampliación:** Instalación completa de Prow; internals/monorepos/operaciones Git avanzadas.

### Sesión 21 · Despliegue declarativo y reconciliación: GitOps con ArgoCD

**Fecha:** 04/02/2027 · 18:00–21:00 · **Docente:** Rael Garcia.

**Objetivo:** Reconciliar el estado del repositorio con Kubernetes.

**Contenido principal:**

- Declarativo, versionado y pull.
- Application, diferencias, health y sync policies.
- Helm/Kustomize.
- Drift y corrección.

**Práctica / evidencia:** Desplegar imagen producida por CI, modificar manifiesto mediante PR, observar sync y provocar drift manual.

**Ampliación:** ApplicationSets avanzado, multi-tenancy, SSO y catálogo completo de hooks/waves.

### Sesión 22 · Entrada de tráfico y service mesh: Traefik e Istio

**Fecha:** 11/02/2027 · 18:00–21:00 · **Docente:** David Girón.

**Objetivo:** Distinguir entrada externa y comunicación segura entre servicios.

**Contenido principal:**

- Traefik para routing/TLS con cert-manager.
- Istio para mTLS y política de acceso.
- Reparto entre versiones como preparación de Rollouts.

**Práctica / evidencia:** Componentes preparados, modificar pocas reglas, comprobar acceso y comunicación y observar reparto de tráfico.

**Ampliación:** Instalación desde cero, catálogo de middlewares, TCP/UDP, tuning Envoy y Ambient Mesh profundo.

### Sesión 23 · Entrega progresiva: canary y blue/green con Argo Rollouts

**Fecha:** 16/02/2027 · 18:00–21:00 · **Docente:** David Girón.

**Objetivo:** Desplegar versiones con métricas que deciden avance o rollback.

**Contenido principal:**

- Canary y blue/green.
- Rollouts.
- Integración con ArgoCD, Prometheus e Istio/Traefik.
- Análisis y rollback.

**Práctica / evidencia:** Canary principal sobre la misma app, provocar degradación y comprobar retorno; blue/green como comparación.

**Ampliación:** Feature flags/Flagger/OpenFeature y estrategias avanzadas; no repetir instalación de networking.

### Sesión 24 · Escalado de aplicaciones y nodos: HPA, VPA, KEDA y Karpenter

**Fecha:** 18/02/2027 · 18:00–21:00 · **Docente:** David Girón.

**Objetivo:** Distinguir ajuste de recursos, réplicas y capacidad de nodos.

**Contenido principal:**

- HPA por CPU como práctica principal.
- Recomendaciones VPA.
- KEDA por eventos y su uso de HPA.
- Karpenter ante Pods pendientes y consolidación.

**Práctica / evidencia:** Generar carga, observar HPA; consulta VPA; demos preparadas de cola KEDA y provisión/consolidación de nodos.

**Ampliación:** Catálogo triggers, métricas complejas, tuning, políticas Spot/capacidad y optimización profunda de costes; evitar controladores compitiendo.

**Preparación:** VPA en recomendación; HPA y KEDA no compiten sobre el mismo workload. Karpenter con infraestructura y permisos preparados.

## M6 · Platform Engineering Avanzado: Operators, Serverless y Multi-Cluster

5 sesiones · 15h · 2 ECTS.

Enfoque: problema → concepto → ejemplo → cuándo usarlo. Docencia: Rael Garcia (operators) y Marc Catrisse (resto del bloque).

### Sesión 25 · Desarrollo de operators: Go y Kubebuilder/Operator SDK

**Fecha:** 23/02/2027 · 18:00–21:00 · **Docente:** Rael Garcia.

**Contenido de M1:** Go aplicado y lectura/modificación del controlador. **Dedicación:** 1,5h incluidas en esta clase.

**Objetivo:** Reconocer cuándo un operator automatiza conocimiento operativo.

**Contenido principal:**

- CRD, estado deseado y reconciliación.
- Go mínimo para leer tipos/structs/errores.
- Organización de Kubebuilder/Operator SDK.

**Práctica / evidencia:** Leer un operator preparado, crear un recurso, observar actuación y modificar un comportamiento pequeño.

**Ampliación:** Curso Go, Cobra/Viper, concurrencia avanzada y operator desarrollado desde cero.

### Sesión 26 · Políticas de admisión y recuperación: OPA/Gatekeeper y Velero

**Fecha:** 25/02/2027 · 18:00–21:00 · **Docente:** Marc Catrisse.

**Objetivo:** Aplicar políticas de admisión y recuperar una aplicación tras una pérdida de recursos.

**Contenido principal:**

- Admisión de recursos; PSA como contexto y OPA/Gatekeeper como motor del ejemplo.
- ConstraintTemplates y Constraints mediante una política preparada; rechazo y corrección de un recurso.
- Velero: copia y restauración, alcance de recursos y datos, dependencias y límites de recuperación.

**Práctica / evidencia:** Aplicar una política OPA/Gatekeeper, rechazar y corregir un recurso; realizar backup, borrar y restaurar una aplicación con Velero.

**Ampliación:** Políticas Rego complejas, catálogo de políticas, recuperación productiva avanzada, firmas y attestations.

### Sesión 27 · Gestión de clústeres: Cluster API y Hosted Control Planes

**Fecha:** 02/03/2027 · 18:00–21:00 · **Docente:** Marc Catrisse.

**Objetivo:** Comparar automatización del ciclo de vida y ubicación del control plane.

**Contenido principal:**

- Cluster API: creación/escalado/upgrades.
- HyperShift, vCluster y Kamaji: aislamiento, arquitectura y casos de uso.
- Enfoques no equivalentes.

**Práctica / evidencia:** Demostraciones preparadas y comparación de responsabilidades, sin asumir integración universal de todas las herramientas.

**Ampliación:** Instalación de todos los productos y operación avanzada.

### Sesión 28 · Serverless en Kubernetes: Knative y Virtual Kubelet

**Fecha:** 04/03/2027 · 18:00–21:00 · **Docente:** Marc Catrisse.

**Objetivo:** Entender cuándo usar ejecución orientada a demanda sobre Kubernetes.

**Contenido principal:**

- Knative Serving, revisions, routing y scale-to-zero.
- Contexto serverless.
- Virtual Kubelet: nodos virtuales e integración con capacidad de ejecución externa; diferencias con Knative.

**Práctica / evidencia:** Publicar un servicio Knative, observar revisions y scale-to-zero; demostrar con un entorno preparado el modelo de nodo virtual de Virtual Kubelet.

**Ampliación:** Knative Eventing avanzado, plataforma serverless completa y desarrollo de providers Virtual Kubelet.

### Sesión 29 · Conectividad multi-cluster: Istio, Cilium Cluster Mesh y Submariner

**Fecha:** 11/03/2027 · 18:00–21:00 · **Docente:** Marc Catrisse.

**Objetivo:** Comparar conectividad de servicios y redes entre clústeres.

**Contenido principal:**

- Istio multicluster.
- Cilium Cluster Mesh.
- Submariner.
- Identidad, conectividad y limitaciones.
- Distinguir sus ámbitos.

**Práctica / evidencia:** Diagramas y demostración preparada de tráfico entre clústeres, comparando opciones.

**Ampliación:** Desplegar las tres soluciones desde cero.

## PF · Trabajo Final

1 sesión · 3h · 1.5 ECTS.

### Sesión 30 · Presentación y defensa del Trabajo Final

**Fecha:** 18/03/2027 · 18:00–21:00 · **Docente:** René Serral y Rael Garcia.

**Objetivo:** Presentar y justificar una plataforma reproducible integrada durante el curso.

**Contenido principal:**

- Arquitectura, decisiones técnicas y resultados del proyecto.
- Demo end-to-end: despliegue, diagnóstico y recuperación.
- Defensa oral y preguntas.

**Práctica / evidencia:** Presentación del repositorio y documentación, demostración funcional y defensa ante René Serral y Rael Garcia.

**Ampliación:** Ampliaciones voluntarias del proyecto; las tecnologías de profundización no son requisitos obligatorios.

## Trabajo Final

Construcción progresiva de una plataforma a partir de las prácticas: IaC en un proveedor, aplicación Kubernetes, Helm/Kustomize, CI con escaneo, ArgoCD, DNS/TLS, secretos externos, métricas/logs/trazas, seguridad y escalado.

**Entregables:** repositorio reproducible, memoria de arquitectura y decisiones técnicas, runbooks, demo funcional con diagnóstico/recuperación y defensa oral. La evaluación considera funcionalidad, reproducibilidad, seguridad, observabilidad, justificación de decisiones, costes, documentación y defensa. Las ampliaciones avanzadas no son obligatorias.

**Presentación y defensa:** sesión 30, **18/03/2027, 18:00–21:00**, con **René Serral y Rael Garcia**, incluida en las 90h. Desarrollo y consolidación mediante trabajo autónomo durante el curso. La última clase de contenido es el 11/03 y el 16/03 queda libre para finalizar el proyecto.

## Contenidos de ampliación

Material complementario para profundizar mediante trabajo autónomo o formación adicional.

- **Sesión 1 · Fundamentos de DevOps y Platform Engineering:** Implantación completa de Backstage y diseño organizativo en profundidad.
- **Sesión 2 · AWS: fundamentos y aprovisionamiento como código:** Curso completo de HCL/boto3; diseño autónomo desde cero; catálogo exhaustivo de bases de datos, mensajería y serverless.
- **Sesión 3 · Azure: fundamentos y aprovisionamiento como código:** SDK Azure completo; diseño avanzado de módulos; catálogo exhaustivo de servicios gestionados.
- **Sesión 4 · GCP: fundamentos y aprovisionamiento como código:** Laboratorio propio de Pulumi; SDK completo; módulos propios avanzados.
- **Sesión 5 · Contenedores y ecosistema OCI: imágenes, runtimes y registros:** Catálogo de runtimes alternativos y builds in-cluster; firma/SBOM como extras, escaneo se concreta en el pipeline Tekton.
- **Sesión 6 · Arquitectura de Kubernetes: API, autenticación y permisos:** Integración OIDC avanzada; el montaje interno se aborda en la sesión de clúster desde cero.
- **Sesión 7 · Aplicaciones en Kubernetes: workloads, configuración y recursos:** Catálogo exhaustivo de controladores y scheduling avanzado.
- **Sesión 8 · Persistencia en Kubernetes: almacenamiento y aplicaciones con estado:** Snapshots/cloning avanzados; comparación exhaustiva de drivers y afinidad avanzada.
- **Sesión 9 · Networking en Kubernetes: comunicación y exposición de servicios:** Instalación/comparación de múltiples CNI; catálogo completo de rutas; networking avanzado se desarrolla con Traefik/Istio.
- **Sesión 10 · Construcción de un clúster Kubernetes componente a componente:** Kubernetes the hard way completo sin ayudas; operación HA y recuperación avanzada.
- **Sesión 11 · Kubernetes en AWS: EKS y clústeres autogestionados con kOps:** Dos despliegues diseñados autónomamente; operación avanzada practicada en profundidad.
- **Sesión 12 · Kubernetes en Azure y GCP: AKS y GKE:** Instalaciones completas independientes y catálogo de add-ons de ambos proveedores.
- **Sesión 13 · Configuración y empaquetado de aplicaciones: Kustomize y Helm:** Creación de charts complejos desde cero y catálogo de plugins.
- **Sesión 14 · Infraestructura declarativa: DNS, certificados y recursos cloud:** DNSSEC/DoH, operación DNS avanzada, Crossplane Compositions/XRDs avanzados y Composition Functions.
- **Sesión 15 · Gestión de secretos externos: Vault y External Secrets Operator:** HA/auto-unseal y operación Vault en producción; implantación completa de todos los backends; no exponer valores sensibles en Terraform state.
- **Sesión 16 · Métricas y alertas: Prometheus, PromQL y Alertmanager:** HA/federación y operación Mimir; reparto orientativo 20/30/40/25/55/10 min para métricas/recogida/PromQL/alertas/lab/cierre.
- **Sesión 17 · Dashboards y logs: Grafana, Loki y Alloy:** Grafana as Code y operación avanzada de Loki; no enseñar todas las capacidades de Alloy.
- **Sesión 18 · Trazas distribuidas y correlación: OpenTelemetry y Tempo:** SDK en profundidad, instrumentación manual completa, sampling avanzado y operación productiva de Collector/Tempo.
- **Sesión 19 · Automatización de pipelines: scripting, Tekton y Trivy:** Curso completo de Bash/Python; Triggers/Chains avanzados y attestations.
- **Sesión 20 · Colaboración y validación de cambios: Git y Prow:** Instalación completa de Prow; internals/monorepos/operaciones Git avanzadas.
- **Sesión 21 · Despliegue declarativo y reconciliación: GitOps con ArgoCD:** ApplicationSets avanzado, multi-tenancy, SSO y catálogo completo de hooks/waves.
- **Sesión 22 · Entrada de tráfico y service mesh: Traefik e Istio:** Instalación desde cero, catálogo de middlewares, TCP/UDP, tuning Envoy y Ambient Mesh profundo.
- **Sesión 23 · Entrega progresiva: canary y blue/green con Argo Rollouts:** Feature flags/Flagger/OpenFeature y estrategias avanzadas; no repetir instalación de networking.
- **Sesión 24 · Escalado de aplicaciones y nodos: HPA, VPA, KEDA y Karpenter:** Catálogo triggers, métricas complejas, tuning, políticas Spot/capacidad y optimización profunda de costes; evitar controladores compitiendo.
- **Sesión 25 · Desarrollo de operators: Go y Kubebuilder/Operator SDK:** Curso Go, Cobra/Viper, concurrencia avanzada y operator desarrollado desde cero.
- **Sesión 26 · Políticas de admisión y recuperación: OPA/Gatekeeper y Velero:** Políticas Rego complejas, catálogo de políticas, recuperación productiva avanzada, firmas y attestations.
- **Sesión 27 · Gestión de clústeres: Cluster API y Hosted Control Planes:** Instalación de todos los productos y operación avanzada.
- **Sesión 28 · Serverless en Kubernetes: Knative y Virtual Kubelet:** Knative Eventing avanzado, plataforma serverless completa y desarrollo de providers Virtual Kubelet.
- **Sesión 29 · Conectividad multi-cluster: Istio, Cilium Cluster Mesh y Submariner:** Desplegar las tres soluciones desde cero.
- **Sesión 30 · Presentación y defensa del Trabajo Final:** Ampliaciones voluntarias del proyecto; las tecnologías de profundización no son requisitos obligatorios.

**IaC:** taller adicional de diseño de módulos, testing avanzado y automatización.

**Seguridad:** políticas Kyverno avanzadas, firma, SBOM, attestations y conexión del análisis de imágenes con admisión; el principal conserva Trivy en Tekton y OPA/Gatekeeper con Velero.
