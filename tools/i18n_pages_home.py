# -*- coding: utf-8 -*-
"""ChatGPT Plus home page builders for non-zh locales."""
import json
from pathlib import Path
from i18n_common import head_common, nav_html, footer_html, ICON, locale_by_code, page_url
from i18n_ui import UI

HOME = json.loads((Path(__file__).with_name("i18n_home_data.json")).read_text(encoding="utf-8"))

SVG_SHIELD = (
    '<svg viewBox="0 0 24 24" focusable="false">'
    '<path d="M12 3 5 6v5c0 4.5 2.9 8.5 7 10 4.1-1.5 7-5.5 7-10V6l-7-3Z"></path>'
    '<path d="m8.5 12 2.2 2.2 4.8-4.8"></path></svg>'
)
SVG_BOT = (
    '<svg viewBox="0 0 24 24" focusable="false">'
    '<rect x="4" y="7" width="16" height="12" rx="3"></rect>'
    '<path d="M12 3v4M8 12h.01M16 12h.01M8 16h8M2 11v4M22 11v4"></path></svg>'
)
SVG_LOCK = (
    '<svg viewBox="0 0 24 24" focusable="false">'
    '<rect x="4" y="10" width="16" height="11" rx="2"></rect>'
    '<path d="M8 10V7a4 4 0 0 1 8 0v3M12 14v3"></path>'
    '<circle cx="12" cy="14" r="1"></circle></svg>'
)
SVG_BOLT = (
    '<svg viewBox="0 0 24 24" focusable="false">'
    '<path d="m13 2-9 12h7l-1 8 9-12h-7l1-8Z"></path></svg>'
)
SVG_FEATS = [SVG_SHIELD, SVG_BOT, SVG_LOCK, SVG_BOLT]
SVG_WHYS = [
    (
        '<svg viewBox="0 0 24 24" focusable="false">'
        '<circle cx="12" cy="12" r="9"></circle>'
        '<path d="M15 8.5c-.7-.7-1.7-1-3-1-1.7 0-3 .8-3 2s1.3 2 3 2 3 .8 3 2-1.3 2-3 2c-1.3 0-2.3-.3-3-1M12 6v12"></path></svg>'
    ),
    (
        '<svg viewBox="0 0 24 24" focusable="false">'
        '<rect x="3" y="5" width="18" height="14" rx="2"></rect>'
        '<path d="M3 10h18M7 15h3"></path></svg>'
    ),
    SVG_SHIELD,
    (
        '<svg viewBox="0 0 24 24" focusable="false">'
        '<path d="M4 21V5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v16M16 9h2a2 2 0 0 1 2 2v10M2 21h20"></path>'
        '<path d="M8 7h2M12 7h2M8 11h2M12 11h2M8 15h2M12 15h2"></path></svg>'
    ),
]


def _card(name, tier, official, amount, feats, href, g, buy, period, featured=False, accent_tier=False):
    mark = ICON["openai"].replace("?v=4", "?v=3")
    feat_li = "\n".join("                        <li>" + f + "</li>" for f in feats)
    tier_html = ""
    if tier:
        cls = "product-tier accent" if accent_tier else "product-tier"
        tier_html = ' <span class="' + cls + '">' + tier + "</span>"
    feat_cls = " featured" if featured else ""
    return (
        '                <article class="pricing-card' + feat_cls + '">\n'
        '                    <div class="pricing-card-head">\n'
        '                        <div class="pricing-title-row">\n'
        '                            <img class="product-mark" src="' + mark + '" width="28" height="28" alt="" aria-hidden="true">\n'
        '                            <h3><span class="product-name">' + name + "</span>" + tier_html + "</h3>\n"
        '                            <span class="invoice-pill">' + g["invoice"] + "</span>\n"
        "                        </div>\n"
        '                        <div class="product-meta-row">\n'
        "                            <span>" + g["meta_own"] + "</span>\n"
        '                            <span class="official-pill">' + official + "</span>\n"
        '                            <span class="buyable-pill">' + g["buyable"] + "</span>\n"
        "                        </div>\n"
        "                    </div>\n"
        '                    <div class="pricing-price">\n'
        '                        <span class="price-currency">&#165;</span>\n'
        '                        <span class="price-amount">' + amount + "</span>\n"
        '                        <span class="price-period">' + period + "</span>\n"
        "                    </div>\n"
        '                    <ul class="pricing-features">\n'
        + feat_li + "\n"
        "                    </ul>\n"
        '                    <a href="' + href + '" target="_blank" rel="noopener noreferrer" class="btn-primary btn-block">' + buy + "</a>\n"
        '                    <p class="pay-methods-hint">' + g["pay_hint"] + "</p>\n"
        "                </article>"
    )


def build_home(code):
    u = UI[code]
    g = HOME[code]
    t = dict(u)
    t["logo_sub"] = g["logo_sub"]
    _, prefix, html_lang, _ = locale_by_code(code)
    buy = u["buy"]
    period = u["per_month"]
    faq_url = page_url(prefix, "faq/")
    support = page_url(prefix, "support/")

    cards = "\n".join([
        _card("ChatGPT Plus", "", g["official20"], "1XX", g["c1_feats"], "https://wzyp.cn/item/bp1jdo", g, buy, period),
        _card("ChatGPT Pro", "5x", g["official100"], "780.00", g["c2_feats"], "https://momoai.czvip.cn/products/m23", g, buy, period),
        _card("ChatGPT Pro", "20x", g["official200"], "1280.00", g["c3_feats"], "https://momoai.czvip.cn/products/m24", g, buy, period, featured=True, accent_tier=True),
        _card("ChatGPT Pro", "50x", g["official_direct"], "3600.00", g["c4_feats"], "https://momoai.czvip.cn/products/gpt-pro-25x", g, buy, period),
    ])

    trust = "\n".join(
        '            <div class="trust-item">\n'
        '                <div class="trust-icon">' + ic + "</div>\n"
        '                <div class="trust-info">\n'
        "                    <strong>" + title + "</strong>\n"
        "                    <span>" + sub + "</span>\n"
        "                </div>\n"
        "            </div>"
        for ic, title, sub in g["trust"]
    )
    after = "\n".join("                            <li>" + x + "</li>" for x in g["after"])
    icons = ["💳", "📋", "⚡"]
    flow_parts = []
    for i, lab in enumerate(g["flow"]):
        flow_parts.append(
            '                        <div class="pay-process-step">\n'
            '                            <span class="pay-process-icon" aria-hidden="true">' + icons[i] + "</span>\n"
            "                            <span>" + lab + "</span>\n"
            "                        </div>"
        )
        if i < 2:
            flow_parts.append('                        <span class="pay-process-arrow" aria-hidden="true">→</span>')
    feats = "\n".join(
        '                <div class="feature-card">\n'
        '                    <span class="feature-icon" aria-hidden="true">' + SVG_FEATS[i] + "</span>\n"
        "                    <h3>" + title + "</h3>\n"
        "                    <p>" + desc + "</p>\n"
        "                </div>"
        for i, (title, desc) in enumerate(g["feats"])
    )
    whys = "\n".join(
        '                <div class="why-us-card">\n'
        '                    <span class="why-us-icon" aria-hidden="true">' + SVG_WHYS[i] + "</span>\n"
        "                    <h3>" + title + "</h3>\n"
        "                    <p>" + desc + "</p>\n"
        "                </div>"
        for i, (title, desc) in enumerate(g["whys"])
    )
    steps = "\n".join(
        '                <div class="step-card">\n'
        '                    <div class="step-number">' + str(i + 1) + "</div>\n"
        '                    <div class="step-content">\n'
        "                        <h3>" + title + "</h3>\n"
        "                        <p>" + desc + "</p>\n"
        "                    </div>\n"
        '                    <span class="step-check">✓</span>\n'
        "                </div>"
        for i, (title, desc) in enumerate(g["steps"])
    )
    faqs = "\n".join(
        '                <div class="faq-item">\n'
        '                    <button class="faq-question">\n'
        "                        <span>" + q + "</span>\n"
        '                        <span class="faq-arrow">+</span>\n'
        "                    </button>\n"
        '                    <div class="faq-answer"><p>' + a + "</p></div>\n"
        "                </div>"
        for q, a in g["faqs"]
    )

    yen = "&#165;"
    return (
        head_common(g["title"], g["desc"], html_lang, "", g.get("kw", "")) + "\n"
        "<body>\n"
        + nav_html(code, "", t, "home", "#pricing", g["cta"]) + "\n\n"
        '    <div class="container">\n'
        '        <section class="hero">\n'
        '            <div class="hero-badge">' + g["badge"] + "</div>\n"
        '            <h1 class="hero-title">' + g["h1a"] + '<span class="hero-title-accent">' + g["h1b"] + "</span>" + g["h1c"] + "</h1>\n"
        '            <p class="hero-desc">' + g["hero"] + "</p>\n"
        '            <div class="hero-actions">\n'
        '                <a href="https://wzyp.cn/item/bp1jdo" target="_blank" rel="noopener noreferrer" class="btn-primary">' + g["buy_plus"] + "</a>\n"
        '                <a href="https://momoai.czvip.cn/products/m24" target="_blank" rel="noopener noreferrer" class="btn-secondary">' + g["buy_pro"] + "</a>\n"
        '                <a href="' + support + '" class="btn-secondary">' + g["contact"] + "</a>\n"
        "            </div>\n"
        '            <div class="hero-avatars">\n'
        '                <img src="https://api.dicebear.com/7.x/notionists/svg?seed=Alice" alt="" class="avatar">\n'
        '                <img src="https://api.dicebear.com/7.x/notionists/svg?seed=Bob" alt="" class="avatar">\n'
        '                <img src="https://api.dicebear.com/7.x/notionists/svg?seed=Carol" alt="" class="avatar">\n'
        '                <span class="avatar-more">+</span>\n'
        '                <span class="avatar-text">' + g["helped"] + "</span>\n"
        "            </div>\n"
        "        </section>\n\n"
        '        <section class="trust-bar">\n'
        + trust + "\n"
        "        </section>\n\n"
        '        <section class="pricing-section" id="pricing">\n'
        '            <div class="section-header">\n'
        "                <h2>" + g["price_h"] + "</h2>\n"
        "                <p>" + g["price_p"] + "</p>\n"
        "            </div>\n"
        '            <div class="pricing-grid quad">\n'
        + cards + "\n"
        "            </div>\n"
        '            <div class="policy-pay-row">\n'
        '                <div class="policy-block">\n'
        "                    <section>\n"
        '                        <h3 id="aftersale-title">' + g["after_h"] + "</h3>\n"
        '                        <ul class="policy-list">\n'
        + after + "\n"
        "                        </ul>\n"
        "                    </section>\n"
        "                </div>\n"
        '                <div class="pay-process-strip" aria-label="flow">\n'
        '                    <div class="pay-process-steps">\n'
        + "\n".join(flow_parts) + "\n"
        "                    </div>\n"
        '                    <p class="pay-process-payhint">' + g["pay_hint"] + "</p>\n"
        "                </div>\n"
        "            </div>\n\n"
        '            <article class="sms-card" id="jie-ma">\n'
        '                <div class="sms-card-left">\n'
        '                    <div class="sms-card-icon" aria-hidden="true">📱</div>\n'
        '                    <div class="sms-card-copy">\n'
        "                        <h3>" + g["sms_h"] + "</h3>\n"
        '                        <span class="sms-card-tag">' + g["sms_tag"] + "</span>\n"
        '                        <p class="sms-card-desc">' + g["sms_d"] + "</p>\n"
        "                    </div>\n"
        "                </div>\n"
        '                <div class="sms-card-action">\n'
        '                    <div class="sms-card-price">\n'
        '                        <span class="price-currency">' + yen + "</span>\n"
        '                        <span class="price-amount">2.78</span>\n'
        "                    </div>\n"
        '                    <p class="sms-card-price-hint">' + g["sms_hint"] + "</p>\n"
        '                    <a href="https://wzyp.cn/item/8fbduz" target="_blank" rel="noopener noreferrer" class="btn-primary">' + buy + "</a>\n"
        "                </div>\n"
        "            </article>\n\n"
        '            <div class="pricing-note"><p>' + g["note"] + "</p></div>\n"
        "        </section>\n\n"
        '        <section class="features-section" id="features">\n'
        '            <div class="section-header">\n'
        "                <h2>" + g["feat_h"] + "</h2>\n"
        "                <p>" + g["feat_p"] + "</p>\n"
        "            </div>\n"
        '            <div class="features-grid">\n'
        + feats + "\n"
        "            </div>\n"
        "        </section>\n\n"
        '        <section class="why-us-section" id="why-us">\n'
        '            <div class="section-header">\n'
        "                <h2>" + g["why_h"] + "</h2>\n"
        "                <p>" + g["why_p"] + "</p>\n"
        "            </div>\n"
        '            <div class="why-us-grid">\n'
        + whys + "\n"
        "            </div>\n"
        "        </section>\n\n"
        '        <section class="steps-section" id="steps">\n'
        '            <div class="section-header">\n'
        "                <h2>" + g["steps_h"] + "</h2>\n"
        "                <p>" + g["steps_p"] + "</p>\n"
        "            </div>\n"
        '            <div class="steps-timeline">\n'
        + steps + "\n"
        "            </div>\n"
        '            <div class="steps-cta">\n'
        '                <a href="#pricing" class="btn-primary">' + g["start"] + "</a>\n"
        "            </div>\n"
        "        </section>\n\n"
        '        <section class="faq-section" id="faq">\n'
        '            <div class="section-header">\n'
        "                <h2>" + g["faq_h"] + "</h2>\n"
        "                <p>" + g["faq_p"] + "</p>\n"
        "            </div>\n"
        '            <div class="faq-list">\n'
        + faqs + "\n"
        "            </div>\n"
        '            <div class="faq-more">\n'
        '                <a href="' + faq_url + '" class="btn-secondary">' + g["more_faq"] + "</a>\n"
        "            </div>\n"
        "        </section>\n\n"
        '        <section class="customer-service" id="contact">\n'
        "            <h2>" + g["cs_h"] + "</h2>\n"
        '            <p class="cs-subtitle">' + g["cs_sub"] + "</p>\n"
        '            <div class="service-info">\n'
        '                <div class="service-item">\n'
        '                    <span class="service-label">' + u["cs_qq"] + "</span>\n"
        '                    <span class="service-value">1002569303</span>\n'
        "                </div>\n"
        '                <div class="service-note">\n'
        "                    <p>" + g["corp"] + "</p>\n"
        "                    <p>" + u["hours_full"] + "</p>\n"
        "                </div>\n"
        "            </div>\n"
        "        </section>\n"
        "    </div>\n\n"
        + footer_html(code, t) + "\n\n"
        '    <script src="/script.js"></script>\n'
        "</body>\n"
        "</html>\n"
    )
