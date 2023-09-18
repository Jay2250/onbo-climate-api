from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Avg
from .models import ClimateRecord
from .serializers import ClimateRecordSerializer

class ClimateRecordListCreateView(APIView):
    def post(self, request, format=None):
        serializer = ClimateRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'error': None, 'data': {'id': serializer.data['id']}}, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'error': serializer.errors, 'data': None}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        climate_records = ClimateRecord.objects.all()
        serializer = ClimateRecordSerializer(climate_records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ClimateRecordDetailView(APIView):
    def get_object(self, area_code, climate):
        return get_object_or_404(ClimateRecord, area_code=area_code, climate=climate)

    def get(self, request, area_code, climate, format=None):
        record = self.get_object(area_code, climate)
        serializer = ClimateRecordSerializer(record)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ClimateChangeIndexView(APIView):
    def post(self, request, format=None):
        # Your calculation logic for climate change index
        # ...

        response_data = {
            'climate_delta': f"{request.data['from_climate']} -> {request.data['to_climate']}",
            'temperature_delta': -67,  # Replace with actual calculation
            'humidity_delta': 79,  # Replace with actual calculation
            'rain_chances_delta': 20,  # Replace with actual calculation
            'climate_change_index': "(delta Temp * delta Humidity) / delta rain_chances",  # Replace with actual calculation
        }

        return Response(response_data, status=status.HTTP_200_OK)
