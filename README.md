<!-- BADGES WITH LINKS -->
[![GIS](https://img.shields.io/badge/GIS-Geospatial%20Analysis-4682B4)](https://www.esri.com/en-us/what-is-gis/overview)
[![ArcGIS Pro](https://img.shields.io/badge/ArcGIS%20Pro-Spatial%20Analyst-1E90FF)](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview)
[![MCDA](https://img.shields.io/badge/MCDA-Decision%20Analysis-32CD32)](https://en.wikipedia.org/wiki/Multiple-criteria_decision_analysis)
[![AHP](https://img.shields.io/badge/AHP-Analytic%20Hierarchy%20Process-228B22)](https://en.wikipedia.org/wiki/Analytic_hierarchy_process)
[![Raster Analysis](https://img.shields.io/badge/Raster%20Analysis-Spatial%20Modelling-8A2BE2)](https://pro.arcgis.com/search/?q=Raster%20Analysis&collection=help&product=arcgis-pro&language=en)
[![Least Cost Path](https://img.shields.io/badge/Least--Cost%20Path-Network%20Routing-FF8C00)](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/optimal-path-as-line.htm)
[![Python (ArcGIS)](https://img.shields.io/badge/Python-ArcGIS%20Raster%20Calculator-FFD43B)](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/raster-calculator.htm)

# Pipeline-Routing-GIS

## Project Overview
This project develops a GIS-based Multi-Criteria Decision Analysis (MCDA) framework to identify an optimal gas pipeline corridor across North and North-East Lincolnshire, UK, supporting infrastructure development for the Humber Carbon Capture and Storage (CCS) network.

The model integrates environmental, engineering, and regulatory constraints within ArcGIS Pro to generate a constraint-compliant least-cost pipeline alignment between **Drax Power Station** and the **WINGAS Saltfleetby** storage facility. The workflow demonstrates how geospatial modelling can support strategic infrastructure planning in complex landscapes.

The final optimized alignment measures **94 km** and avoids protected landscapes and geohazard exclusion zones while maintaining engineering feasibility.

---

## Project Workflow

### 1. Spatial Data Preparation
- Dataset standardization and rasterization  
- Projection: **OSGB 1936 / British National Grid**  
- **25 m** raster resolution  

### 2. Criteria Development
- Land use / land cover  
- Built-up areas  
- Flood risk zones  
- SSSI ecological sites  
- Areas of Outstanding Natural Beauty (AONB)  
- Bedrock geology  
- Slope  
- Fault proximity  
- Landslide susceptibility  

### 3. Criteria Standardization
- Raster reclassification using a **1–4 suitability scale**

### 4. Weight Derivation
- **Analytic Hierarchy Process (AHP)** used to determine relative importance of criteria

### 5. Suitability Analysis
- Weighted Overlay to generate a composite suitability surface

### 6. Constraint Enforcement
- AONB and landslide zones implemented as **hard exclusions** using raster algebra

### 7. Least-Cost Routing
- Cost surface derived from land use  
- Distance Accumulation  
- Back Direction  
- Optimal Path extraction  

### 8. Route Validation
- Intersection analysis against environmental and hazard constraints

---

## Repository Structure

### **Data/**
Contains spatial datasets used in the modelling process, including environmental protection layers, hazard zones, land-use information, infrastructure networks, and terrain data. These datasets serve as the primary inputs for the suitability modelling framework.

### **Scripts/**
Contains raster algebra expressions used within ArcGIS Pro to enforce spatial constraints. Python was used only within ArcGIS tools (Raster Calculator / ModelBuilder) for constraint enforcement.

### **Model/**
Contains ArcGIS ModelBuilder workflows used to automate spatial processing tasks and reproduce the MCDA workflow.

### **Outputs/**
Includes final analytical results such as suitability maps, cost surfaces, and the derived optimal pipeline route.

### **Figures/**
Contains maps, workflow diagrams, and visual outputs illustrating the modelling process and results.

### **Documentation/**
Contains supplementary notes describing methodological decisions, modelling assumptions, and analytical procedures.

---

## How to Use the Repository

1. Download or clone the repository.  
2. Open the project workspace in **ArcGIS Pro**.  
3. Load spatial datasets from the **data** folder.  
4. Run the preprocessing workflows to prepare and standardize spatial datasets into raster format.  
5. Apply the suitability modelling process by combining standardized raster layers using weighted overlay analysis.  
6. Execute cost-distance analysis to calculate cumulative movement cost.  
7. Run least-cost path analysis to extract the optimal pipeline alignment.  
8. Review outputs stored in the **outputs** folder.

Users may modify suitability scores or weighting parameters to explore alternative routing scenarios.

---

## Key Results
- **Optimized pipeline route:** 94 km  
- **Protected landscapes avoided:** 100% (no AONB intersections)  
- **Geohazard compliance:** landslide zones excluded  
- **Improved regulatory feasibility** compared to baseline cost-only routing  

---

## Tools and Technologies
- **ArcGIS Pro**
  - Spatial Analyst  
  - ModelBuilder  
  - Raster Calculator  
  - Distance Accumulation  
  - Optimal Path as Line  

---

## Key Skills Demonstrated
- GIS Multi-Criteria Decision Analysis (MCDA)  
- Analytic Hierarchy Process (AHP)  
- Spatial suitability modelling  
- Raster-based geospatial analysis  
- Least-cost path modelling  
- Infrastructure corridor planning  
- Constraint modelling  

---

## Applications
- Pipeline corridor planning  
- Linear infrastructure routing  
- Energy transition infrastructure  
- Environmental impact minimization  
- Spatial risk assessment  

---

## Author
Chika Akwarandu  
MSc Geographic Information Systems  
University of Portsmouth
