# 🧠 Face2Face Form Intelligence Engine

## Overview

This project crawls websites starting from the homepage, follows CTA links, identifies the most relevant contact or lead-gen form, and produces an enhanced, customized version of the form—ready to be embedded with Face2Face.

The engine is broken into clear, modular components and uses AI in targeted places to maintain control and consistency.

---

## ⚠️ AI INSTRUCTIONS – READ FIRST

Before taking any action, **always follow these steps**:

1. **Read this README** to understand the high-level project structure.
2. **Read the module-level README** in the relevant folder before modifying any code.
3. **Do not create or edit files unless they follow the architecture and contracts described in the READMEs.**
4. When in doubt, ask or leave a placeholder comment instead of guessing.

---

## Folder Structure

```
f2f-form-engine/
├── .gitignore
├── README.md
├── Procfile
├── requirements.txt
├── runtime.txt
├── app.py
├── main_pipeline.py
├── project_description.md
│
├── motion_detector/
│   ├── motion_detector.py
│   ├── ai_cta_classifier.py
│   ├── dom_parser.py
│   ├── link_visitor.py
│   ├── utils.py
│   ├── sample_input.json
│   ├── sample_output.json
│   └── README.md
│
├── homepage_loader/
│   ├── homepage_loader.py
│   ├── utils.py
│   └── README.md
│
├── cta_navigator/
│   ├── cta_navigator.py
│   ├── form_scraper.py
│   └── README.md
│
├── form_ranker/
│   ├── form_ranker.py
│   ├── ai_form_selector.py
│   └── README.md
│
├── form_analyzer/
│   ├── form_analyzer.py
│   ├── schema_builder.py
│   └── README.md
│
├── form_customizer/
│   ├── form_customizer.py
│   ├── enhancer.py
│   ├── template_loader.py
│   └── README.md
│
├── output_writer/
│   ├── output_writer.py
│   ├── storage.py
│   └── README.md
│
├── ui_renderer/
│   ├── ui_renderer.py
│   ├── templates/
│   │   └── preview.html
│   ├── static/
│   │   └── style.css
│   └── README.md
│
└── shared/
    ├── logging_config.py
    ├── openai_client.py
    └── config.py
```

---

## Pipeline Flow

```
Input:     https://example.com

1. motion_detector       → "contact-form"
2. homepage_loader       → ["/contact", "/demo"]
3. cta_navigator         → Finds 3 form candidates
4. form_ranker (AI)      → Picks best form based on fields, context
5. form_analyzer         → Extracts field structure, action, method
6. form_customizer       → Enhances form with Face2Face logic
7. output_writer         → Saves HTML, schema, diffs
8. ui_renderer (optional)→ Shows side-by-side preview
```

---

## Output Example

```json
{
  "form_page_url": "https://example.com/contact",
  "cta_click_path": ["Home", "Contact"],
  "form_schema": {
    "fields": [
      { "name": "email", "type": "email", "label": "Work Email" }
    ],
    "action": "/api/contact",
    "method": "POST"
  },
  "custom_form.html": "<form>...</form>",
  "diff_report.md": "- Added Face2Face widget\n- Changed CTA to 'Start Conversation'"
}
```

---

## Running the Pipeline

> Coming soon: `main_pipeline.py`

This script will:
- Accept a start URL
- Run the full pipeline (Motion Detector → Crawler → Analyzer → Customizer → Output)
- Optionally render previews locally

---

## Dev Notes

- Each module is strictly responsible for one task.
- Use `input.json` and `output.json` mocks inside each module folder to test/debug independently.
- Don’t let AI generate across module boundaries without reading the READMEs.

---

Let’s build ✨