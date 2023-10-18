from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from ColleageListApp import models

# Create your views here
def colleagePage(request):

    if request.method == 'GET':
        data = models.ColleageListDB.objects.all()
        return render(request, 'index.html', {'data':data})
    else:
        models.ColleageListDB(
            colleage_name = request.POST.get('name'),
            address = request.POST.get("address"),
            district = request.POST.get("district"),
            state = request.POST.get("state"),
            pincode = request.POST.get("pincode"),
            email = request.POST.get("email"),
            contact_num = request.POST.get("number"),
            country = request.POST.get("country") ).save()
        data = models.ColleageListDB.objects.all()
        return render(request, 'index.html', {'data': data})
        
        
def delete(request, id):
    data = models.ColleageListDB.objects.get(id=id)
    print(data)
    data.delete()
    #data.save()
    return HttpResponseRedirect("/colleage")


def update(request, id):
    data = models.ColleageListDB.objects.get(id=id)
    return render(request, 'update.html', {'data': data})

def update_data(request, id):
    
    data = models.ColleageListDB.objects.get(id=id)
    
    data.colleage_name = request.POST.get('name')
    data.address = request.POST.get("address")
    data.district = request.POST.get("district")
    data.state = request.POST.get("state")
    data.pincode = request.POST.get("pincode")
    data.email = request.POST.get("email")
    data.contact_num = request.POST.get("number")
    data.country = request.POST.get("country")
    
    data.save()
    return HttpResponseRedirect("/colleage")

    
