"""Module tools for Plane API."""

import json
import os
from typing import Optional

from mcp.server.fastmcp import FastMCP

from plane_mcp.common.request_helper import make_plane_request


def register_module_tools(mcp: FastMCP) -> None:
    """Register module-related tools."""

    @mcp.tool()
    async def list_modules(project_id: str) -> str:
        """
        Get all modules for a specific project.

        Args:
            project_id: The UUID identifier of the project
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "GET",
            f"workspaces/{workspace_slug}/projects/{project_id}/modules/"
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def get_module(project_id: str, module_id: str) -> str:
        """
        Get details of a specific module.

        Args:
            project_id: The UUID identifier of the project
            module_id: The UUID identifier of the module
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "GET",
            f"workspaces/{workspace_slug}/projects/{project_id}/modules/{module_id}/"
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def create_module(
        project_id: str,
        name: str,
        description: Optional[str] = None,
        start_date: Optional[str] = None,
        target_date: Optional[str] = None,
        lead: Optional[str] = None,
    ) -> str:
        """
        Create a new module in a project.

        Args:
            project_id: The UUID identifier of the project
            name: The name of the module
            description: Optional module description
            start_date: Optional start date (YYYY-MM-DD)
            target_date: Optional target/end date (YYYY-MM-DD)
            lead: Optional UUID of the module lead
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        body: dict = {"name": name}

        if description:
            body["description"] = description
        if start_date:
            body["start_date"] = start_date
        if target_date:
            body["target_date"] = target_date
        if lead:
            body["lead"] = lead

        response = await make_plane_request(
            "POST",
            f"workspaces/{workspace_slug}/projects/{project_id}/modules/",
            body=body
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def update_module(
        project_id: str,
        module_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        start_date: Optional[str] = None,
        target_date: Optional[str] = None,
        lead: Optional[str] = None,
        status: Optional[str] = None,
    ) -> str:
        """
        Update an existing module.

        Args:
            project_id: The UUID identifier of the project
            module_id: The UUID identifier of the module
            name: Updated module name
            description: Updated description
            start_date: Updated start date (YYYY-MM-DD)
            target_date: Updated target date (YYYY-MM-DD)
            lead: Updated lead UUID
            status: Updated status
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        body: dict = {}

        if name:
            body["name"] = name
        if description:
            body["description"] = description
        if start_date:
            body["start_date"] = start_date
        if target_date:
            body["target_date"] = target_date
        if lead:
            body["lead"] = lead
        if status:
            body["status"] = status

        response = await make_plane_request(
            "PATCH",
            f"workspaces/{workspace_slug}/projects/{project_id}/modules/{module_id}/",
            body=body
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def delete_module(project_id: str, module_id: str) -> str:
        """
        Delete a module.

        Args:
            project_id: The UUID identifier of the project
            module_id: The UUID identifier of the module
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        await make_plane_request(
            "DELETE",
            f"workspaces/{workspace_slug}/projects/{project_id}/modules/{module_id}/"
        )
        return "Module deleted successfully"
