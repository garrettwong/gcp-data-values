import json
import os


def get_all_google_cloud_regions():
    """
    Gets all available Google Cloud regions and returns them as a list.

    Returns:
      A list of strings, where each string is a Google Cloud region identifier.
    """
    try:
        from googleapiclient.discovery import build
    except ImportError:
        print("Please install the google-api-python-client library to use this function.")
        return []

    service = build('compute', 'v1')
    regions = service.regions().list(
        project=os.environ['PROJECT_ID']).execute()
    return [region['name'] for region in regions['items']]


def get_all_google_cloud_zones():
    """
    Gets all available Google Cloud zones and returns them as a list.

    Returns:
      A list of strings, where each string is a Google Cloud zone identifier.
    """
    try:
        from googleapiclient.discovery import build
    except ImportError:
        print("Please install the google-api-python-client library to use this function.")
        return []

    service = build('compute', 'v1')
    zones = service.zones().list(
        project=os.environ['PROJECT_ID']).execute()
    return [zone['name'] for zone in zones['items']]


# data/regions.json
regions = get_all_google_cloud_regions()
with open('data/regions.json', 'w') as f:
    json.dump(regions, f, indent=2)

# data/zones.json
zones = get_all_google_cloud_zones()
with open('data/zones.json', 'w') as f:
    json.dump(zones, f, indent=2)
