
class FlagMixin(object):

    template_flags = tuple()

    def get_context_data(self, **kwargs):
        context = super(FlagMixin, self).get_context_data(**kwargs)
        for flag in self.template_flags:
            context[flag] = True
        return context
