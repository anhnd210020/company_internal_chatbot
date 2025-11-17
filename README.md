## Dataset
1. **Overview Dataset**

The TTS Handbook is an extensive knowledge-base created by Technology Transformation Services (TTS), a division of the U.S. General Services Administration (GSA).
The entire dataset is fully open-source, publicly accessible, and contains no sensitive information or internal accounts.

Structured into 38 directories and 250+ Markdown files, the collection captures a wide range of organizational knowledge typically found inside a large government-level institution, including:

**- Team operations**

+ HR policies

+ Hiring and onboarding processes

+ Project management guidelines

+ Supervisor and leadership guidance

+ Technical tools and IT procedures

+ Partner and vendor collaboration practices

+ Travel and leave policies

+ Training and professional development

+ Conflict resolution and feedback practices

+ Security policies and technology standards

+ Leadership and management principles

You can browse the original repository here:
https://github.com/GSA-TTS/handbook/tree/main/pages

2. **Dataset Structure**

The TTS Handbook dataset is organized into clear directories, each representing a specific domain of organizational knowledge. Below is a concise breakdown of the major folders and their contents.

**- 18f**

+ Documentation for the 18F team, including:

+ Roles & disciplines: account manager, engineering, design, product, acquisition

+ Internal operations: business development, contractors, project lifecycle, research guidelines, staffing, agreements

+ Leadership materials: candidate guidance, leadership selection

+ Working with partners: consulting engineering, leading projects, project team guidance, distressed project handling

**- about-us**

+ Organizational information and foundational resources:

1. Code of conduct

2. Org charts

3. TTS consulting (mission, operations)

4. Internal communication guidance

5. Training and onboarding materials

**- general-information-and-resources**

+ Core policies and essential employee resources:

+ Business & operations: billing, IG CAP, classified-policy references

+ Employee resources: benefits, check-ins, transit, support programs, work schedules

+ Conflict feedback: frameworks and conflict-resolution guidance

+ Tech policies: passwords, bug bounty, open source, records, security incidents

+ Tools overview: approved software, purchase processes, general contacts

**- getting-started**

+ Primary onboarding materials:

1. Equipment setup

2. Login instructions

3. PIV

4. Welcome package

5. Initial classes and training

**- hiring-staying-or-changing-jobs**

+ Complete HR lifecycle:

1. Hiring processes

2. Hiring authorities

3. Promotions

4. Resume guidance

5. Offboarding

6. Term extensions

**- launching-software**

+ Technical and compliance documentation:

1. Security

2. Infrastructure

3. Legal requirements

4. Privacy

5. Product lifecycle processes

**- office-of-acquisition**

+ Procurement and acquisition workflows.

**- office-of-operations**

+ Operations-related resources:

1. BizOps

2. Blogging

3. Outreach & market development

4. Social media

5. Talent processes

**- office-of-solutions**

+ Materials on:

1. Organizational history

2. Org charts

3. Technology operations

4. Innovation portfolio

**- performance-management**

Employee performance evaluation materials:

1. Mid-year & end-of-year reviews

2. Supervisor resources

3. Annual review cycle timelines

**- supervisor-resources**

+ A comprehensive supervisor playbook (12 plays), covering management responsibilities and best practices.

**- tools**

+ Extensive tool documentation — the most valuable section for IT-support chatbots:

1. Adobe, Airtable

2. Analytics tools

3. Docker Hub

4. GitHub

5. Google Workspace (Docs, Calendar, Meet, Groups)

6. Gmail

7. Mural

8. New Relic

9. Microsoft Office

10. Slack

11. Smartsheet

12. Teams

13. Trello

14. VMware

15. Zoom

16. Shared calendars

17. Text editors

18. Includes a specialized Slack subdirectory:

19. Getting started

20. Guidelines

21. Integrations

22. Notifications

23. User management

24. Records

**- training-and-development**

+ Materials for professional growth:

1. Conferences

2. Development programs

3. GitHub introduction

4. Working groups

5. PRA for user research

**- travel-and-leave**

+ HR-level travel and leave documentation:

1. FMLA

2. Leave policies

3. Overtime

4. Paid parental leave

5. Travel guides

6. Out-of-office procedures

7. Emergency travel

8. Reimbursements

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