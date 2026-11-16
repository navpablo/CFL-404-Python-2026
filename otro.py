import ccxt

# 1. Capacidad de la librería y del exchange
print("=== Explorador de Mercado CCXT ===")
print(f"Exchanges soportados : {len(ccxt.exchanges)} plataformas")
print(f"Ejemplos             : {', '.join(ccxt.exchanges[:6])}...\n")

exchange = ccxt.binance()
exchange.load_markets()

print(f"Exchange activo      : {exchange.name} ({exchange.id})")
print(f"Pares disponibles    : {len(exchange.symbols):,} mercados\n")

# 2. Inspección limpia de los datos clave del Ticker
symbol = 'BTC/USDT'
ticker = exchange.fetch_ticker(symbol)

campos_clave = {
    'Fecha / Hora (UTC)' : ticker['datetime'],
    'Precio Apertura'    : f"${ticker['open']:,.2f} USD",
    'Precio Máximo 24h'  : f"${ticker['high']:,.2f} USD",
    'Precio Mínimo 24h'  : f"${ticker['low']:,.2f} USD",
    'Último Precio'      : f"${ticker['last']:,.2f} USD",
    'Variación 24h'      : f"{ticker['percentage']:.2f}%",
    'Volumen 24h (BTC)'  : f"{ticker['baseVolume']:,.2f} BTC"
}

print(f"=== Ficha Técnica: {symbol} ===")
for etiqueta, valor in campos_clave.items():
    print(f"{etiqueta:<20} : {valor}")