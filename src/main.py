import json
import os

from services.json_service import write_json_with_replacement


def execute_compute_method(sub_service_name, method):
    """
    Gets all available Google Cloud disks and returns them as a list.

    Returns:
      A list of strings, where each string is a Google Cloud region identifier.
    """
    try:
        from googleapiclient.discovery import build
    except ImportError:
        print("Please install the google-api-python-client library to use this function.")
        return []

    service = build('compute', 'v1')

    sub_service = getattr(service, sub_service_name)()
    results = getattr(sub_service, method)(
        project=os.environ['PROJECT_ID']).execute()

    return results


# dynamic - https://cloud.google.com/compute/docs/reference/rest/v1/machineTypes/list
method_list = [
    ('acceleratorTypes', 'aggregatedList'),
    ('diskTypes', 'aggregatedList'),
    ('machineTypes', 'aggregatedList'),
    ('nodeTypes', 'aggregatedList'),
    ('regions', 'list'),
    ('zones', 'list')
]

new_string='[PROJECT_ID]'
for sub_service, methodname in method_list:
    print(sub_service, methodname)
    results = execute_compute_method(sub_service, methodname)
    f = f'data/{sub_service}.json'
    write_json_with_replacement(
        results, filename=f, old_string=os.environ['PROJECT_ID'], new_string=new_string)
