from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'applications': 'storehousepbp', # isikan dengan nama aplikasi sendiri
        'name': 'Humam Al Labib', #isikan dengan nama sendiri
        'class': 'PBP F' # isikan dengan kelas kalian sendiri
    }

    return render(request, "main.html", context)