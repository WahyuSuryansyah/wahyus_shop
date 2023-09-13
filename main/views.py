from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Mochammad Wahyu Suryansyah',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)