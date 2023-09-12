from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'applications': 'storehousepbp',
        'name': 'Humam Al Labib',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)