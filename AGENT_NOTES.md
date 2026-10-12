# Notas de sesion - Optimizacion de contenido del postgrado

> Archivo de continuidad para retomar el trabajo en otra sesion. Resume el estado
> real del repo (que esta aplicado en disco vs que esta acordado en conversacion
> pero AUN NO escrito en ningun archivo). Generado: 2026-10-08.

## Acuerdos posteriores — pendientes de aplicar al generador

Esta sección prevalece sobre las notas históricas inferiores. El usuario pide trabajar localmente, registrar y commitear cada cambio aprobado, y regenerar todos los documentos al final. No ajustar por ahora el contenido para cuadrar horas o ECTS: cubrir el temario oficial copiado por el usuario desde https://upcschool.upc.edu/esp/estudis/formacio/curs/305300/platform-engineering-devops-kubernetes/.

### Últimos acuerdos: reparto y concentración (prevalecen sobre propuestas anteriores)

- Reparto actual: M1 una sesión DevOps/PE; M2 tres sesiones por proveedor (AWS/Azure/GCP), con Terraform/OpenTofu integrado y Python progresivo. Se elimina la sesión independiente de automatización. Bash se aplica principalmente a scripting/Tekton.
- M5: observabilidad (3), scripting/Tekton, Git/Prow, ArgoCD, Traefik/Istio, entrega progresiva, escalado: 9 sesiones. Tekton antes de Prow; introducir Git mínimo para trabajar el repositorio, colaboración/PR después. Usar Python también en la aplicación observada y las verificaciones/pipelines cuando aporte valor.
- M3 seis, M4 cinco y M6 cinco provisionales: total 29 sesiones / 87h, Proyecto Final aparte; una sesión disponible. No confundir con los repartos históricos inferiores.
- Pulumi al final de GCP: 10–15 min, comparar un recurso en HCL con Python (parámetros/dependencias/outputs/estado), sin instalación ni lab propio. Si no cabe, ampliación.
- EKS/kOps pasa de rojo a amarillo: lanzar EKS con Terraform y explicar mientras se despliega; presentar y lanzar kOps con configuración preparada, solapando esperas si procede. Desplegar la misma aplicación y comparar operación, actualizaciones, disponibilidad, costes y recuperación. Permisos/infraestructura comprobados, clústeres de respaldo y limpieza. No buscar dos despliegues autónomos ni operación avanzada.
- AWS pasa de rojo a amarillo: ejemplo Terraform preparado de identidad/red/VM/almacenamiento; explicar durante despliegue, modificar variable, revisar plan/aplicar y ejecutar consulta Python pequeña. Fuera del alcance de esta clase: curso completo de HCL/boto3, diseño autónomo desde cero y catálogo AWS (bases de datos/mensajería/serverless). Estado remoto y módulos se desarrollan después; testing/CI Terraform sigue pendiente de encaje oficial.
- Arquitectura/API/kind/autenticación/RBAC: propuesta guiada alrededor de una petición kubectl; control plane/nodos, API/almacenamiento/reconciliación/Pod, kubeconfig/certificados/tokens/ServiceAccounts, Role/RoleBinding con permiso y denegación. OIDC y admisión conceptuales, configuración pendiente; internos y montaje en la sesión propia del clúster desde cero. Usuario pasó al siguiente rojo sin objeciones; no dar la ubicación de configuración OIDC/admisión por resuelta.
- **Networking M3 aprobado, pasa a amarillo:** recorrer Pod→Pod (CNI), descubrimiento/acceso mediante Service/CoreDNS, exposición con un ejemplo Gateway API y explicación de Ingress, NetworkPolicy para bloquear/permitir lo necesario. Clúster con CNI y controlador de entrada preparados; una aplicación y manifiestos preparados.
- **Fuera del laboratorio de networking M3:** instalación y comparación de varios CNI, catálogo completo de tipos de rutas y networking avanzado. Esto limita la práctica, no elimina Services/DNS/CNI/NetworkPolicy/Ingress/Gateway API del contenido. Traefik/Istio avanzado va a M5; comparativas de CNI y rutas adicionales quedan como ampliación. El usuario pide mantener explícitamente esta nota de exclusiones.

- **Trazas y correlación aprobado, pasa a amarillo:** dos servicios preparados; petición distribuida e instrumentación automática, sin programarla desde cero. Seguir traza por Collector hasta Tempo; provocar latencia y localizar el servicio responsable en Grafana; relacionar con métricas/logs con enlaces previamente configurados. Objetivo: entender y diagnosticar una petición distribuida.
- **Fuera de esta sesión / ampliación:** SDK en profundidad, instrumentación manual completa, sampling avanzado y operación de Collector/Tempo en producción. OpenTelemetry, Collector, Tempo y correlación se mantienen en el contenido.

- **Traefik/Istio aprobado, pasa a amarillo:** componentes preparados; entrada externa con Traefik (routing/TLS reutilizando cert-manager), comunicación entre servicios con Istio (mTLS y política de acceso). Modificar pocas reglas y observar resultados. Mostrar reparto entre dos versiones como preparación de Argo Rollouts, sin repetir el canary completo. Distinguir entrada de tráfico y service mesh.

- **Escalado aprobado, pasa a amarillo:** aplicación sometida a carga; HPA como laboratorio principal (réplicas por CPU), VPA como consulta breve de recomendaciones sin ajustes automáticos que interfieran con HPA; KEDA con cola preparada para mostrar escalado por eventos; Karpenter con demostración preparada de provisión de nodos ante Pods pendientes y consolidación posterior. Mantener los cuatro componentes de la web. Explicar que KEDA usa HPA para el escalado de réplicas y evitar controladores compitiendo sobre el mismo workload durante los labs.
- **Extras de escalado:** catálogo completo de triggers KEDA, métricas personalizadas complejas, tuning avanzado, políticas avanzadas de capacidad/Spot y optimización profunda de costes.

Semáforo actual: 29 sesiones / 87h sin Proyecto Final. DevOps/PE, ExternalDNS/cert-manager y Knative en verde; el resto en amarillo bajo el alcance guiado/preparado o introductorio acordado. No quedan rojos con ese alcance, pero no implica resolución de los contenidos oficiales pendientes. M6 sigue provisional y su amarillo supone visión general/demos. No regenerar documentos aún.

### Extras fuera del alcance principal — registro consolidado

El usuario pide conservar explícitamente todo lo apartado como ampliaciones. No considerarlos tareas aprobadas para desarrollar ahora ni añadir sesiones automáticamente. Limitar profundidad práctica no elimina la cobertura conceptual prometida en la web.

- **Cloud e IaC:** curso completo de HCL, recorrido completo por boto3/SDK de cada cloud, infraestructura diseñada autónomamente desde cero y catálogo exhaustivo de servicios (bases de datos, mensajería, serverless). Diseño avanzado de módulos propios, sesión adicional de IaC y laboratorio propio de Pulumi como posibles ampliaciones. Pulumi permanece como comparación breve si cabe. Estado remoto, variables, outputs y módulos existentes siguen en el recorrido principal.
- **EKS/kOps:** dos despliegues construidos autónomamente y operación avanzada (actualizaciones/recuperación practicadas en profundidad). El recorrido principal despliega ambos con material preparado, explica responsabilidades y compara sobre la misma aplicación.
- **Networking M3:** instalación y comparación de varios CNI, catálogo completo de rutas y networking avanzado. El principal conserva Services/CoreDNS/CNI/NetworkPolicy y un ejemplo Gateway API con explicación de Ingress. Traefik/Istio tiene su sesión principal posterior.
- **Scheduling:** opciones avanzadas y catálogo exhaustivo; mantener scheduling básico y restricciones relevantes de almacenamiento en M3.
- **Helm/Kustomize:** creación de charts complejos desde cero; el principal usa/adapta paquetes existentes y un chart que instala un operator.
- **Vault:** HA, auto-unseal y operación en producción en profundidad; Vault/ESO deben seguir cubiertos en el principal por estar nombrados oficialmente.
- **Métricas:** HA/federación de Prometheus y operación avanzada de Mimir. Mimir se presenta en el principal; no se elimina.
- **Grafana/Loki/Alloy:** Grafana as Code y operación avanzada de Loki; Alloy se mantiene para recoger logs con configuración guiada/preparada.
- **OpenTelemetry/Tempo:** SDK en profundidad, instrumentación manual completa, sampling avanzado y operación de Collector/Tempo en producción. Principal: instrumentación automática y diagnóstico/correlación preparados.
- **Traefik/Istio:** instalación desde cero, catálogo de middlewares, routing TCP/UDP, tuning de Envoy y profundización en Ambient Mesh. Principal: routing/TLS de entrada, mTLS/política de acceso entre servicios y preparación del reparto de tráfico.
- **ArgoCD (propuesta de alcance por afinar):** ApplicationSets avanzado, multi-tenancy y SSO como ampliaciones; mantener aplicaciones, sincronización, health y drift como eje práctico.
- **Operators/Go (M6 provisional):** curso completo de Go, CLIs con Cobra/Viper, concurrencia avanzada y operator desarrollado desde cero. Principal propuesto: leer/modificar un ejemplo y entender CRD/reconciliación/Kubebuilder/Operator SDK.

**Contenido oficial pendiente de encaje, NO clasificar como extras prescindibles:** Git avanzado; testing/CI de Terraform; redes/DNS/CDN con Cloudflare; OIDC/admission controllers. PSA/Kyverno/Gatekeeper son posibles implementaciones, todavía sin decidir ubicación/profundidad. M6 queda pendiente de revisión final; no dar por cerrado el alcance de sus demos.


### M1–M2: sesiones 2–5 reorganizadas y aprobadas

Este reparto sustituye la sesión aislada y concentrada de Bash/Python: programación e IaC se aprenden por capas, aplicadas a un mismo caso real durante cuatro sesiones. La sesión 1 de DevOps/Platform Engineering no cambia. Go se reserva para operators en M6.

2. Automatización local: preparar herramientas y caso práctico. Bash para ejecutar comandos y comprobar resultados; Python para leer configuración, consumir una API y generar un informe. Introducir asistencia de IA y revisión de resultados, sin intentar dominar ambos lenguajes en una clase.
3. AWS: identidad, red, VM y almacenamiento. Terraform/OpenTofu para aprovisionar; Bash/AWS CLI para verificar y Python para consultar recursos. Introducir HCL, provider, recursos y flujo init/plan/apply/destroy conforme se necesitan.
4. Azure: reproducir el caso y entender diferencias. Incorporar variables, outputs y uso de módulos existentes; adaptar verificaciones con Azure CLI y Python, usando ejemplos preparados.
5. GCP: completar comparación entre proveedores. Reutilizar el patrón, introducir estado remoto y comparar brevemente con Pulumi (10–15 min, sin laboratorio propio).

Caso común: crear infraestructura pequeña, consultar su estado y comprobar que funciona. Scripts pequeños preparados: no enseñar tres SDK completos ni recorrer catálogos de servicios. IA para escribir/adaptar código, comprobando permisos, resultados y limpieza de recursos. Kubernetes gestionado permanece en M4. Mantiene cuatro sesiones, sin añadir horas. La posible sesión independiente de IaC avanzado sigue como ampliación futura.

### Cómputo lectivo corregido por el usuario

El Proyecto Final NO computa en las 30 sesiones / 90 horas. Con el reparto provisional M1=2, M2=3, M3=6, M4=5, M5=8 y M6=5: 29 sesiones / 87h lectivas; queda una sesión / 3h disponible. Consolidación y defensa del proyecto se cuentan aparte. Las cifras históricas que incluían PF en las 90h quedan sustituidas.

### M6: propuesta pendiente de retomar

Enfoque de visión general, conceptos/casos de uso/comparación/demos. Último reparto provisional: operators con Go; Cluster API con Hosted Control Planes (HyperShift/vCluster/Kamaji); Knative; multi-cluster (Istio/Cilium/Submariner); Crossplane y Velero. El usuario ve sentido en juntar Cluster API con HCP; no tratar el resto del bloque como cerrado.

### M3 acordado: seis sesiones

1. Contenedores y OCI.
2. Arquitectura, API, kind, autenticación y RBAC básico.
3. Ejecutar y configurar: Pods, Deployments, Jobs, ConfigMaps, Secrets, probes, recursos y scheduling básico.
4. Persistencia y workloads con estado: volúmenes, PV/PVC, StorageClass, CSI, StatefulSets y restricciones de ubicación.
5. Comunicar y exponer: Services, CoreDNS, CNI, NetworkPolicy e Ingress/Gateway API.
6. Clúster desde cero: PKI, etcd, control plane y unión de un nodo. Sesión propia con material preparado.

### M4 acordado: cinco sesiones

1. EKS y Kubernetes autogestionado en AWS; comparar responsabilidades y operación sobre EC2/VPC, sin repetir el montaje desde cero de M3.
2. AKS y GKE: aplicar el mismo marco de identidad, redes, nodos, actualizaciones y modos de operación.
3. Kustomize y Helm: bases/overlays/patches; charts existentes, values/templates/releases; combinación de ambas herramientas; chart que instala un operator. Charts complejos propios como ampliación.
4. ExternalDNS y cert-manager: DNS necesario, publicación de registros, certificados/ACME y renovación; exponer la misma aplicación mediante dominio y HTTPS. Crossplane se concentra en M6, conservando la conexión con M4.
5. Gestión de secretos externos: almacén, identidad/permisos, entrega como Secret o archivos y actualización/rotación. AWS Secrets Manager como ejemplo; ESO y ASCP/CSI como alternativas. Vault y ESO deben cubrirse porque están nombrados oficialmente. Continuidad con Terraform y Helm; no fijar todavía la implementación del laboratorio.

Admisión y políticas (PSA/Kyverno/Gatekeeper) quedan en el aire para decidir ubicación y profundidad. Admission controllers sí aparece en el contenido oficial de M3. Pendiente contrastar también cobertura de Git avanzado, testing/CI de Terraform y redes/DNS/CDN con Cloudflare, recortados previamente pero explícitos en la web; no dar esos huecos por resueltos.

### M5: bloque de observabilidad aprobado

Tres sesiones sobre la misma aplicación, con continuidad del entorno Kubernetes y despliegues Helm preparados. Priorizar consulta y diagnóstico frente a instalación. Aplicación con dos servicios preparada para la tercera sesión.

1. Prometheus, PromQL y Alertmanager: qué medir (infraestructura/aplicación), contadores/histogramas, labels/cardinalidad; scraping, exporters, descubrimiento; Prometheus Operator, ServiceMonitor/PodMonitor; consultas de tasas, errores, latencia y agregaciones; reglas y Alertmanager (agrupación, routing, silencios). Lab: conectar la app, provocar errores/carga, consultar y comprobar una alerta. Introducir Mimir y almacenamiento de métricas a escala, sin laboratorio completo. kube-prometheus-stack preparado. HA/federación/operación avanzada como ampliación.
   Reparto orientativo de 180 min: 20 métricas, 30 recogida, 40 PromQL, 25 alertas, 55 lab, 10 límites/Mimir.
2. Grafana, Loki y Alloy: datasources, paneles, variables y dashboard pequeño con tráfico/errores/latencia; Loki, labels frente a campos del mensaje, cardinalidad; recoger logs de Pods con Alloy, configuración guiada/preparada; LogQL y Explore, filtros y extracción de JSON. Lab: provocar fallo, detectarlo en métricas y encontrar logs en el mismo intervalo. No profundizar en Grafana as Code ni operación avanzada de Loki. **El usuario ha aprobado reintroducir Alloy**: este acuerdo sustituye la propuesta histórica de quitarlo.
3. OpenTelemetry, Collector y Tempo: spans/contexto/propagación entre servicios, instrumentación automática, receivers/processors/exporters y búsqueda de peticiones lentas desde Grafana. Lab: provocar latencia y correlacionar métrica → traza → logs. Preparar trace ID en logs, enlaces de Grafana y exemplars cuando proceda. Collector para trazas; no repetir la recogida de logs con Alloy. Es la sesión más exigente: no desarrollar instrumentación desde cero. Mimir ya se introduce en la primera sesión.

Resultado pedagógico: 1) qué falla y cuándo actuar; 2) qué ocurrió cuando falló; 3) dónde se atasca la petición. Explicar el solapamiento entre Alloy y OTel Collector y el motivo de la configuración elegida para los labs. No presentar su reparto logs/trazas como una limitación de las herramientas.

### M5: orden y separación acordados después de observabilidad

- Git y CI con Prow/Tekton antes de GitOps con ArgoCD: código → PR → validación → imagen → despliegue. Prow preparado para no consumir la clase instalándolo; Tekton ejecuta pipelines. Git básico se introduce con los PR. Se mantienen provisionalmente dos sesiones para este bloque; la propuesta de tres (Git/Prow, Tekton, ArgoCD) NO quedó aprobada.
- Después, networking avanzado con Traefik e Istio.
- **Entrega progresiva en una sesión propia, después de networking:** canary y blue/green con Argo Rollouts, aprovechando ArgoCD, Prometheus y reparto de tráfico con Istio/Traefik. Lab: nueva versión, análisis de métricas y rollback automático.
- **Escalado en otra sesión, después de entrega progresiva:** HPA/VPA, KEDA y Karpenter; distinguir escalado de Pods de capacidad de nodos. Lab: variar carga y observar/adaptar capacidad. No requiere networking avanzado como prerrequisito estricto, pero se mantiene ese orden pedagógico.
- No forzar horas/ECTS; conservar todas las tecnologías del contenido oficial.

Pendiente: afinar el alcance de Git/CI y ArgoCD, revisar networking y concretar las dos sesiones separadas; después M6. No aplicar ni generar documentos todavía; las notas son el registro de continuidad.

---

## Actualización aplicada — decisión del usuario (2026-10-08)

Esta sección prevalece sobre las propuestas y el estado histórico que siguen debajo.

- M2 queda en 3 sesiones / 9h / 1 ECTS: AWS como caso principal, Azure y GCP como transferencia del mismo patrón con ejemplos preparados. Terraform/OpenTofu integrado; identidad, redes, VM y almacenamiento. Pulumi: comparación breve de 10–15 minutos, sin laboratorio propio.
- EKS/AKS/GKE y su aprovisionamiento siguen en M4; no duplicarlos en M2.
- Git avanzado sale de M2. Git básico y principios GitOps se enseñan con ArgoCD; PR y validaciones con Prow/Tekton. M5 pasa a 7 sesiones / 21h / 2 ECTS.
- Total verificado: 30 sesiones / 90h / 12 ECTS. Los ECTS por módulo no cambian.
- **Posible ampliación futura, NO aprobada ni incluida en las 90h:** añadir una cuarta sesión independiente de IaC si se quiere profundizar en Terraform/OpenTofu, diseño de módulos propios, testing y automatización, o dar más práctica por proveedor. Requiere revisar el reparto de horas; no añadirla automáticamente. Pulumi podría ampliarse solo si se decide expresamente.
- Alcance actual: módulos existentes, variables, outputs y estado. No prometer dominio de tres clouds ni diseño avanzado de módulos tras 9h.
- Otros recortes y traslados de contenido de las notas históricas siguen pendientes de aprobación; no aplicar en bloque.
- Mantener el trabajo por cambios concretos aprobados por el usuario.

---

## Contexto del programa

- Posgrado en Platform Engineering y DevOps con Kubernetes (UPC School, curso 305300)
- Ficha oficial publicada: 12 ECTS / 90h lectivas / 30 sesiones de 3h (martes y jueves, 18:00-21:00)
- Inicio 03/11/2026, fin clases 18/03/2027
- Web oficial: https://upcschool.upc.edu/esp/estudis/formacio/curs/305300/postgrau-platform-engineering-devops-kubernetes/
- Fuente de verdad del contenido/calendario: generate_docs.py (dict MODULES, NON_TEACHING, SCHEDULE_START/END). Genera .docx, .xlsx y calendario.md.
- Documento narrativo detallado: roadmap-postgrado-kubernetes-detallado.md (debe reflejar EXACTAMENTE lo que hay en generate_docs.py; en este momento NO coincide del todo, ver mas abajo).
- Vista resumida: roadmap-postgrado-kubernetes.md.
- Contexto general del repo: CLAUDE.md.

## Regla de oro del proyecto

No se puede quitar ninguna tecnologia que la web oficial prometa explicitamente
(p. ej. Prow, Istio+Traefik, HyperShift+vCluster+Kamaji, Istio multicluster+Cilium+Submariner
son compromisos comerciales). Solo se puede recortar/mover contenido que:
1. No este mencionado literalmente en la web oficial, O
2. Sea un rebalanceo interno de horas/sesiones entre modulos que mantenga los ECTS oficiales
   por modulo intactos (patron ya usado en M1/M5/M6).

## ESTADO ACTUAL EN DISCO (verificado con git diff --stat a fecha de hoy)

Archivos modificados respecto a origin/main (sin commitear):
- generate_docs.py
- roadmap-postgrado-kubernetes-detallado.md
- roadmap-postgrado-kubernetes.md
- Calendario_Postgrado_Kubernetes.xlsx, .docx (regenerados desde generate_docs.py)

Archivos nuevos sin trackear: calendario-upc.pdf, calendario.md, .DS_Store, infra/ (ignorar estos dos ultimos).

### Lo que SI esta aplicado en generate_docs.py (y por tanto en calendario.md/.xlsx/.docx regenerados)

1. Calendario alineado con festivos oficiales UPC-FIB: NON_TEACHING = La Immaculada (8 dic 2026),
   vacaciones Navidad (24, 29, 31 dic 2026, 5 ene 2027), festivo UPC (9 feb 2027). (Ya NO incluye
   22 dic/7 ene que eran dias de margen propios, no festivos oficiales.)
2. M1 reducido de 4 a 2 sesiones: Go se saco de M1. M1 ahora = "DevOps y PE" + "Bash y Python
   para DevOps" (6h en vez de 12h). Go se mueve a M6.
3. M5 dividido de 5 a 6 sesiones: Observabilidad paso de 2 sesiones a 3
   ("Prometheus" / "Grafana y Loki (logs)" / "OpenTelemetry, Tempo y correlacion"). M5 ahora 18h.
4. M6 ampliado de 5 a 6 sesiones: nueva sesion "Go: de cero a controlador de Kubernetes"
   insertada ANTES de "Construccion de Operators". M6 ahora 18h.
5. Total se mantiene en 30 sesiones / 90h / 12 ECTS (verificado con script).
6. Sesion "Application bundles" (M4) reordenada: Kustomize -> Helm -> Helm+Kustomize -> caso real
   de chart que instala un operator (con guion de sesion de 180min documentado, bloques con tiempos).

### Snapshot de calendario calculado

Para regenerar el snapshot de fechas/sesiones calculadas por build_calendar():

cd /Users/rael/Code/raelga/UPC-k8s && python3 -c "
import sys
sys.path.insert(0, '.')
from generate_docs import build_calendar
sessions, buffer = build_calendar()
for s in sessions:
    print(s['n'], s['date'], s['day'], s['module_id'], '-', s['theme'])
print('Buffer:', buffer)
"

### DESINCRONIZACION CONOCIDA (IMPORTANTE)

roadmap-postgrado-kubernetes-detallado.md NO coincide completamente con generate_docs.py:
- Las secciones M5/M6/PF en el .md detallado todavia muestran la numeracion/fechas ANTIGUAS
  (Sesion 19-23 para M5, 24-28 para M6) en vez de las nuevas (17-22 para M5, 23-28 para M6).
- Falta reflejar ahi la sesion nueva de Go (M6) y la division de Observabilidad en 3 (M5).
- Accion pendiente: reescribir el bloque M5+M6+PF completo del .md detallado para que
  coincida con generate_docs.py. (Se intento una vez pero quedo a medias - verificar antes de
  volver a tocar para no duplicar trabajo.)

## ACORDADO EN CONVERSACION PERO NO ESCRITO EN NINGUN ARCHIVO TODAVIA

Todo lo de esta seccion es solo discusion verbal de la sesion de hoy. Nada de esto esta en disco.
Hay que aplicarlo a generate_docs.py primero (fuente de verdad), luego regenerar
.docx/.xlsx/calendario.md, y luego sincronizar manualmente roadmap-postgrado-kubernetes-detallado.md
y roadmap-postgrado-kubernetes.md. El usuario quiere aprobar cada cambio antes de escribirlo.

### 1. Eliminar la sesion "Redes, DNS y CDN con Cloudflare" (M2) por completo

Motivo: la mayoria del contenido (TCP/IP generico, DNSSEC/DoH/split-horizon, CDN/anycast,
Cloudflare Workers/R2/WAF) no tiene conexion real con Kubernetes/Platform Engineering - es
networking generico o producto de un vendor sin aplicacion en el resto del programa.

Lo unico con conexion real (Cloudflare Tunnel para exponer servicios sin LB publico) se
reubica como mencion breve en la sesion de CNI/DNS de M3 (ver punto 4).

Efecto: M2 pasa de 4 a 3 sesiones (Git avanzado, Cloud Computing AWS/Azure/GCP, Terraform).
Libera 1 sesion completa en el balance global.

### 2. Recortar la sesion de "Git avanzado" (M2) - quitar lo "super avanzado"

Se queda (uso profesional real):
- Estrategias de branching (Git Flow, GitHub Flow, trunk-based)
- Rebase interactivo (squash, fixup, reword)
- Resolucion de conflictos (merge, rerere)
- Branch protection, CODEOWNERS, signed commits
- PR review (merge strategies, draft PRs)
- Git hooks (pre-commit, commit-msg)

Se quita (sin aplicacion real en contexto K8s/GitOps, confirmado con el usuario):
- Internals de Git (objects, reflog, packfiles, GC)
- bisect, worktree, submodules, subtrees, sparse-checkout
- Monorepos (Nx/Turborepo - ni siquiera aplican al stack del programa)

PENDIENTE DE DECIDIR: se queda como sesion propia de Git recortada, o se fusiona con
"GitOps: principios" (actualmente parte de la sesion GitOps/ArgoCD)? Se estaba evaluando la
fusion cuando se corto la sesion para escribir este archivo. Ultima propuesta sobre la mesa
(sin confirmar):

Sesion "Git y GitOps: del control de versiones al despliegue declarativo"
1. Git para equipos: branching, rebase interactivo, resolucion de conflictos
2. Colaboracion y calidad: branch protection, CODEOWNERS, PR review, hooks
3. GitOps: principios (declarativo, versionado, automatizado, reconciliado, pull vs push) -
   con mencion de que la estructura de branches ya vista aplica al repo GitOps

### 3. Mover fundamentos de TCP/IP/TLS/gRPC a la sesion de networking de M3 (Services/Ingress)

Solo lo que tiene aplicacion directa en K8s: TLS/mTLS (base de Istio/cert-manager),
gRPC (soportado nativamente por GRPCRoute de Gateway API), HTTP/2 (Ingress controllers
modernos). Se descarta explicitamente: capas OSI genericas, HTTP/3/QUIC sin aplicacion K8s.

Se fusiona DENTRO del tema existente "Services" de esa sesion (M3), sin crear un tema nuevo,
para no subir la densidad de una sesion que ya tiene 4 temas.

### 4. Mover CoreDNS + mencion de Cloudflare Tunnel a la sesion de CNI/DNS de M3

Dentro del tema existente de "CNI y DNS" (Calico/Cilium/Flannel/NetworkPolicy/CoreDNS):
anadir mencion de Cloudflare Tunnel como alternativa a LoadBalancer publico para exponer
servicios sin IP publica (conecta con el lab original que ya mencionaba esto).

### 5. Mover DNS fundamentos + ExternalDNS con Cloudflare a la sesion de infra declarativa de M4

La sesion "Infraestructura declarativa: ExternalDNS, cert-manager y Crossplane" (M4) gana
un tema de fundamentos DNS (registros A/CNAME/TXT, resolucion, TTL) justo antes de
ExternalDNS, y ExternalDNS explicitamente menciona Cloudflare como uno de sus providers
(ya estaba, solo se refuerza la conexion).

### 6. Separar responsabilidades entre "Go: de cero a controlador" y "Construccion de Operators" (M6)

Problema detectado: ambas sesiones mencionaban controller-runtime/reconciliation loop,
duplicado a medias.

Fix acordado: la sesion de Go deja de mencionar controller-runtime/reconciliation loop
del todo - se queda solo con fundamentos de Go + client-go (cliente HTTP/REST) + CLIs/tooling
(cobra/viper/testify/golangci-lint). La sesion de "Construccion de Operators" sigue siendo la
UNICA que introduce controller-runtime/reconciliation loop, ahora con todo el contexto
(CRDs propios) en vez de a medias.

Sesion de Go resultante (3 temas, antes 4):
1. Fundamentos de Go: tipos, structs, interfaces, goroutines, channels, errores idiomaticos
2. client-go: clientset, kubeconfig, serializacion, listar/filtrar/crear recursos
3. CLIs y tooling: cobra/viper, logging, go test, mocks con testify, golangci-lint

### 7. Dividir la sesion "GitOps y pipelines CI/CD: ArgoCD, Prow y Tekton" (M5) en 2

Problema: 7 temas en una sesion (demasiado denso) + duplicado con Argo Rollouts (ya
protagonista de otra sesion de M5).

Fix acordado:

Sesion A - GitOps con ArgoCD (3 temas):
1. Principios GitOps: declarativo, versionado, automatizado, reconciliado. Pull vs Push
2. ArgoCD: Applications, AppProjects, ApplicationSets, sync policies, waves, hooks, RBAC
3. ArgoCD avanzado: multi-tenancy, SSO, App of Apps, ApplicationSet generators, notifications

Sesion B - Pipelines CI/CD: Prow y Tekton (3 temas):
1. Prow: arquitectura CI nativa en K8s, plugins, Tide, Deck, ProwJobs
2. Tekton: Tasks, Pipelines, PipelineRuns, Workspaces, Triggers, Chains
3. Integracion Tekton + ArgoCD para workflows end-to-end

(Se quita la mencion de "ArgoCD Image Updater y Argo Rollouts" de aqui - Rollouts ya es
protagonista en la sesion de "Entrega progresiva y escalado".)

Efecto: M5 gana 1 sesion (+1). Esto compensa exactamente la sesion perdida en M2 (punto 1),
manteniendo el total en 30 sesiones / 90h. OJO: revisar con cuidado el balance total antes de
aplicar (ver seccion de proximos pasos, punto 3).

### 8. Grupo A - Recortes puntuales aprobados hace tiempo, AUN sin escribir (anteriores a esta ronda)

Confirmado otra vez que siguen pendientes:

- "Observabilidad (II): Grafana stack" -> quitar Alloy (collector). No esta en la web oficial;
  redundante con el OTel Collector de otra sesion.
- "Entrega progresiva y escalado" -> quitar Feature flags (Flagger/OpenFeature). No esta en la
  web oficial.
- "Multi-cluster" -> quitar OCM, Rancher MCM. No estan en la web oficial.
- "Multi-cloud y Disaster Recovery" -> quitar Thanos/Mimir federados, OTel Collector gateway.
  No estan en la web oficial.

(Confirmado: Virtual Kubelet se queda - el usuario pidio mantenerlo explicitamente, es pieza
clave del serverless.)

## Tabla de densidad

Ultima version compartida (ANTES de los puntos 1-8 de esta ronda) esta en el historial de
conversacion. Esta DESACTUALIZADA respecto a los cambios 1-8 de arriba (que aun no se han
aplicado) - regenerar tabla completa despues de aplicar todo.

Sesiones que seguian en Alta densidad en esa tabla previa (antes de aplicar el Grupo A de
recortes y los puntos 1-7 de esta ronda): GitOps/Prow/Tekton (ahora se divide, ver punto 7),
Traefik/Istio, Entrega progresiva/escalado, Cluster API/serverless, Multi-cluster.

## PROXIMOS PASOS (orden sugerido para la siguiente sesion)

1. Decidir el pendiente del punto 2 (Git recortado: sesion propia o fusion con GitOps?).
2. Aplicar en generate_docs.py (fuente de verdad) los puntos 1, 2 (segun decision), 3, 4, 5, 6, 7, 8.
3. Verificar totales con cuidado: debe seguir dando 30 sesiones / 90h / 12 ECTS tras los cambios.
   M2 pasa de 4 a 3 (punto 1). M5 pasa de 6 a 7 si se aplica la division de GitOps/CI-CD (punto 7).
   Recalcular bien la aritmetica exacta sesion por sesion con build_calendar() antes de escribir
   nada, puede haber un desfase de +1 o -1 sesion segun como se combinen los puntos 1 y 7.
   NO asumir, recalcular con el script.
4. Regenerar .docx/.xlsx/calendario.md con: python3 generate_docs.py
5. Reescribir roadmap-postgrado-kubernetes-detallado.md completo para M2, M3, M4, M5, M6
   para que coincida EXACTAMENTE con generate_docs.py (incluye corregir la desincronizacion
   ya existente de M5/M6/PF mencionada arriba).
6. Actualizar roadmap-postgrado-kubernetes.md (vista resumida) y CLAUDE.md (tabla de
   horas por modulo) a los nuevos totales.
7. Regenerar la tabla de densidad completa con el resultado final.
8. Confirmar con el usuario antes de cada escritura en disco - el usuario ha pedido
   explicitamente ir aprobando cambio por cambio, no aplicar en bloque sin confirmacion.

## Preferencias de estilo del usuario (importante para la siguiente sesion)

- Prefiere avanzar en pasos pequenos, aprobando cada cambio antes de la siguiente propuesta.
- Pide explicitamente NO generar/escribir archivos hasta que lo confirme - en esta ronda de
  conversacion se mantuvo todo a nivel de propuesta verbal a peticion suya (se enfado cuando
  se generaron tablas/archivos sin que lo pidiera explicitamente).
- Cuestiona activamente las justificaciones ("esto tiene sentido en un postgrado de K8s?") -
  no aceptar "no esta en la web" como unico criterio; siempre evaluar relevancia pedagogica real
  para Kubernetes/Platform Engineering, no solo riesgo comercial/legal.
- Le gustan las tablas de densidad (verde/amarillo/rojo) para valorar de un vistazo, pero SOLO
  cuando las pide explicitamente.
