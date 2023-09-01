from django.urls import path

from .v1.views import FileListView, UploadFileView

app_name = "api"

urlpatterns = [
    path("v1/files/", FileListView.as_view(), name="file_list"),
    path("v1/upload/", UploadFileView.as_view(), name="file_upload"),
]
