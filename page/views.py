from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, './main.html')

def story(request):
    return render(request, './story.html')

def artist(request):
    return render(request, './artist.html')

def music(request):
    return render(request, './music.html')

def mypage(request):
    return render(request, './mypage.html')

def adetail(request):
    return render(request, './a-detail.html')

def mdetail(request):
    return render(request, './m-detail.html')


