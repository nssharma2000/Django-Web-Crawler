from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import json
# Create your views here.


def index(request):
    
    return render(request, "home.html")

def crawler(url, depth):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tags = soup.find_all('a')[0: depth]
        links = []
        for i in tags:
            links.append(str(i))
        return links
    
def crawl(request):
    if request.method == "POST":
        crawled_url = request.POST['crawled_url']
        depth = int(request.POST['depth_i'])
    crawled_links = crawler(crawled_url, depth)
    context = { "url" : crawled_url , "crawled_data" : crawled_links, "crawled_links" : json.loads(json.dumps({"crawled_links": crawled_links}))}
    return render(request, "home.html", context)