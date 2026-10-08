# Project Context — UPC DevOps Postgrado

## What is this?

A university postgraduate program proposal for UPC (Universitat Politècnica de Catalunya) focused on Kubernetes, DevOps and Platform Engineering.

## Target Profile

- **Emergent (Junior):** 0-3 years of industry experience
- Entry: software engineers or sysadmins with basic Linux, networking and scripting knowledge
- Exit: Platform Engineer, SRE or Kubernetes Architect

## Program Structure

- **Published title:** "Posgrado en Platform Engineering y DevOps con Kubernetes"
- **Titulación:** Diploma de experto en Platform Engineering y DevOps con Kubernetes (UPC)
- **Total hours:** 90h lectivas
- **Credits:** 12 ECTS
- **Modality:** Live online
- **Duration:** 5 meses (1ª edición)
- **Schedule:** Martes y jueves, 18:00–21:00 · Inicio 03/11/2026 · Fin 18/03/2027 · 30 sesiones de 3h
- **Structure:** 6 módulos + Proyecto Final
- **Dirección académica:** Rael Garcia Arnes, René Serral Gracià
- **Languages:** Content in Spanish (castellano), university proposal form in Catalan
- **Reference:** https://upcschool.upc.edu/esp/estudis/formacio/curs/305300/postgrau-platform-engineering-devops-kubernetes/

## Files in this directory

| File | Description | Status |
|------|-------------|--------|
| `ejemplo.docx` | Reference document from UPC showing expected format (binary, structure extracted) | Reference only |
| `Postgrado_Kubernetes_Platform_Engineering.docx` | Detailed program document following ejemplo.docx format | Generated |
| `Calendario_Postgrado_Kubernetes.xlsx` | Excel: program summary, dated session calendar, module breakdown (ECTS/hours), detailed contents | Generated |
| `roadmap-postgrado-kubernetes.md` | Short/overview roadmap (90h, 12 ECTS, 6 modules + Proyecto Final): titles, calendar, tech | Updated |
| `roadmap-postgrado-kubernetes-detallado.md` | In-depth roadmap of the SAME published program: 30 dated sessions with labs, objetivos, prerequisitos, evaluación, bibliografía per module; condensed 60 ECTS vision as appendix | Current |
| `proposta-universitaria.md` | Catalan texts for UPC proposal form | Updated |
| `generate_docs.py` | Python script to regenerate .docx and .xlsx | Working |
| `CONTEXT.md` | This file | Current |

## Module Breakdown (6 modules + Proyecto Final = 90h / 12 ECTS)

| Module | Title | ECTS | Hours |
|--------|-------|------|-------|
| M1 | Fundamentos DevOps, Platform Engineering y Programación para Infraestructura | 1.5 | 6h |
| M2 | Cloud Computing Multicloud e Infraestructura como Código | 1 | 9h |
| M3 | Contenedores y Kubernetes Core. Ecosistema OCI | 2 | 15h |
| M4 | Kubernetes en Producción y Ecosistema Cloud Native | 2 | 15h |
| M5 | Observabilidad, GitOps, CI/CD y Networking Avanzado | 2 | 21h |
| M6 | Platform Engineering Avanzado: Operators, Serverless y Multi-Cluster | 2 | 18h |
| PF | Proyecto Final | 1.5 | 6h |
| | **Total** | **12** | **90h** |

The 6 published modules aggregate the original 12-module roadmap (M1←old M01+M02; M2←M03+M04+M05+M06; M3←M07+M08; M4←M09+M10 bundles/IaC/secrets; M5←M10 observabilidad+M11; M6←M12). M1 adds AI-assisted programming.

## Catalan Proposal Texts (proposta-universitaria.md)

Contains the following sections required by UPC:
- **Resum de la proposta** (248 words, max 250)
- **Competència o altres informacions** (with similar programs, reports, reference URLs)
- **Continguts de l'estudi** (6 points, max 6)
- **Objectius del procés d'aprenentatge** (6 points, max 6)

## Key Decisions Made

1. Program published by UPC at 90h lectivas / 12 ECTS, Live online, 5 meses
2. Structure: 6 thematic modules + a standalone Proyecto Final (1.5 ECTS / 6h)
3. The 6 published modules aggregate the original detailed 12-module roadmap (see mapping in Module Breakdown)
4. Kubernetes content is the core: M3 (Core + OCI, 15h) + M4 (Producción + Cloud Native, 15h) = 30h
5. Module M1 explicitly includes AI-assisted programming (Bash, Python, Go)
6. Operators referred to as "Operator Framework" (not Go/Kubebuilder specifically) in proposal texts
7. The .docx follows the visual structure of ejemplo.docx (title page, summary tables, module detail tables with topics, certifications, technologies)
8. Aligned with certifications: CKA, CKAD, CKS, Terraform Associate, Vault Associate, KCNA, CGOA

## Pending / Future Work

- [ ] Add instructor/professor assignments per module
- [ ] Add evaluation criteria per module and for the Proyecto Final
- [ ] Add detailed lab descriptions
- [ ] Regenerate .docx/.xlsx if content changes (run `python3 generate_docs.py`)

## How to Regenerate Documents

```bash
cd /Users/rael/Code/raelga/UPC-k8s
python3 generate_docs.py
```

Requires: `pip3 install python-docx openpyxl`

## Important Notes

- The `generate_docs.py` script contains ALL the module data (titles, descriptions, topics, session details). If you need to change content, change it there and re-run.
- The markdown file is maintained separately — changes to one do NOT propagate to the other automatically.
- The Catalan proposal texts in `proposta-universitaria.md` are also maintained separately.
