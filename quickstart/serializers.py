from django.contrib.auth.models import Group, User
from rest_framework import serializers

from quickstart.models import Currency, Conversion


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = [
            'name',
            'symbol'
        ]

class ConversionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conversion
        fields = [
            'from_cur',
            'to_cur',
            'conversion_rate'
        ]