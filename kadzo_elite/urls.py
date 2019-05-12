from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='https://newkadzosplanets.s3.amazonaws.com/static/css/images/favicon.ico',permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('entry.urls')),
    path('contact/',include('contact.urls')),
    path('martor/',include('martor.urls')),
    path('stories/',include('stories.urls')),
    path('blog/',include('blog.urls')),
    re_path(r'^favicon\.ico$',favicon_view)
]
# urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
# Add media URLS
# urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
