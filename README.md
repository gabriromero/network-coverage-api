# Network Coverage API

The **Network Coverage API** provides information on network coverage (2G, 3G, 4G) for major mobile service providers at a given location. You can query network coverage for a specific address using a simple HTTP GET API.

## Description

This API returns the network coverage for mobile operators (Orange, SFR, Free, Bouygues) for a given location. The response contains information about the availability of 2G, 3G, and 4G networks for each operator based on the provided address.

## Endpoints

### `GET /`

#### Query Parameters:

- `q` (required): The address you want to query. You can use a complete address, like "42 rue 75011 Paris".

#### Example Response:

```json
{
    "orange": {
        "2G": true,
        "3G": true,
        "4G": false
    },
    "SFR": {
        "2G": true,
        "3G": true,
        "4G": true
    },
    "Free": {
        "2G": true,
        "3G": false,
        "4G": true
    },
    "Bouygues": {
        "2G": true,
        "3G": true,
        "4G": true
    }
}
```

## Dependencies

This project uses the following dependencies:

### 1. **Django** (>=5.1.6, <6.0.0)

[Django](https://www.djangoproject.com/) is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It is used in this project to handle the web server, routing, and basic application structure.

- **Usage**: Provides the framework for building the web API and handling HTTP requests.

### 2. **Django REST Framework** (>=3.15.2, <4.0.0)

[Django REST Framework](https://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs in Django. It simplifies the process of building RESTful APIs by providing serialization, authentication, viewsets, and other features.

- **Usage**: Used to create the API endpoints, handle HTTP methods (GET), serialize the response data, and manage the communication between the frontend and the backend.

### 3. **PyProj** (>=3.7.1, <4.0.0)

[PyProj](https://pyproj4.github.io/pyproj/) is a Python interface to the PROJ library, which is used for transforming geographic coordinate points from one coordinate system to another. This is crucial for converting Lambert 93 coordinates to GPS (longitude and latitude) coordinates.

- **Usage**: Used for converting coordinates from Lambert 93 (French national coordinate system) to GPS coordinates. This allows the system to determine the precise location based on user input.

### 4. **Requests** (>=2.32.3, <3.0.0)

[Requests](https://requests.readthedocs.io/en/latest/) is a simple and elegant HTTP library for Python. It is designed to handle HTTP requests easily and with a simple API.

- **Usage**: Used for making HTTP requests to external APIs, specifically to the [adresse.data.gouv.fr](https://adresse.data.gouv.fr/api) API. This API is used to retrieve detailed geographic information (e.g., GPS coordinates) based on the provided address.

### 5. **Pydantic** (>=2.10.6, <3.0.0)

[Pydantic](https://pydantic-docs.helpmanual.io/) is a data validation and settings management library for Python. It uses Python type annotations to validate and serialize input/output data.

- **Usage**: Used for validating the query parameters and ensuring the correct data format for the address input. It helps to ensure that only valid data is passed to the backend for further processing.

### Installation

To install all the necessary dependencies, use **Poetry**:

```bash
poetry install
