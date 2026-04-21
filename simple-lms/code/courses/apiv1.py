from ninja import NinjaAPI

from .schemas import CourseOut
from .models import Course
from typing import List

apiv1 = NinjaAPI()

@apiv1.get('hello/')
def helloapi(request):
    return "Menyala abangkuh ..."

@apiv1.get('courses/', response=list[CourseOut])
def listCourse(request):
    """mengambil daftar semua course."""
    return Course.objects\
        .select_related('teacher')\
        .all()