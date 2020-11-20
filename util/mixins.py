from typing import Dict, Final, Iterable, List, Any
from unities.models import Unity, UnityContent


class VisitContextMixin(object):

    __VISITED_CONTEXT: Final = 'page_visited'
    __VISITED_SESSION: Final = 'page_visited_session'
    __MENU_INFO_CONTEXT: Final = 'menu_elements'

    def get_context_data(self, *, object_list=None, **kwargs: Any) -> Dict[str, Any]:
        context = super(VisitContextMixin, self).get_context_data(object_list=object_list, **kwargs)

        try:
            if not self.request.session[self.__VISITED_SESSION]:
                self.request.session[self.__VISITED_SESSION] = True

        except KeyError:
            self.request.session[self.__VISITED_SESSION] = False

        context[self.__VISITED_CONTEXT] = self.request.session[self.__VISITED_SESSION]        
        context[self.__MENU_INFO_CONTEXT] = self.__get_info_menu()

        return context

    def __get_info_menu(self) -> Iterable[Dict[str,str]]:
        menu_info:List[Dict[str,str]] = []
        for unity in Unity.objects.all():
            list_content_info = []
            for content in UnityContent.objects.filter(unity=unity):
                list_content_info.append({
                    'url': content.get_absolute_url(),
                    'title': content.title
                })
            menu_info.append({
                'unity_number': unity.number,
                'slug': unity.slug,
                'content': list_content_info
            })
        return menu_info
# SAMPLE OF USAGE
# {% for info in menu_elements %}
#     <a href="{% url 'unity-content-list' info.slug %}">{{ info.unity_number }}</a>
#     {% for content in info.content %}
#     <h5><a href='{{ content.url }}'>{{ content.title }}</a></h5>
#     {% endfor %}
#   {% endfor %}
