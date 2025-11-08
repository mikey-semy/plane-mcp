"""Project tools for Plane API."""

import json
import os
from typing import Optional

from mcp.server.fastmcp import FastMCP

from plane_mcp.common.request_helper import make_plane_request


def register_project_tools(mcp: FastMCP) -> None:
    """Register project-related tools."""

    @mcp.tool()
    async def get_projects() -> str:
        """Get all projects for the current user."""
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "GET",
            f"workspaces/{workspace_slug}/projects/"
        )

        # Simplify response
        if isinstance(response, dict) and "results" in response:
            projects = [
                {
                    "name": p.get("name"),
                    "id": p.get("id"),
                    "identifier": p.get("identifier"),
                    "description": p.get("description"),
                    "project_lead": p.get("project_lead"),
                }
                for p in response["results"]
            ]
            return json.dumps(projects, indent=2)

        return json.dumps(response, indent=2)

    @mcp.tool()
    async def create_project(
        name: str,
        identifier: str,
        description: Optional[str] = None
    ) -> str:
        """
        Create a new project.

        Args:
            name: The name of the project
            identifier: The identifier of the project (typically 5 uppercase characters)
            description: Optional project description
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")

        body = {
            "name": name,
            "identifier": identifier.upper().replace(" ", ""),
        }
        if description:
            body["description"] = description

        response = await make_plane_request(
            "POST",
            f"workspaces/{workspace_slug}/projects/",
            body=body
        )
        return json.dumps(response, indent=2)
