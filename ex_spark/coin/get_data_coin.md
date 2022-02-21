# team1
The most friendly team
# Используя api.coingecko.com забрать ohlcv информацию о монетах за 365 дней
# По полученным данным посчитать 30ое скользящее стреднее(SMA30) и в отдельный файл вывести те ohlcv, в которых цена закрытия выше чем SMA30 в данном временном блоке.
monet = 'aave'
curl -X 'GET'  'https://api.coingecko.com/api/v3/coins/aave'  -H 'accept: application/json' > coin.json
jupyter notebook
