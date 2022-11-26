from rest_framework import serializers

from .models import Transaction

from uploads.utils import calculate_store_currency


class TransactionSerializer(serializers.ModelSerializer):
    currency = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = ["store", "currency"]

    def get_currency(self, store):
        return calculate_store_currency(store)
