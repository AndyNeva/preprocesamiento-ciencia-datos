import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def cargar_datos(ruta):
    """
    Carga el dataset desde la ruta especificada.
    """
    df = pd.read_csv(ruta)
    return df

def validar_outliers(df):
    """
    Valida que los valores numéricos estén dentro de rangos clínicos plausibles.
    Si encuentra valores imposibles, los convierte en NaN para ser imputados.
    Si son extremos pero posibles, los mantiene.
    """
    # Definición de rangos clínicos seguros
    limites = {
        'age': (0, 120),
        'resting_blood_pressure': (50, 250),
        'cholestoral': (50, 600),
        'Max_heart_rate': (40, (208 - 0.7*df['age'])),
        'oldpeak': (0, 10)
    }
    
    for col, (min_val, max_val) in limites.items():
        # Identificar valores fuera del rango clínico posible
        mask = (df[col] < min_val) | (df[col] > max_val)
        if mask.any():
            print(f"Advertencia: Se encontraron {mask.sum()} valores imposibles en {col}. Se convertirán a NaN.")
            df.loc[mask, col] = np.nan
            
    return df

def limpiar_iniciales(df):
    """
    Elimina duplicados exactos y corrige errores de digitación conocidos.
    """
    # Eliminar filas duplicadas exactas
    df.drop_duplicates(inplace=True)
    
    # Corregir valor 'No' en thalassemia que es un error de dato
    # Se convierte a NaN para ser tratado como valor faltante
    df['thalassemia'] = df['thalassemia'].replace('No', np.nan)
    
    return df

def manejar_nulos(df):
    """
    Gestiona valores faltantes si existen. 
    """
    # Verificar si quedaron nulos tras la limpieza inicial
    if df.isnull().values.any():
        # Imputar numéricas con mediana
        cols_num = ['resting_blood_pressure', 'cholestoral', 'Max_heart_rate', 'oldpeak']
        for col in cols_num:
            if df[col].isnull().any():
                df[col].fillna(df[col].median(), inplace=True)
        
        # Imputar categóricas con moda
        if df['thalassemia'].isnull().any():
            df['thalassemia'].fillna(df['thalassemia'].mode()[0], inplace=True)
            
    return df

def codificar_categoricas(df):
    """
    Convierte variables categóricas a númericas para que el modelo las entienda.
    """
    # Mapeo manual para la variable de fasting_blood_sugar
    df['fasting_blood_sugar'] = df['fasting_blood_sugar'].map({
        'Lower than 120 mg/ml': 0, 
        'Greater than 120 mg/ml': 1
    })
    
    # One-Hot Encoding para variables nominales
    # drop_first=True evita la redundancia de información (multicolinealidad)
    cols_nominales = ['sex', 'chest_pain_type', 'rest_ecg', 'exercise_induced_angina', 'slope', 'thalassemia']
    
    df = pd.get_dummies(df, columns=cols_nominales, drop_first=True)
    
    return df

def normalizar_numericas(df):
    """
    Escala las variables continuas para que estén normalizadas (media 0 y desviación estándar 1).
    """
    scaler = StandardScaler()
    
    cols_a_escalar = ['age', 'resting_blood_pressure', 'cholestoral', 'Max_heart_rate', 'oldpeak']
    
    df[cols_a_escalar] = scaler.fit_transform(df[cols_a_escalar])
    
    return df

def pipeline_completo(ruta_entrada, ruta_salida):
    """
    Ejecuta todo el proceso de preprocesamiento en orden.
    """
    print("Iniciando preprocesamiento...")
    
    # 1. Carga
    df = cargar_datos(ruta_entrada)
    
    # 2. Limpieza básica
    df = limpiar_iniciales(df)

    # 3. Validar Outiers
    df = validar_outliers(df)
    
    # 4. Manejo de nulos
    df = manejar_nulos(df)
    
    # 5. Codificación
    df = codificar_categoricas(df)
    
    # 6. Normalización
    df = normalizar_numericas(df)
    
    # 6. Guardado
    df.to_csv(ruta_salida, index=False)
    print(f"Proceso terminado. Dataset guardado en {ruta_salida}")
    print(f"Dimensiones finales: {df.shape}")

if __name__ == "__main__":
    pipeline_completo('data/raw/heart.csv', 'data/processed/heart_clean.csv')