from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect


def notes_view(request):
    theme = request.COOKIES.get('theme', 'light')

    if theme not in ['light', 'dark']:
        theme = 'light'

    response = render(request, 'notes.html', {'theme': theme})
    return response


def toggle_theme(request):
    if request.method == 'POST':
        new_theme = request.POST.get('theme', 'light')

        if new_theme in ['light', 'dark']:
            theme = new_theme
        else:
            theme = 'light'

        response = HttpResponseRedirect(reverse('notes:notes'))
        response.set_cookie('theme', theme, max_age=30 * 24 * 3600)
        return response

    return HttpResponseRedirect(reverse('notes:notes'))
