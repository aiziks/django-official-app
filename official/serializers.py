from rest_framework import serializers
from .models import Subscription
from rest_framework.validators import UniqueValidator
 

class SubSerializer(serializers.ModelSerializer):

      # validating the uniqueness of email addresses
      email = serializers.EmailField(required=True,
        validators=[UniqueValidator(queryset=Subscription.objects.all())]
         )
      class Meta:
         model = Subscription
         fields = '__all__'



#contact us serializer
class ContactUsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField(min_length=2)
    subject = serializers.CharField(max_length=200)
    message = serializers.CharField(max_length=1000)
    

    class Meta:
        fields = ['name','email','subject' , 'message']
        