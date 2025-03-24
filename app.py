from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import joblib
import numpy as np
import os
import json

app = Flask(__name__)

# Cargar el modelo y los escaladores
try:
    model_path = os.path.join(app.root_path, 'modelos', 'modelo_baleares61R2.h5')
    scaler_X_path = os.path.join(app.root_path, 'modelos', 'scaler_X.pkl')
    scaler_y_path = os.path.join(app.root_path, 'modelos', 'scaler_y.pkl')

    print(f"Intentando cargar el modelo desde: {model_path}")
    model = tf.keras.models.load_model(model_path)
    print(f"Intentando cargar scaler_X desde: {scaler_X_path}")
    scaler_X = joblib.load(scaler_X_path)
    print(f"Intentando cargar scaler_y desde: {scaler_y_path}")
    scaler_y = joblib.load(scaler_y_path)
    print("Modelo y escaladores cargados correctamente.")

except FileNotFoundError as e:
    print(f"Error: No se encontró el archivo: {e.filename}")
    model = None
    scaler_X = None
    scaler_y = None

except Exception as e:
    print(f"Error al cargar el modelo o los escaladores: {e}")
    model = None
    scaler_X = None
    scaler_y = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])  # Cambiado a GET para cargar desde el archivo
def predict():
    if model is None or scaler_X is None or scaler_y is None:
        return jsonify({"error": "Modelo o escaladores no cargados."}), 500

    try:
        # Cargar datos desde el archivo JSON
        with open('input_data.json', 'r') as f:
            data = json.load(f)

        input_data = np.array([data['features']])

        # Escalar los datos de entrada
        input_data_scaled = scaler_X.transform(input_data)

        # Realizar la predicción
        prediction_scaled = model.predict(input_data_scaled)

        # Desnormalizar la predicción
        prediction = scaler_y.inverse_transform(prediction_scaled)

        # Transformar a escala original
        prediction_original = np.expm1(prediction).tolist()

        return jsonify({"prediction": prediction_original})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)