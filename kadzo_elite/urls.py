from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('entry.urls')),
    path('mail/',include('contact.urls')),
    path('martor/',include('martor.urls')),
    path('stories/',include('stories.urls')),
    path('blog/',include('blog.urls')),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
# Add media URLS
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
