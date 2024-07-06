from django.shortcuts import render,redirect
from order.models import Product,UserInfo,Member
from order.forms import UserInfoForm,MemberForm,MemberLogin

# Create your views here.
def index(request):
    status=request.session.get('is_login')
    uname=request.session.get('uname')
    return render(request,'index.html',locals())

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

#會員註冊,方法1
'''
def register(request):
    member=Member.objects.all()
    form=MemberForm(request.POST)
    if request.method=='POST':
        #form=MemberForm(request.POST)
        if form.is_valid(): #如果為有效的
            try:
                form.save()
                request.session['is_login']=True
                request.session['email']=form.cleaned_data['email']
                request.session['pwd']=form.cleaned_data['pwd']
                request.session['uname']=form.cleaned_data['uname']
                return redirect('/member')
            except:
                pass
                return redirect('/register/')
    else:
        form=MemberForm()
    context={
        'member':member,
        'form':form,
    }
    return render(request,'register.html',context)
'''

#會員註冊,方法2
def register(request):
    member=Member.objects.all()
    form=MemberForm(request.POST)
    if request.method=='POST':
        #form=MemberForm(request.POST)
        if form.is_valid(): #如果為有效的
            try:
                form.save()
                email=form.cleaned_data['email']
                result=Member.objects.get(email=email)
                request.session['is_login']=True
                request.session['email']=result.email
                request.session['pwd']=result.pwd
                request.session['uname']=result.uname
                return redirect('/member')
            except:
                pass
                return redirect('/register/')
    else:
        form=MemberForm()
    context={
        'member':member,
        'form':form,
    }
    return render(request,'register.html',context)


#會員註冊OK
def member(request):
    status=request.session.get('is_login')
    email=request.session.get('email')
    pwd=request.session.get('pwd')
    uname=request.session.get('uname')
    if not status:
        return redirect('/')
    return render(request,'member.html',locals())

#會員登出
def logout(request):
    request.session.flush()
    return redirect('/')

#會貝登入函數與登入OK
def login(request):
    member=Member.objects.all()
    form=MemberLogin(request.POST)
    if request.method=='POST':
        #form=MemberForm(request.POST)
        if form.is_valid(): #如果為有效的
            email=form.cleaned_data['email']
            pwd=form.cleaned_data['pwd']
            memberobj=Member.objects.filter(email=email,pwd=pwd).first()#判斷資料庫是否有此記錄
            if not memberobj:
                return redirect('/login')
            else:
                request.session['is_login']=True
                request.session['email']=memberobj.email
                request.session['pwd']=memberobj.pwd
                request.session['uname']=memberobj.uname
                return redirect('/member')           
    else:
        form=MemberLogin()
    context={
        'member':member,
        'form':form,
    }
    return render(request,'login.html',context)

#會員更新
def update(request,email):
    status=request.session.get('is_login')
    if status:
        member=Member.objects.get(email=email)
        form=MemberForm(instance=member)
        if request.method=='POST':
            form=MemberForm(request.POST,instance=member)
            if form.is_valid():
                try:
                    form.save()
                    request.session['is_login']=True
                    request.session['email']=member.email
                    request.session['pwd']=member.pwd
                    request.session['uname']=member.uname
                    return redirect('/updateok')
                except:
                    pass
        context={
            'member':member,
            'form':form
        }
        return render(request,'update.html',context)
    else:
        redirect('/')

#更新會員資料OK
def updateok(request):
    status=request.session.get('is_login')
    email=request.session.get('email')
    pwd=request.session.get('pwd')
    uname=request.session.get('uname')
    if not status:
        return redirect('/')
    return render(request,'updateok.html',locals())

#刪除會員資料
def delete(request,email):
    status=request.session.get('is_login')
    if not status:
        return redirect('/')    
    member=Member.objects.get(email=email)
    member.delete()
    logout(request)
    return render(request,'index.html',{'deflag':True})
