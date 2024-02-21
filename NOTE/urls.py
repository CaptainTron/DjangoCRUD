# notes/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    # Endpoint for listing and creating notes
    path('notes/', NoteListCreateAPIView.as_view(), name='note-list-create'),
    # Endpoint for retrieving, updating, and deleting a specific note
    path('notes/<int:pk>/', NoteRetrieveUpdateDestroyAPIView.as_view(), name='note-detail'),
    # Endpoint for creating a new note
    path('notes/create/', NoteCreate.as_view(), name='note-create'),
]