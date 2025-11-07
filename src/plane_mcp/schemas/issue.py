"""Issue-related schemas."""

from typing import Any, Optional
from uuid import UUID

from pydantic import Field

from .base import FullAuditModel


class Issue(FullAuditModel):
    """
    Plane issue schema.
    
    Issues are the core work items in Plane, representing tasks, bugs,
    features, or any other unit of work.
    
    Attributes:
        name: Issue title/name (max 255 characters)
        description_html: HTML-formatted description
        description_binary: Binary representation of description
        sequence_id: Sequential number within project
        project: UUID of parent project (required)
        state: UUID of current state (e.g., "To Do", "In Progress")
        priority: Priority level (urgent, high, medium, low, none)
        assignees: List of user UUIDs assigned to this issue
        labels: List of label UUIDs applied to this issue
        parent: UUID of parent issue (for sub-issues)
        estimate_point: UUID of estimate point
        point: Story points or estimate value (0-12)
        start_date: Planned start date (YYYY-MM-DD)
        target_date: Target completion date (YYYY-MM-DD)
        completed_at: Actual completion timestamp
        is_draft: Whether this is a draft issue
        type_id: UUID of issue type (bug, feature, etc.)
    """

    name: str = Field(max_length=255, description="Issue title")
    description_html: Optional[str] = Field(None, description="HTML description")
    description_binary: str = Field(description="Binary description representation")
    sequence_id: Optional[int] = Field(None, description="Sequential ID within project")
    
    project: UUID = Field(description="UUID of parent project")
    state: Optional[UUID] = Field(None, description="UUID of current state")
    priority: Optional[Any] = Field(None, description="Priority level")
    
    assignees: Optional[list[UUID]] = Field(None, description="List of assigned user UUIDs")
    labels: Optional[list[UUID]] = Field(None, description="List of label UUIDs")
    
    parent: Optional[UUID] = Field(None, description="UUID of parent issue")
    estimate_point: Optional[UUID] = Field(None, description="UUID of estimate point")
    point: Optional[int] = Field(None, ge=0, le=12, description="Story points (0-12)")
    
    start_date: Optional[str] = Field(None, description="Start date (YYYY-MM-DD)")
    target_date: Optional[str] = Field(None, description="Target date (YYYY-MM-DD)")
    completed_at: Optional[str] = Field(None, description="Completion timestamp")
    
    is_draft: Optional[bool] = Field(None, description="Draft status")
    type_id: Optional[UUID] = Field(None, description="UUID of issue type")


class IssueType(FullAuditModel):
    """
    Issue type schema (Bug, Feature, Task, etc.).
    
    Issue types categorize different kinds of work items.
    
    Attributes:
        name: Type name (max 255 characters)
        description: Optional description
        project_ids: List of project UUIDs using this type
        is_active: Whether this type is currently active
        is_default: Whether this is a default type
        level: Hierarchy level
        logo_props: Logo/icon properties
    """

    name: str = Field(max_length=255, description="Issue type name")
    description: Optional[str] = Field(None, description="Type description")
    project_ids: Optional[list[UUID]] = Field(None, description="Projects using this type")
    is_active: Optional[bool] = Field(None, description="Active status")
    is_default: bool = Field(description="Default type flag")
    level: int = Field(description="Hierarchy level")
    logo_props: Any = Field(description="Logo/icon properties")
