from django.shortcuts import render,redirect
from order.models import Product,UserInfo, Member

from order.forms import UserInfoForm, MemberForm, MemberLogin
# Create your views here.
def index(request):
    status =request.session.get("is_login")
    uname =request.session.get("uname")
    return render(request, "index.html", locals())

def products(request):
    product = Product.objects.all()
    return render(request, "products.html",locals())

def signup(request):
    if request.method =="POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('signupok')
            except:
                pass
    else:
        form =UserInfoForm()
    return render(request, "signup.html", {"form":form})

def signupok(request):
    userinfo = UserInfo.objects.all()
    return render(request,'signupok.html',{'userinfo':userinfo})

'''
def register(request):
    member =Member.objects.all()
    form = MemberForm(request.POST)
    if request.method =="POST":
        #form = UserInfoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                request.session['is_login'] = True
                request.session['email'] = form.cleaned_data['email']
                request.session['pwd'] = form.cleaned_data['pwd']
                request.session['uname'] = form.cleaned_data['uname']
                return redirect('/member')
            except:
                pass
                return redirect('/register')
    else:
        form =MemberForm()

    context ={
        "member":member,
        "form":form
    }
    return render(request, "register.html", context)
'''

#方法2
def register(request):
    #print("test1")
    member =Member.objects.all()
    form = MemberForm(request.POST)
    if request.method =="POST":
        #print("test2")
        if form.is_valid():
            #print("test3")
            try:
                #print("test4")
                form.save()
                #print("test4.5")
                email = form.cleaned_data['email']
                result = Member.objects.get(email = email)
                request.session['is_login'] = True
                request.session['email'] = result.email
                request.session['pwd'] =  result.pwd
                request.session['uname'] = result.uname
                return redirect('/member')
            except:
                print("test5")
                pass
                return redirect('/register')
    else:
        print("test6")
        form =MemberForm()

    context ={
        "member":member,
        "form":form
    }
    return render(request, "register.html", context)

def member(request):
    status =request.session.get("is_login")
    email =request.session.get("email")
    pwd =request.session.get("pwd")
    uname =request.session.get("uname")
    if not status:
        return redirect("/")
    
    return render(request, "member.html", locals())

def logout(request):
    request.session.flush()
    return redirect("/")


def login(request):
    member =Member.objects.all()
    form = MemberForm(request.POST)
    if request.method =="POST":
        if form.is_valid():
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['pwd']
            memberobj = Member.objects.filter(email = email, pwd = pwd).first()
            if not memberobj:
                return redirect('/login')
            
            else:
                request.session['is_login'] = True
                request.session['email'] = memberobj.email
                request.session['pwd'] =  memberobj.pwd
                request.session['uname'] = memberobj.uname

                return redirect('/member')        
    else:
        form =MemberLogin()

    context ={
        "member":member,
        "form":form
    }
    return render(request, "login.html", context)