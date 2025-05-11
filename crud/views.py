from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Gender

# Create your views here.

def gender_list(request):
    try:
        gender = Gender.objects.all()
        
        data = {
            'genders':gender
        }

        return render(request, 'gender/GenderList.html', data)
    except Exception as e:
        return HttpResponse(f'Error occurred during load genders: {e}')

def add_gender(request):
    try:
        if request.method == 'POST':
            gender = request.POST.get('gender')
            Gender.objects.create(gender=gender)
            messages.success(request, 'Gender Added Successfully')
            return redirect('/gender/list')
        else:
            return render(request, 'gender/AddGender.html')
    except Exception as e:
        return HttpResponse(f'Error occurred during add gender: {e}')

    
def edit_gender(request, genderId):
    try:
        if request.method == 'POST':
            genderObj = Gender.objects.get(pk=genderId)
        
            gender = request.POST.get('gender')

            genderObj.gender = gender
            genderObj.save()

            messages.success(request, 'Gender updated successfully')

            data = {
            'gender': genderObj
        }

            return render(request, 'gender/EditGender.html', data)
        else:
            genderObj = Gender.objects.get(pk=genderId)

        data = {
            'gender': genderObj
        }

        return render(request, 'gender/EditGender.html', data)
    except Exception as e:
        return HttpResponse(f'Error occurred during edit gender: {e}')


def delete_gender(request, genderId):
    try:
        if request.method == 'POST':
            genderObj = Gender.objects.get(pk=genderId)
            genderObj.delete()

            messages.success(request, 'Gender deleted successfully')
            return redirect('/gender/list')

        else:
            genderObj = Gender.objects.get(pk=genderId)
            
        data = {
            'gender': genderObj
        }

        return render(request, 'gender/DeleteGender.html', data)
    except Exception as e:
        return HttpResponse(f'Error occurred during delete gender: {e}')