from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from network_coverage.core.csv_data_singleton import CsvDataSingleton
from network_coverage.integrations.addresse_data.client import AddresseDataClient
from network_coverage.schemas.dtos.addresse_data import FeatureSearch
from network_coverage.schemas.serializers.network_coverage import CoverageReadSerializer
from network_coverage.utils.coordinates import lamber93_to_gps

class CoverageViewSet(ViewSet):
    """
    A simple ViewSet for retrieving network coverage
    """

    def list(self, request):

        address = request.query_params.get('address')
        
        addresse_data_client = AddresseDataClient()
        location_response = addresse_data_client.search_location(address)

        if not location_response or not location_response.get('features'):
            return Response({'message': 'No location found'}, status=status.HTTP_404_NOT_FOUND)
        
        feature_search = FeatureSearch(**location_response['features'][0])
        site_mobile_data = CsvDataSingleton.get_site_mobile_data(
            (feature_search.properties.x, feature_search.properties.y)
        )

        if not site_mobile_data:
            return Response({'message': 'No data found'}, status=status.HTTP_404_NOT_FOUND)

        operator_code = site_mobile_data[0]
        coverage_result = site_mobile_data[1]

        response_serializer = CoverageReadSerializer(data={
            CsvDataSingleton.get_operator_name(operator_code): {bool(result) for result in coverage_result}
            
        })

        return Response(response_serializer.data, status=status.HTTP_200_OK)
