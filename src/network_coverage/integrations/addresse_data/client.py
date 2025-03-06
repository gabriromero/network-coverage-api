from network_coverage.integrations.client_base import ClientBase


class AddresseDataClient(ClientBase):
    """Client to interact with the French address API (https://api-adresse.data.gouv.fr)."""

    def __init__(self):
        super().__init__(base_url="https://api-adresse.data.gouv.fr")

    def search_location(self, address):
        """
        Search for an address using the API.

        :param address: The address query string (e.g., '8 bd du port').
        :return: A dictionary containing the API response or None if an error occurs.
        """
        params = {"q": address}
        return self.make_request("/search", method="GET", params=params)
