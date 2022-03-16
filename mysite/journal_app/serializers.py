from rest_framework import serializers
from .models import journal



class journalSerializer(serializers.ModelSerializer):
    class Meta:
        model = journal
        fields = ('id', 'title', 'url', 'notes', 'technologies', 'technologiesList')
