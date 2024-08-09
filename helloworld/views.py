from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Student

user_data = [{"name": "afnan", "password": "12345"},{"name": "ashiq", "password": "4567"}]


def home(request):
    context = {'userdata': user_data}
    return render(request, 'home.html', context=context)


def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password1 = request.POST.get('password')

        for user in user_data:
            if user['name'] == name and user['password'] == password1:
                context = {'message': 'valid user'}
                return render(request, 'login.html', context=context)

        context = {'message': 'invalid user'}
        return render(request, 'login.html', context=context)
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        password1 = request.POST.get('password1')

        password2 = request.POST.get('password2')


        # checking confirm password
        if password1 != password2:
            context = {"alert2": "dont match"}
            return render(request, 'signup.html', context=context)

        # checking duplicate user
        for user in user_data:
            if user["name"] == name:
                context = {"alert": "its used"}
                return render(request, 'signup.html', context=context)

        # data valid scenario
        data = {"name": name, "password": password1}

        user_data.append(data)
        print(user_data)

        return render(request, 'signup.html')

    else:
        return render(request, 'signup.html')


def student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        print(name, age, grade)
        Student.objects.create(name=name, age=age, grade=grade)
        return render(request, 'student.html')
    else:
        return render(request, 'student.html')


def list(request):
    students = Student.objects.all()
    context = {"students": students}
    print(students[0].name)
    return render(request, 'list.html', context=context)


def delete(request,id):
    if request.method == 'POST':
        student_ = Student.objects.get(id=id)
        student_.delete()
        return redirect('/list')
