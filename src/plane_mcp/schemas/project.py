"""Project-related schemas."""

from typing import Any, Optional
from uuid import UUID

from pydantic import Field

from .base import FullAuditModel


class Project(FullAuditModel):
    """
    Plane project schema.

    Projects are the main organizational unit in Plane, containing issues,
    modules, cycles, and other work items.

    Attributes:
        name: Display name of the project (max 255 characters)
        description: Optional detailed description
        identifier: Unique short identifier for the project (e.g., "PROJ", max 12 chars, uppercase)
        emoji: Optional emoji representation
        icon_prop: Custom icon properties
        logo_props: Logo configuration properties
        cover_image: URL to cover image
        network: Network visibility level
        project_lead: UUID of the user who leads this project
        estimate: UUID of estimation system used
        default_state: UUID of default state for new issues
        archive_in: Number of months before auto-archiving (0-12)
        close_in: Number of months before auto-closing (0-12)
    """

    name: str = Field(max_length=255, description="Project name")
    description: Optional[str] = Field(None, description="Project description")
    identifier: str = Field(
        max_length=12,
        pattern=r"^[A-Z0-9_]+$",
        description="Unique project identifier (uppercase, e.g., 'MYPROJ')",
    )
    emoji: Optional[str] = Field(None, max_length=20, description="Emoji representation")
    icon_prop: Optional[Any] = Field(None, description="Icon properties")
    logo_props: Optional[Any] = Field(None, description="Logo properties")
    cover_image: Optional[str] = Field(None, description="Cover image URL")

    network: int = Field(description="Network visibility level")
    project_lead: Optional[UUID] = Field(None, description="UUID of project lead")

    estimate: Optional[UUID] = Field(None, description="UUID of estimation system")
    default_state: Optional[UUID] = Field(None, description="UUID of default state for new issues")

    archive_in: Optional[int] = Field(
        None,
        ge=0,
        le=12,
        description="Auto-archive after this many months",
    )
    close_in: Optional[int] = Field(
        None,
        ge=0,
        le=12,
        description="Auto-close after this many months",
    )
