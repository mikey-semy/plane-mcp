"""Module issue tools for Plane API."""

import json
import os

from mcp.server.fastmcp import FastMCP

from plane_mcp.common.request_helper import make_plane_request


def register_module_issue_tools(mcp: FastMCP) -> None:
    """Register module-issue-related tools."""

    @mcp.tool()
    async def list_module_issues(project_id: str, module_id: str) -> str:
        """
        Get all issues for a specific module.

        Args:
            project_id: The UUID identifier of the project containing the module
            module_id: The UUID identifier of the module to get issues for
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "GET",
            f"workspaces/{workspace_slug}/projects/{project_id}/modules/{module_id}/module-issues/"
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def add_module_issues(project_id: str, module_id: str, issues: list[str]) -> str:
        """
        Add issues to a module. Assign module to issues.

        Args:
            project_id: The UUID identifier of the project containing the module
            module_id: The UUID identifier of the module to add issues to
            issues: Array of issue UUIDs to add to the module
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "POST",
            f"workspaces/{workspace_slug}/projects/{project_id}/modules/{module_id}/module-issues/",
            body={"issues": issues}
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def delete_module_issue(project_id: str, module_id: str, issue_id: str) -> str:
        """
        Remove an issue from a module. Unassign module from issue.

        Args:
            project_id: The UUID identifier of the project containing the module
            module_id: The UUID identifier of the module containing the issue
            issue_id: The UUID identifier of the issue to remove from the module
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        await make_plane_request(
            "DELETE",
            f"workspaces/{workspace_slug}/projects/{project_id}/modules/{module_id}/module-issues/{issue_id}/"
        )
        return "Issue removed from module successfully"
