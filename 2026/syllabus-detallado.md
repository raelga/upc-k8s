# Posgrado en Platform Engineering y DevOps con Kubernetes — edición 2026–2027

UPC School · Curso 305300 · Live online · Castellano · 12 ECTS.

El programa se desarrolla en **30 sesiones lectivas de 3 horas (90h)**, los martes y jueves de 18:00 a 21:00, en la zona horaria **Europe/Madrid**. El curso comienza el 03/11/2026 y finaliza el 18/03/2027. El Proyecto Final cuenta con actividades de consolidación y defensa adicionales a las 90 horas lectivas.

Enlaces: [syllabus resumido](syllabus-resumido.md) · [calendario](calendario.md).

## Enfoque docente y prerrequisitos

Dirigido a perfiles junior con conocimientos básicos de Linux, redes y scripting. Las sesiones de proveedores introducen los fundamentos cloud. Una misma aplicación Python con dos servicios conecta cloud, Kubernetes, observabilidad, CI y GitOps. Bash se practica en Tekton; Python aparece progresivamente en proveedores y automatización; Go se usa para comprender el operator. La IA ayuda a escribir/adaptar código que debe revisarse y verificarse.

Laboratorios guiados con manifiestos/configuraciones preparados. Antes de clase se comprueban cuentas, permisos, cuotas, dominios y costes. Se preservan estados reutilizables; para despliegues lentos, especialmente EKS/kOps, se explican conceptos durante la espera y se dispone de un entorno alternativo preparado. Cada práctica cloud incluye limpieza. Secretos y credenciales no se guardan en repositorios, logs ni estado Terraform; crear el contenedor del secreto no implica cargar su valor mediante IaC.

Semáforo: 🟢 alcance cómodo; 🟡 ajustado con material preparado. No mide dificultad de la herramienta ni garantiza tiempo de despliegue. Las amarillas de M6 suponen demostraciones, no implementaciones completas.

## Resultados de aprendizaje

Al terminar, el participante podrá explicar y aplicar un flujo cloud → Kubernetes → observabilidad → CI/GitOps → entrega/escalado; comparar responsabilidades de operación; verificar configuraciones y permisos; y reconocer cuándo usar las tecnologías avanzadas de M6. El alcance guiado no equivale a dominio autónomo de todos los proveedores o productos.

## M1 · Fundamentos DevOps, Platform Engineering y Programación para Infraestructura

1 sesiones · 3h lectivas · 1.5 ECTS.

### Sesión 1 · DevOps y Platform Engineering

**Fecha:** 03/11/2026 · 18:00–21:00 · **Docente:** René · **Concentración:** 🟢.

**Objetivo:** Relacionar DevOps, SRE y Platform Engineering con necesidades de una organización.

**Entrada:** Contexto inicial del programa.

**Contenido principal:**

- CALMS y prácticas DevOps.
- IDP, golden paths y experiencia de desarrollo.
- Team Topologies y métricas DORA.

**Práctica / evidencia:** Propuesta breve de plataforma para una empresa: usuarios, capacidades y criterios de éxito.

**Ampliación:** Implantación completa de Backstage y diseño organizativo en profundidad.

## M2 · Cloud Computing Multicloud e Infraestructura como Código

3 sesiones · 9h lectivas · 1 ECTS.

### Sesión 2 · AWS, Terraform y Python

**Fecha:** 05/11/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Entender una infraestructura AWS pequeña y verificar su funcionamiento mediante código.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- IAM, regiones y zonas.
- VPC, subredes, Security Groups, EC2 y S3, contexto de ECR.
- HCL, provider, recursos, variables y plan/apply/destroy.
- Consulta Python preparada e IA para adaptar código.

**Práctica / evidencia:** Lanzar el ejemplo preparado, explicar mientras se despliega, modificar una variable, consultar recursos y verificar limpieza.

**Ampliación:** Curso completo de HCL/boto3; diseño autónomo desde cero; catálogo exhaustivo de bases de datos, mensajería y serverless.

### Sesión 3 · Azure, Terraform y automatización Python

**Fecha:** 10/11/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Transferir el patrón de AWS a Azure y reconocer diferencias de identidad y red.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Entra ID, suscripciones, grupos de recursos y Managed Identities.
- VNet, NSG, VM y Blob Storage, contexto de ACR.
- Variables, outputs y módulos existentes.
- Adaptación del script Python.

**Práctica / evidencia:** Reproducir el caso común con configuración preparada y explicar equivalencias y diferencias.

**Ampliación:** SDK Azure completo; diseño avanzado de módulos; catálogo exhaustivo de servicios gestionados.

### Sesión 4 · GCP, estado remoto y comparación de IaC

**Fecha:** 12/11/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Aplicar el caso común en GCP y comparar proveedores y formas de definir infraestructura.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Proyectos, cuentas de servicio e IAM.
- VPC, firewall, Compute Engine y Cloud Storage, contexto de Artifact Registry.
- Estado local/remoto, permisos y locking según backend.
- Pulumi con Python frente a HCL durante 10–15 minutos.

**Práctica / evidencia:** Adaptar el caso preparado, consultar recursos y comparar identidad, red, estado y portabilidad.

**Ampliación:** Laboratorio propio de Pulumi; SDK completo; módulos propios avanzados.

## M3 · Contenedores y Kubernetes Core. Ecosistema OCI

7 sesiones · 21h lectivas · 2 ECTS.

### Sesión 5 · Contenedores y ecosistema OCI

**Fecha:** 17/11/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Construir, ejecutar y publicar una imagen entendiendo aislamiento y runtime.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Namespaces, cgroups y capas OCI.
- Dockerfile y build multi-stage.
- Docker/containerd/CRI-O y CRI.
- Registros e higiene de imágenes.

**Práctica / evidencia:** Construir una imagen pequeña y ejecutar/publicar la aplicación que servirá de hilo conductor.

**Ampliación:** Catálogo de runtimes alternativos y builds in-cluster; firma/SBOM como extras, escaneo se concreta en seguridad y Tekton.

### Sesión 6 · Arquitectura, API, kind, autenticación y RBAC

**Fecha:** 19/11/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Seguir una petición kubectl y distinguir autenticación de autorización.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Control plane y nodos.
- API, etcd, reconciliación y ejecución de Pods.
- Kubeconfig, certificados, tokens y ServiceAccounts.
- Role/RoleBinding.
- OIDC y admisión conceptual.

**Práctica / evidencia:** Levantar kind, localizar componentes y comprobar una operación permitida y otra denegada.

**Ampliación:** Integración OIDC avanzada; el montaje interno se aborda en la sesión de clúster desde cero.

### Sesión 7 · Workloads, configuración y recursos

**Fecha:** 24/11/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Desplegar una aplicación y gestionar su configuración y ciclo de vida.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Pods, Deployments, Jobs y CronJobs.
- ConfigMap/Secret.
- Probes.
- Requests/limits y scheduling básico.
- Namespaces, labels y selectors.

**Práctica / evidencia:** Modificar configuración, observar probes, actualizar la aplicación y comprobar asignación de recursos.

**Ampliación:** Catálogo exhaustivo de controladores y scheduling avanzado.

### Sesión 8 · Persistencia, CSI y StatefulSets

**Fecha:** 26/11/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Mantener datos y comprender las necesidades de workloads con estado.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Volúmenes, PV/PVC, StorageClass y aprovisionamiento dinámico.
- Función de CSI.
- StatefulSet.
- Afinidad y restricciones de ubicación relevantes para almacenamiento.

**Práctica / evidencia:** Añadir persistencia, recrear un Pod y verificar datos y comportamiento del workload.

**Ampliación:** Snapshots/cloning avanzados; comparación exhaustiva de drivers y afinidad avanzada.

### Sesión 9 · Networking y exposición de aplicaciones

**Fecha:** 01/12/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Seguir tráfico entre Pods, descubrir servicios y exponer la aplicación.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- CNI en Pod→Pod.
- Services y CoreDNS.
- Ejemplo Gateway API y relación con Ingress.
- NetworkPolicy.

**Práctica / evidencia:** Con CNI/controlador preparados, exponer la aplicación, bloquear tráfico y permitir solo conexiones necesarias.

**Ampliación:** Instalación/comparación de múltiples CNI; catálogo completo de rutas; networking avanzado se desarrolla con Traefik/Istio.

### Sesión 10 · Clúster componente a componente

**Fecha:** 03/12/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Comprender cómo se ensamblan y autentican los componentes de Kubernetes.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- PKI, etcd, kube-apiserver, scheduler y controller-manager.
- Kubelet, runtime y kube-proxy.
- Unión de un nodo y TLS bootstrapping.

**Práctica / evidencia:** Arrancar un clúster reducido con material preparado, unir un nodo y ejecutar un Pod.

**Ampliación:** Kubernetes the hard way completo sin ayudas; operación HA y recuperación avanzada.

### Sesión 11 · Seguridad de imágenes y políticas de admisión

**Fecha:** 10/12/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Distinguir análisis de imagen y control de recursos admitidos.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Trivy e interpretación de vulnerabilidades.
- PSA.
- Kyverno como herramienta práctica.
- OPA/Gatekeeper como comparación breve.

**Práctica / evidencia:** Revisar una imagen, rechazar un Pod privilegiado o que incumpla una política, corregirlo y comprobar admisión.

**Ampliación:** Firmas, SBOM, attestations y conexión automática entre escaneo/admisión; segundo motor de políticas completo.

## M4 · Kubernetes en Producción y Ecosistema Cloud Native

5 sesiones · 15h lectivas · 2 ECTS.

### Sesión 12 · EKS y kOps en AWS

**Fecha:** 15/12/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Comparar Kubernetes gestionado y autogestionado sobre la misma base AWS.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Terraform para lanzar EKS.
- KOps con configuración preparada.
- Control plane, red, identidad y nodos.
- Responsabilidades, upgrades, disponibilidad, costes y recuperación.

**Práctica / evidencia:** Explicar durante ambos despliegues, solapar esperas, desplegar la misma aplicación y comparar; comprobar permisos y disponer de clústeres de respaldo.

**Ampliación:** Dos despliegues diseñados autónomamente; operación avanzada practicada en profundidad.

### Sesión 13 · AKS y GKE

**Fecha:** 17/12/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Aplicar la comparación de operación cloud a Azure y GCP.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Identidad de workloads.
- Networking.
- Pools de nodos.
- Actualizaciones y responsabilidad operativa.
- GKE Standard/Autopilot y opciones de AKS.

**Práctica / evidencia:** Demostración preparada de los mismos requisitos y comparación razonada con EKS.

**Ampliación:** Instalaciones completas independientes y catálogo de add-ons de ambos proveedores.

### Sesión 14 · Kustomize y Helm

**Fecha:** 22/12/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Adaptar manifiestos y usar paquetes existentes.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Bases, overlays y patches.
- Charts, values, templates y releases.
- Uso combinado de render Helm y Kustomize.
- Chart que instala un operator.

**Práctica / evidencia:** Adaptar la aplicación a dos entornos e instalar/configurar un chart, distinguiendo chart, operator y recursos gestionados.

**Ampliación:** Creación de charts complejos desde cero y catálogo de plugins.

### Sesión 15 · DNS y HTTPS con Cloudflare, ExternalDNS y cert-manager

**Fecha:** 07/01/2027 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟢.

**Objetivo:** Publicar una aplicación con dominio y certificados renovables.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Registros DNS, resolución y TTL.
- Cloudflare como provider.
- ExternalDNS.
- Issuer/ClusterIssuer y ACME DNS-01.
- Protección del token.

**Práctica / evidencia:** Instalar componentes por Helm sobre el entorno anterior, publicar el registro y verificar HTTPS y renovación.

**Ampliación:** DNSSEC/DoH y operación DNS avanzada.

### Sesión 16 · Secretos externos: Vault y External Secrets Operator

**Fecha:** 12/01/2027 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Separar secretos de manifiestos y aplicar identidad y permisos de acceso.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Vault y ESO explícitos del programa.
- Despliegue guiado mediante Helm, operator como opción sin fijar uno.
- Autenticación Kubernetes y política básica.
- SecretStore/ExternalSecret.
- AWS Secrets Manager como alternativa y entrega CSI frente a Secret.

**Práctica / evidencia:** Aplicación consume secreto externo, modificarlo y comprobar sincronización y comportamiento de la aplicación.

**Ampliación:** HA/auto-unseal y operación Vault en producción; implantación completa de todos los backends; no exponer valores sensibles en Terraform state.

## M5 · Observabilidad, GitOps, CI/CD y Networking Avanzado

9 sesiones · 27h lectivas · 2 ECTS.

### Sesión 17 · Prometheus, PromQL y Alertmanager

**Fecha:** 14/01/2027 · 18:00–21:00 · **Docente:** David · **Concentración:** 🟡.

**Objetivo:** Detectar fallos mediante métricas y definir cuándo alertar.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Contadores/histogramas, labels/cardinalidad.
- Scraping/exporters.
- Operator, ServiceMonitor/PodMonitor.
- Tasas, errores, latencia y agregación.
- Reglas, routing y silencios.
- Introducción Mimir.

**Práctica / evidencia:** kube-prometheus-stack preparado, conectar la app, provocar errores/carga, consultar y comprobar una alerta.

**Ampliación:** HA/federación y operación Mimir; reparto orientativo 20/30/40/25/55/10 min para métricas/recogida/PromQL/alertas/lab/cierre.

### Sesión 18 · Grafana, Loki y Alloy

**Fecha:** 19/01/2027 · 18:00–21:00 · **Docente:** David · **Concentración:** 🟡.

**Objetivo:** Pasar de un síntoma en métricas a mensajes que explican el fallo.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Datasources, paneles y variables.
- Dashboard de tráfico/errores/latencia.
- Labels frente a campos de logs.
- Alloy para logs de Pods.
- LogQL, Explore y JSON.

**Práctica / evidencia:** Provocar fallo, detectarlo en el dashboard y localizar logs del mismo intervalo con configuración guiada de Alloy.

**Ampliación:** Grafana as Code y operación avanzada de Loki; no enseñar todas las capacidades de Alloy.

### Sesión 19 · OpenTelemetry, Collector, Tempo y correlación

**Fecha:** 21/01/2027 · 18:00–21:00 · **Docente:** David · **Concentración:** 🟡.

**Objetivo:** Localizar dónde se atasca una petición entre servicios.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Spans, contexto y propagación.
- Instrumentación automática.
- Receivers/processors/exporters.
- Tempo/Grafana.
- Trace ID en logs, enlaces y exemplars cuando proceda.

**Práctica / evidencia:** Dos servicios preparados, provocar latencia y recorrer métrica→traza→logs; Collector para trazas y Alloy para logs.

**Ampliación:** SDK en profundidad, instrumentación manual completa, sampling avanzado y operación productiva de Collector/Tempo.

**Preparación específica:** propagación de contexto entre dos servicios, trace ID en logs y enlaces de Grafana comprobados. Alloy y Collector tienen capacidades solapadas: el reparto logs/trazas elegido es una decisión del lab, no una limitación de las herramientas.

### Sesión 20 · Scripting y pipelines con Tekton

**Fecha:** 26/01/2027 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Automatizar tareas verificables y construir una imagen mediante pipeline.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Git mínimo.
- Bash para CLI, errores y resultados, jq.
- Python cuando aporte valor.
- Asistencia de IA y revisión.
- Tasks, Pipelines, PipelineRuns y Workspaces.
- Trivy en CI.

**Práctica / evidencia:** Conectar tareas preparadas de build/test/scan/publicación y comprobar fallos y resultados.

**Ampliación:** Curso completo de Bash/Python; Triggers/Chains avanzados y attestations.

**Continuidad:** introducir repositorio/commit mínimos antes del pipeline; PR y colaboración se desarrollan después con Prow. No asumir que todos los ProwJobs ejecutan Tekton automáticamente: usar un puente preparado o mostrar ambos sin prometer integración nativa universal.

### Sesión 21 · Git y Prow: colaboración y validaciones

**Fecha:** 28/01/2027 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Conectar un cambio revisado con las comprobaciones conocidas de CI.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Ramas, commits, PR, revisión y conflictos sencillos.
- ProwJobs, plugins, Tide y Deck como visión operativa.
- Relación con pipeline Tekton.

**Práctica / evidencia:** Prow preparado, abrir un PR, observar validaciones y resolver un fallo antes del merge.

**Ampliación:** Instalación completa de Prow; internals/monorepos/operaciones Git avanzadas.

### Sesión 22 · GitOps con ArgoCD

**Fecha:** 02/02/2027 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Reconciliar el estado del repositorio con Kubernetes.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Declarativo, versionado y pull.
- Application, diferencias, health y sync policies.
- Helm/Kustomize.
- Drift y corrección.

**Práctica / evidencia:** Desplegar imagen producida por CI, modificar manifiesto mediante PR, observar sync y provocar drift manual.

**Ampliación:** ApplicationSets avanzado, multi-tenancy, SSO y catálogo completo de hooks/waves.

### Sesión 23 · Traefik e Istio

**Fecha:** 04/02/2027 · 18:00–21:00 · **Docente:** David · **Concentración:** 🟡.

**Objetivo:** Distinguir entrada externa y comunicación segura entre servicios.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Traefik para routing/TLS con cert-manager.
- Istio para mTLS y política de acceso.
- Reparto entre versiones como preparación de Rollouts.

**Práctica / evidencia:** Componentes preparados, modificar pocas reglas, comprobar acceso y comunicación y observar reparto de tráfico.

**Ampliación:** Instalación desde cero, catálogo de middlewares, TCP/UDP, tuning Envoy y Ambient Mesh profundo.

### Sesión 24 · Entrega progresiva con Argo Rollouts

**Fecha:** 11/02/2027 · 18:00–21:00 · **Docente:** David · **Concentración:** 🟡.

**Objetivo:** Desplegar versiones con métricas que deciden avance o rollback.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Canary y blue/green.
- Rollouts.
- Integración con ArgoCD, Prometheus e Istio/Traefik.
- Análisis y rollback.

**Práctica / evidencia:** Canary principal sobre la misma app, provocar degradación y comprobar retorno; blue/green como comparación.

**Ampliación:** Feature flags/Flagger/OpenFeature y estrategias avanzadas; no repetir instalación de networking.

### Sesión 25 · Escalado con HPA, VPA, KEDA y Karpenter

**Fecha:** 16/02/2027 · 18:00–21:00 · **Docente:** David · **Concentración:** 🟡.

**Objetivo:** Distinguir ajuste de recursos, réplicas y capacidad de nodos.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- HPA por CPU como práctica principal.
- Recomendaciones VPA.
- KEDA por eventos y su uso de HPA.
- Karpenter ante Pods pendientes y consolidación.

**Práctica / evidencia:** Generar carga, observar HPA; consulta VPA; demos preparadas de cola KEDA y provisión/consolidación de nodos.

**Ampliación:** Catálogo triggers, métricas complejas, tuning, políticas Spot/capacidad y optimización profunda de costes; evitar controladores compitiendo.

**Precaución del lab:** no dejar HPA y KEDA compitiendo sobre el mismo workload; VPA en modo recomendación. Karpenter requiere infraestructura/permisos preparados y costes controlados.

## M6 · Platform Engineering Avanzado: Operators, Serverless y Multi-Cluster

5 sesiones · 15h lectivas · 2 ECTS.

**Enfoque del bloque:** problema → concepto → ejemplo → cuándo usarlo. Docencia: Profesor UPC.

### Sesión 26 · Operators con Go y Kubebuilder/Operator SDK

**Fecha:** 18/02/2027 · 18:00–21:00 · **Docente:** Profesor UPC · **Concentración:** 🟡.

**Objetivo:** Reconocer cuándo un operator automatiza conocimiento operativo.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- CRD, estado deseado y reconciliación.
- Go mínimo para leer tipos/structs/errores.
- Organización de Kubebuilder/Operator SDK.

**Práctica / evidencia:** Leer un operator preparado, crear un recurso, observar actuación y modificar un comportamiento pequeño.

**Ampliación:** Curso Go, Cobra/Viper, concurrencia avanzada y operator desarrollado desde cero.

### Sesión 27 · Cluster API y Hosted Control Planes

**Fecha:** 23/02/2027 · 18:00–21:00 · **Docente:** Profesor UPC · **Concentración:** 🟡.

**Objetivo:** Comparar automatización del ciclo de vida y ubicación del control plane.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Cluster API: creación/escalado/upgrades.
- HyperShift, vCluster y Kamaji: aislamiento, arquitectura y casos de uso.
- Enfoques no equivalentes.

**Práctica / evidencia:** Demostraciones preparadas y comparación de responsabilidades, sin asumir integración universal de todas las herramientas.

**Ampliación:** Instalación de todos los productos y operación avanzada.

### Sesión 28 · Knative y serverless

**Fecha:** 25/02/2027 · 18:00–21:00 · **Docente:** Profesor UPC · **Concentración:** 🟢.

**Objetivo:** Entender cuándo usar ejecución orientada a demanda sobre Kubernetes.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Knative Serving, revisions, routing y scale-to-zero.
- Contexto serverless.
- Introducción opcional a Virtual Kubelet.

**Práctica / evidencia:** Publicar una función/servicio preparado, generar tráfico y observar escalado a cero.

**Ampliación:** Plataforma serverless completa, Eventing avanzado y Virtual Kubelet profundo.

### Sesión 29 · Multi-cluster: Istio, Cilium y Submariner

**Fecha:** 02/03/2027 · 18:00–21:00 · **Docente:** Profesor UPC · **Concentración:** 🟡.

**Objetivo:** Comparar conectividad de servicios y redes entre clústeres.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Istio multicluster.
- Cilium Cluster Mesh.
- Submariner.
- Identidad, conectividad y limitaciones.
- Distinguir sus ámbitos.

**Práctica / evidencia:** Diagramas y demostración preparada de tráfico entre clústeres, comparando opciones.

**Ampliación:** Desplegar las tres soluciones desde cero.

### Sesión 30 · Crossplane y recuperación con Velero

**Fecha:** 04/03/2027 · 18:00–21:00 · **Docente:** Profesor UPC · **Concentración:** 🟡.

**Objetivo:** Distinguir aprovisionamiento declarativo y recuperación ante desastres.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Crossplane: providers, managed resources, compositions y XRDs.
- Relación con IaC de M2 y M4.
- Velero: backup/restore, alcance y límites.

**Práctica / evidencia:** Demos separadas de recurso cloud reconciliado y recuperación de aplicación; discutir dependencias, datos y RPO/RTO.

**Ampliación:** Composition Functions avanzado, plataforma multicloud completa y DR de producción.

## Proyecto Final

El proyecto integra progresivamente los resultados de las prácticas: infraestructura IaC en un proveedor, aplicación en Kubernetes, configuración con Helm/Kustomize, CI, ArgoCD, DNS/TLS, secretos externos, observabilidad, seguridad, entrega progresiva y escalado.

**Entregables:** repositorio reproducible, memoria de arquitectura y decisiones técnicas, runbooks, demostración end-to-end con un escenario de fallo, diagnóstico y recuperación, y defensa oral.

**Evaluación:** funcionalidad, reproducibilidad, seguridad, observabilidad, justificación de decisiones, control de costes, documentación y defensa. Las tecnologías tratadas como ampliación, como firmas/SBOM y configuraciones multi-cluster avanzadas, son opcionales en el proyecto.

**Consolidación:** 09/03/2027, 18:00–21:00. **Presentación y defensa:** 11/03/2027, 18:00–21:00. Ambas actividades se realizan fuera de las 30 sesiones lectivas. El 16/03 y el 18/03 se reservan para recuperación.

## Contenidos de ampliación

Material complementario para profundizar mediante trabajo autónomo o formación adicional.

- **Sesión 1 · DevOps y Platform Engineering:** Implantación completa de Backstage y diseño organizativo en profundidad.
- **Sesión 2 · AWS, Terraform y Python:** Curso completo de HCL/boto3; diseño autónomo desde cero; catálogo exhaustivo de bases de datos, mensajería y serverless.
- **Sesión 3 · Azure, Terraform y automatización Python:** SDK Azure completo; diseño avanzado de módulos; catálogo exhaustivo de servicios gestionados.
- **Sesión 4 · GCP, estado remoto y comparación de IaC:** Laboratorio propio de Pulumi; SDK completo; módulos propios avanzados.
- **Sesión 5 · Contenedores y ecosistema OCI:** Catálogo de runtimes alternativos y builds in-cluster; firma/SBOM como extras, escaneo se concreta en seguridad y Tekton.
- **Sesión 6 · Arquitectura, API, kind, autenticación y RBAC:** Integración OIDC avanzada; el montaje interno se aborda en la sesión de clúster desde cero.
- **Sesión 7 · Workloads, configuración y recursos:** Catálogo exhaustivo de controladores y scheduling avanzado.
- **Sesión 8 · Persistencia, CSI y StatefulSets:** Snapshots/cloning avanzados; comparación exhaustiva de drivers y afinidad avanzada.
- **Sesión 9 · Networking y exposición de aplicaciones:** Instalación/comparación de múltiples CNI; catálogo completo de rutas; networking avanzado se desarrolla con Traefik/Istio.
- **Sesión 10 · Clúster componente a componente:** Kubernetes the hard way completo sin ayudas; operación HA y recuperación avanzada.
- **Sesión 11 · Seguridad de imágenes y políticas de admisión:** Firmas, SBOM, attestations y conexión automática entre escaneo/admisión; segundo motor de políticas completo.
- **Sesión 12 · EKS y kOps en AWS:** Dos despliegues diseñados autónomamente; operación avanzada practicada en profundidad.
- **Sesión 13 · AKS y GKE:** Instalaciones completas independientes y catálogo de add-ons de ambos proveedores.
- **Sesión 14 · Kustomize y Helm:** Creación de charts complejos desde cero y catálogo de plugins.
- **Sesión 15 · DNS y HTTPS con Cloudflare, ExternalDNS y cert-manager:** DNSSEC/DoH y operación DNS avanzada.
- **Sesión 16 · Secretos externos: Vault y External Secrets Operator:** HA/auto-unseal y operación Vault en producción; implantación completa de todos los backends; no exponer valores sensibles en Terraform state.
- **Sesión 17 · Prometheus, PromQL y Alertmanager:** HA/federación y operación Mimir; reparto orientativo 20/30/40/25/55/10 min para métricas/recogida/PromQL/alertas/lab/cierre.
- **Sesión 18 · Grafana, Loki y Alloy:** Grafana as Code y operación avanzada de Loki; no enseñar todas las capacidades de Alloy.
- **Sesión 19 · OpenTelemetry, Collector, Tempo y correlación:** SDK en profundidad, instrumentación manual completa, sampling avanzado y operación productiva de Collector/Tempo.
- **Sesión 20 · Scripting y pipelines con Tekton:** Curso completo de Bash/Python; Triggers/Chains avanzados y attestations.
- **Sesión 21 · Git y Prow: colaboración y validaciones:** Instalación completa de Prow; internals/monorepos/operaciones Git avanzadas.
- **Sesión 22 · GitOps con ArgoCD:** ApplicationSets avanzado, multi-tenancy, SSO y catálogo completo de hooks/waves.
- **Sesión 23 · Traefik e Istio:** Instalación desde cero, catálogo de middlewares, TCP/UDP, tuning Envoy y Ambient Mesh profundo.
- **Sesión 24 · Entrega progresiva con Argo Rollouts:** Feature flags/Flagger/OpenFeature y estrategias avanzadas; no repetir instalación de networking.
- **Sesión 25 · Escalado con HPA, VPA, KEDA y Karpenter:** Catálogo triggers, métricas complejas, tuning, políticas Spot/capacidad y optimización profunda de costes; evitar controladores compitiendo.
- **Sesión 26 · Operators con Go y Kubebuilder/Operator SDK:** Curso Go, Cobra/Viper, concurrencia avanzada y operator desarrollado desde cero.
- **Sesión 27 · Cluster API y Hosted Control Planes:** Instalación de todos los productos y operación avanzada.
- **Sesión 28 · Knative y serverless:** Plataforma serverless completa, Eventing avanzado y Virtual Kubelet profundo.
- **Sesión 29 · Multi-cluster: Istio, Cilium y Submariner:** Desplegar las tres soluciones desde cero.
- **Sesión 30 · Crossplane y recuperación con Velero:** Composition Functions avanzado, plataforma multicloud completa y DR de producción.

**Ampliación de IaC:** taller adicional de Terraform/OpenTofu centrado en diseño de módulos, testing avanzado y automatización.
