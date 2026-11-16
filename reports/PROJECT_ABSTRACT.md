# Project Abstract

## Power Circuit AI-Lite: An LLM-Driven Pipeline for Automated Netlist Generation of DC-DC Power Converters

Designing a power electronic converter is still a largely manual process. Engineers calculate component values from the performance requirements, then transcribe the circuit into schematic form by hand, which is slow and prone to error. Each change to a specification, such as the input voltage, load current or switching frequency, means repeating the calculations and redrawing the circuit. This project presents **Power Circuit AI-Lite**, an automated pipeline that turns a plain-language requirement into a validated circuit description for DC-DC converters, covering buck and boost topologies.

The system uses a **FastAPI backend** that passes the user's requirements to **Google Gemini**, which extracts a structured specification of input and output voltage, load current and switching frequency. Component values are computed with analytical design equations, so the language model never performs the arithmetic itself. From these values the pipeline generates Python-based **SKiDL** code and runs programmatic **Electrical Rules Checks (ERC)** to detect connectivity and rule violations. It then exports a **KiCad-compatible netlist (`.net`)** for subsequent PCB layout. 

A command-line interface takes a designer from a text prompt to a netlist file in a single step. The approach is expected to shorten early-stage prototyping time and reduce manual calculation errors, since each generated design passes automated ERC validation before it reaches layout tools.

---

### Keywords
`power electronics`, `large language models`, `SKiDL`, `KiCad`, `electrical rules check`, `DC-DC converters`

---

### Project Metadata
- **Institution:** KL Deemed to be University (KLH)
- **Department:** Electronics and Communication Engineering (ECE)
- **Academic Year:** 2026-2027
- **Course:** Generative AI & AI Platform Engineering (`25CS2207E`)
- **Course Coordinator:** DHARAMSOTU BHEEKYA
