import ccxt

binance = ccxt.binance()
kraken = ccxt.kraken()

precio_binance = binance.fetch_ticker('BTC/USDT')['last']
precio_kraken  = kraken.fetch_ticker('BTC/USD')['last']

diferencia = abs(precio_binance - precio_kraken)
porcentaje = (diferencia / min(precio_binance, precio_kraken)) * 100

print("=== Comparativa de Precios (Arbitraje) ===")
print(f"{'EXCHANGE':<12} | {'PAR':<10} | {'PRECIO ACTUAL'}")
print("-" * 42)
print(f"{'Binance':<12} | {'BTC/USDT':<10} | ${precio_binance:,.2f} USD")
print(f"{'Kraken':<12} | {'BTC/USD':<10} | ${precio_kraken:,.2f} USD")
print("-" * 42)
print(f"Diferencia absoluta : ${diferencia:,.2f} USD ({porcentaje:.3f}%)")

print("\n=== Análisis de Oportunidad ===")
if precio_binance > precio_kraken:
    print("-> Comprar en Kraken (más barato) y vender en Binance (más caro).")
elif precio_kraken > precio_binance:
    print("-> Comprar en Binance (más barato) y vender en Kraken (más caro).")
else:
    print("-> Ambos exchanges tienen exactamente el mismo precio.")