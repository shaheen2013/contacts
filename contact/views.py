from django.shortcuts import render
from rest_framework import generics
from contact import seriralizers, models
from rest_framework.filters import SearchFilter

class ContactAPIView(generics.ListAPIView):
       serializer_class = seriralizers.ContactSerializer
       queryset = models.Contact.objects.all()
       filter_backends = [SearchFilter]
       search_fields = ['phone']
       
       
class CountryContactAPIView(generics.ListAPIView):
       serializer_class = seriralizers.ContactSerializer
       queryset = models.Contact.objects.all()
       lookup_field = 'country'
       filter_backends = [SearchFilter]
       search_fields = ['phone']
       
       def get_queryset(self):
              country = self.kwargs.get('country', None)
              return models.Contact.objects.filter(country__name=country)
       