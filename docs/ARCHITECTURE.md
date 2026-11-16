# System Architecture & Pipeline Design

**Power Circuit AI-Lite** implements an automated, multi-stage LLM-driven synthesis pipeline designed to convert unstructured human requirements into valid electrical netlists without hallucinating arithmetic or topology connections.

## Pipeline Architecture

```
+-----------------------------------------------------------+
|                     Natural Language User                 |
|            "Design a 12V to 5V 2A buck converter"          |
+-----------------------------------------------------------+
                              |
                              v
+-----------------------------------------------------------+
|                   Phase 1: Spec Agent                     |
|           (LLM Structured Parameter Extraction)           |
|        Input: Freeform Natural Language Query             |
|        Output: Validated CircuitSpec (Pydantic / JSON)    |
+-----------------------------------------------------------+
                              |
                              v
+-----------------------------------------------------------+
|               Phase 2: SKiDL Synthesis Agent             |
|        Input: Structured Converter Specifications         |
|        - Computes component parameters (L, C, R)          |
|        - Maps KiCad Device Symbols & Footprints           |
|        - Defines Nets, Power Drives, and Connections      |
|        Output: Executable Python SKiDL Script             |
+-----------------------------------------------------------+
                              |
                              v
+-----------------------------------------------------------+
|              Phase 3: Validation & Compilation            |
|        - Programmatic Electrical Rules Check (ERC)        |
|        - KiCad-Compatible Netlist Export (.net)           |
|        - Schematic Preview (Schemdraw)                    |
+-----------------------------------------------------------+
```

## Architectural Highlights

1. **Separation of Reasoning and Arithmetic:**
   - LLMs are prone to arithmetic errors when performing floating-point circuit equations.
   - The Spec Agent handles linguistic extraction and semantic parsing.
   - Sizing calculations use deterministic formulas inside the Python SKiDL domain logic.

2. **Automated Electrical Rules Check (ERC):**
   - SKiDL performs automated verification to ensure that every net is properly driven and no floating inputs or forbidden pin conflicts exist.
   - Critical power rails (`VIN`, `GND`, `GATE`) are designated with `.drive = POWER` to satisfy ERC assertions.

3. **Interoperability with EDA Tools:**
   - The final output is a KiCad `.net` netlist that can be directly imported into KiCad PCB Editor (`pcbnew`) for trace routing and manufacturing preparation.
