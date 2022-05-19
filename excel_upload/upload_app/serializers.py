from rest_framework import serializers
from .models import ExcelData

class ExcelDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelData
        fields = ['id','name','age','hobby','date_created']

    def update(self, instance, validated_data):
        excel_data=instance

        if "name" in validated_data:
            excel_data.name = validated_data["name"]
        if "age" in validated_data:
            excel_data.age = validated_data["age"]
        if "hobby" in validated_data:
            excel_data.hobby = validated_data["hobby"]

        excel_data.save()
        return excel_data.id
    