"""Test different API endpoint variations to find what works."""

import asyncio
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

API_HOST = os.getenv("PLANE_API_HOST_URL", "https://plane.equiply.ru/")
API_KEY = os.getenv("PLANE_API_KEY", "")
WORKSPACE_SLUG = os.getenv("PLANE_WORKSPACE_SLUG", "profitool-store")

# Remove trailing slash for consistency
API_HOST = API_HOST.rstrip("/")

# Test variations
TEST_CASES = [
    # Format: (name, url_pattern, description)
    ("v1_users_me", f"{API_HOST}/api/v1/users/me/", "External API v1 - users/me"),
    ("v1_workspaces", f"{API_HOST}/api/v1/workspaces/{WORKSPACE_SLUG}/", "External API v1 - workspace"),
    ("app_users_me", f"{API_HOST}/api/users/me/", "Web App API - users/me"),
    ("app_workspaces", f"{API_HOST}/api/workspaces/{WORKSPACE_SLUG}/", "Web App API - workspace"),
    ("v1_no_trailing", f"{API_HOST}/api/v1/users/me", "External API v1 - no trailing slash"),
    ("app_no_trailing", f"{API_HOST}/api/users/me", "Web App API - no trailing slash"),
]

# Test with different header variations
HEADER_VARIATIONS = [
    ("X-API-Key", "Standard header"),
    ("X-Api-Key", "Mixed case header"),
    ("Authorization", "Bearer token style", True),  # True = use Bearer prefix
]


async def test_endpoint(url: str, header_name: str, use_bearer: bool = False):
    """Test a single endpoint with specific header."""
    headers = {}
    if use_bearer:
        headers[header_name] = f"Bearer {API_KEY}"
    else:
        headers[header_name] = API_KEY
    
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url, headers=headers)
            return {
                "status": response.status_code,
                "success": response.status_code == 200,
                "error": None if response.status_code == 200 else response.text[:200]
            }
    except Exception as e:
        return {
            "status": None,
            "success": False,
            "error": str(e)[:200]
        }


async def run_tests():
    """Run all test combinations."""
    print("=" * 80)
    print("TESTING PLANE API ENDPOINTS")
    print("=" * 80)
    print(f"Host: {API_HOST}")
    print(f"Workspace: {WORKSPACE_SLUG}")
    print(f"API Key: {API_KEY[:20]}...")
    print("=" * 80)
    print()
    
    results = []
    
    for test_name, url, description in TEST_CASES:
        print(f"\n{'─' * 80}")
        print(f"TEST: {test_name}")
        print(f"Description: {description}")
        print(f"URL: {url}")
        print(f"{'─' * 80}")
        
        for header_name, header_desc, *use_bearer_args in HEADER_VARIATIONS:
            use_bearer = use_bearer_args[0] if use_bearer_args else False
            
            result = await test_endpoint(url, header_name, use_bearer)
            
            status_icon = "✅" if result["success"] else "❌"
            header_display = f"{header_name}: Bearer {{token}}" if use_bearer else f"{header_name}: {{token}}"
            
            print(f"  {status_icon} {header_display:<40} | Status: {result['status']}")
            
            if not result["success"] and result["error"]:
                error_preview = result["error"].replace("\n", " ")[:100]
                print(f"     Error: {error_preview}")
            
            results.append({
                "test": test_name,
                "url": url,
                "header": header_display,
                "status": result["status"],
                "success": result["success"],
                "error": result["error"]
            })
    
    # Summary
    print("\n")
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    successful = [r for r in results if r["success"]]
    
    if successful:
        print(f"\n✅ WORKING CONFIGURATIONS ({len(successful)}):")
        for r in successful:
            print(f"  • {r['test']}: {r['url']}")
            print(f"    Header: {r['header']}")
    else:
        print("\n❌ NO WORKING CONFIGURATIONS FOUND")
    
    print(f"\nTotal tests: {len(results)}")
    print(f"Successful: {len(successful)}")
    print(f"Failed: {len(results) - len(successful)}")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(run_tests())
