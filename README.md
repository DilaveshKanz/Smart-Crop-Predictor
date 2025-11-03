<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Smart Crop Recommendation System — README</title>
  <style>
    :root{
      --bg:#0f1724; --card:#0b1220; --muted:#94a3b8; --accent:#7dd3fc;
      --glass: rgba(255,255,255,0.03);
      --mono: ui-monospace, SFMono-Regular, Menlo, Monaco, "Roboto Mono", "Courier New", monospace;
    }
    html,body{height:100%}
    body{
      margin:0; font-family:Inter,system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial;
      background:linear-gradient(180deg,#071029 0%, #071b2d 100%); color:#e6eef6;
      -webkit-font-smoothing:antialiased; -moz-osx-font-smoothing:grayscale;
      padding:32px;
    }
    .container{max-width:900px;margin:0 auto;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)); border-radius:12px; padding:28px; box-shadow:0 10px 30px rgba(2,6,23,0.6);}
    header{display:flex;gap:18px;align-items:center}
    .logo{
      width:72px;height:72px;border-radius:10px;background:linear-gradient(135deg,var(--accent),#60a5fa);
      display:flex;align-items:center;justify-content:center;font-weight:700;color:#022; font-size:26px;
    }
    h1{margin:0;font-size:22px}
    p.lead{color:var(--muted);margin-top:6px;margin-bottom:18px}
    img.screenshot{width:100%;height:auto;border-radius:8px;border:1px solid rgba(255,255,255,0.04);margin:18px 0}
    h2{margin-top:22px;margin-bottom:10px}
    ul.features{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;padding:0;list-style:none}
    ul.features li{background:var(--glass);padding:12px;border-radius:8px;color:var(--muted);font-size:14px}
    table.tech{width:100%;border-collapse:collapse;margin-top:8px}
    table.tech th, table.tech td{padding:8px;text-align:left;border-bottom:1px solid rgba(255,255,255,0.03);color:var(--muted)}
    pre {background:#071229;border:1px solid rgba(255,255,255,0.03);padding:12px;border-radius:8px;overflow:auto;font-family:var(--mono);font-size:13px;color:#dff0ff}
    code.inline{background:rgba(255,255,255,0.02);padding:2px 6px;border-radius:6px;font-family:var(--mono);font-size:13px;color:#cfeefd}
    .note{color:var(--muted);font-size:13px;margin-top:8px}
    .btn-row{display:flex;gap:10px;margin-top:12px}
    .btn{background:linear-gradient(90deg,#0ea5e9,#60a5fa);color:#012031;padding:10px 14px;border-radius:8px;border:none;cursor:pointer;font-weight:600}
    a.link{color:var(--accent);text-decoration:none}
    footer{color:var(--muted);font-size:13px;margin-top:18px}
    @media (max-width:560px){body{padding:18px}.container{padding:18px}}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="logo">🌾</div>
      <div>
        <h1>Smart Crop Recommendation System</h1>
        <p class="lead">A machine learning–powered web app that suggests the best crop to plant based on soil & climate conditions. Built with Python, scikit-learn and Gradio.</p>
      </div>
    </header>

    <img class="screenshot" alt="App Screenshot" src="https://drive.google.com/uc?export=view&id=1mEJqQ75P2X0jQmmCB0GsUYUVeKGXQGgl" />

    <h2>✨ Key Features</h2>
    <ul class="features">
      <li>🌱 <strong>Smart Crop Suggestions</strong> — Random Forest model for accurate predictions.</li>
      <li>💡 <strong>Simple Web Interface</strong> — Built with Gradio for instant interaction.</li>
      <li>📊 <strong>Data-Driven</strong> — Uses 7 environmental parameters and 22 crop classes.</li>
      <li>⚡ <strong>Lightweight</strong> — Easy local setup, minimal dependencies.</li>
    </ul>

    <h2>🧠 Tech Stack</h2>
    <table class="tech">
      <tr><th>Category</th><th>Tools</th></tr>
      <tr><td>Language</td><td>Python 3.7+</td></tr>
      <tr><td>Libraries</td><td>pandas, scikit-learn, joblib, gradio</td></tr>
      <tr><td>Model</td><td>Random Forest Classifier</td></tr>
      <tr><td>Dataset</td><td><a class="link" href="https://www.kaggle.com/datasets/siddharthss/crop-recommendation-dataset" target="_blank" rel="noopener noreferrer">Crop Recommendation Dataset (Kaggle)</a></td></tr>
    </table>

    <h2>🚀 Getting Started</h2>
    <p class="note">Follow these steps to run the project locally. This README is intentionally limited to the steps <strong>up to launching the app</strong>.</p>

    <h3>1️⃣ Prerequisites</h3>
    <p>Make sure you have <code class="inline">Python 3.7+</code> installed. Check with:</p>
    <pre><code>python --version</code></pre>

    <h3>2️⃣ Clone the Repository</h3>
    <pre><code>git clone https://github.com/DilaveshKanz/Smart-Crop-Predictor.git
cd Smart-Crop-Predictor</code></pre>

    <h3>3️⃣ Install Dependencies</h3>
    <pre><code>pip install pandas scikit-learn joblib gradio</code></pre>

    <h3>4️⃣ Train the Model</h3>
    <p>Run the training script. This will create a saved model file (for example: <code class="inline">crop_recommendation_model.joblib</code>).</p>
    <pre><code>python train.py</code></pre>

    <h3>5️⃣ Launch the App</h3>
    <p>Start the Gradio interface:</p>
    <pre><code>python app.py</code></pre>
    <p class="note">Open the provided <code class="inline">localhost</code> URL in your browser to interact with the app.</p>

    <div class="btn-row">
      <button class="btn" onclick="copyMarkdown()">Copy HTML</button>
      <a class="btn" href="https://github.com/DilaveshKanz/Smart-Crop-Predictor" target="_blank" rel="noopener noreferrer">View on GitHub</a>
    </div>

    <footer>
      <p>Author: <strong>Dilavesh Kanz Nidooli</strong></p>
      <p class="note">Dataset reference: <a class="link" href="https://www.kaggle.com/datasets/siddharthss/crop-recommendation-dataset" target="_blank" rel="noopener noreferrer">Kaggle — Crop Recommendation Dataset</a></p>
    </footer>
  </div>

  <script>
    function copyMarkdown(){
      const html = document.documentElement.outerHTML;
      navigator.clipboard.writeText(html).then(()=>{
        alert('HTML copied to clipboard. Paste into a file and save as index.html.');
      }, (err)=>{
        alert('Unable to copy to clipboard: ' + err);
      });
    }
  </script>
</body>
</html>

