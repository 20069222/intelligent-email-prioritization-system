async function analyze() {
  const email = document.getElementById("email").value;
  const res = await fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({email})
  });
  const data = await res.json();
  document.getElementById("result").innerText = "Priority: " + data.priority;
}
