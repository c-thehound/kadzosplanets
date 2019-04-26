from django.shortcuts import render,redirect
from .models import Subscriber
from entry.models import Message

def subscribe_to_mail(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            new = Subscriber.objects.create(
                email = email
            )
            new.save()

            return redirect('/',success="Successfully added you to our mailing list")
        except:
            return redirect('/',error="Could not add you to our mailing list")
    return redirect('/')
    
def message(request):
     email = request.POST.get('email')
     message = request.POST.get('message')

     try:
          mes = Message.objects.create(
               email = email,
               message = message
          )
          mes.save()
          return redirect('/',success="Successfully added you to our mailing list")
     except:
          return redirect('/',error="Could not add you to our mailing list")
     return redirect('/')