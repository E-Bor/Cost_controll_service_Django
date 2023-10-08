from rest_framework import serializers

from walletdestroyer.models import SpendingModel, EarningModel


class SpendingSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpendingModel
        fields = (
            'cost',
            'description',
            'time_create',
            'category',
        )

    def create(self, validated_data):
        user_id = self.context.get('request').user.id
        validated_data['user_id'] = user_id
        return SpendingModel.objects.create(**validated_data)


class EarningSerializer(serializers.Serializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    cost = serializers.IntegerField()
    time_create = serializers.DateField()

    def update(self, instance, validated_data):
        validated_data['user_id'] = validated_data['user_id'].id
        EarningModel.objects.filter(pk=instance.pk).update(**validated_data)
        return EarningModel.objects.get(pk=instance.pk)

