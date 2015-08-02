from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from Organizer.models import Department
from Organizer.models import Advisor
from Organizer.models import Student
from Organizer.models import Course
from Organizer.models import Degree
from Organizer.models import Certificate
from Organizer.models import Degree_Core_Course_Structure
from Organizer.models import Degree_Elective_Course_Structure
from Organizer.models import Certificate_Course_Structure


def index(request):
    department_list = Department.objects.all()
    template = loader.get_template('Organizer/index.html')
    context = RequestContext(request, {
        'department_list': department_list
    })
    return HttpResponse(template.render(context))

def index2(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    return render(request, 'Organizer/index2.html', {'department': department})

def advisorinfo(request, department_id, advisor_id):
    department = get_object_or_404(Department, pk=department_id)
    advisor = get_object_or_404(Advisor, pk = advisor_id)
    return render(request, 'Organizer/advisorinfo.html', {'department': department, 'advisor': advisor})

def detail(request, department_id, advisor_id):
    department = get_object_or_404(Department, pk=department_id)
    advisor = get_object_or_404(Advisor, pk=advisor_id)
    return render(request, 'Organizer/detail.html', {'department': department,'advisor': advisor})

def advisordegree(request, department_id, advisor_id):
    department = get_object_or_404(Department, pk=department_id)
    advisor = get_object_or_404(Advisor, pk=advisor_id)
    return render(request, 'Organizer/advisordegree.html', {'department': department,'advisor': advisor})

def degree(request, department_id, degree_id):
    department = get_object_or_404(Department, pk=department_id)
    degree = get_object_or_404(Degree, pk=degree_id)
    return render(request, 'Organizer/degree.html', {'department': department,'degree': degree})

def coursedegree(request, degree_id, degree_core_course_structure_id):
    core_course_structure = get_object_or_404(Degree_Core_Course_Structure, pk=degree_core_course_structure_id)
    return render(request, 'Organizer/coursedegree.html', {'core_course_structure': core_course_structure})

def certificate(request, department_id, certificate_id):
    department = get_object_or_404(Department, pk=department_id)
    certificate = get_object_or_404(Certificate, pk=certificate_id)
    return render(request, 'Organizer/certificate.html', {'department': department,'certificate': certificate})
# Create your views here.
