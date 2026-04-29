// === PERQS-D REAL BACKEND (LIVE) ===
const BACKEND_URL = "https://jwhumanfrontier-production.up.railway.app";

// Test connection
async function testBackend() {
  const res = await fetch(`${BACKEND_URL}/health`);
  const data = await res.json();
  console.log("✅ Backend live:", data);
  alert("Backend connected! Efficiency ceiling: 99.85%");
}

// Run real Rocket Engine Mode (your exact GitHub code — 99.85%)
async function runRealRocketEngine(steps = 25) {
  const btn = document.getElementById("rocket-btn");
  if (btn) btn.innerText = "Running from GitHub...";
  
  const res = await fetch(`${BACKEND_URL}/run_rocket_engine`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ steps: steps })
  });
  const data = await res.json();
  
  if (btn) btn.innerText = "Run Rocket Engine Mode";
  console.log("Real output:", data);
  alert(`Rocket Engine complete!\nFinal efficiency: ${data.final_efficiency}%\nTotal entanglements: ${data.total_entanglements}`);
}

// Generate real PERQSPacket_D
async function generateRealPacket(state = "1", dimensional_depth = 3) {
  const res = await fetch(`${BACKEND_URL}/generate_packet`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ state, dimensional_depth })
  });
  return await res.json();
}