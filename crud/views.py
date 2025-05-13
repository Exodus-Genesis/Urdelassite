from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Gender, User
from django.contrib.auth.hashers import make_password

# Create your views here.

def gender_list(request):
    try:
        gender = Gender.objects.select_related('gender')
        
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

def user_list(request):
    try:
        userObj = User.objects.all()

        data = {
            'user': userObj
        }

        return render(request, 'user/UserList.html', data)
    except Exception as e:
        return HttpResponse(f'Error occurred during user list: {e}')

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

def add_user(request):
    try:
        if request.method == 'POST':
            fullName = request.POST.get('full_name')
            gender = request.POST.get('gender')
            birth_date = request.POST.get('birth_date')
            address = request.POST.get('address')
            contactNumber = request.POST.get('contact_number')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            
            User.objects.create(
                full_name=fullName,
                gender=Gender.objects.get(pk=gender),
                birth_date=birth_date,
                address=address,
                contact_number=contactNumber,
                email=email,
                username=username,
                password=make_password(password)
            ).save()

            messages.success(request, 'User added successfully')
            return redirect('/user/add')
        else:
            genderObj = Gender.objects.all()

            data = {
                'gender': genderObj
            }

            return render(request, 'user/Adduser.html', data)
    except Exception as e:
        return HttpResponse(f'Error occurred during add user: {e}')