"""Pydantic schemas for Plane API data models."""

from datetime import datetime
from typing import Any, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class Cycle(BaseModel):
    """Plane cycle schema."""

    id: UUID
    name: str = Field(max_length=255)
    description: Optional[str] = None
    start_date: Optional[str] = Field(None, description="Start date in YYYY-MM-DD format")
    end_date: Optional[str] = Field(None, description="End date in YYYY-MM-DD format")
    project_id: UUID = Field(alias="project")
    workspace: UUID
    owned_by: UUID
    created_by: UUID
    updated_by: UUID
    created_at: datetime
    updated_at: datetime
    archived_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    
    # Issue counts
    total_issues: int
    completed_issues: int
    started_issues: int
    unstarted_issues: int
    backlog_issues: int
    cancelled_issues: int
    
    # Estimates
    total_estimates: float
    completed_estimates: float
    started_estimates: float
    
    sort_order: Optional[float] = None
    external_id: Optional[str] = Field(None, max_length=255)
    external_source: Optional[str] = Field(None, max_length=255)

    class Config:
        populate_by_name = True


class Issue(BaseModel):
    """Plane issue schema."""

    id: UUID
    name: str = Field(max_length=255)
    description_html: Optional[str] = None
    description_binary: str
    sequence_id: Optional[int] = None
    
    project: UUID
    workspace: UUID
    state: Optional[UUID] = None
    priority: Optional[Any] = None
    
    assignees: Optional[list[UUID]] = None
    labels: Optional[list[UUID]] = None
    
    parent: Optional[UUID] = None
    estimate_point: Optional[UUID] = None
    point: Optional[int] = Field(None, ge=0, le=12)
    
    start_date: Optional[str] = None
    target_date: Optional[str] = None
    completed_at: Optional[datetime] = None
    
    created_by: Optional[UUID] = None
    updated_by: UUID
    created_at: datetime
    updated_at: datetime
    archived_at: Optional[str] = None
    deleted_at: Optional[datetime] = None
    
    is_draft: Optional[bool] = None
    sort_order: Optional[float] = None
    external_id: Optional[str] = Field(None, max_length=255)
    external_source: Optional[str] = Field(None, max_length=255)
    type_id: Optional[UUID] = None

    class Config:
        populate_by_name = True


class CycleIssue(BaseModel):
    """Plane cycle issue relation schema."""

    id: UUID
    cycle: UUID
    issue: UUID
    project: UUID
    workspace: UUID
    created_by: Optional[UUID] = None
    updated_by: Optional[UUID] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    sub_issues_count: int

    class Config:
        populate_by_name = True


class IssueType(BaseModel):
    """Plane issue type schema."""

    id: UUID
    name: str = Field(max_length=255)
    description: Optional[str] = None
    workspace: UUID
    project_ids: Optional[list[UUID]] = None
    is_active: Optional[bool] = None
    is_default: bool
    level: int
    logo_props: Any
    created_by: UUID
    updated_by: UUID
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    external_id: Optional[str] = Field(None, max_length=255)
    external_source: Optional[str] = Field(None, max_length=255)

    class Config:
        populate_by_name = True


class Label(BaseModel):
    """Plane label schema."""

    id: UUID
    name: str = Field(max_length=255)
    description: Optional[str] = None
    color: Optional[str] = Field(None, max_length=255)
    project: UUID
    workspace: UUID
    parent: Optional[UUID] = None
    sort_order: Optional[float] = None
    created_by: UUID
    updated_by: UUID
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    external_id: Optional[str] = Field(None, max_length=255)
    external_source: Optional[str] = Field(None, max_length=255)

    class Config:
        populate_by_name = True


class State(BaseModel):
    """Plane state schema."""

    id: UUID
    name: str = Field(max_length=255)
    description: Optional[str] = None
    color: str = Field(max_length=255)
    slug: Optional[str] = Field(None, max_length=100, pattern=r"^[-a-zA-Z0-9_]+$")
    sequence: Optional[float] = None
    group: Optional[Any] = None
    default: Optional[bool] = None
    is_triage: Optional[bool] = None
    project: UUID
    workspace: UUID
    created_by: UUID
    updated_by: UUID
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    external_id: Optional[str] = Field(None, max_length=255)
    external_source: Optional[str] = Field(None, max_length=255)

    class Config:
        populate_by_name = True


class ModuleIssue(BaseModel):
    """Plane module issue relation schema."""

    id: UUID
    module: UUID
    issue: UUID
    project: UUID
    workspace: UUID
    created_by: UUID
    updated_by: UUID
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    sub_issues_count: int

    class Config:
        populate_by_name = True


class Module(BaseModel):
    """Plane module schema."""

    id: UUID
    name: str = Field(max_length=255)
    description: Optional[str] = None
    description_html: Optional[Any] = None
    description_text: Optional[Any] = None
    start_date: Optional[str] = None
    target_date: Optional[str] = None
    status: Optional[Any] = None
    lead: Optional[UUID] = None
    members: Optional[list[UUID]] = None
    project: UUID
    workspace: UUID
    
    # Issue counts
    total_issues: int
    completed_issues: int
    started_issues: int
    unstarted_issues: int
    backlog_issues: int
    cancelled_issues: int
    
    created_by: UUID
    updated_by: UUID
    created_at: datetime
    updated_at: datetime
    archived_at: Optional[datetime] = None
    deleted_at: datetime
    
    sort_order: Optional[float] = None
    external_id: Optional[str] = Field(None, max_length=255)
    external_source: Optional[str] = Field(None, max_length=255)
    logo_props: Optional[Any] = None
    view_props: Optional[Any] = None

    class Config:
        populate_by_name = True


class Project(BaseModel):
    """Plane project schema."""

    id: UUID
    name: str = Field(max_length=255)
    description: Optional[str] = None
    identifier: str = Field(max_length=12, pattern=r"^[A-Z0-9_]+$")
    emoji: Optional[str] = Field(None, max_length=20)
    icon_prop: Optional[Any] = None
    logo_props: Optional[Any] = None
    cover_image: Optional[str] = None
    
    network: int
    workspace: UUID
    project_lead: Optional[UUID] = None
    
    estimate: Optional[UUID] = None
    default_state: Optional[UUID] = None
    
    archive_in: Optional[int] = Field(None, ge=0, le=12)
    close_in: Optional[int] = Field(None, ge=0, le=12)
    
    created_by: UUID
    updated_by: UUID
    created_at: datetime
    updated_at: datetime
    archived_at: Optional[datetime] = None
    deleted_at: datetime

    class Config:
        populate_by_name = True
