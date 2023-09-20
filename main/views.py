from django.http import HttpResponseRedirect, HttpResponse
from main.forms import ItemForm
from django.urls import reverse
from django.shortcuts import render
from .models import Item
from django.core import serializers

# Create your views here.
def show_main(request):
    items = Item.objects.all()
    item_count = Item.objects.count()

    context = {
        'applications': 'storehousepbp', # isikan dengan nama aplikasi sendiri
        'name': 'Humam Al Labib', #isikan dengan nama sendiri
        'class': 'PBP F', # isikan dengan kelas kalian sendiri
        'items': items,
        'item_count': item_count
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")