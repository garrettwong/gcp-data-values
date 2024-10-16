import unittest
from unittest.mock import patch, Mock
from src.main import get_all_google_cloud_regions

class TestGetAllGoogleCloudRegions(unittest.TestCase):

    @patch('googleapiclient.discovery.build')
    def test_get_all_google_cloud_regions_success(self, mock_build):
        # Mock the API response
        mock_service = Mock()
        mock_service.regions.return_value.list.return_value.execute.return_value = {
            'items': [
                {'name': 'us-central1'},
                {'name': 'europe-west1'}
            ]
        }
        mock_build.return_value = mock_service

        # Call the function
        regions = get_all_google_cloud_regions()

        # Assert the results
        self.assertEqual(regions, ['us-central1', 'europe-west1'])


if __name__ == '__main__':
    unittest.main()