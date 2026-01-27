from fasthtml.common import *

def ExperienceItem(exp: dict):
    # Robustly get fields, handling "position" vs "title" and "work" vs "experience"
    title = exp.get("position", exp.get("title", "Role"))
    company = exp.get("company", "Company")
    start = exp.get("startDate", exp.get("start_date", ""))
    end = exp.get("endDate", exp.get("end_date", ""))
    highlights = exp.get("highlights", [])

    return Div(
        Div(
            # Timeline Dot & Line
            Div(
                Div(cls="absolute left-[-5px] top-2 h-2.5 w-2.5 rounded-full bg-emerald-500 ring-4 ring-slate-950"),
                cls="absolute left-0 top-0 bottom-0 w-px bg-slate-800"
            ),
            # Content
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
    # Robustly get fields
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
    # Handle "work" vs "experience" key mismatch
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