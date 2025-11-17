## Dataset
1. **Overview**
Dataset
1. Overview

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