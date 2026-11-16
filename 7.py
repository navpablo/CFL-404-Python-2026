import ccxt
import time

exchange = ccxt.binance()
symbol = 'BTC/USDT'

saldo_inicial = 1000.0
saldo_usd = saldo_inicial
saldo_btc = 0.0

print(f"=== Simulador de Trading: {symbol} ===")
print(f"Capital inicial: ${saldo_inicial:,.2f} USD\n")
print(f"{'RONDA':<6} | {'PRECIO BTC':<13} | {'ACCION':<20} | {'SALDO USD':<12} | {'SALDO BTC'}")
print("-" * 74)

precio_anterior = None

for ronda in range(1, 11):
    precio_actual = exchange.fetch_ticker(symbol)['last']

    # En la ronda 1 hace una compra inicial para tener posicion abierta
    if ronda == 1:
        btc_comprado = 300 / precio_actual
        saldo_btc += btc_comprado
        saldo_usd -= 300
        accion = f"COMPRA (+{btc_comprado:.5f})"

    # Compra $200 USD si el precio bajó respecto a la ronda anterior
    elif precio_actual < precio_anterior and saldo_usd >= 200:
        btc_comprado = 200 / precio_actual
        saldo_btc += btc_comprado
        saldo_usd -= 200
        accion = f"COMPRA (+{btc_comprado:.5f})"

    # Vende todo si el precio subió respecto a la ronda anterior y tiene BTC
    elif precio_actual > precio_anterior and saldo_btc > 0:
        usd_vendido = saldo_btc * precio_actual
        saldo_usd += usd_vendido
        saldo_btc = 0.0
        accion = f"VENTA (+${usd_vendido:.2f})"

    else:
        accion = "MANTIENE POSICION"

    print(f"{ronda:<2}/10  | ${precio_actual:>10,.2f}  | {accion:<20} | ${saldo_usd:>9,.2f}  | {saldo_btc:.5f}")

    precio_anterior = precio_actual
    time.sleep(2)

# Cierre de simulacion
valor_final = saldo_usd + (saldo_btc * precio_actual)
resultado = valor_final - saldo_inicial
signo = "+" if resultado >= 0 else ""

print("-" * 74)
print(f"Valor total final : ${valor_final:,.2f} USD")
print(f"Resultado neto    : {signo}${resultado:,.2f} USD")