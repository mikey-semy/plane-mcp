"""Metadata schemas (States, Labels)."""

from typing import Any, Optional
from uuid import UUID

from pydantic import Field

from .base import FullAuditModel


class State(FullAuditModel):
    """
    Issue state schema (workflow status).
    
    States represent different stages in a workflow (e.g., "To Do", "In Progress", "Done").
    
    Attributes:
        name: State name (max 255 characters)
        description: Optional description
        color: Color hex code for UI display (max 255 characters)
        slug: URL-friendly identifier (alphanumeric, hyphens, underscores)
        sequence: Order in workflow
        group: State group/category
        default: Whether this is the default state
        is_triage: Whether this is a triage state
        project: UUID of parent project
    """

    name: str = Field(max_length=255, description="State name")
    description: Optional[str] = Field(None, description="State description")
    color: str = Field(max_length=255, description="Color hex code (e.g., '#FF5733')")
    slug: Optional[str] = Field(
        None,
        max_length=100,
        pattern=r"^[-a-zA-Z0-9_]+$",
        description="URL-friendly slug",
    )
    sequence: Optional[float] = Field(None, description="Order in workflow")
    group: Optional[Any] = Field(None, description="State group/category")
    default: Optional[bool] = Field(None, description="Default state flag")
    is_triage: Optional[bool] = Field(None, description="Triage state flag")
    project: UUID = Field(description="UUID of parent project")


class Label(FullAuditModel):
    """
    Issue label schema for categorization.
    
    Labels provide flexible categorization for issues (e.g., "bug", "urgent", "backend").
    
    Attributes:
        name: Label name (max 255 characters)
        description: Optional description
        color: Color hex code for UI display (max 255 characters)
        project: UUID of parent project
        parent: Optional UUID of parent label (for hierarchical labels)
    """

    name: str = Field(max_length=255, description="Label name")
    description: Optional[str] = Field(None, description="Label description")
    color: Optional[str] = Field(None, max_length=255, description="Color hex code")
    project: UUID = Field(description="UUID of parent project")
    parent: Optional[UUID] = Field(None, description="UUID of parent label (if hierarchical)")
