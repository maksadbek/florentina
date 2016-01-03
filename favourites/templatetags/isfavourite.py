from django import template
from favourites.models import Favourite
register = template.Library()
@register.filter
def isfavourite(flower,user):
    print "huyyyyyyyyyyyyyyyyyyyy"
    f = Favourite.objects.filter(user=user, flower=flower)
    exist = False
    print "f - fuck:", f
    for i in f:
        print "flower is: ", i
        exist = True
    return exist
