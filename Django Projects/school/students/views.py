from django.shortcuts import render
from django.http import HttpResponse
from .models import RegistrationForm

def registration(request):
    return render(request, 'index.html')
    
def registrationdata(request):
    if request.method=='POST':
        if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('date_of_birth') and request.POST.get('gender') and request.POST.get('roll_no') and request.POST.get('father_name') and request.POST.get('mother_name') and request.POST.get('address'):
            post=RegistrationForm()
            post.first_name=request.POST.get('first_name')
            post.last_name=request.POST.get('last_name')
            post.date_of_birth=request.POST.get('date_of_birth')
            post.gender=request.POST.get('gender')
            post.roll_no=request.POST.get('roll_no')
            post.father_name=request.POST.get('father_name')
            post.mother_name=request.POST.get('mother_name')
            post.address=request.POST.get('address')
            fname = post.first_name
            lname = post.last_name
            dob = post.date_of_birth
            gender = post.gender
            rollno = post.roll_no
            fathername = post.father_name
            mothername = post.mother_name
            address = post.address
            params = {'first_name':fname, 'last_name':lname, 'date_of_birth':dob, 'gender':gender, 'roll_no':rollno, 'father_name':fathername, 'mother_name':mothername, 'address':address}
            post.save()

            return render(request, 'data.html', params)

    else:
        return render(request, 'data.html')