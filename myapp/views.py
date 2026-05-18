from django.shortcuts import render,HttpResponse,redirect
from .forms import *
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
def home(request):
    c=Course_form()
    if request.method=='POST':
        form=Course_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # return render(request,'data.html') 
    return render(request,'form.html',{'form':c}) 
def getdata(request):
    data=Course.objects.all()
    return render(request,'welcome.html',{'data':data}) 

@login_required(login_url='login')
def course_view(request):
    data=Course.objects.all()
    return render(request,'course_view.html',{'data':data})

def register(request):
    r=Registrationform()
    if request.method=='POST':
        form=Registrationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'register.html',{'data':r})

def login_view(request):
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('course')
            else:
                return render(request, 'login.html', {
                    'error': 'Invalid username or password'
                })
    else:
        form = Loginform()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('getdata')

@login_required(login_url='login')
def profile(request):
   user=request.user
   return render(request,'profile.html',{'user':user})

@login_required(login_url='login')
def AddToCart(request,id):
    course=Course.objects.get(id=id)
    cartitem,created=Cart.objects.get_or_create(user=request.user,courses=course)
    cartitem.quantity+=1
    cartitem.save()
    return redirect('cart')

@login_required(login_url='login')
def Cart_view(request):
    data=Cart.objects.all()
    total=sum(i.courses.c_price*i.quantity for i in data)
    return render(request,'cart.html',{'data':data,'total':total})

def Cart_remove(request,id):
    data=Cart.objects.get(id=id)
    if data.quantity>1:
        data.quantity-=1
        data.save()
    else:
        data.delete()
    return redirect('cart')

def Cart_delete(request,id):
    data=Cart.objects.get(id=id)
    data.delete()
    return redirect('cart')

def search_bar(request):
    data=request.GET['searchbar']
    course=Course.objects.filter(c_name__icontains=data)
    return render(request,'search.html',{'course':course}) 