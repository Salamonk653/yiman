from django_elasticsearch_dsl import DocType, Index
from .models import New

# Name of the Elasticsearch index
post = Index('posts')
# See Elasticsearch Indices API reference for available settings
post.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@post.doc_type
class PostDocument(DocType):
    class Meta:
        model = New # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'name',
            'id',
            'slug',
            'image',
            # 'text',
            'created',
        ]