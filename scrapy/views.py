from django.shortcuts import render,HttpResponse
from .models import Home
from bs4 import BeautifulSoup
import re
import requests
from requests.compat import quote_plus
# Create your views here.

def home(request):
    #context={'name':'hemant'}
    return render(request,"home.html")
    #return HttpResponse(context.items())
def new_search(request):
    if request.method=='POST':
        search=request.POST.get('search')
        
        home=Home(search=search)
        home.save()
    base_url='https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    final_base_url=base_url.format(quote_plus(search))
    response=requests.get(final_base_url)
    data=response.text
    soup=BeautifulSoup(data,features='html.parser')
    data=soup.find_all("a",{"class":"_31qSD5"})
    posts=[]
    for post in data:
        price=post.find("div",{"class":"_1vC4OE _2rQ-NK"}).text
        name=post.find("div",{'class':'_3wU53n'}).text.split("-")[0]
        global specs
        specs=post.find("ul",{"class":"vFw0gD"}).text
        
        #url=post.find("a").get(href)
        image=post.find("img").get("src")
        posts.append((price,name,image,specs))
    
#print(price[0].text,name,specs[0].text)
#print(price,name,specs)
    context={"search":search,
            'posts':posts,
            }
    
    return render(request,"new_search.html",context)

def specs1(request):
    specs_data={"specs":specs}
    return render(request,"specs.html",specs_data)


