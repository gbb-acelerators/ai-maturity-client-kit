"""paulasilva-ms branding constants and helpers.

Shared by all scripts that generate output (PDFs, reports, JSONs, MD).
Single source of truth for identity strings, palette, and footer markup.

See referencia/branding/IDENTITY.md and referencia/branding/VOICE.md.
"""

# ============================================================
# Identity strings (canonical, never modify)
# ============================================================

AUTHOR = "Paula Silva"
ROLE = "Global Developer Solutions Advisor"
ROLE_FULL = "Paula Silva, Global Developer Solutions Advisor"
META_BAR = "Paula Silva | Global Developer Solutions Advisor"
CONTACT = "paulasilva@microsoft.com"
TAGLINE = "Building the future of software development with AI and Agentic DevOps"

# ============================================================
# Microsoft 4-color palette (logo, accent)
# ============================================================

MS_BLUE = "#00A4EF"
MS_GREEN = "#7FBA00"
MS_YELLOW = "#FFB900"
MS_RED = "#F25022"

PALETTE = {
    "primary": MS_BLUE,
    "positive": MS_GREEN,
    "warn": MS_YELLOW,
    "critical": MS_RED,
}

# ============================================================
# Output helpers
# ============================================================

DESIGN_SYSTEM = "paulasilva-ms Design System v1.7.0"


def md_header() -> str:
    """HTML comment with paulasilva-ms identity (top of generated .md files)."""
    return (
        f"<!-- paulasilva-ms identity: {META_BAR} · {CONTACT} -->\n"
        f"<!-- {DESIGN_SYSTEM} -->\n"
    )


FOOTER_IDENTITY = {
    "en": "Visual identity: {ds} · see `referencia/branding/`",
    "pt-br": "Identidade visual: {ds} · ver `referencia/branding/`",
}


def md_footer(lang: str = "pt-br") -> str:
    """Markdown footer with Paula Silva attribution (bottom of generated .md files)."""
    identity = FOOTER_IDENTITY.get(lang, FOOTER_IDENTITY["en"])
    return (
        "\n\n---\n\n"
        f"<sub>**{AUTHOR}** | {ROLE} · {CONTACT}</sub>  \n"
        f"<sub>{TAGLINE}</sub>  \n"
        f"<sub>{identity.format(ds=DESIGN_SYSTEM)}</sub>\n"
    )


def json_metadata() -> dict:
    """Branding metadata to inject into generated JSON files."""
    return {
        "branding": {
            "design_system": DESIGN_SYSTEM,
            "author": AUTHOR,
            "role": ROLE,
            "contact": CONTACT,
            "tagline": TAGLINE,
            "palette": PALETTE,
        }
    }


def payload_branding_block() -> dict:
    """Branding block for the Jinja2 PDF payload (consumed by templates)."""
    return {
        "name": META_BAR,
        "author": AUTHOR,
        "role": ROLE,
        "contact": CONTACT,
        "tagline": TAGLINE,
        "design_system": DESIGN_SYSTEM,
        "palette": PALETTE,
    }
