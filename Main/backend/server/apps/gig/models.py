from django.db import models
from django.contrib.auth.models import User
import os


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, default=None)
    bio = models.TextField(max_length=500, default=None)
    image = models.ImageField(upload_to='profiles/')

    gender = models.CharField(max_length=10, choices=(
        ("Male", "Male"), ("Female", "Female")), default="Male", blank=False)

    def __str__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        os.remove(self.image.name)
        super(CustomUser, self).delete(*args, **kwargs)




class Gig(models.Model):

    CATEGORY = (
    ('Web Design', 'Web Design'),
    ('Graphic Design', 'Graphic Design'),
    ('Web Developing', 'Web Developing'),
    ('Software Engineering', 'Software Engineering'),
    ('Scraping', 'Scraping'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, editable=False, blank=True)
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    category = models.CharField(choices=CATEGORY, max_length=30)
    description = models.TextField()
    responsibilities = models.TextField()
    experience = models.CharField(max_length=100)
    job_location = models.CharField(max_length=120)
    Salary = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='media', null=True)
    application_deadline = models.DateTimeField()
    published_on = models.DateTimeField(default=timezone.now)


class Project(models.Model):
    project_name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=300, default=None)
    postedOn = models.DateTimeField(auto_now_add=True, blank=True)
    leader = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    isCompleted = models.BooleanField(default=False)
    deadline = models.DateField(blank=False)
    task_count = models.IntegerField(default=0)

    def __str__(self):
        return self.project_name


class Task(models.Model):
    task_name = models.CharField(max_length=50, blank=False)
    addedOn = models.DateTimeField(auto_now_add=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    credits = models.CharField(max_length=20, choices=(("Paid", "Paid"), ("Other", "Other")), blank=False,
                               default="Paid")
    rating = models.DecimalField(default=0, max_digits=2, decimal_places=1)
    mention = models.CharField(max_length=200, blank=True, null=True)
    amount = models.IntegerField(default=0)
    task_description = models.CharField(max_length=100, default=None)
    task_link = models.URLField(blank=True)
    latest_submission_time = models.DateTimeField(blank=True, null=True)
    isCompleted = models.BooleanField(default=False)
    deadline = models.DateField(blank=False)

    def __str__(self):
        return self.task_name


class TaskSkillsRequired(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    proficiency_level_required = models.IntegerField(1)

    def __str__(self):
        return str(self.task.task_name) + '[id=' + str(self.task.id) + ']'



class Applicant(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    time_of_application = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.user.user.username) + '[id=' + str(self.user.id) + ']'


class Contributor(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    isCreditVerified = models.BooleanField(default=False)
    time_of_selection = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.user.user.username) + '[id=' + str(self.user.id) + ']'


class UserRating(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    emp = models.ForeignKey(
        CustomUser, related_name='rating_by', on_delete=models.CASCADE)
    fre = models.ForeignKey(
        CustomUser, related_name='rating_to', on_delete=models.CASCADE)
    f_rating = models.DecimalField(default=0, max_digits=2, decimal_places=1)
    e_rating = models.DecimalField(default=0, max_digits=2, decimal_places=1)

    def __str__(self):
        return str(self.task.id)+"--"+str(self.fre.user.username)+"--"+str(self.emp.user.username)


class Notification(models.Model):
    _from = models.ForeignKey(
        CustomUser, related_name="msgfrom", on_delete=models.CASCADE)
    _to = models.ForeignKey(
        CustomUser, related_name='msgto', on_delete=models.CASCADE)
    message = models.CharField(default=None, max_length=300)
    has_read = models.BooleanField(default=False)
    sending_time = models.DateTimeField(auto_now_add=True, blank=True)
    recieving_time = models.DateTimeField(default=None, blank=True, null=True)