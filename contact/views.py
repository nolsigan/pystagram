from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ContactForm


# make new contact
@login_required
def new_contact(request):
    if request.method == 'GET':
        new_form = ContactForm()
    elif request.method == 'POST':
        new_form = ContactForm(request.POST)

        if new_form.is_valid():
            new_contact = new_form.save(commit=False)
            new_contact.user = request.user
            new_contact.save()
            return redirect('/blog/')

    return render(request, 'new_contact.html', {
        'form': new_form,
    })
