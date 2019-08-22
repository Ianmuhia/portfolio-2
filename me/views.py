from django.shortcuts import render

from .models import Personal_info, Education, Expirience, Awards


# Create your views here.
def index(request):
    education = Education.objects.all()
    info = Personal_info.objects.all()
    expirience = Expirience.objects.all()
    award = Awards.objects.all()
    context = {
        'education': education,
        'info': info,
        'expirience': expirience,
        'award': award

    }

    # personal info dictionary rendering

    return render(request, 'pages/index.html', context)
