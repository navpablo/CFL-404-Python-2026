import ccxt

exchange = ccxt.binance()
exchange.load_markets()

# Mostramos 5 pares conocidos en vez de los primeros por orden alfabético
pares = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT', 'BNB/USDT', 'XRP/USDT']

print("=== Pares seleccionados en Binance ===")
for par in pares:
    print(f"• {par}")

# Consultamos el precio de Bitcoin
symbol = 'BTC/USDT'
ticker = exchange.fetch_ticker(symbol)

print("\n=== Resumen de BTC/USDT ===")
print(f"Precio actual : ${ticker['last']:,.2f} USD")
print(f"Máximo (24h)  : ${ticker['high']:,.2f} USD")
print(f"Mínimo (24h)  : ${ticker['low']:,.2f} USD")
print(f"Variación     : {ticker['percentage']:.2f}%")