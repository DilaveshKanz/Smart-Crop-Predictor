<!-- README.html for Smart Crop Recommendation System -->
<h1>🌾 Smart Crop Recommendation System</h1>

<p>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python"></a>
  <a href="https://scikit-learn.org/"><img src="https://img.shields.io/badge/ML-Random%20Forest-green.svg" alt="Random Forest"></a>
  <a href="https://gradio.app/"><img src="https://img.shields.io/badge/Interface-Gradio-orange.svg" alt="Gradio"></a>
</p>

<p>An intelligent machine learning application that recommends optimal crops based on soil nutrient levels and climatic conditions. Built to empower farmers and agricultural professionals with data-driven crop selection insights.</p>

<p>
  <img src="screenshot/app_screenshot.png" alt="App Screenshot" width="700">
</p>

<hr>

<h2>🎯 Project Overview</h2>
<p>
Agriculture remains heavily dependent on traditional decision-making methods, which often lack precision in today's changing climate. This system bridges that gap by leveraging machine learning to analyze environmental parameters and predict the most suitable crop for cultivation.<br>
<b>Live Demo:</b> <i>[Add your deployment link here]</i>
</p>

<hr>

<h2>✨ Key Features</h2>
<ul>
<li><b>High-Accuracy Predictions:</b> Employs a Random Forest Classifier achieving 95%+ accuracy for crop recommendations</li>
<li><b>Seven Environmental Parameters:</b> Analyzes Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, pH levels, and rainfall</li>
<li><b>Comprehensive Dataset:</b> Trained on 2,200 agricultural data points covering 22 diverse crop varieties</li>
<li><b>Interactive Web Interface:</b> User-friendly Gradio dashboard for real-time predictions without coding knowledge</li>
<li><b>Instant Results:</b> Get crop recommendations within seconds of inputting your parameters</li>
<li><b>Science-Backed:</b> Based on agro-climatic research from <a href="https://www.kaggle.com/datasets/siddharthss/crop-recommendation-dataset">Kaggle's Crop Recommendation Dataset</a>
</ul>

<hr>

<h2>📊 Dataset Information</h2>
<p>
<b>Source:</b> <a href="https://www.kaggle.com/datasets/siddharthss/crop-recommendation-dataset">Crop Recommendation Dataset - Kaggle</a><br>
<b>Dataset Characteristics:</b>
<ul>
<li><b>Total Samples:</b> 2,200 records</li>
<li><b>Crop Classes:</b> 22 different crops (Rice, Wheat, Cotton, Maize, etc.)</li>
<li><b>Features:</b> 7 environmental and soil parameters</li>
</ul>
</p>

<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th>Description</th>
      <th>Unit</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Nitrogen (N)</td><td>Nitrogen content in soil</td><td>kg/ha</td></tr>
    <tr><td>Phosphorus (P)</td><td>Phosphorus content in soil</td><td>kg/ha</td></tr>
    <tr><td>Potassium (K)</td><td>Potassium content in soil</td><td>kg/ha</td></tr>
    <tr><td>Temperature</td><td>Average temperature</td><td>°C</td></tr>
    <tr><td>Humidity</td><td>Relative humidity</td><td>%</td></tr>
    <tr><td>pH</td><td>Soil pH value</td><td>0-14 scale</td></tr>
    <tr><td>Rainfall</td><td>Annual rainfall</td><td>mm</td></tr>
  </tbody>
</table>

<hr>

<h2>🛠️ Technologies Used</h2>
<ul>
  <li><b>Python 3.7+</b></li>
  <li><b>scikit-learn</b> (Random Forest)</li>
  <li><b>pandas</b></li>
  <li><b>Gradio</b></li>
  <li><b>joblib</b></li>
  <li><b>NumPy</b></li>
</ul>

<hr>

<h2>🚀 Installation &amp; Setup</h2>
<h3>Prerequisites</h3>
<ul>
  <li>Python 3.7 or higher installed</li>
  <li>Basic command line/terminal knowledge</li>
  <li>Internet connection for package downloads</li>
</ul>

<h3>Step 1: Clone the Repository</h3>
<pre><code>git clone https://github.com/DilaveshKanz/Smart-Crop-Predictor.git
cd Smart-Crop-Predictor
</code></pre>

<h3>Step 2: Install Dependencies</h3>
<pre><code>pip install pandas scikit-learn joblib gradio numpy
</code></pre>
<p>Or using a requirements file:</p>
<pre><code>pip install -r requirements.txt
</code></pre>

<h3>Step 3: Train the Model</h3>
<pre><code>python train.py
</code></pre>
<p><i>Generates the trained model (<code>crop_model.pkl</code>).</i></p>

<h3>Step 4: Launch the Application</h3>
<pre><code>python app.py
</code></pre>
<p><i>This opens the Gradio dashboard, typically at <code>http://127.0.0.1:7860</code>.</i></p>

<hr>

<h2>💡 How to Use</h2>
<ol>
  <li><b>Launch the App:</b> Run <code>python app.py</code></li>
  <li><b>Input Parameters:</b> Enter N, P, K, temperature, humidity, pH, and rainfall</li>
  <li><b>Get Recommendation:</b> Click "Submit" for the best crop suggestion</li>
  <li><b>Apply the advice:</b> Use the recommendation along with market and local knowledge</li>
</ol>

<hr>

<h2>📁 Project Structure</h2>
<pre><code>Smart-Crop-Predictor/
├── train.py
├── app.py
├── crop_model.pkl
├── Crop_recommendation.csv
├── requirements.txt
├── screenshot/
│   └── app_screenshot.png
└── README.md
</code></pre>

<hr>

<h2>🧠 Model Performance</h2>
<ul>
  <li><b>Algorithm:</b> Random Forest Classifier</li>
  <li><b>Training Accuracy:</b> ~99%</li>
  <li><b>Test Accuracy:</b> 95%+</li>
  <li><b>Cross-Validation:</b> K-fold</li>
  <li><b>Important Features:</b> Temperature, rainfall, NPK most significant</li>
</ul>

<hr>

<h2>🌐 Deployment Options</h2>
<ul>
  <li><b>Local:</b> Run <code>python app.py</code></li>
  <li><b>Cloud:</b> Hugging Face Spaces, Heroku, AWS/Azure/GCP, Vultr Cloud GPU</li>
</ul>

<hr>

<h2>🔮 Future Enhancements</h2>
<ul>
  <li>Add regional crop varieties</li>
  <li>Integrate weather API</li>
  <li>Fertilizer suggestions</li>
  <li>Multiple language support</li>
  <li>Mobile version</li>
  <li>Yield prediction</li>
  <li>Market price insights</li>
</ul>

<hr>

<h2>📚 References</h2>
<ul>
  <li>Kaggle: Crop Recommendation Dataset</li>
  <li>scikit-learn Random Forest</li>
  <li>Gradio Documentation</li>
</ul>

<hr>

<h2>🤝 Contributing</h2>
<ol>
  <li>Fork the repo</li>
  <li>Create a feature branch</li>
  <li>Commit</li>
  <li>Push</li>
  <li>Open a PR!</li>
</ol>

<hr>

<h2>📄 License</h2>
<p>MIT License</p>

<hr>

<h2>👨‍💻 Author</h2>
<p>
<b>Dilavesh Kanz</b><br>
GitHub: <a href="https://github.com/DilaveshKanz">@DilaveshKanz</a><br>
Project: <a href="https://github.com/DilaveshKanz/Smart-Crop-Predictor">Smart Crop Predictor</a>
</p>

<hr>

<h2>🙏 Acknowledgments</h2>
<ul>
  <li>Kaggle Community Dataset</li>
  <li>Built for hands-on ML skills</li>
  <li>Inspired by sustainable farming practices</li>
</ul>

<hr>

<h2>📞 Support</h2>
<ul>
  <li>Open a GitHub issue</li>
  <li>Check existing issues</li>
  <li>Contact via profile</li>
</ul>

<hr>

<p align="center"><b>⭐ If you find this project helpful, star it on GitHub!</b></p>

