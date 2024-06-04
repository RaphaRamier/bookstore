from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from publication.models import Publication
from publication.serializers import PublicationSerializer
from setup.permissions import GlobalDefaultPermission


class PublicationCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


class PublicationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    def delete(self, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return JsonResponse({'message': 'Publication deleted successfully.'}, status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
