# DGPI Karnataka: KSISU Skillathon 2026

A reproducible analysis for the District Graduate Pressure Index (DGPI), an early-warning signal designed to identify where graduate-registration pressure should be investigated across Karnataka's 31 districts.

**DGPI is not a measure of unemployment, vacancies, or skill shortages.** It measures Yuvanidhi registrations per 1,000 implied residents. The signal identifies where further investigation may be useful; it does not independently determine funding or training-seat allocation.

## Data Sources

All datasets used in the current analysis are publicly available and contain aggregate, non-personal data.

Source: Economic Survey of Karnataka 2025–26 district tables, Directorate of Economics and Statistics, Government of Karnataka.

The analysis uses three district-level datasets:

- `ka_districts-gddp-pci-2025-26.csv` — GDDP, NDDP, and per capita income.
- `ka-district-yuvanidhi-2025.csv` — Yuvanidhi registrations.
- `ka-district-msme-employment-2025.csv` — MSME enterprises and employment.

## Repository Files

- `reproduce_dgpi-1.py` — script for reproducing the analysis.
- `crosswalk-1.csv` — district-matching table, including match types.
- `indicators-1.csv` — district-level indicators, including income, implied population, DGPI, and MSME employment ratios.

## How to Run

Place the datasets and Python script in the same directory.

Install the dependencies:

```bash
pip install pandas numpy scipy
```

Run the analysis:

```bash
python reproduce_dgpi-1.py
```

The script generates `crosswalk.csv` and `indicators.csv`.

Compare these generated files with the committed reference outputs, `crosswalk-1.csv` and `indicators-1.csv`, to check reproducibility.

## Key Results

The current analysis reports:

- **District matching:** 31 of 31 districts matched.
- **Yuvanidhi matching:** 24 exact matches and 7 alias matches.
- **MSME matching:** 21 exact matches and 10 alias matches.
- **Implied population:** approximately 68.36 million.
- **State DGPI:** 2.17 registrants per 1,000 implied residents.
- **Income association:** Spearman correlation of approximately -0.634; approximately -0.596 without Bengaluru Urban.
- **Bootstrap confidence interval:** approximately -0.83 to -0.34 for the reported Spearman association, using seed 42.
- **Five highest DGPI values:** Raichur (4.03), Kalaburagi (3.55), Bagalkot (3.41), Davanagere (3.17), and Yadgir (3.01).

These findings describe an exploratory, cross-sectional analysis of 31 districts. They do not establish causation or prove the existence of a skill shortage.

## Methodology

### District Matching

District names are matched using normalisation and a documented alias table.

The current crosswalk includes spelling variations and renamed district units. The Ramanagara/Bengaluru South equivalence assumes comparable boundaries and requires independent verification.

### Implied Population

Implied population is calculated as:

`NDDP / per capita income`

This is an approximation, not an official population count. The aggregate total follows from the construction of the estimate and does not independently validate individual district populations.

### District Graduate Pressure Index

DGPI is calculated as:

`Yuvanidhi registrants / implied population × 1,000`

It represents scheme-registration intensity rather than unemployment or skill mismatch.

Yuvanidhi eligibility and participation affect registration counts. The indicator may therefore reflect graduate cohort sizes, eligibility, awareness, and scheme take-up in addition to underlying economic conditions.

### MSME Employment

MSME employment is based on reported enterprise and employment data. The employment figures are workplace-based rather than residence-based, and district-level outliers require review.

## Limitations

- The analysis covers one year and 31 districts. Associations are exploratory, not causal.
- Implied population is derived from per capita income, creating mathematical coupling between income and DGPI.
- The implied population estimate is approximate and should be replaced with suitable official district population projections when available.
- Yuvanidhi registrations are a scheme-specific proxy, not a count of all unemployed graduates.
- MSME employment is workplace-based and may be affected by commuting, migration, reporting differences, and outliers.
- District aliases and boundary assumptions require verification.
- Proposed policy thresholds are pilot rules that require calibration.
- The current analysis does not independently establish training shortages, vacancies, or graduate employment outcomes.

The proposed next phase would incorporate training-supply, vacancy, and graduate-outcome evidence before recommending changes to training capacity.

## AI Assistance Disclosure

AI tools were used as assistants during the preparation of this submission.

- **Claude (Anthropic):** assisted with editing the presentation text and parts of the code and analysis review.
- **Gemini (Google):** assisted with presentation preparation, including background design, and with reviewing the presentation.
- **ChatGPT (OpenAI):** assisted with creating presentation backgrounds and reviewing and critiquing drafts.

The participant selected the datasets, directed the project, reviewed the outputs, and takes responsibility for the submitted work.

## Project Context

Prepared for the KSISU Skillathon 2026.

This repository contains the code, crosswalk, and indicator outputs supporting the DGPI analysis described in the accompanying presentation.
