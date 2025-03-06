from rest_framework import serializers

class CoverageReadSerializer(serializers.Serializer):
    company_coverage = serializers.DictField(child=serializers.BooleanField())