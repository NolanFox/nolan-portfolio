from fasthtml.common import *

def PageFooter(email: str = None, github: str = None, linkedin: str = None):
    links = []
    # FIX: Bright text (Gray-300) so it stands out against black
    link_cls = "text-gray-300 hover:text-white transition-colors text-sm font-medium"

    if github:
        links.append(A("GitHub", href=f"https://github.com/{github}" if "github.com" not in github else github, target="_blank", cls=link_cls))

    if linkedin:
        links.append(A("LinkedIn", href=linkedin, target="_blank", cls=link_cls))

    if email:
        links.append(A("Email", href=f"mailto:{email}", cls=link_cls))

    return Footer(
        Div(
            Div(
                Div(
                    # FIX: White Text for Header
                    H3("End of Log", cls="text-sm font-bold text-white uppercase tracking-widest mb-4"),
                    # FIX: Light Gray for subtext
                    P("Every claim in this portfolio is backed by evidence.", cls="text-gray-400 text-sm mb-8"),
                ),
                Div(*links, cls="flex gap-6 justify-center md:justify-start mb-8") if links else None,
                P("© 2026 Nolan Fox. Built with FastHTML.", cls="text-gray-500 text-xs"),
                cls="flex flex-col items-center md:items-start",
            ),
            cls="max-w-7xl mx-auto px-6 py-16",
        ),
        id="contact",
        # FIX: Ensure background is dark but border is visible
        cls="border-t border-gray-800 bg-slate-950",
    )