from pydantic import BaseModel, Field

class ClimateEntity(BaseModel):
    location_id: str = Field(..., description="Unique identifier for the location (e.g., AT-VIE-01)")
    latitude: float = Field(..., ge=-90, le=90, description="Geographical latitude")
    longitude: float = Field(..., ge=-180, le=180, description="Geographical longitude")
    hdd_baseline: float = Field(..., ge=0, description="Heating Degree Days (Annual)")
    cdd_baseline: float = Field(..., ge=0, description="Cooling Degree Days (Annual)")

if __name__ == "__main__":
    dummy_climate = ClimateEntity(
        location_id="AT-VIE-01",
        latitude=48.2082,  # 빈(Vienna) 위도
        longitude=16.3738, # 빈(Vienna) 경도
        hdd_baseline=2850.5,
        cdd_baseline=320.0
    )
    print("✅ Climate Schema is working perfectly!")
    print(dummy_climate.model_dump_json(indent=2))