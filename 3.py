import ccxt
import time
from datetime import datetime

exchange = ccxt.binance()
symbol = 'BTC/USDT'

# 1. Tomamos el precio actual como referencia para calcular un objetivo realista (-0.05% abajo)
precio_inicial = exchange.fetch_ticker(symbol)['last']
precio_objetivo = precio_inicial * 0.9995

print(f"=== Monitor en Vivo: {symbol} ===")
print(f"Precio inicial  : ${precio_inicial:,.2f} USD")
print(f"Alerta si baja a: ${precio_objetivo:,.2f} USD (Ctrl+C para salir)\n")

precio_anterior = precio_inicial

try:
    while True:
        precio = exchange.fetch_ticker(symbol)['last']
        hora = datetime.now().strftime("%H:%M:%S")

        if precio > precio_anterior:
            tendencia = "▲ SUBE"
        elif precio < precio_anterior:
            tendencia = "▼ BAJA"
        else:
            tendencia = "▬ IGUAL"

        print(f"\r[{hora}] BTC: ${precio:,.2f} USD | {tendencia}   ", end="", flush=True)

        if precio <= precio_objetivo:
            print(f"\n\n ¡ALERTA! {symbol} bajó de ${precio_objetivo:,.2f} USD")
            break

        precio_anterior = precio
        time.sleep(3)

except KeyboardInterrupt:
    print("\n\nMonitoreo detenido por el usuario.")