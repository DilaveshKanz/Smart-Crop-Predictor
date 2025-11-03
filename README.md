# 🌾 Smart Crop Recommendation System

A simple web app that suggests the best crop to plant based on soil and climate conditions.

This project was built to demonstrate practical machine learning skills. It takes **real-world** agricultural data and turns it into a useful tool for farmers.

![App Screenshot](screenshot/app_screenshot.png)

---

## ✨ Features

* **Smart Suggestions:** Uses a high-accuracy **Random Forest** model to predict the best crop.
* **Simple Interface:** A clean web dashboard built with **Gradio** lets you enter values and get an instant prediction.
* **Data-Driven:** Trained on a public dataset of 7 environmental factors - 2200 data points covering 22 different crops.

---

## 🛠️ How to Get it Running

Here’s how you can run this project on your own computer.

### 1. Prerequisites

* You'll need **Python 3.7** or newer.

### 2. Install the Dependencies

First, get the code (you can download it as a ZIP or use `git clone https://github.com/DilaveshKanz/Smart-Crop-Predictor`). Then, in your project folder, install the required libraries using `pip`:

```bash
pip install pandas scikit-learn joblib gradio

```bash
python train.py

```bash
python app.py
