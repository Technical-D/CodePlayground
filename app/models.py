from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.timezone import now

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email ,name, password=None):
        if not email:
            raise ValueError("User must have email address.")
        if not name:
            raise ValueError("Users must have an name.")
        

        user = self.model(
            email = self.normalize_email(email),
            name = name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, password):
        user = self.create_user(
            email = self.normalize_email(email),
            name = name,
            password= password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    name = models.CharField(verbose_name='name',max_length=30)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = MyUserManager()

    def __str__(self):
        return self.email

    # Checking for permission
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
class Problem(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    title = models.CharField(max_length=255, unique=True)
    short_description = models.TextField()
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES, default='Easy')
    score = models.PositiveIntegerField()
    starter_code = models.TextField(help_text="Python starter code for the problem")
    description_file = models.FileField(upload_to='descriptions/', help_text="Path to detailed description file")
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class UserProblem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_problems')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='user_problems')
    solved = models.BooleanField(default=False)
    solved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'problem')

    def __str__(self):
        return f"{self.user.username} - {self.problem.title}"