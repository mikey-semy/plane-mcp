"""Module schemas."""

from datetime import datetime
from typing import Any, Optional
from uuid import UUID

from pydantic import Field

from .base import FullAuditModel, TimestampedModel


class Module(FullAuditModel):
    """
    Module schema (work grouping).
    
    Modules group related issues together (similar to epics or features).
    
    Attributes:
        name: Module name (max 255 characters)
        description: Optional description
        description_text: Plain text description
        description_html: HTML description
        start_date: Module start date
        target_date: Module target/due date
        status: Module status
        lead: Optional UUID of module lead user
        members: List of member UUIDs
        view_props: View properties/settings
        project: UUID of parent project
        links_list: List of links
        link_module: List of linked modules
        is_favorite: Whether module is favorited
        total_issues: Total issue count
        cancelled_issues: Cancelled issue count
        completed_issues: Completed issue count
        started_issues: Started issue count
        unstarted_issues: Unstarted issue count
        backlog_issues: Backlog issue count
    """

    name: str = Field(max_length=255, description="Module name")
    description: Optional[str] = Field(None, description="Module description")
    description_text: Optional[Any] = Field(None, description="Plain text description")
    description_html: Optional[Any] = Field(None, description="HTML description")
    start_date: Optional[datetime] = Field(None, description="Start date")
    target_date: Optional[datetime] = Field(None, description="Target/due date")
    status: Optional[str] = Field(None, description="Module status")
    lead: Optional[UUID] = Field(None, description="UUID of module lead")
    members: list[UUID] = Field(default_factory=list, description="List of member UUIDs")
    view_props: Optional[Any] = Field(None, description="View properties")
    project: UUID = Field(description="UUID of parent project")
    links_list: list[Any] = Field(default_factory=list, description="List of links")
    link_module: list[Any] = Field(default_factory=list, description="Linked modules")
    is_favorite: Optional[bool] = Field(None, description="Favorite flag")
    total_issues: Optional[int] = Field(None, ge=0, description="Total issue count")
    cancelled_issues: Optional[int] = Field(None, ge=0, description="Cancelled issue count")
    completed_issues: Optional[int] = Field(None, ge=0, description="Completed issue count")
    started_issues: Optional[int] = Field(None, ge=0, description="Started issue count")
    unstarted_issues: Optional[int] = Field(None, ge=0, description="Unstarted issue count")
    backlog_issues: Optional[int] = Field(None, ge=0, description="Backlog issue count")


class ModuleIssue(TimestampedModel):
    """
    Module-Issue relationship schema.
    
    Links issues to modules (many-to-many relationship).
    
    Attributes:
        id: Unique identifier
        module: UUID of module
        issue: UUID of issue
        workspace: UUID of workspace
        project: UUID of project
        created_by: UUID of creator
        updated_by: UUID of last updater
    """

    id: UUID = Field(description="Unique identifier")
    module: UUID = Field(description="UUID of module")
    issue: UUID = Field(description="UUID of issue")
    workspace: UUID = Field(description="UUID of workspace")
    project: UUID = Field(description="UUID of project")
    created_by: Optional[UUID] = Field(None, description="UUID of creator")
    updated_by: Optional[UUID] = Field(None, description="UUID of last updater")
