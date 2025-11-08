"""Cycle tools for Plane API."""

import json
import os
from typing import Optional

from mcp.server.fastmcp import FastMCP

from plane_mcp.common.request_helper import make_plane_request


def register_cycle_tools(mcp: FastMCP) -> None:
    """Register cycle-related tools."""

    @mcp.tool()
    async def list_cycles(project_id: str) -> str:
        """
        Get all cycles for a specific project.

        Args:
            project_id: The UUID identifier of the project
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "GET",
            f"v1/workspaces/{workspace_slug}/projects/{project_id}/cycles/"
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def get_cycle(project_id: str, cycle_id: str) -> str:
        """
        Get details of a specific cycle.

        Args:
            project_id: The UUID identifier of the project
            cycle_id: The UUID identifier of the cycle
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "GET",
            f"v1/workspaces/{workspace_slug}/projects/{project_id}/cycles/{cycle_id}/"
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def create_cycle(
        project_id: str,
        name: str,
        description: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> str:
        """
        Create a new cycle in a project.

        Args:
            project_id: The UUID identifier of the project
            name: The name of the cycle
            description: Optional cycle description
            start_date: Optional start date (YYYY-MM-DD)
            end_date: Optional end date (YYYY-MM-DD)
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        body: dict = {"name": name}

        if description:
            body["description"] = description
        if start_date:
            body["start_date"] = start_date
        if end_date:
            body["end_date"] = end_date

        response = await make_plane_request(
            "POST",
            f"v1/workspaces/{workspace_slug}/projects/{project_id}/cycles/",
            body=body
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def update_cycle(
        project_id: str,
        cycle_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> str:
        """
        Update an existing cycle.

        Args:
            project_id: The UUID identifier of the project
            cycle_id: The UUID identifier of the cycle
            name: Updated cycle name
            description: Updated description
            start_date: Updated start date (YYYY-MM-DD)
            end_date: Updated end date (YYYY-MM-DD)
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        body: dict = {}

        if name:
            body["name"] = name
        if description:
            body["description"] = description
        if start_date:
            body["start_date"] = start_date
        if end_date:
            body["end_date"] = end_date

        response = await make_plane_request(
            "PATCH",
            f"v1/workspaces/{workspace_slug}/projects/{project_id}/cycles/{cycle_id}/",
            body=body
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def delete_cycle(project_id: str, cycle_id: str) -> str:
        """
        Delete a cycle.

        Args:
            project_id: The UUID identifier of the project
            cycle_id: The UUID identifier of the cycle
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        await make_plane_request(
            "DELETE",
            f"v1/workspaces/{workspace_slug}/projects/{project_id}/cycles/{cycle_id}/"
        )
        return "Cycle deleted successfully"

    @mcp.tool()
    async def transfer_cycle_issues(project_id: str, cycle_id: str, new_cycle_id: str) -> str:
        """
        Transfer issues from one cycle to another.

        Args:
            project_id: The UUID identifier of the project containing the cycle
            cycle_id: The UUID identifier of the source cycle
            new_cycle_id: The UUID identifier of the target cycle
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "POST",
            f"v1/workspaces/{workspace_slug}/projects/{project_id}/cycles/{cycle_id}/transfer-issues/",
            body={"new_cycle_id": new_cycle_id}
        )
        return json.dumps(response, indent=2)
