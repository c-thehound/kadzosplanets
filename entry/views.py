from django.shortcuts import render,redirect
from .models import TeamMember,WeeksTheme,KadzosTagline,Logo,Message
from gallery.models import Image
from shop.models import Product
from stories.models import Story

#Martor
import json
import uuid
import os
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from martor.utils import LazyEncoder

# Blog
from blog.models import BlogPost

def landing(request):
    team = TeamMember.objects.all()
    gallery = Image.objects.all()
    shop = Product.objects.all()
    stories = Story.objects.all()
    active = "landing"
    try:
         logo = Logo.objects.latest('pk')
    except:
         logo = {"image":"No image"}
    try:
         theme = WeeksTheme.objects.latest('pk')
    except:
         theme = {"text":"No theme set","message":"No message set"}
    try:
         tagline = KadzosTagline.objects.latest('pk')
    except:
         tagline = {"text":"Not Tagline set"}

    return render(request,'landing.html',{
         "team":team,
         "gallery":gallery,
         "shop":shop,
         "stories":stories,
         "theme":theme,
         "tagline":tagline,
         "logo":logo,
         "active":active
         })

def blog(request):

    blogposts = BlogPost.objects.all()
    try:
         logo = Logo.objects.latest('pk')
    except:
         logo = {"image":"No image"}

    active = "blog"
    return render(request,'blog.html',{
          "blogposts":blogposts,
          "logo":logo,
          "active":active
     })

def message(request):
     email = request.data.get('email')
     message = request.data.get('message')

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

def acme_challenge(request):
    return HttpResponse(settings.ACME_CHALLENGE_CONTENT)

@login_required
def markdown_uploader(request):
    if request.method == 'POST' and request.is_ajax():
        if 'markdown-image-upload' in request.FILES:
            image = request.FILES['markdown-image-upload']
            image_types = [
                    'image/png','image/jpg','image/jpeg','image/pjpeg','image/gif'
                    ]
            if image.content_type not in image_types:
                data = json.dumps({
                    'status':405,
                    'error':_('Bad image format.')
                    },cls=LazyEncoder)
                return HttpResponse(data,content_type='application/json')
    
            if image.size > settings.MAX_IMAGE_UPLOAD_SIZE:
                to_MB = settings.MAX_IMAGE_UPLOAD_SIZE/(1024*1024)
                data = json.dumps({
                    'status':405,
                    'error':_('Maximum image file is %(size) MB.') % {'size':to_MB}
                    },cls=LazyEncoder)
                return HttpResponse(data,content_type='application/json',status=405)
    
            img_uuid = "{0}-{1}".format(uuid.uuid4().hex[:10],image.name.replace(' ','-'))
            tmp_file = os.path.join(settings.MARTOR_UPLOAD_PATH,img_uuid)
            def_path = default_storage.save(tmp_file,ContentFile(image.read()))
            img_url = os.path.join(settings.MEDIA_URL,def_path)
    
            data = json.dumps({
                'status':200,
                'link':img_url,
                'name':image.name
                })
    
            return HttpResponse(data,content_type='application/json')
        return HttpResponse(_('Invalid request!'))
    return HttpResponse(_('Invalid request!'))



