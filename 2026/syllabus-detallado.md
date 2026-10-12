# Posgrado en Platform Engineering y DevOps con Kubernetes — edición 2026–2027

UPC School · Curso 305300 · Live online · Castellano.

**Versión de trabajo consolidada con los acuerdos del curso.** 30 sesiones lectivas de 3 horas (90h), martes y jueves de 18:00 a 21:00, zona horaria **Europe/Madrid**. Ventana del curso: 03/11/2026–18/03/2027. El Proyecto Final tiene actividades propias fuera de las 30 sesiones y 90 horas, conforme al criterio acordado. Se conservan como referencia los 12 ECTS publicados, incluido PF; no se recalculan proporcionalmente con este reparto interno.

Referencia oficial: https://upcschool.upc.edu/esp/estudis/formacio/curs/305300/platform-engineering-devops-kubernetes/. El contenido oficial se ha contrastado con la transcripción aportada por el usuario; no se dispone de una descarga verificada de la página.

M6 sigue provisional, con enfoque de visión general y demostraciones; docente UPC por confirmar. La asignación Traefik/Istio completa corresponde a David. René y Rael son las denominaciones docentes acordadas; no se inventan nombres completos para David ni para el profesor UPC.

Enlaces: [syllabus resumido](syllabus-resumido.md) · [calendario](calendario.md).

## Enfoque docente y prerrequisitos

Perfil junior: Linux, redes y scripting básicos según el contexto del repositorio; requisitos de acceso oficiales pendientes de verificar. No se exige experiencia cloud previa en esta planificación. Una misma aplicación Python con dos servicios conecta cloud, Kubernetes, observabilidad, CI y GitOps. Bash se practica en Tekton; Python aparece progresivamente en proveedores y automatización; Go se usa para comprender el operator. La IA ayuda a escribir/adaptar código que debe revisarse y verificarse.

Laboratorios guiados con manifiestos/configuraciones preparados. Antes de clase se comprueban cuentas, permisos, cuotas, dominios y costes. Se preservan estados reutilizables; para despliegues lentos, especialmente EKS/kOps, se explican conceptos durante la espera y se dispone de un entorno alternativo preparado. Cada práctica cloud incluye limpieza. Secretos y credenciales no se guardan en repositorios, logs ni estado Terraform; crear el contenedor del secreto no implica cargar su valor mediante IaC.

Semáforo: 🟢 alcance cómodo; 🟡 ajustado con material preparado. No mide dificultad de la herramienta ni garantiza tiempo de despliegue. Las amarillas de M6 suponen demostraciones, no implementaciones completas.

## Resultados de aprendizaje

Al terminar, el participante podrá explicar y aplicar un flujo cloud → Kubernetes → observabilidad → CI/GitOps → entrega/escalado; comparar responsabilidades de operación; verificar configuraciones y permisos; y reconocer cuándo usar las tecnologías avanzadas de M6. El alcance guiado no equivale a dominio autónomo de todos los proveedores o productos.

## M1 · Fundamentos DevOps, Platform Engineering y Programación para Infraestructura

1 sesiones · 3h lectivas · 1.5 ECTS publicados como referencia.

### Sesión 1 · DevOps y Platform Engineering

**Fecha:** 03/11/2026 · 18:00–21:00 · **Docente:** René · **Concentración:** 🟢.

**Objetivo:** Relacionar DevOps, SRE y Platform Engineering con necesidades de una organización.

**Entrada:** Contexto inicial del programa.

**Contenido principal:**

- CALMS y prácticas DevOps.
- IDP, golden paths y experiencia de desarrollo.
- Team Topologies y métricas DORA.

**Práctica / evidencia:** Propuesta breve de plataforma para una empresa: usuarios, capacidades y criterios de éxito.

**Extras y profundidad fuera de la clase:** Implantación completa de Backstage y diseño organizativo en profundidad.

## M2 · Cloud Computing Multicloud e Infraestructura como Código

3 sesiones · 9h lectivas · 1 ECTS publicados como referencia.

### Sesión 2 · AWS, Terraform y Python

**Fecha:** 05/11/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Entender una infraestructura AWS pequeña y verificar su funcionamiento mediante código.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- IAM, regiones y zonas.
- VPC, subredes, Security Groups, EC2 y S3, contexto de ECR.
- HCL, provider, recursos, variables y plan/apply/destroy.
- consulta Python preparada e IA para adaptar código.

**Práctica / evidencia:** Lanzar el ejemplo preparado, explicar mientras se despliega, modificar una variable, consultar recursos y verificar limpieza.

**Extras y profundidad fuera de la clase:** Curso completo de HCL/boto3; diseño autónomo desde cero; catálogo exhaustivo de bases de datos, mensajería y serverless.

### Sesión 3 · Azure, Terraform y automatización Python

**Fecha:** 10/11/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Transferir el patrón de AWS a Azure y reconocer diferencias de identidad y red.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Entra ID, suscripciones, grupos de recursos y Managed Identities.
- VNet, NSG, VM y Blob Storage, contexto de ACR.
- variables, outputs y módulos existentes.
- adaptación del script Python.

**Práctica / evidencia:** Reproducir el caso común con configuración preparada y explicar equivalencias y diferencias.

**Extras y profundidad fuera de la clase:** SDK Azure completo; diseño avanzado de módulos; catálogo exhaustivo de servicios gestionados.

### Sesión 4 · GCP, estado remoto y comparación de IaC

**Fecha:** 12/11/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Aplicar el caso común en GCP y comparar proveedores y formas de definir infraestructura.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Proyectos, cuentas de servicio e IAM.
- VPC, firewall, Compute Engine y Cloud Storage, contexto de Artifact Registry.
- estado local/remoto, permisos y locking según backend.
- Pulumi con Python frente a HCL durante 10–15 minutos.

**Práctica / evidencia:** Adaptar el caso preparado, consultar recursos y comparar identidad, red, estado y portabilidad.

**Extras y profundidad fuera de la clase:** Laboratorio propio de Pulumi; SDK completo; módulos propios avanzados; la comparación Pulumi es ampliación si falta tiempo.

## M3 · Contenedores y Kubernetes Core. Ecosistema OCI

7 sesiones · 21h lectivas · 2 ECTS publicados como referencia.

### Sesión 5 · Contenedores y ecosistema OCI

**Fecha:** 17/11/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Construir, ejecutar y publicar una imagen entendiendo aislamiento y runtime.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Namespaces, cgroups y capas OCI.
- Dockerfile y build multi-stage.
- Docker/containerd/CRI-O y CRI.
- registros e higiene de imágenes.

**Práctica / evidencia:** Construir una imagen pequeña y ejecutar/publicar la aplicación que servirá de hilo conductor.

**Extras y profundidad fuera de la clase:** Catálogo de runtimes alternativos y builds in-cluster; firma/SBOM como extras, escaneo se concreta en seguridad y Tekton.

### Sesión 6 · Arquitectura, API, kind, autenticación y RBAC

**Fecha:** 19/11/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Seguir una petición kubectl y distinguir autenticación de autorización.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Control plane y nodos.
- API, etcd, reconciliación y ejecución de Pods.
- kubeconfig, certificados, tokens y ServiceAccounts.
- Role/RoleBinding.
- OIDC y admisión conceptual.

**Práctica / evidencia:** Levantar kind, localizar componentes y comprobar una operación permitida y otra denegada.

**Extras y profundidad fuera de la clase:** Configuración completa OIDC pendiente de alcance; montaje interno se aborda en la sesión de clúster desde cero.

### Sesión 7 · Workloads, configuración y recursos

**Fecha:** 24/11/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Desplegar una aplicación y gestionar su configuración y ciclo de vida.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Pods, Deployments, Jobs y CronJobs.
- ConfigMap/Secret.
- probes.
- requests/limits y scheduling básico.
- namespaces, labels y selectors.

**Práctica / evidencia:** Modificar configuración, observar probes, actualizar la aplicación y comprobar asignación de recursos.

**Extras y profundidad fuera de la clase:** Catálogo exhaustivo de controladores y scheduling avanzado.

### Sesión 8 · Persistencia, CSI y StatefulSets

**Fecha:** 26/11/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Mantener datos y comprender las necesidades de workloads con estado.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Volúmenes, PV/PVC, StorageClass y aprovisionamiento dinámico.
- función de CSI.
- StatefulSet.
- afinidad y restricciones de ubicación relevantes para almacenamiento.

**Práctica / evidencia:** Añadir persistencia, recrear un Pod y verificar datos y comportamiento del workload.

**Extras y profundidad fuera de la clase:** Snapshots/cloning avanzados; comparación exhaustiva de drivers y afinidad avanzada.

### Sesión 9 · Networking y exposición de aplicaciones

**Fecha:** 01/12/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Seguir tráfico entre Pods, descubrir servicios y exponer la aplicación.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- CNI en Pod→Pod.
- Services y CoreDNS.
- ejemplo Gateway API y relación con Ingress.
- NetworkPolicy.

**Práctica / evidencia:** Con CNI/controlador preparados, exponer la aplicación, bloquear tráfico y permitir solo conexiones necesarias.

**Extras y profundidad fuera de la clase:** Instalación/comparación de múltiples CNI; catálogo completo de rutas; networking avanzado se desarrolla con Traefik/Istio.

### Sesión 10 · Clúster componente a componente

**Fecha:** 03/12/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Comprender cómo se ensamblan y autentican los componentes de Kubernetes.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- PKI, etcd, kube-apiserver, scheduler y controller-manager.
- kubelet, runtime y kube-proxy.
- unión de un nodo y TLS bootstrapping.

**Práctica / evidencia:** Arrancar un clúster reducido con material preparado, unir un nodo y ejecutar un Pod.

**Extras y profundidad fuera de la clase:** Kubernetes the hard way completo sin ayudas; operación HA y recuperación avanzada.

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

**Extras y profundidad fuera de la clase:** Firmas, SBOM, attestations y conexión automática entre escaneo/admisión; segundo motor de políticas completo.

## M4 · Kubernetes en Producción y Ecosistema Cloud Native

5 sesiones · 15h lectivas · 2 ECTS publicados como referencia.

### Sesión 12 · EKS y kOps en AWS

**Fecha:** 15/12/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Comparar Kubernetes gestionado y autogestionado sobre la misma base AWS.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Terraform para lanzar EKS.
- kOps con configuración preparada.
- control plane, red, identidad y nodos.
- responsabilidades, upgrades, disponibilidad, costes y recuperación.

**Práctica / evidencia:** Explicar durante ambos despliegues, solapar esperas, desplegar la misma aplicación y comparar; comprobar permisos y disponer de clústeres de respaldo.

**Extras y profundidad fuera de la clase:** Dos despliegues diseñados autónomamente; operación avanzada practicada en profundidad.

### Sesión 13 · AKS y GKE

**Fecha:** 17/12/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Aplicar la comparación de operación cloud a Azure y GCP.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Identidad de workloads.
- networking.
- pools de nodos.
- actualizaciones y responsabilidad operativa.
- GKE Standard/Autopilot y opciones de AKS.

**Práctica / evidencia:** Demostración preparada de los mismos requisitos y comparación razonada con EKS.

**Extras y profundidad fuera de la clase:** Instalaciones completas independientes y catálogo de add-ons de ambos proveedores.

### Sesión 14 · Kustomize y Helm

**Fecha:** 22/12/2026 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Adaptar manifiestos y usar paquetes existentes.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Bases, overlays y patches.
- charts, values, templates y releases.
- uso combinado de render Helm y Kustomize.
- chart que instala un operator.

**Práctica / evidencia:** Adaptar la aplicación a dos entornos e instalar/configurar un chart, distinguiendo chart, operator y recursos gestionados.

**Extras y profundidad fuera de la clase:** Creación de charts complejos desde cero y catálogo de plugins.

### Sesión 15 · DNS y HTTPS con Cloudflare, ExternalDNS y cert-manager

**Fecha:** 07/01/2027 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟢.

**Objetivo:** Publicar una aplicación con dominio y certificados renovables.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Registros DNS, resolución y TTL.
- Cloudflare como provider.
- ExternalDNS.
- Issuer/ClusterIssuer y ACME DNS-01.
- protección del token.

**Práctica / evidencia:** Instalar componentes por Helm sobre el entorno anterior, publicar el registro y verificar HTTPS y renovación.

**Extras y profundidad fuera de la clase:** DNSSEC/DoH y operación DNS avanzada; CDN de Cloudflare permanece pendiente de encaje, no se elimina como contenido oficial.

### Sesión 16 · Secretos externos: Vault y External Secrets Operator

**Fecha:** 12/01/2027 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Separar secretos de manifiestos y aplicar identidad y permisos de acceso.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Vault y ESO explícitos del programa.
- despliegue guiado mediante Helm, operator como opción sin fijar uno.
- autenticación Kubernetes y política básica.
- SecretStore/ExternalSecret.
- AWS Secrets Manager como alternativa y entrega CSI frente a Secret.

**Práctica / evidencia:** Aplicación consume secreto externo, modificarlo y comprobar sincronización y comportamiento de la aplicación.

**Extras y profundidad fuera de la clase:** HA/auto-unseal y operación Vault en producción; implantación completa de todos los backends; no exponer valores sensibles en Terraform state.

## M5 · Observabilidad, GitOps, CI/CD y Networking Avanzado

9 sesiones · 27h lectivas · 2 ECTS publicados como referencia.

### Sesión 17 · Prometheus, PromQL y Alertmanager

**Fecha:** 14/01/2027 · 18:00–21:00 · **Docente:** David · **Concentración:** 🟡.

**Objetivo:** Detectar fallos mediante métricas y definir cuándo alertar.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Contadores/histogramas, labels/cardinalidad.
- scraping/exporters.
- Operator, ServiceMonitor/PodMonitor.
- tasas, errores, latencia y agregación.
- reglas, routing y silencios.
- introducción Mimir.

**Práctica / evidencia:** kube-prometheus-stack preparado, conectar la app, provocar errores/carga, consultar y comprobar una alerta.

**Extras y profundidad fuera de la clase:** HA/federación y operación Mimir; reparto orientativo 20/30/40/25/55/10 min para métricas/recogida/PromQL/alertas/lab/cierre.

### Sesión 18 · Grafana, Loki y Alloy

**Fecha:** 19/01/2027 · 18:00–21:00 · **Docente:** David · **Concentración:** 🟡.

**Objetivo:** Pasar de un síntoma en métricas a mensajes que explican el fallo.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Datasources, paneles y variables.
- dashboard de tráfico/errores/latencia.
- labels frente a campos de logs.
- Alloy para logs de Pods.
- LogQL, Explore y JSON.

**Práctica / evidencia:** Provocar fallo, detectarlo en el dashboard y localizar logs del mismo intervalo con configuración guiada de Alloy.

**Extras y profundidad fuera de la clase:** Grafana as Code y operación avanzada de Loki; no enseñar todas las capacidades de Alloy.

### Sesión 19 · OpenTelemetry, Collector, Tempo y correlación

**Fecha:** 21/01/2027 · 18:00–21:00 · **Docente:** David · **Concentración:** 🟡.

**Objetivo:** Localizar dónde se atasca una petición entre servicios.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Spans, contexto y propagación.
- instrumentación automática.
- receivers/processors/exporters.
- Tempo/Grafana.
- trace ID en logs, enlaces y exemplars cuando proceda.

**Práctica / evidencia:** Dos servicios preparados, provocar latencia y recorrer métrica→traza→logs; Collector para trazas y Alloy para logs.

**Extras y profundidad fuera de la clase:** SDK en profundidad, instrumentación manual completa, sampling avanzado y operación productiva de Collector/Tempo.

**Preparación específica:** propagación de contexto entre dos servicios, trace ID en logs y enlaces de Grafana comprobados. Alloy y Collector tienen capacidades solapadas: el reparto logs/trazas elegido es una decisión del lab, no una limitación de las herramientas.

### Sesión 20 · Scripting y pipelines con Tekton

**Fecha:** 26/01/2027 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Automatizar tareas verificables y construir una imagen mediante pipeline.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Git mínimo.
- Bash para CLI, errores y resultados, jq.
- Python cuando aporte valor.
- asistencia de IA y revisión.
- Tasks, Pipelines, PipelineRuns y Workspaces.
- Trivy en CI.

**Práctica / evidencia:** Conectar tareas preparadas de build/test/scan/publicación y comprobar fallos y resultados.

**Extras y profundidad fuera de la clase:** Curso completo de Bash/Python; Triggers/Chains avanzados y attestations; testing/CI Terraform pendiente de concretar, no omitir cobertura oficial.

**Continuidad:** introducir repositorio/commit mínimos antes del pipeline; PR y colaboración se desarrollan después con Prow. No asumir que todos los ProwJobs ejecutan Tekton automáticamente: usar un puente preparado o mostrar ambos sin prometer integración nativa universal.

### Sesión 21 · Git y Prow: colaboración y validaciones

**Fecha:** 28/01/2027 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Conectar un cambio revisado con las comprobaciones conocidas de CI.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Ramas, commits, PR, revisión y conflictos sencillos.
- ProwJobs, plugins, Tide y Deck como visión operativa.
- relación con pipeline Tekton.

**Práctica / evidencia:** Prow preparado, abrir un PR, observar validaciones y resolver un fallo antes del merge.

**Extras y profundidad fuera de la clase:** Instalación completa de Prow; internals/monorepos/operaciones Git avanzadas; alcance exacto de Git avanzado oficial pendiente.

### Sesión 22 · GitOps con ArgoCD

**Fecha:** 02/02/2027 · 18:00–21:00 · **Docente:** Rael · **Concentración:** 🟡.

**Objetivo:** Reconciliar el estado del repositorio con Kubernetes.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Declarativo, versionado y pull.
- Application, diferencias, health y sync policies.
- Helm/Kustomize.
- drift y corrección.

**Práctica / evidencia:** Desplegar imagen producida por CI, modificar manifiesto mediante PR, observar sync y provocar drift manual.

**Extras y profundidad fuera de la clase:** ApplicationSets avanzado, multi-tenancy, SSO y catálogo completo de hooks/waves.

### Sesión 23 · Traefik e Istio

**Fecha:** 04/02/2027 · 18:00–21:00 · **Docente:** David · **Concentración:** 🟡.

**Objetivo:** Distinguir entrada externa y comunicación segura entre servicios.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Traefik para routing/TLS con cert-manager.
- Istio para mTLS y política de acceso.
- reparto entre versiones como preparación de Rollouts.

**Práctica / evidencia:** Componentes preparados, modificar pocas reglas, comprobar acceso y comunicación y observar reparto de tráfico.

**Extras y profundidad fuera de la clase:** Instalación desde cero, catálogo de middlewares, TCP/UDP, tuning Envoy y Ambient Mesh profundo.

### Sesión 24 · Entrega progresiva con Argo Rollouts

**Fecha:** 11/02/2027 · 18:00–21:00 · **Docente:** David · **Concentración:** 🟡.

**Objetivo:** Desplegar versiones con métricas que deciden avance o rollback.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Canary y blue/green.
- Rollouts.
- integración con ArgoCD, Prometheus e Istio/Traefik.
- análisis y rollback.

**Práctica / evidencia:** Canary principal sobre la misma app, provocar degradación y comprobar retorno; blue/green como comparación.

**Extras y profundidad fuera de la clase:** Feature flags/Flagger/OpenFeature y estrategias avanzadas; no repetir instalación de networking.

### Sesión 25 · Escalado con HPA, VPA, KEDA y Karpenter

**Fecha:** 16/02/2027 · 18:00–21:00 · **Docente:** David · **Concentración:** 🟡.

**Objetivo:** Distinguir ajuste de recursos, réplicas y capacidad de nodos.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- HPA por CPU como práctica principal.
- recomendaciones VPA.
- KEDA por eventos y su uso de HPA.
- Karpenter ante Pods pendientes y consolidación.

**Práctica / evidencia:** Generar carga, observar HPA; consulta VPA; demos preparadas de cola KEDA y provisión/consolidación de nodos.

**Extras y profundidad fuera de la clase:** Catálogo triggers, métricas complejas, tuning, políticas Spot/capacidad y optimización profunda de costes; evitar controladores compitiendo.

**Precaución del lab:** no dejar HPA y KEDA compitiendo sobre el mismo workload; VPA en modo recomendación. Karpenter requiere infraestructura/permisos preparados y costes controlados.

## M6 · Platform Engineering Avanzado: Operators, Serverless y Multi-Cluster

5 sesiones · 15h lectivas · 2 ECTS publicados como referencia.

**Bloque provisional:** problema → concepto → ejemplo → cuándo usarlo. Profesor UPC por confirmar.

### Sesión 26 · Operators con Go y Kubebuilder/Operator SDK

**Fecha:** 18/02/2027 · 18:00–21:00 · **Docente:** Profesor UPC — por confirmar · **Concentración:** 🟡.

**Objetivo:** Reconocer cuándo un operator automatiza conocimiento operativo.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- CRD, estado deseado y reconciliación.
- Go mínimo para leer tipos/structs/errores.
- organización de Kubebuilder/Operator SDK.

**Práctica / evidencia:** Leer un operator preparado, crear un recurso, observar actuación y modificar un comportamiento pequeño.

**Extras y profundidad fuera de la clase:** Curso Go, Cobra/Viper, concurrencia avanzada y operator desarrollado desde cero; sesión provisional de visión general.

### Sesión 27 · Cluster API y Hosted Control Planes

**Fecha:** 23/02/2027 · 18:00–21:00 · **Docente:** Profesor UPC — por confirmar · **Concentración:** 🟡.

**Objetivo:** Comparar automatización del ciclo de vida y ubicación del control plane.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Cluster API: creación/escalado/upgrades.
- HyperShift, vCluster y Kamaji: aislamiento, arquitectura y casos de uso.
- enfoques no equivalentes.

**Práctica / evidencia:** Demostraciones preparadas y comparación de responsabilidades, sin asumir integración universal de todas las herramientas.

**Extras y profundidad fuera de la clase:** Instalación de todos los productos y operación avanzada; propuesta provisional.

### Sesión 28 · Knative y serverless

**Fecha:** 25/02/2027 · 18:00–21:00 · **Docente:** Profesor UPC — por confirmar · **Concentración:** 🟢.

**Objetivo:** Entender cuándo usar ejecución orientada a demanda sobre Kubernetes.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Knative Serving, revisions, routing y scale-to-zero.
- contexto serverless.
- Virtual Kubelet como mención opcional de continuidad histórica.

**Práctica / evidencia:** Publicar una función/servicio preparado, generar tráfico y observar escalado a cero.

**Extras y profundidad fuera de la clase:** Plataforma serverless completa, Eventing avanzado y Virtual Kubelet profundo; propuesta provisional.

### Sesión 29 · Multi-cluster: Istio, Cilium y Submariner

**Fecha:** 02/03/2027 · 18:00–21:00 · **Docente:** Profesor UPC — por confirmar · **Concentración:** 🟡.

**Objetivo:** Comparar conectividad de servicios y redes entre clústeres.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Istio multicluster.
- Cilium Cluster Mesh.
- Submariner.
- identidad, conectividad y limitaciones.
- distinguir sus ámbitos.

**Práctica / evidencia:** Diagramas y demostración preparada de tráfico entre clústeres, comparando opciones.

**Extras y profundidad fuera de la clase:** Desplegar las tres soluciones desde cero; OCM/Rancher fuera del recorrido actual; propuesta provisional.

### Sesión 30 · Crossplane y recuperación con Velero

**Fecha:** 04/03/2027 · 18:00–21:00 · **Docente:** Profesor UPC — por confirmar · **Concentración:** 🟡.

**Objetivo:** Distinguir aprovisionamiento declarativo y recuperación ante desastres.

**Entrada:** Fundamentos y prácticas de los bloques previos; material preparado según laboratorio.

**Contenido principal:**

- Crossplane: providers, managed resources, compositions y XRDs.
- relación con IaC de M2 y M4.
- Velero: backup/restore, alcance y límites.

**Práctica / evidencia:** Demos separadas de recurso cloud reconciliado y recuperación de aplicación; discutir dependencias, datos y RPO/RTO.

**Extras y profundidad fuera de la clase:** Composition Functions avanzado, plataforma multicloud completa y DR de producción; propuesta provisional.

## Proyecto Final — fuera del cómputo lectivo

Construcción incremental de una plataforma con el material de las prácticas; no se empieza desde cero al acabar las clases. Infraestructura IaC en un proveedor, aplicación en Kubernetes, configuración Helm/Kustomize, CI, ArgoCD, DNS/TLS, secretos externos, observabilidad, seguridad, entrega progresiva y escalado.

Entregables propuestos, basados en el roadmap previo: repositorio reproducible, memoria de arquitectura/decisiones y runbooks, demo end-to-end con fallo/diagnóstico/recuperación y defensa oral. Firmas/SBOM y multi-cluster no se convierten en requisitos obligatorios si se tratan solo como extras o demostraciones.

Criterios para cerrar con el equipo docente: funcionalidad, reproducibilidad, seguridad, observabilidad, justificación de decisiones, limpieza/costes, documentación y defensa. No se fijan pesos nuevos ni tamaño de equipos. Tutoría/tribunal pendientes de asignación.

Actividades propuestas: **09/03/2027 consolidación** y **11/03/2027 presentación/defensa**, 18:00–21:00; no cuentan como sesiones 31/32 ni añaden horas al total lectivo. Fechas de PF por confirmar según organización y número de equipos. 16/03 y 18/03 quedan como reserva/recuperación.

## Cobertura oficial y decisiones pendientes

Este reparto conserva las tecnologías nombradas oficialmente, pero cuatro alcances requieren cierre docente; no se consideran extras prescindibles:

- **Git avanzado:** sesión 21. Se ha acordado práctica de colaboración básica; decidir qué parte avanzada (por ejemplo rebase, conflictos o protección de ramas) cubrir sin volver a un catálogo de operaciones.
- **Testing y CI/CD de Terraform:** vincular ejemplos de M2 con sesión 20; concretar las comprobaciones y el tiempo, sin afirmar que el pipeline de imágenes ya cubre IaC.
- **Cloudflare CDN:** DNS/ExternalDNS/ACME se cubren en sesión 15; falta concretar el ejemplo o explicación de CDN.
- **OIDC:** introducción en sesión 6 y contexto de identidad cloud; configuración práctica y profundidad pendientes.

Admission controllers sí tienen espacio en sesión 11. Vault y ESO permanecen explícitos en sesión 16; Secrets Manager es alternativa, no sustitución. Crossplane se concentra en sesión 30 con referencia desde M4. Mimir se introduce en sesión 17. Alloy se conserva por decisión expresa; no se incluye Snyk. OCM y Rancher no forman parte del reparto actual. La distribución de M6 y su profesor UPC requieren confirmación; las fechas reflejan la propuesta actual y no disponibilidad individual verificada.

## Registro de ampliaciones

Estos extras preservan lo apartado del alcance principal. No añaden sesiones automáticamente.

- **Sesión 1 · DevOps y Platform Engineering:** Implantación completa de Backstage y diseño organizativo en profundidad.
- **Sesión 2 · AWS, Terraform y Python:** Curso completo de HCL/boto3; diseño autónomo desde cero; catálogo exhaustivo de bases de datos, mensajería y serverless.
- **Sesión 3 · Azure, Terraform y automatización Python:** SDK Azure completo; diseño avanzado de módulos; catálogo exhaustivo de servicios gestionados.
- **Sesión 4 · GCP, estado remoto y comparación de IaC:** Laboratorio propio de Pulumi; SDK completo; módulos propios avanzados; la comparación Pulumi es ampliación si falta tiempo.
- **Sesión 5 · Contenedores y ecosistema OCI:** Catálogo de runtimes alternativos y builds in-cluster; firma/SBOM como extras, escaneo se concreta en seguridad y Tekton.
- **Sesión 6 · Arquitectura, API, kind, autenticación y RBAC:** Configuración completa OIDC pendiente de alcance; montaje interno se aborda en la sesión de clúster desde cero.
- **Sesión 7 · Workloads, configuración y recursos:** Catálogo exhaustivo de controladores y scheduling avanzado.
- **Sesión 8 · Persistencia, CSI y StatefulSets:** Snapshots/cloning avanzados; comparación exhaustiva de drivers y afinidad avanzada.
- **Sesión 9 · Networking y exposición de aplicaciones:** Instalación/comparación de múltiples CNI; catálogo completo de rutas; networking avanzado se desarrolla con Traefik/Istio.
- **Sesión 10 · Clúster componente a componente:** Kubernetes the hard way completo sin ayudas; operación HA y recuperación avanzada.
- **Sesión 11 · Seguridad de imágenes y políticas de admisión:** Firmas, SBOM, attestations y conexión automática entre escaneo/admisión; segundo motor de políticas completo.
- **Sesión 12 · EKS y kOps en AWS:** Dos despliegues diseñados autónomamente; operación avanzada practicada en profundidad.
- **Sesión 13 · AKS y GKE:** Instalaciones completas independientes y catálogo de add-ons de ambos proveedores.
- **Sesión 14 · Kustomize y Helm:** Creación de charts complejos desde cero y catálogo de plugins.
- **Sesión 15 · DNS y HTTPS con Cloudflare, ExternalDNS y cert-manager:** DNSSEC/DoH y operación DNS avanzada; CDN de Cloudflare permanece pendiente de encaje, no se elimina como contenido oficial.
- **Sesión 16 · Secretos externos: Vault y External Secrets Operator:** HA/auto-unseal y operación Vault en producción; implantación completa de todos los backends; no exponer valores sensibles en Terraform state.
- **Sesión 17 · Prometheus, PromQL y Alertmanager:** HA/federación y operación Mimir; reparto orientativo 20/30/40/25/55/10 min para métricas/recogida/PromQL/alertas/lab/cierre.
- **Sesión 18 · Grafana, Loki y Alloy:** Grafana as Code y operación avanzada de Loki; no enseñar todas las capacidades de Alloy.
- **Sesión 19 · OpenTelemetry, Collector, Tempo y correlación:** SDK en profundidad, instrumentación manual completa, sampling avanzado y operación productiva de Collector/Tempo.
- **Sesión 20 · Scripting y pipelines con Tekton:** Curso completo de Bash/Python; Triggers/Chains avanzados y attestations; testing/CI Terraform pendiente de concretar, no omitir cobertura oficial.
- **Sesión 21 · Git y Prow: colaboración y validaciones:** Instalación completa de Prow; internals/monorepos/operaciones Git avanzadas; alcance exacto de Git avanzado oficial pendiente.
- **Sesión 22 · GitOps con ArgoCD:** ApplicationSets avanzado, multi-tenancy, SSO y catálogo completo de hooks/waves.
- **Sesión 23 · Traefik e Istio:** Instalación desde cero, catálogo de middlewares, TCP/UDP, tuning Envoy y Ambient Mesh profundo.
- **Sesión 24 · Entrega progresiva con Argo Rollouts:** Feature flags/Flagger/OpenFeature y estrategias avanzadas; no repetir instalación de networking.
- **Sesión 25 · Escalado con HPA, VPA, KEDA y Karpenter:** Catálogo triggers, métricas complejas, tuning, políticas Spot/capacidad y optimización profunda de costes; evitar controladores compitiendo.
- **Sesión 26 · Operators con Go y Kubebuilder/Operator SDK:** Curso Go, Cobra/Viper, concurrencia avanzada y operator desarrollado desde cero; sesión provisional de visión general.
- **Sesión 27 · Cluster API y Hosted Control Planes:** Instalación de todos los productos y operación avanzada; propuesta provisional.
- **Sesión 28 · Knative y serverless:** Plataforma serverless completa, Eventing avanzado y Virtual Kubelet profundo; propuesta provisional.
- **Sesión 29 · Multi-cluster: Istio, Cilium y Submariner:** Desplegar las tres soluciones desde cero; OCM/Rancher fuera del recorrido actual; propuesta provisional.
- **Sesión 30 · Crossplane y recuperación con Velero:** Composition Functions avanzado, plataforma multicloud completa y DR de producción; propuesta provisional.

**Ampliación de IaC:** posible cuarta clase de Terraform/OpenTofu con módulos propios, testing y automatización; solo con decisión expresa y revisión del reparto. No confundir profundización extra con la cobertura mínima de testing/CI que aún exige la descripción oficial.

