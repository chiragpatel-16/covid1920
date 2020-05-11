from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render,redirect
from.models import Developer,DistrictwiseCovid

# Create your views here.
def index(request):
     dests = Developer.objects.all()
     items= DistrictwiseCovid.objects.all()

     return render( request, 'index.html', {'dests': dests,'items':items})
def logout(request):
    auth.logout(request)
    return redirect('/')
def log(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password1']
        if (username != "" and password != ""):
            user=auth.authenticate(username=username,password=password)
            if user is not None:

               auth.login(request, user)
               return redirect('/')
            else:
                messages.info( request, 'invalid credentials' )
                return render( request, 'log.html' )
        else:
            messages.info(request,'Enter Credentials')
            return render(request,'log.html')
    else:
        return render(request,'log.html')

    ##return render(request,'index.html')
def reg(request):

    if (request.method=='POST'):
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if(first_name!='' and last_name!= '' and username!='' and email!='' and email!='' and password1!='' and password2!=''):
            if password1==password2:
                if User.objects.filter(username=username).exists():
                 messages.info(request,'Duplicate User Name')
                 return render(request,'reg.html')
                elif User.objects.filter(email=email).exists():
                 messages.info(request, 'Duplicate Email ID' )
                 return render(request, 'reg.html' )
                else:
                 user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                 user.save();

                return render(request,'log.html')
            else:
                messages.info( request, "Password is not same" )
                return render( request, 'reg.html' )
        else:
            messages.info(request,"Enter Require Data")
            return render(request,'reg.html')
    else:
         return render(request,'reg.html')
def covid(request):
    return render(request,'covidainfo.html')