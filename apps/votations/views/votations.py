from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from votations.models import Room, Votation
from links.models import UserRooms

@login_required
def votations_room(request, slug_room):
    room = Room.get_room(request, slug_room)

    votations = Votation.objects.filter(room__slug = room.slug, is_active = True)

    breadcrumb = [
        { "title": "Dashboard", "url": "/" },
        { "title": room.title },
    ]

    context = {
        "breadcrumb": breadcrumb,
        "votations": votations,
        "slug_room": slug_room
    }

    return render(request, "votations/votations/votations_room.html", context)

@login_required
def create_votation(request, slug_room):
    room = Room.get_room(request, slug_room)

    form = VotationForm()

    if request.POST:
        form = VotationForm(request.POST)
        if form.is_valid():
            votation = form.save(commit = False)
            votation.room = room
            votation.save()

            messages.success(request, DEFAULT_MESSAGES['ADD'])
            return redirect("votations_room", slug_room)

    context = {
        "form": form,
    }

    return render(request, "votations/votations/create_votation.html", context)
