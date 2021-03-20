from django.shortcuts import render , redirect
from django.contrib import messages , auth
from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.


def register(request):
    if request.method== 'POST':
        #Get form values
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        #Check if pwd match

        if password == password2:
            #CHECK USERNAME
            if User.objects.filter(username=username).exists():
                messages.error(request , 'That Username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request , 'That EMAIL is taken')
                    return redirect('register')
                else:
                    #pass
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                    # auth.login(request , user)
                    # messages.success(request , 'YOU ARE LOGGED IN')
                    # return redirect('index')
                    user.save()
                    messages.success(request , 'YOU ARE NOW REGISTERED')
                    return redirect('login')



        else:
            messages.error(request , 'PASSWORDS DONT MATCH')
            return redirect('register')



       
    else:
        return render(request , 'accounts/register.html')


def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password=password)
        
        if user is not None:
            auth.login(request , user)
            messages.success(request , 'YOU ARE NOW LOGGED IN')
            return redirect('dashboard')
        
        else:
            messages.error(request , 'INVALID CREDS')
            return redirect('login')

        
    else:
        return render(request , 'accounts/login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request , "YOU ARE NOW LOGGED OUT")
        return redirect('index')


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = request.user.id)

    context = {

        'contacts' :user_contacts
    }

    return render(request , 'accounts/dashboard.html' , context)
