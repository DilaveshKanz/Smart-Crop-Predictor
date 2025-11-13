import gradio as gr
import pandas as pd
import joblib
import warnings
import os

warnings.filterwarnings("ignore")

# --- 1. Load Model ---
model_file = "RF.joblib"
try:
    model = joblib.load(model_file)
    print("Model loaded successfully")
except FileNotFoundError:
    print("Error: Model file not found. Check if the model has been trained.")
    print("Run 'python train.py' to train the model.")
    model = None 
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# --- 2. Define Validation Limits ---
MAX_N = 100
MAX_P = 100
MAX_K = 100
MAX_RAINFALL = 300
MAX_PH = 14
MAX_HUMIDITY = 100
MAX_TEMP = 50

MIN_N = 0
MIN_P = 0
MIN_K = 0
MIN_RAINFALL = 0
MIN_PH = 0
MIN_HUMIDITY = 10
MIN_TEMP = 5

features = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

# --- 3. Prediction Function (with Validation) ---
def crop_predictor(N, P, K, temperature, humidity, ph, rainfall):
    
    errors = [] # Create an empty list to hold all errors

    # Input Validation
    if not (MIN_N <= N <= MAX_N):
        errors.append(f"Nitrogen (N) must be between {MIN_N} and {MAX_N}.")
    if not (MIN_P <= P <= MAX_P):
        errors.append(f"Phosphorus (P) must be between {MIN_P} and {MAX_P}.")
    if not (MIN_K <= K <= MAX_K):
        errors.append(f"Potassium (K) must be between {MIN_K} and {MAX_K}.")
    if not (MIN_RAINFALL <= rainfall <= MAX_RAINFALL):
        errors.append(f"Rainfall must be between {MIN_RAINFALL} and {MAX_RAINFALL} mm.")
    if not (MIN_TEMP <= temperature <= MAX_TEMP):
        errors.append(f"Temperature must be between {MIN_TEMP} and {MAX_TEMP}°C.")
    if not (MIN_HUMIDITY <= humidity <= MAX_HUMIDITY):
        errors.append(f"Humidity must be between {MIN_HUMIDITY} and {MAX_HUMIDITY}%.")
    if not (MIN_PH <= ph <= MAX_PH):
        errors.append(f"pH must be between {MIN_PH} and {MAX_PH}.")

    # If the errors list is NOT empty, join all error messages and return them.
    if errors:
        return "\n".join(errors)
    
    if model is None:
        return "Error: Model is not loaded. Cannot make a prediction."

    try:
        input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]], columns=features)
        prediction = model.predict(input_data)
        return prediction[0].capitalize()
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return f"Error in prediction: {str(e)}"

# --- 4. Load Example Data ---
example_list = []
try:
    df = pd.read_csv('Crop_recommendation.csv')
    example_list = df.drop('label', axis=1).head().values.tolist()
    print("Example data loaded from CSV.")
except FileNotFoundError:
    print("Warning: 'Crop_recommendation.csv' not found. Using fallback examples.")
    example_list = [
        [90, 42, 43, 20.87, 82, 6.5, 202.93],
        [85, 58, 41, 21.77, 80.32, 5.8, 226.65],
    ]

# --- 5. Create Gradio Interface ---
print("Creating Gradio interface...")
with gr.Blocks(theme=gr.themes.Monochrome()) as app:
    
    gr.HTML(
        """
        <div style="text-align: center; max-width: 800px; margin: 0 auto;">
            <h1 style="font-size: 2.5em; font-weight: 600;">🌾 Smart Crop Recommendation System</h1>
            <p style="font-size: 1.1em; color: #555;">
                Predict the ideal crop to grow based on soil and environmental conditions.
            </p>
        </div>
        """
    )
    
    with gr.Row(variant="panel"):
        # Column 1: Inputs
        with gr.Column(scale=2):
            gr.Markdown("### 1. Enter Soil & Climate Data")
            with gr.Row():
                N = gr.Number(label="Nitrogen (N) in soil", value=90)
                P = gr.Number(label="Phosphorus (P) in soil", value=42)
                K = gr.Number(label="Potassium (K) in soil", value=43)
            with gr.Row():
                temperature = gr.Slider(minimum=MIN_TEMP, maximum=MAX_TEMP, label="Temperature (°C)", value=30)
                humidity = gr.Slider(minimum=MIN_HUMIDITY, maximum=MAX_HUMIDITY, label="Humidity (%)", value=80)
            with gr.Row():
                ph = gr.Slider(minimum=MIN_PH, maximum=MAX_PH, label="pH value of the soil", value=7)
                rainfall = gr.Number(label="Rainfall (mm)", value=200)
            
            predict_btn = gr.Button("Predict Crop", variant="primary")

        # Column 2: Outputs
        with gr.Column(scale=1):
            gr.Markdown("### 2. View Recommendation")
            output_text = gr.Textbox(
                label="Recommended Crop",
                scale=2
            )

    if example_list:
        gr.Examples(
            examples=example_list,
            inputs=[N, P, K, temperature, humidity, ph, rainfall],
            outputs=output_text,
            fn=crop_predictor,
            cache_examples=True
        )

    predict_btn.click(
        fn=crop_predictor,
        inputs=[N, P, K, temperature, humidity, ph, rainfall],
        outputs=output_text
    )

# --- 6. Launch the App ---
print("Launching Gradio app...")
app.launch(share=True)
