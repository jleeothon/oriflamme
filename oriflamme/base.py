import logging

logger = logging.getLogger(__name__)

class FlagMixin(object):

    template_flags = tuple()

    def get_context_data(self, **kwargs):
        context = super(FlagMixin, self).get_context_data(**kwargs)
        for flag in self.template_flags:
            if flag in context:
                logger.error("Object %s already exists in %s" % (flag, self))
            context[flag] = True
        return context
