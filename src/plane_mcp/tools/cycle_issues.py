"""Cycle issue tools for Plane API."""

import json
import os

from mcp.server.fastmcp import FastMCP

from plane_mcp.common.request_helper import make_plane_request


def register_cycle_issue_tools(mcp: FastMCP) -> None:
    """Register cycle-issue-related tools."""
    
    @mcp.tool()
    async def list_cycle_issues(project_id: str, cycle_id: str) -> str:
        """
        Get all issues for a specific cycle.
        
        Args:
            project_id: The UUID identifier of the project containing the cycle
            cycle_id: The UUID identifier of the cycle to get issues for
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "GET",
            f"workspaces/{workspace_slug}/projects/{project_id}/cycles/{cycle_id}/cycle-issues/"
        )
        return json.dumps(response, indent=2)
    
    @mcp.tool()
    async def add_cycle_issues(project_id: str, cycle_id: str, issues: list[str]) -> str:
        """
        Add issues to a cycle.
        
        Args:
            project_id: The UUID identifier of the project containing the cycle
            cycle_id: The UUID identifier of the cycle to add issues to
            issues: Array of issue UUIDs to add to the cycle
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "POST",
            f"workspaces/{workspace_slug}/projects/{project_id}/cycles/{cycle_id}/cycle-issues/",
            body={"issues": issues}
        )
        return json.dumps(response, indent=2)
    
    @mcp.tool()
    async def delete_cycle_issue(project_id: str, cycle_id: str, issue_id: str) -> str:
        """
        Remove an issue from a cycle.
        
        Args:
            project_id: The UUID identifier of the project containing the cycle
            cycle_id: The UUID identifier of the cycle containing the issue
            issue_id: The UUID identifier of the issue to remove from the cycle
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        await make_plane_request(
            "DELETE",
            f"workspaces/{workspace_slug}/projects/{project_id}/cycles/{cycle_id}/cycle-issues/{issue_id}/"
        )
        return "Issue removed from cycle successfully"
