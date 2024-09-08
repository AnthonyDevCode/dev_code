from django.shortcuts import render

def home(request):
	import requests
	import json
	#Grab crypto News
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)

	#Grab crypto price data
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH&tsyms=USD,EUR")
	price = json.loads(price_request.content)

	return render(request, 'home.html',{'api':api, 'price':price})

def prices(request):
	if request.method == 'POST':		
		import requests
		import json

		#Format Input
		quote = request.POST['quote']
		quote = quote.replace('"','')
		quote = quote.replace("'","")
		quote = quote.upper()

		#Grab crypto price data
		crypto_request = requests.get(f"https://min-api.cryptocompare.com/data/pricemultifull?fsyms={quote}&tsyms=USD,EUR")
		crypto_price = json.loads(crypto_request.content)


		#Grab crypto News
		crypto_api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
		crypto_api = json.loads(crypto_api_request.content)

		return render(request, 'prices.html', {'crypto_price':crypto_price, 'crypto_api':crypto_api, 'quote':quote})

	else:
		return render(request, 'prices.html',{})

