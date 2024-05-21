from django.shortcuts import render , redirect, HttpResponse
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User 
from home.models import urls , visits
def loginUser(request):
    context = dict()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            context['errorMessage'] = 'Login failed. Check your username and password'
    elif request.user.is_authenticated:
        return redirect('homepage')
    return render(request,'login.html', context)

def logoutUser(request):
    if not request.user.is_authenticated:
        return redirect('homepage')
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))


def register(request):
    if request.method == "POST":
        userName = request.POST['userName']
        try:
            User.objects.get(username=userName)
            error = 'User already Exists'
            return render(request,"register.html",{'error':error})
        except:
            pass
            
        email = request.POST['email']
        password1 = request.POST['pwd']
        password2 = request.POST['confirm-pwd']
        
        if len(password1)<8:
            error="Password must be at least 8 characters"
            return render(request,"register.html",{'error':error})
        elif password1!=password2:
            error='Passwords do not match'
            return render(request,"register.html",{'error':error})
        else:
            user = User(username=userName, email=email)
            user.set_password(password1)
            user.save()
            return redirect('login')
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'register.html')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    URLs = urls.objects.filter(user_id=request.user.id)
    visitLST = [len(visits.objects.filter(url=URLs[i])) for i in range(len(URLs))]
    context = {'urls':zip(URLs,visitLST), 'n':len(URLs)}

    return render(request, 'dashboard.html' , context)

def deleteURL(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        url = urls.objects.get(id=id)
    except:
        return HttpResponse('Invalid Operation')
    if url.user_id!=request.user.id:
        return HttpResponse('Invalid Operation')
    else:
        url.delete()
        return redirect('dashboard')