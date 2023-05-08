from .models import Kit, Medicine
from rest_framework import serializers
from django.core.exceptions import ValidationError


class KitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kit
        fields = ['id', 'location']


class KitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kit
        fields = ['id', 'location']

    def create(self, validated_data):
        request = self.context["request"]
        validated_data['user'] = request.user
        return super().create(validated_data)


class MedicineSerializer(serializers.ModelSerializer):
    kit = KitSerializer()

    class Meta:
        model = Medicine
        fields = ['id', 'kit', 'name', 'expire_date', 'count']
        read_only_fields = ['kit']


class MedicineCreateSerializer(serializers.ModelSerializer):
    kit_id = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Kit.objects.all(),
        source="kit",
        write_only=True,
    )

    class Meta:
        model = Medicine
        fields = ['kit_id', 'name', 'expire_date', 'count']

    def validate(self, attrs):
        request = self.context["request"]
        if attrs["kit"].user != request.user:
            raise ValidationError("User is not owner of the kit.")
        return super().validate(attrs)
