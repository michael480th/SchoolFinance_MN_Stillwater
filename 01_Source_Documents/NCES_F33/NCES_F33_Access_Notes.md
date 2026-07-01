# NCES F-33 — Access Notes and Download URLs
# Stillwater Area Public Schools (NCES ID: 2738190)

*Captured: 2026-07-01*

---

## Summary

The NCES F-33 (Local Education Agency Finance Survey) provides standardized federal-format revenue and expenditure data for school districts. The most recent data available via CCD district detail is **FY2022-2023** (see NCES_CCD_District_Profile.md for extracted figures).

---

## NCES Tools — Access Status

| Tool | URL | Status |
|------|-----|--------|
| CCD District Search | https://nces.ed.gov/ccd/districtsearch/ | ✅ Accessible — fiscal tab captured |
| F-33 Peer Search | https://nces.ed.gov/edfin/search/search_intro.asp | ⚠️ Form submission not working via automation |
| ELSI Table Generator | https://nces.ed.gov/ccd/elsi/ | ❌ JavaScript SPA, no accessible text |
| CCD Data Files | https://nces.ed.gov/ccd/files.asp | ❌ JavaScript SPA, no accessible text |

---

## F-33 Bulk Download URLs (Annual Data Files)

These ZIP files contain national F-33 data for all districts. Use NCES ID **2738190** to filter for Stillwater.

| Year | File | URL |
|------|------|-----|
| FY2022-23 | sdf23_1a.zip | https://nces.ed.gov/ccd/data/zip/sdf23_1a.zip |
| FY2021-22 | sdf22_1a.zip | https://nces.ed.gov/ccd/data/zip/sdf22_1a.zip |
| FY2020-21 | sdf21_1a.zip | https://nces.ed.gov/ccd/data/zip/sdf21_1a.zip |
| FY2019-20 | sdf20_1a.zip | https://nces.ed.gov/ccd/data/zip/sdf20_1a.zip |
| FY2018-19 | sdf19_1a.zip | https://nces.ed.gov/ccd/data/zip/sdf19_1a.zip |

*Note: File naming convention is sdfYY_1a.zip where YY = last two digits of fiscal year end.*
*Documentation: https://nces.ed.gov/ccd/f33agency.asp*

---

## Already Captured F-33 Data

The CCD District Detail fiscal tab (captured in NCES_CCD_District_Profile.md) contains the most recent F-33 summary figures for FY2022-2023:
- Total Revenue: $154,733,000 (Federal 5% / Local 40% / State 54%)
- Total Expenditures: $162,354,000
- Total Current Expenditures: $130,603,000 (Instruction 60% / Support 10% / Admin 9% / Ops 21%)

---

## Manual Download Steps

To get multi-year F-33 data for ISD 834:
1. Download the ZIP files from the URLs above
2. Filter rows where `NCESDISTID = 2738190` (or `LEAID = 2738190`)
3. Key fields: `TOTALREV`, `TFEDREV`, `TSTREV`, `TLOCREV`, `TOTALEXP`, `TCURSSVC`, `TINSTRUC`
