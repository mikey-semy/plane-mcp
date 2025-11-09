"""Test External API after Plane update to v1.1.0."""

import asyncio
import httpx

API_HOST = "https://plane.equiply.ru"
API_KEY = "plane_api_e63e2f6e51ef4192bc817216b2ed8a58"

async def test_v1_api():
    """Test if External API v1 is available after update."""
    url = f"{API_HOST}/api/v1/users/me/"
    headers = {"X-API-Key": API_KEY}
    
    print(f"Testing: {url}")
    print(f"Header: X-API-Key: {API_KEY[:20]}...")
    print("-" * 60)
    
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url, headers=headers)
            
            print(f"Status: {response.status_code}")
            print(f"Response:\n{response.text[:500]}")
            
            if response.status_code == 200:
                print("\n✅ SUCCESS! External API v1 works!")
                return True
            elif response.status_code == 404:
                print("\n❌ Still 404 - Plane not updated or services not started")
                return False
            else:
                print(f"\n⚠️ Unexpected status: {response.status_code}")
                return False
                
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False

if __name__ == "__main__":
    asyncio.run(test_v1_api())
