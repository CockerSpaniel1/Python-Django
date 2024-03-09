from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def coffee(request):
    return render(request,"coffee/coffee.html")

def slogan(request):              
    return HttpResponse("再忙也要陪你喝咖啡!")

def history(request):
    response =  HttpResponse()
    response.write("<h1>Coffee Histroy</h1>")
    response.write("<hr>")
    response.write("<p>咖啡的來源已無從稽考。諸多傳說之一指咖啡原產於衣索比亞(Ethiopia)西南部的咖法省高原地區,")
    response.write("據說是一位牧羊人發現羊吃了一種植物後，變得非常興奮活潑，因此發現了咖啡。</p>")
    response.write("<a href='./coffeeWeb' >咖啡品項</a>")
    return response

def coffee1(request):
    return render(request,"coffee/coffee1.html")

