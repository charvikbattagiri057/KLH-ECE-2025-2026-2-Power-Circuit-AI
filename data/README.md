# Data and Component Knowledge Base

This directory documents the data sources, schemas, and component library references used by **Power Circuit AI-Lite**.

## 1. Specification Schema (`/data/spec_schemas/`)
- `buck_spec_schema.json`: Strict JSON schema used by the `SpecAgent` to validate extracted converter parameters from natural language inputs before downstream synthesis.
  - Parameters captured:
    - `topology`: Circuit topology (e.g., `buck_converter`, `boost_converter`).
    - `vin_min`: Minimum input voltage (V).
    - `vin_max`: Maximum input voltage (V).
    - `vout`: Regulated target output voltage (V).
    - `iout_max`: Maximum rated output load current (A).
    - `fsw`: Switching frequency in Hz (defaults to 100 kHz).
    - `mode`: Inductor conduction mode (`CCM` - Continuous Conduction Mode or `DCM` - Discontinuous Conduction Mode).

## 2. Component and Footprint Mappings (`/data/components/`)
- `component_footprints.json`: Standardized KiCad component library and PCB footprint tables.
- Standard libraries referenced:
  - **KiCad 8.x / 10.x Official Symbol Libraries** (`Device.kicad_sym`, `power.kicad_sym`, `Connector.kicad_sym`).
  - Standard SMD package footprints (`TO-252-2` DPAK, `D_SMA`, `Inductor_SMD:L_12x12mm`, `C_1206_3216Metric`, `R_0805_2012Metric`).

## 3. Analytical Design Formulations
Component values are not guessed by the LLM. Instead, standard power electronics design equations are applied:
- **Duty Cycle ($D$):**
  $$D = \frac{V_{out}}{V_{in}}$$
- **Filter Inductor ($L$):**
  $$L = \frac{V_{in} - V_{out}}{\Delta I_L \cdot f_{sw}} \cdot D$$
  *(where ripple current $\Delta I_L \approx 0.3 \cdot I_{out}$)*
- **Output Capacitor ($C$):**
  $$C = \frac{\Delta I_L}{8 \cdot f_{sw} \cdot \Delta V_{out}}$$
- **Equivalent Load Resistance ($R_{load}$):**
  $$R_{load} = \frac{V_{out}}{I_{out}}$$
