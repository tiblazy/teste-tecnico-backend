from rest_framework.generics import ListCreateAPIView

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer

from .serializers import UploadSerializer
from .mixins import SerializerByMethodMixin
from .utils import normalize_file_txt


class UploadView(SerializerByMethodMixin, ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_map = {
        "GET": TransactionSerializer,
        "POST": UploadSerializer,
    }

    def perform_create(self, _):
        uploaded_file = self.request.FILES["file_uploaded"]
        normalize_file_txt(uploaded_file)
