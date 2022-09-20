from rest_framework import serializers
from contact.models import *

class CountrySerializer(serializers.ModelSerializer):
       
       class Meta:
              model = Country
              fields = '__all__'
              
class ContactSerializer(serializers.ModelSerializer):
       country = CountrySerializer(read_only=True, many=False)
       class Meta:
              model = Contact
              fields = ['id', 'phone', 'country']
              
              
