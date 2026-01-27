# NOTE: We avoid 'from fasthtml.common import *' because it imports the Database (APSW)
# which crashes on Vercel. We import only what we need for a static site.
from fasthtml.core import FastHTML
from fasthtml.components import *
from fasthtml.xtend import Script, Link, Style, Title, Body, Main, Div, Nav, Header, Footer, A, P, H1, H2, H3, Span, Ul, Li, Section
import yaml
from pathlib import Path
import uvicorn

# --- DATA LOADER ---
def load_resume():
    try:
        base_dir = Path(__file__).resolve().parent
        yaml_path = base_dir / "data" / "resume.yaml"
        with open(yaml_path, "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading resume: {e}")
        return {"name": "Nolan Fox", "title": "Portfolio", "projects": []}

# --- COMPONENT DEFINITIONS ---
# (Re-defining these here ensures we don't rely on broken imports)

def PageHeader():
    return Header(
        Nav(
            Div(
                A("NF", href="/", cls="text-xl font-bold text-white hover:text-emerald-400 transition-colors tracking-tight"),
                cls="flex items-center",
            ),
            Div(
                A("About", href="#about", cls="text-slate-400 hover:text-white transition-colors text-sm font-medium"),
                A("Resume", href="#resume", cls="text-slate-400 hover:text-white transition-colors text-sm font-medium"),
                A("Projects", href="#projects", cls="text-slate-400 hover:text-white transition-colors text-sm font-medium"),
                A("Contact", href="#contact", cls="text-slate-400 hover:text-white transition-colors text-sm font-medium"),
                cls="flex items-center space-x-8",
            ),
            cls="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center",
        ),
        cls="fixed top-0 left-0 right-0 bg-slate-950/80 backdrop-blur-md border-b border-slate-800/60 z-50",
    )

def Hero(name, title, summary):
    return Section(
        Div(
            H1(name, cls="text-5xl lg:text-7xl font-bold tracking-tight text-white mb-6"),
            P(title, cls="text-xl text-emerald-400 font-mono mb-8"),
            P(summary, cls="text-slate-400 leading-relaxed max-w-2xl text-lg"),
            Div(
                A("View Resume", href="#resume", cls="bg-white text-slate-950 px-6 py-2 rounded font-medium hover:bg-emerald-400 transition-colors mr-4"),
                A("See Projects", href="#projects", cls="border border-slate-700 text-slate-300 px-6 py-2 rounded font-medium hover:border-slate-500 transition-colors"),
                cls="mt-8 flex"
            ),
            cls="max-w-3xl mx-auto px-6"
        ),
        id="about",
        cls="py-24 lg:py-32 border-b border-slate-800/60"
    )

def ExperienceItem(exp: dict):
    title = exp.get("position", exp.get("title", "Role"))
    company = exp.get("company", "Company")
    start = exp.get("startDate", exp.get("start_date", ""))
    end = exp.get("endDate", exp.get("end_date", ""))
    highlights = exp.get("highlights", [])

    return Div(
        Div(
            Div(
                Div(cls="absolute left-[-5px] top-2 h-2.5 w-2.5 rounded-full bg-emerald-500 ring-4 ring-slate-950"),
                cls="absolute left-0 top-0 bottom-0 w-px bg-slate-800"
            ),
            Div(
                Div(
                    H3(company, cls="text-lg font-bold text-slate-100"),
                    Span(f"{start} — {end}", cls="text-xs text-slate-500 font-mono"),
                    cls="flex justify-between items-baseline mb-1"
                ),
                P(title, cls="text-sm text-emerald-400 font-medium mb-3"),
                Ul(
                    *[Li(h, cls="text-slate-400 text-sm mb-2 leading-relaxed") for h in highlights],
                    cls="list-disc list-outside ml-4 space-y-1"
                ),
                cls="ml-8 pb-12"
            ),
            cls="relative"
        )
    )

def EducationItem(edu: dict):
    degree = edu.get("degree", edu.get("area", "Degree"))
    institution = edu.get("institution", "University")
    date = edu.get("endDate", edu.get("graduation_date", ""))
    
    return Div(
        Div(
            Div(cls="absolute left-[-5px] top-2 h-2.5 w-2.5 rounded-full bg-slate-700 ring-4 ring-slate-950"),
            cls="absolute left-0 top-0 bottom-0 w-px bg-slate-800"
        ),
        Div(
            Div(
                H3(institution, cls="text-lg font-bold text-slate-100"),
                Span(date, cls="text-xs text-slate-500 font-mono"),
                cls="flex justify-between items-baseline mb-1"
            ),
            P(degree, cls="text-sm text-slate-400 font-medium mb-3"),
            cls="ml-8 pb-8"
        ),
        cls="relative"
    )

def SkillsSection(skills_list: list):
    if not skills_list: return Div()
    return Div(
        *[Div(P(s, cls="text-xs text-emerald-400 bg-emerald-950/30 border border-emerald-900 px-3 py-1 rounded font-mono")) for s in skills_list],
        cls="flex flex-wrap gap-2"
    )

def ResumeSection(resume_data: dict):
    experience_list = resume_data.get("work", resume_data.get("experience", []))
    return Section(
        Div(
            H2("Experience Log", cls="text-xs font-bold tracking-widest text-slate-500 uppercase mb-8"),
            Div(*[ExperienceItem(exp) for exp in experience_list]),
            H2("Education", cls="text-xs font-bold tracking-widest text-slate-500 uppercase mb-8 mt-4"),
            Div(*[EducationItem(edu) for edu in resume_data.get("education", [])]),
            H2("Capabilities", cls="text-xs font-bold tracking-widest text-slate-500 uppercase mb-8 mt-4"),
            SkillsSection(resume_data.get("skills", [])),
            cls="max-w-3xl mx-auto px-6"
        ),
        id="resume",
        cls="py-20"
    )

def ProjectCard(title, description, tags, status, link):
    tags = tags or []
    status_badge = None
    if status:
        status_colors = {
            "In Progress": "text-amber-300 border-amber-500/30 bg-amber-900/20",
            "Completed": "text-emerald-300 border-emerald-500/30 bg-emerald-900/20",
            "Planned": "text-gray-400 border-gray-700 bg-gray-800/50",
        }
        color_cls = status_colors.get(status, "text-gray-400 border-gray-700 bg-gray-800/50")
        status_badge = Span(status, cls=f"text-[10px] uppercase tracking-wider px-2 py-0.5 rounded border {color_cls}")

    card_content = Div(
        Div(H3(title, cls="text-lg font-bold text-white"), status_badge, cls="flex items-center justify-between gap-2 mb-3"),
        P(description, cls="text-gray-300 text-sm leading-relaxed mb-6"),
        Div(*[Span(f"#{tag}", cls="text-xs text-gray-500 mr-3 font-mono") for tag in tags], cls="flex flex-wrap mt-auto pt-4 border-t border-gray-800") if tags else None,
        cls="p-6 flex flex-col h-full",
    )
    card_cls = "block bg-slate-900/40 border border-gray-800 rounded-lg hover:border-gray-600 hover:bg-slate-900/80 transition-all duration-300 h-full"
    if link: return A(card_content, href=link, cls=card_cls)
    return Div(card_content, cls=card_cls)

def ProjectsSection(projects: list[dict]):
    return Section(
        Div(
            H2("Projects", cls="text-xs font-bold tracking-widest text-gray-400 uppercase mb-8"),
            P("A selection of systems I've architected.", cls="text-gray-300 mb-8"),
            Div(*[ProjectCard(title=p.get("title", ""), description=p.get("description", ""), tags=p.get("tags", []), status=p.get("status"), link=p.get("link")) for p in projects], cls="grid grid-cols-1 md:grid-cols-2 gap-6"),
            cls="max-w-3xl mx-auto px-6",
        ),
        id="projects",
        cls="py-24 border-t border-gray-800",
    )

def PageFooter(email, github, linkedin):
    links = []
    link_cls = "text-gray-300 hover:text-white transition-colors text-sm font-medium"
    if github: links.append(A("GitHub", href=f"https://github.com/{github}" if "github.com" not in github else github, target="_blank", cls=link_cls))
    if linkedin: links.append(A("LinkedIn", href=linkedin, target="_blank", cls=link_cls))
    if email: links.append(A("Email", href=f"mailto:{email}", cls=link_cls))

    return Footer(
        Div(
            Div(Div(*links, cls="flex gap-6 justify-center md:justify-start mb-8") if links else None, P("© 2026 Nolan Fox. Built with FastHTML.", cls="text-gray-500 text-xs"), cls="flex flex-col items-center md:items-start"),
            cls="max-w-7xl mx-auto px-6 py-16",
        ),
        id="contact",
        cls="border-t border-gray-800 bg-slate-950",
    )

# --- APP CONFIGURATION ---
headers = (
    Script(src="https://cdn.tailwindcss.com"),
    Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap"),
    Style("""
        html, body { background-color: #020617 !important; color: #f8fafc; font-family: 'Inter', sans-serif; min-height: 100vh; }
        p, span, div, a, li, h1, h2, h3, h4, h5, h6 { opacity: 1 !important; }
        .mono { font-family: 'JetBrains Mono', monospace; }
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

# NOTE: We use FastHTML() directly instead of fast_app(). 
# This bypasses the Database creation that was crashing Vercel.
app = FastHTML(hdrs=headers, live=False)
rt = app.route

@rt("/")
def get():
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

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5003, reload=True)