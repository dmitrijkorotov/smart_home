from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView, RetrieveAPIView
from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer


class SensorList(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetail(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorCreate(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreate(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
