# glow-ai-model
Comparación de modelos NLP zero-shot para comprender necesidades de skincare en lenguaje natural.

Glow AI es un prototipo académico de un asistente de inteligencia artificial que interpreta las necesidades de los clientes de skincare expresadas en español.

El sistema identifica intenciones relacionadas con el tipo de piel, los objetivos cosméticos, los ingredientes que se desean evitar, el presupuesto, las preferencias de producto y las solicitudes de recomendación.

El proyecto compara tres modelos de clasificación zero-shot del ecosistema Hugging Face para determinar cuál ofrece el mejor equilibrio entre desempeño, latencia y consumo de recursos.

Glow AI no sustituye a un dermatólogo ni realiza diagnósticos médicos. Su función es facilitar la búsqueda de productos cosméticos a partir de las preferencias declaradas por el cliente.

Objetivos
- Comparar al menos tres modelos de NLP.
- Evaluar accuracy, precision, recall y F1-score.
- Medir el tiempo de carga y la latencia de inferencia.
- Documentar los recursos computacionales utilizados.
- Analizar errores y diferencias entre las intenciones.
- Establecer criterios reproducibles para seleccionar un modelo.

Modelos evaluados
- valhalla/distilbart-mnli-12-1
- facebook/bart-large-mnli
- MoritzLaurer/bge-m3-zeroshot-v2.0-c

Los modelos se cargan desde Hugging Face Hub. Sus fichas oficiales deben consultarse para verificar arquitectura, licencia y requisitos de uso.

Tecnologías
- Python
- Google Colab
- Hugging Face Hub
- Hugging Face Transformers
- Hugging Face Datasets
- PyTorch
- scikit-learn
- pandas
- NumPy
-  Matplotlib

Entorno de ejecución

El experimento se desarrolla en Google Colab con Python y las bibliotecas especificadas en requirements.txt.

Se recomienda habilitar una GPU cuando esté disponible. El notebook también contempla la ejecución en CPU, aunque puede ser considerablemente más lenta.

Las mediciones dependen del hardware, las versiones de las bibliotecas, el tamaño del lote y la configuración de inferencia.

Instalación

- Clona el repositorio:

git clone https://github.com/USUARIO/glow-ai-model-comparison.git
cd glow-ai-model-comparison

- Crea un entorno virtual:

python -m venv .venv

- Actívalo en Windows:

.venv\Scripts\activate

- Actívalo en Linux o macOS:

source .venv/bin/activate

Instala las dependencias:

- pip install -r requirements.txt
- Pasos de ejecución
- Abre notebooks/glow_ai_model_comparison.ipynb en Google Colab.
- Configura el entorno de ejecución y habilita GPU si está disponible.
- Instala las dependencias.
- Configura opcionalmente el token de Hugging Face mediante los secretos de Colab.
- Carga y valida el dataset.
- Ejecuta la inferencia de los tres modelos.
- Calcula las métricas en el conjunto de prueba.
- Mide latencia y consumo de memoria.
- Genera las tablas y exporta los resultados.
- Actualiza este README y el reporte con los resultados reales.
- Métricas

Se calculan:

- Accuracy de coincidencia exacta entre las etiquetas reales y las predichas.
- Precision micro.
- Recall micro.
- F1 micro.
- F1 macro.
- Latencia media por mensaje.
- Percentil 95 de latencia cuando se dispone de suficientes mediciones.
- Tiempo de carga y memoria de GPU cuando corresponda.

Los umbrales de clasificación se ajustan con el conjunto de validación, no con el conjunto de prueba.
