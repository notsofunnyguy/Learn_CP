from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=20, default='Easy')

    @staticmethod
    def get_all_objects():
        return Category.objects.all()


    def __str__(self):
        return self.title


class Problem(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=10000)
    points = models.IntegerField(default=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , default=1)
    test_case = models.TextField(max_length=10000, null=set)
    hidden_test_cases = models.TextField(max_length=10000000, null=set)
    constraints = models.TextField(max_length=1000, null=set)


    @staticmethod
    def get_all_objects():
        return Problem.objects.all()


    @staticmethod
    def get_all_objects_by_categoryid(category_ID):
        if category_ID:
            return Problem.objects.filter(category = category_ID)
        else:
            return Problem.get_all_objects()

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20, default='Username', unique=set)
    email = models.EmailField()
    password = models.CharField(max_length=500)
