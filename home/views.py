from django.shortcuts import render , redirect
import random
import string
from .models import urls,visits



def home(request):
    extracontext = {}
    if request.method == 'POST':
        newURL = urls()
        newURL.url = request.POST['url']
        while True:
            shorturlSlug = ''.join(random.choices(string.ascii_lowercase, k=6))
            try:
                allURLs = urls.objects.get(slug = shorturlSlug)
            except:
                newURL.slug = shorturlSlug
                if request.user.is_authenticated:
                    newURL.user_id = request.user.id
                    newURL.Name = request.POST['alias']
                newURL.save()
                break
        extracontext = {'url': 'http://127.0.0.1:8000/s/'+ shorturlSlug}
    return render(request, 'index.html',extracontext)

def redir(request, slug):
    try:
        urlObject = urls.objects.get(slug=slug)
        print(urlObject.url)
        redirectURL = ('http://' if "http://" not in urlObject.url and "https://" not in urlObject.url else '') +urlObject.url
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        print(x_forwarded_for)
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        visit=visits(url = urlObject)
        visit.save()
        return redirect(redirectURL)
    except:
        return render(request,'error.html') 
