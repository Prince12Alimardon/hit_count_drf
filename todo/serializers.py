from rest_framework import serializers
from hitcount.models import HitCount
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    hit_count = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completed', 'hit_count']

    def get_hit_count(self, obj):
        # Retrieve the hit count for this Todo object
        hit_count = HitCount.objects.get_for_object(obj)
        return hit_count.hits
