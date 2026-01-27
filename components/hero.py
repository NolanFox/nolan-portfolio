from fasthtml.common import *

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