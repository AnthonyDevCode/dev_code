class HomeController < ApplicationController
  def index

    require 'net/http'
    require 'Json'

    # Get news api
    @url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
    @uri = URI(@url)
    @response = Net::HTTP.get(@uri)
    @news = JSON.parse(@response)


    # Get prices api
    @prices_url = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH&tsyms=USD,EUR"
    @prices_uri = URI(@prices_url)
    @prices_response = Net::HTTP.get(@prices_uri)
    @prices = JSON.parse(@prices_response)


  end
  
  def prices

    @symbol = params[:sym]

    @symbol = @symbol.upcase


    # Get single prices api
    @prices_url_single = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+@symbol+"&tsyms=USD,EUR"
    @prices_uri_single = URI(@prices_url_single)
    @prices_response_single = Net::HTTP.get(@prices_uri_single)
    @prices_single = JSON.parse(@prices_response_single)


    # Get news api
    @url_single = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
    @uri_single = URI(@url_single)
    @response_single = Net::HTTP.get(@uri_single)
    @news_single = JSON.parse(@response_single)



  end
end
