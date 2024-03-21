import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# Carga del conjunto de datos
file_path = 'data_customer_classification.csv'
data = pd.read_csv(file_path)

# Conversión de trans_date a datetime
data['trans_date'] = pd.to_datetime(data['trans_date'])

# Cálculo de métricas necesarias para cada cliente
customer_metrics = data.groupby('customer_id').agg(
    purchase_frequency=('trans_date', 'count'),  # Número de transacciones
    average_spending=('tran_amount', 'mean'),  # Gasto promedio por transacción
    max_spending=('tran_amount', 'max')  # Máximo gasto en una transacción
).reset_index()

# Definición de categorías basadas en percentiles para cada métrica
percentiles = customer_metrics.quantile([0.33, 0.66]).to_dict()


def classify_customer(row):
    # Clasificación basada en frecuencia de compra
    if row['purchase_frequency'] <= percentiles['purchase_frequency'][0.33]:
        frequency_class = 'Low'
    elif row['purchase_frequency'] <= percentiles['purchase_frequency'][0.66]:
        frequency_class = 'Medium'
    else:
        frequency_class = 'High'

    # Clasificación basada en gasto promedio
    if row['average_spending'] <= percentiles['average_spending'][0.33]:
        spending_class = 'Low'
    elif row['average_spending'] <= percentiles['average_spending'][0.66]:
        spending_class = 'Medium'
    else:
        spending_class = 'High'

    # Clasificación basada en máximo gasto
    if row['max_spending'] <= percentiles['max_spending'][0.33]:
        max_spending_class = 'Low'
    elif row['max_spending'] <= percentiles['max_spending'][0.66]:
        max_spending_class = 'Medium'
    else:
        max_spending_class = 'High'

    # Agregación de clasificaciones
    classifications = [frequency_class, spending_class, max_spending_class]
    final_class = max(set(classifications), key=classifications.count, default='Medium')
    return final_class


# Aplicación de la clasificación
customer_metrics['customer_value'] = customer_metrics.apply(classify_customer, axis=1)

# Preparación de características de entrada (X) y variable objetivo (y)
X = customer_metrics[['purchase_frequency', 'average_spending', 'max_spending']].values
y = customer_metrics['customer_value'].values

# Codificación numérica de la variable objetivo y
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
y_one_hot = to_categorical(y_encoded)

# División de los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y_one_hot, test_size=0.2, random_state=42)

# Normalización de los datos de características
scaler = StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Definición del modelo
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    Dense(64, activation='relu'),
    Dense(y_train.shape[1], activation='softmax')
])

# Compilación del modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Entrenamiento del modelo
history = model.fit(X_train_scaled, y_train, epochs=100, validation_split=0.2, verbose=1)

# Evaluación del modelo en el conjunto de prueba
test_loss, test_acc = model.evaluate(X_test_scaled, y_test, verbose=2)
print('\nTest accuracy:', test_acc)


import numpy as np

# Realizar predicciones en el conjunto de prueba
predictions_proba = model.predict(X_test_scaled)

# Transformar las probabilidades de las predicciones en etiquetas categóricas
predictions = np.argmax(predictions_proba, axis=1)
predicted_labels = label_encoder.inverse_transform(predictions)

# Si deseas comparar con las etiquetas reales, primero transforma y_one_hot a etiquetas categóricas
true_labels = np.argmax(y_test, axis=1)
true_labels = label_encoder.inverse_transform(true_labels)

# Ahora puedes visualizar las predicciones, por ejemplo, viendo las primeras 10
for i in range(10):
    print(f"Cliente {i+1}: Verdadero Valor = {true_labels[i]}, Valor Predicho = {predicted_labels[i]}")