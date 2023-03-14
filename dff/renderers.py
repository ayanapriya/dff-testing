from rest_framework.renderers import JSONRenderer


class EmbedJSONRenderer(JSONRenderer):
    # https://www.django-rest-framework.org/api-guide/renderers/#renderers
    # https://stackoverflow.com/questions/20424521/override-jsonserializer-on-django-rest-framework

    def render(
            self, data, accepted_media_type=None, renderer_context=None
    ):
        response = {}
        try:
            if isinstance(data['status'], int):
                status = data.pop('status', 1)
                response['status'] = status
            else:
                status = 1
                response['status'] = status
        except (KeyError, AttributeError, TypeError):
            status = 1
        message = data.pop(
            'detail', None) if isinstance(data, dict) \
            else None
        if hasattr(renderer_context['response'],
                   'custom_response_message'):
            message = renderer_context[
                'response'].custom_response_message
        if not status:
            response['data'] = {}
            if data:
                response['errors'] = data
                if not message:
                    message = 'Invalid data'
        else:
            response['data'] = data
            response['status'] = status
            if not message:
                message = 'Success'

        response['message'] = message
        return super(EmbedJSONRenderer, self).render(
            response, accepted_media_type, renderer_context)
