import ccxt
import pandas as pd
import matplotlib.pyplot as plt

exchange = ccxt.binance()

# Pedimos 48 velas de 1 hora para que coincida con el título (últimas 48h)
ohlcv = exchange.fetch_ohlcv('BTC/USDT', '1h', limit=48)

df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

# Estilo oscuro y tamaño cómodo de ventana
plt.style.use('dark_background')
plt.figure(figsize=(10, 5))

# Línea principal y sombreado suave debajo
plt.plot(df['timestamp'], df['close'], color='#00ffcc', linewidth=2, label='Precio Cierre')
plt.fill_between(df['timestamp'], df['close'], df['close'].min(), color='#00ffcc', alpha=0.1)

# Detalles visuales: título, etiquetas, cuadrícula y rotación de fechas
plt.title("Evolución BTC/USDT (Últimas 48 horas)", fontsize=13, fontweight='bold')
plt.xlabel("Fecha y Hora")
plt.ylabel("Precio (USD)")
plt.xticks(rotation=30)
plt.grid(True, linestyle='--', alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()