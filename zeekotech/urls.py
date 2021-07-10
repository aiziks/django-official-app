
from django.contrib import admin
from django.urls import path , include
from django.views.generic import  TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('' , TemplateView.as_view(template_name='index.html') ),
    path('api/' , include('official.urls')),
    path('admin/', admin.site.urls),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
#change this on production