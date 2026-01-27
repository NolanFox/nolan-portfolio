from fasthtml.common import *


def PageFooter(email: str = None, github: str = None, linkedin: str = None):
    links = []

    if github:
        links.append(
            A(
                "GitHub",
                href=f"https://{github}" if not github.startswith("http") else github,
                target="_blank",
                cls="text-zinc-500 hover:text-zinc-900 transition-colors",
            )
        )

    if linkedin:
        links.append(
            A(
                "LinkedIn",
                href=f"https://{linkedin}" if not linkedin.startswith("http") else linkedin,
                target="_blank",
                cls="text-zinc-500 hover:text-zinc-900 transition-colors",
            )
        )

    if email:
        links.append(
            A(
                "Email",
                href=f"mailto:{email}",
                cls="text-zinc-500 hover:text-zinc-900 transition-colors",
            )
        )

    return Footer(
        Div(
            Div(
                Div(
                    H3("Get in Touch", cls="text-lg font-semibold text-zinc-900 mb-2"),
                    P(
                        "Interested in working together? Let's connect.",
                        cls="text-zinc-600",
                    ),
                    A(
                        email,
                        href=f"mailto:{email}",
                        cls="text-zinc-900 hover:text-zinc-600 transition-colors mt-2 inline-block",
                    ) if email else None,
                    cls="mb-8",
                ),
                Div(
                    *links,
                    cls="flex gap-6 mb-8",
                ) if links else None,
                Div(
                    P(
                        "© 2025 Nolan Fox. Built with FastHTML.",
                        cls="text-zinc-400 text-sm",
                    ),
                ),
                cls="text-center",
            ),
            cls="max-w-5xl mx-auto px-6 py-16",
        ),
        id="contact",
        cls="border-t border-zinc-100",
    )
