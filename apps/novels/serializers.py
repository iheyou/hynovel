from rest_framework import serializers

from novels.models import Novel


class NovelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Novel
        fields = "__all__"