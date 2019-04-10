from django.shortcuts import render,redirect
from .models import Subscriber

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
    