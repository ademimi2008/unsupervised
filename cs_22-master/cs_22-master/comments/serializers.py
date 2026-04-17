from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    account_name = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'text', 'account_name']

    def get_account_name(self, obj):
        return obj.account.name
