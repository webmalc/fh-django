from collections import OrderedDict
from django.views.generic import ListView, DetailView, UpdateView
from tv.models import Channel


class ChannelList(ListView):
    """
    Channels list
    """
    model = Channel
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(ChannelList, self).get_context_data(**kwargs)
        channels = OrderedDict()
        for channel in context['object_list']:
            if channel.category not in channels:
                channels[channel.category] = []
            channels[channel.category].append(channel)
        context['channels'] = channels
        context['icons'] = Channel.CATEGORIES
        return context

    def get_queryset(self):
        return Channel.objects.all().filter(is_enabled=True)


class ChannelShow(UpdateView):
    """
    Channel show
    """
    model = Channel
    fields = ['is_favorite']

