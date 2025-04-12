from django.urls import include, path, re_path, register_converter
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from quickstart import views
from quickstart.views import convert_currency, DecimalPathConverter

router = routers.DefaultRouter()
router.register(r'currency', views.CurrencyViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

register_converter(DecimalPathConverter, "decimal")

urlpatterns = [
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('conversion/<str:from_cur_str>/<str:to_cur_str>/<decimal:amount>/', views.convert_currency),
    path('conversion/<str:from_cur_str>/<str:to_cur_str>/<int:amount>/', views.convert_currency)
]
