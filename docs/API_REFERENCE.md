# API Reference Documentation

The **Power Circuit AI-Lite** backend is built on **FastAPI** and provides RESTful endpoints to process circuit design prompts.

## Base URL
```
http://localhost:8000
```

---

## 1. Health Check
- **Endpoint:** `GET /`
- **Description:** Verifies that the API service is active and responsive.
- **Response:**
  ```json
  {
    "status": "Power Circuit AI-Lite API is running"
  }
  ```

---

## 2. Extract Specifications
- **Endpoint:** `POST /api/v1/generate-spec`
- **Description:** Extracts structured converter parameters (Vin, Vout, Iout, fsw, mode) from a natural language prompt using the `SpecAgent`.
- **Request Body:**
  ```json
  {
    "user_prompt": "I need a buck converter stepping down 12V to 3.3V with 1.5A load at 200kHz CCM"
  }
  ```
- **Response:**
  ```json
  {
    "status": "success",
    "received_prompt": "I need a buck converter stepping down 12V to 3.3V with 1.5A load at 200kHz CCM",
    "spec": {
      "topology": "buck_converter",
      "vin_min": 12.0,
      "vin_max": 12.0,
      "vout": 3.3,
      "iout_max": 1.5,
      "fsw": 200000.0,
      "mode": "CCM"
    }
  }
  ```

---

## 3. End-to-End Circuit Synthesis
- **Endpoint:** `POST /api/v1/generate-circuit`
- **Description:** Executes the full pipeline: extracts specifications and invokes the `SKiDL synthesis agent` to return executable Python code containing net declarations, pin wiring, ERC checks, and netlist export.
- **Request Body:**
  ```json
  {
    "user_prompt": "Design a 24V to 5V 3A buck converter running at 150kHz"
  }
  ```
- **Response:**
  ```json
  {
    "status": "success",
    "received_prompt": "Design a 24V to 5V 3A buck converter running at 150kHz",
    "spec": {
      "topology": "buck_converter",
      "vin_min": 24.0,
      "vin_max": 24.0,
      "vout": 5.0,
      "iout_max": 3.0,
      "fsw": 150000.0,
      "mode": "CCM"
    },
    "skidl_code": "import os\n# SKiDL circuit definition code...\nERC()\ngenerate_netlist(file_='circuit.net')"
  }
  ```
