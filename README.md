## Dataset
1. **Overview Dataset**

The TTS Handbook is an extensive knowledge-base created by Technology Transformation Services (TTS), a division of the U.S. General Services Administration (GSA).
The entire dataset is fully open-source, publicly accessible, and contains no sensitive information or internal accounts.

Structured into 38 directories and 250+ Markdown files, the collection captures a wide range of organizational knowledge typically found inside a large government-level institution, including:

Team operations

HR policies

Hiring and onboarding processes

Project management guidelines

Supervisor and leadership guidance

Technical tools and IT procedures

Partner and vendor collaboration practices

Travel and leave policies

Training and professional development

Conflict resolution and feedback practices

Security policies and technology standards

Leadership and management principles

You can browse the original repository here:
https://github.com/GSA-TTS/handbook/tree/main/pages

2. **Dataset Structure**

The TTS Handbook dataset is organized into clear directories, each representing a specific domain of organizational knowledge. Below is a concise breakdown of the major folders and their contents.

**18f**

Documentation for the 18F team, including:

Roles & disciplines: account manager, engineering, design, product, acquisition

Internal operations: business development, contractors, project lifecycle, research guidelines, staffing, agreements

Leadership materials: candidate guidance, leadership selection

Working with partners: consulting engineering, leading projects, project team guidance, distressed project handling

**about-us**

Organizational information and foundational resources:

Code of conduct

Org charts

TTS consulting (mission, operations)

Internal communication guidance

Training and onboarding materials

**general-information-and-resources**

Core policies and essential employee resources:

Business & operations: billing, IG CAP, classified-policy references

Employee resources: benefits, check-ins, transit, support programs, work schedules

Conflict feedback: frameworks and conflict-resolution guidance

Tech policies: passwords, bug bounty, open source, records, security incidents

Tools overview: approved software, purchase processes, general contacts

**getting-started**

Primary onboarding materials:

Equipment setup

Login instructions

PIV

Welcome package

Initial classes and training

**hiring-staying-or-changing-jobs**

Complete HR lifecycle:

Hiring processes

Hiring authorities

Promotions

Résumé guidance

Offboarding

Term extensions

**launching-software**

Technical and compliance documentation:

Security

Infrastructure

Legal requirements

Privacy

Product lifecycle processes

**office-of-acquisition**

Procurement and acquisition workflows.

**office-of-operations**

Operations-related resources:

BizOps

Blogging

Outreach & market development

Social media

Talent processes

**office-of-solutions**

Materials on:

Organizational history

Org charts

Technology operations

Innovation portfolio

**performance-management**

Employee performance evaluation materials:

Mid-year & end-of-year reviews

Supervisor resources

Annual review cycle timelines

**supervisor-resources**

A comprehensive supervisor playbook (12 plays), covering management responsibilities and best practices.

**tools**

Extensive tool documentation — the most valuable section for IT-support chatbots:

Adobe, Airtable

Analytics tools

Docker Hub

GitHub

Google Workspace (Docs, Calendar, Meet, Groups)

Gmail

Mural

New Relic

Microsoft Office

Slack

Smartsheet

Teams

Trello

VMware

Zoom

Shared calendars

Text editors

Includes a specialized Slack subdirectory:

Getting started

Guidelines

Integrations

Notifications

User management

Records

**training-and-development**

Materials for professional growth:

Conferences

Development programs

GitHub introduction

Working groups

PRA for user research

**travel-and-leave**

HR-level travel and leave documentation:

FMLA

Leave policies

Overtime

Paid parental leave

Travel guides

Out-of-office procedures

Emergency travel

Reimbursements

## File Organization
```text
company-internal-chatbot/
├── pages/                          # Bộ tài liệu nội bộ (markdown) để ingest
│   ├── onboarding/
│   ├── it/
│   ├── hr/
│   └── ...                         # (Toàn bộ .md lấy từ handbook)
│
├── chroma_db/                      # Vector database (auto-generated sau ingestion)
│   └── ...                         
│
├── config.py                       #  Config chung (Gemini client + E5 embed model + Chroma)
├── ingest_handbook.py              #  Ingestion pipeline (đọc pages → chunk → embed → lưu vector DB)
├── rag_core.py                     #  RAG core (embed query → retrieve → Gemini generate)
├── api.py                          #  FastAPI server (endpoint /chatbot_query)
│
├── requirements.txt                #  Danh sách thư viện chạy project
├── README.md                       #  Mô tả dự án, pipeline, cách chạy
└── .gitignore                      # (optional) Ignore venv, chroma_db, cache, etc.
```

**Nguyễn Đức Anh**

University: Hanoi University of Science and Technology (HUST)

Email: [anh.nd210020@gmail.com](mailto:anh.nd210020@gmail.com)

Address: Hanoi, Vietnam

GitHub: [anhnd210020](https://github.com/anhnd210020)