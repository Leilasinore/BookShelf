from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Profile, Book
from .serializers import ProfileSerializer, BookSerializer

@api_view(['GET'])
def get_profiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)

    return Response(serializer.data)

# GET SINGLE PROFILE
@api_view(['GET'])
def get_profile(request, pk):
    try:
        profile = Profile.objects.get(id=pk)
    except Profile.DoesNotExist:
        return Response(
            {"error": "Profile not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ProfileSerializer(profile)

    return Response(serializer.data)

# UPDATE PROFILE
@api_view(['PUT'])
def update_profile(request, pk):

    try:
        profile = Profile.objects.get(id=pk)
    except Profile.DoesNotExist:
        return Response(
            {"error": "Profile not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ProfileSerializer(profile, data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
def create_profile(request):
    serializer = ProfileSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE PROFILE
@api_view(['DELETE'])
def delete_profile(request, pk):

    try:
        profile = Profile.objects.get(id=pk)
    except Profile.DoesNotExist:
        return Response(
            {"error": "Profile not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    profile.delete()

    return Response(
        {"message": "Profile deleted successfully"},
        status=status.HTTP_204_NO_CONTENT
    )

# Book controllers
@api_view(['GET'])
def get_books(request):

    books = Book.objects.all()

    serializer = BookSerializer(books, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_book(request, pk):

    try:
        book = Book.objects.get(id=pk)

    except Book.DoesNotExist:
        return Response(
            {"error": "Book not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = BookSerializer(book)

    return Response(serializer.data)

@api_view(['POST'])
def create_book(request):

    serializer = BookSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['PUT'])
def update_book(request, pk):

    try:
        book = Book.objects.get(id=pk)

    except Book.DoesNotExist:
        return Response(
            {"error": "Book not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = BookSerializer(book, data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )
@api_view(['DELETE'])
def delete_book(request, pk):

    try:
        book = Book.objects.get(id=pk)

    except Book.DoesNotExist:
        return Response(
            {"error": "Book not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    book.delete()

    return Response(
        {"message": "Book deleted successfully"},
        status=status.HTTP_204_NO_CONTENT
    )