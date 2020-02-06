import requests


def get_response(site_name):
    response = requests.get(site_name)
    return response.status_code



