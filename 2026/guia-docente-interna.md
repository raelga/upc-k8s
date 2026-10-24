# Planificación docente interna · 2026–2027

Documento de preparación docente. Reúne los mínimos de contenido de la descripción del programa y el alcance práctico de cada clase; no forma parte del syllabus para el alumnado.

Fuente: descripción de asignaturas transcrita de https://upcschool.upc.edu/esp/estudis/formacio/curs/305300/platform-engineering-devops-kubernetes/. Las listas son una distribución docente de esa descripción, no citas literales ni requisitos de instalar todas las herramientas. Los contenidos pueden cambiar de bloque sin perder su cobertura.

**Concentración:** 🟢 Baja · 🟡 Media · 🔴 Alta. El indicador valora la densidad de contenido y práctica dentro de una clase de tres horas.

30 clases / 90h, incluida la defensa. M1: 9h de contenido propio/transversal, sin duplicarlas en el cómputo.

## Comprobaciones de cobertura prioritarias

- **Git avanzado:** incluir un ejemplo profesional en sesión 18; PR/commits básicos no bastan por sí solos.
- **Terraform:** HCL, estado y módulos en proveedores; testing y CI/CD conectados con sesión 17. No confundir CI de imágenes con validación de IaC.
- **Cloudflare:** además de DNS/ACME, cubrir redes y explicar CDN en sesión 15.
- **OIDC:** incluirlo expresamente en sesión 6; no limitar toda autenticación a certificados/tokens.
- **Go e IA:** mantenerlos en el ejemplo de operators y sus evidencias de trabajo transversal M1.

## Índice de sesiones

- [01 · Fundamentos de DevOps y Platform Engineering](#sesion-01) — M1
- [02 · AWS: fundamentos y aprovisionamiento como código](#sesion-02) — M2
- [03 · Azure: fundamentos y aprovisionamiento como código](#sesion-03) — M2
- [04 · GCP: fundamentos y aprovisionamiento como código](#sesion-04) — M2
- [05 · Contenedores y ecosistema OCI: imágenes, runtimes y registros](#sesion-05) — M3
- [06 · Arquitectura de Kubernetes: API, autenticación y permisos](#sesion-06) — M3
- [07 · Aplicaciones en Kubernetes: workloads, configuración y recursos](#sesion-07) — M3
- [08 · Persistencia en Kubernetes: almacenamiento y aplicaciones con estado](#sesion-08) — M3
- [09 · Networking en Kubernetes: comunicación y exposición de servicios](#sesion-09) — M3
- [10 · Construcción de un clúster Kubernetes componente a componente](#sesion-10) — M3
- [11 · Kubernetes en AWS: EKS y clústeres autogestionados con kOps](#sesion-11) — M4
- [12 · Kubernetes en Azure y GCP: AKS y GKE](#sesion-12) — M4
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

**M1 · René Serral · 3 horas · Concentración 🟢 Baja**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Contextualización de DevOps y su evolución hacia Platform Engineering.<br>• Presentar la programación asistida por IA como práctica transversal del curso. |
| **Resultado de aprendizaje** | Relacionar DevOps, SRE y Platform Engineering con necesidades de una organización. |
| **Actividad práctica** | Propuesta breve de plataforma para una empresa: usuarios, capacidades y criterios de éxito. |
| **Alcance y profundidad** | Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva. |
| **Requisitos de preparación** | Caso de organización y plantilla de propuesta de plataforma. |
| **Contenido complementario** | Implantación completa de Backstage y diseño organizativo en profundidad. |

<a id="sesion-02"></a>

### 02 · AWS: fundamentos y aprovisionamiento como código

**M2 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Recursos fundamentales AWS: computación, redes, almacenamiento, identidad y servicios gestionados.<br>• Aprovisionamiento declarativo con Terraform: HCL y recursos.<br>• Automatización con Python asistida por IA; contenido transversal de M1. |
| **Resultado de aprendizaje** | Entender una infraestructura AWS pequeña y verificar su funcionamiento mediante código. |
| **Actividad práctica** | Lanzar el ejemplo preparado, explicar mientras se despliega, modificar una variable, consultar recursos y verificar limpieza; identificar recursos facturables, revisar el desglose de costes y comprobar la limpieza. |
| **Alcance y profundidad** | Un ejemplo cloud pequeño, Python preparado y explicación durante aprovisionamiento. Python/CLI para comprobaciones; no sustituir recursos cloud por un catálogo de sintaxis. AWS Billing y Cost Explorer: consulta por servicio, región y etiquetas; presupuestos y alertas con AWS Budgets. Reservar 15–20 minutos al cierre para costes, alertas y limpieza. Los datos de facturación pueden aparecer con retraso; una alerta de presupuesto no detiene automáticamente el gasto. |
| **Requisitos de preparación** | Cuenta AWS, permisos/cuotas, ejemplo Terraform, CLI y consulta Python comprobados. Acceso de lectura a facturación/costes y permisos para presupuestos; desglose de muestra si los recursos recién creados aún no aparecen. |
| **Contenido complementario** | Curso completo de HCL/boto3; diseño autónomo desde cero; catálogo exhaustivo de bases de datos, mensajería y serverless. |

<a id="sesion-03"></a>

### 03 · Azure: fundamentos y aprovisionamiento como código

**M2 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Recursos fundamentales Azure: computación, redes, almacenamiento, identidad y servicios gestionados.<br>• Terraform: parametrización y uso de módulos.<br>• Adaptación de automatización Python asistida por IA; contenido transversal de M1. |
| **Resultado de aprendizaje** | Transferir el patrón de AWS a Azure y reconocer diferencias de identidad y red. |
| **Actividad práctica** | Reproducir el caso común con configuración preparada y explicar equivalencias y diferencias; identificar recursos facturables, revisar el desglose de costes y comprobar la limpieza. |
| **Alcance y profundidad** | Reutilizar el patrón AWS; evitar enseñar el SDK completo. Azure Cost Management: consulta por suscripción, grupo de recursos, servicio y etiquetas; presupuestos y alertas. Reservar 15–20 minutos al cierre para costes, alertas y limpieza. Los datos de facturación pueden aparecer con retraso; una alerta de presupuesto no detiene automáticamente el gasto. |
| **Requisitos de preparación** | Cuenta Azure, permisos, configuración Terraform y adaptación Python del caso AWS. Acceso de lectura a facturación/costes y permisos para presupuestos; desglose de muestra si los recursos recién creados aún no aparecen. |
| **Contenido complementario** | SDK Azure completo; diseño avanzado de módulos; catálogo exhaustivo de servicios gestionados. |

<a id="sesion-04"></a>

### 04 · GCP: fundamentos y aprovisionamiento como código

**M2 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Recursos fundamentales GCP: computación, redes, almacenamiento, identidad y servicios gestionados.<br>• Terraform: gestión del estado y comparación del aprovisionamiento multicloud.<br>• Automatización con Python; contenido transversal de M1. |
| **Resultado de aprendizaje** | Aplicar el caso común en GCP y comparar proveedores y formas de definir infraestructura. |
| **Actividad práctica** | Adaptar el caso preparado, consultar recursos y comparar identidad, red, estado y portabilidad; identificar recursos facturables, revisar el desglose de costes y comprobar la limpieza. |
| **Alcance y profundidad** | Reutilizar patrón y estado; Pulumi breve. Pulumi/OpenTofu son comparaciones complementarias; no están nombrados en la descripción publicada. Cloud Billing de GCP: informes por proyecto, servicio y etiquetas/labels según disponibilidad; presupuestos y alertas. Reservar 15–20 minutos al cierre para costes, alertas y limpieza. Los datos de facturación pueden aparecer con retraso; una alerta de presupuesto no detiene automáticamente el gasto. |
| **Requisitos de preparación** | Cuenta GCP, permisos, backend de estado y ejemplos comparativos preparados. Acceso de lectura a facturación/costes y permisos para presupuestos; desglose de muestra si los recursos recién creados aún no aparecen. |
| **Contenido complementario** | Laboratorio propio de Pulumi; SDK completo; módulos propios avanzados. |

<a id="sesion-05"></a>

### 05 · Contenedores y ecosistema OCI: imágenes, runtimes y registros

**M3 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Ecosistema OCI: construcción de imágenes, runtimes, registros y seguridad. |
| **Resultado de aprendizaje** | Construir, ejecutar y publicar una imagen entendiendo aislamiento y runtime. |
| **Actividad práctica** | Construir una imagen pequeña y ejecutar/publicar la aplicación que servirá de hilo conductor. |
| **Alcance y profundidad** | Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva. Los productos concretos de build/runtime/escaneo son elecciones del laboratorio. |
| **Requisitos de preparación** | Runtime de contenedores, registro y código de la aplicación disponibles. |
| **Contenido complementario** | Catálogo de runtimes alternativos y builds in-cluster; firma/SBOM como extras, escaneo se concreta en el pipeline Tekton. |

<a id="sesion-06"></a>

### 06 · Arquitectura de Kubernetes: API, autenticación y permisos

**M3 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Arquitectura Kubernetes: plano de control y relación con los nodos.<br>• Autenticación/autorización: RBAC y OIDC. |
| **Resultado de aprendizaje** | Seguir una petición kubectl y distinguir autenticación de autorización. |
| **Actividad práctica** | Levantar kind, localizar componentes y comprobar una operación permitida y otra denegada. |
| **Alcance y profundidad** | Seguir una petición kubectl; no repetir el montaje manual. kind es el entorno local elegido; el requisito es explicar arquitectura, RBAC y OIDC. |
| **Requisitos de preparación** | kind, kubectl, kubeconfig y ejemplos de Role/RoleBinding preparados. |
| **Contenido complementario** | Integración OIDC avanzada; el montaje interno se aborda en la sesión de clúster desde cero. |

<a id="sesion-07"></a>

### 07 · Aplicaciones en Kubernetes: workloads, configuración y recursos

**M3 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Workloads, configuración y scheduling como bloques fundamentales de Kubernetes. |
| **Resultado de aprendizaje** | Desplegar una aplicación y gestionar su configuración y ciclo de vida. |
| **Actividad práctica** | Modificar configuración, observar probes, actualizar la aplicación y comprobar asignación de recursos. |
| **Alcance y profundidad** | Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva. |
| **Requisitos de preparación** | Clúster local, imagen de la aplicación y manifiestos de workloads/configuración. |
| **Contenido complementario** | Catálogo exhaustivo de controladores y scheduling avanzado. |

<a id="sesion-08"></a>

### 08 · Persistencia en Kubernetes: almacenamiento y aplicaciones con estado

**M3 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Almacenamiento Kubernetes: PV/PVC y CSI. |
| **Resultado de aprendizaje** | Mantener datos y comprender las necesidades de workloads con estado. |
| **Actividad práctica** | Añadir persistencia, recrear un Pod y verificar datos y comportamiento del workload. |
| **Alcance y profundidad** | Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva. |
| **Requisitos de preparación** | StorageClass y driver CSI disponibles; ejemplo con datos persistentes. |
| **Contenido complementario** | Snapshots/cloning avanzados; comparación exhaustiva de drivers y afinidad avanzada. |

<a id="sesion-09"></a>

### 09 · Networking en Kubernetes: comunicación y exposición de servicios

**M3 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Networking Kubernetes: Services, Ingress, Gateway API, CNI y Network Policies. |
| **Resultado de aprendizaje** | Seguir tráfico entre Pods, descubrir servicios y exponer la aplicación. |
| **Actividad práctica** | Con CNI/controlador preparados, exponer la aplicación, bloquear tráfico y permitir solo conexiones necesarias. |
| **Alcance y profundidad** | CNI/controlador preparados; un recorrido y pocas políticas. CoreDNS y el CNI preparado permiten enseñar el recorrido sin comparar todos los productos. |
| **Requisitos de preparación** | CNI compatible con NetworkPolicy, controlador de entrada y manifiestos preparados. |
| **Contenido complementario** | Instalación/comparación de múltiples CNI; catálogo completo de rutas; networking avanzado se desarrolla con Traefik/Istio. |

<a id="sesion-10"></a>

### 10 · Construcción de un clúster Kubernetes componente a componente

**M3 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Construcción de un clúster Kubernetes componente a componente. |
| **Resultado de aprendizaje** | Comprender cómo se ensamblan y autentican los componentes de Kubernetes. |
| **Actividad práctica** | Arrancar un clúster reducido con material preparado, unir un nodo y ejecutar un Pod. |
| **Alcance y profundidad** | Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva. |
| **Requisitos de preparación** | Máquinas de laboratorio, certificados y guion de arranque de componentes. |
| **Contenido complementario** | Kubernetes the hard way completo sin ayudas; operación HA y recuperación avanzada. |

<a id="sesion-11"></a>

### 11 · Kubernetes en AWS: EKS y clústeres autogestionados con kOps

**M4 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Operación de EKS y de otros entornos Kubernetes. |
| **Resultado de aprendizaje** | Comparar Kubernetes gestionado y autogestionado sobre la misma base AWS. |
| **Actividad práctica** | Explicar durante ambos despliegues, solapar esperas, desplegar la misma aplicación y comparar; comprobar permisos y disponer de clústeres de respaldo; identificar recursos facturables, revisar el desglose de costes y comprobar la limpieza. |
| **Alcance y profundidad** | Permisos y cuotas comprobados; despliegues solapados y clústeres de respaldo. kOps es el ejemplo de entorno autogestionado; la web no exige kOps por nombre. Costes Kubernetes en AWS: control plane EKS frente a autogestión con kOps, nodos, balanceadores, discos y tráfico. |
| **Requisitos de preparación** | AWS/Terraform/kOps, permisos/cuotas y configuraciones comprobados; clústeres de respaldo. |
| **Contenido complementario** | Dos despliegues diseñados autónomamente; operación avanzada practicada en profundidad. |

<a id="sesion-12"></a>

### 12 · Kubernetes en Azure y GCP: AKS y GKE

**M4 · Rael Garcia · 3 horas · Concentración 🟡 Media**

| Apartado | Contenido |
|---|---|
| **Cobertura requerida** | • Operación de AKS y GKE. |
| **Resultado de aprendizaje** | Aplicar la comparación de operación cloud a Azure y GCP. |
| **Actividad práctica** | Demostración preparada de los mismos requisitos y comparación razonada con EKS; identificar recursos facturables, revisar el desglose de costes y comprobar la limpieza. |
| **Alcance y profundidad** | Usar el caso común y el material preparado; priorizar comprobación del comportamiento frente a instalación exhaustiva. Costes Kubernetes en AKS/GKE: modalidades de control plane, nodos, balanceadores, discos y tráfico. |
| **Requisitos de preparación** | Entornos AKS/GKE, acceso y configuraciones comparativas preparados. |
| **Contenido complementario** | Instalaciones completas independientes y catálogo de add-ons de ambos proveedores. |

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

**PF · René Serral y Rael Garcia · 3 horas · Concentración 🟡 Media**

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
