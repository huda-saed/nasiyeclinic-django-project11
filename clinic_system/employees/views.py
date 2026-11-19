from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employee
from .forms import EmployeeForm


@login_required
def employee_register(request):
    """Employee Registration page - inserts the submitted form into the database."""
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Shaqaalaha si guul leh ayaa loo diiwaan geliyay!")
            return redirect('employee_register')
    else:
        form = EmployeeForm()
    employees = Employee.objects.all()
    return render(request, 'employees/employee_form.html', {'form': form, 'employees': employees})
