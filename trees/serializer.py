from rest_framework import serializers
from .models import Tree


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'tree_name', 'tree_facts', 'created_at', 'updated_at')
        model = Tree
