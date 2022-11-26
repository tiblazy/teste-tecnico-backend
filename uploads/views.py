from rest_framework.generics import ListCreateAPIView

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer

from .serializers import UploadSerializer
from .mixins import SerializerByMethodMixin
from .utils import normalize_file_txt, filter_store


class UploadView(SerializerByMethodMixin, ListCreateAPIView):
    serializer_map = {
        "GET": TransactionSerializer,
        "POST": UploadSerializer,
    }

    def get_queryset(self):
        store = filter_store(Transaction.objects.all())
        return store

    def perform_create(self, _):
        uploaded_file = self.request.FILES["file_uploaded"]
        normalize_file_txt(uploaded_file)
