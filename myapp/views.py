from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets
from . import models

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DateTimeModel
        fields = '__all__'

class TestViewSet(viewsets.ModelViewSet):
    queryset = models.DateTimeModel.objects.all()
    serializer_class = TestSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = {
        'created': ('exact', 'lt', 'gt', 'lte', 'gte'),
    }
