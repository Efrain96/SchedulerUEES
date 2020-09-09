# Import urls module
from django.urls import path

from main.views import logout, login, DeleteSchedulerView, change_state, DetailSchedulerView
from main.views.classroom import ClassroomViewSet
from main.views.scheduler import SchedulerListView, create_scheduler, edit_scheduler

from main.views.teacher import TeacherListView, TeacherDeleteView, TeacherViewSet
from main.views.career import CareerViewSet
from main.views.subject import SubjectListView, SubjectViewSet

app_name = 'main'

# API Views
# Teachers
teachers_list = TeacherViewSet.as_view({
    'get': 'list'
})
teachers_detail = TeacherViewSet.as_view({
    'get': 'retrieve'
})
# Subject
subjects_list = SubjectViewSet.as_view({
    'get': 'list'
})
subject_detail = SubjectViewSet.as_view({
    'get': 'retrieve'
})
# Career
careers_list = CareerViewSet.as_view({
    'get': 'list'
})
career_detail = CareerViewSet.as_view({
    'get': 'retrieve'
})
# Classroom
classroom_list = ClassroomViewSet.as_view({
    "get": "list"
})
classroom_detail = ClassroomViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    # Planning
    path('', SchedulerListView.as_view(), name='list-scheduler'),
    path('planificaciones/crear/', create_scheduler, name='add-scheduler'),
    path('planificaciones/detalle/<int:pk>/', DetailSchedulerView.as_view(), name='detail-scheduler'),
    path('planificaciones/editar/<int:id>/', edit_scheduler, name='edit-scheduler'),
    path('planificaciones/eliminar/<int:pk>/', DeleteSchedulerView.as_view(), name='delete-scheduler'),
    path('planificaciones/verificar/', change_state, name='verified-scheduler'),

    # Teachers
    path('profesores/', TeacherListView.as_view(), name='list-teachers'),
    path('profesores/eliminar/<int:pk>', TeacherDeleteView.as_view(), name='delete-teachers'),

    # Subjects
    path('materias/', SubjectListView.as_view(), name='list-subjects'),

    # API
    # Carreras
    path('api/v1/careers/', careers_list, name='api-careers'),
    path('api/v1/careers/<int:pk>/', career_detail, name='api-careers-detail'),
    # Profesores
    path('api/v1/teachers/', teachers_list, name='api-teachers'),
    path('api/v1/teachers/<int:pk>/', teachers_list, name='api-teachers-detail'),
    # Materias
    path('api/v1/subjects/', subjects_list, name='api-subjects'),
    path('api/v1/subjects/<int:pk>/', subject_detail, name='api-subjects-detail'),
    # Aulas
    path('api/v1/classroom/', classroom_list, name='api-classroom'),
    path('api/v1/classroom/<int:pk>/', classroom_detail, name='api-classroom-detail'),

    # Account user
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
]
