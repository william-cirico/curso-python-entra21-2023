from django import template
import re

register = template.Library()

@register.filter(name="format_phone")
def format_phone(value):
    phone_pattern = r"(\d{2})(\d)?(\d{4})(\d{4})"
    
    match = re.match(phone_pattern, value)
    if match:
        return "({}) {} {}-{}".format(*match.groups())
    
    return value