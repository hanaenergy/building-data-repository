from pydantic import BaseModel, Field
from typing import Optional

class MaterialEntity(BaseModel):
    material_id: str = Field(..., description="Unique identifier for the construction material.")
    material_name: str = Field(..., description="Standardized name of the building material.")
    u_value: Optional[float] = Field(None, gt=0, description="Thermal transmittance value (W/m2K).")
    gwp_total: float = Field(..., description="Global Warming Potential (kgCO2e/kg).")
    density: Optional[float] = Field(None, gt=0, description="Material density (kg/m3).")
    service_life: Optional[int] = Field(None, gt=0, description="Estimated service life in years.")

if __name__ == "__main__":
    dummy_material = MaterialEntity(
        material_id="OKO-INS-042",
        material_name="EPS Insulation Board",
        u_value=0.035,
        gwp_total=2.5,
        density=15.0,
        service_life=50
    )
    print("✅ Material Schema is working perfectly!")
    print(dummy_material.model_dump_json(indent=2))