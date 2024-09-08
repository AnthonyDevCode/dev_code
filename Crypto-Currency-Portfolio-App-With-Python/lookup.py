
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from tkinter import *
import requests
import json
import os 
import random

os.system('cls')


def red_green(amount):	
	try:
		if float(amount) < 0:
			return "red"

		else:
			pass
	except ValueError:
	    pass


def red_green2(amount):	
	try:
		if float(amount) < 0:
			return "red"

		else:
			return "green"
	except ValueError:
	    pass

def random_color_generator():
    color = random.choice(list(mcolors.CSS4_COLORS.keys()))
    return color


root = Tk()
root.title("Currency Portfolio")
# root.iconbitmap()

# Create header
header = ["Name","Rank","Amount Owned","Current Price (£)","Price Paid (£)","P/L Per (£)","24 Hr Change %", "High 24 (£)", "Low 24 (£)", "Current Value (£)", "P/L Total (£)"]

position = 0
bg = "white"
for x in header:
	x = Label(root, text=f"{x}" ,bg=bg, font="Verdana 8 bold")
	x.grid(row=0, column=int(position), sticky=N+S+E+W)
	position += 1
	if bg == "white":
		bg = "silver"
	else:
		bg = "white"


def lookup():

	api_request = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&order=market_cap_desc&per_page=10&page=1&sparkline=false")
	api = json.loads(api_request.content)

	my_portfolio = [{						
					"sym": "DOGE",
					"amount_owned": 5,
					"price_paid_per": .55
					},{						
					"sym": "ETH",
					"amount_owned": 6,
					"price_paid_per": 1500.65
					},{						
					"sym": "USDT",
					"amount_owned": 8,
					"price_paid_per": .15
					},{						
					"sym": "BNB",
					"amount_owned": 7,
					"price_paid_per": .54
					},{						
					"sym": "SOL",
					"amount_owned": 9,
					"price_paid_per": .84
					},{						
					"sym": "USDC",
					"amount_owned": 7,
					"price_paid_per": 1.80
					},{						
					"sym": "XRP",
					"amount_owned": 6,
					"price_paid_per": 6.80
					},{						
					"sym": "BTC",
					"amount_owned": 1,
					"price_paid_per": 42135
					},{						
					"sym": "STETH",
					"amount_owned": 3,
					"price_paid_per": 2.87
					},{						
					"sym": "TRX",
					"amount_owned": 8,
					"price_paid_per": 2.80
					}]

	position_z = 1	
	portfolio_profit_loss = 0	
	total_current_value = 0

	pie = []
	pie_size = []

	for x in api:
		profit_loss = 0
		profit_loss_per_coin = 0
		
		for coin in my_portfolio:
			
			if coin["sym"] == x["symbol"] or coin["sym"].lower() == x["symbol"]:
				total_paid = float(coin["amount_owned"]) * float(coin["price_paid_per"])
				current_value = float(coin["amount_owned"]) * float(x["current_price"])				
				

				if float(coin["amount_owned"]) > 0:
					profit_loss = current_value - total_paid
					profit_loss_per_coin = float(x["current_price"]) - float(coin["price_paid_per"])


				portfolio_profit_loss += profit_loss
				total_current_value += current_value	

				pie.append(x["name"])
				pie_size.append(coin["amount_owned"])

				data_sets = [x["name"],x["market_cap_rank"],coin["amount_owned"],"{0:.2f}".format(float(x["current_price"])),"{0:.2f}".format(float(coin["price_paid_per"])),
				"{0:.2f}".format(float(profit_loss_per_coin)),"{0:.2f}".format(float(x["price_change_24h"])),"{0:.2f}".format(float(x["high_24h"])),
				 "{0:.2f}".format(float(x["low_24h"])), "{0:.2f}".format(float(current_value)) , "{0:.2f}".format(float(profit_loss)) ]

				position_y = 0
				bg_y = "white"
				for y in data_sets:
					y = Label(root, text=y ,bg=bg_y, fg=red_green(y))
					y.grid(row=int(position_z), column=int(position_y), sticky=N+S+E+W)
					position_y += 1
					
					if bg_y == "white":
						bg_y = "silver"
					else:
						bg_y = "white"

		position_z += 1


	portfolio_profits = Label(root, text="Portfolio Profit/Loss £{0:.2f}".format(float(portfolio_profit_loss)), font="Verdana 8 bold", fg=red_green2(portfolio_profit_loss))
	portfolio_profits.grid(row=position_z, column=0, sticky=W, padx=10,pady=10)




	def create_chart(pie,pie_size):	
		# Defining data for the chart
		labels = pie
		sizes = pie_size
		colors = [random_color_generator(), random_color_generator(), random_color_generator(), random_color_generator(),
		 random_color_generator(), random_color_generator(), random_color_generator(), random_color_generator(), random_color_generator(), random_color_generator()]
		explode = (0, 0.1, 0, 0,0,0,0,0,0,0)  # explode 1st slice

		# Plotting the chart
		plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
		plt.axis('equal')
		plt.show()



	update_button = Button(root, text="Pie Chart", command=lambda: create_chart(pie,pie_size))
	update_button.grid(row=position_z, column=2, sticky=E+S, padx=5,pady=5)


	position_z += 1


	update_button = Button(root, text="Update Prices", command=lookup)
	update_button.grid(row=position_z, column=10, sticky=E+S, padx=5,pady=5)

	portfolio_profits = Label(root, text="Portfolio Total Current Value £{0:.2f}".format(float(total_current_value)), font="Verdana 8 bold", fg=red_green2(total_current_value))
	portfolio_profits.grid(row=position_z, column=0, sticky=W, padx=10,pady=10)

	api = ''



lookup()



root.mainloop()
