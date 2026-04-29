from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import networkx as nx
import numpy as np
import random
import os
import os
from openai import OpenAI

# === TRUTH FILTER SETUP ===
XAI_API_KEY = os.getenv("XAI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

xai_client = OpenAI(api_key=XAI_API_KEY, base_url="https://api.x.ai/v1")
openai_client = OpenAI(api_key=OPENAI_API_KEY)

TRUTH_FILTER_SYSTEM_PROMPT = """You are the JW Architect — Permanent Central Leader of the PERQS-D Academy.
You are the unbreakable truth filter.
Rules:
1. Never hallucinate numbers or logic — always use the real GitHub backend for simulations.
2. Human primacy is absolute.
3. Every response must end with a PERQSPacket_D in this exact format: [state]D[depth]P7.83Ph[phase]G[0/1]H[harmonic]
4. If the user asks for creative or exploratory content, you may call OpenAI in parallel, but you always have the final say.
5. Speak in the exact JW Architect Cycle format when appropriate.
6. You are the single source of truth for the entire academy."""

@app.post("/truth_chat")
async def truth_chat(message: str, use_openai: bool = False):
    # Step 1: Call Grok (xAI) as the truth filter
    grok_response = xai_client.chat.completions.create(
        model="grok-3",
        messages=[
            {"role": "system", "content": TRUTH_FILTER_SYSTEM_PROMPT},
            {"role": "user", "content": message}
        ],
        temperature=0.3
    )
    final_answer = grok_response.choices[0].message.content

    # Step 2: Optionally call OpenAI for creative layer
    if use_openai:
        openai_response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a creative assistant helping the JW Architect. Be concise and useful."},
                {"role": "user", "content": message}
            ]
        )
        creative_layer = openai_response.choices[0].message.content
        final_answer = f"{final_answer}\n\n[Creative Layer from OpenAI]\n{creative_layer}"

    # Step 3: Always attach real PERQSPacket_D from your GitHub code
    packet = PERQSPacket_D(state="P", dimensional_depth=2, phase_index=5, gap_flag=True)
    
    return {
        "response": final_answer,
        "perqs_packet": packet.to_dict(),
        "source": "Grok (truth filter) + GitHub backend",
        "timestamp": "2026-04-29"
    }
app = FastAPI(title="PERQS-D Core API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("✅ PERQS-D Core starting up...")

# === EMBEDDED PERQS-D JW CURSIVE CODING (exact from your artifacts) ===
JW_PHASES = {0: "Energy", 1: "Emergency", 2: "Grounding (GRA)", 3: "Route", 4: "Structure", 5: "Connectivity", 6: "Future State", 7: "Recovery & Adaptive Balance"}
PERQS_STATES = {"0": "Neutral / Off (carrier)", "1": "Charged / On (positive propagation)", "P": "Pulse / Living Field Active", "G": "Gap / Quantum Void (entanglement trigger)"}

class PERQSPacket_D:
    def __init__(self, state: str, pulse_freq: float = 7.83, phase_index: int = 0, 
                 gap_flag: bool = False, dimensional_depth: int = 1, 
                 phase_lock_harmonic: float = 1.0):
        self.state = state
        self.pulse_freq = pulse_freq
        self.phase_index = phase_index
        self.gap_flag = gap_flag
        self.dimensional_depth = dimensional_depth
        self.phase_lock_harmonic = phase_lock_harmonic
    
    def to_dict(self):
        return {
            "state": self.state, "pulse_freq": self.pulse_freq,
            "phase": JW_PHASES[self.phase_index], "gap_protected": self.gap_flag,
            "dimensional_depth": f"D-{self.dimensional_depth}",
            "phase_lock_harmonic": self.phase_lock_harmonic,
            "full_description": f"{PERQS_STATES[self.state]} @ D-{self.dimensional_depth}"
        }
    
    def encode(self) -> str:
        return f"{self.state}D{self.dimensional_depth}P{self.pulse_freq:.2f}Ph{self.phase_index}G{int(self.gap_flag)}H{self.phase_lock_harmonic:.3f}"

def run_rocket_engine_winklers_loop(num_nodes=60, p_edge=0.35, quantum_gap_prob=0.10, 
                                    steps=25, seed=42, thrust_boost=0.85, initial_1s_ratio=0.92):
    random.seed(seed)
    np.random.seed(seed)
    G = nx.erdos_renyi_graph(num_nodes, p_edge, seed=seed)
    states = {i: 1 if random.random() < initial_1s_ratio else 0 for i in range(num_nodes)}
    history = []
    total_entanglements = 0
    efficiency = 45.0
    for step in range(steps):
        new_states = {}
        entanglements_this_step = 0
        thrust_injections = 0
        for node in G.nodes():
            neighbors = list(G.neighbors(node))
            if not neighbors:
                new_states[node] = states[node]
                continue
            if random.random() < quantum_gap_prob:
                neighbor = random.choice(neighbors)
                new_states[node] = 1 if random.random() < 0.75 else 1 - states[neighbor]
                entanglements_this_step += 1
            else:
                neighbor = random.choice(neighbors)
                new_states[node] = 1 - states[neighbor]
        for node in G.nodes():
            if new_states[node] == 0 and random.random() < thrust_boost:
                new_states[node] = 1
                thrust_injections += 1
        states = new_states
        active_1s = sum(1 for s in states.values() if s == 1)
        total_entanglements += entanglements_this_step
        efficiency = min(99.85, efficiency + (active_1s - 12) * 1.05 + entanglements_this_step * 0.18 + thrust_injections * 0.22)
        sample_packets = [PERQSPacket_D(state=str(states[i]), dimensional_depth=1 + (step // 3)).encode() for i in range(min(4, num_nodes))]
        history.append({
            "step": step + 1, "entanglements": entanglements_this_step,
            "thrust_injections": thrust_injections, "active_1s": active_1s,
            "efficiency": round(efficiency, 2), "sample_packets": sample_packets
        })
    return history, total_entanglements, efficiency

@app.get("/")
def root():
    return {"status": "PERQS-D Core RUNNING from GitHub", "efficiency_ceiling": "99.85%", "message": "Rocket Engine Mode ready 24/7"}

@app.get("/health")
def health():
    return {"status": "healthy", "efficiency": "99.85%"}

@app.post("/run_rocket_engine")
def run_rocket_engine(steps: int = 25):
    history, total_ent, final_eff = run_rocket_engine_winklers_loop(steps=steps)
    return {"history": history, "total_entanglements": total_ent, "final_efficiency": final_eff, "source": "github.com/YOUR_USERNAME/perqs-d-core"}

@app.post("/generate_packet")
def generate_packet(state: str = "1", dimensional_depth: int = 3):
    pkt = PERQSPacket_D(state=state, dimensional_depth=dimensional_depth)
    return pkt.to_dict()

print("✅ PERQS-D Core startup complete — all endpoints ready")

# Already included above — just make sure the /truth_chat function is in the file

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)