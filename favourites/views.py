from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from favourites.models import Favourite
from flowers.models import Flower

def show(request):
    print Favourite.objects.all()
    f = Favourite.objects.filter(user=request.user)
    context = {"favourites":f}
    return render(request, "favourites/show.html", context)

def new(request):
    postdata = request.POST.copy()
    flower_id = postdata.get("flower_id")
    print flower_id
    flower = get_object_or_404(Flower, id=flower_id)
    favourite = Favourite() 
    favourite.user = request.user
    favourite.flower = flower
    favourite.save()
    return HttpResponse("ok")

def delete(request, id):
    id = id
    favourite = get_object_or_404(Favourite, id=id)
    favourite.delete()
    return HttpResponse("ok")
