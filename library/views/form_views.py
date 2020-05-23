# Saves Form - Unlisted & Edit
from django.http import JsonResponse
from django.template.loader import render_to_string

from library.forms import DemoForm


def save_content_form(request, form, template_name, context):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


# Demo Form
def demo(request):
    if request.method == 'POST':
        form = DemoForm(request.POST)
    else:
        form = DemoForm()
    context = {'form': form,
               'class': 'js-form',
               'action': request.path,
               'header': "Demo Form",
               'cancel': "Cancel",
               'submit': "Submit"}
    return save_content_form(request, form, 'library/includes/generic_modal_form.html', context)