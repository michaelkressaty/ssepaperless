from django.contrib import admin
from Organizer.models import Department
from Organizer.models import Advisor
from Organizer.models import Student
from Organizer.models import Course
from Organizer.models import Degree
from Organizer.models import Certificate
from Organizer.models import Degree_Core_Course_Structure
from Organizer.models import Degree_Elective_Course_Structure
from Organizer.models import Certificate_Course_Structure

class RequiredCourseInline(admin.TabularInline):
	model = Course.RequiredCore.through

class ElectiveCourseInline(admin.TabularInline):
	model = Course.ElectiveOption.through

class ElectiveAdmin(admin.ModelAdmin):
	inlines = [ElectiveCourseInline,]

class CertificateCourseInline(admin.TabularInline):
	model = Course.CertificateRequiredCourse.through

class CertificateAdmin(admin.ModelAdmin):
	inlines = [CertificateCourseInline,]

class StudentInline(admin.TabularInline):
	model = Student
	extra = 0

class AdvisorAdmin(admin.ModelAdmin):
	inlines = [StudentInline,]

class ElectiveCoursesInline(admin.TabularInline):
	model = Degree_Elective_Course_Structure
	extra = 3


class RequiredCoreAdmin(admin.ModelAdmin):
	inlines = [RequiredCourseInline,ElectiveCoursesInline]

admin.site.register(Department)
admin.site.register(Advisor, AdvisorAdmin)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Degree)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Degree_Core_Course_Structure, RequiredCoreAdmin)
admin.site.register(Degree_Elective_Course_Structure, ElectiveAdmin)



# Register your models here.
