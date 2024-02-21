# notes/serializers.py

from rest_framework import serializers
from .models import NOTE

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NOTE
        fields = '__all__'
