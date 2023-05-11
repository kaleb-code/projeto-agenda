from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from django.core.paginator import Paginator

from contact.models import Contact
from contact.forms import ContactForm



def create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        context ={
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
    context ={
            'form': ContactForm()
        }
    return render(
        request,
        'contact/create.html',
        context
    )