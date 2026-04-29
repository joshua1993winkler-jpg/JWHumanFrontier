const BACKEND_URL = "https://jwhumanfrontier-production.up.railway.app";

async function queryAcademy(message, useOpenAI = false) {
  const res = await fetch(`${BACKEND_URL}/truth_chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message, use_openai: useOpenAI })
  });
  const data = await res.json();
  console.log("Truth-filtered response:", data);
  return data;
}

// Example usage in your app:
queryAcademy("Explain quantum gaps and run Rocket Engine Mode", true);