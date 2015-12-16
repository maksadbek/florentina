from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from favourites.models import Favourite
from flowers.models import Flower
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def show(request):
    print Favourite.objects.all()
    f = Favourite.objects.filter(user=request.user)
    context = {"favourites":f}
    return render(request, "favourites/show.html", context)

@login_required(login_url='/')
def new(request):
    postdata = request.POST.copy()
    flower_id = postdata.get("flower_id")
    flower = get_object_or_404(Flower, id=flower_id)
    favourite = Favourite() 
    favourite.user = request.user
    favourite.flower = flower
    favourite.save()
    return HttpResponse(status=201)

@login_required(login_url='/')
def delete(request, id):
    favourite = get_object_or_404(Favourite, id=id)
    favourite.delete()
    return HttpResponse(status=204)
