from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from quickstart.models import Currency, Conversion
from quickstart.serializers import CurrencySerializer, ConversionSerializer

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class ConversionViewSet(viewsets.ModelViewSet):
    queryset = Conversion.objects.all()
    serializer_class = ConversionSerializer

# class ConvertCurrency(APIView):
#     def get(self, from_cur_str, to_cur_str, amount):
#         print("Hi")
#         from_cur = get_object_or_404(Currency, name=from_cur_str)
#         to_cur = get_object_or_404(Currency, name=to_cur_str)
#
#         conversions = Conversion.objects.filter(from_cur=from_cur)
#         conversion = get_object_or_404(conversions, to_cur=to_cur)
#
#         return Response(amount * conversion.conversion_rate)

class DecimalPathConverter:
    regex = "[0-9]+\.?[0-9]+"

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)

# class ConvertCurrency(APIView):
#     def get_object(self, from_cur_str, ):
#         print("Hi")
#         from_cur = get_object_or_404(Currency, name=from_cur_str)
#
#         return from_cur

@api_view(['GET'])
def convert_currency(request, from_cur_str, to_cur_str, amount):
    if request.method == 'GET':
        from_cur = get_object_or_404(Currency, name=from_cur_str)
        to_cur = get_object_or_404(Currency, name=to_cur_str)

        conversions = Conversion.objects.filter(from_cur=from_cur)
        conversion = get_object_or_404(conversions, to_cur=to_cur)
        print(amount)
        print(conversion.conversion_rate)
        print(amount * float(conversion.conversion_rate))
        return Response(amount * float(conversion.conversion_rate))