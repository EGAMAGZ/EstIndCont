from core.models import ProsoftDoc
from typing import Final, Any, Dict, List


class VisitContextMixin(object):

    __VISITED_CONTEXT: Final = 'page_visited'
    __VISITED_SESSION: Final = 'page_visited_session'
    __MENU_INFO_CONTEXT: Final = 'menu_elements'
    
    def _get_info_menu(self) -> List[Dict[str, str]]:
        menu_info: List[Dict[str, str]] = []

        for document in ProsoftDoc.objects.order_by('created')[:5]:

            menu_info.append({
                'title': document.title,
                'url': document.get_absolute_url()
            })

        return menu_info

    def get_context_data(self, *, object_list=None, **kwargs: Any) -> Dict[str, Any]:
        context = super(VisitContextMixin, self).get_context_data(object_list=object_list, **kwargs)

        try:
            if not self.request.session[self.__VISITED_SESSION]:
                self.request.session[self.__VISITED_SESSION] = True

        except KeyError:
            self.request.session[self.__VISITED_SESSION] = False

        context[self.__VISITED_CONTEXT] = self.request.session[self.__VISITED_SESSION]
        context[self.__MENU_INFO_CONTEXT] = self._get_info_menu()

        return context

# SAMPLE OF USAGE
# {% for info in menu_elements %}
#     <a href="{% url 'unity-content-list' info.slug %}">{{ info.unity_number }}</a>
#     {% for content in info.content %}
#     <h5><a href='{{ content.url }}'>{{ content.title }}</a></h5>
#     {% endfor %}
#   {% endfor %}
