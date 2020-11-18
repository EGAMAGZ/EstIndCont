from typing import Final


class VisitContextMixin(object):

    CONTEXT_NAME: Final = 'page_visited'
    SESSION_NAME: Final = 'page_visited_session'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VisitContextMixin, self).get_context_data(object_list=object_list, **kwargs)

        try:
            if not self.request.session[self.SESSION_NAME]:
                self.request.session[self.SESSION_NAME] = True

        except KeyError:
            self.request.session[self.SESSION_NAME] = False

        context[self.CONTEXT_NAME] = self.request.session[self.SESSION_NAME]
# https://docs.djangoproject.com/en/3.1/ref/models/querysets/#in-bulk
        return context
