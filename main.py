# main.py — Deploy this on Railway / Render / Fly.io
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import importlib.util
import sys
from pathlib import Path

app = FastAPI(title="PERQS-D Core API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend URL later for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === LOAD YOUR EXACT CODE FROM GITHUB (this is the magic) ===
def load_from_github():
    url = "https://raw.githubusercontent.com/YOUR_USERNAME/perqs-d-core/main/rocket_engine_winklers_loop.py"
    response = requests.get(url)
    with open("/tmp/rocket_engine.py", "w") as f:
        f.write(response.text)
    
    spec = importlib.util.spec_from_file_location("rocket_engine", "/tmp/rocket_engine.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules["rocket_engine"] = module
    spec.loader.exec_module(module)
    return module

rocket = load_from_github()

@app.get("/")
def root():
    return {"status": "PERQS-D Core running from GitHub", "efficiency_ceiling": "99.85%"}

@app.post("/run_rocket_engine")
def run_rocket_engine(steps: int = 25):
    history, total_ent, final_eff = rocket.run_rocket_engine_winklers_loop(steps=steps)
    return {
        "history": history,
        "total_entanglements": total_ent,
        "final_efficiency": final_eff,
        "source": "github.com/YOUR_USERNAME/perqs-d-core"
    }

@app.post("/generate_packet")
def generate_packet(state: str = "1", dimensional_depth: int = 3):
    pkt = rocket.PERQSPacket_D(state=state, dimensional_depth=dimensional_depth)
    return pkt.to_dict()

# Add more endpoints as needed (daily_pulse, process_emergency, etc.)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)