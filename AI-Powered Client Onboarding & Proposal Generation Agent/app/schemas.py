from pydantic import BaseModel, Field
from typing import List, Optional

class TechnicalRequirement(BaseModel):
    category: str = Field(description="e.g., Frontend, Backend, Database, AI, DevOps")
    details: str = Field(description="Specific technology or feature required")

class FeatureItem(BaseModel):
    name: str = Field(description="Name of the software feature")
    description: str = Field(description="Brief summary of what the feature does")
    estimated_complexity: str = Field(description="Low, Medium, or High")

class StructuredProjectBrief(BaseModel):
    client_name: str = Field(description="Extracted name of the company or prospective client")
    project_goals: List[str] = Field(description="The primary objectives of the proposed system")
    technical_stack: List[TechnicalRequirement] = Field(description="List of identified technical needs")
    core_features: List[FeatureItem] = Field(description="List of software features discovered in the brief")
    estimated_weeks: int = Field(description="A realistic timeline estimation in weeks based on features")
