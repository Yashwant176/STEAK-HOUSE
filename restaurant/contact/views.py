from django.shortcuts import render,redirect
from .models import Contact


def contact(request): 
    if request.method == "POST":
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        review = request.POST.get('review')
        Contact.objects.create(name=name, email=email, review=review)
        return render(request, 'contact.html')
    
    service = Contact.objects.all()
    data = {'service': service}
    return render(request, 'contact.html', data)
    




def delete(request,id):
    dele=Contact.objects.get(id=id)
    dele.delete()
    return redirect('/contact')

    
    

