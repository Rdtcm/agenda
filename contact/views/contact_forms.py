from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from contact.models import Contact

from contact.forms import ContactForm


# Pasta views criada para poder separar as views em varios arquivos


def create(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        
        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect('contact:create')

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
       'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context
    )