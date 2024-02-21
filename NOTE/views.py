# notes/views.py

# notes/views.py

from rest_framework import generics
from .models import NOTE
from .serializers import NoteSerializer

class NoteListCreateAPIView(generics.ListCreateAPIView):
    print("GETTING ALL OF THEM")
    queryset = NOTE.objects.all()
    serializer_class = NoteSerializer

class NoteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = NOTE.objects.all()
  serializer_class = NoteSerializer

class NoteCreate(generics.CreateAPIView):
    print("GETTING ALL OF THEM")
    queryset = NOTE.objects.all()
    serializer_class = NoteSerializer