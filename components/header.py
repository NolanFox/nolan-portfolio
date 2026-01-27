from fasthtml.common import *


def PageHeader():
    return Header(
        Nav(
            Div(
                A(
                    "NF",
                    href="/",
                    cls="text-xl font-bold text-zinc-900 hover:text-zinc-600 transition-colors",
                ),
                cls="flex items-center",
            ),
            Div(
                A("About", href="#about", cls="text-zinc-600 hover:text-zinc-900 transition-colors"),
                A("Resume", href="#resume", cls="text-zinc-600 hover:text-zinc-900 transition-colors"),
                A("Projects", href="#projects", cls="text-zinc-600 hover:text-zinc-900 transition-colors"),
                A("Contact", href="#contact", cls="text-zinc-600 hover:text-zinc-900 transition-colors"),
                cls="flex items-center space-x-8",
            ),
            cls="max-w-5xl mx-auto px-6 py-4 flex justify-between items-center",
        ),
        cls="fixed top-0 left-0 right-0 bg-white/80 backdrop-blur-sm border-b border-zinc-100 z-50",
    )
