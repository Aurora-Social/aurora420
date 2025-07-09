from django.shortcuts import redirect, render
from django.contrib import messages
from .models import NewsletterSubscriber, ContactMessage

def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            obj, created = NewsletterSubscriber.objects.get_or_create(email=email)
            
            if request.path.startswith('/en'):
                if created:
                    messages.success(request, "Thank you for subscribing! 🎉")
                else:
                    messages.info(request, "You're already subscribed.")
            else:
                if created:
                    messages.success(request, "¡Gracias por suscribirte! 🎉")
                else:
                    messages.info(request, "Ya estás suscrito.")
    
    return redirect(request.META.get('HTTP_REFERER', '/'))  # geldiği sayfaya yönlendir

def contact_form_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            
            if request.path.startswith('/en'):
                messages.success(request, "Your message has been received! We'll get back to you 💌")
            else:
                messages.success(request, "¡Hemos recibido tu mensaje! Te contactaremos pronto 💌")

    return redirect(request.META.get('HTTP_REFERER', '/'))

from .models import GalleryImage

def index_view(request):
    gallery_images = GalleryImage.objects.all()
    return render(request, 'core/index.html', {
        'gallery_images': gallery_images,
    })



def spanish_homepage(request):
    gallery_images = GalleryImage.objects.all()
    return render(request, 'core/pagina.html', {
        'gallery_images': gallery_images,
    })
