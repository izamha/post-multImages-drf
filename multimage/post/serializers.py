from rest_framework.serializers import ModelSerializer
from .models import Post, Image


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'images',)
        extra_kwargs = {
            "images": {
                "required": False,
            }
        }
    # # function that returns the owner of a tweet
    # def get_tweep_username(self, tweets):
    #     tweep = tweets.tweep.username
    #     return tweep

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'