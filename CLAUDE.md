# Project Context — UPC DevOps Postgrado

## What is this?

A university postgraduate program proposal for UPC (Universitat Politècnica de Catalunya) focused on Kubernetes, DevOps and Platform Engineering.

## Target Profile

- **Emergent (Junior):** 0-3 years of industry experience
- Entry: software engineers or sysadmins with basic Linux, networking and scripting knowledge
- Exit: Platform Engineer, SRE or Kubernetes Architect

## Program Structure

- **Title candidates:**
  - "Postgrado en DevOps, Kubernetes y Platform Engineering" (latest preferred)
  - "Postgrado en DevOps y Kubernetes: De la Infraestructura Cloud al Ecosistema Cloud Native"
  - "Postgrado en Kubernetes: Arquitectura, Operación y Ecosistema Cloud Native"
- **Total hours:** 140h lectivas
- **Session format:** 40 sessions of 3.5h each
- **Weekly dedication:** 7h/week (2 sessions)
- **Duration:** 20 weeks
- **Modules:** 12 modules in 9 thematic blocks
- **Languages:** Content in Spanish (castellano), university proposal form in Catalan

## Files in this directory

| File | Description | Status |
|------|-------------|--------|
| `ejemplo.docx` | Reference document from UPC showing expected format (binary, structure extracted) | Reference only |
| `Postgrado_Kubernetes_Platform_Engineering.docx` | Detailed program document following ejemplo.docx format | Generated |
| `Calendario_Postgrado_Kubernetes.xlsx` | Excel with 3 sheets: weekly calendar, module summary, session detail | Generated |
| `roadmap-postgrado-kubernetes.md` | Full roadmap in markdown (140h, 40 sessions of 3.5h) | Updated |
| `roadmap-postgrado-kubernetes-full.md` | Original expanded version (pre-140h adjustment) | Legacy, can be deleted |
| `proposta-universitaria.md` | Catalan texts for UPC proposal form | Updated |
| `generate_docs.py` | Python script to regenerate .docx and .xlsx | Working |
| `CONTEXT.md` | This file | Current |

## Module Breakdown (40 sessions = 140h)

| Module | Title | Sessions | Hours |
|--------|-------|----------|-------|
| M01 | Fundamentos de DevOps y Platform Engineering | 1 | 3.5h |
| M02 | Programación para DevOps: Go, Python y Bash | 2 | 7h |
| M03 | Redes, DNS y CDN con Cloudflare | 1 | 3.5h |
| M04 | Control de Versiones Avanzado con Git | 1 | 3.5h |
| M05 | Cloud Computing: AWS, Azure y GCP | 3 | 10.5h |
| M06 | Infraestructura como Código con Terraform | 2 | 7h |
| M07 | Contenedores y Ecosistema OCI | 2 | 7h |
| M08 | Kubernetes Core: Arquitectura y Building Blocks | 8 | 28h |
| M09 | Kubernetes en Producción: Multi-cloud | 2 | 7h |
| M10 | Ecosistema Cloud Native: Bundles, IaC, Secrets y Observabilidad | 7 | 24.5h |
| M11 | GitOps, Pipelines y Networking Avanzado | 6 | 21h |
| M12 | Platform Engineering Avanzado: Operators y Multi-cluster | 5 | 17.5h |

## Catalan Proposal Texts (proposta-universitaria.md)

Contains the following sections required by UPC:
- **Resum de la proposta** (248 words, max 250)
- **Competència o altres informacions** (with similar programs, reports, reference URLs)
- **Continguts de l'estudi** (6 points, max 6)
- **Objectius del procés d'aprenentatge** (6 points, max 6)

## Key Decisions Made

1. Session blocks are exactly 3.5h (university scheduling constraint)
2. 7h/week, 2 sessions per week
3. Total 140h (adjusted from original 150h)
4. Kubernetes Core (M08) is the largest module at 28h (8 sessions) — intentional
5. No separate "Proyecto Final" module — project is embedded in the program
6. Operators referred to as "Operator Framework" (not Go/Kubebuilder specifically) in proposal texts
7. The .docx follows the visual structure of ejemplo.docx (title page, summary tables, block headers, module detail tables with topics, session breakdown tables, certifications, technologies)
8. Aligned with certifications: CKA, CKAD, CKS, Terraform Associate, Vault Associate, KCNA, CGOA

## Pending / Future Work

- [ ] Final title selection
- [ ] Fill in "Fecha orientativa" column in the Excel (actual calendar dates)
- [ ] Review and potentially adjust module hours based on UPC feedback
- [ ] Add instructor/professor assignments
- [ ] Add evaluation criteria per module
- [ ] Add detailed lab descriptions per session
- [ ] Potentially add a "Proyecto Final" if UPC requires it as a separate deliverable
- [ ] Regenerate .docx if content changes (run `python3 generate_docs.py`)

## How to Regenerate Documents

```bash
cd /Users/rael/UPC-DevOps
python3 generate_docs.py
```

Requires: `pip3 install python-docx openpyxl`

## Important Notes

- The `generate_docs.py` script contains ALL the module data (titles, descriptions, topics, session details). If you need to change content, change it there and re-run.
- The markdown file is maintained separately — changes to one do NOT propagate to the other automatically.
- The Catalan proposal texts in `proposta-universitaria.md` are also maintained separately.
