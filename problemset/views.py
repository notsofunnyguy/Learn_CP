from django.shortcuts import render
from .models import Problem, Category

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
    return render(request, 'problemset/home.html', data)


def problem(request):
    problems = Problem.get_all_objects()
    return render(request, 'problemset/problem.html',  {'problems':problems })


def submitcode(request):
    return render(request, 'problemset/submitcode.html')


def discussions(request):
    return render(request, 'problemset/discussions.html')


def register(request):
    return render(request, 'problemset/register.html')