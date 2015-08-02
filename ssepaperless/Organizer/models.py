from django.db import models

class Department(models.Model):
    DepartmentName = models.CharField(max_length=75)
    def __str__(self):              # __unicode__ on Python 2
        return self.DepartmentName

class Advisor(models.Model):
    id = models.AutoField(primary_key=True)
    AdvisorName = models.CharField(max_length=200)
    Department = models.ForeignKey(Department)
    def __str__(self):              # __unicode__ on Python 2
       return self.AdvisorName

class Student(models.Model):
    StudentName = models.CharField(max_length=75)
    Advisor = models.ForeignKey(Advisor)
    StudentID = models.IntegerField(max_length=8)
    SemesterAccepted = models.CharField(max_length = 5, default = "S2105")
    StudyPlanChoices = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('IP', 'In Progress')
    )
    StudyPlanApproved = models.CharField(max_length=2, choices = StudyPlanChoices, default = 'Y')
    StudyPlanPDF = models.FileField(upload_to='StudyPlanPDF/', blank = True)
    def __str__(self):              # __unicode__ on Python 2
        return self.StudentName


class Degree(models.Model):
    DegreeName = models.CharField(max_length=75)
    Advisors = models.ManyToManyField(Advisor)
    Department = models.ManyToManyField(Department)
    def __str__(self):              # __unicode__ on Python 2
        return self.DegreeName

class Certificate(models.Model):
    CertificateName = models.CharField(max_length=200)
    Department = models.ManyToManyField(Department)
    def __str__(self):              # __unicode__ on Python 2
            return self.CertificateName

class Degree_Core_Course_Structure(models.Model):
    Degree_Core_Course_Structure_ID = models.CharField(max_length=50)
    Degree = models.ForeignKey(Degree)
    def __str__(self):              # __unicode__ on Python 2
        return self.Degree_Core_Course_Structure_ID

class Degree_Elective_Course_Structure(models.Model):
    Degree_Elective_Course_Structure_ID = models.CharField(max_length=50)
    CoreRelation = models.OneToOneField(Degree_Core_Course_Structure)
    Choose = models.IntegerField(max_length=2)
    def __str__(self):              # __unicode__ on Python 2
        return self.Degree_Elective_Course_Structure_ID

class Certificate_Course_Structure(models.Model):
    Certificate_Course_Structure_ID = models.CharField(max_length=50)
    Certificate = models.ForeignKey(Certificate)
    def __str__(self):              # __unicode__ on Python 2
        return self.Certificate_Course_Structure_ID


class Course(models.Model):
    CourseName = models.CharField(max_length=200)
    CourseID = models.CharField(max_length=10)
    Credits = models.IntegerField(max_length=2)
    RequiredCore = models.ManyToManyField(Degree_Core_Course_Structure, blank = True)
    ElectiveOption = models.ManyToManyField(Degree_Elective_Course_Structure, blank = True)
    CertificateRequiredCourse = models.ManyToManyField(Certificate, blank = True)
    def __str__(self):              # __unicode__ on Python 2
       return self.CourseName
    def __str__(self):              # __unicode__ on Python 2
       return self.CourseID
# Create your models here.
