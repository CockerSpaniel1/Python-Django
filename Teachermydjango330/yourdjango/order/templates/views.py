from django.shortcuts import render,redirect
from order.models import Product,UserInfo
from order.forms import UserInfoForm

# Create your views here.
def index(request):
    return render(request,'index.html')

#查看所有商品
def products(request):
    product=Product.objects.all()
    return render(request,'products.html',locals())

#註冊
def signup(request):
    if request.method=='POST':
        form=UserInfoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/signupok')
            except:
                pass
    else:
        form=UserInfoForm()
    return render(request,'signup.html',{'form':form})


#註冊ok
def signupok(request):
    userinfo=UserInfo.objects.all()
    return render(request,'signupok.html',{'userinfo':userinfo})
