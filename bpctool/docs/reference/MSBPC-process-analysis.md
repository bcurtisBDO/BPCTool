# Azure DevOps Process Analysis
Process Template: MSBPCTemplate
Generated: 2026-08-09T14:11:50.621Z
Work item types: 43 (40 enabled, 3 disabled)

## Contents
|  |  |  |  |
| --- | --- | --- | --- |
| [Action item](#action-item) | [Assumption](#assumption) | [Bug](#bug) | [Business task](#business-task) |
| [Change request](#change-request) | [Configuration](#configuration) | [Decision](#decision) | [Deliverable](#deliverable) |
| [Documentation](#documentation) | [End to end](#end-to-end) | [Enhancement](#enhancement) | [Environment](#environment) |
| [Epic (disabled)](#epic-disabled) | [Feature (disabled)](#feature-disabled) | [Folder](#folder) | [Functional area](#functional-area) |
| [Infrastructure](#infrastructure) | [Integration](#integration) | [Issue](#issue) | [Job](#job) |
| [Migration](#migration) | [Objective](#objective) | [Phase](#phase) | [Process](#process) |
| [Process area](#process-area) | [Report](#report) | [Requirement](#requirement) | [Risk](#risk) |
| [Scenario](#scenario) | [Security](#security) | [Status report](#status-report) | [System process](#system-process) |
| [Task](#task) | [Test Case](#test-case) | [Test Plan](#test-plan) | [Test Suite](#test-suite) |
| [Testing](#testing) | [Ticket](#ticket) | [Tree](#tree) | [User interface](#user-interface) |
| [User Story (disabled)](#user-story-disabled) | [Workflow](#workflow) | [Workshop](#workshop) |  |

## Action item
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Actionitem`

Quick actions, not requiring estimates, a parent work item but must be assigned to someone to ensure completion.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Target Date | Microsoft.VSTS.Scheduling.TargetDate | dateTime | Details | Dates | N/A | The target date for completing the epic |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Original Estimate | Microsoft.VSTS.Scheduling.OriginalEstimate | double | Details | Effort | N/A | Initial value for Remaining Work - set once, when work begins |  | **Yes** |
| Remaining Work | Microsoft.VSTS.Scheduling.RemainingWork | double | Details | Effort | N/A | An estimate of the number of units of work remaining to complete this bug |  | **Yes** |
| Estimated complexity MS BPC | MSBPC.estimatedcomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the estimated complexity (e.g., Small, Medium, Large) for this work item. Use the pick list to indicate project impact. |  | **Yes** |
| Estimated project impact MS BPC | MSBPC.estimatedprojectimpact | string | Details | Planning details | Critical \| High \| Low \| Medium | Select the estimated impact (e.g., Low, Medium, High) this work item will have on the project. Use the pick list to indicate significance. |  | **Yes** |
| Priority | Microsoft.VSTS.Common.Priority | integer | Details | Priority | N/A |  |  | **Yes** |
| Contributor MS BPC | MSBPC.contributor | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the contributor(s) for this work item. Use the pick list to assign roles or individuals. |  | **Yes** |
| Program areas MS BPC | MSBPC.programareas | string | Details | Responsibilities | Business Process Management \| Data Management & Governance \| Executive Leadership \| Infrastructure Management \| Integrations & Interfaces \| Organizational Change Management \| Project Management & Governance \| Reporting & Business Analytics \| Security Management \| Solution Architecture \| Solution Development \| Solution Testing \| Training \| Usability & Experience \| Workflow Management | Choose the program area (e.g., Reporting & Business Analytics, Solution Architecture) that best fits this work item. |  | **Yes** |
| Responsible party MS BPC | MSBPC.responsibleparty | string | Details | Responsibilities | Customer \| Partner | Indicate the party responsible for this work item (e.g., Business Process Owner, Project Manager). |  | **Yes** |
| Responsible role MS BPC | MSBPC.responsiblerole | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the role responsible for this work item (e.g., Application Administrator, Data Architect). Use the pick list for options. |  | **Yes** |
| Role type MS BPC | MSBPC.roletype | string | Details | Responsibilities | Functional \| Governance \| Technical | Choose the type of role involved (e.g., Functional, Technical, Executive). Use the pick list for options. |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Assumption
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Assumption`

Any assumptions or work that will have an impact on the project. The log captures the assumption made, who made it and the next steps.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Target Date | Microsoft.VSTS.Scheduling.TargetDate | dateTime | Details | Dates | N/A | The target date for completing the epic |  | **Yes** |
| Decision maker MS BPC | MSBPC.decisionmaker | string, Identity | Details | Decision details | N/A | The individual who made the decision. |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Priority | Microsoft.VSTS.Common.Priority | integer | Details | Priority | N/A |  |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Bug
- **Enabled:** Yes
- **Class:** Derived
- **Reference name:** `MSBPCTemplate.Bug`

Describes a divergence between required and actual behavior, and tracks the work done to correct the defect and verify the correction.

### States
- Proposed
  - New
- InProgress
  - Active
- Resolved
  - Resolved
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Resolved]
D[Closed]
A --> B
B --> C
C --> D
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Completed Work | Microsoft.VSTS.Scheduling.CompletedWork | double | Details | Effort (Hours) | N/A | The number of units of work that have been spent on this bug |  | **Yes** |
| Original Estimate | Microsoft.VSTS.Scheduling.OriginalEstimate | double | Details | Effort (Hours) | N/A | Initial value for Remaining Work - set once, when work begins |  | **Yes** |
| Remaining Work | Microsoft.VSTS.Scheduling.RemainingWork | double | Details | Effort (Hours) | N/A | An estimate of the number of units of work remaining to complete this bug |  | **Yes** |
| Activity | Microsoft.VSTS.Common.Activity | string | Details | Planning | N/A | Type of work involved |  | **Yes** |
| Priority | Microsoft.VSTS.Common.Priority | integer | Details | Planning | N/A |  |  | **Yes** |
| Resolved Reason | Microsoft.VSTS.Common.ResolvedReason | string | Details | Planning | N/A |  |  | **Yes** |
| Severity | Microsoft.VSTS.Common.Severity | string | Details | Planning | N/A |  |  | **Yes** |
| Story Points | Microsoft.VSTS.Scheduling.StoryPoints | double | Details | Planning | N/A |  |  | **Yes** |
| Postmortem MS BPC | MSBPC.postmortem | html | Details | Postmortem | N/A | Provide the subjective summary as to how well the objective was achieved in the sprint or program increment/tollgate. |  | **Yes** |
| Repro Steps | Microsoft.VSTS.TCM.ReproSteps | html | Details | Repro Steps | N/A |  |  | **Yes** |
| Found In | Microsoft.VSTS.Build.FoundIn | string | Details | System Info | N/A |  |  | **Yes** |
| Integration Build | Microsoft.VSTS.Build.IntegrationBuild | string | Details | System Info | N/A | The build on which the test suite was executed |  | **Yes** |
| System Info | Microsoft.VSTS.TCM.SystemInfo | html | Details | System Info | N/A |  |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Business task
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Businesstask`

A Task that will be integrated with the Mavim application to allow business users to be assigned tasks

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Target Date | Microsoft.VSTS.Scheduling.TargetDate | dateTime | Details | Dates | N/A | The target date for completing the epic |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Original Estimate | Microsoft.VSTS.Scheduling.OriginalEstimate | double | Details | Effort | N/A | Initial value for Remaining Work - set once, when work begins |  | **Yes** |
| Remaining Work | Microsoft.VSTS.Scheduling.RemainingWork | double | Details | Effort | N/A | An estimate of the number of units of work remaining to complete this bug |  | **Yes** |
| Estimated complexity MS BPC | MSBPC.estimatedcomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the estimated complexity (e.g., Small, Medium, Large) for this work item. Use the pick list to indicate project impact. |  | **Yes** |
| Estimated project impact MS BPC | MSBPC.estimatedprojectimpact | string | Details | Planning details | Critical \| High \| Low \| Medium | Select the estimated impact (e.g., Low, Medium, High) this work item will have on the project. Use the pick list to indicate significance. |  | **Yes** |
| Priority | Microsoft.VSTS.Common.Priority | integer | Details | Priority | N/A |  |  | **Yes** |
| Contributor MS BPC | MSBPC.contributor | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the contributor(s) for this work item. Use the pick list to assign roles or individuals. |  | **Yes** |
| Program areas MS BPC | MSBPC.programareas | string | Details | Responsibilities | Business Process Management \| Data Management & Governance \| Executive Leadership \| Infrastructure Management \| Integrations & Interfaces \| Organizational Change Management \| Project Management & Governance \| Reporting & Business Analytics \| Security Management \| Solution Architecture \| Solution Development \| Solution Testing \| Training \| Usability & Experience \| Workflow Management | Choose the program area (e.g., Reporting & Business Analytics, Solution Architecture) that best fits this work item. |  | **Yes** |
| Responsible party MS BPC | MSBPC.responsibleparty | string | Details | Responsibilities | Customer \| Partner | Indicate the party responsible for this work item (e.g., Business Process Owner, Project Manager). |  | **Yes** |
| Responsible role MS BPC | MSBPC.responsiblerole | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the role responsible for this work item (e.g., Application Administrator, Data Architect). Use the pick list for options. |  | **Yes** |
| Role type MS BPC | MSBPC.roletype | string | Details | Responsibilities | Functional \| Governance \| Technical | Choose the type of role involved (e.g., Functional, Technical, Executive). Use the pick list for options. |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Partner phase MS BPC | MSBPC.partnerphase | string | References | Methodology | Partner defined | Select the phase of the partner engagement. Map this to the Success by Design phases for consistency. |  | **Yes** |
| Success by Design phase MS BPC | MSBPC.successbydesignphase | string | References | Methodology | 10 - Strategize \| 20 - Initiate \| 31 - Implement - Analysis \| 32 - Implement - Design \| 33 - Implement - Development \| 34 - Implement - Test \| 45 - Prepare - Train \| 49 - Prepare - Cutover \| 50 - Operate | Select the Success by Design phase (e.g., Strategize, Implement, Test) relevant to this work item. Use the pick list for options. |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Change request
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Changerequest`

The identification that new requirements have come in since the scope of each area has been firmed which requires review and approval by the steering committee to confirm it is allowed to be added to the scope of the project.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Alternative solution MS BPC | MSBPC.alternativesolution | html | Details | Alternative solution | N/A | Determine if there are any other possible solutions that could avoid the need for this change request. |  | **Yes** |
| Change order MS BPC | MSBPC.changeorder | string | Details | Change request details | N/A | Capture the change order number that this change request has been accepted to for execution. |  | **Yes** |
| Change request type MS BPC | MSBPC.changerequesttype | string | Details | Change request details | Design Change \| Estimation Change \| Scope Change | Document the type of change that is being requested in this change request. |  | **Yes** |
| Requestor MS BPC | MSBPC.requestor | string, Identity | Details | Change request details | N/A | Provide the identity of the individual who requested the change. |  | **Yes** |
| Target Date | Microsoft.VSTS.Scheduling.TargetDate | dateTime | Details | Dates | N/A | The target date for completing the epic |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Impact assessment MS BPC | MSBPC.impactassessment | html | Details | Impact assessment | N/A | Provide some context as to what impact this change request has on the project. |  | **Yes** |
| Impedes MS BPC | MSBPC.impedes | html | Details | Impedes | N/A | Provide any documentation if this change request is impeding progress in other areas of the project. |  | **Yes** |
| Justification | Microsoft.VSTS.CMMI.Justification | html | Details | Justification | N/A |  |  | **Yes** |
| Priority | Microsoft.VSTS.Common.Priority | integer | Details | Priority | N/A |  |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Configuration
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Configuration`

A deliverable required to Configure/Setup the system to modify the way it operates without development in order for the processes to occur as desired.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Acceptance Criteria | Microsoft.VSTS.Common.AcceptanceCriteria | html | Details | Acceptance criteria | N/A |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Baseline complexity MS BPC | MSBPC.baselinecomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the baseline complexity (e.g., Simple, Medium, Complex) for this process. This value indicates the baseline suggested complexity for estimating the project effort related to the work product. |  | **Yes** |
| Estimated complexity MS BPC | MSBPC.estimatedcomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the estimated complexity (e.g., Small, Medium, Large) for this work item. Use the pick list to indicate project impact. |  | **Yes** |
| Estimated project impact MS BPC | MSBPC.estimatedprojectimpact | string | Details | Planning details | Critical \| High \| Low \| Medium | Select the estimated impact (e.g., Low, Medium, High) this work item will have on the project. Use the pick list to indicate significance. |  | **Yes** |
| Story Points | Microsoft.VSTS.Scheduling.StoryPoints | double | Details | Planning details | N/A |  |  | **Yes** |
| Contributor MS BPC | MSBPC.contributor | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the contributor(s) for this work item. Use the pick list to assign roles or individuals. |  | **Yes** |
| Program areas MS BPC | MSBPC.programareas | string | Details | Responsibilities | Business Process Management \| Data Management & Governance \| Executive Leadership \| Infrastructure Management \| Integrations & Interfaces \| Organizational Change Management \| Project Management & Governance \| Reporting & Business Analytics \| Security Management \| Solution Architecture \| Solution Development \| Solution Testing \| Training \| Usability & Experience \| Workflow Management | Choose the program area (e.g., Reporting & Business Analytics, Solution Architecture) that best fits this work item. |  | **Yes** |
| Responsible party MS BPC | MSBPC.responsibleparty | string | Details | Responsibilities | Customer \| Partner | Indicate the party responsible for this work item (e.g., Business Process Owner, Project Manager). |  | **Yes** |
| Responsible role MS BPC | MSBPC.responsiblerole | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the role responsible for this work item (e.g., Application Administrator, Data Architect). Use the pick list for options. |  | **Yes** |
| Role type MS BPC | MSBPC.roletype | string | Details | Responsibilities | Functional \| Governance \| Technical | Choose the type of role involved (e.g., Functional, Technical, Executive). Use the pick list for options. |  | **Yes** |
| Scope MS BPC | MSBPC.scope | string | Details | Scoping | 10 - Unspecified \| 20 - In scope \| 30 - Out of scope \| 40 - Not applicable | Define the scope of the work item (e.g., In scope, Out of scope). Use the pick list for boundaries and expectations. | **Yes** | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Authorized for deployment MS BPC | MSBPC.authorizedfordeployment | string | Information | Application lifecycle | Partner defined \| DEV \| TEST \| PROD | Indicate the environment/branch that is authorized next for the code or data attached to this deliverable. |  | **Yes** |
| Current highest deployment MS BPC | MSBPC.currenthighestdeployment | string | Information | Application lifecycle | Partner defined \| DEV \| TEST \| PROD | Indicate what the current highest environment/branch is for the code or data attached to this deliverable. |  | **Yes** |
| Configuration type MS BPC | MSBPC.configurationtype | string | Information | Configuration details | Parameters \| Number sequences \| List of values | Select the type of configuration (e.g., Parameter, Setup data). Use the pick list to clarify configuration details. |  | **Yes** |
| Cutover method MS BPC | MSBPC.cutovermethod | string | Information | Configuration details | Manual configuration \| Data migration upload \| Copy gold database \| Database export/import \| Integration sync \| Initial data sync \| Continous sync \| Third-party tool migration \| AI-Generated configuration \| Unspecified | Pick from the list the manner in which the data will be populated for this configuration. | **Yes** | **Yes** |
| Configuration keys MS BPC | MSBPC.configurationkeys | string | Information | Configuration settings | N/A | Enter any configuration keys relevant to the application or module. Use this to manage feature access and settings. |  | **Yes** |
| Country region codes MS BPC | MSBPC.countryregioncodes | string | Information | Configuration settings | N/A | Enter applicable country or region codes. Use this to specify localization or compliance requirements. |  | **Yes** |
| Feature management keys MS BPC | MSBPC.featuremanagementkeys | string | Information | Configuration settings | N/A | Enter any feature management keys relevant to the application. Use this to control feature availability. |  | **Yes** |
| Data package MS BPC | MSBPC.datapackage | string | Information | Entity details | N/A | Provide the name of the Data Package that this configuration will be added to in order to load into various environments. |  | **Yes** |
| Execution sequence MS BPC | MSBPC.executionsequence | integer | Information | Entity details | N/A | Enter the execution sequence number within the named Data Package for this process or job. Use this to define order of operations. |  | **Yes** |
| Functional design MS BPC | MSBPC.functionaldesign | html | Information | Functional design | N/A | Provide the functional design details (content or hyperlink) for how the solution will meet the business needs. |  | **Yes** |
| At least one MS BPC | MSBPC.atleastone | boolean | Information | Toggles | Default: 0 | Indicate if at least one configuration or recommendation is required. Set to "Yes" if mandatory. | **Yes** | **Yes** |
| Can add later MS BPC | MSBPC.canaddlater | boolean | Information | Toggles | Default: 0 | Indicate if this configuration or field can be added later. Set to "Yes" if it’s not required at initial setup. | **Yes** | **Yes** |
| Can change later MS BPC | MSBPC.canchangelater | boolean | Information | Toggles | Default: 0 | Indicate if this configuration or field can be changed after initial setup. Set to "Yes" if changes are allowed. | **Yes** | **Yes** |
| Continuous MS BPC | MSBPC.continuous | boolean | Information | Toggles | Default: 0 | Indicate if this process or job is continuous. Set to "Yes" for ongoing or recurring activities. | **Yes** | **Yes** |
| Early MS BPC | MSBPC.early | boolean | Information | Toggles | Default: 0 | Indicate if this process or configuration should be completed early in the project lifecycle. Set to "Yes" if applicable. | **Yes** | **Yes** |
| Gold environment MS BPC | MSBPC.goldenvironment | boolean | Information | Toggles | Default: 0 | Indicates if this process or configuration should be completed in the Gold environment. Gold configs are copied to production during cutover. | **Yes** | **Yes** |
| Manadatory MS BPC | MSBPC.mandatory | boolean | Information | Toggles | Default: 0 | Indicate if this field or process is mandatory. Set to "Yes" if required for completion. | **Yes** | **Yes** |
| Multiple are recommended MS BPC | MSBPC.multiplearerecommended | boolean | Information | Toggles | Default: 0 | Indicate if multiple recommendations are suggested for this configuration. Set to "Yes" if more than one approach is recommended. | **Yes** | **Yes** |
| Menu item name MS BPC | MSBPC.menuitemname | string | References | Application details | N/A | Enter the name of the menu item in the application. Use this to identify navigation points. |  | **Yes** |
| Menu path MS BPC | MSBPC.menupath | string | References | Application details | N/A | Enter the menu path for accessing the relevant feature or process. |  | **Yes** |
| Module MS BPC | MSBPC.module | string | References | Application details | Accounts payable \| Accounts receivable \| App settings \| Asset leasing \| Asset management \| Audit workbench \| Benefits management \| Budgeting \| Business Performance Analytics \| Business Performance Planning \| Cash and bank management \| Common \| Consolidations \| Cost accounting \| Cost management \| Credit and collections \| Demand planning \| Engineering change management \| Expense management \| Fiscal books \| Fixed assets \| General ledger \| Human resources \| Inventory \| Inventory management \| Landed cost \| Leave and absence \| Master planning \| Material handling equipment interface \| Organization administration \| Payroll \| Personal settings \| Pricing management \| Procurement and sourcing \| Product information management \| Production control \| Project management and accounting \| Projects \| Questionnaire \| Rebate management \| Resources \| Retail \| Sales \| Sales and marketing \| Sales insights settings \| Scheduling \| Service \| Service management \| Settings \| Subscription billing \| System administration \| Systems settings \| Tax \| Time and attendance \| Transportation management \| Warehouse management | Select the Dynamics 365 module related to this work item (e.g., Accounts payable, Inventory management). Use the pick list for options. |  | **Yes** |
| Application family MS BPC | MSBPC.applicationfamily | string | References | Application information | Azure \| Business Central \| Cross Functional \| Customer Engagement \| Finance and Operations \| Productivity \| Power Platform | Select the application family (e.g., Business Central, Finance and Operations) relevant to this work item. This helps categorize the process. |  | **Yes** |
| Products MS BPC | MSBPC.products | string | References | Application information | Azure \| Business Central \| Commerce \| Contact Center \| Copilot Studio \| Customer Insights Data \| Customer Insights Journey \| Customer Service \| Customer Voice \| Field Service \| Finance \| Fraud Protection \| Guides \| Human Resources \| Microsoft 365 \| Other \| Power Apps \| Power Automate \| Power BI \| Power Pages \| Project \| Project Operations \| Remote Assist \| Sales \| Sales Copilot \| SharePoint \| Supply Chain Management \| Teams \| Customer Insights \| Microsoft Cloud for Sustainability | Select the relevant products (e.g., Business Central, Finance and Operations) associated with this work item. Use the pick list for options. |  | **Yes** |
| Software development company MS BPC | MSBPC.softwaredevelopmentcompany | string | References | Application information | N/A | Enter the name of the Software development company |  | **Yes** |
| Software solutions MS BPC | MSBPC.softwaresolutions | string | References | Application information | N/A | Enter the name(s) of the Software soluionts |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Industries MS BPC | MSBPC.industries | string | References | Industry focus | Agriculture (01-09) \| Construction (15-17) \| Finance, Insurance, Real Estate (60-67) \| Manufacturing (20-39) \| Mining (10-14) \| Public Administration (90-99) \| Retail Trade (52-59) \| Services (70-89) \| Transportation and Public Utilities (40-49) \| Wholesales Trade (50-51) | Select the industry or industries relevant to this work item (e.g., Manufacturing, Retail). Use the pick list for options. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Decision
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Decision`

Any decision or work that are have an impact on the project. The log captures the decision made, who made it and the decision / next steps.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Target Date | Microsoft.VSTS.Scheduling.TargetDate | dateTime | Details | Dates | N/A | The target date for completing the epic |  | **Yes** |
| Decision maker MS BPC | MSBPC.decisionmaker | string, Identity | Details | Decision details | N/A | The individual who made the decision. |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Priority | Microsoft.VSTS.Common.Priority | integer | Details | Priority | N/A |  |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Deliverable
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Deliverable`

This is a work item that defines a Deliverable that will be produced such as the Business Process Catalog, Solution Blueprint, Delivery Plan or Readiness Assessment.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Estimated complexity MS BPC | MSBPC.estimatedcomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the estimated complexity (e.g., Small, Medium, Large) for this work item. Use the pick list to indicate project impact. |  | **Yes** |
| Estimated project impact MS BPC | MSBPC.estimatedprojectimpact | string | Details | Planning details | Critical \| High \| Low \| Medium | Select the estimated impact (e.g., Low, Medium, High) this work item will have on the project. Use the pick list to indicate significance. |  | **Yes** |
| Contributor MS BPC | MSBPC.contributor | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the contributor(s) for this work item. Use the pick list to assign roles or individuals. |  | **Yes** |
| Program areas MS BPC | MSBPC.programareas | string | Details | Responsibilities | Business Process Management \| Data Management & Governance \| Executive Leadership \| Infrastructure Management \| Integrations & Interfaces \| Organizational Change Management \| Project Management & Governance \| Reporting & Business Analytics \| Security Management \| Solution Architecture \| Solution Development \| Solution Testing \| Training \| Usability & Experience \| Workflow Management | Choose the program area (e.g., Reporting & Business Analytics, Solution Architecture) that best fits this work item. |  | **Yes** |
| Responsible party MS BPC | MSBPC.responsibleparty | string | Details | Responsibilities | Customer \| Partner | Indicate the party responsible for this work item (e.g., Business Process Owner, Project Manager). |  | **Yes** |
| Responsible role MS BPC | MSBPC.responsiblerole | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the role responsible for this work item (e.g., Application Administrator, Data Architect). Use the pick list for options. |  | **Yes** |
| Role type MS BPC | MSBPC.roletype | string | Details | Responsibilities | Functional \| Governance \| Technical | Choose the type of role involved (e.g., Functional, Technical, Executive). Use the pick list for options. |  | **Yes** |
| Scope MS BPC | MSBPC.scope | string | Details | Scoping | 10 - Unspecified \| 20 - In scope \| 30 - Out of scope \| 40 - Not applicable | Define the scope of the work item (e.g., In scope, Out of scope). Use the pick list for boundaries and expectations. | **Yes** | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Partner phase MS BPC | MSBPC.partnerphase | string | References | Methodology | Partner defined | Select the phase of the partner engagement. Map this to the Success by Design phases for consistency. |  | **Yes** |
| Success by Design phase MS BPC | MSBPC.successbydesignphase | string | References | Methodology | 10 - Strategize \| 20 - Initiate \| 31 - Implement - Analysis \| 32 - Implement - Design \| 33 - Implement - Development \| 34 - Implement - Test \| 45 - Prepare - Train \| 49 - Prepare - Cutover \| 50 - Operate | Select the Success by Design phase (e.g., Strategize, Implement, Test) relevant to this work item. Use the pick list for options. |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Documentation
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Documentation`

A deliverable required to document a given Process to communicate to the business users what the Policies are and how to perform the given Process during routine operations.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Acceptance Criteria | Microsoft.VSTS.Common.AcceptanceCriteria | html | Details | Acceptance criteria | N/A |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Baseline complexity MS BPC | MSBPC.baselinecomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the baseline complexity (e.g., Simple, Medium, Complex) for this process. This value indicates the baseline suggested complexity for estimating the project effort related to the work product. |  | **Yes** |
| Estimated complexity MS BPC | MSBPC.estimatedcomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the estimated complexity (e.g., Small, Medium, Large) for this work item. Use the pick list to indicate project impact. |  | **Yes** |
| Estimated project impact MS BPC | MSBPC.estimatedprojectimpact | string | Details | Planning details | Critical \| High \| Low \| Medium | Select the estimated impact (e.g., Low, Medium, High) this work item will have on the project. Use the pick list to indicate significance. |  | **Yes** |
| Story Points | Microsoft.VSTS.Scheduling.StoryPoints | double | Details | Planning details | N/A |  |  | **Yes** |
| Contributor MS BPC | MSBPC.contributor | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the contributor(s) for this work item. Use the pick list to assign roles or individuals. |  | **Yes** |
| Program areas MS BPC | MSBPC.programareas | string | Details | Responsibilities | Business Process Management \| Data Management & Governance \| Executive Leadership \| Infrastructure Management \| Integrations & Interfaces \| Organizational Change Management \| Project Management & Governance \| Reporting & Business Analytics \| Security Management \| Solution Architecture \| Solution Development \| Solution Testing \| Training \| Usability & Experience \| Workflow Management | Choose the program area (e.g., Reporting & Business Analytics, Solution Architecture) that best fits this work item. |  | **Yes** |
| Responsible party MS BPC | MSBPC.responsibleparty | string | Details | Responsibilities | Customer \| Partner | Indicate the party responsible for this work item (e.g., Business Process Owner, Project Manager). |  | **Yes** |
| Responsible role MS BPC | MSBPC.responsiblerole | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the role responsible for this work item (e.g., Application Administrator, Data Architect). Use the pick list for options. |  | **Yes** |
| Role type MS BPC | MSBPC.roletype | string | Details | Responsibilities | Functional \| Governance \| Technical | Choose the type of role involved (e.g., Functional, Technical, Executive). Use the pick list for options. |  | **Yes** |
| Scope MS BPC | MSBPC.scope | string | Details | Scoping | 10 - Unspecified \| 20 - In scope \| 30 - Out of scope \| 40 - Not applicable | Define the scope of the work item (e.g., In scope, Out of scope). Use the pick list for boundaries and expectations. | **Yes** | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Menu item name MS BPC | MSBPC.menuitemname | string | References | Application details | N/A | Enter the name of the menu item in the application. Use this to identify navigation points. |  | **Yes** |
| Menu path MS BPC | MSBPC.menupath | string | References | Application details | N/A | Enter the menu path for accessing the relevant feature or process. |  | **Yes** |
| Module MS BPC | MSBPC.module | string | References | Application details | Accounts payable \| Accounts receivable \| App settings \| Asset leasing \| Asset management \| Audit workbench \| Benefits management \| Budgeting \| Business Performance Analytics \| Business Performance Planning \| Cash and bank management \| Common \| Consolidations \| Cost accounting \| Cost management \| Credit and collections \| Demand planning \| Engineering change management \| Expense management \| Fiscal books \| Fixed assets \| General ledger \| Human resources \| Inventory \| Inventory management \| Landed cost \| Leave and absence \| Master planning \| Material handling equipment interface \| Organization administration \| Payroll \| Personal settings \| Pricing management \| Procurement and sourcing \| Product information management \| Production control \| Project management and accounting \| Projects \| Questionnaire \| Rebate management \| Resources \| Retail \| Sales \| Sales and marketing \| Sales insights settings \| Scheduling \| Service \| Service management \| Settings \| Subscription billing \| System administration \| Systems settings \| Tax \| Time and attendance \| Transportation management \| Warehouse management | Select the Dynamics 365 module related to this work item (e.g., Accounts payable, Inventory management). Use the pick list for options. |  | **Yes** |
| Application family MS BPC | MSBPC.applicationfamily | string | References | Application information | Azure \| Business Central \| Cross Functional \| Customer Engagement \| Finance and Operations \| Productivity \| Power Platform | Select the application family (e.g., Business Central, Finance and Operations) relevant to this work item. This helps categorize the process. |  | **Yes** |
| Products MS BPC | MSBPC.products | string | References | Application information | Azure \| Business Central \| Commerce \| Contact Center \| Copilot Studio \| Customer Insights Data \| Customer Insights Journey \| Customer Service \| Customer Voice \| Field Service \| Finance \| Fraud Protection \| Guides \| Human Resources \| Microsoft 365 \| Other \| Power Apps \| Power Automate \| Power BI \| Power Pages \| Project \| Project Operations \| Remote Assist \| Sales \| Sales Copilot \| SharePoint \| Supply Chain Management \| Teams \| Customer Insights \| Microsoft Cloud for Sustainability | Select the relevant products (e.g., Business Central, Finance and Operations) associated with this work item. Use the pick list for options. |  | **Yes** |
| Software development company MS BPC | MSBPC.softwaredevelopmentcompany | string | References | Application information | N/A | Enter the name of the Software development company |  | **Yes** |
| Software solutions MS BPC | MSBPC.softwaresolutions | string | References | Application information | N/A | Enter the name(s) of the Software soluionts |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Industries MS BPC | MSBPC.industries | string | References | Industry focus | Agriculture (01-09) \| Construction (15-17) \| Finance, Insurance, Real Estate (60-67) \| Manufacturing (20-39) \| Mining (10-14) \| Public Administration (90-99) \| Retail Trade (52-59) \| Services (70-89) \| Transportation and Public Utilities (40-49) \| Wholesales Trade (50-51) | Select the industry or industries relevant to this work item (e.g., Manufacturing, Retail). Use the pick list for options. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## End to end
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Endtoend`

The top-level node of the Business Process Catalog.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Process sequence ID MS BPC | MSBPC.processsequenceid | string | Details | Process IDs | N/A | Enter the unique sequence ID for the business process. Use this to organize and reference processes. | **Yes** | **Yes** |
| Scope MS BPC | MSBPC.scope | string | Details | Scoping | 10 - Unspecified \| 20 - In scope \| 30 - Out of scope \| 40 - Not applicable | Define the scope of the work item (e.g., In scope, Out of scope). Use the pick list for boundaries and expectations. | **Yes** | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Application family MS BPC | MSBPC.applicationfamily | string | References | Application information | Azure \| Business Central \| Cross Functional \| Customer Engagement \| Finance and Operations \| Productivity \| Power Platform | Select the application family (e.g., Business Central, Finance and Operations) relevant to this work item. This helps categorize the process. |  | **Yes** |
| Products MS BPC | MSBPC.products | string | References | Application information | Azure \| Business Central \| Commerce \| Contact Center \| Copilot Studio \| Customer Insights Data \| Customer Insights Journey \| Customer Service \| Customer Voice \| Field Service \| Finance \| Fraud Protection \| Guides \| Human Resources \| Microsoft 365 \| Other \| Power Apps \| Power Automate \| Power BI \| Power Pages \| Project \| Project Operations \| Remote Assist \| Sales \| Sales Copilot \| SharePoint \| Supply Chain Management \| Teams \| Customer Insights \| Microsoft Cloud for Sustainability | Select the relevant products (e.g., Business Central, Finance and Operations) associated with this work item. Use the pick list for options. |  | **Yes** |
| Software development company MS BPC | MSBPC.softwaredevelopmentcompany | string | References | Application information | N/A | Enter the name of the Software development company |  | **Yes** |
| Software solutions MS BPC | MSBPC.softwaresolutions | string | References | Application information | N/A | Enter the name(s) of the Software soluionts |  | **Yes** |
| APQC description MS BPC | MSBPC.apqcdescription | string | References | APQC references | N/A | Enter a brief description of the APQC process mapping. Required if APQC ID is provided. |  | **Yes** |
| APQC ID MS BPC | MSBPC.apqcid | string | References | APQC references | N/A | Enter the APQC ID for process mapping. Use this to align with industry-standard process frameworks. |  | **Yes** |
| Business process flow source MS BPC | MSBPC.businessprocessflowsource | string | References | Business process flow details | Microsoft \| Partner \| Customer | Select the organization that created or owns the business process flow. | **Yes** | **Yes** |
| Business process flow status MS BPC | MSBPC.businessprocessflowstatus | string | References | Business process flow details | 10 - Not started \| 20 - Drafted \| 30 - Published \| 40 - Updated \| 50 - Update required | Select the current status of the business process flow (e.g., Not started, In progress).This status indicates the status of the flow diagram from Microsoft being published in the Git Hub repository. | **Yes** | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Industries MS BPC | MSBPC.industries | string | References | Industry focus | Agriculture (01-09) \| Construction (15-17) \| Finance, Insurance, Real Estate (60-67) \| Manufacturing (20-39) \| Mining (10-14) \| Public Administration (90-99) \| Retail Trade (52-59) \| Services (70-89) \| Transportation and Public Utilities (40-49) \| Wholesales Trade (50-51) | Select the industry or industries relevant to this work item (e.g., Manufacturing, Retail). Use the pick list for options. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Alternate process sequence ID MS BPC | MSBPC.alternateprocesssequenceid | string | References | Process IDs | N/A | Enter the alternate sequence ID for deprecated or parallel processes. This value is required for any process that is deprecated and indicates the alternative process to use in place of the deprecated row. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Enhancement
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Enhancement`

A deliverable required in order to modify the application with development in order for the processes to function as desired.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Acceptance Criteria | Microsoft.VSTS.Common.AcceptanceCriteria | html | Details | Acceptance criteria | N/A |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Baseline complexity MS BPC | MSBPC.baselinecomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the baseline complexity (e.g., Simple, Medium, Complex) for this process. This value indicates the baseline suggested complexity for estimating the project effort related to the work product. |  | **Yes** |
| Estimated complexity MS BPC | MSBPC.estimatedcomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the estimated complexity (e.g., Small, Medium, Large) for this work item. Use the pick list to indicate project impact. |  | **Yes** |
| Estimated project impact MS BPC | MSBPC.estimatedprojectimpact | string | Details | Planning details | Critical \| High \| Low \| Medium | Select the estimated impact (e.g., Low, Medium, High) this work item will have on the project. Use the pick list to indicate significance. |  | **Yes** |
| Story Points | Microsoft.VSTS.Scheduling.StoryPoints | double | Details | Planning details | N/A |  |  | **Yes** |
| Contributor MS BPC | MSBPC.contributor | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the contributor(s) for this work item. Use the pick list to assign roles or individuals. |  | **Yes** |
| Program areas MS BPC | MSBPC.programareas | string | Details | Responsibilities | Business Process Management \| Data Management & Governance \| Executive Leadership \| Infrastructure Management \| Integrations & Interfaces \| Organizational Change Management \| Project Management & Governance \| Reporting & Business Analytics \| Security Management \| Solution Architecture \| Solution Development \| Solution Testing \| Training \| Usability & Experience \| Workflow Management | Choose the program area (e.g., Reporting & Business Analytics, Solution Architecture) that best fits this work item. |  | **Yes** |
| Responsible party MS BPC | MSBPC.responsibleparty | string | Details | Responsibilities | Customer \| Partner | Indicate the party responsible for this work item (e.g., Business Process Owner, Project Manager). |  | **Yes** |
| Responsible role MS BPC | MSBPC.responsiblerole | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the role responsible for this work item (e.g., Application Administrator, Data Architect). Use the pick list for options. |  | **Yes** |
| Role type MS BPC | MSBPC.roletype | string | Details | Responsibilities | Functional \| Governance \| Technical | Choose the type of role involved (e.g., Functional, Technical, Executive). Use the pick list for options. |  | **Yes** |
| Scope MS BPC | MSBPC.scope | string | Details | Scoping | 10 - Unspecified \| 20 - In scope \| 30 - Out of scope \| 40 - Not applicable | Define the scope of the work item (e.g., In scope, Out of scope). Use the pick list for boundaries and expectations. | **Yes** | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Authorized for deployment MS BPC | MSBPC.authorizedfordeployment | string | Information | Application lifecycle | Partner defined \| DEV \| TEST \| PROD | Indicate the environment/branch that is authorized next for the code or data attached to this deliverable. |  | **Yes** |
| Current highest deployment MS BPC | MSBPC.currenthighestdeployment | string | Information | Application lifecycle | Partner defined \| DEV \| TEST \| PROD | Indicate what the current highest environment/branch is for the code or data attached to this deliverable. |  | **Yes** |
| Development technology MS BPC | MSBPC.developmenttechnology | string | Information | Enhancement details | Azure Data Bricks \| Azure Data Factory \| Azure Functions \| Azure Logic Apps \| Business Events \| C# \| Canvas App \| Commerce SDK \| Copilot Studio \| Java Script \| Model Driven App \| Plug-in \| Power Pages \| React/Bootstrap \| X++ | Pick the technology(ies) that will be employed to solve the needs of the enhancement. |  | **Yes** |
| Functional design MS BPC | MSBPC.functionaldesign | html | Information | Functional design | N/A | Provide the functional design details (content or hyperlink) for how the solution will meet the business needs. |  | **Yes** |
| Technical design MS BPC | MSBPC.technicaldesign | html | Information | Technical design | N/A | Provide the technical design details (content or hyperlink) for how the solution will meet be completed technically. |  | **Yes** |
| Menu item name MS BPC | MSBPC.menuitemname | string | References | Application details | N/A | Enter the name of the menu item in the application. Use this to identify navigation points. |  | **Yes** |
| Menu path MS BPC | MSBPC.menupath | string | References | Application details | N/A | Enter the menu path for accessing the relevant feature or process. |  | **Yes** |
| Module MS BPC | MSBPC.module | string | References | Application details | Accounts payable \| Accounts receivable \| App settings \| Asset leasing \| Asset management \| Audit workbench \| Benefits management \| Budgeting \| Business Performance Analytics \| Business Performance Planning \| Cash and bank management \| Common \| Consolidations \| Cost accounting \| Cost management \| Credit and collections \| Demand planning \| Engineering change management \| Expense management \| Fiscal books \| Fixed assets \| General ledger \| Human resources \| Inventory \| Inventory management \| Landed cost \| Leave and absence \| Master planning \| Material handling equipment interface \| Organization administration \| Payroll \| Personal settings \| Pricing management \| Procurement and sourcing \| Product information management \| Production control \| Project management and accounting \| Projects \| Questionnaire \| Rebate management \| Resources \| Retail \| Sales \| Sales and marketing \| Sales insights settings \| Scheduling \| Service \| Service management \| Settings \| Subscription billing \| System administration \| Systems settings \| Tax \| Time and attendance \| Transportation management \| Warehouse management | Select the Dynamics 365 module related to this work item (e.g., Accounts payable, Inventory management). Use the pick list for options. |  | **Yes** |
| Application family MS BPC | MSBPC.applicationfamily | string | References | Application information | Azure \| Business Central \| Cross Functional \| Customer Engagement \| Finance and Operations \| Productivity \| Power Platform | Select the application family (e.g., Business Central, Finance and Operations) relevant to this work item. This helps categorize the process. |  | **Yes** |
| Products MS BPC | MSBPC.products | string | References | Application information | Azure \| Business Central \| Commerce \| Contact Center \| Copilot Studio \| Customer Insights Data \| Customer Insights Journey \| Customer Service \| Customer Voice \| Field Service \| Finance \| Fraud Protection \| Guides \| Human Resources \| Microsoft 365 \| Other \| Power Apps \| Power Automate \| Power BI \| Power Pages \| Project \| Project Operations \| Remote Assist \| Sales \| Sales Copilot \| SharePoint \| Supply Chain Management \| Teams \| Customer Insights \| Microsoft Cloud for Sustainability | Select the relevant products (e.g., Business Central, Finance and Operations) associated with this work item. Use the pick list for options. |  | **Yes** |
| Software development company MS BPC | MSBPC.softwaredevelopmentcompany | string | References | Application information | N/A | Enter the name of the Software development company |  | **Yes** |
| Software solutions MS BPC | MSBPC.softwaresolutions | string | References | Application information | N/A | Enter the name(s) of the Software soluionts |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Industries MS BPC | MSBPC.industries | string | References | Industry focus | Agriculture (01-09) \| Construction (15-17) \| Finance, Insurance, Real Estate (60-67) \| Manufacturing (20-39) \| Mining (10-14) \| Public Administration (90-99) \| Retail Trade (52-59) \| Services (70-89) \| Transportation and Public Utilities (40-49) \| Wholesales Trade (50-51) | Select the industry or industries relevant to this work item (e.g., Manufacturing, Retail). Use the pick list for options. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Environment
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Environment`

A deliverable that tracks any type of item needed by IT Infrastructure such as hardware, network, security, etc.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Acceptance Criteria | Microsoft.VSTS.Common.AcceptanceCriteria | html | Details | Acceptance criteria | N/A |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Baseline complexity MS BPC | MSBPC.baselinecomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the baseline complexity (e.g., Simple, Medium, Complex) for this process. This value indicates the baseline suggested complexity for estimating the project effort related to the work product. |  | **Yes** |
| Estimated project impact MS BPC | MSBPC.estimatedprojectimpact | string | Details | Planning details | Critical \| High \| Low \| Medium | Select the estimated impact (e.g., Low, Medium, High) this work item will have on the project. Use the pick list to indicate significance. |  | **Yes** |
| Story Points | Microsoft.VSTS.Scheduling.StoryPoints | double | Details | Planning details | N/A |  |  | **Yes** |
| Scope MS BPC | MSBPC.scope | string | Details | Scoping | 10 - Unspecified \| 20 - In scope \| 30 - Out of scope \| 40 - Not applicable | Define the scope of the work item (e.g., In scope, Out of scope). Use the pick list for boundaries and expectations. | **Yes** | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Epic *(disabled)*
- **Enabled:** No
- **Class:** Derived
- **Reference name:** `MSBPCTemplate.Epic`

Not used

### States
- Proposed
  - New
- InProgress
  - Active
  - Resolved
- Completed
  - Closed
- Removed
  - Removed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Resolved]
D[Closed]
E[Removed]
A --> B
B --> C
C --> D
D --> E
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Value Area | Microsoft.VSTS.Common.ValueArea | string | Details | Classification | N/A | Business = Customer-facing epics; Architectural = Technology initiatives to support current and future business needs |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Business Value | Microsoft.VSTS.Common.BusinessValue | integer | Details | Planning | N/A | The business value for the customer when the epic is released |  | **Yes** |
| Effort | Microsoft.VSTS.Scheduling.Effort | double | Details | Planning | N/A | The estimated effort to implemented the epic |  | **Yes** |
| Priority | Microsoft.VSTS.Common.Priority | integer | Details | Planning | N/A |  |  | **Yes** |
| Risk | Microsoft.VSTS.Common.Risk | string | Details | Planning | N/A | Uncertainty in epic |  | **Yes** |
| Start Date | Microsoft.VSTS.Scheduling.StartDate | dateTime | Details | Planning | N/A | The date to start the task |  | **Yes** |
| Target Date | Microsoft.VSTS.Scheduling.TargetDate | dateTime | Details | Planning | N/A | The target date for completing the epic |  | **Yes** |
| Time Criticality | Microsoft.VSTS.Common.TimeCriticality | double | Details | Planning | N/A | How does the business value decay over time. Higher values make the epic more time critical |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Feature *(disabled)*
- **Enabled:** No
- **Class:** Derived
- **Reference name:** `MSBPCTemplate.Feature`

Not used

### States
- Proposed
  - New
- InProgress
  - Active
  - Resolved
- Completed
  - Closed
- Removed
  - Removed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Resolved]
D[Closed]
E[Removed]
A --> B
B --> C
C --> D
D --> E
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Value Area | Microsoft.VSTS.Common.ValueArea | string | Details | Classification | N/A | Business = Customer-facing epics; Architectural = Technology initiatives to support current and future business needs |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Business Value | Microsoft.VSTS.Common.BusinessValue | integer | Details | Planning | N/A | The business value for the customer when the epic is released |  | **Yes** |
| Effort | Microsoft.VSTS.Scheduling.Effort | double | Details | Planning | N/A | The estimated effort to implemented the epic |  | **Yes** |
| Priority | Microsoft.VSTS.Common.Priority | integer | Details | Planning | N/A |  |  | **Yes** |
| Risk | Microsoft.VSTS.Common.Risk | string | Details | Planning | N/A | Uncertainty in epic |  | **Yes** |
| Start Date | Microsoft.VSTS.Scheduling.StartDate | dateTime | Details | Planning | N/A | The date to start the task |  | **Yes** |
| Target Date | Microsoft.VSTS.Scheduling.TargetDate | dateTime | Details | Planning | N/A | The target date for completing the epic |  | **Yes** |
| Time Criticality | Microsoft.VSTS.Common.TimeCriticality | double | Details | Planning | N/A | How does the business value decay over time. Higher values make the epic more time critical |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Folder
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Folder`

The folder work item type simply allows for various levels of folders or groupings to organize large lists of work items into logical groupings.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Functional area
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Functionalarea`

Groupings of Scenarios by the Functional Area or Department that will perform these Processes. Examples are Accounts Payable, Sales, Inventory Management, etc.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Business process owner MS BPC | MSBPC.businessprocessowner | string, Identity | Details | Business assignments | N/A | Enter the name or role of the business process owner. Assign accountability for process management. |  | **Yes** |
| Subject matter expert MS BPC | MSBPC.subjectmatterexpert | string, Identity | Details | Business assignments | N/A | Enter the name or role of the subject matter expert for this work item. Identify who can provide guidance. |  | **Yes** |
| Workstream lead MS BPC | MSBPC.workstreamlead | string, Identity | Details | Business assignments | N/A | Enter the name or role of the workstream lead. Assign who will oversee and drive the team to produce the deliverables. |  | **Yes** |
| Start Date | Microsoft.VSTS.Scheduling.StartDate | dateTime | Details | Dates | N/A | The date to start the task |  | **Yes** |
| Target Date | Microsoft.VSTS.Scheduling.TargetDate | dateTime | Details | Dates | N/A | The target date for completing the epic |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Baseline complexity MS BPC | MSBPC.baselinecomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the baseline complexity (e.g., Simple, Medium, Complex) for this process. This value indicates the baseline suggested complexity for estimating the project effort related to the work product. |  | **Yes** |
| Estimated complexity MS BPC | MSBPC.estimatedcomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the estimated complexity (e.g., Small, Medium, Large) for this work item. Use the pick list to indicate project impact. |  | **Yes** |
| Estimated project impact MS BPC | MSBPC.estimatedprojectimpact | string | Details | Planning details | Critical \| High \| Low \| Medium | Select the estimated impact (e.g., Low, Medium, High) this work item will have on the project. Use the pick list to indicate significance. |  | **Yes** |
| Story Points | Microsoft.VSTS.Scheduling.StoryPoints | double | Details | Planning details | N/A |  |  | **Yes** |
| Priority | Microsoft.VSTS.Common.Priority | integer | Details | Priority | N/A |  |  | **Yes** |
| Scope approach MS BPC | MSBPC.scopeapproach | html | Details | Solution information | N/A | Provide a brief write up as to the approach for the expected solution will be solved for. |  | **Yes** |
| Workstream MS BPC | MSBPC.workstream | string | Details | Workstream | Partner defined | Assign the Workstream that the Functional Area is being assigned to for each consecutive workstream of the project. |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Infrastructure
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Infrastructure`

A deliverable that tracks any type of item needed by IT Infrastructure such as hardware, network, security, etc.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Acceptance Criteria | Microsoft.VSTS.Common.AcceptanceCriteria | html | Details | Acceptance criteria | N/A |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Baseline complexity MS BPC | MSBPC.baselinecomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the baseline complexity (e.g., Simple, Medium, Complex) for this process. This value indicates the baseline suggested complexity for estimating the project effort related to the work product. |  | **Yes** |
| Estimated complexity MS BPC | MSBPC.estimatedcomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the estimated complexity (e.g., Small, Medium, Large) for this work item. Use the pick list to indicate project impact. |  | **Yes** |
| Estimated project impact MS BPC | MSBPC.estimatedprojectimpact | string | Details | Planning details | Critical \| High \| Low \| Medium | Select the estimated impact (e.g., Low, Medium, High) this work item will have on the project. Use the pick list to indicate significance. |  | **Yes** |
| Story Points | Microsoft.VSTS.Scheduling.StoryPoints | double | Details | Planning details | N/A |  |  | **Yes** |
| Contributor MS BPC | MSBPC.contributor | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the contributor(s) for this work item. Use the pick list to assign roles or individuals. |  | **Yes** |
| Program areas MS BPC | MSBPC.programareas | string | Details | Responsibilities | Business Process Management \| Data Management & Governance \| Executive Leadership \| Infrastructure Management \| Integrations & Interfaces \| Organizational Change Management \| Project Management & Governance \| Reporting & Business Analytics \| Security Management \| Solution Architecture \| Solution Development \| Solution Testing \| Training \| Usability & Experience \| Workflow Management | Choose the program area (e.g., Reporting & Business Analytics, Solution Architecture) that best fits this work item. |  | **Yes** |
| Responsible party MS BPC | MSBPC.responsibleparty | string | Details | Responsibilities | Customer \| Partner | Indicate the party responsible for this work item (e.g., Business Process Owner, Project Manager). |  | **Yes** |
| Responsible role MS BPC | MSBPC.responsiblerole | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the role responsible for this work item (e.g., Application Administrator, Data Architect). Use the pick list for options. |  | **Yes** |
| Role type MS BPC | MSBPC.roletype | string | Details | Responsibilities | Functional \| Governance \| Technical | Choose the type of role involved (e.g., Functional, Technical, Executive). Use the pick list for options. |  | **Yes** |
| Scope MS BPC | MSBPC.scope | string | Details | Scoping | 10 - Unspecified \| 20 - In scope \| 30 - Out of scope \| 40 - Not applicable | Define the scope of the work item (e.g., In scope, Out of scope). Use the pick list for boundaries and expectations. | **Yes** | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Integration
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Integration`

A deliverable between two or more systems for a given process to function as desired.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Acceptance Criteria | Microsoft.VSTS.Common.AcceptanceCriteria | html | Details | Acceptance criteria | N/A |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Baseline complexity MS BPC | MSBPC.baselinecomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the baseline complexity (e.g., Simple, Medium, Complex) for this process. This value indicates the baseline suggested complexity for estimating the project effort related to the work product. |  | **Yes** |
| Estimated complexity MS BPC | MSBPC.estimatedcomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the estimated complexity (e.g., Small, Medium, Large) for this work item. Use the pick list to indicate project impact. |  | **Yes** |
| Estimated project impact MS BPC | MSBPC.estimatedprojectimpact | string | Details | Planning details | Critical \| High \| Low \| Medium | Select the estimated impact (e.g., Low, Medium, High) this work item will have on the project. Use the pick list to indicate significance. |  | **Yes** |
| Story Points | Microsoft.VSTS.Scheduling.StoryPoints | double | Details | Planning details | N/A |  |  | **Yes** |
| Contributor MS BPC | MSBPC.contributor | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the contributor(s) for this work item. Use the pick list to assign roles or individuals. |  | **Yes** |
| Program areas MS BPC | MSBPC.programareas | string | Details | Responsibilities | Business Process Management \| Data Management & Governance \| Executive Leadership \| Infrastructure Management \| Integrations & Interfaces \| Organizational Change Management \| Project Management & Governance \| Reporting & Business Analytics \| Security Management \| Solution Architecture \| Solution Development \| Solution Testing \| Training \| Usability & Experience \| Workflow Management | Choose the program area (e.g., Reporting & Business Analytics, Solution Architecture) that best fits this work item. |  | **Yes** |
| Responsible party MS BPC | MSBPC.responsibleparty | string | Details | Responsibilities | Customer \| Partner | Indicate the party responsible for this work item (e.g., Business Process Owner, Project Manager). |  | **Yes** |
| Responsible role MS BPC | MSBPC.responsiblerole | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the role responsible for this work item (e.g., Application Administrator, Data Architect). Use the pick list for options. |  | **Yes** |
| Role type MS BPC | MSBPC.roletype | string | Details | Responsibilities | Functional \| Governance \| Technical | Choose the type of role involved (e.g., Functional, Technical, Executive). Use the pick list for options. |  | **Yes** |
| Scope MS BPC | MSBPC.scope | string | Details | Scoping | 10 - Unspecified \| 20 - In scope \| 30 - Out of scope \| 40 - Not applicable | Define the scope of the work item (e.g., In scope, Out of scope). Use the pick list for boundaries and expectations. | **Yes** | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Authorized for deployment MS BPC | MSBPC.authorizedfordeployment | string | Information | Application lifecycle | Partner defined \| DEV \| TEST \| PROD | Indicate the environment/branch that is authorized next for the code or data attached to this deliverable. |  | **Yes** |
| Current highest deployment MS BPC | MSBPC.currenthighestdeployment | string | Information | Application lifecycle | Partner defined \| DEV \| TEST \| PROD | Indicate what the current highest environment/branch is for the code or data attached to this deliverable. |  | **Yes** |
| Data cleansing strategy MS BPC | MSBPC.datacleansingstrategy | html | Information | Data cleansing strategy | N/A | Provide a summary for how data is expected to be cleansed for the project prior to being migrated or integrated with. |  | **Yes** |
| Source data entity MS BPC | MSBPC.sourcedataentity | string | Information | Entity details | N/A | Enter the name of the source data entity for migration or integration. Track where data originates. |  | **Yes** |
| Source system MS BPC | MSBPC.sourcesystem | string | Information | Entity details | N/A | Specify the source system for migration or integration (e.g., Business Central, Finance and Operations). |  | **Yes** |
| Target data entity MS BPC | MSBPC.targetdataentity | string | Information | Entity details | N/A | Enter the target data entity in Finance and Operations for migration or integration. |  | **Yes** |
| Target system MS BPC | MSBPC.targetsystem | string | Information | Entity details | N/A | Specify the target system for migration or integration (e.g., Business Central, Finance and Operations). |  | **Yes** |
| Functional design MS BPC | MSBPC.functionaldesign | html | Information | Functional design | N/A | Provide the functional design details (content or hyperlink) for how the solution will meet the business needs. |  | **Yes** |
| Average daily volume MS BPC | MSBPC.averagedailyvolume | integer | Information | Integration details | N/A | Enter the expected average daily transaction volume. Use this for capacity and performance planning. |  | **Yes** |
| Average hourly transactions MS BPC | MSBPC.averagehourlytransactions | integer | Information | Integration details | N/A | Enter the expected average number of transactions per hour. Helps with system sizing and monitoring as well as selecting the correct technology for the integration or data migration. |  | **Yes** |
| Initial data sync mechanism MS BPC | MSBPC.initialdatasyncmechanism | string | Information | Integration details | Full Load \| Incremental Load \| Delta Load \| Bulk Import \| Real-Time Sync \| Manual Upload \| Staged Migration \| Dual Write Initial Sync \| Dual Write Incremental Sync \| Dual Write Full Refresh | Specify the mechanism used for initial data synchronization (e.g., Batch, Real-time). |  | **Yes** |
| Interface mode MS BPC | MSBPC.interfacemode | string | Information | Integration details | Batch (one-time) \| Event driven \| Hybrid \| Manual trigger \| Near real-time (Asynchronous) \| Real-time (Synchronous) \| Recurring batch | Select the mode of interface (e.g., Real-time, Batch). Use the pick list for options. |  | **Yes** |
| Interface model MS BPC | MSBPC.interfacemodel | string | Information | Integration details | Point-to-Point \| Hub-and-Spoke \| API-Based \| File-Based \| Message Queue \| Event-Driven \| Hybrid \| Dual Write-Standard \| Dual Write-Custom \| Dual Write-Hybrid | Enter the model used for the interface (e.g., API, File-based). |  | **Yes** |
| Interface technology MS BPC | MSBPC.interfacetechnology | string | Information | Integration details | Logic App \| Power Automate \| 3rd Party | Specify the technology used for the interface (e.g., Power Automate, Azure Logic App). |  | **Yes** |
| Middleware MS BPC | MSBPC.middleware | string | Information | Integration details | N/A | Specify the middleware technology used for integrations (e.g., Azure Logic App, Dataverse). |  | **Yes** |
| Peak hour volume MS BPC | MSBPC.peakhourvolume | integer | Information | Integration details | N/A | Enter the expected transaction volume during peak hours. Use this for system capacity planning. |  | **Yes** |
| Transformation technology MS BPC | MSBPC.transformationtechnology | string | Information | Integration details | N/A | Enter the technology used for data transformation (e.g., Azure Data Factory, Custom ETL tool). |  | **Yes** |
| Validation method MS BPC | MSBPC.validationmethod | string | Information | Integration details | Audit trail review \| Automated reconciliation \| Business user sign-off \| Checksum validation \| Manual spot check \| Record counts \| Test case execution | Select the method used to validate data or processes (e.g., Audit trail review, Checksum validation). Use the pick list for options. |  | **Yes** |
| Technical design MS BPC | MSBPC.technicaldesign | html | Information | Technical design | N/A | Provide the technical design details (content or hyperlink) for how the solution will meet be completed technically. |  | **Yes** |
| Menu item name MS BPC | MSBPC.menuitemname | string | References | Application details | N/A | Enter the name of the menu item in the application. Use this to identify navigation points. |  | **Yes** |
| Menu path MS BPC | MSBPC.menupath | string | References | Application details | N/A | Enter the menu path for accessing the relevant feature or process. |  | **Yes** |
| Module MS BPC | MSBPC.module | string | References | Application details | Accounts payable \| Accounts receivable \| App settings \| Asset leasing \| Asset management \| Audit workbench \| Benefits management \| Budgeting \| Business Performance Analytics \| Business Performance Planning \| Cash and bank management \| Common \| Consolidations \| Cost accounting \| Cost management \| Credit and collections \| Demand planning \| Engineering change management \| Expense management \| Fiscal books \| Fixed assets \| General ledger \| Human resources \| Inventory \| Inventory management \| Landed cost \| Leave and absence \| Master planning \| Material handling equipment interface \| Organization administration \| Payroll \| Personal settings \| Pricing management \| Procurement and sourcing \| Product information management \| Production control \| Project management and accounting \| Projects \| Questionnaire \| Rebate management \| Resources \| Retail \| Sales \| Sales and marketing \| Sales insights settings \| Scheduling \| Service \| Service management \| Settings \| Subscription billing \| System administration \| Systems settings \| Tax \| Time and attendance \| Transportation management \| Warehouse management | Select the Dynamics 365 module related to this work item (e.g., Accounts payable, Inventory management). Use the pick list for options. |  | **Yes** |
| Application family MS BPC | MSBPC.applicationfamily | string | References | Application information | Azure \| Business Central \| Cross Functional \| Customer Engagement \| Finance and Operations \| Productivity \| Power Platform | Select the application family (e.g., Business Central, Finance and Operations) relevant to this work item. This helps categorize the process. |  | **Yes** |
| Products MS BPC | MSBPC.products | string | References | Application information | Azure \| Business Central \| Commerce \| Contact Center \| Copilot Studio \| Customer Insights Data \| Customer Insights Journey \| Customer Service \| Customer Voice \| Field Service \| Finance \| Fraud Protection \| Guides \| Human Resources \| Microsoft 365 \| Other \| Power Apps \| Power Automate \| Power BI \| Power Pages \| Project \| Project Operations \| Remote Assist \| Sales \| Sales Copilot \| SharePoint \| Supply Chain Management \| Teams \| Customer Insights \| Microsoft Cloud for Sustainability | Select the relevant products (e.g., Business Central, Finance and Operations) associated with this work item. Use the pick list for options. |  | **Yes** |
| Software development company MS BPC | MSBPC.softwaredevelopmentcompany | string | References | Application information | N/A | Enter the name of the Software development company |  | **Yes** |
| Software solutions MS BPC | MSBPC.softwaresolutions | string | References | Application information | N/A | Enter the name(s) of the Software soluionts |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Industries MS BPC | MSBPC.industries | string | References | Industry focus | Agriculture (01-09) \| Construction (15-17) \| Finance, Insurance, Real Estate (60-67) \| Manufacturing (20-39) \| Mining (10-14) \| Public Administration (90-99) \| Retail Trade (52-59) \| Services (70-89) \| Transportation and Public Utilities (40-49) \| Wholesales Trade (50-51) | Select the industry or industries relevant to this work item (e.g., Manufacturing, Retail). Use the pick list for options. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Issue
- **Enabled:** Yes
- **Class:** Derived
- **Reference name:** `MSBPCTemplate.Issue`

An Issue is something that has occurred that may impact the project. A "Risk" is something that could happen. An "Issue" is something that has happened.

### States
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[Active]
B[Closed]
A --> B
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Target Date | Microsoft.VSTS.Scheduling.TargetDate | dateTime | Details | Dates | N/A | The target date for completing the epic |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Issue | Microsoft.VSTS.Common.Issue | string | Details | Issue details | N/A |  |  | **Yes** |
| Reported by MS BPC | MSBPC.reportedby | string, Identity | Details | Issue details | N/A | Capture the individual who reported the issue. |  | **Yes** |
| Resolution | Microsoft.VSTS.Common.Resolution | html | Details | Issue information | N/A |  |  | **Yes** |
| Due Date | Microsoft.VSTS.Scheduling.DueDate | dateTime | Details | Planning | N/A | The date by which this issue needs to be closed |  | **Yes** |
| Priority | Microsoft.VSTS.Common.Priority | integer | Details | Planning | N/A |  |  | **Yes** |
| Stack Rank | Microsoft.VSTS.Common.StackRank | double | Details | Planning | N/A |  |  | **Yes** |
| Postmortem MS BPC | MSBPC.postmortem | html | Details | Postmortem | N/A | Provide the subjective summary as to how well the objective was achieved in the sprint or program increment/tollgate. |  | **Yes** |
| Impact MS BPC | MSBPC.impact | html | Details | System info | N/A | Specify the perceived project impact this issue is causing. |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Job
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Job`

A deliverable that will be used to schedule routine background jobs to perform automated functions to update records for specific criteria. For example, automatically invoice all Sales Orders that have had products delivered for the current day.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Acceptance Criteria | Microsoft.VSTS.Common.AcceptanceCriteria | html | Details | Acceptance criteria | N/A |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Baseline complexity MS BPC | MSBPC.baselinecomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the baseline complexity (e.g., Simple, Medium, Complex) for this process. This value indicates the baseline suggested complexity for estimating the project effort related to the work product. |  | **Yes** |
| Estimated complexity MS BPC | MSBPC.estimatedcomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the estimated complexity (e.g., Small, Medium, Large) for this work item. Use the pick list to indicate project impact. |  | **Yes** |
| Estimated project impact MS BPC | MSBPC.estimatedprojectimpact | string | Details | Planning details | Critical \| High \| Low \| Medium | Select the estimated impact (e.g., Low, Medium, High) this work item will have on the project. Use the pick list to indicate significance. |  | **Yes** |
| Story Points | Microsoft.VSTS.Scheduling.StoryPoints | double | Details | Planning details | N/A |  |  | **Yes** |
| Contributor MS BPC | MSBPC.contributor | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the contributor(s) for this work item. Use the pick list to assign roles or individuals. |  | **Yes** |
| Program areas MS BPC | MSBPC.programareas | string | Details | Responsibilities | Business Process Management \| Data Management & Governance \| Executive Leadership \| Infrastructure Management \| Integrations & Interfaces \| Organizational Change Management \| Project Management & Governance \| Reporting & Business Analytics \| Security Management \| Solution Architecture \| Solution Development \| Solution Testing \| Training \| Usability & Experience \| Workflow Management | Choose the program area (e.g., Reporting & Business Analytics, Solution Architecture) that best fits this work item. |  | **Yes** |
| Responsible party MS BPC | MSBPC.responsibleparty | string | Details | Responsibilities | Customer \| Partner | Indicate the party responsible for this work item (e.g., Business Process Owner, Project Manager). |  | **Yes** |
| Responsible role MS BPC | MSBPC.responsiblerole | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the role responsible for this work item (e.g., Application Administrator, Data Architect). Use the pick list for options. |  | **Yes** |
| Role type MS BPC | MSBPC.roletype | string | Details | Responsibilities | Functional \| Governance \| Technical | Choose the type of role involved (e.g., Functional, Technical, Executive). Use the pick list for options. |  | **Yes** |
| Scope MS BPC | MSBPC.scope | string | Details | Scoping | 10 - Unspecified \| 20 - In scope \| 30 - Out of scope \| 40 - Not applicable | Define the scope of the work item (e.g., In scope, Out of scope). Use the pick list for boundaries and expectations. | **Yes** | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Authorized for deployment MS BPC | MSBPC.authorizedfordeployment | string | Information | Application lifecycle | Partner defined \| DEV \| TEST \| PROD | Indicate the environment/branch that is authorized next for the code or data attached to this deliverable. |  | **Yes** |
| Current highest deployment MS BPC | MSBPC.currenthighestdeployment | string | Information | Application lifecycle | Partner defined \| DEV \| TEST \| PROD | Indicate what the current highest environment/branch is for the code or data attached to this deliverable. |  | **Yes** |
| Configuration keys MS BPC | MSBPC.configurationkeys | string | Information | Configuration settings | N/A | Enter any configuration keys relevant to the application or module. Use this to manage feature access and settings. |  | **Yes** |
| Country region codes MS BPC | MSBPC.countryregioncodes | string | Information | Configuration settings | N/A | Enter applicable country or region codes. Use this to specify localization or compliance requirements. |  | **Yes** |
| Feature management keys MS BPC | MSBPC.featuremanagementkeys | string | Information | Configuration settings | N/A | Enter any feature management keys relevant to the application. Use this to control feature availability. |  | **Yes** |
| Functional design MS BPC | MSBPC.functionaldesign | html | Information | Functional design | N/A | Provide the functional design details (content or hyperlink) for how the solution will meet the business needs. |  | **Yes** |
| Execution frequency MS BPC | MSBPC.executionfrequency | string | Information | Job details | Ad hoc \| Annually \| Bi-weekly \| Daily \| Event-driven \| Hourly \| Monthly \| Other \| Quarterly \| Weekly | Select how often this job or report should be executed (e.g., Daily, Weekly, Monthly). Use the pick list for options. |  | **Yes** |
| Job execution type MS BPC | MSBPC.jobexecutiontype | string | Information | Job details | API triggered \| Event-driven \| Manual \| Scheduled | Select the type of job execution (e.g., Batch, Event-driven). Use the pick list for options. |  | **Yes** |
| Job purpose MS BPC | MSBPC.jobpurpose | string | Information | Job details | Archiving \| Cleanup \| Cutover or one-time \| Data processing \| Integration \| Monitoring \| Notification \| Reporting | Select the purpose of the job (e.g., Cleanup, Data processing). Use the pick list for options. |  | **Yes** |
| Job type MS BPC | MSBPC.jobtype | string | Information | Job details | Azure Data Factory Pipeline \| Azure Function \| Azure Logic App \| Batch (one-time) \| Custom \| Dataverse plugin \| Other \| Power Automate \| Recurring batch \| Third-party | Select the type of job (e.g., Custom job, Integration). Use the pick list for options. | **Yes** | **Yes** |
| At least one MS BPC | MSBPC.atleastone | boolean | Information | Toggles | Default: 0 | Indicate if at least one configuration or recommendation is required. Set to "Yes" if mandatory. | **Yes** | **Yes** |
| Can add later MS BPC | MSBPC.canaddlater | boolean | Information | Toggles | Default: 0 | Indicate if this configuration or field can be added later. Set to "Yes" if it’s not required at initial setup. | **Yes** | **Yes** |
| Can change later MS BPC | MSBPC.canchangelater | boolean | Information | Toggles | Default: 0 | Indicate if this configuration or field can be changed after initial setup. Set to "Yes" if changes are allowed. | **Yes** | **Yes** |
| Continuous MS BPC | MSBPC.continuous | boolean | Information | Toggles | Default: 0 | Indicate if this process or job is continuous. Set to "Yes" for ongoing or recurring activities. | **Yes** | **Yes** |
| Early MS BPC | MSBPC.early | boolean | Information | Toggles | Default: 0 | Indicate if this process or configuration should be completed early in the project lifecycle. Set to "Yes" if applicable. | **Yes** | **Yes** |
| Gold environment MS BPC | MSBPC.goldenvironment | boolean | Information | Toggles | Default: 0 | Indicates if this process or configuration should be completed in the Gold environment. Gold configs are copied to production during cutover. | **Yes** | **Yes** |
| Manadatory MS BPC | MSBPC.mandatory | boolean | Information | Toggles | Default: 0 | Indicate if this field or process is mandatory. Set to "Yes" if required for completion. | **Yes** | **Yes** |
| Multiple are recommended MS BPC | MSBPC.multiplearerecommended | boolean | Information | Toggles | Default: 0 | Indicate if multiple recommendations are suggested for this configuration. Set to "Yes" if more than one approach is recommended. | **Yes** | **Yes** |
| Menu item name MS BPC | MSBPC.menuitemname | string | References | Application details | N/A | Enter the name of the menu item in the application. Use this to identify navigation points. |  | **Yes** |
| Menu path MS BPC | MSBPC.menupath | string | References | Application details | N/A | Enter the menu path for accessing the relevant feature or process. |  | **Yes** |
| Module MS BPC | MSBPC.module | string | References | Application details | Accounts payable \| Accounts receivable \| App settings \| Asset leasing \| Asset management \| Audit workbench \| Benefits management \| Budgeting \| Business Performance Analytics \| Business Performance Planning \| Cash and bank management \| Common \| Consolidations \| Cost accounting \| Cost management \| Credit and collections \| Demand planning \| Engineering change management \| Expense management \| Fiscal books \| Fixed assets \| General ledger \| Human resources \| Inventory \| Inventory management \| Landed cost \| Leave and absence \| Master planning \| Material handling equipment interface \| Organization administration \| Payroll \| Personal settings \| Pricing management \| Procurement and sourcing \| Product information management \| Production control \| Project management and accounting \| Projects \| Questionnaire \| Rebate management \| Resources \| Retail \| Sales \| Sales and marketing \| Sales insights settings \| Scheduling \| Service \| Service management \| Settings \| Subscription billing \| System administration \| Systems settings \| Tax \| Time and attendance \| Transportation management \| Warehouse management | Select the Dynamics 365 module related to this work item (e.g., Accounts payable, Inventory management). Use the pick list for options. |  | **Yes** |
| Application family MS BPC | MSBPC.applicationfamily | string | References | Application information | Azure \| Business Central \| Cross Functional \| Customer Engagement \| Finance and Operations \| Productivity \| Power Platform | Select the application family (e.g., Business Central, Finance and Operations) relevant to this work item. This helps categorize the process. |  | **Yes** |
| Products MS BPC | MSBPC.products | string | References | Application information | Azure \| Business Central \| Commerce \| Contact Center \| Copilot Studio \| Customer Insights Data \| Customer Insights Journey \| Customer Service \| Customer Voice \| Field Service \| Finance \| Fraud Protection \| Guides \| Human Resources \| Microsoft 365 \| Other \| Power Apps \| Power Automate \| Power BI \| Power Pages \| Project \| Project Operations \| Remote Assist \| Sales \| Sales Copilot \| SharePoint \| Supply Chain Management \| Teams \| Customer Insights \| Microsoft Cloud for Sustainability | Select the relevant products (e.g., Business Central, Finance and Operations) associated with this work item. Use the pick list for options. |  | **Yes** |
| Software development company MS BPC | MSBPC.softwaredevelopmentcompany | string | References | Application information | N/A | Enter the name of the Software development company |  | **Yes** |
| Software solutions MS BPC | MSBPC.softwaresolutions | string | References | Application information | N/A | Enter the name(s) of the Software soluionts |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Industries MS BPC | MSBPC.industries | string | References | Industry focus | Agriculture (01-09) \| Construction (15-17) \| Finance, Insurance, Real Estate (60-67) \| Manufacturing (20-39) \| Mining (10-14) \| Public Administration (90-99) \| Retail Trade (52-59) \| Services (70-89) \| Transportation and Public Utilities (40-49) \| Wholesales Trade (50-51) | Select the industry or industries relevant to this work item (e.g., Manufacturing, Retail). Use the pick list for options. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Migration
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Migration`

A deliverable required to create or update data to provide the records within the system, this could be a migration from one system to another, mass update of existing data, or possibly a script to change existing data.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Acceptance Criteria | Microsoft.VSTS.Common.AcceptanceCriteria | html | Details | Acceptance criteria | N/A |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Baseline complexity MS BPC | MSBPC.baselinecomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the baseline complexity (e.g., Simple, Medium, Complex) for this process. This value indicates the baseline suggested complexity for estimating the project effort related to the work product. |  | **Yes** |
| Estimated complexity MS BPC | MSBPC.estimatedcomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the estimated complexity (e.g., Small, Medium, Large) for this work item. Use the pick list to indicate project impact. |  | **Yes** |
| Estimated project impact MS BPC | MSBPC.estimatedprojectimpact | string | Details | Planning details | Critical \| High \| Low \| Medium | Select the estimated impact (e.g., Low, Medium, High) this work item will have on the project. Use the pick list to indicate significance. |  | **Yes** |
| Story Points | Microsoft.VSTS.Scheduling.StoryPoints | double | Details | Planning details | N/A |  |  | **Yes** |
| Contributor MS BPC | MSBPC.contributor | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the contributor(s) for this work item. Use the pick list to assign roles or individuals. |  | **Yes** |
| Program areas MS BPC | MSBPC.programareas | string | Details | Responsibilities | Business Process Management \| Data Management & Governance \| Executive Leadership \| Infrastructure Management \| Integrations & Interfaces \| Organizational Change Management \| Project Management & Governance \| Reporting & Business Analytics \| Security Management \| Solution Architecture \| Solution Development \| Solution Testing \| Training \| Usability & Experience \| Workflow Management | Choose the program area (e.g., Reporting & Business Analytics, Solution Architecture) that best fits this work item. |  | **Yes** |
| Responsible party MS BPC | MSBPC.responsibleparty | string | Details | Responsibilities | Customer \| Partner | Indicate the party responsible for this work item (e.g., Business Process Owner, Project Manager). |  | **Yes** |
| Responsible role MS BPC | MSBPC.responsiblerole | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the role responsible for this work item (e.g., Application Administrator, Data Architect). Use the pick list for options. |  | **Yes** |
| Role type MS BPC | MSBPC.roletype | string | Details | Responsibilities | Functional \| Governance \| Technical | Choose the type of role involved (e.g., Functional, Technical, Executive). Use the pick list for options. |  | **Yes** |
| Scope MS BPC | MSBPC.scope | string | Details | Scoping | 10 - Unspecified \| 20 - In scope \| 30 - Out of scope \| 40 - Not applicable | Define the scope of the work item (e.g., In scope, Out of scope). Use the pick list for boundaries and expectations. | **Yes** | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Authorized for deployment MS BPC | MSBPC.authorizedfordeployment | string | Information | Application lifecycle | Partner defined \| DEV \| TEST \| PROD | Indicate the environment/branch that is authorized next for the code or data attached to this deliverable. |  | **Yes** |
| Current highest deployment MS BPC | MSBPC.currenthighestdeployment | string | Information | Application lifecycle | Partner defined \| DEV \| TEST \| PROD | Indicate what the current highest environment/branch is for the code or data attached to this deliverable. |  | **Yes** |
| Cutover method MS BPC | MSBPC.cutovermethod | string | Information | Configuration details | Manual configuration \| Data migration upload \| Copy gold database \| Database export/import \| Integration sync \| Initial data sync \| Continous sync \| Third-party tool migration \| AI-Generated configuration \| Unspecified | Pick from the list the manner in which the data will be populated for this configuration. | **Yes** | **Yes** |
| Data cleansing strategy MS BPC | MSBPC.datacleansingstrategy | html | Information | Data cleansing strategy | N/A | Provide a summary for how data is expected to be cleansed for the project prior to being migrated or integrated with. |  | **Yes** |
| Data package MS BPC | MSBPC.datapackage | string | Information | Entity details | N/A | Provide the name of the Data Package that this configuration will be added to in order to load into various environments. |  | **Yes** |
| Execution sequence MS BPC | MSBPC.executionsequence | integer | Information | Entity details | N/A | Enter the execution sequence number within the named Data Package for this process or job. Use this to define order of operations. |  | **Yes** |
| Source data entity MS BPC | MSBPC.sourcedataentity | string | Information | Entity details | N/A | Enter the name of the source data entity for migration or integration. Track where data originates. |  | **Yes** |
| Source system MS BPC | MSBPC.sourcesystem | string | Information | Entity details | N/A | Specify the source system for migration or integration (e.g., Business Central, Finance and Operations). |  | **Yes** |
| Target data entity MS BPC | MSBPC.targetdataentity | string | Information | Entity details | N/A | Enter the target data entity in Finance and Operations for migration or integration. |  | **Yes** |
| Target system MS BPC | MSBPC.targetsystem | string | Information | Entity details | N/A | Specify the target system for migration or integration (e.g., Business Central, Finance and Operations). |  | **Yes** |
| Functional design MS BPC | MSBPC.functionaldesign | html | Information | Functional design | N/A | Provide the functional design details (content or hyperlink) for how the solution will meet the business needs. |  | **Yes** |
| Interface mode MS BPC | MSBPC.interfacemode | string | Information | Integration details | Batch (one-time) \| Event driven \| Hybrid \| Manual trigger \| Near real-time (Asynchronous) \| Real-time (Synchronous) \| Recurring batch | Select the mode of interface (e.g., Real-time, Batch). Use the pick list for options. |  | **Yes** |
| Interface model MS BPC | MSBPC.interfacemodel | string | Information | Integration details | Point-to-Point \| Hub-and-Spoke \| API-Based \| File-Based \| Message Queue \| Event-Driven \| Hybrid \| Dual Write-Standard \| Dual Write-Custom \| Dual Write-Hybrid | Enter the model used for the interface (e.g., API, File-based). |  | **Yes** |
| Transformation technology MS BPC | MSBPC.transformationtechnology | string | Information | Integration details | N/A | Enter the technology used for data transformation (e.g., Azure Data Factory, Custom ETL tool). |  | **Yes** |
| Validation method MS BPC | MSBPC.validationmethod | string | Information | Integration details | Audit trail review \| Automated reconciliation \| Business user sign-off \| Checksum validation \| Manual spot check \| Record counts \| Test case execution | Select the method used to validate data or processes (e.g., Audit trail review, Checksum validation). Use the pick list for options. |  | **Yes** |
| Data type MS BPC | MSBPC.datatype | string | Information | Job details | Master data \| Setup data \| Transactional data | Select the type of data involved (e.g., Master data, Transactional data). Use the pick list for options. | **Yes** | **Yes** |
| Data migration volume MS BPC | MSBPC.datamigrationvolume | string | Information | Migration details | N/A | Enter the estimated volume of data to be migrated. Helps with planning and resource allocation. |  | **Yes** |
| Data scrubbing technology MS BPC | MSBPC.datascrubbingtechnology | string | Information | Migration details | N/A | Specify the technology used for data scrubbing (e.g., Azure Data Factory, Custom ETL tool). |  | **Yes** |
| Migration method MS BPC | MSBPC.migrationmethod | string | Information | Migration details | 3rd Party ETL tool \| API based \| Azure Data Factory \| Custom ETL tool \| Data import wizard \| Data management framework (DMF) \| Dual Write \| Excel Add-in \| Manual entry \| Other \| Power Query \| Script \| Stored Procedure | Select the technology or mechanism used to migrate data into the target system. |  | **Yes** |
| Technical design MS BPC | MSBPC.technicaldesign | html | Information | Technical design | N/A | Provide the technical design details (content or hyperlink) for how the solution will meet be completed technically. |  | **Yes** |
| Menu item name MS BPC | MSBPC.menuitemname | string | References | Application details | N/A | Enter the name of the menu item in the application. Use this to identify navigation points. |  | **Yes** |
| Menu path MS BPC | MSBPC.menupath | string | References | Application details | N/A | Enter the menu path for accessing the relevant feature or process. |  | **Yes** |
| Module MS BPC | MSBPC.module | string | References | Application details | Accounts payable \| Accounts receivable \| App settings \| Asset leasing \| Asset management \| Audit workbench \| Benefits management \| Budgeting \| Business Performance Analytics \| Business Performance Planning \| Cash and bank management \| Common \| Consolidations \| Cost accounting \| Cost management \| Credit and collections \| Demand planning \| Engineering change management \| Expense management \| Fiscal books \| Fixed assets \| General ledger \| Human resources \| Inventory \| Inventory management \| Landed cost \| Leave and absence \| Master planning \| Material handling equipment interface \| Organization administration \| Payroll \| Personal settings \| Pricing management \| Procurement and sourcing \| Product information management \| Production control \| Project management and accounting \| Projects \| Questionnaire \| Rebate management \| Resources \| Retail \| Sales \| Sales and marketing \| Sales insights settings \| Scheduling \| Service \| Service management \| Settings \| Subscription billing \| System administration \| Systems settings \| Tax \| Time and attendance \| Transportation management \| Warehouse management | Select the Dynamics 365 module related to this work item (e.g., Accounts payable, Inventory management). Use the pick list for options. |  | **Yes** |
| Application family MS BPC | MSBPC.applicationfamily | string | References | Application information | Azure \| Business Central \| Cross Functional \| Customer Engagement \| Finance and Operations \| Productivity \| Power Platform | Select the application family (e.g., Business Central, Finance and Operations) relevant to this work item. This helps categorize the process. |  | **Yes** |
| Products MS BPC | MSBPC.products | string | References | Application information | Azure \| Business Central \| Commerce \| Contact Center \| Copilot Studio \| Customer Insights Data \| Customer Insights Journey \| Customer Service \| Customer Voice \| Field Service \| Finance \| Fraud Protection \| Guides \| Human Resources \| Microsoft 365 \| Other \| Power Apps \| Power Automate \| Power BI \| Power Pages \| Project \| Project Operations \| Remote Assist \| Sales \| Sales Copilot \| SharePoint \| Supply Chain Management \| Teams \| Customer Insights \| Microsoft Cloud for Sustainability | Select the relevant products (e.g., Business Central, Finance and Operations) associated with this work item. Use the pick list for options. |  | **Yes** |
| Software development company MS BPC | MSBPC.softwaredevelopmentcompany | string | References | Application information | N/A | Enter the name of the Software development company |  | **Yes** |
| Software solutions MS BPC | MSBPC.softwaresolutions | string | References | Application information | N/A | Enter the name(s) of the Software soluionts |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Industries MS BPC | MSBPC.industries | string | References | Industry focus | Agriculture (01-09) \| Construction (15-17) \| Finance, Insurance, Real Estate (60-67) \| Manufacturing (20-39) \| Mining (10-14) \| Public Administration (90-99) \| Retail Trade (52-59) \| Services (70-89) \| Transportation and Public Utilities (40-49) \| Wholesales Trade (50-51) | Select the industry or industries relevant to this work item (e.g., Manufacturing, Retail). Use the pick list for options. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Objective
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Objective`

Objective targeted to be accomplished in a given Sprint or Program Increment/Tollgate

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Severity | Microsoft.VSTS.Common.Severity | string | Details | Bug details | Default: 3 - Medium |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Grade MS BPC | MSBPC.grade | string | Details | Objective details | A - Met all objectives \| B - Mostly complete \| C - Needs more work \| D - Needs significant work \| F - Failed to meet objectives | Provide the subjective grade as to how well the team did at achieving this objective in the given sprint or program increment/tollgate. | **Yes** | **Yes** |
| Objective type MS BPC | MSBPC.objectivetype | string | Details | Objective details | Executive \| Project \| Sprint \| Tollgate | Catalog the type of objective for this record. |  | **Yes** |
| Workstream MS BPC | MSBPC.workstream | string | Details | Workstream | Partner defined | Assign the Workstream that the Functional Area is being assigned to for each consecutive workstream of the project. |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Phase
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Phase`

Phases allow the partner to place their various phases into the Delivery Plan to provide an overview of when and how the project will be executed.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Start Date | Microsoft.VSTS.Scheduling.StartDate | dateTime | Details | Dates | N/A | The date to start the task |  | **Yes** |
| Target Date | Microsoft.VSTS.Scheduling.TargetDate | dateTime | Details | Dates | N/A | The target date for completing the epic |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Duration MS BPC | MSBPC.duration | string | Details | Duration | N/A | Estimate the number of weeks of duration for the phase. |  | **Yes** |
| Story Points | Microsoft.VSTS.Scheduling.StoryPoints | double | Details | Planning details | N/A |  |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Partner phase MS BPC | MSBPC.partnerphase | string | References | Methodology | Partner defined | Select the phase of the partner engagement. Map this to the Success by Design phases for consistency. |  | **Yes** |
| Success by Design phase MS BPC | MSBPC.successbydesignphase | string | References | Methodology | 10 - Strategize \| 20 - Initiate \| 31 - Implement - Analysis \| 32 - Implement - Design \| 33 - Implement - Development \| 34 - Implement - Test \| 45 - Prepare - Train \| 49 - Prepare - Cutover \| 50 - Operate | Select the Success by Design phase (e.g., Strategize, Implement, Test) relevant to this work item. Use the pick list for options. |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Process
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Process`

The third level node of the Business Process Catalog which are system agnostic.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Business process owner MS BPC | MSBPC.businessprocessowner | string, Identity | Details | Business assignments | N/A | Enter the name or role of the business process owner. Assign accountability for process management. |  | **Yes** |
| Subject matter expert MS BPC | MSBPC.subjectmatterexpert | string, Identity | Details | Business assignments | N/A | Enter the name or role of the subject matter expert for this work item. Identify who can provide guidance. |  | **Yes** |
| Workstream lead MS BPC | MSBPC.workstreamlead | string, Identity | Details | Business assignments | N/A | Enter the name or role of the workstream lead. Assign who will oversee and drive the team to produce the deliverables. |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Baseline complexity MS BPC | MSBPC.baselinecomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the baseline complexity (e.g., Simple, Medium, Complex) for this process. This value indicates the baseline suggested complexity for estimating the project effort related to the work product. |  | **Yes** |
| Process sequence ID MS BPC | MSBPC.processsequenceid | string | Details | Process IDs | N/A | Enter the unique sequence ID for the business process. Use this to organize and reference processes. | **Yes** | **Yes** |
| Scope MS BPC | MSBPC.scope | string | Details | Scoping | 10 - Unspecified \| 20 - In scope \| 30 - Out of scope \| 40 - Not applicable | Define the scope of the work item (e.g., In scope, Out of scope). Use the pick list for boundaries and expectations. | **Yes** | **Yes** |
| Fit gap status MS BPC | MSBPC.fitgapstatus | string | Details | Solution details | Fit \| Gap \| Unspecified | Select the fit-gap status (e.g., Fit, Gap) for this process. Use the pick list to indicate alignment with requirements. |  | **Yes** |
| Gap solution approach MS BPC | MSBPC.gapsolutionapproach | string | Details | Solution details | 10 - Unspecified \| 20 - Personalization \| 30 - Power Platform \| 40 - Java/Plug-in \| 50 - X++ Extension \| 60 - ISV \| 70 - ISV Extension | Select the approach for addressing gaps (e.g., Customization, Third-party solution). Use the pick list for options. |  | **Yes** |
| Scope approach MS BPC | MSBPC.scopeapproach | html | Details | Solution information | N/A | Provide a brief write up as to the approach for the expected solution will be solved for. |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Application family MS BPC | MSBPC.applicationfamily | string | References | Application information | Azure \| Business Central \| Cross Functional \| Customer Engagement \| Finance and Operations \| Productivity \| Power Platform | Select the application family (e.g., Business Central, Finance and Operations) relevant to this work item. This helps categorize the process. |  | **Yes** |
| Products MS BPC | MSBPC.products | string | References | Application information | Azure \| Business Central \| Commerce \| Contact Center \| Copilot Studio \| Customer Insights Data \| Customer Insights Journey \| Customer Service \| Customer Voice \| Field Service \| Finance \| Fraud Protection \| Guides \| Human Resources \| Microsoft 365 \| Other \| Power Apps \| Power Automate \| Power BI \| Power Pages \| Project \| Project Operations \| Remote Assist \| Sales \| Sales Copilot \| SharePoint \| Supply Chain Management \| Teams \| Customer Insights \| Microsoft Cloud for Sustainability | Select the relevant products (e.g., Business Central, Finance and Operations) associated with this work item. Use the pick list for options. |  | **Yes** |
| Software development company MS BPC | MSBPC.softwaredevelopmentcompany | string | References | Application information | N/A | Enter the name of the Software development company |  | **Yes** |
| Software solutions MS BPC | MSBPC.softwaresolutions | string | References | Application information | N/A | Enter the name(s) of the Software soluionts |  | **Yes** |
| APQC description MS BPC | MSBPC.apqcdescription | string | References | APQC references | N/A | Enter a brief description of the APQC process mapping. Required if APQC ID is provided. |  | **Yes** |
| APQC ID MS BPC | MSBPC.apqcid | string | References | APQC references | N/A | Enter the APQC ID for process mapping. Use this to align with industry-standard process frameworks. |  | **Yes** |
| Business process flow source MS BPC | MSBPC.businessprocessflowsource | string | References | Business process flow details | Microsoft \| Partner \| Customer | Select the organization that created or owns the business process flow. | **Yes** | **Yes** |
| Business process flow status MS BPC | MSBPC.businessprocessflowstatus | string | References | Business process flow details | 10 - Not started \| 20 - Drafted \| 30 - Published \| 40 - Updated \| 50 - Update required | Select the current status of the business process flow (e.g., Not started, In progress).This status indicates the status of the flow diagram from Microsoft being published in the Git Hub repository. | **Yes** | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Industries MS BPC | MSBPC.industries | string | References | Industry focus | Agriculture (01-09) \| Construction (15-17) \| Finance, Insurance, Real Estate (60-67) \| Manufacturing (20-39) \| Mining (10-14) \| Public Administration (90-99) \| Retail Trade (52-59) \| Services (70-89) \| Transportation and Public Utilities (40-49) \| Wholesales Trade (50-51) | Select the industry or industries relevant to this work item (e.g., Manufacturing, Retail). Use the pick list for options. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Alternate process sequence ID MS BPC | MSBPC.alternateprocesssequenceid | string | References | Process IDs | N/A | Enter the alternate sequence ID for deprecated or parallel processes. This value is required for any process that is deprecated and indicates the alternative process to use in place of the deprecated row. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Process area
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Processarea`

The second level nodes within the Business Process Catalog.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Process sequence ID MS BPC | MSBPC.processsequenceid | string | Details | Process IDs | N/A | Enter the unique sequence ID for the business process. Use this to organize and reference processes. | **Yes** | **Yes** |
| Scope MS BPC | MSBPC.scope | string | Details | Scoping | 10 - Unspecified \| 20 - In scope \| 30 - Out of scope \| 40 - Not applicable | Define the scope of the work item (e.g., In scope, Out of scope). Use the pick list for boundaries and expectations. | **Yes** | **Yes** |
| Scope approach MS BPC | MSBPC.scopeapproach | html | Details | Solution information | N/A | Provide a brief write up as to the approach for the expected solution will be solved for. |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Application family MS BPC | MSBPC.applicationfamily | string | References | Application information | Azure \| Business Central \| Cross Functional \| Customer Engagement \| Finance and Operations \| Productivity \| Power Platform | Select the application family (e.g., Business Central, Finance and Operations) relevant to this work item. This helps categorize the process. |  | **Yes** |
| Products MS BPC | MSBPC.products | string | References | Application information | Azure \| Business Central \| Commerce \| Contact Center \| Copilot Studio \| Customer Insights Data \| Customer Insights Journey \| Customer Service \| Customer Voice \| Field Service \| Finance \| Fraud Protection \| Guides \| Human Resources \| Microsoft 365 \| Other \| Power Apps \| Power Automate \| Power BI \| Power Pages \| Project \| Project Operations \| Remote Assist \| Sales \| Sales Copilot \| SharePoint \| Supply Chain Management \| Teams \| Customer Insights \| Microsoft Cloud for Sustainability | Select the relevant products (e.g., Business Central, Finance and Operations) associated with this work item. Use the pick list for options. |  | **Yes** |
| Software development company MS BPC | MSBPC.softwaredevelopmentcompany | string | References | Application information | N/A | Enter the name of the Software development company |  | **Yes** |
| Software solutions MS BPC | MSBPC.softwaresolutions | string | References | Application information | N/A | Enter the name(s) of the Software soluionts |  | **Yes** |
| APQC description MS BPC | MSBPC.apqcdescription | string | References | APQC references | N/A | Enter a brief description of the APQC process mapping. Required if APQC ID is provided. |  | **Yes** |
| APQC ID MS BPC | MSBPC.apqcid | string | References | APQC references | N/A | Enter the APQC ID for process mapping. Use this to align with industry-standard process frameworks. |  | **Yes** |
| Business process flow source MS BPC | MSBPC.businessprocessflowsource | string | References | Business process flow details | Microsoft \| Partner \| Customer | Select the organization that created or owns the business process flow. | **Yes** | **Yes** |
| Business process flow status MS BPC | MSBPC.businessprocessflowstatus | string | References | Business process flow details | 10 - Not started \| 20 - Drafted \| 30 - Published \| 40 - Updated \| 50 - Update required | Select the current status of the business process flow (e.g., Not started, In progress).This status indicates the status of the flow diagram from Microsoft being published in the Git Hub repository. | **Yes** | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Industries MS BPC | MSBPC.industries | string | References | Industry focus | Agriculture (01-09) \| Construction (15-17) \| Finance, Insurance, Real Estate (60-67) \| Manufacturing (20-39) \| Mining (10-14) \| Public Administration (90-99) \| Retail Trade (52-59) \| Services (70-89) \| Transportation and Public Utilities (40-49) \| Wholesales Trade (50-51) | Select the industry or industries relevant to this work item (e.g., Manufacturing, Retail). Use the pick list for options. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Alternate process sequence ID MS BPC | MSBPC.alternateprocesssequenceid | string | References | Process IDs | N/A | Enter the alternate sequence ID for deprecated or parallel processes. This value is required for any process that is deprecated and indicates the alternative process to use in place of the deprecated row. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Report
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Report`

A deliverable to create on enhance a Report, Dashboard or Analytic in order to allow a Process to function properly.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Acceptance Criteria | Microsoft.VSTS.Common.AcceptanceCriteria | html | Details | Acceptance criteria | N/A |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Baseline complexity MS BPC | MSBPC.baselinecomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the baseline complexity (e.g., Simple, Medium, Complex) for this process. This value indicates the baseline suggested complexity for estimating the project effort related to the work product. |  | **Yes** |
| Estimated complexity MS BPC | MSBPC.estimatedcomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the estimated complexity (e.g., Small, Medium, Large) for this work item. Use the pick list to indicate project impact. |  | **Yes** |
| Estimated project impact MS BPC | MSBPC.estimatedprojectimpact | string | Details | Planning details | Critical \| High \| Low \| Medium | Select the estimated impact (e.g., Low, Medium, High) this work item will have on the project. Use the pick list to indicate significance. |  | **Yes** |
| Story Points | Microsoft.VSTS.Scheduling.StoryPoints | double | Details | Planning details | N/A |  |  | **Yes** |
| Contributor MS BPC | MSBPC.contributor | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the contributor(s) for this work item. Use the pick list to assign roles or individuals. |  | **Yes** |
| Program areas MS BPC | MSBPC.programareas | string | Details | Responsibilities | Business Process Management \| Data Management & Governance \| Executive Leadership \| Infrastructure Management \| Integrations & Interfaces \| Organizational Change Management \| Project Management & Governance \| Reporting & Business Analytics \| Security Management \| Solution Architecture \| Solution Development \| Solution Testing \| Training \| Usability & Experience \| Workflow Management | Choose the program area (e.g., Reporting & Business Analytics, Solution Architecture) that best fits this work item. |  | **Yes** |
| Responsible party MS BPC | MSBPC.responsibleparty | string | Details | Responsibilities | Customer \| Partner | Indicate the party responsible for this work item (e.g., Business Process Owner, Project Manager). |  | **Yes** |
| Responsible role MS BPC | MSBPC.responsiblerole | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the role responsible for this work item (e.g., Application Administrator, Data Architect). Use the pick list for options. |  | **Yes** |
| Role type MS BPC | MSBPC.roletype | string | Details | Responsibilities | Functional \| Governance \| Technical | Choose the type of role involved (e.g., Functional, Technical, Executive). Use the pick list for options. |  | **Yes** |
| Scope MS BPC | MSBPC.scope | string | Details | Scoping | 10 - Unspecified \| 20 - In scope \| 30 - Out of scope \| 40 - Not applicable | Define the scope of the work item (e.g., In scope, Out of scope). Use the pick list for boundaries and expectations. | **Yes** | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Authorized for deployment MS BPC | MSBPC.authorizedfordeployment | string | Information | Application lifecycle | Partner defined \| DEV \| TEST \| PROD | Indicate the environment/branch that is authorized next for the code or data attached to this deliverable. |  | **Yes** |
| Current highest deployment MS BPC | MSBPC.currenthighestdeployment | string | Information | Application lifecycle | Partner defined \| DEV \| TEST \| PROD | Indicate what the current highest environment/branch is for the code or data attached to this deliverable. |  | **Yes** |
| Compliance requirement MS BPC | MSBPC.compliancerequirement | boolean | Information | Compliance requirement | Default: 0 | Indicate if there are compliance requirements for this work item. Set to "Yes" if regulatory or policy compliance is needed. | **Yes** | **Yes** |
| Configuration keys MS BPC | MSBPC.configurationkeys | string | Information | Configuration settings | N/A | Enter any configuration keys relevant to the application or module. Use this to manage feature access and settings. |  | **Yes** |
| Country region codes MS BPC | MSBPC.countryregioncodes | string | Information | Configuration settings | N/A | Enter applicable country or region codes. Use this to specify localization or compliance requirements. |  | **Yes** |
| Feature management keys MS BPC | MSBPC.featuremanagementkeys | string | Information | Configuration settings | N/A | Enter any feature management keys relevant to the application. Use this to control feature availability. |  | **Yes** |
| Functional design MS BPC | MSBPC.functionaldesign | html | Information | Functional design | N/A | Provide the functional design details (content or hyperlink) for how the solution will meet the business needs. |  | **Yes** |
| Job execution type MS BPC | MSBPC.jobexecutiontype | string | Information | Job details | API triggered \| Event-driven \| Manual \| Scheduled | Select the type of job execution (e.g., Batch, Event-driven). Use the pick list for options. |  | **Yes** |
| Report audience MS BPC | MSBPC.reportaudience | string | Information | Report details | Cross-functional \| External - Customer \| External - Vendor \| Internal - Executive \| Internal - Technical \| Internal - Operational \| Other \| Regulatory & Compliance | Specify the intended audience for the report (e.g., Internal Executive, External Customer). Use the pick list for options. |  | **Yes** |
| Report technology MS BPC | MSBPC.reporttechnology | string | Information | Report details | Business Performance Analytics (BPA) \| Custom Report \| Dataverse \| Electronic Reporting \| Excel Add-In \| Financial Reporter \| Power BI \| SSRS \| Third-party | Select the technology used to generate the report (e.g., Power BI, SSRS). Use the pick list for options. |  | **Yes** |
| Report type MS BPC | MSBPC.reporttype | string | Information | Report details | Analytical \| Audit \| Exception \| Financial \| Management \| Official document \| Operational \| Other \| Regulatory \| Transactional | Choose the type of report (e.g., Analytical, Audit, Financial). Use the pick list for options. |  | **Yes** |
| Technical design MS BPC | MSBPC.technicaldesign | html | Information | Technical design | N/A | Provide the technical design details (content or hyperlink) for how the solution will meet be completed technically. |  | **Yes** |
| At least one MS BPC | MSBPC.atleastone | boolean | Information | Toggles | Default: 0 | Indicate if at least one configuration or recommendation is required. Set to "Yes" if mandatory. | **Yes** | **Yes** |
| Can add later MS BPC | MSBPC.canaddlater | boolean | Information | Toggles | Default: 0 | Indicate if this configuration or field can be added later. Set to "Yes" if it’s not required at initial setup. | **Yes** | **Yes** |
| Can change later MS BPC | MSBPC.canchangelater | boolean | Information | Toggles | Default: 0 | Indicate if this configuration or field can be changed after initial setup. Set to "Yes" if changes are allowed. | **Yes** | **Yes** |
| Continuous MS BPC | MSBPC.continuous | boolean | Information | Toggles | Default: 0 | Indicate if this process or job is continuous. Set to "Yes" for ongoing or recurring activities. | **Yes** | **Yes** |
| Early MS BPC | MSBPC.early | boolean | Information | Toggles | Default: 0 | Indicate if this process or configuration should be completed early in the project lifecycle. Set to "Yes" if applicable. | **Yes** | **Yes** |
| Gold environment MS BPC | MSBPC.goldenvironment | boolean | Information | Toggles | Default: 0 | Indicates if this process or configuration should be completed in the Gold environment. Gold configs are copied to production during cutover. | **Yes** | **Yes** |
| Manadatory MS BPC | MSBPC.mandatory | boolean | Information | Toggles | Default: 0 | Indicate if this field or process is mandatory. Set to "Yes" if required for completion. | **Yes** | **Yes** |
| Multiple are recommended MS BPC | MSBPC.multiplearerecommended | boolean | Information | Toggles | Default: 0 | Indicate if multiple recommendations are suggested for this configuration. Set to "Yes" if more than one approach is recommended. | **Yes** | **Yes** |
| Menu item name MS BPC | MSBPC.menuitemname | string | References | Application details | N/A | Enter the name of the menu item in the application. Use this to identify navigation points. |  | **Yes** |
| Menu path MS BPC | MSBPC.menupath | string | References | Application details | N/A | Enter the menu path for accessing the relevant feature or process. |  | **Yes** |
| Module MS BPC | MSBPC.module | string | References | Application details | Accounts payable \| Accounts receivable \| App settings \| Asset leasing \| Asset management \| Audit workbench \| Benefits management \| Budgeting \| Business Performance Analytics \| Business Performance Planning \| Cash and bank management \| Common \| Consolidations \| Cost accounting \| Cost management \| Credit and collections \| Demand planning \| Engineering change management \| Expense management \| Fiscal books \| Fixed assets \| General ledger \| Human resources \| Inventory \| Inventory management \| Landed cost \| Leave and absence \| Master planning \| Material handling equipment interface \| Organization administration \| Payroll \| Personal settings \| Pricing management \| Procurement and sourcing \| Product information management \| Production control \| Project management and accounting \| Projects \| Questionnaire \| Rebate management \| Resources \| Retail \| Sales \| Sales and marketing \| Sales insights settings \| Scheduling \| Service \| Service management \| Settings \| Subscription billing \| System administration \| Systems settings \| Tax \| Time and attendance \| Transportation management \| Warehouse management | Select the Dynamics 365 module related to this work item (e.g., Accounts payable, Inventory management). Use the pick list for options. |  | **Yes** |
| Application family MS BPC | MSBPC.applicationfamily | string | References | Application information | Azure \| Business Central \| Cross Functional \| Customer Engagement \| Finance and Operations \| Productivity \| Power Platform | Select the application family (e.g., Business Central, Finance and Operations) relevant to this work item. This helps categorize the process. |  | **Yes** |
| Products MS BPC | MSBPC.products | string | References | Application information | Azure \| Business Central \| Commerce \| Contact Center \| Copilot Studio \| Customer Insights Data \| Customer Insights Journey \| Customer Service \| Customer Voice \| Field Service \| Finance \| Fraud Protection \| Guides \| Human Resources \| Microsoft 365 \| Other \| Power Apps \| Power Automate \| Power BI \| Power Pages \| Project \| Project Operations \| Remote Assist \| Sales \| Sales Copilot \| SharePoint \| Supply Chain Management \| Teams \| Customer Insights \| Microsoft Cloud for Sustainability | Select the relevant products (e.g., Business Central, Finance and Operations) associated with this work item. Use the pick list for options. |  | **Yes** |
| Software development company MS BPC | MSBPC.softwaredevelopmentcompany | string | References | Application information | N/A | Enter the name of the Software development company |  | **Yes** |
| Software solutions MS BPC | MSBPC.softwaresolutions | string | References | Application information | N/A | Enter the name(s) of the Software soluionts |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Industries MS BPC | MSBPC.industries | string | References | Industry focus | Agriculture (01-09) \| Construction (15-17) \| Finance, Insurance, Real Estate (60-67) \| Manufacturing (20-39) \| Mining (10-14) \| Public Administration (90-99) \| Retail Trade (52-59) \| Services (70-89) \| Transportation and Public Utilities (40-49) \| Wholesales Trade (50-51) | Select the industry or industries relevant to this work item (e.g., Manufacturing, Retail). Use the pick list for options. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Requirement
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Requirement`

A requirement gathered from the business communicating a detail about how the processes and/or system should function.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Acceptance Criteria | Microsoft.VSTS.Common.AcceptanceCriteria | html | Details | Acceptance criteria | N/A |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Priority | Microsoft.VSTS.Common.Priority | integer | Details | Priority | N/A |  |  | **Yes** |
| Requirement mapping MS BPC | MSBPC.requirementmapping | html | Details | Requirement information | N/A | Provide details as to how the requirement was solved by other deliverables that will be produced to tailor the system to meet the client's needs. |  | **Yes** |
| Fit gap status MS BPC | MSBPC.fitgapstatus | string | Details | Solution details | Fit \| Gap \| Unspecified | Select the fit-gap status (e.g., Fit, Gap) for this process. Use the pick list to indicate alignment with requirements. |  | **Yes** |
| Gap solution approach MS BPC | MSBPC.gapsolutionapproach | string | Details | Solution details | 10 - Unspecified \| 20 - Personalization \| 30 - Power Platform \| 40 - Java/Plug-in \| 50 - X++ Extension \| 60 - ISV \| 70 - ISV Extension | Select the approach for addressing gaps (e.g., Customization, Third-party solution). Use the pick list for options. |  | **Yes** |
| Scope approach MS BPC | MSBPC.scopeapproach | html | Details | Solution information | N/A | Provide a brief write up as to the approach for the expected solution will be solved for. |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Risk
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Risk`

The documentation of a known or perceived Risk that could negatively impact the project timeline, scope or budget with plans to mitigate them.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Contingency Plan | Microsoft.VSTS.CMMI.ContingencyPlan | html | Details | Contingency plan | N/A |  |  | **Yes** |
| Target Date | Microsoft.VSTS.Scheduling.TargetDate | dateTime | Details | Dates | N/A | The target date for completing the epic |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Priority | Microsoft.VSTS.Common.Priority | integer | Details | Priority | N/A |  |  | **Yes** |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity | Details | Risk details | N/A |  |  | **Yes** |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime | Details | Risk details | N/A |  |  | **Yes** |
| Created By | System.CreatedBy | string, Identity | Details | Risk details | N/A |  |  | **Yes** |
| Created Date | System.CreatedDate | dateTime | Details | Risk details | N/A |  |  | **Yes** |
| Probability | Microsoft.VSTS.CMMI.Probability | integer | Details | Risk details | N/A |  |  | **Yes** |
| Risk category MS BPC | MSBPC.riskcategory | string | Details | Risk details | External \| Functional \| Management \| Organizational \| Technical | General category in which risk will impact |  | **Yes** |
| Risk owner MS BPC | MSBPC.riskowner | string, Identity | Details | Risk details | N/A | Document the individual who owns the risk plan for this item. |  | **Yes** |
| Risk response MSBPC | MSBPC.riskresponse | string | Details | Risk details | Accept \| Avoid \| Mitigate \| Transfer | Activities to be taken to lower the probability and/or impact of a risk. |  | **Yes** |
| Risk impact assessment MS BPC | MSBPC.riskimpactassessment | html | Details | Risk impact assessment | N/A | Summarize the perceived risk impact being identified for this risk. |  | **Yes** |
| Triggers MS BPC | MSBPC.triggers | html | Details | Triggers | N/A | List any identified triggers that may cause this risk to be invoked. |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Scenario
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Scenario`

The fourth level node of the Business Process Catalog which now moves into how to perform each Scenario within a given application.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Business process owner MS BPC | MSBPC.businessprocessowner | string, Identity | Details | Business assignments | N/A | Enter the name or role of the business process owner. Assign accountability for process management. |  | **Yes** |
| Subject matter expert MS BPC | MSBPC.subjectmatterexpert | string, Identity | Details | Business assignments | N/A | Enter the name or role of the subject matter expert for this work item. Identify who can provide guidance. |  | **Yes** |
| Workstream lead MS BPC | MSBPC.workstreamlead | string, Identity | Details | Business assignments | N/A | Enter the name or role of the workstream lead. Assign who will oversee and drive the team to produce the deliverables. |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Baseline complexity MS BPC | MSBPC.baselinecomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the baseline complexity (e.g., Simple, Medium, Complex) for this process. This value indicates the baseline suggested complexity for estimating the project effort related to the work product. |  | **Yes** |
| Priority | Microsoft.VSTS.Common.Priority | integer | Details | Priority | N/A |  |  | **Yes** |
| Process sequence ID MS BPC | MSBPC.processsequenceid | string | Details | Process IDs | N/A | Enter the unique sequence ID for the business process. Use this to organize and reference processes. | **Yes** | **Yes** |
| Scope MS BPC | MSBPC.scope | string | Details | Scoping | 10 - Unspecified \| 20 - In scope \| 30 - Out of scope \| 40 - Not applicable | Define the scope of the work item (e.g., In scope, Out of scope). Use the pick list for boundaries and expectations. | **Yes** | **Yes** |
| Fit gap status MS BPC | MSBPC.fitgapstatus | string | Details | Solution details | Fit \| Gap \| Unspecified | Select the fit-gap status (e.g., Fit, Gap) for this process. Use the pick list to indicate alignment with requirements. |  | **Yes** |
| Gap solution approach MS BPC | MSBPC.gapsolutionapproach | string | Details | Solution details | 10 - Unspecified \| 20 - Personalization \| 30 - Power Platform \| 40 - Java/Plug-in \| 50 - X++ Extension \| 60 - ISV \| 70 - ISV Extension | Select the approach for addressing gaps (e.g., Customization, Third-party solution). Use the pick list for options. |  | **Yes** |
| Scope approach MS BPC | MSBPC.scopeapproach | html | Details | Solution information | N/A | Provide a brief write up as to the approach for the expected solution will be solved for. |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Menu item name MS BPC | MSBPC.menuitemname | string | References | Application details | N/A | Enter the name of the menu item in the application. Use this to identify navigation points. |  | **Yes** |
| Menu path MS BPC | MSBPC.menupath | string | References | Application details | N/A | Enter the menu path for accessing the relevant feature or process. |  | **Yes** |
| Module MS BPC | MSBPC.module | string | References | Application details | Accounts payable \| Accounts receivable \| App settings \| Asset leasing \| Asset management \| Audit workbench \| Benefits management \| Budgeting \| Business Performance Analytics \| Business Performance Planning \| Cash and bank management \| Common \| Consolidations \| Cost accounting \| Cost management \| Credit and collections \| Demand planning \| Engineering change management \| Expense management \| Fiscal books \| Fixed assets \| General ledger \| Human resources \| Inventory \| Inventory management \| Landed cost \| Leave and absence \| Master planning \| Material handling equipment interface \| Organization administration \| Payroll \| Personal settings \| Pricing management \| Procurement and sourcing \| Product information management \| Production control \| Project management and accounting \| Projects \| Questionnaire \| Rebate management \| Resources \| Retail \| Sales \| Sales and marketing \| Sales insights settings \| Scheduling \| Service \| Service management \| Settings \| Subscription billing \| System administration \| Systems settings \| Tax \| Time and attendance \| Transportation management \| Warehouse management | Select the Dynamics 365 module related to this work item (e.g., Accounts payable, Inventory management). Use the pick list for options. |  | **Yes** |
| Application family MS BPC | MSBPC.applicationfamily | string | References | Application information | Azure \| Business Central \| Cross Functional \| Customer Engagement \| Finance and Operations \| Productivity \| Power Platform | Select the application family (e.g., Business Central, Finance and Operations) relevant to this work item. This helps categorize the process. |  | **Yes** |
| Products MS BPC | MSBPC.products | string | References | Application information | Azure \| Business Central \| Commerce \| Contact Center \| Copilot Studio \| Customer Insights Data \| Customer Insights Journey \| Customer Service \| Customer Voice \| Field Service \| Finance \| Fraud Protection \| Guides \| Human Resources \| Microsoft 365 \| Other \| Power Apps \| Power Automate \| Power BI \| Power Pages \| Project \| Project Operations \| Remote Assist \| Sales \| Sales Copilot \| SharePoint \| Supply Chain Management \| Teams \| Customer Insights \| Microsoft Cloud for Sustainability | Select the relevant products (e.g., Business Central, Finance and Operations) associated with this work item. Use the pick list for options. |  | **Yes** |
| Software development company MS BPC | MSBPC.softwaredevelopmentcompany | string | References | Application information | N/A | Enter the name of the Software development company |  | **Yes** |
| Software solutions MS BPC | MSBPC.softwaresolutions | string | References | Application information | N/A | Enter the name(s) of the Software soluionts |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Industries MS BPC | MSBPC.industries | string | References | Industry focus | Agriculture (01-09) \| Construction (15-17) \| Finance, Insurance, Real Estate (60-67) \| Manufacturing (20-39) \| Mining (10-14) \| Public Administration (90-99) \| Retail Trade (52-59) \| Services (70-89) \| Transportation and Public Utilities (40-49) \| Wholesales Trade (50-51) | Select the industry or industries relevant to this work item (e.g., Manufacturing, Retail). Use the pick list for options. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Alternate process sequence ID MS BPC | MSBPC.alternateprocesssequenceid | string | References | Process IDs | N/A | Enter the alternate sequence ID for deprecated or parallel processes. This value is required for any process that is deprecated and indicates the alternative process to use in place of the deprecated row. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Security
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Security`

A deliverable required to build or configure the security objects in order to control which users are allowed to access or perform which processes.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Acceptance Criteria | Microsoft.VSTS.Common.AcceptanceCriteria | html | Details | Acceptance criteria | N/A |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Baseline complexity MS BPC | MSBPC.baselinecomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the baseline complexity (e.g., Simple, Medium, Complex) for this process. This value indicates the baseline suggested complexity for estimating the project effort related to the work product. |  | **Yes** |
| Estimated complexity MS BPC | MSBPC.estimatedcomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the estimated complexity (e.g., Small, Medium, Large) for this work item. Use the pick list to indicate project impact. |  | **Yes** |
| Estimated project impact MS BPC | MSBPC.estimatedprojectimpact | string | Details | Planning details | Critical \| High \| Low \| Medium | Select the estimated impact (e.g., Low, Medium, High) this work item will have on the project. Use the pick list to indicate significance. |  | **Yes** |
| Story Points | Microsoft.VSTS.Scheduling.StoryPoints | double | Details | Planning details | N/A |  |  | **Yes** |
| Contributor MS BPC | MSBPC.contributor | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the contributor(s) for this work item. Use the pick list to assign roles or individuals. |  | **Yes** |
| Program areas MS BPC | MSBPC.programareas | string | Details | Responsibilities | Business Process Management \| Data Management & Governance \| Executive Leadership \| Infrastructure Management \| Integrations & Interfaces \| Organizational Change Management \| Project Management & Governance \| Reporting & Business Analytics \| Security Management \| Solution Architecture \| Solution Development \| Solution Testing \| Training \| Usability & Experience \| Workflow Management | Choose the program area (e.g., Reporting & Business Analytics, Solution Architecture) that best fits this work item. |  | **Yes** |
| Responsible party MS BPC | MSBPC.responsibleparty | string | Details | Responsibilities | Customer \| Partner | Indicate the party responsible for this work item (e.g., Business Process Owner, Project Manager). |  | **Yes** |
| Responsible role MS BPC | MSBPC.responsiblerole | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the role responsible for this work item (e.g., Application Administrator, Data Architect). Use the pick list for options. |  | **Yes** |
| Role type MS BPC | MSBPC.roletype | string | Details | Responsibilities | Functional \| Governance \| Technical | Choose the type of role involved (e.g., Functional, Technical, Executive). Use the pick list for options. |  | **Yes** |
| Scope MS BPC | MSBPC.scope | string | Details | Scoping | 10 - Unspecified \| 20 - In scope \| 30 - Out of scope \| 40 - Not applicable | Define the scope of the work item (e.g., In scope, Out of scope). Use the pick list for boundaries and expectations. | **Yes** | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Authorized for deployment MS BPC | MSBPC.authorizedfordeployment | string | Information | Application lifecycle | Partner defined \| DEV \| TEST \| PROD | Indicate the environment/branch that is authorized next for the code or data attached to this deliverable. |  | **Yes** |
| Current highest deployment MS BPC | MSBPC.currenthighestdeployment | string | Information | Application lifecycle | Partner defined \| DEV \| TEST \| PROD | Indicate what the current highest environment/branch is for the code or data attached to this deliverable. |  | **Yes** |
| Target system MS BPC | MSBPC.targetsystem | string | Information | Entity details | N/A | Specify the target system for migration or integration (e.g., Business Central, Finance and Operations). |  | **Yes** |
| Functional design MS BPC | MSBPC.functionaldesign | html | Information | Functional design | N/A | Provide the functional design details (content or hyperlink) for how the solution will meet the business needs. |  | **Yes** |
| Menu item name MS BPC | MSBPC.menuitemname | string | References | Application details | N/A | Enter the name of the menu item in the application. Use this to identify navigation points. |  | **Yes** |
| Menu path MS BPC | MSBPC.menupath | string | References | Application details | N/A | Enter the menu path for accessing the relevant feature or process. |  | **Yes** |
| Module MS BPC | MSBPC.module | string | References | Application details | Accounts payable \| Accounts receivable \| App settings \| Asset leasing \| Asset management \| Audit workbench \| Benefits management \| Budgeting \| Business Performance Analytics \| Business Performance Planning \| Cash and bank management \| Common \| Consolidations \| Cost accounting \| Cost management \| Credit and collections \| Demand planning \| Engineering change management \| Expense management \| Fiscal books \| Fixed assets \| General ledger \| Human resources \| Inventory \| Inventory management \| Landed cost \| Leave and absence \| Master planning \| Material handling equipment interface \| Organization administration \| Payroll \| Personal settings \| Pricing management \| Procurement and sourcing \| Product information management \| Production control \| Project management and accounting \| Projects \| Questionnaire \| Rebate management \| Resources \| Retail \| Sales \| Sales and marketing \| Sales insights settings \| Scheduling \| Service \| Service management \| Settings \| Subscription billing \| System administration \| Systems settings \| Tax \| Time and attendance \| Transportation management \| Warehouse management | Select the Dynamics 365 module related to this work item (e.g., Accounts payable, Inventory management). Use the pick list for options. |  | **Yes** |
| Application family MS BPC | MSBPC.applicationfamily | string | References | Application information | Azure \| Business Central \| Cross Functional \| Customer Engagement \| Finance and Operations \| Productivity \| Power Platform | Select the application family (e.g., Business Central, Finance and Operations) relevant to this work item. This helps categorize the process. |  | **Yes** |
| Products MS BPC | MSBPC.products | string | References | Application information | Azure \| Business Central \| Commerce \| Contact Center \| Copilot Studio \| Customer Insights Data \| Customer Insights Journey \| Customer Service \| Customer Voice \| Field Service \| Finance \| Fraud Protection \| Guides \| Human Resources \| Microsoft 365 \| Other \| Power Apps \| Power Automate \| Power BI \| Power Pages \| Project \| Project Operations \| Remote Assist \| Sales \| Sales Copilot \| SharePoint \| Supply Chain Management \| Teams \| Customer Insights \| Microsoft Cloud for Sustainability | Select the relevant products (e.g., Business Central, Finance and Operations) associated with this work item. Use the pick list for options. |  | **Yes** |
| Software development company MS BPC | MSBPC.softwaredevelopmentcompany | string | References | Application information | N/A | Enter the name of the Software development company |  | **Yes** |
| Software solutions MS BPC | MSBPC.softwaresolutions | string | References | Application information | N/A | Enter the name(s) of the Software soluionts |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Industries MS BPC | MSBPC.industries | string | References | Industry focus | Agriculture (01-09) \| Construction (15-17) \| Finance, Insurance, Real Estate (60-67) \| Manufacturing (20-39) \| Mining (10-14) \| Public Administration (90-99) \| Retail Trade (52-59) \| Services (70-89) \| Transportation and Public Utilities (40-49) \| Wholesales Trade (50-51) | Select the industry or industries relevant to this work item (e.g., Manufacturing, Retail). Use the pick list for options. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Status report
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Statusreport`

A work item that captures the cover page content of the status report with additional ADO queries and dashboards as addendums.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Start Date | Microsoft.VSTS.Scheduling.StartDate | dateTime | Details | Dates | N/A | The date to start the task |  | **Yes** |
| Target Date | Microsoft.VSTS.Scheduling.TargetDate | dateTime | Details | Dates | N/A | The target date for completing the epic |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Approved budget MS BPC | MSBPC.approvedbudget | string | Details | Status report details | N/A | Provide the list of approved (original SOW plus approved Change Orders) dollars. |  | **Yes** |
| Approved hours MS BPC | MSBPC.approvedhours | string | Details | Status report details | N/A | Provide the list of approved (original SOW plus approved Change Orders) hours. |  | **Yes** |
| Report date MS BPC | MSBPC.reportdate | dateTime | Details | Status report details | N/A | Capture the date that the status report was created. |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Executive summary MS BPC | MSBPC.executivesummary | html | Information | Executive summary | N/A | Provide the executive summary as for the project for the period being covered by the current status report. |  | **Yes** |
| Project name MS BPC | MSBPC.projectname | html | Information | Project name | N/A | Provide the name of the project that this status report is being provided for. |  | **Yes** |
| Billed dollars MS BPC | MSBPC.billeddollars | string | Status report | Current status | N/A | Provide the sum of dollars billed up to the cutoff for this status report. |  | **Yes** |
| Billed hours MS BPC | MSBPC.billedhours | string | Status report | Current status | N/A | Provide the sum of hours billed up to the cutoff for this status report. |  | **Yes** |
| EAC dollars MS BPC | MSBPC.eacdollars | string | Status report | Current status | N/A | Provide the estimate at completion dollars based on the current analysis. |  | **Yes** |
| EAC hours MS BPC | MSBPC.eachours | string | Status report | Current status | N/A | Provide the estimate at completion hours based on the current analysis. |  | **Yes** |
| Percent complete MS BPC | MSBPC.percentcomplete | string | Status report | Current status | N/A | Provide the current percent complete for the project. |  | **Yes** |
| Percent variance MS BPC | MSBPC.percentvariance | string | Status report | Current status | N/A | Provide the current percent variance between approved dollars and estimate at completion dollars. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## System process
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Systemprocess`

The fifth level in the Business Process Catalog. At this level we are normally declaring each form that is used to complete the Scenario.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Priority | Microsoft.VSTS.Common.Priority | integer | Details | Priority | N/A |  |  | **Yes** |
| Process sequence ID MS BPC | MSBPC.processsequenceid | string | Details | Process IDs | N/A | Enter the unique sequence ID for the business process. Use this to organize and reference processes. | **Yes** | **Yes** |
| Fit gap status MS BPC | MSBPC.fitgapstatus | string | Details | Solution details | Fit \| Gap \| Unspecified | Select the fit-gap status (e.g., Fit, Gap) for this process. Use the pick list to indicate alignment with requirements. |  | **Yes** |
| Gap solution approach MS BPC | MSBPC.gapsolutionapproach | string | Details | Solution details | 10 - Unspecified \| 20 - Personalization \| 30 - Power Platform \| 40 - Java/Plug-in \| 50 - X++ Extension \| 60 - ISV \| 70 - ISV Extension | Select the approach for addressing gaps (e.g., Customization, Third-party solution). Use the pick list for options. |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Menu item name MS BPC | MSBPC.menuitemname | string | References | Application details | N/A | Enter the name of the menu item in the application. Use this to identify navigation points. |  | **Yes** |
| Menu path MS BPC | MSBPC.menupath | string | References | Application details | N/A | Enter the menu path for accessing the relevant feature or process. |  | **Yes** |
| Module MS BPC | MSBPC.module | string | References | Application details | Accounts payable \| Accounts receivable \| App settings \| Asset leasing \| Asset management \| Audit workbench \| Benefits management \| Budgeting \| Business Performance Analytics \| Business Performance Planning \| Cash and bank management \| Common \| Consolidations \| Cost accounting \| Cost management \| Credit and collections \| Demand planning \| Engineering change management \| Expense management \| Fiscal books \| Fixed assets \| General ledger \| Human resources \| Inventory \| Inventory management \| Landed cost \| Leave and absence \| Master planning \| Material handling equipment interface \| Organization administration \| Payroll \| Personal settings \| Pricing management \| Procurement and sourcing \| Product information management \| Production control \| Project management and accounting \| Projects \| Questionnaire \| Rebate management \| Resources \| Retail \| Sales \| Sales and marketing \| Sales insights settings \| Scheduling \| Service \| Service management \| Settings \| Subscription billing \| System administration \| Systems settings \| Tax \| Time and attendance \| Transportation management \| Warehouse management | Select the Dynamics 365 module related to this work item (e.g., Accounts payable, Inventory management). Use the pick list for options. |  | **Yes** |
| Application family MS BPC | MSBPC.applicationfamily | string | References | Application information | Azure \| Business Central \| Cross Functional \| Customer Engagement \| Finance and Operations \| Productivity \| Power Platform | Select the application family (e.g., Business Central, Finance and Operations) relevant to this work item. This helps categorize the process. |  | **Yes** |
| Products MS BPC | MSBPC.products | string | References | Application information | Azure \| Business Central \| Commerce \| Contact Center \| Copilot Studio \| Customer Insights Data \| Customer Insights Journey \| Customer Service \| Customer Voice \| Field Service \| Finance \| Fraud Protection \| Guides \| Human Resources \| Microsoft 365 \| Other \| Power Apps \| Power Automate \| Power BI \| Power Pages \| Project \| Project Operations \| Remote Assist \| Sales \| Sales Copilot \| SharePoint \| Supply Chain Management \| Teams \| Customer Insights \| Microsoft Cloud for Sustainability | Select the relevant products (e.g., Business Central, Finance and Operations) associated with this work item. Use the pick list for options. |  | **Yes** |
| Software development company MS BPC | MSBPC.softwaredevelopmentcompany | string | References | Application information | N/A | Enter the name of the Software development company |  | **Yes** |
| Software solutions MS BPC | MSBPC.softwaresolutions | string | References | Application information | N/A | Enter the name(s) of the Software soluionts |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Industries MS BPC | MSBPC.industries | string | References | Industry focus | Agriculture (01-09) \| Construction (15-17) \| Finance, Insurance, Real Estate (60-67) \| Manufacturing (20-39) \| Mining (10-14) \| Public Administration (90-99) \| Retail Trade (52-59) \| Services (70-89) \| Transportation and Public Utilities (40-49) \| Wholesales Trade (50-51) | Select the industry or industries relevant to this work item (e.g., Manufacturing, Retail). Use the pick list for options. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Alternate process sequence ID MS BPC | MSBPC.alternateprocesssequenceid | string | References | Process IDs | N/A | Enter the alternate sequence ID for deprecated or parallel processes. This value is required for any process that is deprecated and indicates the alternative process to use in place of the deprecated row. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Task
- **Enabled:** Yes
- **Class:** Derived
- **Reference name:** `MSBPCTemplate.Task`

A Task declares that something needs to be done in order to move a Deliverable or Workshop towards completion. The Task is used to communicate what needs to be done, who needs to do it, when should it be done, what the current status is and estimated time.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed
- Removed
  - Removed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
D[Removed]
A --> B
B --> C
C --> D
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Target Date | Microsoft.VSTS.Scheduling.TargetDate | dateTime | Details | Dates | N/A | The target date for completing the epic |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Completed Work | Microsoft.VSTS.Scheduling.CompletedWork | double | Details | Effort (Hours) | N/A | The number of units of work that have been spent on this bug |  | **Yes** |
| Original Estimate | Microsoft.VSTS.Scheduling.OriginalEstimate | double | Details | Effort (Hours) | N/A | Initial value for Remaining Work - set once, when work begins |  | **Yes** |
| Remaining Work | Microsoft.VSTS.Scheduling.RemainingWork | double | Details | Effort (Hours) | N/A | An estimate of the number of units of work remaining to complete this bug |  | **Yes** |
| Impediment reason MS BPC | MSBPC.impedimentreason | html | Details | Impediment information | N/A | Provide a short explaination as to what is impeding the start or continued progress of the work required to complete this task. |  | **Yes** |
| Integration Build | Microsoft.VSTS.Build.IntegrationBuild | string | Details | Implementation | N/A | The build on which the test suite was executed |  | **Yes** |
| Activity | Microsoft.VSTS.Common.Activity | string | Details | Planning | N/A | Type of work involved |  | **Yes** |
| Priority | Microsoft.VSTS.Common.Priority | integer | Details | Planning | N/A |  |  | **Yes** |
| Estimated complexity MS BPC | MSBPC.estimatedcomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the estimated complexity (e.g., Small, Medium, Large) for this work item. Use the pick list to indicate project impact. |  | **Yes** |
| Estimated project impact MS BPC | MSBPC.estimatedprojectimpact | string | Details | Planning details | Critical \| High \| Low \| Medium | Select the estimated impact (e.g., Low, Medium, High) this work item will have on the project. Use the pick list to indicate significance. |  | **Yes** |
| Contributor MS BPC | MSBPC.contributor | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the contributor(s) for this work item. Use the pick list to assign roles or individuals. |  | **Yes** |
| Program areas MS BPC | MSBPC.programareas | string | Details | Responsibilities | Business Process Management \| Data Management & Governance \| Executive Leadership \| Infrastructure Management \| Integrations & Interfaces \| Organizational Change Management \| Project Management & Governance \| Reporting & Business Analytics \| Security Management \| Solution Architecture \| Solution Development \| Solution Testing \| Training \| Usability & Experience \| Workflow Management | Choose the program area (e.g., Reporting & Business Analytics, Solution Architecture) that best fits this work item. |  | **Yes** |
| Responsible party MS BPC | MSBPC.responsibleparty | string | Details | Responsibilities | Customer \| Partner | Indicate the party responsible for this work item (e.g., Business Process Owner, Project Manager). |  | **Yes** |
| Responsible role MS BPC | MSBPC.responsiblerole | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the role responsible for this work item (e.g., Application Administrator, Data Architect). Use the pick list for options. |  | **Yes** |
| Role type MS BPC | MSBPC.roletype | string | Details | Responsibilities | Functional \| Governance \| Technical | Choose the type of role involved (e.g., Functional, Technical, Executive). Use the pick list for options. |  | **Yes** |
| Scope MS BPC | MSBPC.scope | string | Details | Scoping | 10 - Unspecified \| 20 - In scope \| 30 - Out of scope \| 40 - Not applicable | Define the scope of the work item (e.g., In scope, Out of scope). Use the pick list for boundaries and expectations. | **Yes** | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Partner phase MS BPC | MSBPC.partnerphase | string | References | Methodology | Partner defined | Select the phase of the partner engagement. Map this to the Success by Design phases for consistency. |  | **Yes** |
| Success by Design phase MS BPC | MSBPC.successbydesignphase | string | References | Methodology | 10 - Strategize \| 20 - Initiate \| 31 - Implement - Analysis \| 32 - Implement - Design \| 33 - Implement - Development \| 34 - Implement - Test \| 45 - Prepare - Train \| 49 - Prepare - Cutover \| 50 - Operate | Select the Success by Design phase (e.g., Strategize, Implement, Test) relevant to this work item. Use the pick list for options. |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Test Case
- **Enabled:** Yes
- **Class:** Derived
- **Reference name:** `MSBPCTemplate.TestCase`

The collection of all Steps that are needed field by field and click by click to complete the action in a given application.

### States
- Proposed
  - Design
- InProgress
  - Ready
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[Design]
B[Ready]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Process sequence ID MS BPC | MSBPC.processsequenceid | string | Details | Process IDs | N/A | Enter the unique sequence ID for the business process. Use this to organize and reference processes. | **Yes** | **Yes** |
| Fit gap status MS BPC | MSBPC.fitgapstatus | string | Details | Solution details | Fit \| Gap \| Unspecified | Select the fit-gap status (e.g., Fit, Gap) for this process. Use the pick list to indicate alignment with requirements. |  | **Yes** |
| Gap solution approach MS BPC | MSBPC.gapsolutionapproach | string | Details | Solution details | 10 - Unspecified \| 20 - Personalization \| 30 - Power Platform \| 40 - Java/Plug-in \| 50 - X++ Extension \| 60 - ISV \| 70 - ISV Extension | Select the approach for addressing gaps (e.g., Customization, Third-party solution). Use the pick list for options. |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Menu item name MS BPC | MSBPC.menuitemname | string | References | Application details | N/A | Enter the name of the menu item in the application. Use this to identify navigation points. |  | **Yes** |
| Menu path MS BPC | MSBPC.menupath | string | References | Application details | N/A | Enter the menu path for accessing the relevant feature or process. |  | **Yes** |
| Module MS BPC | MSBPC.module | string | References | Application details | Accounts payable \| Accounts receivable \| App settings \| Asset leasing \| Asset management \| Audit workbench \| Benefits management \| Budgeting \| Business Performance Analytics \| Business Performance Planning \| Cash and bank management \| Common \| Consolidations \| Cost accounting \| Cost management \| Credit and collections \| Demand planning \| Engineering change management \| Expense management \| Fiscal books \| Fixed assets \| General ledger \| Human resources \| Inventory \| Inventory management \| Landed cost \| Leave and absence \| Master planning \| Material handling equipment interface \| Organization administration \| Payroll \| Personal settings \| Pricing management \| Procurement and sourcing \| Product information management \| Production control \| Project management and accounting \| Projects \| Questionnaire \| Rebate management \| Resources \| Retail \| Sales \| Sales and marketing \| Sales insights settings \| Scheduling \| Service \| Service management \| Settings \| Subscription billing \| System administration \| Systems settings \| Tax \| Time and attendance \| Transportation management \| Warehouse management | Select the Dynamics 365 module related to this work item (e.g., Accounts payable, Inventory management). Use the pick list for options. |  | **Yes** |
| Application family MS BPC | MSBPC.applicationfamily | string | References | Application information | Azure \| Business Central \| Cross Functional \| Customer Engagement \| Finance and Operations \| Productivity \| Power Platform | Select the application family (e.g., Business Central, Finance and Operations) relevant to this work item. This helps categorize the process. |  | **Yes** |
| Products MS BPC | MSBPC.products | string | References | Application information | Azure \| Business Central \| Commerce \| Contact Center \| Copilot Studio \| Customer Insights Data \| Customer Insights Journey \| Customer Service \| Customer Voice \| Field Service \| Finance \| Fraud Protection \| Guides \| Human Resources \| Microsoft 365 \| Other \| Power Apps \| Power Automate \| Power BI \| Power Pages \| Project \| Project Operations \| Remote Assist \| Sales \| Sales Copilot \| SharePoint \| Supply Chain Management \| Teams \| Customer Insights \| Microsoft Cloud for Sustainability | Select the relevant products (e.g., Business Central, Finance and Operations) associated with this work item. Use the pick list for options. |  | **Yes** |
| Software development company MS BPC | MSBPC.softwaredevelopmentcompany | string | References | Application information | N/A | Enter the name of the Software development company |  | **Yes** |
| Software solutions MS BPC | MSBPC.softwaresolutions | string | References | Application information | N/A | Enter the name(s) of the Software soluionts |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Industries MS BPC | MSBPC.industries | string | References | Industry focus | Agriculture (01-09) \| Construction (15-17) \| Finance, Insurance, Real Estate (60-67) \| Manufacturing (20-39) \| Mining (10-14) \| Public Administration (90-99) \| Retail Trade (52-59) \| Services (70-89) \| Transportation and Public Utilities (40-49) \| Wholesales Trade (50-51) | Select the industry or industries relevant to this work item (e.g., Manufacturing, Retail). Use the pick list for options. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Alternate process sequence ID MS BPC | MSBPC.alternateprocesssequenceid | string | References | Process IDs | N/A | Enter the alternate sequence ID for deprecated or parallel processes. This value is required for any process that is deprecated and indicates the alternative process to use in place of the deprecated row. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |
| Automation status | Microsoft.VSTS.TCM.AutomationStatus | string | Steps | Status | N/A |  |  | **Yes** |
| Priority | Microsoft.VSTS.Common.Priority | integer | Steps | Status | N/A |  |  | **Yes** |
| Steps | Microsoft.VSTS.TCM.Steps | html | Steps | Steps | N/A | Steps required to perform the test |  | **Yes** |
| Description | System.Description | html | Summary | Description | N/A |  |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Test Plan
- **Enabled:** Yes
- **Class:** Derived
- **Reference name:** `MSBPCTemplate.TestPlan`

Tracks test activities for a specific milestone or release.

### States
- InProgress
  - Active
- Completed
  - Inactive

### State Flow
:::mermaid
flowchart LR
A[Active]
B[Inactive]
A --> B
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Finish Date | Microsoft.VSTS.Scheduling.FinishDate | dateTime | Details | Timelines | N/A | The completion date for all the tasks implementing this story |  | **Yes** |
| Start Date | Microsoft.VSTS.Scheduling.StartDate | dateTime | Details | Timelines | N/A | The date to start the task |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Test Suite
- **Enabled:** Yes
- **Class:** Derived
- **Reference name:** `MSBPCTemplate.TestSuite`

Tracks test activities for a specific feature, requirement, or user story.

### States
- InProgress
  - In Planning
  - In Progress
- Completed
  - Completed

### State Flow
:::mermaid
flowchart LR
A[In Planning]
B[In Progress]
C[Completed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Test Suite Type | Microsoft.VSTS.TCM.TestSuiteType | string | Details | Classification | N/A | Specifies the category of the test suite. |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Testing
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Testing`

A Work Product to catalog the various Testing events that will occur within the Delivery Plan.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Estimated complexity MS BPC | MSBPC.estimatedcomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the estimated complexity (e.g., Small, Medium, Large) for this work item. Use the pick list to indicate project impact. |  | **Yes** |
| Estimated project impact MS BPC | MSBPC.estimatedprojectimpact | string | Details | Planning details | Critical \| High \| Low \| Medium | Select the estimated impact (e.g., Low, Medium, High) this work item will have on the project. Use the pick list to indicate significance. |  | **Yes** |
| Contributor MS BPC | MSBPC.contributor | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the contributor(s) for this work item. Use the pick list to assign roles or individuals. |  | **Yes** |
| Program areas MS BPC | MSBPC.programareas | string | Details | Responsibilities | Business Process Management \| Data Management & Governance \| Executive Leadership \| Infrastructure Management \| Integrations & Interfaces \| Organizational Change Management \| Project Management & Governance \| Reporting & Business Analytics \| Security Management \| Solution Architecture \| Solution Development \| Solution Testing \| Training \| Usability & Experience \| Workflow Management | Choose the program area (e.g., Reporting & Business Analytics, Solution Architecture) that best fits this work item. |  | **Yes** |
| Responsible party MS BPC | MSBPC.responsibleparty | string | Details | Responsibilities | Customer \| Partner | Indicate the party responsible for this work item (e.g., Business Process Owner, Project Manager). |  | **Yes** |
| Responsible role MS BPC | MSBPC.responsiblerole | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the role responsible for this work item (e.g., Application Administrator, Data Architect). Use the pick list for options. |  | **Yes** |
| Role type MS BPC | MSBPC.roletype | string | Details | Responsibilities | Functional \| Governance \| Technical | Choose the type of role involved (e.g., Functional, Technical, Executive). Use the pick list for options. |  | **Yes** |
| Scope MS BPC | MSBPC.scope | string | Details | Scoping | 10 - Unspecified \| 20 - In scope \| 30 - Out of scope \| 40 - Not applicable | Define the scope of the work item (e.g., In scope, Out of scope). Use the pick list for boundaries and expectations. | **Yes** | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Partner phase MS BPC | MSBPC.partnerphase | string | References | Methodology | Partner defined | Select the phase of the partner engagement. Map this to the Success by Design phases for consistency. |  | **Yes** |
| Success by Design phase MS BPC | MSBPC.successbydesignphase | string | References | Methodology | 10 - Strategize \| 20 - Initiate \| 31 - Implement - Analysis \| 32 - Implement - Design \| 33 - Implement - Development \| 34 - Implement - Test \| 45 - Prepare - Train \| 49 - Prepare - Cutover \| 50 - Operate | Select the Success by Design phase (e.g., Strategize, Implement, Test) relevant to this work item. Use the pick list for options. |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Ticket
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Ticket`

A work item raised by the user to request assistance for break/fix issues, configuration changes, and etc.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Severity | Microsoft.VSTS.Common.Severity | string | Details | Bug details | Default: 3 - Medium |  |  | **Yes** |
| Requestor MS BPC | MSBPC.requestor | string, Identity | Details | Change request details | N/A | Provide the identity of the individual who requested the change. |  | **Yes** |
| Target Date | Microsoft.VSTS.Scheduling.TargetDate | dateTime | Details | Dates | N/A | The target date for completing the epic |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Story Points | Microsoft.VSTS.Scheduling.StoryPoints | double | Details | Planning details | N/A |  |  | **Yes** |
| Postmortem MS BPC | MSBPC.postmortem | html | Details | Postmortem | N/A | Provide the subjective summary as to how well the objective was achieved in the sprint or program increment/tollgate. |  | **Yes** |
| Repro Steps | Microsoft.VSTS.TCM.ReproSteps | html | Details | Repro steps | N/A |  |  | **Yes** |
| Resolution type MS BPC | MSBPC.resolutiontype | string | Details | Ticket details | 1 - No problem found \| 2 - Training needed \| 3 - Configuration change \| 4 - Enhancement required \| 5 - Defect identified \| 6 - Project request | Denote the primary resolution type that was used to resolve the issue. |  | **Yes** |
| Support level MS BPC | MSBPC.supportlevel | string | Details | Ticket details | 1 - Help Desk \| 2 - Internal Escalation \| 3 - Partner \| 4 - Vendor | Specify the current support level of the ticket. |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Tree
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Tree`

The Tree work item is used to delineate the topmost node of the different backlog types such as Business Process Catalog, Deliverables and Delivery Plan.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## User interface
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Userinterface`

A deliverable required to configure the user interface to optimize the controls and efficiency for the effected processes.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Acceptance Criteria | Microsoft.VSTS.Common.AcceptanceCriteria | html | Details | Acceptance criteria | N/A |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Baseline complexity MS BPC | MSBPC.baselinecomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the baseline complexity (e.g., Simple, Medium, Complex) for this process. This value indicates the baseline suggested complexity for estimating the project effort related to the work product. |  | **Yes** |
| Estimated complexity MS BPC | MSBPC.estimatedcomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the estimated complexity (e.g., Small, Medium, Large) for this work item. Use the pick list to indicate project impact. |  | **Yes** |
| Estimated project impact MS BPC | MSBPC.estimatedprojectimpact | string | Details | Planning details | Critical \| High \| Low \| Medium | Select the estimated impact (e.g., Low, Medium, High) this work item will have on the project. Use the pick list to indicate significance. |  | **Yes** |
| Story Points | Microsoft.VSTS.Scheduling.StoryPoints | double | Details | Planning details | N/A |  |  | **Yes** |
| Contributor MS BPC | MSBPC.contributor | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the contributor(s) for this work item. Use the pick list to assign roles or individuals. |  | **Yes** |
| Program areas MS BPC | MSBPC.programareas | string | Details | Responsibilities | Business Process Management \| Data Management & Governance \| Executive Leadership \| Infrastructure Management \| Integrations & Interfaces \| Organizational Change Management \| Project Management & Governance \| Reporting & Business Analytics \| Security Management \| Solution Architecture \| Solution Development \| Solution Testing \| Training \| Usability & Experience \| Workflow Management | Choose the program area (e.g., Reporting & Business Analytics, Solution Architecture) that best fits this work item. |  | **Yes** |
| Responsible party MS BPC | MSBPC.responsibleparty | string | Details | Responsibilities | Customer \| Partner | Indicate the party responsible for this work item (e.g., Business Process Owner, Project Manager). |  | **Yes** |
| Responsible role MS BPC | MSBPC.responsiblerole | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the role responsible for this work item (e.g., Application Administrator, Data Architect). Use the pick list for options. |  | **Yes** |
| Role type MS BPC | MSBPC.roletype | string | Details | Responsibilities | Functional \| Governance \| Technical | Choose the type of role involved (e.g., Functional, Technical, Executive). Use the pick list for options. |  | **Yes** |
| Scope MS BPC | MSBPC.scope | string | Details | Scoping | 10 - Unspecified \| 20 - In scope \| 30 - Out of scope \| 40 - Not applicable | Define the scope of the work item (e.g., In scope, Out of scope). Use the pick list for boundaries and expectations. | **Yes** | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Authorized for deployment MS BPC | MSBPC.authorizedfordeployment | string | Information | Application lifecycle | Partner defined \| DEV \| TEST \| PROD | Indicate the environment/branch that is authorized next for the code or data attached to this deliverable. |  | **Yes** |
| Current highest deployment MS BPC | MSBPC.currenthighestdeployment | string | Information | Application lifecycle | Partner defined \| DEV \| TEST \| PROD | Indicate what the current highest environment/branch is for the code or data attached to this deliverable. |  | **Yes** |
| Functional design MS BPC | MSBPC.functionaldesign | html | Information | Functional design | N/A | Provide the functional design details (content or hyperlink) for how the solution will meet the business needs. |  | **Yes** |
| Menu item name MS BPC | MSBPC.menuitemname | string | References | Application details | N/A | Enter the name of the menu item in the application. Use this to identify navigation points. |  | **Yes** |
| Menu path MS BPC | MSBPC.menupath | string | References | Application details | N/A | Enter the menu path for accessing the relevant feature or process. |  | **Yes** |
| Module MS BPC | MSBPC.module | string | References | Application details | Accounts payable \| Accounts receivable \| App settings \| Asset leasing \| Asset management \| Audit workbench \| Benefits management \| Budgeting \| Business Performance Analytics \| Business Performance Planning \| Cash and bank management \| Common \| Consolidations \| Cost accounting \| Cost management \| Credit and collections \| Demand planning \| Engineering change management \| Expense management \| Fiscal books \| Fixed assets \| General ledger \| Human resources \| Inventory \| Inventory management \| Landed cost \| Leave and absence \| Master planning \| Material handling equipment interface \| Organization administration \| Payroll \| Personal settings \| Pricing management \| Procurement and sourcing \| Product information management \| Production control \| Project management and accounting \| Projects \| Questionnaire \| Rebate management \| Resources \| Retail \| Sales \| Sales and marketing \| Sales insights settings \| Scheduling \| Service \| Service management \| Settings \| Subscription billing \| System administration \| Systems settings \| Tax \| Time and attendance \| Transportation management \| Warehouse management | Select the Dynamics 365 module related to this work item (e.g., Accounts payable, Inventory management). Use the pick list for options. |  | **Yes** |
| Application family MS BPC | MSBPC.applicationfamily | string | References | Application information | Azure \| Business Central \| Cross Functional \| Customer Engagement \| Finance and Operations \| Productivity \| Power Platform | Select the application family (e.g., Business Central, Finance and Operations) relevant to this work item. This helps categorize the process. |  | **Yes** |
| Products MS BPC | MSBPC.products | string | References | Application information | Azure \| Business Central \| Commerce \| Contact Center \| Copilot Studio \| Customer Insights Data \| Customer Insights Journey \| Customer Service \| Customer Voice \| Field Service \| Finance \| Fraud Protection \| Guides \| Human Resources \| Microsoft 365 \| Other \| Power Apps \| Power Automate \| Power BI \| Power Pages \| Project \| Project Operations \| Remote Assist \| Sales \| Sales Copilot \| SharePoint \| Supply Chain Management \| Teams \| Customer Insights \| Microsoft Cloud for Sustainability | Select the relevant products (e.g., Business Central, Finance and Operations) associated with this work item. Use the pick list for options. |  | **Yes** |
| Software development company MS BPC | MSBPC.softwaredevelopmentcompany | string | References | Application information | N/A | Enter the name of the Software development company |  | **Yes** |
| Software solutions MS BPC | MSBPC.softwaresolutions | string | References | Application information | N/A | Enter the name(s) of the Software soluionts |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Industries MS BPC | MSBPC.industries | string | References | Industry focus | Agriculture (01-09) \| Construction (15-17) \| Finance, Insurance, Real Estate (60-67) \| Manufacturing (20-39) \| Mining (10-14) \| Public Administration (90-99) \| Retail Trade (52-59) \| Services (70-89) \| Transportation and Public Utilities (40-49) \| Wholesales Trade (50-51) | Select the industry or industries relevant to this work item (e.g., Manufacturing, Retail). Use the pick list for options. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## User Story *(disabled)*
- **Enabled:** No
- **Class:** Derived
- **Reference name:** `MSBPCTemplate.UserStory`

Not used

### States
- Proposed
  - New
- InProgress
  - Active
  - Resolved
- Completed
  - Closed
- Removed
  - Removed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Resolved]
D[Closed]
E[Removed]
A --> B
B --> C
C --> D
D --> E
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Acceptance Criteria | Microsoft.VSTS.Common.AcceptanceCriteria | html | Details | Acceptance Criteria | N/A |  |  | **Yes** |
| Value Area | Microsoft.VSTS.Common.ValueArea | string | Details | Classification | N/A | Business = Customer-facing epics; Architectural = Technology initiatives to support current and future business needs |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Priority | Microsoft.VSTS.Common.Priority | integer | Details | Planning | N/A |  |  | **Yes** |
| Risk | Microsoft.VSTS.Common.Risk | string | Details | Planning | N/A | Uncertainty in epic |  | **Yes** |
| Story Points | Microsoft.VSTS.Scheduling.StoryPoints | double | Details | Planning | N/A |  |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Workflow
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Workflow`

A deliverable required in order to configure and setup a Workflow for approval, automation and sophisticated alerts for a Process to function as desired.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Acceptance Criteria | Microsoft.VSTS.Common.AcceptanceCriteria | html | Details | Acceptance criteria | N/A |  |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Baseline complexity MS BPC | MSBPC.baselinecomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the baseline complexity (e.g., Simple, Medium, Complex) for this process. This value indicates the baseline suggested complexity for estimating the project effort related to the work product. |  | **Yes** |
| Estimated complexity MS BPC | MSBPC.estimatedcomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the estimated complexity (e.g., Small, Medium, Large) for this work item. Use the pick list to indicate project impact. |  | **Yes** |
| Estimated project impact MS BPC | MSBPC.estimatedprojectimpact | string | Details | Planning details | Critical \| High \| Low \| Medium | Select the estimated impact (e.g., Low, Medium, High) this work item will have on the project. Use the pick list to indicate significance. |  | **Yes** |
| Story Points | Microsoft.VSTS.Scheduling.StoryPoints | double | Details | Planning details | N/A |  |  | **Yes** |
| Contributor MS BPC | MSBPC.contributor | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the contributor(s) for this work item. Use the pick list to assign roles or individuals. |  | **Yes** |
| Program areas MS BPC | MSBPC.programareas | string | Details | Responsibilities | Business Process Management \| Data Management & Governance \| Executive Leadership \| Infrastructure Management \| Integrations & Interfaces \| Organizational Change Management \| Project Management & Governance \| Reporting & Business Analytics \| Security Management \| Solution Architecture \| Solution Development \| Solution Testing \| Training \| Usability & Experience \| Workflow Management | Choose the program area (e.g., Reporting & Business Analytics, Solution Architecture) that best fits this work item. |  | **Yes** |
| Responsible party MS BPC | MSBPC.responsibleparty | string | Details | Responsibilities | Customer \| Partner | Indicate the party responsible for this work item (e.g., Business Process Owner, Project Manager). |  | **Yes** |
| Responsible role MS BPC | MSBPC.responsiblerole | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the role responsible for this work item (e.g., Application Administrator, Data Architect). Use the pick list for options. |  | **Yes** |
| Role type MS BPC | MSBPC.roletype | string | Details | Responsibilities | Functional \| Governance \| Technical | Choose the type of role involved (e.g., Functional, Technical, Executive). Use the pick list for options. |  | **Yes** |
| Scope MS BPC | MSBPC.scope | string | Details | Scoping | 10 - Unspecified \| 20 - In scope \| 30 - Out of scope \| 40 - Not applicable | Define the scope of the work item (e.g., In scope, Out of scope). Use the pick list for boundaries and expectations. | **Yes** | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Configuration keys MS BPC | MSBPC.configurationkeys | string | Information | Configuration settings | N/A | Enter any configuration keys relevant to the application or module. Use this to manage feature access and settings. |  | **Yes** |
| Country region codes MS BPC | MSBPC.countryregioncodes | string | Information | Configuration settings | N/A | Enter applicable country or region codes. Use this to specify localization or compliance requirements. |  | **Yes** |
| Feature management keys MS BPC | MSBPC.featuremanagementkeys | string | Information | Configuration settings | N/A | Enter any feature management keys relevant to the application. Use this to control feature availability. |  | **Yes** |
| Functional design MS BPC | MSBPC.functionaldesign | html | Information | Functional design | N/A | Provide the functional design details (content or hyperlink) for how the solution will meet the business needs. |  | **Yes** |
| At least one MS BPC | MSBPC.atleastone | boolean | Information | Toggles | Default: 0 | Indicate if at least one configuration or recommendation is required. Set to "Yes" if mandatory. | **Yes** | **Yes** |
| Can add later MS BPC | MSBPC.canaddlater | boolean | Information | Toggles | Default: 0 | Indicate if this configuration or field can be added later. Set to "Yes" if it’s not required at initial setup. | **Yes** | **Yes** |
| Can change later MS BPC | MSBPC.canchangelater | boolean | Information | Toggles | Default: 0 | Indicate if this configuration or field can be changed after initial setup. Set to "Yes" if changes are allowed. | **Yes** | **Yes** |
| Continuous MS BPC | MSBPC.continuous | boolean | Information | Toggles | Default: 0 | Indicate if this process or job is continuous. Set to "Yes" for ongoing or recurring activities. | **Yes** | **Yes** |
| Early MS BPC | MSBPC.early | boolean | Information | Toggles | Default: 0 | Indicate if this process or configuration should be completed early in the project lifecycle. Set to "Yes" if applicable. | **Yes** | **Yes** |
| Gold environment MS BPC | MSBPC.goldenvironment | boolean | Information | Toggles | Default: 0 | Indicates if this process or configuration should be completed in the Gold environment. Gold configs are copied to production during cutover. | **Yes** | **Yes** |
| Manadatory MS BPC | MSBPC.mandatory | boolean | Information | Toggles | Default: 0 | Indicate if this field or process is mandatory. Set to "Yes" if required for completion. | **Yes** | **Yes** |
| Multiple are recommended MS BPC | MSBPC.multiplearerecommended | boolean | Information | Toggles | Default: 0 | Indicate if multiple recommendations are suggested for this configuration. Set to "Yes" if more than one approach is recommended. | **Yes** | **Yes** |
| Approval levels MS BPC | MSBPC.approvallevels | integer | Information | Workflow details | N/A | Specify the number of approval levels required for this workflow. Enter an integer value based on project needs. |  | **Yes** |
| Approval types MS BPC | MSBPC.approvaltypes | string | Information | Workflow details | AI-assisted \| Automatic \| Compliance approval \| Delegated \| Escalated \| External approval \| Group approval \| Hierarchical \| Manual \| Named user \| Other \| Parallel \| Role-based \| Rule-based \| Sequential | Choose the type(s) of approval required (e.g., Compliance, Technical). Select from the pick list to clarify approval requirements. |  | **Yes** |
| Workflow type MS BPC | MSBPC.workflowtype | string | Information | Workflow details | Azure Logic App \| Custom workflow extension \| Dataverse Business process flow \| Dataverse Classic workflow \| Finance and Operations workflow \| Other \| Power Automate Flow | Choose the type of workflow associated with this work item (e.g., Custom workflow extension, Dataverse Business process flow). Use the pick list for options. | **Yes** | **Yes** |
| Menu item name MS BPC | MSBPC.menuitemname | string | References | Application details | N/A | Enter the name of the menu item in the application. Use this to identify navigation points. |  | **Yes** |
| Menu path MS BPC | MSBPC.menupath | string | References | Application details | N/A | Enter the menu path for accessing the relevant feature or process. |  | **Yes** |
| Module MS BPC | MSBPC.module | string | References | Application details | Accounts payable \| Accounts receivable \| App settings \| Asset leasing \| Asset management \| Audit workbench \| Benefits management \| Budgeting \| Business Performance Analytics \| Business Performance Planning \| Cash and bank management \| Common \| Consolidations \| Cost accounting \| Cost management \| Credit and collections \| Demand planning \| Engineering change management \| Expense management \| Fiscal books \| Fixed assets \| General ledger \| Human resources \| Inventory \| Inventory management \| Landed cost \| Leave and absence \| Master planning \| Material handling equipment interface \| Organization administration \| Payroll \| Personal settings \| Pricing management \| Procurement and sourcing \| Product information management \| Production control \| Project management and accounting \| Projects \| Questionnaire \| Rebate management \| Resources \| Retail \| Sales \| Sales and marketing \| Sales insights settings \| Scheduling \| Service \| Service management \| Settings \| Subscription billing \| System administration \| Systems settings \| Tax \| Time and attendance \| Transportation management \| Warehouse management | Select the Dynamics 365 module related to this work item (e.g., Accounts payable, Inventory management). Use the pick list for options. |  | **Yes** |
| Application family MS BPC | MSBPC.applicationfamily | string | References | Application information | Azure \| Business Central \| Cross Functional \| Customer Engagement \| Finance and Operations \| Productivity \| Power Platform | Select the application family (e.g., Business Central, Finance and Operations) relevant to this work item. This helps categorize the process. |  | **Yes** |
| Products MS BPC | MSBPC.products | string | References | Application information | Azure \| Business Central \| Commerce \| Contact Center \| Copilot Studio \| Customer Insights Data \| Customer Insights Journey \| Customer Service \| Customer Voice \| Field Service \| Finance \| Fraud Protection \| Guides \| Human Resources \| Microsoft 365 \| Other \| Power Apps \| Power Automate \| Power BI \| Power Pages \| Project \| Project Operations \| Remote Assist \| Sales \| Sales Copilot \| SharePoint \| Supply Chain Management \| Teams \| Customer Insights \| Microsoft Cloud for Sustainability | Select the relevant products (e.g., Business Central, Finance and Operations) associated with this work item. Use the pick list for options. |  | **Yes** |
| Software development company MS BPC | MSBPC.softwaredevelopmentcompany | string | References | Application information | N/A | Enter the name of the Software development company |  | **Yes** |
| Software solutions MS BPC | MSBPC.softwaresolutions | string | References | Application information | N/A | Enter the name(s) of the Software soluionts |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Industries MS BPC | MSBPC.industries | string | References | Industry focus | Agriculture (01-09) \| Construction (15-17) \| Finance, Insurance, Real Estate (60-67) \| Manufacturing (20-39) \| Mining (10-14) \| Public Administration (90-99) \| Retail Trade (52-59) \| Services (70-89) \| Transportation and Public Utilities (40-49) \| Wholesales Trade (50-51) | Select the industry or industries relevant to this work item (e.g., Manufacturing, Retail). Use the pick list for options. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None

## Workshop
- **Enabled:** Yes
- **Class:** Custom
- **Reference name:** `MSBPCTemplate.Workshop`

The Workshop type is used to catalog that a key meeting exists within the partner's methodology to be placed in the Delivery Plan backlog.

### States
- Proposed
  - New
- InProgress
  - Active
- Completed
  - Closed

### State Flow
:::mermaid
flowchart LR
A[New]
B[Active]
C[Closed]
A --> B
B --> C
:::

### Fields
<details>
<summary>Expand for Field-level Details</summary>

| Field | Reference name | Type | Page | Group | Values/Definition | Description | Required | Visible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Activated By | Microsoft.VSTS.Common.ActivatedBy | string, Identity |  |  | N/A |  |  |  |
| Activated Date | Microsoft.VSTS.Common.ActivatedDate | dateTime |  |  | N/A |  |  |  |
| Closed By | Microsoft.VSTS.Common.ClosedBy | string, Identity |  |  | N/A |  |  |  |
| Closed Date | Microsoft.VSTS.Common.ClosedDate | dateTime |  |  | N/A |  |  |  |
| Resolved By | Microsoft.VSTS.Common.ResolvedBy | string, Identity |  |  | N/A |  |  |  |
| Resolved Date | Microsoft.VSTS.Common.ResolvedDate | dateTime |  |  | N/A |  |  |  |
| State Change Date | Microsoft.VSTS.Common.StateChangeDate | dateTime |  |  | N/A |  |  |  |
| Area Path | System.AreaPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Assigned To | System.AssignedTo | string, Identity | (System) | (System controls) | N/A |  |  | **Yes** |
| Iteration Path | System.IterationPath | treePath | (System) | (System controls) | N/A |  |  | **Yes** |
| Reason | System.Reason | string | (System) | (System controls) | N/A |  |  | **Yes** |
| State | System.State | string | (System) | (System controls) | Default: New |  | **Yes** | **Yes** |
| Title | System.Title | string | (System) | (System controls) | N/A |  |  | **Yes** |
| Agenda MS BPC | MSBPC.agenda | html | Details | Agenda | N/A | Provide the agenda of the expected content to be covered in each workshop. |  | **Yes** |
| Start Date | Microsoft.VSTS.Scheduling.StartDate | dateTime | Details | Dates | N/A | The date to start the task |  | **Yes** |
| Description | System.Description | html | Details | Description | N/A |  |  | **Yes** |
| Duration MS BPC | MSBPC.duration | string | Details | Duration | N/A | Estimate the number of weeks of duration for the phase. |  | **Yes** |
| Key questions MS BPC | MSBPC.keyquestions | html | Details | Key questions | N/A | Provide the listing of the key questions that are expected to be discussed and resolved as an outcome of the workshop. |  | **Yes** |
| Estimated complexity MS BPC | MSBPC.estimatedcomplexity | string | Details | Planning details | L - Large \| M - Medium \| S - Small \| XL - Extra Large \| XS - Extra Small | Select the estimated complexity (e.g., Small, Medium, Large) for this work item. Use the pick list to indicate project impact. |  | **Yes** |
| Estimated project impact MS BPC | MSBPC.estimatedprojectimpact | string | Details | Planning details | Critical \| High \| Low \| Medium | Select the estimated impact (e.g., Low, Medium, High) this work item will have on the project. Use the pick list to indicate significance. |  | **Yes** |
| Contributor MS BPC | MSBPC.contributor | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the contributor(s) for this work item. Use the pick list to assign roles or individuals. |  | **Yes** |
| Program areas MS BPC | MSBPC.programareas | string | Details | Responsibilities | Business Process Management \| Data Management & Governance \| Executive Leadership \| Infrastructure Management \| Integrations & Interfaces \| Organizational Change Management \| Project Management & Governance \| Reporting & Business Analytics \| Security Management \| Solution Architecture \| Solution Development \| Solution Testing \| Training \| Usability & Experience \| Workflow Management | Choose the program area (e.g., Reporting & Business Analytics, Solution Architecture) that best fits this work item. |  | **Yes** |
| Responsible party MS BPC | MSBPC.responsibleparty | string | Details | Responsibilities | Customer \| Partner | Indicate the party responsible for this work item (e.g., Business Process Owner, Project Manager). |  | **Yes** |
| Responsible role MS BPC | MSBPC.responsiblerole | string | Details | Responsibilities | Application Administrator \| Build Manager \| Business Analyst \| Business Architect \| Business Change Leads \| Business Lead \| Business Process Owner \| Business Subject Matter Experts (SME) \| Business Unit Sponsors \| Change Management Lead \| Communications Lead \| Compliance Manager \| Data Architect \| Data Migration Analyst \| Data Migration Lead \| Database Administrator \| Delivery Lead \| Deployment Lead \| Developer \| Development Lead \| Enterprise Architect \| Executive - Business (CEO/CFO/COO) \| Executive - Technology (VP/Director/CTO/CIO) \| Executive Sponsor \| Infrastructure Lead \| Integration Analyst \| Integration Architect \| Integration Lead \| Network Administrator \| Program Manager \| Project Manager \| Project Sponsor \| Quality Analyst \| Reporting Analyst \| Reporting Lead \| Security Administrator \| Security Analyst \| Security Developer \| Security Lead \| Solution Architect \| Solution Manager \| Solution Specialist \| Support Analyst \| Support Manager \| Technical Architect \| Testing Lead \| Trainer \| Training Lead \| UX Designer \| Workflow Analyst \| Workflow Lead | Select the role responsible for this work item (e.g., Application Administrator, Data Architect). Use the pick list for options. |  | **Yes** |
| Role type MS BPC | MSBPC.roletype | string | Details | Responsibilities | Functional \| Governance \| Technical | Choose the type of role involved (e.g., Functional, Technical, Executive). Use the pick list for options. |  | **Yes** |
| Scheduling notes MS BPC | MSBPC.schedulingnotes | html | Details | Scheduling notes | N/A | Provide information that will help in determining when the workshop should be scheduled. |  | **Yes** |
| Scope MS BPC | MSBPC.scope | string | Details | Scoping | 10 - Unspecified \| 20 - In scope \| 30 - Out of scope \| 40 - Not applicable | Define the scope of the work item (e.g., In scope, Out of scope). Use the pick list for boundaries and expectations. | **Yes** | **Yes** |
| Workshop assumptions MS BPC | MSBPC.workshopassumptions | html | Details | Workshop assumptions | N/A | List various assumptions and pre-requisites expected prior to each workshop. |  | **Yes** |
| History | System.History | history | History | History | N/A |  |  | **Yes** |
| Article status MS BPC | MSBPC.articlestatus | string | References | Catalog details | 10 - Not started \| 20 - In progress \| 30 - Assigned \| 40 - Technical review \| 50 - Publish requested \| 60 - Published \| 70 - Update required \| 90 - Help wanted | Select the current status of the article (e.g., Not started, Drafted, Published). This status indicates the progress of a Microsoft Learn article that documents the process. | **Yes** | **Yes** |
| Author MS BPC | MSBPC.author | string | References | Catalog details | Microsoft \| Partner \| Project | Denote if the current version of this catalog entry is Microsoft, Partner or Project pecific. |  | **Yes** |
| Catalog status MS BPC | MSBPC.catalogstatus | string | References | Catalog details | 10 - New \| 20 - Review \| 30 - Updated \| 40 - Published \| 50 - Custom \| 60 - Deprecated \| 65 - Deprecated (final) \| 70 - Deleted | Select the current status of the catalog item (e.g., New, In progress, Published). Use this field to determine which rows are new, updated, or deprecated from Microsoft. | **Yes** | **Yes** |
| Mavim ID MS BPC | MSBPC.mavimid | string | References | External IDs | N/A |  |  | **Yes** |
| Microsoft ID MS BPC | MSBPC.microsoftid | string | References | External IDs | N/A | Indicates the unique Microsoft ID associated with this work item. This ID can be used for matching and taking updates to the work items. | **Yes** | **Yes** |
| Partner ID MS BPC | MSBPC.partnerid | string | References | External IDs | N/A | Enter the partner ID if this process or item is managed by a partner. Required for custom processes involving external partners. |  | **Yes** |
| Internal references MS BPC | MSBPC.internalreferences | html | References | Internal references | N/A | Provide links to various client specific reference materials. |  | **Yes** |
| Mavim reference MS BPC | MSBPC.mavimreference | html | References | Mavim reference | N/A |  |  | **Yes** |
| Partner phase MS BPC | MSBPC.partnerphase | string | References | Methodology | Partner defined | Select the phase of the partner engagement. Map this to the Success by Design phases for consistency. |  | **Yes** |
| Success by Design phase MS BPC | MSBPC.successbydesignphase | string | References | Methodology | 10 - Strategize \| 20 - Initiate \| 31 - Implement - Analysis \| 32 - Implement - Design \| 33 - Implement - Development \| 34 - Implement - Test \| 45 - Prepare - Train \| 49 - Prepare - Cutover \| 50 - Operate | Select the Success by Design phase (e.g., Strategize, Implement, Test) relevant to this work item. Use the pick list for options. |  | **Yes** |
| Microsoft references MS BPC | MSBPC.microsoftreferences | html | References | Microsoft references | N/A | Enter any relevant Microsoft documentation or reference links that support this work item. |  | **Yes** |
| Partner references MS BPC | MSBPC.partnerreferences | html | References | Partner references | N/A | Provide any links to Partner documentation or references that support this work item. |  | **Yes** |
| Update comments MS BPC | MSBPC.updatecomments | html | References | Update comments | N/A | Add any comments or notes about updates made to this work item. Provide context for changes or revisions. |  | **Yes** |
| Partner workshop type MS BPC | MSBPC.partnerworkshoptype | string | References | Workshop details | Partner defined | Specify the workshop type based on the partner's methodology. |  | **Yes** |

</details>

### Rules
- Custom Rules
  - None
