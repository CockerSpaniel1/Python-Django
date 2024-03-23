from django.shortcuts import render,redirect
from django.http import HttpResponse


from django.template.loader import get_template
import random
from cafe.models import Product,Category,UserInfo
from datetime import datetime

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
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>SQLite Products</title>
            {}
        </head>
        <body>
            <h1>所有產品資訊</h1>
            <hr>
            <h3>產品項目</h3>
            <table>
                {}
            </table>  
        </body>
        </html>
        '''

    style='''
        <style>
        table{
            width: 100%;
            border: 1.25rem green solid;        
            border-collapse:collapse;    
        }

        td{
            border: 0.05rem gold solid;            
            padding:0.5em;
            
        }
         </style>
        '''
    
    js="window.alert(this.innerHTML)"

    product=Product.objects.all()   #取得Product的所有物件
    e="<tr><td>產品編號</td><td>產品名稱</td><td>產品價格</td><td>產品尺寸</td></tr>"

    for p in product:
        e += "<tr><td onclick={}>{}</td>".format(js,p.pid)
        e += "<td>{}</td>".format(p.name)
        e += "<td>{}</td>".format(p.price)
        e += "<td>{}</td></tr>".format(p.size)
    return HttpResponse(html.format(style,e))

def coffee7(request):
    html='''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>SQLite Categorys</title>
            {}
        </head>
        <body>
            <h1>所有類別資訊</h1>
            <hr>
            <h3>類別項目</h3>
            <table>
                {}
            </table>  
        </body>
        </html>
    '''

    style='''
         <style>
        table{
            width: 100%;
            border: 1.25rem green solid;        
            border-collapse:collapse;    
        }

        td{
            border: 0.05rem gold solid;            
            padding:0.5em;            
        }
         </style>
        '''
    
    js="window.alert(this.innerHTML)"

    category=Category.objects.all()   #取得Category的所有物件
    e="<tr><td>類別編號</td><td>類別名稱</td></tr>"

    for c in category:
        e += "<tr><td onclick={}>{}</td>".format(js,c.cid)
        e += "<td>{}</td></tr>".format(c.name)       
    return HttpResponse(html.format(style,e))


def coffee8(request):
    product=Product.objects.all()
    template=get_template('coffee/coffee8.html')
    html=template.render({"product":product})
    return HttpResponse(html)

def coffee9(request,pid):
    p=Product.objects.get(pid=pid)
    template=get_template('coffee/coffee9.html')
    html=template.render({"product":p})
    return HttpResponse(html)

def coffee10(request):
    return render(request,'coffee/coffee10.html')


def coffee11(request):
    coffee=[
        {'image':'arabica.png',
         'name':'阿拉比卡咖啡(Arabica coffee) 原產於東非伊索比亞南部的阿比西 尼亞高原，現今沿海尚有野生種。'},

         {'image':'robusta.png',
         'name':'羅布斯塔咖啡(Robusta coffee) 羅布斯塔咖啡屬於剛果咖啡的突變 種，原產於西非剛果，本種有缺乏香氣之 憾，苦味較強，酸味不足。'},

         {'image':'liberia.png',
         'name':'利比亞咖啡(Liberia coffee) 原產於西非利比亞，本種香味不佳， 苦味較強。除少數生產國自己消費外，只 有歐洲人飲用利比亞咖啡。'}
    ]

    now=datetime.now()  #取得目前時間
    hour=now.timetuple().tm_hour
    template=get_template('coffee/coffee11.html')
    html=template.render(locals())
    return HttpResponse(html)

def mycookie1(request):
    template=get_template('cookie/mycookie1.html')

    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        message="support cookie!!"
    else:
        message="not support cookie!!"

    request.session.set_test_cookie()
    html=template.render(locals())
    return HttpResponse(html)    

#登入的使用者介面驗證
def mycookie2(request):
    if request.method=='GET':
        return render(request,'cookie/mycookie2.html')
    
    username=request.POST.get('username')   #表單欄位名稱
    password=request.POST.get('password')

    userobj=UserInfo.objects.filter(
        username=username,password=password).first()    # 判斷資料庫是否有此使用者
    
    if not userobj:
        return redirect('/mycookie2/')
    else:
        myredirect=redirect('/mycookie3/')
        myredirect.set_cookie('is_login',True)
        myredirect.set_cookie('username',username)
        myredirect.set_cookie('password',password)
        return myredirect

#登入的函數    
def mycookie3(request):
    status=request.COOKIES.get('is_login')
    username=request.COOKIES.get('username')
    password=request.COOKIES.get('password')

    if not status:
        return redirect('/mycookie2/')
    return render(request,'cookie/mycookie3.html',locals())

#登出的函數
def mycookie4(request):
    myredirect=redirect('/mycookie2')
    myredirect.delete_cookie('is_login')
    myredirect.delete_cookie('username')
    myredirect.delete_cookie('password')
    return myredirect





























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