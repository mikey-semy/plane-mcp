"""Cycle schemas."""

from datetime import datetime
from typing import Any, Optional
from uuid import UUID

from pydantic import Field

from .base import FullAuditModel, TimestampedModel


class Cycle(FullAuditModel):
    """
    Cycle schema (sprint/iteration).
    
    Cycles represent sprints or iterations for time-boxed work.
    
    Attributes:
        name: Cycle name (max 255 characters)
        description: Optional description
        start_date: Cycle start date
        end_date: Cycle end date
        owned_by: UUID of cycle owner
        view_props: View properties/settings
        progress_snapshot: Progress data snapshot
        project: UUID of parent project
        status: Current cycle status
        is_favorite: Whether cycle is favorited
        total_issues: Total issue count
        cancelled_issues: Cancelled issue count
        completed_issues: Completed issue count
        started_issues: Started issue count
        unstarted_issues: Unstarted issue count
        backlog_issues: Backlog issue count
    """

    name: str = Field(max_length=255, description="Cycle name")
    description: Optional[str] = Field(None, description="Cycle description")
    start_date: Optional[datetime] = Field(None, description="Start date")
    end_date: Optional[datetime] = Field(None, description="End date")
    owned_by: Optional[UUID] = Field(None, description="UUID of cycle owner")
    view_props: Optional[Any] = Field(None, description="View properties")
    progress_snapshot: Optional[Any] = Field(None, description="Progress snapshot")
    project: UUID = Field(description="UUID of parent project")
    status: Optional[str] = Field(None, description="Cycle status")
    is_favorite: Optional[bool] = Field(None, description="Favorite flag")
    total_issues: Optional[int] = Field(None, ge=0, description="Total issue count")
    cancelled_issues: Optional[int] = Field(None, ge=0, description="Cancelled issue count")
    completed_issues: Optional[int] = Field(None, ge=0, description="Completed issue count")
    started_issues: Optional[int] = Field(None, ge=0, description="Started issue count")
    unstarted_issues: Optional[int] = Field(None, ge=0, description="Unstarted issue count")
    backlog_issues: Optional[int] = Field(None, ge=0, description="Backlog issue count")


class CycleIssue(TimestampedModel):
    """
    Cycle-Issue relationship schema.
    
    Links issues to cycles (many-to-many relationship).
    
    Attributes:
        id: Unique identifier
        cycle: UUID of cycle
        issue: UUID of issue
        workspace: UUID of workspace
        project: UUID of project
        created_by: UUID of creator
        updated_by: UUID of last updater
    """

    id: UUID = Field(description="Unique identifier")
    cycle: UUID = Field(description="UUID of cycle")
    issue: UUID = Field(description="UUID of issue")
    workspace: UUID = Field(description="UUID of workspace")
    project: UUID = Field(description="UUID of project")
    created_by: Optional[UUID] = Field(None, description="UUID of creator")
    updated_by: Optional[UUID] = Field(None, description="UUID of last updater")
