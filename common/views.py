from django.shortcuts import render,redirect
from .models import User

# Create your views here.
def commonhome(request):
    return render(request,'commonhome.html')
    
def agency_login(request):
    return render(request,'agency_login.html')

def traveller_login(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(email = username, password = password)
            request.session['user'] = user.id
            return redirect('common:commonhome')
        except:
            msg = 'incorrect email or password'
    return render(request,'traveller_login.html',{'msg': msg})

def agency_reg(request):
    return render(request,'agency_reg.html')

def traveller_reg(request):
    msg = ''
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']

        user = User(first_name = first_name, last_name = last_name, email = email, 
        phone = phone, password = password)
        user.save()

        msg = 'registered successfully'

    return render(request,'traveller_reg.html',{'msg':msg})