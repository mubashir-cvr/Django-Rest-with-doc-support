from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer


class StudentList(generics.ListCreateAPIView):
    """Create API"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer