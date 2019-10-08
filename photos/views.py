from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image
from .models import location

# Create your views here.
def welcome(request):
    all_images  = Image.objects.all()
    context = {'all_images':all_images}
    return render(request, 'all-photos/welcome.html', context)

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/image.html", {"image":image})

def search(request):
    if 'Category' in request.GET and request.GET['Category']:
        search_word = request.GET.get('Category')
        search_images = Category.search_image(search_word)
        if len(search_images) > 0:
            arr = []
            for i in search_images:
                arr.append(i.id)

            category = arr[0]
            images = Image.objects.filter(categ_id=category)

            '''
            getting locations
            '''
            try:
                locations = Location.get_location()
            except ValueError:
                raise Http404()
                assert False

            return render(request, "search.html", {"images": images, 'word': search_word, 'categories': search_images, "locations": locations})

        else:
            message = "No image found"
            return render(request, "search.html", {"message": message})   

   