from django import forms
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from antu.models import Post
from antu.pyimsearch import cv2tools
from antu.pyimsearch.cv2tools import find_string
from antu.pyimsearch.database_tools import find_data_by_number
from antu.pyimsearch.search import searchImage, searchString, pic_catch


class PostForm(forms.Form):
    img = forms.ImageField(required=False)


@csrf_exempt
def search(request):
    img = request.FILES['img']

    x1=int(float(request.POST['x1'])//1)
    y1=int(float(request.POST['y1'])//1)
    x2=int(float(request.POST['x2'])//1)
    y2=int(float(request.POST['y2'])//1)

    print(x1,y1,x2,y2)


    post = Post(img=img)

    try:
        post.save()
    except:
        pass

    image = cv2tools.find_im(post.img.name)

    img2=pic_catch(x1,y1,x2,y2,post.img.name)
    s = find_string(img2)

    list_1 = searchImage(image)
    list_2 = searchString(s)

    print(list_1[0])

    if list_1[0]['id'] != 'NULL':
        return render(request, 'result.html', {'list1': list_1,
                                               'list2': list_2})
    else:
        return render(request, 'fail.html', {'list2': list_2})


def submit(request):
    return render(request, 'submit.html')


def info(request, list_id):
    id_ = int(list_id)
    data = find_data_by_number(id_)

    return render(request, 'info.html', data)
