from unittest import TestCase
from django import forms


class TestCaseForm(forms.ModelForm):
    class Meta:
        model = TestCase
        fields = ['input_rank', 'expected_department', 'valid']