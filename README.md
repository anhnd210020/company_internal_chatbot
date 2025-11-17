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
.
├── api.py                      # FastAPI: /chatbot_query endpoint
├── config.py                   # Gemini, embeddings, and Chroma configuration
├── rag_core.py                 # RAG logic: retrieval + generation
├── ingest_handbook.py          # Ingest TTS Handbook into ChromaDB
│
├── pages/                      # TTS Handbook dataset (Markdown files)
│   ├── 18f/                    # 18F team: history, projects, leadership
│   ├── about-us/               # Organization info, code of conduct, org chart
│   ├── general-information-and-resources/  # Policies, employee resources, tech policies
│   ├── getting-started/        # Onboarding, equipment, login guides
│   ├── hiring-staying-or-changing-jobs/    # Hiring, promotions, role changes
│   ├── launching-software/     # Software lifecycle, security, privacy
│   ├── office-of-acquisition/  # Procurement processes, roles & responsibilities
│   ├── office-of-operations/   # BizOps, outreach, internal communications
│   ├── office-of-solutions/    # Tech operations, innovation portfolio
│   ├── performance-management/ # Performance reviews: mid-year, end-year
│   ├── supervisor-resources/   # Supervisor playbook and management guides
│   ├── tools/                  # Guides for Slack, GitHub, Google, Zoom, etc.
│   ├── training-and-development/ # Training, conferences, working groups
│   ├── travel-and-leave/       # Leave policies, overtime, travel guidelines
│   └── updating-the-handbook/  # How to edit and update the handbook
│
├── chroma_db/                  # Chroma vector store (auto-generated after ingestion)
├── gemini_env/                 # Gemini environment / configuration
├── tts_handbook/               # Original TTS Handbook clone (optional)
│
├── README.md
├── requirements.txt
└── __pycache__/                # Python cache files
```

**Nguyễn Đức Anh**

University: Hanoi University of Science and Technology (HUST)

Email: [anh.nd210020@gmail.com](mailto:anh.nd210020@gmail.com)

Address: Hanoi, Vietnam

GitHub: [anhnd210020](https://github.com/anhnd210020)