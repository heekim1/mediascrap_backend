from django.urls import path

from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('profiles', views.ProfileViewSet)

urlpatterns = router.urls


"""
urlpatterns = [
    path('profiles/', views.profile_list),
    path('profiles/<int:id>/', views.channel_info_detail)
]
"""