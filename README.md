## Dataset
1. **Overview**

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