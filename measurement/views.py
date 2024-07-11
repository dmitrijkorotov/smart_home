from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView
from .models import Measurement, Sensor
from rest_framework.views import APIView
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer
from rest_framework.response import Response


class SensorList(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetail(APIView):
    def get(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        serializer = SensorDetailSerializer(sensor)
        return Response(serializer.data)


class SensorUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorCreate(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreate(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
