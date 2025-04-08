from django.shortcuts import render, redirect
from .forms import RankForm, TestCaseForm
from .models import Rank, Department, TestCase

def run_test_cases(test_cases):
    results = []
    for test in test_cases:
        rank = test.input_rank
        expected_department_name = test.expected_department
        valid = test.valid
        
        if valid:
            department = Department.objects.filter(name=expected_department_name).first()
            if department:
                result = Rank.objects.filter(rank=rank, department=department).exists()
            else:
                result = False
        else:
            result = not Rank.objects.filter(rank=rank).exists()
        
        results.append({
            'test_case_id': test.id,
            'input_rank': rank,
            'expected_department': expected_department_name,
            'result': result,
            'class': test.class_type
        })
    return results

def rank_allotment(request):
    if request.method == 'POST':
        rank_form = RankForm(request.POST)
        test_case_form = TestCaseForm(request.POST)
        
        if rank_form.is_valid():
            rank_form.save()
            return redirect('allotment:success')
        elif test_case_form.is_valid():
            test_case_form.save()
    else:
        rank_form = RankForm()
        test_case_form = TestCaseForm()

    # Get all test cases
    test_cases = TestCase.objects.all()
    test_results = run_test_cases(test_cases)

    return render(request, 'allotment/rank_form.html', {
        'rank_form': rank_form,
        'test_case_form': test_case_form,
        'test_results': test_results
    })

def success(request):
    return render(request, 'allotment/success.html')

# forms/rank_forms.py
from django import forms
from .models import Rank

class RankForm(forms.ModelForm):
    class Meta:
        model = Rank
        fields = '__all__'


