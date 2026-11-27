# Planificación docente interna · 2026–2027

Documento de preparación docente. Reúne los mínimos de contenido de la descripción del programa y el alcance práctico de cada clase; no forma parte del syllabus para el alumnado.

Fuente: descripción de asignaturas transcrita de https://upcschool.upc.edu/esp/estudis/formacio/curs/305300/platform-engineering-devops-kubernetes/. Las listas son una distribución docente de esa descripción, no citas literales ni requisitos de instalar todas las herramientas. Los contenidos pueden cambiar de bloque sin perder su cobertura.

**Concentración:** 🟢 Baja · 🟡 Media · 🔴 Alta. El indicador valora la densidad de contenido y práctica dentro de una clase de tres horas.

30 clases / 90h, incluida la defensa. M1: 9h de contenido propio/transversal, sin duplicarlas en el cómputo.

M3 reúne 7 sesiones / 21h (4–10); M2 reúne 2 sesiones / 6h (2–3), sin cambiar sus ECTS. La sesión 1 incluye la preparación de AWS Academy dentro de sus 3h compartidas. Las tres clases de contenedores requieren el entorno preparado y verificado antes de sesión 4. AWS es el laboratorio principal de IaC; Azure y GCP se trabajan mediante demostraciones preparadas y análisis de equivalencias, no mediante dos despliegues completos del alumnado.

La distribución de M1 es: sesión 1, 3h; sesión 2, 1h de Python e IA; sesión 3, 1h de adaptación de scripts; sesión 5, 1h prevista de validación Python y revisión de código con IA, pendiente de confirmar; operators (14), 1,5h; Tekton (17), 1,5h. Estas horas integradas ya forman parte de las sesiones respectivas.

## Comprobaciones de cobertura prioritarias

- **Git avanzado:** incluir un ejemplo profesional en sesión 18; PR/commits básicos no bastan por sí solos.
- **Terraform:** HCL, estado y módulos en proveedores; testing y CI/CD conectados con sesión 17. No confundir CI de imágenes con validación de IaC.
- **Cloudflare:** además de DNS/ACME, cubrir redes y explicar CDN en sesión 15.
- **OIDC:** incluirlo expresamente en sesión 6; no limitar toda autenticación a certificados/tokens.
- **Go e IA:** mantenerlos en el ejemplo de operators y sus evidencias de trabajo transversal M1.

## Índice de sesiones

- [01 · Fundamentos de DevOps y Platform Engineering](#sesion-01) — M1
- [02 · AWS: fundamentos y aprovisionamiento como código](#sesion-02) — M2
- [03 · AWS WordPress: de EC2 con estado a instancias reemplazables](#sesion-03) — M2
- [04 · Fundamentos de contenedores](#sesion-04) — M3
- [05 · Imágenes y contenedores](#sesion-05) — M3
- [06 · De contenedores a Kubernetes](#sesion-06) — M3
- [07 · Fundamentos de Kubernetes](#sesion-07) — M3
- [08 · Aplicaciones y configuración en Kubernetes](#sesion-08) — M3
- [09 · Persistencia en Kubernetes](#sesion-09) — M3
- [10 · EKS y networking en Kubernetes](#sesion-10) — M3
- [11 · Construcción y seguridad de un clúster Kubernetes](#sesion-11) — M4
- [12 · Kubernetes gestionado: AKS y GKE](#sesion-12) — M4
- [13 · Configuración y empaquetado de aplicaciones: Kustomize y Helm](#sesion-13) — M4
- [14 · Desarrollo de operators: Go y Kubebuilder/Operator SDK](#sesion-14) — M6
- [15 · Infraestructura declarativa: DNS, certificados y recursos cloud](#sesion-15) — M4
- [16 · Gestión de secretos externos: Vault y External Secrets Operator](#sesion-16) — M4
- [17 · Automatización de pipelines: scripting, Tekton y Trivy](#sesion-17) — M5
- [18 · Colaboración y validación de cambios: Git y Prow](#sesion-18) — M5
- [19 · Despliegue declarativo y reconciliación: GitOps con ArgoCD](#sesion-19) — M5
- [20 · Métricas y alertas: Prometheus, PromQL y Alertmanager](#sesion-20) — M5
- [21 · Dashboards y logs: Grafana, Loki y Alloy](#sesion-21) — M5
- [22 · Trazas distribuidas y correlación: OpenTelemetry y Tempo](#sesion-22) — M5
- [23 · Entrada de tráfico y service mesh: Traefik e Istio](#sesion-23) — M5
- [24 · Entrega progresiva: canary y blue/green con Argo Rollouts](#sesion-24) — M5
- [25 · Escalado de aplicaciones y nodos: HPA, VPA, KEDA y Karpenter](#sesion-25) — M5
- [26 · Políticas de admisión y recuperación: OPA/Gatekeeper y Velero](#sesion-26) — M6
- [27 · Gestión de clústeres: Cluster API y Hosted Control Planes](#sesion-27) — M6
- [28 · Serverless en Kubernetes: Knative y Virtual Kubelet](#sesion-28) — M6
- [29 · Conectividad multi-cluster: Istio, Cilium Cluster Mesh y Submariner](#sesion-29) — M6
- [30 · Presentación y defensa del Trabajo Final](#sesion-30) — PF

<a id="sesion-01"></a>

### 01 · Fundamentos de DevOps y Platform Engineering

**M1 · 3 horas · Concentración 🟢 Baja**

**Docentes:**<br>René Serral<br>Rael Garcia

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Evolución de Systems Engineer, DevOps, SRE y Platform Engineering; autoservicio y plataforma como producto, a nivel introductorio.<br>• SLI, SLO y SLA: indicadores, objetivos y acuerdos de nivel de servicio.<br>• Introducción a Terraform e IaC: HCL, providers, plan/apply, state, módulos y Registry.<br>• Presentar la programación asistida por IA como práctica transversal del curso.<br>• Presentar AWS Academy y explicar el acceso y funcionamiento del laboratorio asignado. |
| **Resultado de aprendizaje** | Distinguir DevOps, SRE y Platform Engineering, relacionar SLI, SLO y SLA, identificar los fundamentos de Terraform y acceder al entorno Academy siguiendo las instrucciones del laboratorio asignado. |
| **Actividad práctica** | Repaso conceptual de roles, SLI/SLO/SLA y del flujo de Terraform. Recorrido guiado por Academy: acceder al curso y laboratorio, iniciarlo, localizar credenciales temporales e interpretar estado, tiempo, presupuesto y permisos. Explicar y practicar parada/finalización según las instrucciones del laboratorio, incluida la persistencia y limpieza de recursos. |
| **Alcance y profundidad** | Integrar el recorrido introductorio de Academy en las 3h existentes, compartidas por René Serral y Rael Garcia, sin añadir horas. No asumir interfaz, tipo de laboratorio ni persistencia universales: mostrar el entorno realmente asignado. Priorizar la comprensión y preparación del laboratorio antes de los contenedores de sesión 4. |
| **Requisitos de preparación** | Presentación introductoria de roles y Terraform: [diapositivas 1–9](https://docs.google.com/presentation/d/14q6t7KH7PqUf-ja0a4BbPE4IcS0NQ5ssL6CnASEItxg/htmlpresent), con DevOps, SRE y la tabla SLI/SLO/SLA. Invitación al curso Academy enviada y acceso comprobado. El docente confirma el laboratorio exacto, sus instrucciones y límites y deja preparado y verificado antes de sesión 4 el entorno de contenedores: runtime disponible y permitido, CLI/Compose, registro, conectividad, puertos y cuotas; comprobar credenciales temporales y reglas de duración, persistencia y limpieza. |
| **Contenido complementario** | Implantación completa de Backstage y diseño organizativo en profundidad. |

<a id="sesion-02"></a>

### 02 · AWS: fundamentos y aprovisionamiento como código

**M2 · Rael Garcia · 3 horas · Concentración 🟡 Media**

**Material:** [Estado de Terraform](https://github.com/raelga/kubernetes-talks/tree/main/course/infra/labs/aws/00-terraform-state) · [Fundamentos de EC2](https://github.com/raelga/kubernetes-talks/tree/main/course/infra/labs/aws/01-ec2-basics). Verificar permisos y cuotas de Academy.

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Credenciales de AWS Academy, IAM, región, redes, cómputo y almacenamiento.<br>• Ciclo de vida de Terraform, variables, outputs y estado remoto.<br>• Conservar la hora integrada de M1 para consultas de recursos con Python y revisión de código asistida por IA. |
| **Resultado de aprendizaje** | Crear y reutilizar un backend remoto de Terraform, aprovisionar EC2, interpretar el plan y el estado, comprobar acceso y bootstrap y destruir los recursos de cada laboratorio. |
| **Actividad práctica** | Crear y migrar el backend de S3; reutilizarlo para EC2, inspeccionar el estado de Terraform y verificar el acceso. Revisar costes, presupuestos y limpieza; conservar el bucket de estado mientras sea necesario. |
| **Alcance y profundidad** | Usar el entorno Academy presentado en sesión 1 y un ejemplo cloud pequeño y guiado, sin diseño desde cero; introducir variables, outputs y estado para sesión 3. Conservar 1h transversal M1 y 15–20 minutos para AWS Billing/Cost Explorer (consultas y filtros por servicio, región y etiquetas), AWS Budgets, alertas y limpieza. Si Academy restringe estas vistas, mostrarlas desde un entorno docente o con desgloses preparados. Los datos de facturación pueden aparecer con retraso; los presupuestos y sus alertas no detienen automáticamente el gasto. Tampoco interpretar el indicador de presupuesto del laboratorio como una garantía universal de parada automática. |
| **Requisitos de preparación** | Acceso Academy preparado en sesión 1, permisos/cuotas, Terraform, AWS CLI y los tres laboratorios comprobados; verificar la VPC/subred pública y la clave vockey del laboratorio EC2, y LabInstanceProfile/LabRole, SSM y permisos RDS/Secrets Manager para la demo WordPress. Mantener la consulta Python preparada. Seguir las reglas del laboratorio sobre credenciales, duración, persistencia y limpieza. Preparar acceso docente a facturación/presupuestos y desgloses de muestra cuando el laboratorio o los retrasos de facturación impidan consultarlos directamente. |
| **Contenido complementario** | Curso completo de HCL/boto3; diseño autónomo desde cero; catálogo exhaustivo de bases de datos, mensajería y serverless. |

<a id="sesion-03"></a>

### 03 · AWS WordPress: de EC2 con estado a instancias reemplazables

**M2 · Rael Garcia · 3 horas · Concentración 🟡 Media**

**Material:** [02 · Evolución de WordPress](https://github.com/raelga/kubernetes-talks/tree/main/course/infra/labs/aws/02-wordpress).

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | EC2/MariaDB local, RDS y Elastic IP, módulos y estados independientes, ALB/Auto Scaling, AMI versionadas con Packer y archivos multimedia en S3. |
| **Resultado de aprendizaje** | Explicar qué persiste al reemplazar una instancia y por qué importan las imágenes inmutables y el almacenamiento externo antes de Kubernetes. |
| **Actividad práctica** | Seguir la evolución, inspeccionar los outputs y el estado remoto de Terraform y comparar el reemplazo de instancias. Proteger secretos y estado; revisar costes y limpieza. |
| **Alcance y profundidad** | Conservar la hora integrada de M1 para adaptación de scripts y configuración. Completar excepcionalmente el cierre de EC2 a Auto Scaling, AMI y S3 en la sesión 4. |

<a id="sesion-04"></a>

### 04 · Fundamentos de contenedores

**M3 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Cierre excepcional del laboratorio AWS WordPress: de EC2 a Auto Scaling, AMI versionadas y archivos multimedia en S3.<br>• Contenedores desde cero: namespaces, cgroups, aislamiento, sistema de ficheros y función del runtime.<br>• Introducción a imágenes y capas OCI. |
| **Resultado de aprendizaje** | Explicar la evolución de WordPress y los mecanismos de aislamiento y ejecución que sustentan los contenedores. |
| **Actividad práctica** | Completar el cierre guiado del laboratorio AWS y explorar namespaces, cgroups y runtime en el entorno preparado. |
| **Alcance y profundidad** | Reservar parte de la sesión para el cierre excepcional de AWS y el resto para fundamentos. El ciclo Docker se trabaja en sesión 5 y Compose en sesión 6. |
| **Requisitos de preparación** | Laboratorio WordPress y entorno Academy preparados; verificar runtime compatible, CLI, conectividad, permisos y cuotas. Comprobar credenciales temporales y persistencia según el laboratorio asignado; no se requiere una cuenta cloud personal adicional. |
| **Contenido complementario** | Catálogo de runtimes alternativos y builds in-cluster; firma/SBOM como extras. El escaneo se concreta en el pipeline Tekton. |

<a id="sesion-05"></a>

### 05 · Imágenes y contenedores

**M3 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | Docker, capas OCI, Dockerfile multi-stage, construcción, etiquetado y publicación; cómo Docker utiliza namespaces y cgroups; ejecución, puertos, variables, redes, volúmenes, logs e inspección. M1: 1h prevista de validación Python y revisión de código con IA, pendiente de confirmar. |
| **Resultado de aprendizaje** | Construir y ejecutar imágenes y explicar el aislamiento y los límites de recursos. |
| **Actividad práctica** | Construir, ejecutar y publicar una imagen y diagnosticar su ejecución. La actividad M1 no consta como realizada. |
| **Requisitos de preparación** | Entorno Academy validado, runtime y registro accesibles, código y Dockerfile preparados; comprobar permisos, cuotas y credenciales. |
| **Contenido complementario** | Optimización avanzada de imágenes. |

<a id="sesion-06"></a>

### 06 · De contenedores a Kubernetes

**M3 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | ECR, publicación y descarga; Compose, redes, volúmenes y aplicación de dos servicios; transición a Kubernetes con kind. |
| **Resultado de aprendizaje** | Conectar imágenes y servicios multicontenedor con un clúster Kubernetes. |
| **Actividad práctica** | Publicar en ECR, levantar y diagnosticar los servicios con Compose y preparar kind. |
| **Requisitos de preparación** | Runtime y Compose, permisos ECR, imágenes, código, kind y kubectl preparados. |
| **Contenido complementario** | Escenarios complejos de Compose. |

<a id="sesion-07"></a>

### 07 · Fundamentos de Kubernetes

**M3 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | Control plane, nodos, API, etcd y reconciliación; namespaces, labels, annotations, selectors, Pods, requests/limits e introducción a probes. |
| **Resultado de aprendizaje** | Explicar arquitectura y objetos fundamentales de Kubernetes. |
| **Actividad práctica** | Explorar kind y crear y examinar Pods, metadatos, recursos y probes. |
| **Requisitos de preparación** | kind, kubectl y manifiestos preparados. |
| **Contenido complementario** | Scheduling avanzado. |

<a id="sesion-08"></a>

### 08 · Aplicaciones y configuración en Kubernetes

**M3 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Contenido abordado** | Probes, ReplicaSets y almacenamiento. |
| **Continuación** | Deployments, ConfigMaps, Secrets, Jobs y CronJobs quedan programados para la sesión 9. |
| **Contenido complementario** | Selectores y adopción de Pods, rolling update manual con ReplicaSets, StatefulSet, DaemonSet, scheduling y estrategias de despliegue. |

<a id="sesion-09"></a>

### 09 · Persistencia en Kubernetes

**M3 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | Deployments, ConfigMaps y Secrets; Jobs y CronJobs, al menos mediante demostración docente. Retomar persistencia: volúmenes, PV/PVC, StorageClass, aprovisionamiento dinámico, CSI, StatefulSet y afinidad de almacenamiento. |
| **Resultado de aprendizaje** | Gestionar aplicaciones y su configuración, mantener datos y comprender workloads con estado. |
| **Actividad práctica** | Actualizar una aplicación con Deployment y configurar ConfigMaps y Secrets; practicar Jobs y CronJobs de forma guiada si queda tiempo o demostrarlos. Añadir persistencia, recrear un Pod y verificar datos. |
| **Requisitos de preparación** | Clúster, kubectl, imagen y manifiestos preparados; StorageClass y driver CSI disponibles y ejemplo con datos persistentes. |
| **Contenido complementario** | Actualización en vivo de ConfigMap, práctica adicional de Jobs y CronJobs, snapshots/cloning y afinidad avanzada. |

<a id="sesion-10"></a>

### 10 · EKS y networking en Kubernetes

**M3 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | EKS, CNI, Services, CoreDNS, Ingress, Gateway API y NetworkPolicy. |
| **Resultado de aprendizaje** | Seguir tráfico entre Pods y exponer la aplicación. |
| **Actividad práctica** | Desplegar EKS con Terraform, exponer la aplicación y aplicar políticas de red; disponer de clúster de respaldo. |
| **Requisitos de preparación** | Permisos y cuotas Academy, Terraform, clúster de respaldo, CNI y controlador de entrada; verificar costes y limpieza. |
| **Contenido complementario** | Comparación de CNI y rutas avanzadas. |

<a id="sesion-11"></a>

### 11 · Construcción y seguridad de un clúster Kubernetes

**M4 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | Construcción componente a componente: PKI, etcd, API, scheduler, controller-manager, kubelet, runtime, kube-proxy, unión y TLS bootstrapping; kubeconfig, certificados, tokens, ServiceAccounts, RBAC, OIDC y admisión. |
| **Resultado de aprendizaje** | Comprender el ensamblaje y distinguir autenticación de autorización. |
| **Actividad práctica** | Arrancar un clúster reducido con material preparado, unir un nodo, ejecutar un Pod y comprobar operaciones permitidas y denegadas. |
| **Requisitos de preparación** | Máquinas, certificados, guion y ejemplos RBAC preparados. |
| **Contenido complementario** | Montaje completo sin ayudas, HA, recuperación e integración OIDC avanzada. |

<a id="sesion-12"></a>

### 12 · Kubernetes gestionado: AKS y GKE

**M4 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | AKS y GKE, identidad, redes, cómputo, almacenamiento y registros; control plane, identidad de workloads, pools, actualizaciones, responsabilidad operativa y GKE Standard/Autopilot. Reservar 15–20 minutos por proveedor para consultas, filtros, presupuestos, alertas y limpieza en Azure Cost Management y GCP Cloud Billing; facturación retrasada y presupuestos que no detienen gasto. Revisar costes de control plane, nodos, balanceadores, discos y tráfico. |
| **Resultado de aprendizaje** | Comparar Kubernetes gestionado en Azure y GCP con EKS. |
| **Actividad práctica** | Demostraciones preparadas en cuentas docentes; comparar, identificar costes y comprobar limpieza sin exigir despliegues del alumnado. |
| **Requisitos de preparación** | Cuentas docentes, permisos, cuotas y entornos AKS/GKE preparados. |
| **Contenido complementario** | Instalación independiente, operación avanzada y comparación opcional con kOps. |

<a id="sesion-13"></a>

### 13 · Configuración y empaquetado de aplicaciones: Kustomize y Helm

**M4 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Application bundles: Helm y Kustomize. |
| **Resultado de aprendizaje** | Adaptar manifiestos y usar paquetes existentes. |
| **Actividad práctica** | Adaptar la aplicación a dos entornos e instalar/configurar un chart, distinguiendo chart, operator y recursos gestionados. |
| **Alcance y profundidad** | Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva. |
| **Requisitos de preparación** | Helm/Kustomize, manifiestos de aplicación y chart de ejemplo disponibles. |
| **Contenido complementario** | Creación de charts complejos desde cero y catálogo de plugins. |

<a id="sesion-14"></a>

### 14 · Desarrollo de operators: Go y Kubebuilder/Operator SDK

**M6 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Construcción de operators personalizados con Kubebuilder/Operator SDK.<br>• Go aplicado a construcción de controladores; programación asistida por IA como parte transversal de M1. |
| **Resultado de aprendizaje** | Reconocer cuándo un operator automatiza conocimiento operativo. |
| **Actividad práctica** | Leer un operator preparado, crear un recurso, observar actuación y modificar un comportamiento pequeño. |
| **Alcance y profundidad** | Ejemplo de operator preparado; no añadir Crossplane. La clase completa se reserva a operators; Go se aprende leyendo/modificando el ejemplo. |
| **Requisitos de preparación** | Proyecto Go con Kubebuilder/Operator SDK, CRD y operator ejecutable preparados. |
| **Contenido complementario** | Curso Go, Cobra/Viper, concurrencia avanzada y operator desarrollado desde cero. |

<a id="sesion-15"></a>

### 15 · Infraestructura declarativa: DNS, certificados y recursos cloud

**M4 · Rael Garcia · 3 horas · Concentración 🟢 Baja**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Redes/DNS/CDN con Cloudflare, en conexión con los fundamentos cloud y la exposición de la aplicación.<br>• Infraestructura declarativa: ExternalDNS, cert-manager y Crossplane. |
| **Resultado de aprendizaje** | Gestionar DNS, certificados y un recurso cloud mediante controladores declarativos. |
| **Actividad práctica** | Publicar DNS y verificar HTTPS con ExternalDNS/cert-manager sobre Cloudflare; demostrar con configuración preparada un recurso cloud gestionado por Crossplane. |
| **Alcance y profundidad** | DNS/certificados como práctica principal; Crossplane como demo breve. La cobertura CDN añade presión: limitarla a un ejemplo concreto. Cloudflare cubre DNS y ACME; dedicar también un ejemplo/explicación a CDN. Crossplane introductorio, sin Compositions complejas. |
| **Requisitos de preparación** | Dominio Cloudflare, permisos DNS, ExternalDNS/cert-manager y demo Crossplane preparados. |
| **Contenido complementario** | DNSSEC/DoH, operación DNS avanzada, Crossplane Compositions/XRDs avanzados y Composition Functions. |

<a id="sesion-16"></a>

### 16 · Gestión de secretos externos: Vault y External Secrets Operator

**M4 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Gestión de secretos con HashiCorp Vault y External Secrets Operator. |
| **Resultado de aprendizaje** | Separar secretos de manifiestos y aplicar identidad y permisos de acceso. |
| **Actividad práctica** | Aplicación consume secreto externo, modificarlo y comprobar sincronización y comportamiento de la aplicación. |
| **Alcance y profundidad** | Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva. AWS Secrets Manager/ASCP son alternativas complementarias; no sustituyen Vault y ESO. |
| **Requisitos de preparación** | Vault/ESO y autenticación Kubernetes disponibles; secreto de laboratorio y aplicación consumidora. |
| **Contenido complementario** | HA/auto-unseal y operación Vault en producción; implantación completa de todos los backends; no exponer valores sensibles en Terraform state. |

<a id="sesion-17"></a>

### 17 · Automatización de pipelines: scripting, Tekton y Trivy

**M5 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Programación Bash asistida por IA aplicada a automatización, con Python cuando corresponda; contenido M1.<br>• Pipelines con Tekton.<br>• Testing y CI/CD de Terraform: conectar las prácticas IaC con comprobaciones automatizadas.<br>• Seguridad de imágenes: aplicación práctica en el pipeline. |
| **Resultado de aprendizaje** | Automatizar tareas verificables y construir una imagen mediante pipeline. |
| **Actividad práctica** | Conectar tareas preparadas build → test → scan → publicación; provocar un fallo de Trivy, interpretar el resultado, corregir la imagen y repetir el pipeline. |
| **Alcance y profundidad** | Tareas preparadas; reservar tiempo para escaneo y comprobaciones IaC. Trivy es la herramienta elegida para escaneo; no está nombrada en la web. El pipeline de imágenes no cubre por sí solo testing/CI de Terraform. |
| **Requisitos de preparación** | Tekton, registro y repositorio, tareas build/test/scan, Trivy y ejemplo de validación Terraform preparados. |
| **Contenido complementario** | Curso completo de Bash/Python; Triggers/Chains avanzados y attestations. |

<a id="sesion-18"></a>

### 18 · Colaboración y validación de cambios: Git y Prow

**M5 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Control de versiones avanzado con Git.<br>• GitOps/colaboración con Prow: situar su función junto al flujo GitOps y CI. |
| **Resultado de aprendizaje** | Conectar un cambio revisado con las comprobaciones conocidas de CI. |
| **Actividad práctica** | Prow preparado, abrir un PR, observar validaciones y resolver un fallo antes del merge. |
| **Alcance y profundidad** | Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva. No dar Git avanzado por cubierto únicamente con commit/PR; incluir una operación profesional preparada, sin curso de internals. |
| **Requisitos de preparación** | Repositorio con PR, Prow y validaciones; ejemplo profesional Git preparado. |
| **Contenido complementario** | Instalación completa de Prow; internals/monorepos/operaciones Git avanzadas. |

<a id="sesion-19"></a>

### 19 · Despliegue declarativo y reconciliación: GitOps con ArgoCD

**M5 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • GitOps con ArgoCD. |
| **Resultado de aprendizaje** | Reconciliar el estado del repositorio con Kubernetes. |
| **Actividad práctica** | Desplegar imagen producida por CI, modificar manifiesto mediante PR, observar sync y provocar drift manual. |
| **Alcance y profundidad** | Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva. |
| **Requisitos de preparación** | ArgoCD, repositorio de manifiestos y aplicación Helm/Kustomize disponibles. |
| **Contenido complementario** | ApplicationSets avanzado, multi-tenancy, SSO y catálogo completo de hooks/waves. |

<a id="sesion-20"></a>

### 20 · Métricas y alertas: Prometheus, PromQL y Alertmanager

**M5 · David Girón · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Prometheus y Grafana como parte del stack de observabilidad.<br>• Mimir: explicar su función en el almacenamiento de métricas. |
| **Resultado de aprendizaje** | Detectar fallos mediante métricas y definir cuándo alertar. |
| **Actividad práctica** | kube-prometheus-stack preparado, conectar la app, provocar errores/carga, consultar y comprobar una alerta. |
| **Alcance y profundidad** | Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva. PromQL, Alertmanager y Operator desarrollan la práctica de métricas; Mimir permanece introductorio. |
| **Requisitos de preparación** | kube-prometheus-stack, aplicación instrumentada y generador de carga preparados. |
| **Contenido complementario** | HA/federación y operación Mimir; reparto orientativo 20/30/40/25/55/10 min para métricas/recogida/PromQL/alertas/lab/cierre. |

<a id="sesion-21"></a>

### 21 · Dashboards y logs: Grafana, Loki y Alloy

**M5 · David Girón · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Grafana y Loki para visualización y logs. |
| **Resultado de aprendizaje** | Pasar de un síntoma en métricas a mensajes que explican el fallo. |
| **Actividad práctica** | Provocar fallo, detectarlo en el dashboard y localizar logs del mismo intervalo con configuración guiada de Alloy. |
| **Alcance y profundidad** | Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva. Alloy es el recolector elegido, no una obligación explícita de la web. |
| **Requisitos de preparación** | Grafana/Loki/Alloy, logs de Pods y dashboard inicial disponibles. |
| **Contenido complementario** | Grafana as Code y operación avanzada de Loki; no enseñar todas las capacidades de Alloy. |

<a id="sesion-22"></a>

### 22 · Trazas distribuidas y correlación: OpenTelemetry y Tempo

**M5 · David Girón · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • OpenTelemetry y Tempo como parte del stack de observabilidad completo. |
| **Resultado de aprendizaje** | Localizar dónde se atasca una petición entre servicios. |
| **Actividad práctica** | Dos servicios preparados, provocar latencia y recorrer métrica→traza→logs; Collector para trazas y Alloy para logs. |
| **Alcance y profundidad** | Dos servicios preparados, instrumentación automática, trace ID y enlaces comprobados. Collector y correlación son el enfoque de práctica; no desarrollar un curso completo de SDK. |
| **Requisitos de preparación** | Dos servicios con instrumentación, Collector/Tempo, trace ID en logs y enlaces Grafana comprobados. |
| **Contenido complementario** | SDK en profundidad, instrumentación manual completa, sampling avanzado y operación productiva de Collector/Tempo. |

<a id="sesion-23"></a>

### 23 · Entrada de tráfico y service mesh: Traefik e Istio

**M5 · David Girón · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Networking avanzado con Traefik e Istio, incluyendo service mesh. |
| **Resultado de aprendizaje** | Distinguir entrada externa y comunicación segura entre servicios. |
| **Actividad práctica** | Componentes preparados, modificar pocas reglas, comprobar acceso y comunicación y observar reparto de tráfico. |
| **Alcance y profundidad** | Componentes preparados; entrada/mTLS como práctica, sin catálogo de routing. |
| **Requisitos de preparación** | Traefik/Istio y cert-manager preparados; aplicación con dos versiones. |
| **Contenido complementario** | Instalación desde cero, catálogo de middlewares, TCP/UDP, tuning Envoy y Ambient Mesh profundo. |

<a id="sesion-24"></a>

### 24 · Entrega progresiva: canary y blue/green con Argo Rollouts

**M5 · David Girón · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Canary y blue/green con Argo Rollouts. |
| **Resultado de aprendizaje** | Desplegar versiones con métricas que deciden avance o rollback. |
| **Actividad práctica** | Canary principal sobre la misma app, provocar degradación y comprobar retorno; blue/green como comparación. |
| **Alcance y profundidad** | Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva. |
| **Requisitos de preparación** | Argo Rollouts, rutas de tráfico, Prometheus y escenario de degradación preparados. |
| **Contenido complementario** | Feature flags/Flagger/OpenFeature y estrategias avanzadas; no repetir instalación de networking. |

<a id="sesion-25"></a>

### 25 · Escalado de aplicaciones y nodos: HPA, VPA, KEDA y Karpenter

**M5 · David Girón · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Escalado de workloads con HPA, VPA, KEDA y Karpenter. |
| **Resultado de aprendizaje** | Distinguir ajuste de recursos, réplicas y capacidad de nodos. |
| **Actividad práctica** | Generar carga, observar HPA; consulta VPA; demos preparadas de cola KEDA y provisión/consolidación de nodos. |
| **Alcance y profundidad** | HPA como lab; VPA recomendaciones y demos KEDA/Karpenter sin competir por el mismo workload. |
| **Requisitos de preparación** | Generador de carga, HPA, VPA en recomendación, cola KEDA y permisos Karpenter preparados. |
| **Contenido complementario** | Catálogo triggers, métricas complejas, tuning, políticas Spot/capacidad y optimización profunda de costes; evitar controladores compitiendo. |

<a id="sesion-26"></a>

### 26 · Políticas de admisión y recuperación: OPA/Gatekeeper y Velero

**M6 · Marc Catrisse · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Admission controllers como contenido de autenticación/control de Kubernetes.<br>• Disaster Recovery con Velero. |
| **Resultado de aprendizaje** | Aplicar políticas de admisión y recuperar una aplicación tras una pérdida de recursos. |
| **Actividad práctica** | Aplicar una política OPA/Gatekeeper, rechazar y corregir un recurso; realizar backup, borrar y restaurar una aplicación con Velero. |
| **Alcance y profundidad** | Una política y una restauración preparadas; no enseñar Rego ni DR completos. OPA/Gatekeeper es la implementación elegida para admisión; la web no exige ese motor por nombre. Kyverno/PSA son alternativas o ampliaciones. |
| **Requisitos de preparación** | OPA/Gatekeeper, política de ejemplo, Velero y almacenamiento de copias disponibles. |
| **Contenido complementario** | Políticas Rego complejas, catálogo de políticas, recuperación productiva avanzada, firmas y attestations. |

<a id="sesion-27"></a>

### 27 · Gestión de clústeres: Cluster API y Hosted Control Planes

**M6 · Marc Catrisse · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Gestión del ciclo de vida de clústeres con Cluster API.<br>• Hosted Control Planes: HyperShift, vCluster y Kamaji. |
| **Resultado de aprendizaje** | Comparar automatización del ciclo de vida y ubicación del control plane. |
| **Actividad práctica** | Demostraciones preparadas y comparación de responsabilidades, sin asumir integración universal de todas las herramientas. |
| **Alcance y profundidad** | Visión general y demos; no instalar cuatro plataformas. |
| **Requisitos de preparación** | Diagramas y demos de Cluster API/HCP preparadas; alcance de cada entorno comprobado. |
| **Contenido complementario** | Instalación de todos los productos y operación avanzada. |

<a id="sesion-28"></a>

### 28 · Serverless en Kubernetes: Knative y Virtual Kubelet

**M6 · Marc Catrisse · 3 horas · Concentración 🟢 Baja**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Serverless con Knative. |
| **Resultado de aprendizaje** | Entender cuándo usar ejecución orientada a demanda sobre Kubernetes. |
| **Actividad práctica** | Publicar un servicio Knative, observar revisions y scale-to-zero; demostrar con un entorno preparado el modelo de nodo virtual de Virtual Kubelet. |
| **Alcance y profundidad** | Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva. Virtual Kubelet está incluido por diseño del curso, además del Knative nombrado en la web. |
| **Requisitos de preparación** | Knative y demostración Virtual Kubelet preparadas; servicio y generador de peticiones. |
| **Contenido complementario** | Knative Eventing avanzado, plataforma serverless completa y desarrollo de providers Virtual Kubelet. |

<a id="sesion-29"></a>

### 29 · Conectividad multi-cluster: Istio, Cilium Cluster Mesh y Submariner

**M6 · Marc Catrisse · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Gestión/despliegue multi-cluster: Istio multicluster, Cilium Cluster Mesh y Submariner. |
| **Resultado de aprendizaje** | Comparar conectividad de servicios y redes entre clústeres. |
| **Actividad práctica** | Diagramas y demostración preparada de tráfico entre clústeres, comparando opciones. |
| **Alcance y profundidad** | Comparación y ejemplo entre clústeres, no desplegar tres redes desde cero. |
| **Requisitos de preparación** | Entorno/diagramas multi-cluster y conectividad entre clústeres comprobados. |
| **Contenido complementario** | Desplegar las tres soluciones desde cero. |

<a id="sesion-30"></a>

### 30 · Presentación y defensa del Trabajo Final

**PF · 3 horas · Concentración 🟡 Media**

**Docentes:**<br>René Serral<br>Rael Garcia

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Proyecto Final: presentación y defensa del trabajo integrador. La web nombra Proyecto Final; formato/defensa es el diseño docente del curso. |
| **Resultado de aprendizaje** | Presentar y justificar una plataforma reproducible integrada durante el curso. |
| **Actividad práctica** | Presentación del repositorio y documentación, demostración funcional y defensa ante René Serral y Rael Garcia. |
| **Alcance y profundidad** | Ajustar duración de demos y preguntas al número de equipos. Una sesión dentro de las 30/90h, impartida por René Serral y Rael Garcia; trabajo autónomo previo. |
| **Requisitos de preparación** | Repositorio, memoria y demostración de cada equipo; orden y tiempos de defensa definidos. |
| **Contenido complementario** | Ampliaciones voluntarias del proyecto; las tecnologías de profundización no son requisitos obligatorios.  |

## Referencias docentes y evaluación

Bibliografía de apoyo recuperada del roadmap anterior; no añade contenidos obligatorios ni amplía las prácticas:

- **M1:** *The Phoenix Project* (Kim, Behr, Spafford), *Team Topologies* (Skelton, Pais), *The DevOps Handbook* y documentación oficial de Bash y Python.
- **M2:** documentación de AWS, Azure, GCP, Terraform y OpenTofu; Pulumi como referencia comparativa.
- **M3:** *Kubernetes in Action* (Lukša), *Programming Kubernetes* (Hausenblas, Schimanski), documentación de Kubernetes y currículos CKA/CKAD/CKS.
- **M4:** documentación de EKS/GKE/AKS, Helm, Kustomize, cert-manager, ExternalDNS, Crossplane y External Secrets Operator; currículo Vault Associate.
- **M5:** documentación de Prometheus, Grafana, OpenTelemetry, Git, ArgoCD, Prow, Tekton, Istio, Argo Rollouts y KEDA.
- **M6:** *Programming Kubernetes*, Kubebuilder Book y documentación de Cluster API, Knative, vCluster, HyperShift, Kamaji y Velero.

Como criterios cualitativos de apoyo, valorar reproducibilidad, claridad de las decisiones, calidad del código, idempotencia y limpieza de recursos cloud, en coherencia con los entregables actuales. Los porcentajes 40/60 y las pruebas asociadas a sesiones históricas no se trasladan a esta edición. La evaluación del Trabajo Final se describe en el syllabus; esta recopilación no establece nuevas ponderaciones ni exige un operator propio o imágenes firmadas.
