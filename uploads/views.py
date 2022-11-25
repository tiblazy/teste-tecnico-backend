from rest_framework.generics import ListCreateAPIView

from .serializers import UploadSerializer
from .utils import normalize_file_txt


class UploadView(ListCreateAPIView):
    serializer_class = UploadSerializer

    def perform_create(self, _):
        uploaded_file = self.request.FILES["file_uploaded"]
        normalize_file_txt(uploaded_file)
