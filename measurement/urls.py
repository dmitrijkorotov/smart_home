from django.urls import path
from measurement.views import SensorCreate, MeasurementCreate, SensorUpdate, SensorDetail, SensorList

urlpatterns = [
    path('sensors/', SensorCreate.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
    path('sensors/<pk>/', SensorUpdate.as_view()),
    path('sensor/<pk>/', SensorDetail.as_view()),
    path('all_sensors/', SensorList.as_view()),
]
