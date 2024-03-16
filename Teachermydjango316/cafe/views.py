from django.shortcuts import render
from django.http import HttpResponse


from django.template.loader import get_template
import random

# Create your views here.
def index(request):
    return render(request,'index.html')

def coffee(request):
    return render(request,'coffee/coffee.html')

def slogan(request):
    return HttpResponse("在忙也要陪你喝杯咖啡!!")

def history(request):
    response=HttpResponse()
    response.write("<h1>Coffee History</h1>")
    response.write("<hr>")
    response.write("<p>咖啡的來源已無從稽考。諸多傳說之一指咖啡原產於衣索比亞（Ethiopia）西南部的咖法省高原地區，據說是一位牧羊人發現羊吃了一種植物後，變得非常興奮活潑，因此發現了咖啡。</p>")
    response.write("<a href='/coffee'>咖啡品項</a>")
    return response

def coffee1(request):
    return render(request,'coffee/coffee1.html')

def coffee2(request):
    return render(request,'coffee/coffee2.html')

def coffee3(request):
    return render(request,'coffee/coffee3.html',
                  {
                      "name":"阿拉比卡","price":500,"qty":10
                  })    #字典dict

def coffee4(request):
    promo="世界咖咖節,全面買一送一"
    item={
        "name":"羅布斯塔",
        "price":450,
        "qty":10
    }
    return render(request,'coffee/coffee4.html',locals())

def coffee5(request):
    template=get_template('coffee/coffee5.html')
    item=[
        '抺茶拿鐵',
        '美式咖啡',
        '義式咖啡',
        '卡布奇諾']
    html=template.render({"item":random.choice(item)})
    return HttpResponse(html)
































def coffee6(request):
    html='''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Welcome to Cafe Time</title>
            {}
        </head>
        <body>
        <table>{}</table>            
        </body>
        </html>
    '''

    style='''
            <style>
                table{
                    width:100%;
                    border: 3px green solid;
                }

                td{
                    border: 1px gray solid;
                    text-align:center
                }
            </style>
    '''
    js="window.alert(this.innerHTML)"
    
    product=Product.objects.all()
    e="<tr><td>產品編號</td><td>產品名稱</td><td>產品價格</td><td>產品尺寸</td></tr>"
    for p in product:
        e +="<tr><td onclick={}>{}</td>".format(js,p.pid)
        e +="<td onclick={}>{}</td>".format(js,p.name)
        e +="<td>{}</td>".format(p.price)
        e +="<td>{}</td></tr>".format(p.size)
    return HttpResponse(html.format(style,e))


def tea(request):
    return render(request,'tea/tea.html')

def tea1(request):
    return render(request,'tea/tea1.html')