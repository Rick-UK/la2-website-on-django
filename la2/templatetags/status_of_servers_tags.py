from random import randint
from django import template

register = template.Library()

@register.inclusion_tag("la2/status_of_servers.html")
def get_status_of_servers():
    status_of_servers = get_servers_info()
    return {"status_of_servers": status_of_servers}

def get_servers_info():
    servers_info = {
        'x2':randint(0,5000),
        'x50':randint(0,4000),
        'x1200': randint(0,3000)
    }
    return servers_info
