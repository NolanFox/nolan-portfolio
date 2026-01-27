from fasthtml.common import *

def ProjectCard(
    title: str,
    description: str,
    tags: list[str] = None,
    status: str = None,
    link: str = None,
):
    tags = tags or []

    status_badge = None
    if status:
        # High Contrast Status Colors
        status_colors = {
            "In Progress": "text-amber-300 border-amber-500/30 bg-amber-900/20",
            "Completed": "text-emerald-300 border-emerald-500/30 bg-emerald-900/20",
            "Planned": "text-gray-400 border-gray-700 bg-gray-800/50",
        }
        color_cls = status_colors.get(status, "text-gray-400 border-gray-700 bg-gray-800/50")
        
        status_badge = Span(
            status,
            cls=f"text-[10px] uppercase tracking-wider px-2 py-0.5 rounded border {color_cls}",
        )

    card_content = Div(
        Div(
            # FIX: White Title
            H3(title, cls="text-lg font-bold text-white"),
            status_badge,
            cls="flex items-center justify-between gap-2 mb-3",
        ),
        # FIX: Light Gray Description (Readable)
        P(description, cls="text-gray-300 text-sm leading-relaxed mb-6"),
        Div(
            *[
                Span(f"#{tag}", cls="text-xs text-gray-500 mr-3 font-mono")
                for tag in tags
            ],
            cls="flex flex-wrap mt-auto pt-4 border-t border-gray-800",
        ) if tags else None,
        cls="p-6 flex flex-col h-full",
    )

    # Hover Effects
    card_cls = "block bg-slate-900/40 border border-gray-800 rounded-lg hover:border-gray-600 hover:bg-slate-900/80 transition-all duration-300 h-full"

    if link:
        return A(card_content, href=link, cls=card_cls)

    return Div(card_content, cls=card_cls)


def ProjectsSection(projects: list[dict]):
    return Section(
        Div(
            # FIX: White Header
            H2(
                "Projects",
                cls="text-xs font-bold tracking-widest text-gray-400 uppercase mb-8",
            ),
            P(
                "A selection of systems I've architected.",
                cls="text-gray-300 mb-8",
            ),
            Div(
                *[
                    ProjectCard(
                        title=p.get("title", ""),
                        description=p.get("description", ""),
                        tags=p.get("tags", []),
                        status=p.get("status"),
                        link=p.get("link"),
                    )
                    for p in projects
                ],
                cls="grid grid-cols-1 md:grid-cols-2 gap-6",
            ),
            cls="max-w-3xl mx-auto px-6",
        ),
        id="projects",
        cls="py-24 border-t border-gray-800",
    )