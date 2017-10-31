import xmlrpc.client
import sys

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:

	site = input("Please enter a website: ")
	siteCraw = 'https://'+site
	palavra = input("Enter a word: ")
	#max_page = int(input("Digite a quantidade maxima de paginas: "))
	print ('Client conected')
	#proxy.spider(siteCraw, palavra)
	try:
		proxy.spider(siteCraw, palavra)
		print ('Search success!')
	except:
		print ('An error ocurred!')