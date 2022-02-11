from rest_framework import status, generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post, Image
from .serializers import ImageSerializer, PostSerializer

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_post(request):
    # user = request.user
    if request.method == 'POST':
        files = request.FILES.getlist('images')
        if files:
            request.data.pop('images')
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print(serializer.data['id'])
                post_qs = Post.objects.get(id=serializer.data['id'])
                uploaded_files = []
                for file in files:
                    content = Image.objects.create(image=file)
                    uploaded_files.append(content)

                post_qs.images.add(*uploaded_files)
                context = serializer.data
                context["images"] = [file.id for file in uploaded_files]
                return Response(context, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                context = serializer.data            
                return Response(context, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'status': '405 METHOD_NOT_ALLOWED'})


class ListPost(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ListImage(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer