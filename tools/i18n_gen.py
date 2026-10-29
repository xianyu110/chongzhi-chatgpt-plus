# -*- coding: utf-8 -*-
"""Generate localized pages + sitemap; patch Chinese pages with lang switcher."""
from __future__ import annotations
import re
from pathlib import Path
from i18n_common import (
    ROOT, LOCALES, PAGES, SITE, write, lang_switcher, hreflang_links, abs_url, page_url
)
from i18n_pages_home import build_home
from i18n_pages_product import build_gemini, build_grok, build_claude
from i18n_pages_help import build_faq, build_check, build_support

BUILDERS = {
    "": build_home,
    "gemini/": build_gemini,
    "grok/": build_grok,
    "claude/": build_claude,
    "faq/": build_faq,
    "check/": build_check,
    "support/": build_support,
}

NON_ZH = [c for c, *_ in LOCALES if c != "zh"]

LANG_SWITCHER_ZH = lang_switcher("zh", "{PAGE}")  # placeholder replaced per page

CHEVRON = (
    '<svg class="nav-chevron" width="10" height="6" viewBox="0 0 10 6" fill="none" aria-hidden="true">'
    '<path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.5" '
    'stroke-linecap="round" stroke-linejoin="round"/></svg>'
)


def gen_locales():
    for code in NON_ZH:
        prefix = next(p for c, p, *_ in LOCALES if c == code)
        for page, builder in BUILDERS.items():
            html = builder(code)
            if page == "":
                out = ROOT / prefix.strip("/") / "index.html" if prefix else ROOT / "index.html"
                # prefix is like /en → en/index.html
                out = ROOT / prefix.lstrip("/") / "index.html"
            else:
                out = ROOT / prefix.lstrip("/") / page / "index.html"
            write(out, html)


def patch_zh_pages():
    """Add hreflang + language dropdown to Chinese root pages."""
    mapping = {
        ROOT / "index.html": "",
        ROOT / "gemini" / "index.html": "gemini/",
        ROOT / "grok" / "index.html": "grok/",
        ROOT / "claude" / "index.html": "claude/",
        ROOT / "faq" / "index.html": "faq/",
        ROOT / "check" / "index.html": "check/",
        ROOT / "support" / "index.html": "support/",
    }
    for path, page in mapping.items():
        if not path.exists():
            print(f"skip missing {path}")
            continue
        text = path.read_text(encoding="utf-8")
        # Insert hreflang before </head>
        if 'hreflang=' not in text:
            links = hreflang_links(page)
            text = text.replace("</head>", links + "\n</head>", 1)
        switcher = lang_switcher("zh", page)
        # Replace bare EN tab if present
        text2, n = re.subn(
            r'\s*<a href="/en/" class="nav-tab">EN</a>\s*',
            "\n" + switcher + "\n",
            text,
            count=1,
        )
        if n:
            text = text2
        elif 'nav-lang' not in text:
            # Insert before closing </div> of navbar-links — after last help dropdown
            # Find the help dropdown end then insert
            marker = None
            # Prefer insert before </div>\n            <a href=...navbar-cta
            m = re.search(
                r'(</div>\s*</div>\s*)(<a href="[^"]*" class="navbar-cta")',
                text,
            )
            if m:
                text = text[: m.start()] + m.group(1) + switcher + "\n            " + m.group(2) + text[m.end() :]
            else:
                # fallback: before mobile-menu or navbar-cta
                m2 = re.search(r'(\s*)(<a href="[^"]*" class="navbar-cta")', text)
                if m2:
                    text = text[: m2.start()] + "\n" + switcher + "\n" + m2.group(0) + text[m2.end() :]
                else:
                    print(f"WARN: could not insert switcher into {path}")
        path.write_text(text, encoding="utf-8")
        print(f"patched {path.relative_to(ROOT)}")


def write_sitemap():
    urls = []
    for code, prefix, *_ in LOCALES:
        for page in PAGES:
            loc = abs_url(prefix, page)
            urls.append(f"""  <url>
    <loc>{loc}</loc>
    <changefreq>weekly</changefreq>
    <priority>{"1.0" if page == "" and code == "zh" else "0.8"}</priority>
  </url>""")
    # Optional Chinese-only pages
    for extra in ["download-codex/", "blog/"]:
        urls.append(f"""  <url>
    <loc>{SITE}/{extra}</loc>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>""")
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    write(ROOT / "sitemap.xml", xml)


def main():
    gen_locales()
    patch_zh_pages()
    write_sitemap()
    print("done")


if __name__ == "__main__":
    main()
