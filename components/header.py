from fasthtml.common import *

def PageHeader():
    return Header(
        Nav(
            Div(
                A(
                    "NF",
                    href="/",
                    cls="text-xl font-bold text-white hover:text-emerald-400 transition-colors tracking-tight",
                ),
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