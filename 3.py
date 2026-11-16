import ccxt

exchange = ccxt.binance()
symbol = 'BTC/USDT'

# 1. Libro de órdenes (ofertas activas)
order_book = exchange.fetch_order_book(symbol)
mejor_compra = order_book['bids'][0][0]
mejor_venta  = order_book['asks'][0][0]
spread       = mejor_venta - mejor_compra

print(f"=== Libro de Órdenes ({symbol}) ===")
print(f"Mejor oferta de compra : ${mejor_compra:,.2f} USD")
print(f"Mejor oferta de venta  : ${mejor_venta:,.2f} USD")
print(f"Diferencia (Spread)    : ${spread:.2f} USD")

# 2. Últimas 5 operaciones concretadas
trades = exchange.fetch_trades(symbol, limit=5)

print(f"\n=== Últimas 5 Operaciones ===")
print(f"{'TIPO':<8} | {'CANTIDAD':<12} | {'PRECIO'}")
print("-" * 38)

for t in trades:
    tipo = "COMPRA" if t['side'] == 'buy' else "VENTA"
    print(f"{tipo:<8} | {t['amount']:.5f} BTC  | ${t['price']:,.2f}")

# 3. Precio promedio
promedio = sum(t['price'] for t in trades) / len(trades)
print("-" * 38)
print(f"Precio promedio        : ${promedio:,.2f} USD")