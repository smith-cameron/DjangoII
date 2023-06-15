from django.shortcuts import render, HttpResponse, redirect
from .models import Show

def index(request):
    return redirect("/shows")

def dashboard(request):
    all_shows = Show.objects.all()
    for show in all_shows:
        print(show)
    context = {
        "all_shows": all_shows
    }

    return render(request, "dashboard.html", context)

def new(request):
    # if request.method == "GET":
    #     print(request.GET)
    return render(request, "create.html")   
    
def create(request):
    if request.method == "POST": 
        print(request.POST)
        # save to DB
        Show.objects.create(title = request.POST["title"], 
                            network = request.POST["network"], 
                            release_date = request.POST["release_date"], 
                            description = request.POST["description"], 
                            )
    return redirect("/shows")

def display(request, show_id):
    return render(request, "show.html")

def edit(request, show_id):
    this_show = Show.objects.get(id=show_id)
    if request.method == "POST":
        this_show.title = request.POST['title']
        this_show.network = request.POST['network']
        this_show.release_date = request.POST['release_date']
        this_show.description = request.POST['description']
        this_show.save()
        return redirect("/shows")
    context = {
        'show' : this_show
    }
    return render(request, "edit.html", {'show' : Show.objects.get(id=show_id)})

def delete(request, show_id):
    print(f"Delete show where id = {show_id}")
    Show.objects.get(id=show_id).delete()
    return redirect("/shows")

