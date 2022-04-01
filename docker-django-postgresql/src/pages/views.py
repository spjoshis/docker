from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs   ):
    return render(request, 'home.html', {})


def cms_view(request, *args, **kwargs):
    contex = {
        'title': 'About',
        'text': [
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry.Lorem Ipsum has beenthe industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum",
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry.Lorem Ipsum has beenthe industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum",
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry.Lorem Ipsum has beenthe industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"
        ]
    }
    return render(request, 'cms.html', contex)