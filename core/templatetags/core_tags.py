import datetime, pytz

from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def time_greeting() -> str:
    """ Template tag to return a greeting in spanish, that will change
    with the time of the user
    Returns
    --------
        greeting: str
            Return the greeting, that will change with the actual hour
    """
    current_time = datetime.datetime.now(tz=pytz.timezone(str(settings.TIME_ZONE)))
    if current_time.hour < 12:
        return 'Buenos dias'
    elif current_time.hour >= 12 and current_time.hour < 18:
        return 'Buenas tardes'
    else:
        return 'Buenas noches'
