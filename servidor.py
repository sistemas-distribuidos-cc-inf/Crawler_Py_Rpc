from xmlrpc.server import SimpleXMLRPCServer
from html.parser import HTMLParser  
from urllib.request import urlopen  
from urllib import parse
from xmlrpc.server import SimpleXMLRPCRequestHandler


class LinkParser(HTMLParser):


    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    newUrl = parse.urljoin(self.baseUrl, value)
                    self.links = self.links + [newUrl]

					
    def getLinks(self, url):
        self.links = []
        self.baseUrl = url
        response = urlopen(url)
        if response.getheader('Content-Type')=='text/html':
            htmlBytes = response.read()
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return htmlString, self.links
        else:
            return "",[]


def spider(url, word):
	maxPages = 50
	pagesToVisit = [url]
	numberVisited = 0
	foundWord = False

	while numberVisited < maxPages and pagesToVisit != []:
		numberVisited = numberVisited +1
        # Start from the beginning of our collection of pages to visit:
		url = pagesToVisit[0]
		pagesToVisit = pagesToVisit[1:]
		try:
			print(numberVisited, "Visiting:", url,"\n")
			parser = LinkParser()
			data, links = parser.getLinks(url)
			if data.find(word)>-1:
				foundWord = True
                # Add the pages that we visited to the end of our collection
                # of pages to visit:
				pagesToVisit = pagesToVisit + links
				print(" **Success!**")
				arquivo = open('Crawler.txt', 'w')
		except:
			print(" **Failed!**")
		if foundWord:
			#print("The word", word, "was found at", url)
			conteudo = (word, " - ", url)
			arquivo.writelines(conteudo)
			arquivo.writelines("\n")
		else:
			print("Word never found")
	print("Process finished")
			

server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
print("Listening on port 8000...")
server.register_function(spider, "spider")
server.serve_forever()		