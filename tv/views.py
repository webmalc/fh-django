from django.views.generic import ListView, DetailView
from tv.models import Channel


class ChannelList(ListView):
    """
    Channels list
    """
    model = Channel
    paginate_by = 20


class ChannelShow(DetailView):
    model = Channel

