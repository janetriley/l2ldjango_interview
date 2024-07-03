from django import template
from datetime import datetime

register = template.Library()
ISO_INPUT_FORMAT = '%Y-%m-%dT%H:%M:%S'
L2L_DT_OUTPUT_FORMAT = '%Y-%m-%d %H:%M:%S'


@register.filter()
def l2l_dt(value: str | datetime) -> str:
    if type(value) is str:
        value = datetime.strptime(value, ISO_INPUT_FORMAT)
    return value.strftime(L2L_DT_OUTPUT_FORMAT)
