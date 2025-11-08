"""Work log tools for Plane API."""

import json
import os
from typing import Optional

from mcp.server.fastmcp import FastMCP

from plane_mcp.common.request_helper import make_plane_request


def register_worklog_tools(mcp: FastMCP) -> None:
    """Register worklog-related tools."""

    @mcp.tool()
    async def get_issue_worklogs(project_id: str, issue_id: str) -> str:
        """
        Get all worklogs for a specific issue.

        Args:
            project_id: The UUID identifier of the project containing the issue
            issue_id: The UUID identifier of the issue to get worklogs for
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "GET",
            f"v1/workspaces/{workspace_slug}/projects/{project_id}/issues/{issue_id}/worklogs/"
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def get_total_worklogs(project_id: str) -> str:
        """
        Get total logged time for a project.

        Args:
            project_id: The UUID identifier of the project to get total worklogs for
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "GET",
            f"v1/workspaces/{workspace_slug}/projects/{project_id}/total-worklogs/"
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def create_worklog(
        project_id: str,
        issue_id: str,
        duration: float,
        description: str,
        started_at: Optional[str] = None,
    ) -> str:
        """
        Create a new worklog for an issue.

        Args:
            project_id: The UUID identifier of the project containing the issue
            issue_id: The UUID identifier of the issue to create worklog for
            duration: Duration in hours (e.g., 2.5 for 2 hours 30 minutes)
            description: Description of the work done
            started_at: Optional timestamp when work started (ISO 8601 format)
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        body: dict = {
            "duration": duration,
            "description": description,
        }

        if started_at:
            body["started_at"] = started_at

        response = await make_plane_request(
            "POST",
            f"v1/workspaces/{workspace_slug}/projects/{project_id}/issues/{issue_id}/worklogs/",
            body=body
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def update_worklog(
        project_id: str,
        issue_id: str,
        worklog_id: str,
        duration: Optional[float] = None,
        description: Optional[str] = None,
        started_at: Optional[str] = None,
    ) -> str:
        """
        Update an existing worklog.

        Args:
            project_id: The UUID identifier of the project containing the issue
            issue_id: The UUID identifier of the issue containing the worklog
            worklog_id: The UUID identifier of the worklog to update
            duration: Updated duration in hours
            description: Updated description
            started_at: Updated timestamp when work started
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        body: dict = {}

        if duration is not None:
            body["duration"] = duration
        if description:
            body["description"] = description
        if started_at:
            body["started_at"] = started_at

        response = await make_plane_request(
            "PATCH",
            f"v1/workspaces/{workspace_slug}/projects/{project_id}/issues/{issue_id}/worklogs/{worklog_id}/",
            body=body
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def delete_worklog(project_id: str, issue_id: str, worklog_id: str) -> str:
        """
        Delete a worklog.

        Args:
            project_id: The UUID identifier of the project containing the issue
            issue_id: The UUID identifier of the issue containing the worklog
            worklog_id: The UUID identifier of the worklog to delete
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        await make_plane_request(
            "DELETE",
            f"v1/workspaces/{workspace_slug}/projects/{project_id}/issues/{issue_id}/worklogs/{worklog_id}/"
        )
        return "Worklog deleted successfully"
