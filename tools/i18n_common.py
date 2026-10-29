# -*- coding: utf-8 -*-
"""Shared i18n helpers: locales, paths, nav, footer, hreflang, lang switcher."""
from __future__ import annotations
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://chongzhi.chatgpt-plus.top"

# (code, url_prefix, html_lang, label)
LOCALES = [
    ("zh", "", "zh-CN", "简体中文"),
    ("en", "/en", "en", "English"),
    ("zh-tw", "/zh-tw", "zh-TW", "繁體中文"),
    ("ja", "/ja", "ja", "日本語"),
    ("ko", "/ko", "ko", "한국어"),
    ("es", "/es", "es", "Español"),
    ("ru", "/ru", "ru", "Русский"),
]

PAGES = ["", "gemini/", "grok/", "claude/", "faq/", "check/", "support/"]
PAGE_KEYS = ["home", "gemini", "grok", "claude", "faq", "check", "support"]

CHEVRON = (
    '<svg class="nav-chevron" width="10" height="6" viewBox="0 0 10 6" fill="none" aria-hidden="true">'
    '<path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.5" '
    'stroke-linecap="round" stroke-linejoin="round"/></svg>'
)

ICON = {
    "openai": '/assets/icons/openai-mark.svg?v=4',
    "gemini": '/assets/icons/gemini-mark.svg?v=1',
    "grok": '/assets/icons/grok-mark.svg?v=1',
    "claude": '/assets/icons/claude-mark.svg?v=1',
}


def locale_by_code(code: str):
    for loc in LOCALES:
        if loc[0] == code:
            return loc
    raise KeyError(code)


def page_url(prefix: str, page: str) -> str:
    """page is '' or 'gemini/' etc. Returns site path starting with /."""
    if not prefix:
        return "/" if page == "" else f"/{page}"
    if page == "":
        return f"{prefix}/"
    return f"{prefix}/{page}"


def abs_url(prefix: str, page: str) -> str:
    path = page_url(prefix, page)
    if path == "/":
        return f"{SITE}/"
    return f"{SITE}{path}"


def hreflang_links(page: str) -> str:
    lines = []
    for code, prefix, html_lang, _ in LOCALES:
        href = abs_url(prefix, page)
        lines.append(f'    <link rel="alternate" hreflang="{html_lang}" href="{href}">')
    lines.append(f'    <link rel="alternate" hreflang="x-default" href="{abs_url("", page)}">')
    return "\n".join(lines)


def lang_switcher(code: str, page: str) -> str:
    _, _, _, cur_label = locale_by_code(code)
    items = []
    for c, prefix, _, label in LOCALES:
        href = page_url(prefix, page)
        active = " active" if c == code else ""
        items.append(
            f'                        <a href="{href}" class="nav-dropdown-item{active}" role="menuitem">{label}</a>'
        )
    return f"""                <div class="nav-dropdown nav-lang">
                    <button type="button" class="nav-tab nav-dropdown-toggle" aria-expanded="false" aria-haspopup="true" aria-label="Language">
                        {cur_label} {CHEVRON}
                    </button>
                    <div class="nav-dropdown-menu" role="menu">
{chr(10).join(items)}
                    </div>
                </div>"""


def head_common(title: str, desc: str, html_lang: str, page: str, keywords: str = "") -> str:
    kw = f'\n    <meta name="keywords" content="{keywords}">' if keywords else ""
    return f"""<!DOCTYPE html>
<html lang="{html_lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">{kw}
    <link rel="stylesheet" href="/style.css">
    <link rel="icon" href="/assets/icons/favicon.svg" type="image/svg+xml">
    <link rel="icon" href="/assets/icons/favicon.ico" sizes="any">
    <link rel="apple-touch-icon" href="/assets/icons/apple-touch-icon.png">
    <meta name="theme-color" content="#17201A">
    <meta property="og:image" content="https://chongzhi.chatgpt-plus.top/assets/icons/og-icon.png">
{hreflang_links(page)}
</head>"""


def nav_html(code: str, page: str, t: dict, active: str, cta_href: str, cta_label: str) -> str:
    """active: home|gemini|grok|claude|tools|help|faq|check|support"""
    prefix = locale_by_code(code)[1]
    p = lambda slug: page_url(prefix, slug)

    def tab(slug, label, icon_key, key):
        cls = "nav-tab active" if active == key else "nav-tab"
        icon = f'<img class="nav-ai-icon" src="{ICON[icon_key]}" width="16" height="16" alt="" aria-hidden="true">'
        return f'<a href="{p(slug)}" class="{cls}">{icon}{label}</a>'

    tools_active = " active" if active in ("tools", "check") else ""
    help_active = " active" if active in ("help", "faq", "support") else ""
    check_active = " active" if active == "check" else ""
    faq_active = " active" if active == "faq" else ""
    support_active = " active" if active == "support" else ""

    logo_sub = t.get("logo_sub", t.get("logo_sub_default", ""))
    return f"""    <nav class="navbar">
        <div class="navbar-container">
            <a href="{p('')}" class="navbar-logo">
                <span class="logo-icon">G</span>
                <span class="logo-text">{t['brand']}<span class="logo-sub">{logo_sub}</span></span>
            </a>
            <div class="navbar-links">
                {tab('', 'ChatGPT Plus', 'openai', 'home')}
                {tab('gemini/', 'Gemini', 'gemini', 'gemini')}
                {tab('grok/', 'Grok', 'grok', 'grok')}
                {tab('claude/', 'Claude', 'claude', 'claude')}
                <div class="nav-dropdown">
                    <button type="button" class="nav-tab nav-dropdown-toggle{tools_active}" aria-expanded="false" aria-haspopup="true">
                        {t['nav_tools']} {CHEVRON}
                    </button>
                    <div class="nav-dropdown-menu" role="menu">
                        <a href="{p('check/')}" class="nav-dropdown-item{check_active}" role="menuitem">{t['nav_check']}</a>
                        <a class="nav-dropdown-item" href="https://codexinstall.asia/zh/codex-reset/" target="_blank" rel="noopener noreferrer" role="menuitem">{t['nav_radar']}</a>
                        <a href="/download-codex/" class="nav-dropdown-item" role="menuitem">{t['nav_codex']}</a>
                    </div>
                </div>
                <div class="nav-dropdown">
                    <button type="button" class="nav-tab nav-dropdown-toggle{help_active}" aria-expanded="false" aria-haspopup="true">
                        {t['nav_help']} {CHEVRON}
                    </button>
                    <div class="nav-dropdown-menu" role="menu">
                        <a href="{p('faq/')}" class="nav-dropdown-item{faq_active}" role="menuitem">{t['nav_faq']}</a>
                        <a href="{p('support/')}" class="nav-dropdown-item{support_active}" role="menuitem">{t['nav_support']}</a>
                    </div>
                </div>
{lang_switcher(code, page)}
            </div>
            <a href="{cta_href}" class="navbar-cta"{' target="_blank" rel="noopener noreferrer"' if cta_href.startswith('http') else ''}>{cta_label}</a>
            <button class="mobile-menu-btn" id="mobile-menu-btn" aria-label="{t.get('menu', 'Menu')}">
                <span></span><span></span><span></span>
            </button>
        </div>
    </nav>"""


def footer_html(code: str, t: dict) -> str:
    prefix = locale_by_code(code)[1]
    p = lambda slug: page_url(prefix, slug)
    return f"""    <footer class="footer">
        <div class="footer-container">
            <div class="footer-top">
                <div class="footer-brand">
                    <div class="footer-logo">
                        <span class="logo-icon">G</span>
                        <span>{t['brand']}</span>
                    </div>
                    <p>{t['footer_tagline']}</p>
                </div>
                <div class="footer-links">
                    <div class="footer-col">
                        <h4>{t['footer_services']}</h4>
                        <a href="{p('')}">{t['footer_chatgpt']}</a>
                        <a href="{p('gemini/')}">{t['footer_gemini']}</a>
                        <a href="{p('grok/')}">{t['footer_grok']}</a>
                        <a href="{p('claude/')}">{t['footer_claude']}</a>
                    </div>
                    <div class="footer-col">
                        <h4>{t['footer_help']}</h4>
                        <a href="{p('check/')}">{t['footer_check']}</a>
                        <a href="https://codexinstall.asia/zh/codex-reset/" target="_blank" rel="noopener noreferrer">{t['footer_radar']}</a>
                        <a href="/download-codex/">{t['footer_codex']}</a>
                        <a href="{p('faq/')}">{t['footer_faq']}</a>
                        <a href="{p('support/')}">{t['footer_support']}</a>
                    </div>
                    <div class="footer-col">
                        <h4>{t['footer_contact']}</h4>
                        <p>QQ: 1002569303</p>
                        <p>{t['footer_hours']}</p>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024-2026 {t['brand']}. All rights reserved.</p>
            </div>
        </div>
    </footer>"""


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}")
