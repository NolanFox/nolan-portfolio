from pathlib import Path
import yaml
from fasthtml.common import *
from components import PageFooter, PageHeader, Hero, ProjectsSection, ResumeSection

def load_resume():
    resume_path = Path(__file__).parent / "data" / "resume.yaml"
    with open(resume_path) as f:
        return yaml.safe_load(f)

# V2 Design: Dark Mode + Cyber Grid
headers = (
    Script(src="https://cdn.tailwindcss.com"),
    Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap"),
    Style("""
        body { font-family: 'Inter', sans-serif; background-color: #020617; color: #e2e8f0; }
        .mono { font-family: 'JetBrains Mono', monospace; }
        
        /* The Cyber-Grid Background */
        .bg-grid {
            background-size: 40px 40px;
            background-image: linear-gradient(to right, rgba(255, 255, 255, 0.03) 1px, transparent 1px),
                              linear-gradient(to bottom, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
            mask-image: linear-gradient(to bottom, black 40%, transparent 100%);
        }
    """)
)

app, rt = fast_app(hdrs=headers, live=True)

@rt("/")
def get():
    resume = load_resume()

    return (
        Title(f"{resume['name']} - {resume['title']}"),
        Body(
            PageHeader(),
            Main(
                Hero(
                    name=resume["name"],
                    title=resume["title"],
                    summary=resume["summary"],
                ),
                ResumeSection(resume),
                # Pull projects from YAML, default to empty list if missing
                ProjectsSection(resume.get("projects", [])),
                cls="max-w-7xl mx-auto w-full"
            ),
            PageFooter(
                email=resume.get("email"),
                github="nolanandrewfox", 
                linkedin=None 
            ),
            # Dark Mode Classes
            cls="bg-slate-950 text-slate-100 bg-grid min-h-screen",
        ),
    )

serve()