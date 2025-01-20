from django.contrib import admin
from app.models import User, Problem, UserProblem
from django.contrib.auth.models import Group
# Register your models here.
admin.site.register(User)
admin.site.register(Problem)
admin.site.register(UserProblem)
admin.site.unregister(Group)
