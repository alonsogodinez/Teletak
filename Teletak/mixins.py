from django.contrib import messages



class SuccessMessageMixin(object):

    success_message = ''

    def form_valid(self, form):
        response = super(SuccessMessageMixin, self).form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)

        if  form.has_changed() and success_message:
            messages.success(self.request, success_message)

        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data


class JSONMixin(object):

    def render_to_response(self, context, **httpresponse_kwargs):
        return self.get_json_response(
            self.convert_context_to_json(context),
            **httpresponse_kwargs
        )

    def get_json_response(self, content, **httpresponse_kwargs):
        return HttpResponse(
            content,
            content_type='application/json',
            **httpresponse_kwargs
        )

    def convert_context_to_json(self, context):
        form = context.get('form')
        to_json = {}
        options = context.get('options', {})
        to_json.update(options=options)
        to_json.update(success=context.get('success', False))

        fields = {}
        for field_name, field in form.fields.items():
            if isinstance(field, DateField) \
                    and isinstance(form[field_name].value(), datetime.date):
                fields[field_name] = \
                    unicode(form[field_name].value().strftime('%d.%m.%Y'))
            else:
                fields[field_name] = \
                    form[field_name].value() \
                    and unicode(form[field_name].value()) \
                    or form[field_name].value()

        to_json.update(fields=fields)

        if form.errors:
            errors = {
                'non_field_errors': form.non_field_errors(),
            }
            fields = {}
            for field_name, text in form.errors.items():
                fields[field_name] = text
            errors.update(fields=fields)
            to_json.update(errors=errors)

        return json.dumps(to_json)