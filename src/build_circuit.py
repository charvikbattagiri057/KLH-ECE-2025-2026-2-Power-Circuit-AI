import requests
import subprocess
import sys

# Your local FastAPI endpoint
API_URL = "http://localhost:8000/api/v1/generate-circuit"
OUTPUT_FILE = "generated_circuit.py"

def main():
    print("\n⚡ Power Circuit AI-Lite Builder ⚡")
    print("-" * 35)
    
    user_prompt = input("What circuit do you want to build?\n> ")
    if not user_prompt.strip():
        print("Prompt empty. Exiting.")
        return

    print("\n⏳ Designing circuit and calculating components... (This may take 5-10 seconds)")
    
    try:
        response = requests.post(API_URL, json={"user_prompt": user_prompt})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection error: {e}")
        print("Ensure your FastAPI server is running in another terminal window!")
        return

    data = response.json()
    
    if data.get("status") != "success" or "skidl_code" not in data:
        print("❌ API Error:", data)
        return
        
    skidl_code = data["skidl_code"]
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(skidl_code)
        
    print(f"✅ SKiDL code saved to {OUTPUT_FILE}")
    print(f"⚙️  Running Electrical Rules Check (ERC) and exporting netlist...\n")
    
    try:
        subprocess.run([sys.executable, OUTPUT_FILE], check=True, text=True)
        print("\n🎉 Success! Your KiCad .net file is ready in the project folder.")
    except subprocess.CalledProcessError:
        print("\n❌ SKiDL flagged some ERC errors (see terminal output above).")

if __name__ == "__main__":
    main()
