import gradio as gr
import pandas as pd
import joblib
import warnings

warnings.filterwarnings("ignore")

model_file = "RF.joblib"
try:
    model = joblib.load(model_file)
    print("Model loaded successfully")
except FileNotFoundError:
    print("Model file not found. Check if the model has been trained.")
    print("Run python train.py to train the model.")
    model = None # Set model to None so app can still load
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# --- 1. Define Validation Limits ---
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

# --- 2. Updated Prediction Function ---
def crop_predictor(N, P, K, temperature, humidity, ph, rainfall):
    
    # *** THIS IS THE FIX ***
    errors = [] # Create an empty list to hold all errors

    # --- Input Validation ---
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
    # --- End of Validation Fix ---

    if model is None:
        return "Error: Model is not loaded. Cannot make a prediction."

    try:
        input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]], columns=features)
        prediction = model.predict(input_data)
        return prediction[0].capitalize()
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return f"Error in prediction: {str(e)}"

# --- 3. Load Example Data ---
try:
    df = pd.read_csv('dataset.csv')
    eg_data = df.drop('label', axis=1).head().values.tolist()
except FileNotFoundError:
    eg_data = [
        [90, 42, 43, 20.87, 82, 6.5, 202.935536],
        [85, 58, 41, 25.45, 80.32, 5.8, 226.655426],
        [60, 55, 44, 23.25, 82.25, 6.1, 94.964286],
        [74, 35, 40, 26.28, 80.79, 5.6, 158.737500],
        [78, 42, 37, 24.7, 81.54, 6.19, 103.492857]
    ]

# --- 4. Create Gradio Interface ---
with gr.Blocks(theme='lone17/kotaemon') as demo:
    gr.Markdown("# 🌾 Smart Crop Recommendation System")
    gr.Markdown("Predict the most suitable common Indian crop to cultivate based on soil and environmental parameters using Machine Learning.")

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

    predict_btn = gr.Button("Predict Crop")
    output = gr.Textbox(label="Best Suitable Crop")

    predict_btn.click(
        fn=crop_predictor,
        inputs=[N, P, K, temperature, humidity, ph, rainfall],
        outputs=output
    )

    gr.Examples(
        examples=eg_data,
        inputs=[N, P, K, temperature, humidity, ph, rainfall]
    )

demo.launch(share=True)
