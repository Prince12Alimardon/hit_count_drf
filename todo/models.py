from django.db import models
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic')

    def __str__(self):
        return self.title
