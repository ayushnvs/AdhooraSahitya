from django.shortcuts import render
import json

contents = [{
    "title": 'त्वमेव माता चपिता त्वमेव',
    'collection': 'Poetry',
    'id': '1'
}, {
    'title': 'Father we thank thee',
    'collection': 'Poetry',
    'id': '2'
}, {
    'title': 'पुष्प की अभिलाषा',
    'author': 'माखन लाल चतुर्वेदी',
    'collection': 'Poetry',
    'id': '3'
}]

metadata = str(contents)
print(metadata)

my_dict = {'contents': contents, 'metadata': metadata}


def home_page(request):
    return render(request, 'home.html', my_dict)

def base_page(request):
    return render(request, 'base.html', {})