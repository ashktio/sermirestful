from django.shortcuts import render, redirect 
from . models import Show

# Create your views here.

def new_show(request):
    return render(request, 'new_show.html')

def create_show(request):
    new_show = Show.objects.create(title = request.POST['title'], network = request.POST['network'], release_date = request.POST['date'], description = request.POST['description'])
    return redirect(f'/shows/{new_show.id}')
    # return redirect("/shows/" + new_show.id) an other way of doing it

def show_profile(request, show_id):
    this_show = Show.objects.get (id = show_id)
    context = {
        'one_show' : this_show
    }
    return render(request, 'show_profile.html', context)

def all_shows(request):
    shows_added = Show.objects.all()
    context = {
        'every_show' : shows_added
    }
    return render(request, 'all_shows.html', context)
    

def edit_show(request, show_id):
    this_show = Show.objects.get (id = show_id)
    context = {
        'one_show' : this_show
    }
    return render(request, 'edit_show.html', context)


def update_show(request, show_id):
    this_show = Show.objects.get (id = show_id)
    this_show.title = request.POST['title']
    this_show.network = request.POST['network']
    this_show.date = request.POST['date']
    this_show.save()
    return redirect(f"/shows/{this_show.id}")

def destroy_show(request, show_id): #Deleting always should be a post request
    this_show = Show.objects.get (id = show_id)
    this_show.delete()
    return redirect('/shows')
    # return redirect(f"/shows/{this_show.id}/delete")

# def delete_show(request, show_id):
#     this_show = Show.objects.get (id = show_id)
#     this_show.delete()
#     return redirect('/shows')
