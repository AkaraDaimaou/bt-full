from django.urls import path
from .views import course_details, Teacher_list, SchoolFacilityList, LaboratoryList

urlpatterns = [
    path('course/<int:course_id>/', course_details, name='course_details'),
    path('teachers/', Teacher_list.as_view(), name='teacher_list'),
]