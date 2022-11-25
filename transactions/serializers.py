from rest_framework import serializers

from .models import Transaction
from .utils import calculate_store_currency


class TransactionSerializer(serializers.ModelSerializer):
    currency = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = ["store", "currency"]

        extra_kwargs = {
            "type": {"write_only": True},
            "value": {"write_only": True},
        }

    def get_currency(self, store):
        return calculate_store_currency(store)
