from django.shortcuts import render, redirect
from .models import School, Student


def school_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            school = School.objects.get(username=username, password=password)

            request.session["school_id"] = school.id

            return redirect("dashboard")

        except:
            return render(request,"login.html",{"error":"Invalid Login"})

    return render(request,"login.html")

def logout_view(request):
    request.session.flush()
    return redirect("login")


def dashboard(request):

    school_id = request.session.get("school_id")

    if not school_id:
        return redirect("login")

    school = School.objects.get(id=school_id)

    return render(request,"dashboard.html",{"school":school})


def students(request):

    school_id = request.session.get("school_id")

    students = Student.objects.filter(school_id=school_id)

    return render(request,"students.html",{"students":students})


def add_student(request):

    school_id = request.session.get("school_id")

    if request.method == "POST":

        name = request.POST.get("name")
        student_class = request.POST.get("student_class")
        roll = request.POST.get("roll")

        school = School.objects.get(id=school_id)

        Student.objects.create(
            school=school,
            name=name,
            student_class=student_class,
            roll=roll
        )

        return redirect("students")

    return render(request,"add_student.html")


def edit_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":

        student.name = request.POST.get("name")
        student.student_class = request.POST.get("student_class")
        student.roll = request.POST.get("roll")

        student.save()

        return redirect("students")

    return render(request, "edit_student.html", {"student": student})


def delete_student(request,id):

    student = Student.objects.get(id=id)
    student.delete()

    return redirect("students")

def students(request):

    school_id = request.session.get("school_id")

    query = request.GET.get("q")

    students = Student.objects.filter(school_id=school_id)

    if query:
        students = students.filter(name__icontains=query)

    return render(request,"students.html",{"students":students})