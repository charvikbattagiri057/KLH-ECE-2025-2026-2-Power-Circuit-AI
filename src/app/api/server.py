from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

from app.agents.spec_agent import parse_user_request
from app.agents.skidl_agent import generate_skidl_code

# Load environment variables from .env
load_dotenv()

app = FastAPI(
    title="Power Circuit AI-Lite",
    description="FastAPI backend for natural language power circuit specification parsing and SKiDL schematic code generation",
    version="0.2"
)

class CircuitRequest(BaseModel):
    user_prompt: str

@app.get("/")
def read_root():
    return {"status": "Power Circuit AI-Lite API is running"}

@app.post("/api/v1/generate-spec")
def generate_spec(request: CircuitRequest):
    """
    Phase 1 endpoint: Extract circuit specifications from natural language prompt.
    """
    try:
        parsed_spec = parse_user_request(request.user_prompt)
        return {
            "status": "success",
            "received_prompt": request.user_prompt,
            "spec": parsed_spec
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

@app.post("/api/v1/generate-circuit")
def generate_circuit(request: CircuitRequest):
    """
    Phase 2 endpoint: Chained pipeline that parses specs from the prompt
    and generates complete Python SKiDL code to model the circuit schematic.
    """
    try:
        # Step 1: Parse user prompt into circuit specifications
        parsed_spec = parse_user_request(request.user_prompt)
        
        # Step 2: Generate SKiDL code from the parsed specification
        skidl_code = generate_skidl_code(parsed_spec)
        
        return {
            "status": "success",
            "received_prompt": request.user_prompt,
            "spec": parsed_spec,
            "skidl_code": skidl_code
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
