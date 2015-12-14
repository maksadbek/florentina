from django.http import HttpResponse 
from django.template import RequestContext 
from django.utils import simplejson 

def category_get_types(request): 
    id = request.GET.get('id','') 
    result = Category.objects.filter(id=id)
    types = result.types.objects.all()
    return HttpResponse(simplejson.dumps(result), mimetype='application/javascript') 
