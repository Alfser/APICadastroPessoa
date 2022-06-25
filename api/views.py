'''
 ViewSet são classes que mapeiam ações da de acordo com os métodos HTTP.
 
 autor : Janison Serra
 email : j.janilson12@gmail.com
'''

from rest_framework.viewsets import ModelViewSet

from .serializers import PersonSerializer
from .models import Person
class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

