# Modelo de Clasificación de Clientes para Campañas de Marketing

## Visión General del Proyecto
Este proyecto tiene como objetivo entender mejor a los clientes de una tienda de comestibles clasificándolos en tres categorías de valor: bajo, medio y alto. La clasificación se basa en la frecuencia de sus compras, sus hábitos de gasto y el monto máximo que gastan en la tienda. Se desarrolla un modelo en Keras para realizar esta clasificación, que puede utilizarse para crear campañas de marketing personalizadas.

## Configuración del Entorno
Para ejecutar este proyecto, necesitarás tener Python instalado en tu sistema junto con las siguientes bibliotecas:
- TensorFlow
- Keras
- Pandas
- Scikit-learn
- Numpy

Se recomienda utilizar un entorno virtual para gestionar las dependencias.

## Cómo Configurar
1. Clona este repositorio en tu máquina local.
2. Crea un entorno virtual:
python -m venv env

3. Activa el entorno virtual:
- En Windows: `env\Scripts\activate`
- En macOS/Linux: `source env/bin/activate`
4. Instala las dependencias requeridas:

pip install -r requirements.txt


## Ejecutando el Modelo
Para entrenar y evaluar el modelo, ejecuta el script `model_script.py` (reemplaza con el nombre real del script):

python model_script.py


## Notas Adicionales
- Asegúrate de que el archivo del conjunto de datos `data_customer_classification.csv` se encuentre en el directorio correcto según se especifica en el script.
- Ajusta los parámetros del modelo y la configuración del entrenamiento según sea necesario basado en el rendimiento y los requisitos específicos de tu proyecto.

requirements.txt

pip install --force-reinstall requests charset_normalizer

Prueba 
Test accuracy: 0.9891146421432495
Cliente 1: Verdadero Valor = Low, Valor Predicho = Low
Cliente 2: Verdadero Valor = Low, Valor Predicho = Low
Cliente 3: Verdadero Valor = Medium, Valor Predicho = Medium
Cliente 4: Verdadero Valor = High, Valor Predicho = High
Cliente 5: Verdadero Valor = Low, Valor Predicho = Low
Cliente 6: Verdadero Valor = High, Valor Predicho = High
Cliente 7: Verdadero Valor = Low, Valor Predicho = Low
Cliente 8: Verdadero Valor = Low, Valor Predicho = Low
Cliente 9: Verdadero Valor = High, Valor Predicho = High
Cliente 10: Verdadero Valor = Medium, Valor Predicho = Medium