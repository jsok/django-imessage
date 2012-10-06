from django.shortcuts import render_to_response
from django.template import RequestContext

from messages.models import Message, Handle

def index(request, template_name="messages/index.html"):

    context = {
        "handles": Handle.objects.all()
    }

    return render_to_response(template_name,
            RequestContext(request, context))

def messages(request, handle_id, template_name="messages/messages.html"):

    handle = Handle.objects.get(pk=handle_id)

    context = {
        "handle": handle,
    }

    return render_to_response(template_name,
            RequestContext(request, context))
