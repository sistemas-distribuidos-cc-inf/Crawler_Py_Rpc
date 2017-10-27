import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:

	site = input("Digite o site: ")
	siteCraw = 'http://'+site
	palavra = input("Digite a palavra: ")
	max_page = int(input("Digite a quantidade maxima de paginas: "))
	print (siteCraw)
	proxy.spider(siteCraw, palavra, max_page)