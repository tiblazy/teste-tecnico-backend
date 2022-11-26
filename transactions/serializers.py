from rest_framework import serializers

from .models import Transaction

from uploads.utils import transactions_store, calculate_store_currency


class TransactionSerializer(serializers.ModelSerializer):
    transactions = serializers.SerializerMethodField()
    currency = serializers.SerializerMethodField()
    class Meta:
        model = Transaction
        fields = ["store", "currency", "transactions"]

    def get_transactions(self, store):
        return transactions_store(store)
    
    def get_currency(self, store):
        return calculate_store_currency(store)
