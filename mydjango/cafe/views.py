from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
import random

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

def tea(request):
    return render(request,"tea/tea.html")

def tea1(request):
    return render(request,"tea/tea1.html")

def coffee2(request):
    return render(request,"coffee/coffee2.html")

def coffee3(request):
    return render(request,"coffee/coffee3.html",{
        "name":"阿拉比卡","price":500,"qty":10
    })
def coffee4(request):
    promo ="世界咖啡節，全面買一送一"
    item={
        "name":"羅布斯塔", "price":450, "qty":10
    }

    return render(request,"coffee/coffee4.html", locals())

def coffee5(request):
    template = get_template("coffee/coffee5.html")
    item = ["抹茶拿鐵","美式咖啡","義式咖啡","卡布奇諾"]
    html = template.render({"item":random.choice(item)})
    return HttpResponse(html)
