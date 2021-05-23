from typing import final
from django.shortcuts import render
from users.models import Profile
from .models import Category, Problem
import subprocess

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
    input = problems[0].test_case
    input = input.split("END")
    input = [x.replace("\r", "") for x in input]
    example = 'Example:'
    count = 1
    final_input=""
    for inp in input[0:]:
        inpo = inp.split("INPUT")
        if len(inpo)==1:
            break
        final_input = final_input + example + ' '+ str(count) + '\n\nInput:\n' + inpo[0] + '\nOutput:' + inpo[1] + '\n'
        count+=1
    return render(request, 'problemset/problem.html', {'problems': problems, 'final_input': final_input})

def check(request, pk):
    cod = request.POST.get("cod")
    points = request.POST.get("points")
    usr = request.user
    if usr.is_authenticated:
        file = open("problem.cpp", "w+")
        file.write(cod)
        input = request.POST.get("input")
        inp = input.split("END")
        inp = [x.replace("\r", "") for x in inp]
        for inpo in inp[:-1]:
            file1 = open("input.txt", "w+")
            inputo = inpo.split("INPUT")
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
            if inputo[1][1:-1] != oup[:-1]:
                file2 = open("problemset/static/problemset/output.txt", "w+")
                file2.write("Wrong Answer")
                return render(request, 'problemset/problem.html')
        file2 = open("problemset/static/problemset/output.txt", "w+")
        file2.write("Correct Answer")
        t = Profile.objects.get(id=usr.id - 2)
        t.points = t.points + int(points)
        t.save()
        return render(request, 'problemset/problem.html')
    else:
        file2 = open("problemset/static/problemset/output.txt", "w+")
        file2.write("LOGIN REQUIRED")
        return render(request, 'problemset/problem.html')

def lead(request):
    i = 1
    data = {"username":"" , "points":""}
    datas = []
    while i>0 :
        try :
            t = Profile.objects.get(id =i)
        except:
            break
        i=i+1
        s = str(t)
        data["username"] = s.split(' ')[0]
        data["points"] = t.points
        datas.append(data.copy())

    print(datas)
    datas = sorted(datas,key = lambda i:(i['points']),reverse=True)
    return render(request, 'problemset/leaderboard.html',{"datas":datas})


