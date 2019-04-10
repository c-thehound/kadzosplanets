from django.shortcuts import render
from .models import TeamMember,WeeksTheme,KadzosTagline,Logo
from gallery.models import Image
from shop.models import Product
from stories.models import Story

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