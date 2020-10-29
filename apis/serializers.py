from rest_framework import serializers

class IngestSerializer(serializers.Serializer):
    index = serializers.CharField(max_length=50, error_messages={
        "required" : "Index name is required",
        "blank" : "Index name should not be blank"
    })
    payload = serializers.JSONField()
