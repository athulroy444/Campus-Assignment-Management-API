from rest_framework import generics, viewsets, permissions, status
from rest_framework.response import Response
from .models import Student, Assignment
from .serializers import StudentSerializer, AssignmentSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterView(generics.CreateAPIView):
    queryset = Student.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = StudentSerializer

class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # A student should only be able to access their own assignments
        return Assignment.objects.filter(student=self.request.user)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)
