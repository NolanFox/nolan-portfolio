from pathlib import Path
import yaml
from fasthtml.common import *

# DIRECT IMPORTS
from components.header import PageHeader
from components.hero import Hero
from components.resume import ResumeSection
from components.project_card import ProjectsSection
from components.footer import PageFooter

def load_resume():
    try:
        # Vercel-safe path handling
        current_dir = Path(__file__).parent
        resume_path = current_dir / "data" / "resume.yaml"
        
        if not resume_path.exists():
            print(f"WARNING: Resume file not found at {resume_path}")
            # Fallback to avoid crashing if path is wrong in cloud
            return {
                "name": "Nolan Fox", 
                "title": "Data Scientist", 
                "summary": "Resume data could not be loaded.", 
                "projects": []
            }
            
        with open(resume_path) as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading resume: {e}")
        return {"name": "Nolan Fox", "title": "Error Loading Data", "projects": []}

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

        /* TEXT VISIBILITY ENFORCEMENT */
        p, span, div, a, li, h1, h2, h3, h4, h5, h6 {
            opacity: 1 !important; /* Never let text fade */
        }
        
        .mono { font-family: 'JetBrains Mono', monospace; }
        
        /* THE FIX: Isolate the grid pattern */
        .fixed-grid-background {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0; /* Behind everything */
            
            /* The Grid Pattern */
            background-size: 40px 40px;
            background-image: linear-gradient(to right, rgba(255, 255, 255, 0.03) 1px, transparent 1px),
                              linear-gradient(to bottom, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
            
            /* Only fade the GRID, not the content */
            mask-image: linear-gradient(to bottom, black 40%, transparent 100%);
            -webkit-mask-image: linear-gradient(to bottom, black 40%, transparent 100%);
        }
        
        /* Ensure content sits on top */
        .content-layer {
            position: relative;
            z-index: 10;
        }
    """)
)

app, rt = fast_app(hdrs=headers, live=True, pico=False)

@rt("/")
def get():
    resume = load_resume()

    return (
        Title(f"{resume.get('name', 'Nolan Fox')} - {resume.get('title', 'Data Scientist')}"),
        Body(
            # LAYER 1: The Fixed Background Grid
            Div(cls="fixed-grid-background"),

            # LAYER 2: The Actual Content
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

# CRITICAL FIX FOR VERCEL:
# Only run the server if this file is run directly (locally).
# Vercel imports 'app' and skips this block.
if __name__ == "__main__":
    serve(port=5003)