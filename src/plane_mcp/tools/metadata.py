"""Metadata tools for Plane API."""

import json
import os

from mcp.server.fastmcp import FastMCP

from plane_mcp.common.request_helper import make_plane_request


def register_metadata_tools(mcp: FastMCP) -> None:
    """Register metadata-related tools."""

    @mcp.tool()
    async def list_labels(project_id: str) -> str:
        """
        List all labels for a project.

        Args:
            project_id: The UUID identifier of the project
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "GET",
            f"workspaces/{workspace_slug}/projects/{project_id}/labels/"
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def get_label(project_id: str, label_id: str) -> str:
        """
        Get details of a specific label.

        Args:
            project_id: The UUID identifier of the project
            label_id: The UUID identifier of the label
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "GET",
            f"workspaces/{workspace_slug}/projects/{project_id}/labels/{label_id}/"
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def create_label(
        project_id: str,
        name: str,
        description: str = "",
        color: str = "#000000"
    ) -> str:
        """
        Create a new label.

        Args:
            project_id: The UUID identifier of the project
            name: Name of the label
            description: Description of the label
            color: Color hex code for the label
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "POST",
            f"workspaces/{workspace_slug}/projects/{project_id}/labels/",
            body={
                "name": name,
                "description": description,
                "color": color
            }
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def update_label(
        project_id: str,
        label_id: str,
        name: str | None = None,
        description: str | None = None,
        color: str | None = None
    ) -> str:
        """
        Update an existing label.

        Args:
            project_id: The UUID identifier of the project
            label_id: The UUID identifier of the label
            name: New name for the label
            description: New description for the label
            color: New color hex code for the label
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        body = {}
        if name is not None:
            body["name"] = name
        if description is not None:
            body["description"] = description
        if color is not None:
            body["color"] = color

        response = await make_plane_request(
            "PATCH",
            f"workspaces/{workspace_slug}/projects/{project_id}/labels/{label_id}/",
            body=body
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def delete_label(project_id: str, label_id: str) -> str:
        """
        Delete a label.

        Args:
            project_id: The UUID identifier of the project
            label_id: The UUID identifier of the label
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        await make_plane_request(
            "DELETE",
            f"workspaces/{workspace_slug}/projects/{project_id}/labels/{label_id}/"
        )
        return "Label deleted successfully"

    @mcp.tool()
    async def get_state(project_id: str, state_id: str) -> str:
        """
        Get details of a specific state.

        Args:
            project_id: The UUID identifier of the project
            state_id: The UUID identifier of the state
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "GET",
            f"workspaces/{workspace_slug}/projects/{project_id}/states/{state_id}/"
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def create_state(
        project_id: str,
        name: str,
        group: str,
        description: str = "",
        color: str = "#000000"
    ) -> str:
        """
        Create a new state.

        Args:
            project_id: The UUID identifier of the project
            name: Name of the state
            group: Group of the state (backlog, unstarted, started, completed, cancelled)
            description: Description of the state
            color: Color hex code for the state
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "POST",
            f"workspaces/{workspace_slug}/projects/{project_id}/states/",
            body={
                "name": name,
                "group": group,
                "description": description,
                "color": color
            }
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def update_state(
        project_id: str,
        state_id: str,
        name: str | None = None,
        group: str | None = None,
        description: str | None = None,
        color: str | None = None
    ) -> str:
        """
        Update an existing state.

        Args:
            project_id: The UUID identifier of the project
            state_id: The UUID identifier of the state
            name: New name for the state
            group: New group for the state (backlog, unstarted, started, completed, cancelled)
            description: New description for the state
            color: New color hex code for the state
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        body = {}
        if name is not None:
            body["name"] = name
        if group is not None:
            body["group"] = group
        if description is not None:
            body["description"] = description
        if color is not None:
            body["color"] = color

        response = await make_plane_request(
            "PATCH",
            f"workspaces/{workspace_slug}/projects/{project_id}/states/{state_id}/",
            body=body
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def delete_state(project_id: str, state_id: str) -> str:
        """
        Delete a state.

        Args:
            project_id: The UUID identifier of the project
            state_id: The UUID identifier of the state
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        await make_plane_request(
            "DELETE",
            f"workspaces/{workspace_slug}/projects/{project_id}/states/{state_id}/"
        )
        return "State deleted successfully"

    @mcp.tool()
    async def get_issue_type(project_id: str, issue_type_id: str) -> str:
        """
        Get details of a specific issue type.

        Args:
            project_id: The UUID identifier of the project
            issue_type_id: The UUID identifier of the issue type
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "GET",
            f"workspaces/{workspace_slug}/projects/{project_id}/issue-types/{issue_type_id}/"
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def create_issue_type(
        project_id: str,
        name: str,
        description: str = "",
        color: str = "#000000",
        icon: str = ""
    ) -> str:
        """
        Create a new issue type.

        Args:
            project_id: The UUID identifier of the project
            name: Name of the issue type
            description: Description of the issue type
            color: Color hex code for the issue type
            icon: Icon identifier for the issue type
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "POST",
            f"workspaces/{workspace_slug}/projects/{project_id}/issue-types/",
            body={
                "name": name,
                "description": description,
                "color": color,
                "icon": icon
            }
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def update_issue_type(
        project_id: str,
        issue_type_id: str,
        name: str | None = None,
        description: str | None = None,
        color: str | None = None,
        icon: str | None = None
    ) -> str:
        """
        Update an existing issue type.

        Args:
            project_id: The UUID identifier of the project
            issue_type_id: The UUID identifier of the issue type
            name: New name for the issue type
            description: New description for the issue type
            color: New color hex code for the issue type
            icon: New icon identifier for the issue type
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        body = {}
        if name is not None:
            body["name"] = name
        if description is not None:
            body["description"] = description
        if color is not None:
            body["color"] = color
        if icon is not None:
            body["icon"] = icon

        response = await make_plane_request(
            "PATCH",
            f"workspaces/{workspace_slug}/projects/{project_id}/issue-types/{issue_type_id}/",
            body=body
        )
        return json.dumps(response, indent=2)

    @mcp.tool()
    async def delete_issue_type(project_id: str, issue_type_id: str) -> str:
        """
        Delete an issue type.

        Args:
            project_id: The UUID identifier of the project
            issue_type_id: The UUID identifier of the issue type
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        await make_plane_request(
            "DELETE",
            f"workspaces/{workspace_slug}/projects/{project_id}/issue-types/{issue_type_id}/"
        )
        return "Issue type deleted successfully"

    @mcp.tool()
    async def list_states(project_id: str) -> str:
        """
        Get all states for a specific project.

        Args:
            project_id: The UUID identifier of the project to get states for
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")
        response = await make_plane_request(
            "GET",
            f"workspaces/{workspace_slug}/projects/{project_id}/states/"
        )
        return json.dumps(response, indent=2)
