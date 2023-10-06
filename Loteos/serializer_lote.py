from rest_framework import serializers
from .models import Lote


# Define el serializador para el modelo Lote
class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote # Especifica el modelo que se va a serializar
        fields = '__all__' # Incluye todos los campos del modelo en la serialización
