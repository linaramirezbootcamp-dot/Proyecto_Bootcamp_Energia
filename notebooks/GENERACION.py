import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib 

# Cargar y preparar datos
df = pd.read_csv('data/Generacion.csv')
df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')
df = df[['Fecha', 'GeneracionRealEstimada']].dropna()
df_agrup = df.groupby(['Fecha'], as_index=False).sum()

# Preparar datos para Prophet
df_prophet = df_agrup.copy()
df_prophet.rename(columns={'Fecha': 'ds', 'GeneracionRealEstimada': 'y'}, inplace=True)
df_prophet['ds'] = pd.to_datetime(df_prophet['ds'])

# Crear festivos colombianos (simulado)
def obtener_festivos_colombia(year):
    festivos = [
        pd.to_datetime(f'{year}-01-01'),  # Año Nuevo
        pd.to_datetime(f'{year}-01-06'),  # Reyes Magos
        pd.to_datetime(f'{year}-05-01'),  # Día del Trabajo
        pd.to_datetime(f'{year}-07-20'),  # Independencia
        pd.to_datetime(f'{year}-08-07'),  # Boyacá
        pd.to_datetime(f'{year}-12-08'),  # Inmaculada
        pd.to_datetime(f'{year}-12-25'),  # Navidad
    ]
    return pd.DataFrame({
        'holiday': 'colombia_holiday',
        'ds': festivos,
        'lower_window': 0,
        'upper_window': 1
    })

años = range(df_prophet['ds'].min().year, df_prophet['ds'].max().year + 1)
festivos_df = pd.concat([obtener_festivos_colombia(year) for year in años])
festivos_df = festivos_df.drop_duplicates(subset=['ds']).reset_index(drop=True)

# Entrenar modelo Prophet
modelo = Prophet(
    holidays=festivos_df,
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False,
    seasonality_mode='multiplicative'
)
modelo.fit(df_prophet)

# Guardar modelo
MODEL_PATH = os.path.join('models', 'modelo_prophet_generacion.joblib')
joblib.dump(modelo, MODEL_PATH)

# Predicción futura
dias_futuros = 365
future = modelo.make_future_dataframe(periods=dias_futuros)
forecast = modelo.predict(future)

# Evaluación en datos históricos
df_pred = pd.merge(df_prophet, forecast[['ds', 'yhat']], on='ds', how='inner')
y_true = df_pred['y']
y_pred = df_pred['yhat']

mae_historico = mean_absolute_error(y_true, y_pred)
rmse_historico = np.sqrt(mean_squared_error(y_true, y_pred))
r2_historico = r2_score(y_true, y_pred)

# Validación cruzada
df_cv = cross_validation(
    modelo,
    initial='365 days',
    period='30 days',
    horizon='90 days'
)

# Métricas de validación cruzada
metrics_cv = performance_metrics(df_cv)
metrics_promedio = metrics_cv[['mse', 'rmse', 'mae', 'mape']].mean()

# Resultados finales
resultados = {
    'Evaluación Histórica': {
        'MAE': round(mae_historico, 2),
        'RMSE': round(rmse_historico, 2),
        'R²': round(r2_historico, 4)
    },
    'Validación Cruzada (Promedio)': {
        'MAE': round(metrics_promedio['mae'], 2),
        'RMSE': round(metrics_promedio['rmse'], 2),
        'MSE': round(metrics_promedio['mse'], 2),
        'MAPE': round(metrics_promedio['mape'], 4)
    }
}

# Mostrar resultados
for categoria, metricas in resultados.items():
    print(f"\n{categoria}:")
    for metrica, valor in metricas.items():
        print(f"  {metrica}: {valor:,}")

# Interpretación del R²
if r2_historico > 0.8:
    interpretacion = "Excelente ajuste (>80% varianza explicada)"
elif r2_historico > 0.5:
    interpretacion = "Buen ajuste (>50% varianza explicada)"
else:
    interpretacion = "Ajuste limitado (<50% varianza explicada)"

print(f"\nInterpretación: {interpretacion}")

# Visualización de resultados
fig, axes = plt.subplots(2, 1, figsize=(15, 10))

# Gráfico 1: Predicción vs Real (últimos 2 años)
ultimos_datos = df_pred.tail(730)
axes[0].plot(ultimos_datos['ds'], ultimos_datos['y'], label='Real', alpha=0.7)
axes[0].plot(ultimos_datos['ds'], ultimos_datos['yhat'], label='Predicción', alpha=0.7)
axes[0].set_title('Generación Real vs Predicción (Últimos 2 años)')
axes[0].set_ylabel('Generación (kW)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Gráfico 2: Predicción futura
axes[1].plot(forecast.tail(365)['ds'], forecast.tail(365)['yhat'],
             label='Predicción Futura', color='red', alpha=0.8)
axes[1].fill_between(forecast.tail(365)['ds'],
                     forecast.tail(365)['yhat_lower'],
                     forecast.tail(365)['yhat_upper'],
                     alpha=0.2, color='red')
axes[1].set_title('Predicción Futura (365 días)')
axes[1].set_xlabel('Fecha')
axes[1].set_ylabel('Generación (kW)')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Componentes del modelo
modelo.plot_components(forecast)
plt.show()
