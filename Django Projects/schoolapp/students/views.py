from django.shortcuts import render, redirect
from django.http import HttpResponse
from students.models import RegistrationForm
from students.forms import Registration

def registration(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')   
            except:
                pass
    else:
        form = Registration()
    return render(request,'index.html',{'form':form})

def show(request):  
    showdata = RegistrationForm.objects.all()  
    return render(request,"show.html",{'showdata':showdata})

def edit(request, id):  
    student = RegistrationForm.objects.get(id=id)  
    return render(request,'edit.html', {'student':student})

def update(request, id):  
    student = RegistrationForm.objects.get(id=id)  
    form = Registration(request.POST, instance = student)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'student': student})

def destroy(request, id):  
    student = RegistrationForm.objects.get(id=id)  
    student.delete()  
    return redirect("/show")    
    
    
    #return redirect('/')