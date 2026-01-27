from fasthtml.common import *
import yaml
from pathlib import Path

# Clean imports from your components folder
from components.header import PageHeader
from components.hero import Hero
from components.resume import ResumeSection
from components.project_card import ProjectsSection
from components.footer import PageFooter

def load_resume():
    try:
        # Resolve gets the absolute path, fixing "File Not Found" errors in the cloud
        base_dir = Path(__file__).resolve().parent
        yaml_path = base_dir / "data" / "resume.yaml"
        
        with open(yaml_path, "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading resume: {e}")
        # Fallback to prevent 500 Crash if file is moved/missing
        return {
            "name": "Nolan Fox", 
            "title": "Portfolio", 
            "summary": "Could not load data.", 
            "projects": []
        }

# --- APP CONFIGURATION ---
headers = (
    Script(src="https://cdn.tailwindcss.com"),
    Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap"),
    Style("""
        /* FORCE Dark Background */
        html, body { 
            background-color: #020617 !important; 
            color: #f8fafc; 
            font-family: 'Inter', sans-serif; 
            min-height: 100vh;
        }
        /* Text Visibility Enforcement */
        p, span, div, a, li, h1, h2, h3, h4, h5, h6 {
            opacity: 1 !important;
        }
        .mono { font-family: 'JetBrains Mono', monospace; }
        
        /* The Fixed Background Grid */
        .fixed-grid-background {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0;
            background-size: 40px 40px;
            background-image: linear-gradient(to right, rgba(255, 255, 255, 0.03) 1px, transparent 1px),
                              linear-gradient(to bottom, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
            mask-image: linear-gradient(to bottom, black 40%, transparent 100%);
            -webkit-mask-image: linear-gradient(to bottom, black 40%, transparent 100%);
        }
        .content-layer { position: relative; z-index: 10; }
    """)
)

# CRITICAL FOR VERCEL: live=False
app, rt = fast_app(hdrs=headers, live=False, pico=False)

@rt("/")
def get():
    # Load data from YAML on every request
    resume = load_resume()

    return (
        Title(f"{resume.get('name', 'Nolan Fox')} - {resume.get('title', 'Data Scientist')}"),
        Body(
            Div(cls="fixed-grid-background"),
            Div(
                PageHeader(),
                Main(
                    Hero(
                        name=resume.get("name", "Nolan Fox"),
                        title=resume.get("title", "Data Scientist"),
                        summary=resume.get("summary", "Building AI systems."),
                    ),
                    ResumeSection(resume),
                    ProjectsSection(resume.get("projects", [])),
                    cls="max-w-7xl mx-auto w-full"
                ),
                PageFooter(
                    email=resume.get("email"),
                    github="NolanFox", 
                    linkedin="https://www.linkedin.com/in/nolanfox/" 
                ),
                cls="content-layer flex flex-col min-h-screen"
            ),
            cls="bg-slate-950 text-slate-100"
        ),
    )

# Ensures server only runs locally, not in the cloud
if __name__ == "__main__":
    serve(port=5003)