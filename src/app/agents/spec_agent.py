import os
import json
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

load_dotenv()

class CircuitSpec(BaseModel):
    topology: str = Field(description="The type of circuit, e.g., 'buck_converter'")
    vin_min: float = Field(description="Minimum input voltage in Volts")
    vin_max: float = Field(description="Maximum input voltage in Volts")
    vout: float = Field(description="Target output voltage in Volts")
    iout_max: float = Field(description="Maximum output current in Amps")
    fsw: float = Field(description="Switching frequency in Hz")
    mode: str = Field(description="Operating mode, e.g., 'CCM' or 'DCM'")

def parse_user_request(user_prompt: str) -> dict:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set in the environment.")

    client = genai.Client(api_key=api_key)
    
    system_instruction = """
    You are an expert power electronics engineer. 
    Extract the specifications from the user's prompt into the requested JSON schema.
    If a switching frequency (fsw) is not provided, default to 100000 (100kHz).
    If a mode is not provided, default to 'CCM'.
    """
    
    # Use gemini-3.5-flash which is active and available for this API key
    model_name = os.environ.get("SPEC_MODEL", "gemini-3.5-flash")
    
    response = client.models.generate_content(
        model=model_name,
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            response_mime_type="application/json",
            response_schema=CircuitSpec,
            temperature=0.1
        ),
    )
    
    return json.loads(response.text)
