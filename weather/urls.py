from django.urls import path

from . import views

urlpatterns = [
    path('forecast/week/', views.forecast_week, name='forecast_week'),
    path('forecast/week/alert/', views.forecast_week_alert, name='forecast_week_alert'),
    path('forecast/month/', views.forecast_month, name='forecast_month'),
    path('forecast/month/alert/', views.forecast_month_alert, name='forecast_month_alert'),
    path('forecast/', views.forecast, name='forecast'),
    path('forecast/alert/', views.forecast_alert, name='forecast_alert'),
    path('comparison/', views.comparison, name='comparison'),
    path('comparison/alt/', views.comparison_alt, name='comparison_alt'),
    path('comparison/alert/', views.comparison_alert, name='comparison_alert'),
    path('', views.index, name='index'),
]