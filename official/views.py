from django.shortcuts import render
from .serializers import SubSerializer 
from .models import Subscription
from rest_framework import viewsets , permissions
from rest_framework import generics
from .utils import Util
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .serializers import ContactUsSerializer


class SubViewSet(viewsets.ModelViewSet ) :
    queryset = Subscription.objects.all()
    serializer_class = SubSerializer
    permission_classes = [permissions.AllowAny]
        
    

    def perform_create(self  , serializer):
        
       print(serializer.is_valid())
       print(serializer.validated_data)
       # serializer.save(owner = self.request.user)
       serializer.save()



#contact us
class ContactUs(generics.GenericAPIView):
    serializer_class = ContactUsSerializer

    def  post(self, request , *args , **kwargs):
        print(request.data)

        # hideval = request.data['shopped']
        # # print(hideval)
        # if   hideval != "shopit" :
        #     raise AuthenticationFailed('Invalid Data')


        
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        print(serializer.validated_data['email'])

        name = serializer.validated_data['name']
        email = serializer.validated_data['email']
        subject  = serializer.validated_data['subject']
        message = serializer.validated_data['message']
           

        email_body = 'Name: '+ name +'\nemail: '+ email +'\nmessage: '+ message 
        data = {'email_body' : email_body , 'email_subject':subject , 'to_email':'adedayoaiziks@gmail.com'} 

        Util.send_email(data)
       
        

        return Response({'message':'Message Sent Successfully'} , status = status.HTTP_200_OK)
        
