import ccxt
import pandas as pd
import matplotlib.pyplot as plt

exchange = ccxt.binance()
symbol = 'BTC/USDT'

# 1. Descargamos las últimas 72 horas (3 días) en velas de 1 hora
ohlcv = exchange.fetch_ohlcv(symbol, '1h', limit=72)
df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

# 2. Calculamos dos Medias Móviles (tendencia corta vs tendencia larga)
df['SMA_7'] = df['close'].rolling(window=7).mean()
df['SMA_24'] = df['close'].rolling(window=24).mean()

# 3. Creamos una ventana con 2 paneles: Precio arriba (más grande) y Volumen abajo
plt.style.use('dark_background')
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 6), sharex=True, gridspec_kw={'height_ratios': [3, 1]})

# Panel superior: Precio y Medias Móviles
ax1.plot(df['timestamp'], df['close'], color='#00ffcc', linewidth=1.8, label='Precio Cierre (1h)')
ax1.plot(df['timestamp'], df['SMA_7'], color='#ffcc00', linestyle='--', linewidth=1.3, label='Media Móvil 7h (Rápida)')
ax1.plot(df['timestamp'], df['SMA_24'], color='#ff5577', linestyle='-', linewidth=1.5, label='Media Móvil 24h (Lenta)')

ax1.set_title(f"Análisis Técnico {symbol} - Medias Móviles y Volumen (72h)", fontsize=13, fontweight='bold')
ax1.set_ylabel("Precio (USD)")
ax1.grid(True, linestyle='--', alpha=0.25)
ax1.legend(loc='upper left')

# Panel inferior: Barras de Volumen
ax2.bar(df['timestamp'], df['volume'], color='#4da6ff', alpha=0.6, width=0.03)
ax2.set_ylabel("Volumen (BTC)")
ax2.set_xlabel("Fecha y Hora")
ax2.grid(True, linestyle='--', alpha=0.25)

plt.xticks(rotation=30)
plt.tight_layout()
plt.show()