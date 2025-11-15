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
