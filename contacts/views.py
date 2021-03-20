from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import send_mail
from .models import Contact



def contact(request):  
  if request.method == 'POST.GET':
    listing_id = request.POST.GET['listing_id']
    listing = request.POST.GET['listing']
    name = request.POST.GET['name']
    email = request.POST.GET['email']
    phone = request.POST.GET['phone']
    message = request.POST.GET['message']
    user_id = request.POST.GET['user_id']
    realtor_email = request.POST.GET['realtor_email']

  #  Check if user has made inquiry already
    if request.user.is_authenticated:
        user_id = request.user.id
        has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
        if has_contacted:
            messages.error(request, 'You have already made an inquiry for this listing')
            return redirect('/listings/'+listing_id)

    

    contact = Contact(listing=listing,listing_id=listing_id, user_id=user_id,  name=name, email=email, phone=phone, message=message)

    contact.save()

    #send mail

    send_mail(
        'PROPERTY LISTING ENQUIRY' , 'There has been an enquiry for'+listing+'.Sign into the admin panel for more info' ,'raysujana@gmail.com' , 'password',[xyz@gmail.com , raysujana@gmail.com] ,fail_silently=False)


    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/listings/'+listing_id)
  else:
      return render(request,'accounts/dashboard.html')
#'accounts/contact.html'
