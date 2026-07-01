# Minnesota Public School Financial Data — Data Request Inventory

*Prepared: July 1, 2026 · Scope: K‑12 public school district financial data in Minnesota*
*MDE sections below verified against live education.mn.gov pages on July 1, 2026.*

This is a hierarchical inventory of public data sources and the specific items available (or requestable) under each. Organized as **Source → Major dataset → Sub-items**. No data has been pulled yet; this is the map of what exists and where to get it.

> Note on MDE's Data Center: the actual spreadsheets and reports live in an interactive analytics portal at **pub.education.mn.gov/MDEAnalytics/Data.jsp** ("School Finance Reports and Spreadsheets"). The report lists render inside a dynamic widget, so exact file names/vintages must be read in that portal directly; the category structure below is confirmed from the MDE topic pages that point into it.

---

## 1. Minnesota Department of Education (MDE) — primary authoritative source

The MDE School Finance Division administers the state's PreK‑12 finance system: it collects student and financial data from local education agencies (LEAs), calculates aid entitlements/payments and levy limitations, and audits the data driving aids and levies. It works with district business managers, MMB, the Department of Revenue, and county auditors.

**The division's subject areas (each a distinct data topic):** Audits · Charter Schools · Community Education/ECFE/School Readiness · Facilities and Technology · Federal Aid · Fiscal Monitoring · Financial Management · Funding Projections and Trends · General Education · Levy Certification · MARSS Student Accounting · Nonpublic · PSEO · Special Education · Transportation.

### 1.1 UFARS — Uniform Financial Accounting and Reporting Standards
*The statewide standardized chart of accounts; administered by Financial Management; mandated for all districts, charters, and cooperatives since 1980. The backbone dataset — the source of most revenue/expenditure data.*

- **Revenue data** (coded by dimension: Fund, Organization, Program, Finance, Source, Course)
- **Expenditure data** (same dimensions, with Object instead of Source)
- **Balance sheet data** (fund balances, assets, liabilities)
- **The six UFARS coding dimensions**
  - Fund (2-digit) — e.g., 01 General, 02 Food Service, 04 Community Service, 06 Building Construction; plus debt service, trust, internal service, etc.
  - Organization / Site (3-digit)
  - Program (3-digit)
  - Finance (3-digit)
  - Object [expenditures] / Source [revenues] (3-digit)
  - Course (3-digit)
- **Reference material**
  - Current UFARS Manual (FY2026) and prior editions
  - Chapter 1 — Fund Dimension; Chapter 4 — Finance Dimension; Chapter 9 — full List of Codes
  - Voluntary Prekindergarten / School Readiness Plus UFARS code memos

### 1.2 Financial Management section
*Accounting/reporting support; collects and reviews all financial audit data from districts, charters, and cooperatives; administers the MN Credit Enhancement Program.*

- District Revenues and Expenditures Budget (current: FY2026 and FY2027)
- Summary of Audit Requirements (annual)
- Statutory Operating Debt plans / Corrective Action Plans
- GASB 84 Fiduciary Activities guidance; student activity / senior class fund guidance
- School Business Bulletins

### 1.3 MDE Data Center — School Finance Reports & Spreadsheets *(analytics portal)*
*Practical download point; most items are Excel. Organized by the topic areas below.*

- **General Education spreadsheets**
  - Interactive Projection Models ("WHAT‑IF" models)
  - Area Learning Centers (ALC)
  - Operating Referendums
  - Q Comp Revenue
  - General Education Revenue Disparity Reports
  - Trust Land Endowment Payments
  - Levy Summaries
  - Interstate K‑12 Tuition Agreements
  - Sparsity Revenue
- **Special Education spreadsheets**
  - Cross-Subsidy Reports
  - Excess Cost Projection Models
  - Special Education Finance Codes
- **Transportation spreadsheets**
  - Revenue and Expenditures Analysis
  - Pupil Transportation Data
  - District Total Mileage, Hours and Routes
  - Transportation Statistics
- **Facilities and Technology spreadsheets**
  - Building Age Reports
  - Review and Comments
- **Financial Profiles** (per-district revenue/expenditure/fund-balance profiles)
- **Indirect Cost Rates** (annual approved rates for federal/state grant recovery)

### 1.4 Minnesota Funding Reports (MFR) *(analytics portal, Topic ID 9)*
*District-by-district aid and levy detail — the actual calculated numbers.*

- Actual general education aid and levy revenue calculations per district/charter
- Aid entitlements and payment schedules by program
- Proposed levies and updated levy limitations

### 1.5 General Education revenue — program components
*The primary operating-funds program: a mix of state aid + local property tax. Components worth requesting individually:*

- Basic general education revenue
- Extended time revenue
- Gifted and talented revenue
- Basic skills / compensatory revenue
- Sparsity revenue
- Operating capital revenue
- Quality Compensation (Q Comp) revenue
- Referendum revenue

### 1.6 Levy Certification / Property Tax data
*The local-revenue side of school funding.*

- Levy Certification System (the filing/certification system itself)
- Proposed property tax levy (certified to MDE + county auditor by Sept 30)
- Final property tax levy (certified by ~Dec 28)
- Levy limitation reports and Payable-year Levy Limitation & Certification Calendar
- Debt Excess Fund Balance reports
- Levy Forms and Instructions (annual)
- Certification of Truth-in-Taxation (TnT) Compliance *(filed to Dept. of Revenue, not MDE)*

### 1.7 MARSS — Minnesota Automated Reporting Student System
*Not dollars, but the student counts that drive nearly every funding formula — essential for per-pupil work.*

- October 1 enrollments
- December 1 child counts (special education)
- Average Daily Membership (ADM) / pupil units

### 1.8 Funding Projections and Trends
*Forecast and legislative-session spreadsheets.*

- Enacted E‑12 Legislative Funding District/Charter Summary (by year)
- Formula Allowance Inflation Adjustment memos
- Compensatory Revenue (preliminary/final, hold-harmless)
- English Learner (EL) Cross Subsidy Revenue
- READ Act / Literacy Aid
- Q Comp funding summaries
- Student Support Personnel Aid; School Library Aid; School Unemployment Aid

### 1.9 Federal Aid
- Federal aid program allocations to districts/charters (by program)
- Compensatory reporting / funding memos
- (Historic: EdJobs Fund allocations)

### 1.10 Audits (MDE audit section)
*Verification audits — distinct from the independent financial audits below.*

- Verification of district pupil counts, levy limitations, and aid entitlements
- Minimum 25 districts audited annually (M.S. 127A.41, subd. 3)
- Procedures for Conducting District Audits and Audit Appeals

### 1.11 Independent Financial Audits (submitted to MDE)
- Audited financial data submitted electronically by each LEA
- Fiscal Compliance Table — auditor-completed annual confirmation that UFARS balance-sheet data ties to the independent audit (data-quality/validation layer)

### 1.12 Minnesota Report Card (rc.education.mn.gov)
*Public-facing, non-technical.*

- Per-district revenue and expenditure data
- Contextual data (enrollment, demographics, test results) for per-pupil normalization

---

## 2. Minnesota state oversight & context sources

### 2.1 Office of the State Auditor (OSA)
*Independent audit and compliance layer.*

- School district audit reports (those issued under OSA's cover)
- Required audit report components for every district:
  - Comprehensive/Annual Comprehensive Financial Report (CAFR/ACFR)
  - Management Letter
  - Special Purpose (legal compliance) Report
  - Extra-curricular Student Activity Report
- Minnesota Legal Compliance Guide (the standard districts audit against)
- Statewide Single Audit reports (federal award compliance)

### 2.2 Minnesota Management and Budget (MMB)
- Statewide payroll / transparency data
- State budget forecasts (fiscal frame for education funding)

### 2.3 Minnesota Legislature — House Research & Fiscal
*Explanatory, not raw data — the map of how funding works.*

- "Minnesota School Finance: A Guide for Legislators"
- "Financing Education in Minnesota" (annual, House Fiscal)
- Teacher Compensation and related short subjects

### 2.4 Minnesota Department of Revenue
- Truth-in-Taxation program and compliance data
- K‑12 Education Credit Assignment Program

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
- Truth-in-Taxation (proposed levy) presentation
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

1. **UFARS + Data Center spreadsheets + MFR** — authoritative raw revenue/expenditure/fund-balance numbers and calculated aid/levy.
2. **MARSS** — enrollment/ADM to normalize everything per pupil.
3. **Minnesota Report Card** — fast per-district public views for context.
4. **OSA audit reports + district CAFRs** — verified, detailed figures and fund-balance detail.
5. **NCES F‑33** — national benchmarking against peer districts/states.

---

## Source links

- MDE School Finance — https://education.mn.gov/MDE/dse/schfin/
- MDE Financial Management (UFARS) — https://education.mn.gov/MDE/dse/schfin/fin/
- MDE General Education — https://education.mn.gov/MDE/dse/schfin/GenEd/
- MDE Levy Certification — https://education.mn.gov/MDE/dse/schfin/Levy/
- MDE Special Education Finance — https://education.mn.gov/MDE/dse/schfin/sped/
- MDE Transportation — https://education.mn.gov/MDE/dse/schfin/Trans/
- MDE Facilities and Technology — https://education.mn.gov/MDE/dse/schfin/fac/
- MDE Federal Aid — https://education.mn.gov/MDE/dse/schfin/aid/
- MDE Funding Projections and Trends — https://education.mn.gov/MDE/dse/schfin/trend/
- MDE Audits — https://education.mn.gov/MDE/dse/schfin/aud/
- MDE MARSS Student Accounting — https://education.mn.gov/MDE/dse/schfin/MARSS/
- Data Center — School Finance Reports & Spreadsheets — https://pub.education.mn.gov/MDEAnalytics/Data.jsp
- Minnesota Funding Reports (MFR) — https://pub.education.mn.gov/MDEAnalytics/DataTopic.jsp?TOPICID=9
- Minnesota Report Card — https://rc.education.mn.gov/
- Office of the State Auditor — School Districts — https://www.auditor.state.mn.us/reports-data-analysis/local-government/school-districts/
- MMB Payroll / Transparency Data — https://mn.gov/mmb/transparency-mn/payrolldata.jsp
- MN House — Financing Education in Minnesota — https://www.house.mn.gov/Fiscal/Download/3620
- MN House Research — School Finance Guide — https://www.house.mn.gov/hrd/pubs/mnschfin.pdf
- MN Dept. of Revenue — Truth-in-Taxation — https://www.revenue.state.mn.us/truth-taxation
- NCES F‑33 District Finance Survey — https://nces.ed.gov/ccd/f33agency.asp
- MN State Demographic Center — school district data — https://mn.gov/admin/demography/data-by-place/school-district-data.jsp
- PELSB Teacher & Paraprofessional Compensation Report — https://mn.gov/pelsb/assets/Teacher%20and%20Paraprofessional%20Compensation%20Working%20Group%20Report%20Final_tcm1113-675426.pdf
