from author.models import CustomUser, AuthorPoint
from rest_framework.response import Response
from blogs.models import Blogs
from .serializers import BlogSerializer, UserSerializer, AuthorPointSerializer
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.generics import GenericAPIView
#from rest_framework.mixins import ListModelMixin, CreateModelMixin

class BogListCreateApiView(generics.ListCreateAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer

class BlogDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer

class UserListCreateApiView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class AuthorPointListCreateApiView(generics.ListCreateAPIView):
    queryset = AuthorPoint.objects.all()
    serializer_class = AuthorPointSerializer

class AuthorPointDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorPoint.objects.all()
    serializer_class = AuthorPointSerializer

""" Function based """

# @api_view(["GET","POST"])
# def blog_list_create_api_view(request):
#     if request.method == "GET":
#         blogs = Blogs.objects.all()
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data = serializer.data, status = status.HTTP_201_CREATED)
#         return Response(status = status.HTTP_400_BAD_REQUEST)

# @api_view(["GET","PUT","DELETE"])
# def blog_list_detail_api_view(request, pk):
#     try:
#         blog_instance = Blogs.objects.get(pk=pk)
#     except:
#         return Response(
#             {
#                 'errors' : {
#                     'code' : 404,
#                     'message' : f'{pk} id-li blog tapilmadi'
#                 }
#             },
#             status = status.HTTP_404_NOT_FOUND
#         )

#     if request.method == "GET":
#         serializer = BlogSerializer(blog_instance)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = BlogSerializer(blog_instance, data = request.data) #partial = True
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_200_OK)
#         return Response(status = status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == "DELETE":
#         blog_instance.delete()
#         return Response(
#             {
#                 'errors' : {
#                     'code' : 204,
#                     'message' : f'{pk} id-li blog silindi'
#                 }
#             },
#             status = status.HTTP_204_NO_CONTENT
#         )

""" Class based """

# class BlogListCreateApiView(APIView):
#     def get(self, request):
#         blogs = Blogs.objects.all()
#         serializer = BlogSerializer(blogs, many=True, context = {'request': request})
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = BlogSerializer(data=request.data, context = {'request': request})
#         if serializer.is_valid():
#             # title = request.data.get('title') I usul
#             # title = serializer.validated_data.get('title') II usul
#             # print(f'{title=}')
#             # upper_title = title.upper()
#             # serializer.save(title = upper_title)
#             serializer.save()
#             return Response(data = serializer.data, status = status.HTTP_201_CREATED)
#         return Response(status = status.HTTP_400_BAD_REQUEST)

# class BlogDetailApiView(APIView):
#     def get_object(self, pk):
#         blog_instance = Blogs.objects.get(pk=pk)
#         return blog_instance

#     def get(self, request, pk):
#         blog = self.get_object(pk=pk)
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         blog = self.get_object(pk=pk)
#         serializer = BlogSerializer(blog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

#     def delete(self, request, pk):
#         blog = self.get_object(pk=pk)
#         blog.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)


# class UserListCreateApiView(APIView):
#     def get(self, request):
#         users = CustomUser.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data = serializer.data, status = status.HTTP_201_CREATED)
#         return Response(status = status.HTTP_400_BAD_REQUEST)

# class UserDetailApiView(APIView):
#     def get_object(self, pk):
#         user_instance = CustomUser.objects.get(pk=pk)
#         return user_instance

#     def get(self, request, pk):
#         user = self.get_object(pk=pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         user = self.get_object(pk=pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

#     def delete(self, request, pk):
#         user = self.get_object(pk=pk)
#         user.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)