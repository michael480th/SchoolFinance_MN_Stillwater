# Minnesota Public School Financial Data — Data Request Inventory

*Prepared: July 1, 2026 · Scope: K‑12 public school district financial data in Minnesota*

This is a hierarchical inventory of public data sources and the specific items available (or requestable) under each. It is organized as **Source → Major dataset → Sub-items**. No data has been pulled yet; this is the map of what exists and where to get it.

---

## 1. Minnesota Department of Education (MDE) — primary authoritative source

The state hub for all district financial data. Almost every other dataset derives from MDE's UFARS collection.

### 1.1 UFARS — Uniform Financial Accounting and Reporting Standards
*The statewide standardized chart of accounts; mandated for all districts, charters, and cooperatives since 1980. This is the backbone dataset.*

- **Revenue data** (coded by dimension)
  - By Fund
  - By Source (revenue equivalent of the object dimension)
  - By Finance code (grant/program tracking)
- **Expenditure data** (coded by dimension)
  - By Fund
  - By Program
  - By Object (salaries, benefits, supplies, capital, etc.)
  - By Organization / Site
  - By Course
- **Balance sheet data** (fund balances, assets, liabilities)
- **The six UFARS coding dimensions** (structure to understand any extract)
  - Fund (2-digit) — e.g., 01 General, 02 Food Service, 04 Community Service, 06 Building Construction, plus debt service, trust, internal service, etc.
  - Organization / Site (3-digit)
  - Program (3-digit)
  - Finance (3-digit)
  - Object (expenditures) / Source (revenues) (3-digit)
  - Course (3-digit)
- **Reference material**
  - Current UFARS Manual (FY2026) and prior-year editions
  - Chapter 9 — full List of Codes
  - Chapter 1 — Fund Dimension definitions

### 1.2 MDE Data Center — School Finance Spreadsheets
*The practical download point; most items published as Excel.*

- **General Education spreadsheets**
  - Interactive Projection Models ("WHAT‑IF" models)
  - General Education Revenue calculations
  - General Education Revenue Disparity Reports
  - Operating Referendum data
  - Q‑Comp (Quality Compensation) Revenue
  - Sparsity Revenue
  - Area Learning Center (ALC) revenue
  - Interstate K‑12 Tuition Agreements
  - Trust Land Endowment Payments
  - Levy Summaries
- **Financial Profiles** (per-district revenue/expenditure/fund-balance profiles)
- **Indirect Cost Rates** (annual approved rates for federal/state grant recovery)

### 1.3 Minnesota Funding Reports (MFR)
*District-by-district aid and levy detail.*

- Aid entitlements and payment schedules by program
- Actual general education aid and levy revenue calculations per district/charter
- Proposed levies and updated levy limitations

### 1.4 Levy / Property Tax data
*The local-revenue side of school funding.*

- Levy Certification System (certified levies filed with county auditor + MDE)
- Levy limitation reports (limits by district)
- Tax Shift Information reports
- Payable-year levy limitation & certification files (historical)

### 1.5 Minnesota Report Card (rc.education.mn.gov)
*Public-facing, non-technical.*

- Per-district revenue data
- Per-district expenditure data
- Contextual data (enrollment, demographics, test results) for per-pupil normalization

### 1.6 Fiscal Compliance Table
*Data-quality / validation layer.*

- Auditor-completed annual confirmation that UFARS balance-sheet data ties to the independent audit
- Useful to validate any UFARS extract before analysis

### 1.7 Federal Funding Tracker
- Federal dollars by district (Title programs, IDEA, child nutrition, ESSER/relief, etc.)
- Year-over-year federal funding by district

### 1.8 Independent Financial Audits (submitted to MDE)
- Audited financial data submitted electronically by each district
- Audit report components (see also OSA below)

---

## 2. Minnesota state oversight & context sources

### 2.1 Office of the State Auditor (OSA)
*Independent audit and compliance layer.*

- School district audit reports (those issued under OSA's cover)
- Audit report components required of every district:
  - Comprehensive/Annual Comprehensive Financial Report (CAFR/ACFR)
  - Management Letter
  - Special Purpose (legal compliance) Report
  - Extra-curricular Student Activity Report
- Minnesota Legal Compliance Guide (the standard districts audit against)
- Statewide Single Audit reports (federal award compliance)

### 2.2 Minnesota Management and Budget (MMB)
- Statewide payroll / transparency data
- State budget forecasts (fiscal frame for education funding)

### 2.3 Minnesota Legislature — House Research & nonpartisan offices
*Explanatory, not raw data — the map of how funding works.*

- "Minnesota School Finance: A Guide for Legislators"
- Teacher Compensation and related short subjects
- Fiscal notes / funding formula documentation

---

## 3. Federal / national sources (cross-state comparability)

### 3.1 NCES Common Core of Data — F‑33 School District Finance Survey
*Standardized, comparable across all U.S. districts; ~2 years lagged.*

- Revenues by source (local, state, federal)
- Expenditures by function and by object
- Indebtedness (short- and long-term)
- Assets / cash & investments
- Student membership counts (for per-pupil calculations)
- District identification variables (NCES ID, etc.)

### 3.2 U.S. Census Bureau — Annual Survey of School System Finances
- The underlying collection feeding F‑33
- Technical documentation and questionnaires

### 3.3 MN State Demographic Center — school district data
- Enrollment, population, and demographic context by district

---

## 4. District-level primary documents (most current & granular)

*Not standardized across districts, but the freshest and most detailed. For this project: Stillwater Area Public Schools / ISD 834.*

- Adopted annual budget
- Comprehensive/Annual Comprehensive Financial Report (CAFR/ACFR)
- School board budget presentations and meeting materials
- Truth-in-Taxation (proposed levy) presentations
- Long-range financial / fund-balance projections

---

## 5. Salary & labor data (a known gap area)

*No single statewide teacher salary database — each district bargains its own step-and-lane schedule.*

- MDE historical average-salary spreadsheets (statewide/by district)
- Education Minnesota member bargaining tools & schedules
- NCTQ Teacher Contract Database (major districts)
- MMB payroll data (state-level)
- PELSB Teacher & Paraprofessional Compensation reports
- **Gap:** education support professional (paraprofessional) compensation is not systematically collected statewide

---

## Suggested priority for data gathering

1. **UFARS + MDE Data Center spreadsheets** — authoritative raw revenue/expenditure/fund-balance numbers.
2. **Minnesota Report Card** — fast per-district public views for context and per-pupil normalization.
3. **OSA audit reports + district CAFRs** — verified, detailed figures and fund-balance detail.
4. **NCES F‑33** — national benchmarking against peer districts/states.
5. **Levy / Funding Reports** — local property-tax revenue and aid detail.

---

## Source links

- MDE School Finance — https://education.mn.gov/MDE/dse/schfin/
- MDE Financial Management / UFARS — https://education.mn.gov/mde/dse/schfin/fin/ufars/
- MDE Data Center — https://education.mn.gov/mde/data/
- Minnesota Report Card — https://rc.education.mn.gov/
- MDE Fiscal Compliance Table — https://education.mn.gov/MDE/dse/datasub/FiscCompTable/index.html
- MDE Levy Certification System — https://education.mn.gov/mde/dse/datasub/levycertsys/
- MDE Independent Financial Audits — https://education.mn.gov/MDE/dse/schfin/fin/ifa/
- MDE General Education — https://education.mn.gov/MDE/dse/schfin/GenEd/
- Office of the State Auditor — School Districts — https://www.auditor.state.mn.us/reports-data-analysis/local-government/school-districts/
- MMB Payroll / Transparency Data — https://mn.gov/mmb/transparency-mn/payrolldata.jsp
- MN House Research — School Finance Guide — https://www.house.mn.gov/hrd/pubs/mnschfin.pdf
- NCES F‑33 District Finance Survey — https://nces.ed.gov/ccd/f33agency.asp
- MN State Demographic Center — school district data — https://mn.gov/admin/demography/data-by-place/school-district-data.jsp
- PELSB Teacher & Paraprofessional Compensation Report — https://mn.gov/pelsb/assets/Teacher%20and%20Paraprofessional%20Compensation%20Working%20Group%20Report%20Final_tcm1113-675426.pdf
