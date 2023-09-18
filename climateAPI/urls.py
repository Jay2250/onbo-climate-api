from django.urls import path
from .views import ClimateRecordListCreateView, ClimateRecordDetailView, ClimateChangeIndexView

urlpatterns = [
    path('save/', ClimateRecordListCreateView.as_view(), name='save_climate_record'),
    path('records/', ClimateRecordListCreateView.as_view(), name='get_all_records'),
    path('records/<int:area_code>/<str:climate>/', ClimateRecordDetailView.as_view(), name='get_records_by_area_and_climate'),
    path('climate_change_index/', ClimateChangeIndexView.as_view(), name='climate_change_index'),
]
