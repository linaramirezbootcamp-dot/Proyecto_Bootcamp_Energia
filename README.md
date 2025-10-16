# ⚡ Proyecto Bootcamp Energía: Planeación de Demanda Energética

Este proyecto forma parte del **Bootcamp de Ciencia de Datos en Energía**, y tiene como objetivo desarrollar un sistema de **planeación y predicción de la demanda energética en Colombia**, integrando análisis de datos, consultas SQL y modelado predictivo en Python.

---

## 🧭 Objetivo del Proyecto

Analizar, modelar y proyectar la **demanda energética nacional** a partir de datos históricos del sector energético colombiano.  
El propósito es apoyar la **toma de decisiones informadas** sobre generación, distribución y consumo de energía.

---

## 🧩 Descripción General

- Obtención y procesamiento de datos desde el portal oficial [**SIMEM**](https://www.simem.co/).  
- Análisis exploratorio y limpieza de datos en Python.  
- Construcción de consultas SQL para extraer, transformar y unir información relevante.  
- Modelado predictivo de la demanda energética utilizando técnicas estadísticas y de *machine learning*.  
- Visualización de tendencias energéticas y resultados.

---

## 🧰 Tecnologías Utilizadas

- **Lenguajes:** Python 🐍 y SQL 💾  
- **Librerías Python:**  
  - `pandas`, `numpy` → Análisis y manipulación de datos  
  - `matplotlib`, `seaborn` → Visualización  
  - `scikit-learn` → Modelado predictivo  
  - `sqlalchemy` → Conexión y manejo de bases de datos  
  - `python-dotenv` → Manejo de variables de entorno (opcional)  
- **Entorno:** Jupyter Notebook  
- **Base de datos / Fuente:** Datos provenientes de **[SIMEM](https://www.simem.co/)** (Sistema de Información Minero Energético Colombiano)

---

## 📂 Estructura del Proyecto

```
Proyecto_Bootcamp_Energia/
│
├── data/               # Datos descargados o transformados (raw/processed)
├── notebooks/          # Jupyter Notebooks de análisis y modelado
├── sql/                # Consultas SQL utilizadas (.sql)
├── src/                # Funciones auxiliares y scripts de procesamiento
├── models/             # Modelos entrenados o serializados (.pkl, .joblib)
├── results/            # Gráficos, reportes y resultados del modelado
├── docs/               # Documentación adicional (opcional)
├── requirements.txt    # Librerías necesarias
└── README.md           # Este archivo
```

---

## 🚀 Ejecución del Proyecto

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/usuario/Proyecto_Bootcamp_Energia.git
   cd Proyecto_Bootcamp_Energia
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno**  
   Crea un archivo `.env` (no subir al repositorio) con las credenciales/URIs necesarias para conectarte a la base de datos o APIs, por ejemplo:
   ```
   DB_USER=tu_usuario
   DB_PASS=tu_contraseña
   DB_HOST=host_de_bd
   DB_NAME=nombre_bd
   ```

4. **Ejecutar notebooks o scripts**
   ```bash
   jupyter notebook
   ```
   o ejecutar scripts desde `src/`:
   ```bash
   python src/etl.py
   python src/train_model.py
   ```

5. **Conectar a la base de datos SIMEM**  
   - Si usas descargas directas desde el portal, guarda los CSV en `data/raw/`.  
   - Si trabajas con una copia local o exportada a una BD, usa `sqlalchemy` o tu conector preferido para ejecutar las consultas en `sql/`.

---

## 🔍 Ejemplo de consulta SQL (simple)

```sql
-- Total de consumo por año y por departamento (ejemplo)
SELECT
  departamento,
  EXTRACT(YEAR FROM fecha) AS año,
  SUM(consumo_mwh) AS consumo_anual_mwh
FROM consumo_energia
GROUP BY departamento, EXTRACT(YEAR FROM fecha)
ORDER BY departamento, año;
```

---

## 📈 Resultados Esperados

- Limpieza y estructuración de datos energéticos de Colombia.  
- Visualización de patrones de consumo por región, hora y tipo de energía.  
- Modelos de predicción de demanda a corto y mediano plazo (p. ej. regresión, series temporales).  
- Informe final con hallazgos, métricas de modelo (MAE, RMSE) y recomendaciones para planeación.

---

## 👩‍💻 Autores

Proyecto desarrollado por el equipo del **Bootcamp Energía**:

- **Santiago Arboleda**
- **Julián Caro**  
- **Liliana Correa**
- **Yan Hoyos**  
- **Lina Ramírez**  


---

## 🤝 Contribuciones

Si deseas contribuir:

1. Haz un *fork* del repositorio.  
2. Crea una rama (`feature/nombre`), realiza cambios y haz *commit*.  
3. Envía un *pull request* explicando tus mejoras.  

Por favor añade issues para errores o propuestas grandes.

---

## 📬 Contacto

**Autores:** Contactar a cualquiera de los autores  
**GitHub:** [@tu_usuario](https://github.com/tu_usuario)  
**Email:** [tu.email@ejemplo.com]

---

## 📄 Licencia

Indica aquí la licencia deseada (por ejemplo MIT). Si no tienes una preferencia, puedo sugerir una plantilla.

---

> “Holi” ⚙️
