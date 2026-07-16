from pydantic import BaseModel, Field
from typing import List

# load the other schemas
from building import BuildingEntity
from material import MaterialEntity
from climate import ClimateEntity

class RetrofitScenario(BaseModel):
    scenario_id: str = Field(..., description="Unique ID for this retrofit project")
    description: str = Field(..., description="Summary of the retrofit goal")
    
    # each schema is embedded as a nested model
    building: BuildingEntity
    climate: ClimateEntity
    materials_applied: List[MaterialEntity] # materials used in the retrofit, can be multiple

if __name__ == "__main__":
    # 1. building setup
    bldg = BuildingEntity(building_id="AUT-WIE-001", construction_year=1985, building_type="MFH", climate_zone="AT-East", total_floor_area=450.5, heating_system="Gas")
    # 2. climate setup
    clim = ClimateEntity(location_id="AT-VIE-01", latitude=48.2082, longitude=16.3738, hdd_baseline=2850.5, cdd_baseline=320.0)
    # 3. material setup
    mat1 = MaterialEntity(material_id="OKO-INS-042", material_name="EPS Insulation", u_value=0.035, gwp_total=2.5)
    mat2 = MaterialEntity(material_id="OKO-WIN-011", material_name="Triple Glazed Window", u_value=0.8, gwp_total=45.0)
    
    # 4. scenario integration
    scenario = RetrofitScenario(
        scenario_id="RS-2026-001",
        description="Deep energy retrofit for Vienna MFH using EPS and Triple Glazing",
        building=bldg,
        climate=clim,
        materials_applied=[mat1, mat2]
    )
    
    print("🚀 Retrofit Scenario Integrated Successfully!")
    print(scenario.model_dump_json(indent=2))