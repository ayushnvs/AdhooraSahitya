from django.shortcuts import render

contents = [{
    "title": 'त्वमेव माता चपिता त्वमेव',
    'collection': 'Poetry'
}, {
    'title': 'Father we thank thee',
    'collection': 'Poetry'
}, {
    'title': 'पुष्प की अभिलाषा',
    'author': 'माखन लाल चतुर्वेदी',
    'collection': 'Poetry'
}]

my_dict = {'contents': contents}


def home_page(request):
    return render(request, 'index.html', my_dict)
