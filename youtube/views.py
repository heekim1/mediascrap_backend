from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django.http import JsonResponse, HttpResponseNotFound
from .mongodb import ChannelInfo, ChannelStats

class ChannelInfoList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        channel_info = ChannelInfo()
        documents = channel_info.get_documents()
        return Response({'documents': documents})

class ChannelInfoDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        channel_info = ChannelInfo()
        document = channel_info.collection.find_one({'_id': id})

        if document:
            return Response(document)
        else:
            return Response({"detail": "Document not found"}, status=404)
        

class ChannelStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        channel_stats = ChannelStats()
        stats = channel_stats.get_documents({'channel_id': id})
        return Response(stats)

"""
def channel_info_list(request):
    # Instantiate your MongoDB class
    channel_info = ChannelInfo()
    documents = channel_info.get_documents()
    return JsonResponse({'documents': documents}, safe=False)

def channel_info_detail(request, id):
    # Instantiate your MongoDB class
    channel_info = ChannelInfo()
    document = channel_info.collection.find_one({'_id': id})

    if document:
        # Successfully found the document
        return JsonResponse(document, safe=False)
    else:
        # Document not found
        return HttpResponseNotFound("Document not found")

def channel_stats(request, id):
    channel_stats = ChannelStats()
    stats = channel_stats.get_documents({'channel_id':id})

    return JsonResponse(stats, safe=False)
"""