"""Work log schemas."""

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import TimestampedModel


class IssueWorkLog(TimestampedModel):
    """
    Issue work log entry schema.
    
    Tracks time spent on issues.
    
    Attributes:
        id: Unique identifier
        issue: UUID of parent issue
        project: UUID of parent project
        workspace: UUID of parent workspace
        user: UUID of user who logged work
        duration: Time spent in minutes
        description: Optional description of work done
        logged_at: When the work was performed
        created_by: UUID of creator
        updated_by: UUID of last updater
    """

    id: UUID = Field(description="Unique identifier")
    issue: UUID = Field(description="UUID of parent issue")
    project: UUID = Field(description="UUID of parent project")
    workspace: UUID = Field(description="UUID of parent workspace")
    user: UUID = Field(description="UUID of user who logged work")
    duration: int = Field(ge=0, description="Time spent in minutes")
    description: Optional[str] = Field(None, description="Description of work done")
    logged_at: datetime = Field(description="When the work was performed")
    created_by: Optional[UUID] = Field(None, description="UUID of creator")
    updated_by: Optional[UUID] = Field(None, description="UUID of last updater")
