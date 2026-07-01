# Data Collection Status — Stillwater Area Public Schools (ISD 834)
*Last updated: 2026-07-01*
*Resume point: Session 3 — MDE navigation reference complete, OSA legal compliance guide captured, continuing NCES F-33 and other sources*

---

## Overall Progress Summary

| Priority | Source | Status | Files |
|----------|--------|--------|-------|
| 1a | UFARS Manual | ✅ URLs captured | MDE_UFARS/UFARS_DOWNLOAD_URLS.md |
| 1b | MDE School Finance pages | ✅ Complete | MDE_SchoolFinance_Navigation_Reference.md |
| 1c | MDE Financial Management docs | ✅ Document IDs captured | See Navigation Reference |
| 1d | MDE Funding Projections | ✅ Document IDs captured | See Navigation Reference |
| 1e | MDE Data Center (MFR, Profiles) | ❌ Flash portal — inaccessible | MDE_Financial_Profiles/, MDE_Funding_Reports_MFR/ |
| 2a | MARSS enrollment data | ❌ Flash portal — inaccessible | MARSS_Enrollment/ |
| 3a | MN Report Card — Fiscal Transparency | ✅ FY2021–FY2025 | MN_Report_Card/ |
| 3b | MN Report Card — Demographics | ✅ FY2023–FY2026 | MN_Report_Card/ |
| 4a | OSA — ISD 834 audit reports | ✅ None found (ACFRs in own folder) | OSA_Audit_Reports/ |
| 4b | OSA — Legal Compliance Guide 2025 | ✅ Complete (2,204 lines) | OSA_Audit_Reports/ |
| 4c | ACFRs / CAFRs | ✅ FY2021–FY2025 (pre-existing) | ACFRs/ |
| 5a | NCES F-33 | ⚠️ FY2023 summary only | NCES_F33/ |
| 6a | MN Legislature — School Finance Guide | ✅ 156-page guide (2,046 lines) | MN_Legislature/ |
| 6b | MN Legislature — Act Summaries | ✅ 2025 SS1 Ch.10, 2024 Ch.115, 2024 Ch.109 | MN_Legislature/ |
| 6c | MN Legislature — Compensatory Revenue | ✅ Nov 2025 | MN_Legislature/ |
| 6d | MN Legislature — K-12 Education Tax Credit | ✅ Jan 2026 | MN_Legislature/ |
| 7a | Budget documents | ✅ FY2025-26, FY2026-27 (pre-existing) | Budget_FY2025-26/, Budget_FY2026-27/ |
| 8a | MMB Payroll (state employees only) | ❌ Not started — note: excludes ISD 834 staff | MMB_Payroll/ |

---

## Files Created This Project

### MDE_UFARS/
- `UFARS_DOWNLOAD_URLS.md` — all 18 FY2026 chapter download URLs

### MDE School Finance Navigation
- `MDE_SchoolFinance_Navigation_Reference.md` — comprehensive reference for all MDE school finance subpages:
  - Transportation, Levy Certification, Financial Management, UFARS, Guidance and Reports, Funding Projections
  - All document IDs (dDocName) for ~30+ documents
  - All Data Center topic IDs (Flash portal — inaccessible)

### MN_Report_Card/
- `RC_FiscalTransparency_FY2021.md` through `RC_FiscalTransparency_FY2025.md` (5 files) ✅
- `RC_Demographics_FY2023.md` through `RC_Demographics_FY2026.md` (4 files) ✅

### NCES_F33/
- `NCES_CCD_District_Profile.md` — ISD 834 profile, FY2022-23 F-33 data (NCESDISTID=2738190)
- `NCES_F33_Access_Notes.md` — bulk ZIP download URLs (manual download required)

### OSA_Audit_Reports/
- `OSA_SchoolDistricts_Page_Notes.md` — confirms no ISD 834 entries in OSA report list
- `OSA_LegalComplianceGuide_2025_SchoolDistricts.txt` — full 2025 guide (2,204 lines) ✅
- `OSA_LegalComplianceGuide_2025_SummaryOfChanges.md` — summary of 2024→2025 changes ✅

### MN_Legislature/
- `MNSchoolFinanceGuide_Nov2025.txt` — 156-page legislator guide (2,046 lines) ✅
- `ActSummary_2025_SS1_Ch10_K12Finance.txt` ✅
- `ActSummary_2024_Ch115_K12Finance.txt` (2,038 lines) ✅
- `ActSummary_2024_Ch109_EducationPolicy.txt` ✅
- `CompensatoryRevenue_Nov2025.md` ✅
- `K12EducationSubtractionCredit_Jan2026.md` ✅
- `HouseResearch_Education_URLs.md` ✅

---

## Automation Barriers

| Barrier | Systems Affected | Workaround |
|---------|-----------------|------------|
| Flash/Java portal | MDE Data Center (all TOPICID URLs) | Manual access with Flash-enabled browser |
| idcplg file system | All MDE document downloads | Chrome MCP can load but PDF text not extractable |
| JavaScript SPA | MN Report Card (some years), NCES ELSI | Chrome can render; fiscal data accessible per-year |
| Binary/octet-stream | Some MDE/House documents | Manual download |
| Proxy block | NCES bulk ZIP downloads from bash sandbox | Manual download, then filter NCESDISTID=2738190 |
| OSA Report Search | JavaScript filter on client side | Direct URL params don't filter |

---

## Key Document IDs for Manual Download

### MDE idcplg Documents (HIGH PRIORITY)
All use: `https://education.mn.gov/mdeprod/idcplg?IdcService=GET_FILE&dDocName=XXXXX&RevisionSelectionMethod=latestReleased&Rendition=primary`

| Document | dDocName | Priority |
|----------|----------|----------|
| School Business Bulletin 78 (May 2026) | PROD099250 | HIGH |
| School Business Bulletin 77 (Nov 2025) | PROD098320 | HIGH |
| District Revenues & Expenditures Budget FY2026/27 | 005481 | HIGH |
| 2025 Enacted E-12 Legislative Funding District-Charter Summary | PROD086587 | HIGH |
| Payable 2027 Levy Limitation and Certification Calendar | PROD086588 | MED |
| FY27 Compensatory Revenue Hold Harmless | PROD098832 | MED |
| FY 2027 EL Cross Subsidy Revenue | PROD099496 | MED |
| Preliminary FY2027 Compensatory Revenue | PROD098788 | MED |
| 2024 School Finance Award Recipients | PROD084128 | MED |
| Summary of Audit Requirements FY 2026 | 056209 | LOW |

### NCES F-33 ZIP Files (manual download — filter NCESDISTID=2738190)
| Year | URL |
|------|-----|
| FY2022-23 | https://nces.ed.gov/ccd/data/zip/sdf23_1a.zip |
| FY2021-22 | https://nces.ed.gov/ccd/data/zip/sdf22_1a.zip |
| FY2020-21 | https://nces.ed.gov/ccd/data/zip/sdf21_1a.zip |
| FY2019-20 | https://nces.ed.gov/ccd/data/zip/sdf20_1a.zip |

---

## Folder Structure

```
01_Source_Documents/
├── ACFRs/                          ✅ FY2021-FY2025 (5 PDFs, pre-existing)
├── Budget_FY2025-26/               ✅ (pre-existing)
├── Budget_FY2026-27/               ✅ (pre-existing)
├── DATA_COLLECTION_STATUS.md       ✅ This file
├── MDE_SchoolFinance_Navigation_Reference.md  ✅ All subpage doc IDs
├── MDE_UFARS/
│   └── UFARS_DOWNLOAD_URLS.md      ✅ All chapter URLs
├── MDE_Financial_Profiles/         ❌ Flash portal — empty
├── MDE_Funding_Reports_MFR/        ❌ Flash portal — empty
├── MDE_GeneralEd_Spreadsheets/     ❌ Flash portal — empty
├── MDE_SpecialEd_Spreadsheets/     ❌ Flash portal — empty
├── MDE_Transportation_Spreadsheets/❌ Flash portal — empty
├── MDE_Levy/                       ⚠️ Doc IDs captured; PDFs need manual download
├── MARSS_Enrollment/               ❌ Flash portal — empty
├── MMB_Payroll/                    ❌ Not started (note: state employees only, not ISD 834)
├── MN_Legislature/                 ✅ 7 files
├── MN_Legislature_Reference/       (see MN_Legislature/)
├── MN_Report_Card/                 ✅ 9 files (fiscal FY2021-25, demographics FY2023-26)
├── NCES_F33/                       ⚠️ FY2023 summary; ZIP files need manual download
└── OSA_Audit_Reports/              ✅ Legal compliance guide + notes (3 files)
```

---

## Next Steps (Priority Order)

1. **Manual downloads needed** (cannot automate):
   - NCES F-33 ZIP files → filter NCESDISTID=2738190 → save CSV rows
   - MDE idcplg documents (especially PROD086587, 005481, PROD099250)
   - MDE Data Center spreadsheets (requires Flash-enabled browser or alternative access)

2. **Still automatable**:
   - MDE MARSS subpage content and additional document IDs
   - MDE Federal Aid page (/MDE/dse/schfin/aid/)
   - MDE Fiscal Monitoring page (/MDE/dse/schfin/fismont/)
   - Additional MN House Research publications (via web_fetch if PDF)

3. **Lower priority**:
   - MMB payroll data (state employees only — excludes ISD 834 staff)
   - OSA interactive dashboards

