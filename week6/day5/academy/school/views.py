from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Teacher, Course
from .serializers import TeacherSerializer


class TeacherList(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    


    def course_details(request, id):
        course = get_object_or_404(Course, id=id)
        return JsonResponse({'course_name': course.course_name, 'course_code': course.course_code})


