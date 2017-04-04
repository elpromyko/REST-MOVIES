from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MovieSerializer
from movies.models import Movie


class MoviesView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieView(APIView):
    def get(self, request, id):
        # movie = Movie.objects.get(pk=id)
        movie = get_object_or_404(Movie, pk=id)
        serializer = MovieSerializer(movie, context={"request": request})
        return Response(serializer.data)

    def delete(self, request, id):
        Movie.objects.filter(pk=id).delete()

    def put(self, request, id):
        movie = Movie.objects.get(pk=id)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



