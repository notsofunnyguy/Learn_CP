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
    file = open("problem.cpp", "w+")
    file1 = open("input.txt", "w+")
    file.write(cod)
    file1.write(input)
    print(file.read())
    print(file1.read())
    filename = "problem.cpp"
    runcode = subprocess.getoutput('g++ ' + filename)
    if runcode != "":
        file2 = open("problemset/static/problemset/output.txt", "w+")
        file2.write(runcode)
        return render(request, 'problemset/ide.html')

    ps_process = subprocess.Popen(["cat", "input.txt"], stdout=subprocess.PIPE)
    output = subprocess.Popen(['./a.out'], stdin=ps_process.stdout, stdout=subprocess.PIPE)
    ps_process.stdout.close()
    while output.poll() is None:
        continue
    file2 = open("problemset/static/problemset/output.txt", "w+")
    file2.write(output.stdout.read().decode("utf-8"))
    return render(request, 'problemset/ide.html')


def submitcode(request):
    return render(request, 'problemset/submitcode.html')

def problem(request, pk):
    print(pk)
    problems = Problem.get_all_objects_by_id(pk)
    return render(request, 'problemset/problem.html', {'problems': problems})

def check(request, pk):
    cod = request.POST.get("cod")
    #print(cod)
    file = open("problem.cpp", "w+")
    file.write(cod)
    input = request.POST.get("input")
    inp = input.split("END")
    for inpo in inp[:-1]:
        file1 = open("input.txt", "w+")
        inputo = inpo.split("INPUT")
        print(inputo[0])
        if inputo[0] != "None":
            file1.write(inputo[0])
        print(file.read())
        print(file1.read())
        filename = "problem.cpp"
        runcode = subprocess.getoutput('g++ ' + filename)
        if runcode != "":
            file2 = open("problemset/static/problemset/output.txt", "w+")
            file2.write(runcode)
            return render(request, 'problemset/problem.html')
        ps_process = subprocess.Popen(["cat", "input.txt"], stdout=subprocess.PIPE)
        output = subprocess.Popen(['./a.out'], stdin=ps_process.stdout, stdout=subprocess.PIPE)
        ps_process.stdout.close()
        while output.poll() is None:
            continue
        oup = output.stdout.read().decode("utf-8")
        print(oup[:-1],inputo[1][2:-2])
        if inputo[1][2:-2] != oup[:-1]:
            file2 = open("problemset/static/problemset/output.txt", "w+")
            file2.write("Wrong Answer")
            return render(request, 'problemset/problem.html')
        print("CORRECT")
    file2 = open("problemset/static/problemset/output.txt", "w+")
    file2.write("Correct Answer")
    return render(request, 'problemset/problem.html')

