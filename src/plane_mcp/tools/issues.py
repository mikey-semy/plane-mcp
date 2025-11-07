"""Issue tools for Plane API."""

import json
import os
from typing import Optional

from mcp.server.fastmcp import FastMCP

from plane_mcp.common.request_helper import make_plane_request


def register_issue_tools(mcp: FastMCP) -> None:
    """Register issue-related tools."""

    @mcp.tool()
    async def list_project_issues(project_id: str) -> str:
        """
        Get all issues for a specific project.

        Args:
            project_id: The UUID identifier of the project to get issues for
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "GET",
            f"workspaces/{workspace_slug}/projects/{project_id}/issues/"
        )

        # Simplify response
        if isinstance(response, dict) and "results" in response:
            issues = [
                {
                    "id": issue.get("id"),
                    "name": issue.get("name"),
                    "sequence_id": issue.get("sequence_id"),
                    "state": issue.get("state_detail") or issue.get("state"),
                    "priority": issue.get("priority_detail") or issue.get("priority"),
                    "created_at": issue.get("created_at"),
                    "updated_at": issue.get("updated_at"),
                }
                for issue in response["results"]
            ]
            result = {
                "total_count": response.get("total_count"),
                "count": response.get("count"),
                "results": issues,
            }
            return json.dumps(result, indent=2)

        return json.dumps(response, indent=2)

    @mcp.tool()
    async def get_issue(project_id: str, issue_id: str) -> str:
        """
        Get details of a specific issue.

        Args:
            project_id: The UUID identifier of the project
            issue_id: The UUID identifier of the issue
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "GET",
            f"workspaces/{workspace_slug}/projects/{project_id}/issues/{issue_id}/"
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def get_issue_using_readable_identifier(project_identifier: str, issue_identifier: str) -> str:
        """
        Get a specific issue using its readable identifier.

        When issue identifier is provided as FIRST-123, ABC-123, etc.
        For FIRST-123: project_identifier is FIRST and issue_identifier is 123

        Args:
            project_identifier: The readable identifier of the project (e.g., 'FIRST' for FIRST-123)
            issue_identifier: The issue number (e.g., '123' for FIRST-123)
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "GET",
            f"workspaces/{workspace_slug}/issues/{project_identifier}-{issue_identifier}/"
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def get_issue_comments(project_id: str, issue_id: str) -> str:
        """
        Get all comments for a specific issue.

        Args:
            project_id: The UUID identifier of the project
            issue_id: The UUID identifier of the issue
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "GET",
            f"workspaces/{workspace_slug}/projects/{project_id}/issues/{issue_id}/comments/"
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def add_issue_comment(project_id: str, issue_id: str, comment_html: str) -> str:
        """
        Add a comment to a specific issue.

        Args:
            project_id: The UUID identifier of the project
            issue_id: The UUID identifier of the issue
            comment_html: The HTML content of the comment to add
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "POST",
            f"workspaces/{workspace_slug}/projects/{project_id}/issues/{issue_id}/comments/",
            body={"comment_html": comment_html}
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def create_issue(
        project_id: str,
        name: str,
        description: Optional[str] = None,
        state_id: Optional[str] = None,
        priority: Optional[str] = None,
        assignees: Optional[list[str]] = None,
        labels: Optional[list[str]] = None,
    ) -> str:
        """
        Create a new issue in a project.

        Args:
            project_id: The UUID identifier of the project
            name: The title/name of the issue
            description: Optional HTML description of the issue
            state_id: Optional UUID of the issue state
            priority: Optional priority (urgent, high, medium, low, none)
            assignees: Optional list of assignee UUIDs
            labels: Optional list of label UUIDs
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        body: dict = {"name": name}

        if description:
            body["description_html"] = description
        if state_id:
            body["state"] = state_id
        if priority:
            body["priority"] = priority
        if assignees:
            body["assignees"] = assignees
        if labels:
            body["labels"] = labels

        response = await make_plane_request(
            "POST",
            f"workspaces/{workspace_slug}/projects/{project_id}/issues/",
            body=body
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def update_issue(
        project_id: str,
        issue_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        state: Optional[str] = None,
        priority: Optional[str] = None,
        assignees: Optional[list[str]] = None,
        labels: Optional[list[str]] = None,
    ) -> str:
        """
        Update an existing issue.

        Args:
            project_id: The UUID identifier of the project
            issue_id: The UUID identifier of the issue to update
            name: Updated issue name
            description: Updated HTML description
            state: Updated state UUID
            priority: Updated priority
            assignees: Updated list of assignee UUIDs
            labels: Updated list of label UUIDs
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        body: dict = {}

        if name:
            body["name"] = name
        if description:
            body["description_html"] = description
        if state:
            body["state"] = state
        if priority:
            body["priority"] = priority
        if assignees is not None:
            body["assignees"] = assignees
        if labels is not None:
            body["labels"] = labels

        response = await make_plane_request(
            "PATCH",
            f"workspaces/{workspace_slug}/projects/{project_id}/issues/{issue_id}/",
            body=body
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def delete_issue(project_id: str, issue_id: str) -> str:
        """
        Delete an issue.

        Args:
            project_id: The UUID identifier of the project
            issue_id: The UUID identifier of the issue to delete
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        await make_plane_request(
            "DELETE",
            f"workspaces/{workspace_slug}/projects/{project_id}/issues/{issue_id}/"
        )
        return "Issue deleted successfully"
