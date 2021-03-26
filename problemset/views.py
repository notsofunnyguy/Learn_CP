from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Category, Problem
from django.utils import timezone
import os, subprocess

def home(request):
    problems = None
    categories = Category.get_all_objects()
    category_ID = request.GET.get('category')
    print(category_ID)
    if category_ID:
        problems = Problem.get_all_objects_by_categoryid(category_ID)
    else:
        problems = Problem.get_all_objects()
    data = {}
    data['problems'] = problems
    data['categories'] = categories
    print('you are : ' ,request.session.get('email'))
    return render(request, 'problemset/home.html', data)


def discussions(request):
    return render(request, 'problemset/discussions.html')


def ide(request):
    return render(request, 'problemset/ide.html')


def run(request):
    cod = request.POST.get("cod")
    input = request.POST.get("input")
    print(cod)
    file = open("problem.cpp", "w+")
    file1 = open("input.txt", "w+")
    file.write(cod)
    file1.write(input)
    print(file.read())
    print(file1.read())
    filename = "problem.cpp"
    runcode = subprocess.Popen(['g++', filename], stdout=subprocess.PIPE)
    while runcode.poll() is None:
        continue
    ps_process = subprocess.Popen(["cat", "input.txt"], stdout=subprocess.PIPE)
    output = subprocess.Popen(['./a.out'], stdin=ps_process.stdout, stdout=subprocess.PIPE)
    ps_process.stdout.close()
    file2 = open("problemset/static/problemset/output.txt", "w+")
    file2.write(output.stdout.read().decode("utf-8"))
    # print(output.stdout.read().decode("utf-8"))
    print("P")
    while output.poll() is None:
        continue
    # if output.poll() is None :
    return render(request, 'problemset/ide.html')


def submitcode(request):
    return render(request, 'problemset/submitcode.html')

def problem(request, pk):
    print(pk)
    problems = Problem.get_all_objects_by_id(pk)
    return render(request, 'problemset/problem.html', {'problems': problems})