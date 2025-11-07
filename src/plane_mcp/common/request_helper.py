"""HTTP request helper for Plane API."""

import os
from typing import Any, Optional

import httpx


class PlaneAPIError(Exception):
    """Exception raised for Plane API errors."""


async def make_plane_request(
    method: str,
    path: str,
    body: Optional[dict[str, Any]] = None,
    timeout: float = 30.0,
) -> Any:
    """
    Make an HTTP request to Plane API.
    
    Args:
        method: HTTP method (GET, POST, PATCH, DELETE)
        path: API path (without /api/v1/ prefix)
        body: Request body for POST/PATCH requests
        timeout: Request timeout in seconds
        
    Returns:
        Response data as dict/list
        
    Raises:
        PlaneAPIError: If the request fails
    """
    host_url = os.getenv("PLANE_API_HOST_URL", "https://api.plane.so/")
    host = host_url if host_url.endswith("/") else f"{host_url}/"
    url = f"{host}api/v1/{path}"
    
    api_key = os.getenv("PLANE_API_KEY", "")
    if not api_key:
        raise PlaneAPIError("PLANE_API_KEY environment variable is not set")
    
    headers = {
        "X-API-Key": api_key,
    }
    
    # Add Content-Type for non-GET requests
    if method.upper() != "GET":
        headers["Content-Type"] = "application/json"
    
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            if method.upper() == "GET":
                response = await client.get(url, headers=headers)
            elif method.upper() == "POST":
                response = await client.post(url, headers=headers, json=body)
            elif method.upper() == "PATCH":
                response = await client.patch(url, headers=headers, json=body)
            elif method.upper() == "DELETE":
                response = await client.delete(url, headers=headers)
            else:
                raise PlaneAPIError(f"Unsupported HTTP method: {method}")
            
            response.raise_for_status()
            return response.json()
            
    except httpx.HTTPStatusError as e:
        error_msg = f"HTTP {e.response.status_code}: {e.response.text}"
        raise PlaneAPIError(error_msg) from e
    except httpx.RequestError as e:
        raise PlaneAPIError(f"Request failed: {str(e)}") from e
    except Exception as e:
        raise PlaneAPIError(f"Unexpected error: {str(e)}") from e
