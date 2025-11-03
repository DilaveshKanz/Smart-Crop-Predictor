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
    exit()

features = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

def crop_predictor(N, P, K, temperature, humidity, ph, rainfall):
    try:
        input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]], columns=features)
        prediction = model.predict(input_data)
        return prediction[0].capitalize()
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return f"Error in prediction: {str(e)}"

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

with gr.Blocks(theme='lone17/kotaemon') as demo:
    gr.Markdown("# 🌾 Smart Crop Recommendation System")
    gr.Markdown("Predict the most suitable common Indian crop to cultivate based on soil and environmental parameters using Machine Learning.")

    with gr.Row():
        N = gr.Number(label="Nitrogen (N) in soil", value=90)
        P = gr.Number(label="Phosphorus (P) in soil", value=42)
        K = gr.Number(label="Potassium (K) in soil", value=43)

    with gr.Row():
        temperature = gr.Slider(minimum=0, maximum=50, label="Temperature (°C)", value=30)
        humidity = gr.Slider(minimum=0, maximum=100, label="Humidity (%)", value=80)

    with gr.Row():
        ph = gr.Slider(minimum=0, maximum=14, label="pH value of the soil", value=7)
        rainfall = gr.Number(label="Rainfall (mm)", value=1000)

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
