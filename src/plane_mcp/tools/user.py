"""User tools for Plane API."""

import json
import os

from mcp.server.fastmcp import FastMCP

from plane_mcp.common.request_helper import make_plane_request


def register_user_tools(mcp: FastMCP) -> None:
    """Register user-related tools."""

    @mcp.tool()
    async def get_current_user() -> str:
        """Get information about the current authenticated user."""
        response = await make_plane_request("GET", "users/me/")
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def get_workspace_members() -> str:
        """Get all members in the current workspace."""
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request("GET", f"workspaces/{workspace_slug}/members/")
        return json.dumps(response, indent=2)
