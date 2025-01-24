# from django.shortcuts import render
from django.conf import settings

# Create your views here.
from rest_framework.views import APIView
from django.db import transaction  # error -> all the db taken back
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Amenity, Room
from .serializers import (
    AmenitySerializer,
    RoomListSerializer,
    RoomDetailSerializer,
)
from categories.models import Category
from medias.serializers import PhotoSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from reviews.serializers import ReviewSerializer

"""
api/v1/rooms/amenities/1
"""


class Amenities(APIView):
    def get(self, request):  # every method has self and request
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(
            all_amenities, many=True
        )  # more than 1 object -> mant = True
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            amenity = serializer.save()  #
            return Response(
                AmenitySerializer(amenity).data,  # return new data
            )
        else:
            return Response(serializer.errors)


class AmenitiesDetail(APIView):
    def get_object(self, pk):  # get pk object
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data)

    def put(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(  # handle user sending data
            amenity,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_amenity = serializer.save()
            return Response(
                AmenitySerializer(updated_amenity).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()
        return Response(status=HTTP_204_NO_CONTENT)


"""
generate room, delete-> authentication needed! 
"""


class Rooms(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomListSerializer(rooms, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = RoomDetailSerializer(data=request.data)
        if serializer.is_valid():
            category_pk = request.data.get("category")
            if not category_pk:
                raise ParseError(
                    "Category is required"
                )  # 400 bad request for wrong data
            try:
                category = Category.objects.get(pk=category_pk)
                if category.kind == Category.CategoryKindChocies.EXPERIENCES:
                    raise ParseError("Cateogory kind should be rooms")
            except Category.DoesNotExist:
                raise ParseError("Category does not exist")
            try:
                # print(request.data.get('amenities'))
                with transaction.atomic():
                    room = serializer.save(  # tells who is the user
                        owner=request.user,  # this goes to validated_data para field of create() method
                        category=category,
                    )
                    # when u post user provided data, it automatically call create() method
                    amenities = request.data.get("amenities")
                    for amenity_pk in amenities:
                        amenity = Amenity.objects.get(pk=amenity_pk)
                        room.amenities.add(amenity)
                        # or just pass : fail in silence
                    # what if user send amenities that does not exist? or wrong datatype?
                    serializer = RoomDetailSerializer(room)
                    return Response(serializer.data)
            except Exception:
                raise ParseError("amenity not found")
        else:
            return Response(serializer.errors)
        # handle attributes that has an relation with others


class RoomDetails(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            room = Room.objects.get(pk=pk)
            return room
        except Room.DoesNotExist:
            raise NotFound  # HTTP 404 NOT FOUND

    def get(self, request, pk):
        room = self.get_object(pk=pk)
        serializer = RoomDetailSerializer(
            room,
            context={"request": request},
        )
        return Response(serializer.data)

    def put(self, request, pk):
        room = self.get_object(pk=pk)
        serializer = RoomDetailSerializer(
            room,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_room = serializer.save()
            return Response(RoomDetailSerializer(updated_room).data)
        else:
            return Response(serializer.error)

    def delete(self, request, pk):  # delete handle
        room = self.get_object(pk)
        if room.owner != request.user:
            raise PermissionDenied
        room.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class RoomReviews(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, request, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def post(self, request, pk):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save(
                user=request.user,  # send extra data that doesn't come from user data(data=request.data)
                room=self.get_object(pk),
            )
            serializer = ReviewSerializer(review)
            return Response(serializer.data)


class RoomPhotos(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def post(self, request, pk):
        room = self.get_object(pk)
        if request.user != room.owner:
            raise PermissionDenied
        serializer = PhotoSerializer(data=request)
        if serializer.is_valid():
            photo = serializer.save(room=room)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
