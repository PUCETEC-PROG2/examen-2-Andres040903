from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


from django.shortcuts import get_object_or_404

def movie_detail(request, movie_id):
    movie = get_object_or_404(movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
