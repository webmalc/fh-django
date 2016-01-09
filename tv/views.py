from django.views.generic import ListView, DetailView
from tv.models import Channel


class ChannelList(ListView):
    """
    Channels list
    """
    model = Channel
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(ChannelList, self).get_context_data(**kwargs)
        channels = {}
        channels['Kids'] = []
        for channel in context['object_list']:
            if channel.category not in channels:
                channels[channel.category] = []
            channels[channel.category].append(channel)
        context['channels'] = channels
        return context


class ChannelShow(DetailView):
    model = Channel

