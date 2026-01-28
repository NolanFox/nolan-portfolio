```markdown
# Agentic AI Portfolio (FastHTML + Python)

A serverless, database-free personal portfolio website engineered to be fast, modular, and easy to maintain. 
Built using an **Agentic Workflow** (Claude Code + Cursor) on a pure Python stack.

**Live Site:** [nolanandrewfox.com](https://www.nolanandrewfox.com)

## ⚡️ Tech Stack

* **Framework:** [FastHTML](https://fastht.ml/) (Modern Python web framework)
* **Styling:** Tailwind CSS (via CDN)
* **Hosting:** Vercel (Serverless Python Runtime)
* **Data Source:** YAML (`data/resume.yaml`)
* **Architecture:** Database-free, Static Asset serving via Python

## 📂 Project Structure

```text
nolan-portfolio/
├── api/                # Vercel Serverless Entry Point
│   └── index.py        # Bridge between Vercel and main.py
├── components/         # UI Modules (Atomic Design)
│   ├── header.py       # Navigation
│   ├── hero.py         # Landing section
│   ├── resume.py       # Experience & Education timeline
│   └── project_card.py # Project grid
├── data/
│   └── resume.yaml     # SINGLE SOURCE OF TRUTH for all text
├── public/             # Static Assets (Images, Favicons)
│   └── favicon.ico     # Site Icon
├── main.py             # Application Logic & Routing
├── requirements.txt    # Python Dependencies
├── runtime.txt         # Enforces Python 3.11 on Vercel
└── vercel.json         # Serverless Configuration

```

## 🚀 How to Run Locally

1. **Clone the repository:**
```bash
git clone [https://github.com/NolanFox/nolan-portfolio.git](https://github.com/NolanFox/nolan-portfolio.git)
cd nolan-portfolio

```


2. **Install dependencies:**
```bash
pip install -r requirements.txt

```


3. **Run the server:**
```bash
python main.py

```


4. **View it:**
Open your browser to `http://localhost:5003`

## 📝 How to Update Content

You do not need to touch the Python code to update your resume or add projects.

### 1. Update Resume Text

Edit `data/resume.yaml`. The site pulls `name`, `summary`, `work`, and `education` directly from this file.

### 2. Add a New Project

Add a new block to the `projects` list in `data/resume.yaml`:

```yaml
- title: "New AI Agent"
  description: "Description of what I built..."
  status: "In Progress"  # Options: In Progress, Completed, Planned
  tags: ["Python", "LLM", "RAG"]
  link: "[https://github.com/](https://github.com/)..."

```

### 3. Add Static Images

1. Place the image in the `public/` folder.
2. Link to it using the **Absolute URL** (required for Vercel serverless stability):
`https://www.nolanandrewfox.com/your-image.jpg`

## ☁️ Deployment (Vercel)

This project is configured for **Continuous Deployment**.

1. **Commit your changes:**
```bash
git add .
git commit -m "Update content"
git push

```


2. **That's it.** Vercel detects the push and deploys automatically in ~60 seconds.

## 🧠 Architecture Decisions & Fixes

This project encountered and solved several specific serverless challenges:

* **Database Bypass:** FastHTML defaults to using `apsw` (SQLite), which crashes on Vercel's Amazon Linux environment. We successfully refactored `main.py` to use `FastHTML()` directly, removing the database dependency entirely.
* **Static Assets:** Vercel's Python runtime has strict routing rules. We solved the "Favicon 404" issue by implementing a specific Python route (`def favicon`) and using Absolute URLs in the HTML header to guarantee path resolution.
* **Runtime Locking:** We use `runtime.txt` to force Vercel to use Python 3.11, matching the local development environment.

```

```