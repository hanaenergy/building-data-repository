# Hana Energy: Building Data Infrastructure for Europe

## Vision and Overview
The European building sector is highly fragmented, with energy, material, and climate data scattered across disparate local databases (TABULA, OKOBAUDAT, Open-Meteo, EPC registries). 

Hana Energy is building the foundational Data Infrastructure that connects these isolated datasets into a single, unified Knowledge Graph. 
This repository (`building-data-repository`) serves as the Core Schema and Data Dictionary. It acts as the central rulebook of our data infrastructure, strictly defining how data should be structured, validated, and integrated before it is processed by any ETL pipelines.

> Note: This repository holds the Data Models (Pydantic Schemas) and Data Lineage. The actual execution of data extraction and transformation is handled separately in our `building-data-pipeline` repository.

## Repository Structure

```text
building-data-repository/
├── schemas/                 # Pydantic schemas enforcing data validation
│   ├── building.py          # Schema for building archetypes (e.g., TABULA)
│   ├── material.py          # Schema for construction materials (e.g., OKOBAUDAT)
│   ├── climate.py           # Schema for weather and climate (e.g., Open-Meteo)
│   └── retrofit_scenario.py # Integrated schema combining Building, Material, and Climate
├── dictionary/              # Centralized Data Dictionary 
│   └── data_dictionary.md   # Detailed mapping of all entity fields and sources
├── lineage/                 # Data architecture and flow diagrams
│   └── data_lineage.md      # Mermaid.js flowcharts
└── README.md                # Project documentation
```

## Core Technologies
* Python 3.10+
* Pydantic: For rigorous data validation and schema enforcement.
* Mermaid.js: For generating dynamic data lineage architectures.

## How to Run the Schemas
To verify the integrity of the data models and see how the integrated RetrofitScenario generates a unified JSON structure, run the following commands:

```bash
# Activate virtual environment (Windows)
.\.venv\Scripts\activate

# Run the integrated scenario schema
python schemas/retrofit_scenario.py
```

## Roadmap and Next Steps
- [x] Define Base Entities (Building, Material, Climate)
- [x] Establish Integrated Retrofit Scenario Schema
- [ ] Ingest sample data from OKOBAUDAT API matching the MaterialEntity
- [ ] Connect building-data-pipeline to consume these schemas as a dependency