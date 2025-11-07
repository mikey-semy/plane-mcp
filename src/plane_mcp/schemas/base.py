"""Base schemas with common fields for Plane API models."""

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


def _serialize_datetime(v: datetime) -> str:
    """Serialize datetime to ISO format."""
    return v.isoformat()


def _serialize_uuid(v: UUID) -> str:
    """Serialize UUID to string."""
    return str(v)


class PlaneBaseModel(BaseModel):
    """Base model for all Plane entities."""

    class Config:
        """Pydantic configuration."""
        populate_by_name = True
        json_encoders = {
            datetime: _serialize_datetime,
            UUID: _serialize_uuid,
        }


class TimestampedModel(PlaneBaseModel):
    """Model with creation and update timestamps."""

    created_at: datetime = Field(description="Entity creation timestamp")
    updated_at: datetime = Field(description="Entity last update timestamp")


class AuditedModel(TimestampedModel):
    """Model with audit fields (who created/updated)."""

    created_by: UUID = Field(description="UUID of user who created the entity")
    updated_by: UUID = Field(description="UUID of user who last updated the entity")


class WorkspaceOwnedModel(AuditedModel):
    """Model that belongs to a workspace."""

    workspace: UUID = Field(description="UUID of the workspace this entity belongs to")


class ProjectOwnedModel(WorkspaceOwnedModel):
    """Model that belongs to a project within a workspace."""

    project: UUID = Field(description="UUID of the project this entity belongs to")


class SoftDeletableModel(PlaneBaseModel):
    """Model that supports soft deletion."""

    deleted_at: datetime = Field(description="Timestamp when entity was deleted (soft delete)")


class ArchivableModel(PlaneBaseModel):
    """Model that can be archived."""

    archived_at: Optional[datetime] = Field(None, description="Timestamp when entity was archived")


class ExternallyIdentifiableModel(PlaneBaseModel):
    """Model that can be linked to external systems."""

    external_id: Optional[str] = Field(None, max_length=255, description="External system identifier")
    external_source: Optional[str] = Field(None, max_length=255, description="External system source name")


class SortableModel(PlaneBaseModel):
    """Model with sort order support."""

    sort_order: Optional[float] = Field(None, description="Sort order for manual ordering")


class FullAuditModel(
    WorkspaceOwnedModel,
    SoftDeletableModel,
    ArchivableModel,
    ExternallyIdentifiableModel,
    SortableModel,
):
    """
    Comprehensive audit model combining all common audit fields.

    Includes:
    - Workspace ownership
    - Creation/update tracking
    - Soft deletion
    - Archive support
    - External system linking
    - Manual sorting
    """

    id: UUID = Field(description="Unique identifier (UUID)")
