from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import UserCollectNovels


class UserCollectionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = UserCollectNovels
        validators = [
            UniqueTogetherValidator(
                queryset = UserCollectNovels.objects.all(),
                fields = ('user', 'novel'),
                message= '已经收藏'
            )
        ]
        fields = ('user', 'novel', 'id')
