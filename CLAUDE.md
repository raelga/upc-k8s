# Project Context — UPC DevOps Postgrado

## Active edition

Posgrado en Platform Engineering y DevOps con Kubernetes · UPC School.
Titulación: Diploma de experto en Platform Engineering y DevOps con Kubernetes.
12 ECTS · 90h · Live online · Castellano · 5 meses.
Dirección académica: Rael Garcia Arnes y René Serral Gracià.
Entry profile: junior engineers/sysadmins with basic Linux, networking and scripting.

`2026/README.md` is the edition entry point. `2026/curso.json` contains structured session data; the syllabi, teaching guide, Markdown calendar and CSV are maintained separately. Update affected representations together; there is no document generator or automatic synchronization.

## Approved planning constraints

- 30 sessions of 3h, Tuesday/Thursday 18:00–21:00, Europe/Madrid, from 03/11/2026 to 18/03/2027.
- 29 content classes plus the final-project presentation and defense on 18/03/2027 with René Serral and Rael Garcia, included in the 90h. Project development is autonomous work.
- Last content class: 11/03/2027. No class on 09/03 or 16/03; Christmas breaks include 22/12 and 07/01. See the edition calendar for all non-teaching dates.
- Six thematic modules plus Proyecto Final. M1 comprises 9h within the 90h: 3 dedicated hours and 6 integrated hours (1h in each cloud-provider session, 1.5h Tekton, 1.5h operators). Do not double-count these hours. Its 1.5 ECTS include assessed autonomous work.
- Confirmed instructors: René Serral, Rael Garcia, David Girón and Marc Catrisse. Preserve dates and assignments unless explicitly changed.
- Keep required core, guided lab and optional extensions distinct. Do not turn advanced extensions into mandatory project requirements.
- Trivy belongs in Tekton; no separate security session. OPA/Gatekeeper and Velero belong in M6. Crossplane belongs with Cloudflare/ExternalDNS/cert-manager, not operators/Go. Snyk was explicitly excluded.
- Preserve coverage of advanced Git, Terraform testing/CI, Cloudflare CDN, OIDC, Go and AI-assisted programming as detailed in the internal teaching guide.
- Operators/Go is curricular M6 taught by Rael after Helm: session 14, 12/01/2027. Marc teaches sessions 26–29. Tekton, Git/Prow and ArgoCD precede observability: sessions 17–19 with Rael, 21/01–28/01. David teaches observability in sessions 20–22. Rael's last content class is 28/01; he retains the 18/03 defense. M1 transversal coverage is in sessions 1, 2, 3, 4, 14 and 17.
- Include 15–20 minutes per cloud provider for cost queries, filters, budgets/alerts and cleanup (AWS Billing/Cost Explorer/Budgets, Azure Cost Management, GCP Cloud Billing). Explain billing delays and that budgets do not automatically stop spending. Revisit control-plane, node, load-balancer, disk and traffic costs in managed-cluster sessions. This is a teaching-design addition, not a literal requirement of the published website.

## Repository layout

- `2026/`: authoritative edition documents and structured data.
- `docs/proposta-universitaria.md`: Catalan university proposal, not the teaching calendar. Preserve UPC form limits; proposal terminology uses Operator Framework.
- `references/calendario-upc.pdf`: undergraduate academic-calendar reference, not the course calendar.
- `README.md`: repository navigation and maintenance guidance.

Historical roadmaps, generated Word/Excel documents and the old generator were retired because they describe a superseded allocation. Their content remains in Git history. Do not restore their dates, grading percentages or hour allocation as current policy.
