import unittest
from unittest.mock import patch, Mock
from src.main import execute_compute_method


class TestGetAllGoogleCloudRegions(unittest.TestCase):

    @patch('googleapiclient.discovery.build')
    def test_get_all_google_cloud_regions_success(self, mock_build):
        # Mock the API response
        mock_service = Mock()
        mock_service.regions.return_value.list.return_value.execute.return_value = [
            'us-central1',
            'europe-west1'
        ]
        mock_build.return_value = mock_service

        # Call the function
        regions = execute_compute_method('regions', 'list')

        # Assert the results
        self.assertEqual(regions, ['us-central1', 'europe-west1'])


if __name__ == '__main__':
    unittest.main()
