import ccxt
import time
from datetime import datetime

exchange = ccxt.binance()
symbol = 'BTC/USDT'
umbral_compra = -3.20

print(f"=== Monitor de Variacion 24h: {symbol} ===")
print(f"Senal de compra si la variacion baja de {umbral_compra:.2f}% (Ctrl+C para salir)\n")

try:
    while True:
        ticker = exchange.fetch_ticker(symbol)
        precio = ticker['last']
        cambio = ticker['percentage']
        hora = datetime.now().strftime("%H:%M:%S")

        signo = "+" if cambio >= 0 else ""

        if cambio > umbral_compra:
            sugerencia = "SEÑAL: Evaluar VENTA (precio sostenido)"
        else:
            sugerencia = "SEÑAL: Evaluar COMPRA (caida pronunciada)"

        print(f"\r[{hora}] BTC: ${precio:,.2f} USD ({signo}{cambio:.2f}%) | {sugerencia}   ", end="", flush=True)
        time.sleep(7)

except KeyboardInterrupt:
    print("\n\nMonitoreo finalizado por el usuario.")