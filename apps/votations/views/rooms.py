from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from votations.forms import RoomForm
from votations.models import Room
from home.default_messages import *
from links.models import UserRooms
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required
def create_room(request):
    form = RoomForm()

    if request.POST:
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit = False)
            room.code = Room.get_generated_code()
            room.admin = request.user
            room.save()

            user_rooms = UserRooms(room = room, is_active = True)
            user_rooms.save()
            user_rooms.users.add(request.user)

            messages.success(request, DEFAULT_MESSAGES['ADD'])
            return redirect("/")

    context = {
        "form": form,
    }

    return render(request, "votations/rooms/create_room.html", context)

@login_required
def change_room(request, slug_room):
    room = Room.get_room(request, slug_room)

    form = RoomForm(instance = room)

    if request.POST:
        form = RoomForm(request.POST, instance = room)
        if form.is_valid():
            room = form.save(commit = False)
            room.admin = request.user
            room.update_at = datetime.now()
            room.save()
            messages.success(request, DEFAULT_MESSAGES['CHANGED'])
            return redirect('/')

    context = {
        "form": form,
    }

    return render(request, 'votations/rooms/create_room.html', context)

@login_required
def desactivate_room(request, slug_room):
    room = Room.get_room(request, slug_room)

    room.is_active = False
    room.desactivate_at = datetime.now()
    room.save()
    messages.success(request, DEFAULT_MESSAGES['DESACTIVATE'])
    return redirect("/")

@login_required
def connect_room(request):
    if request.POST:
        code = request.POST.get("room", False)
        try:
            if Room.objects.select_related('admin').get(code__icontains = code).exists():
                user_rooms = UserRooms.objects.select_related('room').prefetch_related('users').get(room__code = code)
            # if room:
            #     messages.error(request, f"Você já está conectado(a) a sala: {sala.title}!")
        except Room.DoesNotExists:
            print("A")
            # room = Room.objects.select_related('admin').get(code__icontains = code)
            # if room:
            #     messages.success(request, f"Você conectou a room: {room.title}!")

        return redirect("index")

    context = {
        "teste": "teste"
    }

    return render(request, "votations/rooms/connect_room.html", context)
