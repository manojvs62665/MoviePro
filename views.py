from django.shortcuts import render
from .models import moviedata
from .forms import insertdata,updatedata,deletedata
from django.http.response import HttpResponse

def home_page(request):
    return render(request,'home_page.html')

def insert_view(request):
    if request.method == "POST":
        iform = insertdata(request.POST)
        if iform.is_valid():

            movie_id = request.POST.get('movie_id')
            movie_name = request.POST.get('movie_name')
            movie_cast = request.POST.get('movie_cast')
            movie_rating = request.POST.get('movie_rating')
            movie_feedback = request.POST.get('movie_feedback')

            data = moviedata(
                movie_id=movie_id,
                movie_name=movie_name,
                movie_cast=movie_cast,
                movie_rating=movie_rating,
                movie_feedback=movie_feedback
            )

            data.save()
            iform = insertdata()
            return render(request,'insertdata.html',{'iform':iform})

        else:
            return HttpResponse("User Invalid Data")

    else:
        iform  = insertdata()
        return render(request,'insertdata.html',{'iform':iform})


def retrieve_view(request):
    mdata = moviedata.objects.all()
    return render(request,'retrive.html',{'mdata':mdata})


def update_view(request):
    if request.method == "POST":
        uform = updatedata(request.POST)
        if uform.is_valid():

            movie_id = request.POST.get('movie_id')
            movie_rating = request.POST.get('movie_rating')

            mdata = moviedata.objects.filter(movie_id=movie_id)

            if mdata:
                mdata.update(movie_rating=movie_rating)
                uform = updatedata()
                return render(request,'updatedata.html',{'uform':uform})
            else:
                return HttpResponse("Movie Id Not Availble")
        else:
            return HttpResponse("Movie Details Not Found")
    else:
        uform = updatedata()
        return render(request,'updatedata.html',{'uform':uform})


def delete_view(request):
    if request.method == "POST":
        dform = deletedata()
        if dform.is_valid():

            movie_id = request.POST.get('movie_id')

            mid = moviedata.objects.filter(movie_id=movie_id)

            if mid:
                mid.delete()
                dform = deletedata()
                return render(request,'deletedata.html',{'dform':dform})
            else:
                return HttpResponse("Movie Id Not Availbale")
        else:
            return HttpResponse("Movie Details Not Found")
    else:
        dform = deletedata()
        return render(request,'deletedata.html',{'dform':dform})
