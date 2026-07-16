from pydantic import BaseModel, Field
from typing import Optional

class BuildingEntity(BaseModel):
    building_id: str = Field(..., description="Unique identifier for the building asset.")
    construction_year: int = Field(..., ge=1800, le=2026, description="The year the building was originally constructed.")
    building_type: str = Field(..., description="Classification of the building (e.g., SFH, MFH).")
    climate_zone: str = Field(..., description="Designated European climate zone code.")
    total_floor_area: float = Field(..., gt=0, description="Gross floor area in square meters.")
    heating_system: Optional[str] = Field(None, description="Primary heating system installed.")

# test code to verify the schema works as expected
if __name__ == "__main__":
    dummy_building = BuildingEntity(
        building_id="AUT-WIE-001",
        construction_year=1985,
        building_type="MFH",
        climate_zone="AT-East",
        total_floor_area=450.5,
        heating_system="Gas Boiler"
    )
    print("✅ Building Schema is working perfectly!")
    print(dummy_building.model_dump_json(indent=2))
