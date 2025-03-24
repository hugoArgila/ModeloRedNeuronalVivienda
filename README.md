## **Proyecto de Predicción de Precios de Vivienda**

Este proyecto consiste en una API Flask que utiliza un modelo de aprendizaje automático para predecir los precios de las viviendas. El modelo se entrena con un conjunto de datos que incluye diversas características de las propiedades, como el número de habitaciones, el tamaño en metros cuadrados y otras características relevantes.

**Características principales:**

* **API Flask:** La aplicación proporciona una API RESTful construida con Flask.  
* **Predicción de precios:** La API expone un endpoint /predict que acepta datos de entrada y devuelve el precio de vivienda predicho por el modelo.  
* **Modelo de aprendizaje automático:** El proyecto incluye un modelo de regresión entrenado.  
* **Escalado de datos:** Los datos de entrada se escalan utilizando RobustScaler antes de ser introducidos en el modelo.  
* **Manejo de datos JSON:** La API puede recibir datos de entrada en formato JSON.  
* **Despliegue sencillo:** La aplicación se puede ejecutar fácilmente usando Python.

**Tecnologías utilizadas:**

* Python  
* Flask  
* TensorFlow  
* scikit-learn  
* joblib  
* NumPy

**Instalación:**

1. Clona este repositorio:  
   git clone \<URL\_DEL\_REPOSITORIO\>

2. Crea un entorno virtual (recomendado):  
   python3 \-m venv venv  
   cd venv  
   source bin/activate  \# En macOS/Linux  
   . venv/Scripts/activate  \# En Windows

3. Instala las dependencias:  
   pip install \-r requirements.txt

**Uso:**

1. Asegúrate de tener un modelo entrenado y los escaladores guardados en la carpeta modelos.  
2. Ejecuta la aplicación:  
   python app.py

3. La API estará disponible en http://127.0.0.1:5000.

**Endpoint de Predicción:**

* POST /predict  
  * Descripción: Este endpoint se utiliza para obtener la predicción del precio de una vivienda.  
  * Método: POST  
  * Formato de entrada: JSON

  Ejemplo de entrada:{  
    "features": \[  
        1.000000e+00,  
        0.000000e+00,  
        2.000000e+00,  
        0.000000e+00,  
        0.000000e+00,  
        0.000000e+00,  
        1.400000e+02,  
        0.000000e+00,  
        3.000000e+00,  
        0.000000e+00,  
        1.000000e+00,  
        0.000000e+00,  
        9.098071e-01,  
        2.288987e-01,  
        7.114148e-03,  
        1.375402e-01,  
        3.788183e-01,  
        3.321945e-01,  
        3.967042e-02,  
        3.876608e-01  
    \]  
    }

  * Respuesta: JSON con el precio predicho.

Ejemplo de respuesta:{  
"prediction": \[  
    \[  
        300000.00  
    \]  
\]  
}

**Estado del proyecto:**

Este proyecto se encuentra en desarrollo. Se aceptan contribuciones y sugerencias.