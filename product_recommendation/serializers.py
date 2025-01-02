from rest_framework import serializers

class JdoodleCompileSerializer(serializers.Serializer):
    script = serializers.CharField(required=True)
    language = serializers.CharField(required=True)
    stdin = serializers.CharField(required=False)  # Optional stdin input
    versionIndex = serializers.IntegerField(required=False, default=0)  # Optional version index

    def validate(self, attrs):
        # You can add custom validation logic here, for example:
        #  - Check if the provided language is supported by Jdoodle
        #  - Ensure the script length is within a reasonable limit
        return attrs