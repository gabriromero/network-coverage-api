import requests

class ClientBase:
    """Base client to handle API requests with a persistent session."""

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def make_request(self, endpoint, method="GET", params=None, data=None, json=None, headers=None):
        """
        Generic method to make API requests.
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.request(method, url, params=params, data=data, json=json, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data from API: {e}")
            return None

    def close(self):
        """Close the session when the client is no longer needed."""
        self.session.close()
