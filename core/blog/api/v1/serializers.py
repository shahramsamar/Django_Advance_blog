from  rest_framework import serializers
from ...models import Post, Category



# class  PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
    
class  CategorySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Category
        fields =['id','name']

    
class  PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = serializers.SerializerMethodField()
    category = serializers.SlugRelatedField(many=False, slug_field="name", queryset=Category.objects.all())
    # category = CategorySerializer()
    
    
    class Meta:
        model = Post
        # fields = "__all__"
        fields = ['id','author','title','category','content','snippet',
                 'relative_url','absolute_url','status','created_date','published_date']
        read_only_fields = ['author']
    
    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)
    #when we need to change data for show #
    def to_representation(self, instance):
        request = self.context.get("request")
        rep =  super().to_representation(instance)
        
        # rep['state'] = 'list'
        # if request.parser_context.get("kwargs").get('pk'):
        #     rep['state'] = 'single'
        if request.parser_context.get("kwargs").get('pk'):
            rep.pop('snippet')
            rep.pop('relative_url')
            rep.pop('absolute_url')
        else:
            rep.pop('content', None)

        rep['category'] = CategorySerializer(instance.category).data
        return rep
    
    
    
    

       