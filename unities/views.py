from django.shortcuts import render

from .models import Unity, UnityContent

# Create your views here.
def unity_list_content(request, unity_slug):

    unity = Unity.objects.get(slug=unity_slug)
    content_list = UnityContent.objects.filter(unity=unity)

    return render(request, 'unities/unity_content_list.html', {'content_list': content_list})

def unity_content(request, unity_slug, topic_slug):
    
    content = UnityContent.objects.get(slug=topic_slug)
    # TODO: IMPROVE URL DISPATCHER
    return render(request, 'unities/unity_content.html', {'content':content, 'unity': unity_slug})
