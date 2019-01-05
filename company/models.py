from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.


class Company(models.Model):
    c_id = models.IntegerField(unique=True, primary_key=True, verbose_name='Company ID')
    c_name = models.CharField(max_length=30, verbose_name='Company Name')
    c_email = models.CharField(max_length=30, verbose_name='Company E-mail')
    c_address = RichTextField(verbose_name='Company Address')
    c_phone = models.CharField(max_length=20, verbose_name = 'Company Phone')
    c_password = models.CharField(max_length=6,  verbose_name='Company Password')

    def __str__(self):
        return self.c_name


class ForeignCompany(Company):
    f_rating = models.IntegerField(verbose_name='Foreign Company Rating')
    #fCompany = models.ForeignKey(Company, unique=True, primary_key=True, verbose_name='Company ID')


class Department(models.Model):
    d_id = models.IntegerField(primary_key=True, verbose_name='Department ID')
    d_name = models.CharField(max_length=30, verbose_name='Department Name')
    d_capacity = models.IntegerField(verbose_name='Department Capacity')
    d_phone = models.IntegerField(verbose_name='Department Phone')
    d_password = models.CharField(max_length=6, verbose_name='Department Password')
    dCompany = models.ForeignKey(Company, verbose_name='Company Name')
    d_slug = models.SlugField(unique=True,editable=False, max_length=130)

    def __str__(self):
        return self.d_name

    def get_department_url(self):
        return reverse('app:detailD', kwargs={'d_slug': self.d_slug})

    def get_createD_url(self):
        return reverse('app:createD')

    def get_updateD_url(self):
        return reverse('app:updateD', kwargs={'d_slug': self.d_slug})

    def get_deleteD_url(self):
        return reverse('app:deleteD', kwargs={'d_slug': self.d_slug})

    def get_unique_D_slug(self):
        d_slug = slugify(self.d_name.replace('ı', 'i'))
        unique_slug = d_slug
        counter = 1
        while Department.objects.filter(d_slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(d_slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.d_slug = self.get_unique_D_slug()
        return super(Department, self).save(*args, **kwargs)


class Employee(models.Model):
    e_id = models.IntegerField(primary_key=True, serialize=False, verbose_name='Employee ID')
    e_name = models.CharField(max_length=30, verbose_name='Name')
    e_surname = models.CharField(max_length=30, verbose_name='Surname')
    e_password = models.CharField(max_length=6, verbose_name='Password')
    e_email = models.CharField(max_length=30, verbose_name='Email')
    e_phone = models.IntegerField(verbose_name='Phone')
    e_degree = models.IntegerField(verbose_name='Degree')
    e_salary = models.IntegerField(verbose_name='Salary')
    eDepartment = models.ForeignKey(Department, verbose_name="Department Name")
    eCompany = models.ForeignKey(Company, verbose_name="Company Name")
    e_slug = models.SlugField(unique=True,editable=False, max_length=130)

    def __str__(self):
        return self.e_name

    def get_absolute_url(self):
        return reverse('app:detail', kwargs={'e_slug': self.e_slug})

    def get_create_url(self):
        return reverse('app:create')

    def get_update_url(self):
        return reverse('app:update', kwargs={'e_slug': self.e_slug})

    def get_delete_url(self):
        return reverse('app:delete', kwargs={'e_slug': self.e_slug})

    def get_unique_E_slug(self):
        e_slug = slugify(self.e_name.replace('ı', 'i'))
        unique_slug = e_slug
        counter = 1
        while Employee.objects.filter(e_slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(e_slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.e_slug = self.get_unique_E_slug()
        return super(Employee, self).save(*args, **kwargs)


class Project(models.Model):
    p_id = models.IntegerField(primary_key=True, verbose_name='Project ID')
    p_startdate = models.DateTimeField(verbose_name='Project Start Date')
    p_enddate = models.DateTimeField(verbose_name='Project End Date')
    p_title = models.CharField(max_length=75, verbose_name='Project Title')
    p_situation = models.CharField(max_length=20, verbose_name='Project Situation')
    dProject = models.ForeignKey(Department, verbose_name='Department Name')
    image = models.ImageField(null=True, blank=True)
    p_slug = models.SlugField(unique=True,editable=False, max_length=130)

    def __str__(self):
        return self.p_title

    def get_project_url(self):
        return reverse('app:detailP', kwargs={'p_slug': self.p_slug})

    def get_createP_url(self):
        return reverse('app:createP')

    def get_updateP_url(self):
        return reverse('app:updateP', kwargs={'p_slug': self.p_slug})

    def get_deleteP_url(self):
        return reverse('app:deleteP', kwargs={'p_slug': self.p_slug})

    def get_unique_P_slug(self):
        p_slug = slugify(self.p_title.replace('ı', 'i'))
        unique_slug = p_slug
        counter = 1
        while Project.objects.filter(p_slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(p_slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.p_slug = self.get_unique_P_slug()
        return super(Project, self).save(*args, **kwargs)

    class Meta:
        ordering = ['p_enddate']

class Helps(models.Model):
    h_price = models.IntegerField(verbose_name='Project Price')
    h_type = models.CharField(max_length=50, verbose_name='Help Type')
    h_timestart = models.DateTimeField(verbose_name='Help Time Start')
    h_timeend = models.DateTimeField(verbose_name='Help Time End')
    pHelps = models.ForeignKey(Project, verbose_name='Which Project Helps (ID)')
    cHelps = models.ForeignKey(Company, verbose_name='Which Company Helps (ID)')


class Other(models.Model):
    o_studyproject = models.ForeignKey(Project, verbose_name='Works Project ID')
    eOther = models.ForeignKey(Employee, unique=True, primary_key=True, serialize=False, verbose_name='Employee')


class Head(models.Model):
    eHead = models.ForeignKey(Employee, unique=True, primary_key=True, serialize=False, verbose_name='Employee')
    h_degree = models.IntegerField(verbose_name='Head Degree')


class Issue(models.Model):
    i_id = models.IntegerField(unique=True, primary_key=True, verbose_name='Issue ID')
    i_type = models.CharField(max_length=30, verbose_name='Issue Type')
    i_extra = RichTextField(verbose_name='Issue Notes')
    i_content = RichTextField(verbose_name='Issue Content')
    pIssue = models.ForeignKey(Project, verbose_name='Project ID')


class Subtask(models.Model):
    sub_id = models.IntegerField(unique=True, primary_key=True, verbose_name='Subtask ID')
    iIssue = models.ForeignKey(Issue, verbose_name='Issue ID')


class ProjectPlan(models.Model):
    plan_id = models.IntegerField(unique=True, primary_key=True, verbose_name='Plan ID')
    plan_type = models.CharField(max_length=30, verbose_name='Plan Type')
    plan_date = models.DateTimeField(verbose_name='Plan Date')
    headMakes = models.ForeignKey(Head, verbose_name='Head ID')
    pProjectPlan = models.ForeignKey(Project, verbose_name='Project ID')


class WorkFlow(models.Model):
    w_type = models.CharField(max_length=30, verbose_name='Workflow Type')
    w_date = models.DateTimeField(verbose_name='Workflow Date')


class Report(models.Model):
    r_type = models.CharField(max_length=30, verbose_name='Report Type')
    r_version = models.CharField(max_length=5, verbose_name="Report Version")
    r_createdate = models.DateTimeField(verbose_name='Report Create Date')
    pReport = models.ForeignKey(Project, verbose_name='Project ID')
    oReport = models.ForeignKey(Other, verbose_name='Prepare Employee ID')
