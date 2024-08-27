from app.models import Population
from rest_framework import serializers

class PopulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Population
        fields = "__all__"