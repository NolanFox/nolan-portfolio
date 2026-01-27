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
        status_colors = {
            "In Progress": "bg-amber-100 text-amber-800",
            "Completed": "bg-green-100 text-green-800",
            "Planned": "bg-zinc-100 text-zinc-600",
        }
        color_cls = status_colors.get(status, "bg-zinc-100 text-zinc-600")
        status_badge = Span(
            status,
            cls=f"text-xs px-2 py-1 rounded-full {color_cls}",
        )

    card_content = Div(
        Div(
            H3(title, cls="text-lg font-semibold text-zinc-900"),
            status_badge,
            cls="flex items-center justify-between gap-2",
        ),
        P(description, cls="text-zinc-600 mt-2 text-sm leading-relaxed"),
        Div(
            *[
                Span(tag, cls="text-xs px-2 py-1 bg-zinc-100 text-zinc-600 rounded")
                for tag in tags
            ],
            cls="flex flex-wrap gap-2 mt-4",
        ) if tags else None,
        cls="p-6",
    )

    if link:
        return A(
            card_content,
            href=link,
            cls="block bg-white border border-zinc-200 rounded-xl hover:border-zinc-300 hover:shadow-md transition-all",
        )

    return Div(
        card_content,
        cls="bg-white border border-zinc-200 rounded-xl",
    )


def ProjectsSection(projects: list[dict]):
    return Section(
        Div(
            H2(
                "Projects",
                cls="text-3xl font-bold text-zinc-900 mb-2",
            ),
            P(
                "A selection of things I've built",
                cls="text-zinc-500 mb-12",
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
            cls="max-w-5xl mx-auto px-6",
        ),
        id="projects",
        cls="py-24 bg-zinc-50",
    )
