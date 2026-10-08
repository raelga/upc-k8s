# Notas de sesion - Optimizacion de contenido del postgrado

> Archivo de continuidad para retomar el trabajo en otra sesion. Resume el estado
> real del repo (que esta aplicado en disco vs que esta acordado en conversacion
> pero AUN NO escrito en ningun archivo). Generado: 2026-10-08.

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
