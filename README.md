# Power Circuit AI-Lite: An LLM-Driven Pipeline for Automated Netlist Generation of DC-DC Power Converters

[![Course](https://img.shields.io/badge/Course-25CS2207E%20GenAI%20%26%20AI%20Platform%20Engineering-blue)](https://github.com/charvikbattagiri057)
[![Academic Year](https://img.shields.io/badge/Academic%20Year-2026--2027-green)]()
[![Deliverable Tag](https://img.shields.io/badge/Release-Review--1%20Deliverable-orange)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

---

## 👥 Team Information & Mentors

* **Department:** Department of Electronics and Communication Engineering (ECE)
* **Institution:** KL Deemed to be University (KLH)
* **Course:** Generative AI & AI Platform Engineering (`25CS2207E`)
* **Course Coordinator:** DHARAMSOTU BHEEKYA
* **Project Guide / Supervisor:** Dr. V Sahiti / Dr. A Kiran Kumar

### Team Members
| S.No | Student Name | ID Number | GitHub Profile |
| :---: | :--- | :---: | :--- |
| 1 | **B. Ranga Charvik** (Lead) | `2520040108` | [@charvikbattagiri057](https://github.com/charvikbattagiri057) |
| 2 | **K. Pavan Karthik** | `2520040071` | Contributor |
| 3 | **R. Gnaneshwar** | `2520040076` | Contributor |

---

## 📄 Abstract

Designing a power electronic converter is still a largely manual process. Engineers calculate component values from the performance requirements, then transcribe the circuit into schematic form by hand, which is slow and prone to error. Each change to a specification, such as the input voltage, load current or switching frequency, means repeating the calculations and redrawing the circuit. This project presents **Power Circuit AI-Lite**, an automated pipeline that turns a plain-language requirement into a validated circuit description for DC-DC converters, covering buck and boost topologies.

The system uses a **FastAPI backend** that passes the user's requirements to **Google Gemini**, which extracts a structured specification of input and output voltage, load current and switching frequency. Component values are computed with analytical design equations, so the language model never performs the arithmetic itself. From these values the pipeline generates Python-based **SKiDL** code and runs programmatic **Electrical Rules Checks (ERC)** to detect connectivity and rule violations. It then exports a **KiCad-compatible netlist (`.net`)** for subsequent PCB layout. A command-line interface takes a designer from a text prompt to a netlist file in a single step. The approach is expected to shorten early-stage prototyping time and reduce manual calculation errors, since each generated design passes automated ERC validation before it reaches layout tools.

---

## 📂 Repository Structure

```plaintext
.
├── src/                      # Core application source code
│   ├── app/
│   │   ├── agents/           # LLM agent definitions (SpecAgent, SKiDLAgent)
│   │   ├── api/              # FastAPI server and route handlers
│   │   └── prompts/          # Few-shot prompts & system instructions
│   ├── tests/                # Smoke tests and unit verification
│   ├── build_circuit.py      # End-to-end interactive CLI generator
│   └── requirements.txt      # Python dependencies
├── docs/                     # Technical documentation & guides
│   ├── ARCHITECTURE.md       # Multi-agent system architecture
│   ├── API_REFERENCE.md      # FastAPI endpoints and schemas
│   └── KICAD_SKIDL_GUIDE.md  # KiCad symbol path & SKiDL configuration
├── data/                     # Reference data & component mappings
│   ├── README.md             # Data documentation & formulation notes
│   ├── spec_schemas/         # Converter specification JSON schemas
│   └── components/           # KiCad symbol and footprint definitions
├── results/                  # Generated circuit netlists, scripts & ERC logs
│   ├── buck_converter/       # Validated Buck converter outputs
│   └── sample_schematic.png  # Schematic smoke test visual
├── reports/                  # Project reports and review documentation
│   ├── PROJECT_ABSTRACT.md   # Full project abstract and metadata
│   ├── PHASE_STATUS.md       # Milestones and deliverables tracker
│   └── Abstract.docx         # Project abstract submission document
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore rules (protects credentials & cache)
└── README.md                 # Primary project documentation
```

---

## 🚀 Setup and Execution Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/charvikbattagiri057/KLH-ECE-2026-2027-T01-PowerCircuitAILite.git
cd KLH-ECE-2026-2027-T01-PowerCircuitAILite
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv venv

# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# On Linux/macOS:
source venv/bin/activate

# Install requirements:
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Copy the `.env.example` file to create your `.env`:
```bash
cp .env.example .env
```
Edit `.env` with your API credentials and local KiCad symbol path:
```ini
GEMINI_API_KEY=AIzaSy...your_gemini_api_key_here
SPEC_MODEL=gemini-2.5-flash
SKIDL_MODEL=gemini-2.5-flash
KICAD_SYMBOL_DIR=D:\Kicad\share\kicad\symbols
```

### 4. Run the FastAPI Backend Server
Start the backend service from the `src` directory:
```bash
uvicorn src.app.api.server:app --reload --host 0.0.0.0 --port 8000
```
Interactive Swagger documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs).

### 5. Generate a Circuit via CLI
Open a new terminal, activate your virtual environment, and run:
```bash
python src/build_circuit.py
```
**Example Interaction:**
```
⚡ Power Circuit AI-Lite Builder ⚡
-----------------------------------
What circuit do you want to build?
> Design a 12V to 5V 2A buck converter at 100kHz

⏳ Designing circuit and calculating components...
✅ SKiDL code saved to generated_circuit.py
⚙️ Running Electrical Rules Check (ERC) and exporting netlist...

ERC INFO: 0 errors found while running ERC.
🎉 Success! Your KiCad .net file is ready in the project folder.
```

---

## 📌 Current Project Phase Status

* **Current Deliverable:** **Review 1 / Phase 2 Completed ✅**
* **Git Deliverable Tag:** [`review-1`](https://github.com/charvikbattagiri057)
* **Milestone Achievements:**
  * [x] Prompt-to-specification LLM agent with Pydantic validation.
  * [x] Chained SKiDL code generation with automatic component sizing.
  * [x] Zero-error Electrical Rules Check (ERC) execution with KiCad 8/10 symbol bindings.
  * [x] KiCad netlist (`.net`) generation for downstream PCB layout.
  * [x] Single-step interactive CLI runner.

---

## 🛡️ Contribution & Security Guidelines

1. **Authentication & Secret Safety:** Never commit `.env` or credentials. All secrets are ignored via `.gitignore`.
2. **Weekly Contributions:** Every team member commits from their verified GitHub account.
3. **Milestone Tagging:** Deliverables are tagged per review (`review-1`, `review-2`, `final`).
4. **Access Control:** The repository is configured to be accessible to faculty mentors, the Supervisor, and the Course Coordinator.
