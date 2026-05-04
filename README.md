# Preprocesamiento de Datos en Ciencia de Datos

**Autor:** Andrés Nevárez  
**Carrera:** Ciencia de Datos e Inteligencia Artificial
**Fecha:** 10 de mayo de 2026

## Objetivo del Proyecto
Demostrar la aplicación práctica de **Git y GitHub** para la gestión de proyectos de datos. Implementar un pipeline de preprocesamiento y limpieza de datos para el dataset Heart Disease UCI.

En este proyecto se va transformar un dataset crudo en un dataset procesado listo para el modelado. Para esp se seguirán los siguientes pasos:
1. Gestión de valores nulos (imputación/eliminación).
2. Codificación de variables categóricas.
3. Normalización/Escalado de variables numéricas.
4. Eliminación de duplicados.

## Estructura del Proyecto
Este proyecto sigue una estructura modular de acuerdo a los estándares de la industria para garantizar la reproducibilidad y el orden. A continuación  se detalla la estructura:

preprocesamiento-ciencia-datos/
├── .gitignore              # Configuración para ignorar archivos innecesarios
├── README.md               # Documentación principal del proyecto
├── DOCUMENTACION.md        # Informe técnico del proyecto con comandos Git y evidencias
├── preprocesamiento.py     # Script principal con las funciones de limpieza
├── requirements.txt        # Dependencias del proyecto (pandas, numpy, etc.)
├── data/
│   ├── raw/                # Dataset original (sin modificar)
│   └── processed/          # Dataset limpio resultante del pipeline
└── notebooks/              # Exploración inicial de datos (EDA)
