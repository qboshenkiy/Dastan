from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Survey, Response
from .forms import ResponseForm
from django.shortcuts import render

def success(request):
    return render(request, 'surveys/success.html')



def survey_detail(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)

    form = ResponseForm(request.POST or None)

    if form.is_bound:
        if form.is_valid():
            response = form.save(commit=False)
            response.survey = survey
            response.save()
            return redirect('success')  # Используйте имя URL для страницы подтверждения

    return render(request, 'surveys/survey_detail.html', {'survey': survey, 'form': form})




def survey_list(request):
    surveys = Survey.objects.all()
    return render(request, 'surveys/survey_list.html', {'surveys': surveys})

