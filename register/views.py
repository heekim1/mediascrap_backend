from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Profile
from .serializers import ProfileSerializer
from .permissions import FullDjangoModelPermissions, IsAdminOrReadOnly, ViewProfileHistoryPermission

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]

    """
    if you allows authenticated user to read other user's profile
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]
    """

    @action(detail=True, permission_classes=[ViewProfileHistoryPermission])
    def history(self, request, pk):
        return Response('ok')

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        profile = Profile.objects.get(user_id=request.user.id)
        if request.method == 'GET':
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = ProfileSerializer(profile, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

"""
@api_view()
def profile_list(request):
    return Response('ok')

@api_view()
def profile_detail(request, id):
    try:
        return Response(id)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)
"""