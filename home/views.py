from django.shortcuts import render, redirect
import json

contents = [{
    "title": 'त्वमेव माता चपिता त्वमेव',
    'collection': 'Poetry',
    'id': '1',
    'content': '''त्वमेव माता च पिता त्वमेव, त्वमेव बन्धुश्च सखा त्वमेव।
त्वमेव विद्या, द्रविणं त्वमेव, त्वमेव सर्वम् मम देव देव।।''',
}, {
    'title': 'Father we thank thee',
    'collection': 'Poetry',
    'id': '2'
}, {
    'title': 'पुष्प की अभिलाषा',
    'author': 'माखन लाल चतुर्वेदी',
    'collection': 'Poetry',
    'id': '3'
}, {
    'title': 'पुष्प की अभिलाषा',
    'author': 'माखन लाल चतुर्वेदी',
    'collection': 'Poetry',
    'id': '4'
}, {
    'title': 'पुष्प की अभिलाषा',
    'author': 'माखन लाल चतुर्वेदी',
    'collection': 'Poetry',
    'id': '5'
}, {
    'title': 'पुष्प की अभिलाषा',
    'author': 'माखन लाल चतुर्वेदी',
    'collection': 'Poetry',
    'id': '6'
}]

metadata = str(contents)
print(metadata)

my_dict = {'contents': contents, 'metadata': metadata}

def requested_blog(id, blog_title):
    try:
        if contents[int(id)-1] or contents[int(id)-1].title == blog_title:
            return contents[int(id)-1]
    except IndexError:
        return False

def home_page(request):
    return render(request, 'home.html', my_dict)

def about_page(request):
    return render(request, 'about.html', my_dict)

def blog_page(request, id, blog_title):

    blog_content = requested_blog(id, blog_title)
    print('Id, Blog_Title', id, blog_title)
    if blog_content:
        return render(request, 'blog.html', {'content': blog_content})
    return redirect('404')

def page_not_found(request):
    return render(request, '404.html', {})

def base_page(request):
    return render(request, 'base.html', {})