# DGPI Karnataka: KSISU Skillathon 2026

Reproducible code and data for the District Graduate Pressure Index (DGPI), an early-warning signal for where to investigate graduate registration pressure across Karnataka's 31 districts.

**DGPI is not unemployment, a vacancy count or a skill-shortage measure.** It is Yuvanidhi registrants per 1,000 residents (implied). A signal triggers a diagnosis; it does not allocate funds on its own.

## Data
All public, non-personal. Source: Economic Survey of Karnataka 2025-26 district tables (Directorate of Economics and Statistics, Government of Karnataka).
- `ka_districts-gddp-pci-2025-26.csv`: GDDP, NDDP, per capita income
- `ka-district-yuvanidhi-2025.csv`: Yuvanidhi registrations
- `ka-district-msme-employment-2025.csv`: MSME units and employment

## Files
- `reproduce_dgpi.py`: runs the whole analysis
- `crosswalk.csv`: district name match across the three tables, with match type
- `indicators.csv`: income, implied population, DGPI and MSME job density per district

## How to run
Put all files in one folder, then:
`pip install pandas numpy scipy`
`python reproduce_dgpi.py`

## Expected output
- 31 of 31 districts matched. Yuvanidhi: 24 exact, 7 alias. MSME: 21 exact, 10 alias.
- Implied population: 68.36 million. State DGPI: 2.17 per 1,000.
- Spearman correlation, income vs DGPI: -0.634 (-0.596 without Bengaluru Urban). Bootstrap 95% CI about -0.83 to -0.34 (seed 42).
- Top five by DGPI: Raichur 4.03, Kalaburagi 3.55, Bagalkote 3.41, Davanagere 3.17, Yadgir 3.01.

## Method notes
- District names are matched through a documented alias table (spelling variants and renamed units). Ramanagara = Bengaluru South assumes the same boundary.
- Implied population = NDDP / per capita income. This is an approximation, not a census count, and the total matches the state figure by construction.
- Yuvanidhi covers only 2022-23 graduates who remain unemployed for 180 days, so DGPI also reflects graduate output and scheme take-up.

## Limitations
One year, 31 districts: association, not causation. MSME employment is workplace-based and has outliers (for example Bengaluru Rural). The thresholds in the proposal are pilot rules to be calibrated.

## AI disclosure
Claude (Anthropic) was used as an assistant for the code and the analysis review. The participant selected the data, directed the work and takes responsibility for the content.
