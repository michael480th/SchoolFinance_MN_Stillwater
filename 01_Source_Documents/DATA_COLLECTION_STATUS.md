# Data Collection Status — Stillwater Area Public Schools (ISD 834)
*Last updated: 2026-07-01 (Session 4)*
*Resume point: MDE School Finance page navigation COMPLETE. All subpages documented in Navigation Reference. 2025 Act Summary saved. Next: manual downloads of idcplg docs and NCES ZIPs.*

---

## Overall Progress Summary

| Priority | Source | Status | Files |
|----------|--------|--------|-------|
| 1a | UFARS Manual | ✅ URLs captured | MDE_UFARS/UFARS_DOWNLOAD_URLS.md |
| 1b | MDE School Finance — ALL subpages | ✅ COMPLETE | MDE_SchoolFinance_Navigation_Reference.md |
| 1c | MDE Data Center (MFR, Profiles) | ❌ Flash portal — inaccessible | Barriers noted |
| 2a | MARSS enrollment data | ❌ Flash portal — inaccessible | MARSS_Enrollment/ |
| 3a | MN Report Card — Fiscal Transparency | ✅ FY2021–FY2025 | MN_Report_Card/ |
| 3b | MN Report Card — Demographics | ✅ FY2023–FY2026 | MN_Report_Card/ |
| 4a | OSA — ISD 834 audit reports | ✅ None found (ACFRs in own folder) | OSA_Audit_Reports/ |
| 4b | OSA — Legal Compliance Guide 2025 | ✅ Complete (2,204 lines) | OSA_Audit_Reports/ |
| 4c | ACFRs / CAFRs | ✅ FY2021–FY2025 (pre-existing) | ACFRs/ |
| 5a | NCES F-33 | ⚠️ FY2023 summary only; ZIP files need manual download | NCES_F33/ |
| 6a | MN Legislature — School Finance Guide | ✅ 156-page guide (2,046 lines) | MN_Legislature/ |
| 6b | MN Legislature — Act Summaries | ✅ 2025 SS1 Ch.10, 2024 Ch.115, 2024 Ch.109 | MN_Legislature/ |
| 6c | MN Legislature — Compensatory Revenue | ✅ Nov 2025 | MN_Legislature/ |
| 6d | MN Legislature — K-12 Education Tax Credit | ✅ Jan 2026 | MN_Legislature/ |
| 7a | Budget documents | ✅ FY2025-26, FY2026-27 (pre-existing) | Budget_FY2025-26/, Budget_FY2026-27/ |
| 8a | MMB Payroll | ❌ NOT APPLICABLE — state employees only; excludes ISD 834 staff | — |

---

## Files Created This Project

### DATA_COLLECTION_STATUS.md
- This file ✅

### MDE_UFARS/
- `UFARS_DOWNLOAD_URLS.md` — all 18 FY2026 UFARS chapter download URLs

### MDE School Finance Navigation
- `MDE_SchoolFinance_Navigation_Reference.md` — complete reference for ALL MDE school finance subpages:
  - Financial Management (main + all sub-sections)
  - UFARS (chapter URLs)
  - Guidance and Reports
  - Funding Projections and Trends
  - Transportation (main + subpages)
  - Levy Certification Process
  - General Education
  - Special Education
  - MARSS Student Accounting (main + subpage list)
  - Fiscal Monitoring (IDEA compliance)
  - Community Education, ECFE, School Readiness
  - Facilities and Technology (main + LTFM + Health & Safety)
  - Nonpublic
  - PSEO
  - Audits (MDE)
  - ~60+ document IDs (dDocNames) catalogued across all pages
  - All Data Center topic IDs documented (Flash portal barrier noted)

### MN_Report_Card/
- `RC_FiscalTransparency_FY2021.md` through `RC_FiscalTransparency_FY2025.md` (5 files) ✅
- `RC_Demographics_FY2023.md` through `RC_Demographics_FY2026.md` (4 files) ✅

### NCES_F33/
- `NCES_CCD_District_Profile.md` — ISD 834 profile, FY2022-23 F-33 summary data (NCESDISTID=2738190)
- `NCES_F33_Access_Notes.md` — bulk ZIP download URLs for FY2019-20 through FY2022-23

### OSA_Audit_Reports/
- `OSA_SchoolDistricts_Page_Notes.md` — confirms no ISD 834 entries in OSA report list
- `OSA_LegalComplianceGuide_2025_SchoolDistricts.txt` — full 2025 guide (2,204 lines) ✅
- `OSA_LegalComplianceGuide_2025_SummaryOfChanges.md` — summary of 2024→2025 changes ✅

### MN_Legislature/
- `MNSchoolFinanceGuide_Nov2025.txt` — 156-page legislator guide, Nov 2025 (2,046 lines) ✅
- `ActSummary_2025_1SS_Ch10_K12FinancePolicy.txt` — 2025 SS1 H.F. 5 (1,064 lines) ✅
- `ActSummary_2024_Ch115_K12Finance.txt` — 2024 Ch.115 K-12 Finance ✅
- `ActSummary_2024_Ch109_EducationPolicy.txt` — 2024 Ch.109 Education Policy ✅
- `CompensatoryRevenue_Nov2025.md` — compensatory revenue formula reference ✅
- `K12EducationSubtractionCredit_Jan2026.md` — tax subtraction/credit reference ✅
- `HouseResearch_Education_URLs.md` — index of all MN House Research education publications ✅

---

## Automation Barriers

| Barrier | Systems Affected | Workaround |
|---------|-----------------|------------|
| Flash/Java portal | MDE Data Center (all TOPICID URLs) | Manual access with Flash-enabled browser |
| idcplg file system | All MDE document downloads | Chrome can navigate but PDF text not extractable; use manual download |
| Proxy block | NCES bulk ZIP downloads from bash sandbox | Manual download, then filter NCESDISTID=2738190 |
| OSA report search | JavaScript client-side filter | Direct URL params don't filter; must search manually |

---

## Key Document IDs for Manual Download

### MDE idcplg Priority Documents
URL pattern: `https://education.mn.gov/mdeprod/idcplg?IdcService=GET_FILE&dDocName=XXXXX&RevisionSelectionMethod=latestReleased&Rendition=primary`

| Document | dDocName | Priority | Notes |
|----------|----------|----------|-------|
| **2025 Enacted E-12 Legislative Funding District-Charter Summary** | **PROD086587** | **HIGH** | Per-district funding breakdown — Excel file |
| District Revenues & Expenditures Budget FY2026/27 | 005481 | HIGH | District-level budget data |
| School Business Bulletin 78 (May 2026) | PROD099250 | HIGH | Most recent guidance bulletin |
| School Business Bulletin 77 (Nov 2025) | PROD098320 | HIGH | Previous guidance bulletin |
| Max Revenue Health Safety & Env. Mgmt FIN-352 FY2026-27 | PROD082577 | HIGH | ISD 834 LTFM/H&S revenue cap |
| FY27 Compensatory Revenue Hold Harmless | PROD098832 | MED | ISD 834 comp rev adjustment |
| Payable 2027 Levy Limitation and Certification Calendar | PROD086588 | MED | Levy calendar |
| FY 2027 English Learner Cross Subsidy Revenue | PROD099496 | MED | EL revenue data |
| Preliminary FY2027 Compensatory Revenue | PROD098788 | MED | Comp rev projections |
| FY 2028 LTFM Ten-Year Revenue Projection (form) | PROD086516 | LOW | LTFM planning form |
| 2024-25 LTFM Approved-UFARS Cost Reconciliation FY2025 | PROD098238 | LOW | LTFM reconciliation |
| LTFM Guide for Allowable Expenditures | 022061 | LOW | Reference guide |
| UFARS Code Request | 005483 | LOW | Admin form |

### MDE Data Center — Flash Portal (Manual Access Required)
All at: `https://public.education.mn.gov/MDEAnalytics/DataTopic.jsp?TOPICID=XX`

| Topic | TOPICID | Key Content for ISD 834 |
|-------|---------|------------------------|
| Minnesota Funding Reports (MFR) | 9 | Per-district revenue/expenditure reports |
| General Education | 44 | ADM, enrollment, gen ed aid |
| Financial Profiles | 42 | District financial profile spreadsheets |
| Indirect Cost Rates | 45 | Indirect cost rate tables |
| Transportation | 47 | Transportation revenue/expenditure data |
| Facilities and Technology | 48 | Building age reports, review & comment |

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
├── ACFRs/                              ✅ FY2021-FY2025 (5 PDFs, pre-existing)
├── Budget_FY2025-26/                   ✅ (pre-existing)
├── Budget_FY2026-27/                   ✅ (pre-existing)
├── DATA_COLLECTION_STATUS.md           ✅ This file
├── MDE_SchoolFinance_Navigation_Reference.md  ✅ ALL subpages documented
├── MDE_UFARS/
│   └── UFARS_DOWNLOAD_URLS.md          ✅ All chapter URLs
├── MDE_Financial_Profiles/             ❌ Flash portal — manual access needed
├── MDE_Funding_Reports_MFR/            ❌ Flash portal — manual access needed
├── MDE_GeneralEd_Spreadsheets/         ❌ Flash portal — manual access needed
├── MDE_SpecialEd_Spreadsheets/         ❌ Flash portal — manual access needed
├── MDE_Transportation_Spreadsheets/    ❌ Flash portal — manual access needed
├── MDE_Levy/                           ⚠️ Doc IDs captured; PDFs need manual download
├── MARSS_Enrollment/                   ❌ Flash portal — manual access needed
├── MN_Legislature/                     ✅ 7 files (guides, act summaries, formula refs)
├── MN_Report_Card/                     ✅ 9 files (fiscal FY2021-25, demographics FY2023-26)
├── NCES_F33/                           ⚠️ FY2023 summary; ZIP files need manual download
└── OSA_Audit_Reports/                  ✅ Legal compliance guide + notes (3 files)
```

---

## Next Steps (Priority Order)

### 1. Manual Downloads — Cannot Automate

**MDE idcplg documents** (open in Chrome, save PDF):
- PROD086587 → `01_Source_Documents/MDE_Levy/` — district-charter funding summary
- 005481 → `01_Source_Documents/MDE_Financial_Profiles/` — district budget data
- PROD099250 → `01_Source_Documents/MDE_Financial_Profiles/` — School Business Bulletin 78
- PROD082577 → `01_Source_Documents/MDE_Financial_Profiles/` — H&S/LTFM max revenue

**MDE Data Center** (requires Flash-enabled browser or alternative):
- TOPICID=9 (MFR) → `MDE_Funding_Reports_MFR/`
- TOPICID=42 (Financial Profiles) → `MDE_Financial_Profiles/`
- TOPICID=44 (General Education) → `MDE_GeneralEd_Spreadsheets/`
- TOPICID=47 (Transportation) → `MDE_Transportation_Spreadsheets/`
- TOPICID=48 (Facilities) → (add to MDE_Financial_Profiles/)

**NCES F-33 ZIP files** → filter to NCESDISTID=2738190 → save rows to `NCES_F33/`

### 2. Potentially Automatable (lower priority)
- MDE MARSS subpages (memo lists, reporting instructions) — additional document IDs
- MDE Facilities subpages (Lease Authority, School Construction, Alternative Facilities)
- MDE Charter Schools page (/MDE/dse/schfin/char/)
- Additional MN House Research publications (Dual Enrollment, Teacher Recruitment)
- MN Report Card — test scores/proficiency data for ISD 834

### 3. No Action Needed
- MMB payroll data: state employees only — ISD 834 staff NOT included
- OSA interactive dashboards: aggregate state data only

