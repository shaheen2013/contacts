from django.shortcuts import render
from rest_framework import generics
from contact import seriralizers, models
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1000
    
class ContactAPIView(generics.ListAPIView):
       serializer_class = seriralizers.ContactSerializer
       queryset = models.Contact.objects.all()
       filter_backends = [SearchFilter]
       pagination_class = StandardResultsSetPagination
       search_fields = ['phone']
       
       
class CountryContactAPIView(generics.ListAPIView):
       serializer_class = seriralizers.ContactSerializer
       queryset = models.Contact.objects.all()
       lookup_field = 'country'
       pagination_class = StandardResultsSetPagination
       filter_backends = [SearchFilter]
       search_fields = ['phone']
       
       def get_queryset(self):
              country = self.kwargs.get('country', None)
              return models.Contact.objects.filter(country__name=country)
       