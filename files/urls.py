# Import urls module
from django.urls import path

from files.views import IbmPlanListView, generate_document

app_name = 'files'
urlpatterns = [
    path('ibm/planificaciones/', IbmPlanListView.as_view(), name='list-ibm'),
    path('ibm/planificaciones/document/', generate_document, name='generate-ibm'),
]
