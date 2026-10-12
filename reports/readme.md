Criterios de comparación

Los modelos se analizan considerando:

- Desempeño: accuracy de coincidencia exacta, precision, recall, F1 micro y F1 macro.
- Latencia: tiempo de carga y tiempo de inferencia por mensaje.
- Recursos: memoria utilizada y dispositivo de ejecución.
- Compatibilidad: facilidad de implementación con Python, Google Colab y Hugging Face Transformers.
- Español: capacidad de interpretar mensajes relacionados con el cuidado de la piel.
- Licencia: condiciones de uso documentadas en las fichas oficiales de cada modelo.

Metodología

La evaluación utiliza un conjunto de mensajes de skincare etiquetados según las intenciones del cliente.

Los modelos reciben los mismos mensajes y las mismas etiquetas candidatas para mantener condiciones de comparación consistentes. Los umbrales de clasificación se ajustan utilizando el conjunto de validación, mientras que el conjunto de prueba se reserva para la evaluación final.

Las mediciones de rendimiento deben documentar las versiones de las bibliotecas, el hardware utilizado, el tamaño del lote y la configuración de inferencia.

Resultados y conclusiones

Las métricas experimentales se obtienen al ejecutar el notebook de Google Colab y se almacenan en la carpeta results/.

La selección del modelo recomendado se basará en el equilibrio entre desempeño, latencia, consumo de recursos y requisitos de implementación.

No se considerará que un modelo es superior hasta analizar los resultados reales y sus errores por intención.

Limitaciones y seguridad

El dataset sintético permite realizar una evaluación preliminar, pero no garantiza el mismo desempeño con clientes reales.

Glow AI tiene como finalidad orientar la búsqueda de productos cosméticos a partir de las preferencias declaradas por el usuario. No realiza diagnósticos médicos ni sustituye a un dermatólogo.

Los ingredientes, precios y disponibilidad deben verificarse mediante un catálogo de productos confiable y actualizado.

Reproducibilidad

El código experimental y las instrucciones de ejecución se encuentran en la carpeta notebooks/ y en el archivo README.md principal del repositorio.

Para reproducir los resultados, deben ejecutarse las celdas del notebook y conservarse las métricas obtenidas durante la evaluación.
