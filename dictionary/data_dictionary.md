# Hana Energy Data Dictionary

## Overview
This document defines the core data entities, attributes, and sources used within the Hana Energy Building Data Infrastructure. It serves as the single source of truth for all data mapping and ETL processes.

## 1. Building Entity
| Field Name | Data Type | Source | Description |
|:---|:---|:---|:---|
| `building_id` | String | Internal | Unique identifier for the building asset. |
| `construction_year` | Integer | TABULA | The year the building was originally constructed. |
| `building_type` | String | TABULA | Classification of the building (e.g., Single Family House, Multi Family House). |
| `climate_zone` | String | EU Taxonomy / EPC | Designated European climate zone code. |
| `total_floor_area` | Float | EPC / Internal | Gross floor area of the building in square meters (m²). |
| `heating_system` | String | TABULA / EPC | Primary heating system installed in the building. |

## 2. Climate Entity
| Field Name | Data Type | Source | Description |
|:---|:---|:---|:---|
| `latitude` | Float | Open-Meteo | Geographical latitude coordinate. |
| `longitude` | Float | Open-Meteo | Geographical longitude coordinate. |
| `hdd_baseline` | Float | Open-Meteo | Heating Degree Days (HDD) representing annual heating demand. |
| `cdd_baseline` | Float | Open-Meteo | Cooling Degree Days (CDD) representing annual cooling demand. |

## 3. Material Entity
| Field Name | Data Type | Source | Description |
|:---|:---|:---|:---|
| `material_id` | String | Internal | Unique identifier for the construction material. |
| `material_name` | String | ÖKOBAUDAT | Standardized name of the building material. |
| `u_value` | Float | Manufacturer / ÖKOBAUDAT | Thermal transmittance value (W/m²K). |
| `gwp_total` | Float | ÖKOBAUDAT | Global Warming Potential (kgCO₂e/kg) indicating embodied carbon. |
| `density` | Float | ÖKOBAUDAT | Material density (kg/m³). |
| `service_life` | Integer | ÖKOBAUDAT | Estimated service life of the material in years. |