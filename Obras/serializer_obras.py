from rest_framework import serializers
from .models import Obra


# Define un serializador para el modelo de Obra
class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra # Especifica el modelo al que se aplica este serializador
        fields = '__all__' # Incluye todos los campos del modelo en la serialización
