from django.urls import path
from .views import ChannelInfoList, ChannelInfoDetail, ChannelStatsView

urlpatterns = [
    path('channels/', ChannelInfoList.as_view(), name='channel-info-list'),
    path('channels/<str:id>/', ChannelInfoDetail.as_view(), name='channel-info-detail'),
    path('channels/<str:id>/stats', ChannelStatsView.as_view(), name='channel-stat'),
]