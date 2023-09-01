from rest_framework.generics import ListAPIView, CreateAPIView

from files.models import File
from .serializers import FileSerializer
from .tasks import render_file


class UploadFileView(CreateAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()

    def perform_create(self, serializer):
        file = serializer.save()
        render_file.delay(file_id=file.id)


class FileListView(ListAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()
