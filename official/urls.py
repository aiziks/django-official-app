
from  django.urls import path , include
from rest_framework import routers
from .views import SubViewSet , ContactUs


router = routers.DefaultRouter()

router.register('subscribe' , SubViewSet , 'subscribe')


urlpatterns = [
    path('contact/' , ContactUs.as_view() ),
    path('' , include(router.urls)) 

]