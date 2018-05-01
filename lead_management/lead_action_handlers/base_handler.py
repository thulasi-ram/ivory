import abc


class BaseActionHandler(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    @abc.abstractmethod
    def handle(self, **kwargs):
        pass
