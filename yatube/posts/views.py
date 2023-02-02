from django.http import HttpResponse

# Главная страница
def index(request):    
    return HttpResponse('Главная страница')

# Страница с информацией об одном посте;
# view-функция принимает параметр pk из path()
def group_posts(request, pk):
    return HttpResponse(f'Post number {pk}') 