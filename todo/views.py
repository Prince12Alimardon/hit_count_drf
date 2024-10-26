from rest_framework import generics
from hitcount.views import HitCountMixin
from hitcount.models import HitCount
from .models import Todo
from .serializers import TodoSerializer


class TodoListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetailView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        # Hitni oshirish
        self.increase_hit_count(instance)

        return super().retrieve(request, *args, **kwargs)

    def increase_hit_count(self, instance):
        hit_count, created = HitCount.objects.get_or_create(object_pk=instance.pk, content_type=self.get_content_type())
        hit_count.hits += 1
        hit_count.save()

    def get_content_type(self):
        from django.contrib.contenttypes.models import ContentType
        return ContentType.objects.get_for_model(Todo)
