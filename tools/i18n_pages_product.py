# -*- coding: utf-8 -*-
"""Gemini / Grok / Claude localized page content + builders."""
from i18n_common import head_common, nav_html, footer_html, ICON, locale_by_code, page_url
from i18n_ui import UI

# ---- GEMINI ----
GEMINI = {
"en": {
    "title": "GPTPro – Google Gemini Ready Accounts & Top-up",
    "desc": "Google Gemini ready accounts and top-up. Gemini 3, Gemini Pro multimodal access without a foreign credit card. Support 9:00–04:00, near-instant delivery.",
    "logo_sub": "Gemini accounts & top-up",
    "cta": "Top up now",
    "badge": "Google Gemini official accounts & mirror",
    "h1": "Google Gemini Ready Accounts & Top-up",
    "hero": "We focus on Gemini ready accounts and top-up. After checkout you get a login-ready account or we top up your existing one—Gemini 3, Gemini Pro, and more multimodal plans.",
    "buy": "Buy now",
    "contact": "Contact support",
    "tags": ["Gemini 3 ready accounts", "Gemini Pro top-up", "Invoice available", "Support 9:00–04:00", "Near-instant delivery"],
    "sec_h": "Official account & mirror options",
    "sec_p": "Official accounts are opened by support; the mirror offers an all-in-one experience",
    "c1_badge": "Official account",
    "c1_name": "Gemini Pro", "c1_tier": "18 months",
    "c1_desc": "Gemini Pro redemption link with Google One 5TB, about 18 months.",
    "c1_period": "/ 18 months",
    "c1_feats": ["Gemini Pro redemption link", "Includes Google One 5TB", "About 18 months validity", "After-sales tech support"],
    "c2_badge": "Popular",
    "c2_name": "Mirror site", "c2_tier": "No VPN needed",
    "c2_desc": "Mirror packs GPT, Claude, Gemini, Grok and more—no official IP/region/payment limits.",
    "c2_period": "/ mo from",
    "c2_feats": ["Covers Gemini 3 Pro", "Phone & desktop direct access", "GPT + Claude + Gemini + Grok", "95%+ parity with official"],
    "c2_btn": "Buy mirror pass",
    "note": "Virtual goods are non-refundable after purchase—confirm your needs before ordering",
    "why_h": "Why GPTPro", "why_p": "Reliable Gemini account service",
    "why": [
        ("⚡", "Near-instant delivery", "Auto delivery or manual open within seconds after order."),
        ("💰", "Pay in CNY", "Alipay, WeChat Pay and more—no foreign credit card."),
        ("🛠", "After-sales cover", "Support online 9:00–04:00; reach out when stuck."),
        ("🏢", "Business ready", "Bulk orders, corporate transfer, invoices available."),
    ],
    "cs_h": "Still have questions?",
    "cs_sub": "We typically reply within 5 minutes for quotes, contracts, invoices, and tech handoff",
    "corp": "Corporate transfer / company card accepted",
},
"zh-tw": {
    "title": "GPTPro代儲 - Google Gemini 成品帳號 & 儲值服務",
    "desc": "Google Gemini 成品帳號與儲值服務，支援 Gemini 3、Gemini Pro 等多模態體驗，無需海外信用卡，客服 9:00 - 翌日 4:00，秒級到帳。",
    "logo_sub": "Gemini 帳號 & 儲值",
    "cta": "立即儲值",
    "badge": "Google Gemini 官方帳號 & 鏡像站",
    "h1": "Google Gemini 成品帳號 & 儲值",
    "hero": "我們專注提供 Gemini 成品帳號和儲值服務。完成下單即可取得可登入帳號，或幫你在現有帳號中儲值，支援 Gemini 3、Gemini Pro 等多模態體驗。",
    "buy": "立即購買",
    "contact": "聯絡客服",
    "tags": ["支援 Gemini 3 成品帳號", "支援 Gemini Pro 儲值", "支援開票", "客服 9:00 - 翌日 4:00", "秒級到帳"],
    "sec_h": "官方帳號 & 鏡像站雙方案",
    "sec_p": "官方帳號由客服人工開通，鏡像站則提供多合一體驗",
    "c1_badge": "官方帳號",
    "c1_name": "Gemini Pro", "c1_tier": "18個月",
    "c1_desc": "Gemini Pro 兌換連結，含 Google One 5TB，約 18 個月時長。",
    "c1_period": "/ 18個月",
    "c1_feats": ["Gemini Pro 兌換連結", "含 Google One 5TB", "約 18 個月有效", "售後技術支援"],
    "c2_badge": "推薦",
    "c2_name": "鏡像站", "c2_tier": "免翻即用",
    "c2_desc": "鏡像系統整合 GPT、Claude、Gemini、Grok 等模型，免去官網的 IP/地區/支付限制。",
    "c2_period": "/ 月 起",
    "c2_feats": ["覆蓋 Gemini 3 Pro", "手機/電腦均可直接存取", "GPT + Claude + Gemini + Grok", "95% 以上能力與官方一致"],
    "c2_btn": "購買鏡像站通行證",
    "note": "虛擬商品購買後不退不換，下單前請確認需求",
    "why_h": "為什麼選擇 GPTPro代儲", "why_p": "穩定可靠的 Gemini 帳號服務",
    "why": [
        ("⚡", "秒級到帳", "下單後自動出貨或人工秒開，無需等待。"),
        ("💰", "人民幣支付", "支援支付寶、微信等支付方式，無需海外信用卡。"),
        ("🛠", "售後保障", "客服 9:00 - 翌日 4:00 在線，遇到問題及時聯絡。"),
        ("🏢", "支援企業", "支援批量採購、對公支付，可開立發票。"),
    ],
    "cs_h": "還有其它疑問？",
    "cs_sub": "我們會在 5 分鐘內回應，提供報價、合約、開票與技術對接",
    "corp": "支援對公轉帳/公司卡付款",
},
"ja": {
    "title": "GPTPro – Google Gemini アカウント＆チャージ",
    "desc": "Google Gemini の完成アカウントとチャージ。海外クレカ不要。Gemini 3 / Pro など。サポート 9:00〜翌4:00、即時納品。",
    "logo_sub": "Gemini アカウント＆チャージ",
    "cta": "今すぐチャージ",
    "badge": "Google Gemini 公式アカウント＆ミラー",
    "h1": "Google Gemini 完成アカウント＆チャージ",
    "hero": "Gemini の完成アカウントとチャージに特化。注文後にログイン可能なアカウント、または既存アカウントへのチャージ。Gemini 3 / Pro など多モーダル対応。",
    "buy": "今すぐ購入",
    "contact": "サポートに連絡",
    "tags": ["Gemini 3 完成アカウント", "Gemini Pro チャージ", "請求書対応", "サポート 9:00〜翌4:00", "即時納品"],
    "sec_h": "公式アカウントとミラーの2プラン",
    "sec_p": "公式はサポートが開通、ミラーはオールインワン体験",
    "c1_badge": "公式アカウント",
    "c1_name": "Gemini Pro", "c1_tier": "18ヶ月",
    "c1_desc": "Gemini Pro 交換リンク、Google One 5TB 付き、約18ヶ月。",
    "c1_period": "/ 18ヶ月",
    "c1_feats": ["Gemini Pro 交換リンク", "Google One 5TB 付き", "約18ヶ月有効", "アフターサポート"],
    "c2_badge": "おすすめ",
    "c2_name": "ミラーサイト", "c2_tier": "VPN不要",
    "c2_desc": "GPT / Claude / Gemini / Grok などを統合。公式の IP・地域・決済制限を回避。",
    "c2_period": "/ 月〜",
    "c2_feats": ["Gemini 3 Pro 対応", "スマホ／PCから直接", "GPT + Claude + Gemini + Grok", "公式と95%以上同等"],
    "c2_btn": "ミラーパスを購入",
    "note": "デジタル商品は購入後の返品不可。注文前にご確認ください",
    "why_h": "GPTPro を選ぶ理由", "why_p": "安定した Gemini アカウントサービス",
    "why": [
        ("⚡", "即時納品", "注文後に自動発送、または手動ですぐ開通。"),
        ("💰", "人民元決済", "Alipay / WeChat Pay など。海外クレカ不要。"),
        ("🛠", "アフター保証", "9:00〜翌4:00 対応。困ったらすぐ連絡を。"),
        ("🏢", "法人対応", "まとめて購入・対公振込・請求書対応。"),
    ],
    "cs_h": "ほかにご質問は？",
    "cs_sub": "通常5分以内に返信。見積・契約・請求書・技術連携も対応",
    "corp": "対公振込／会社カード対応",
},
"ko": {
    "title": "GPTPro – Google Gemini 계정 & 충전",
    "desc": "Google Gemini 완제품 계정과 충전. 해외 카드 없이 Gemini 3 / Pro. 고객지원 9:00–익일 4:00, 즉시 지급.",
    "logo_sub": "Gemini 계정 & 충전",
    "cta": "지금 충전",
    "badge": "Google Gemini 공식 계정 & 미러",
    "h1": "Google Gemini 완제품 계정 & 충전",
    "hero": "Gemini 완제품 계정과 충전에 집중합니다. 주문 후 로그인 가능한 계정 또는 기존 계정 충전. Gemini 3, Gemini Pro 등 멀티모달 지원.",
    "buy": "바로 구매",
    "contact": "고객지원 문의",
    "tags": ["Gemini 3 완제품 계정", "Gemini Pro 충전", "세금계산서 가능", "지원 9:00–익일 4:00", "즉시 지급"],
    "sec_h": "공식 계정 & 미러  Dual 옵션",
    "sec_p": "공식은 상담원이 개통, 미러는 올인원 경험 제공",
    "c1_badge": "공식 계정",
    "c1_name": "Gemini Pro", "c1_tier": "18개월",
    "c1_desc": "Gemini Pro 교환 링크, Google One 5TB 포함, 약 18개월.",
    "c1_period": "/ 18개월",
    "c1_feats": ["Gemini Pro 교환 링크", "Google One 5TB 포함", "약 18개월 유효", "애프터 기술 지원"],
    "c2_badge": "추천",
    "c2_name": "미러 사이트", "c2_tier": "VPN 불필요",
    "c2_desc": "GPT, Claude, Gemini, Grok 등을 통합. 공식 IP/지역/결제 제한 없음.",
    "c2_period": "/ 월부터",
    "c2_feats": ["Gemini 3 Pro 지원", "폰/PC 직접 접속", "GPT + Claude + Gemini + Grok", "공식과 95%+ 동등"],
    "c2_btn": "미러 패스 구매",
    "note": "가상 상품은 구매 후 환불·교환 불가. 주문 전 확인하세요",
    "why_h": "GPTPro를 선택하는 이유", "why_p": "안정적인 Gemini 계정 서비스",
    "why": [
        ("⚡", "즉시 지급", "주문 후 자동 발송 또는 수동 즉시 개통."),
        ("💰", "위안화 결제", "Alipay / WeChat Pay 등. 해외 카드 불필요."),
        ("🛠", "애프터 보장", "9:00–익일 4:00 응대. 문제 시 바로 연락."),
        ("🏢", "기업 지원", "대량 구매, 법인 이체, 세금계산서 가능."),
    ],
    "cs_h": "다른 궁금한 점이 있나요?",
    "cs_sub": "보통 5분 내 응답. 견적·계약·세금계산서·기술 연동 지원",
    "corp": "법인 이체 / 회사 카드 가능",
},
"es": {
    "title": "GPTPro – Cuentas Gemini listas y recarga",
    "desc": "Cuentas Google Gemini listas y recarga. Gemini 3 / Pro sin tarjeta extranjera. Soporte 9:00–04:00, entrega casi inmediata.",
    "logo_sub": "Cuentas y recarga Gemini",
    "cta": "Recargar ahora",
    "badge": "Cuentas oficiales Gemini y espejo",
    "h1": "Cuentas Google Gemini listas y recarga",
    "hero": "Nos enfocamos en cuentas Gemini listas y recargas. Tras el pedido obtienes una cuenta lista o recargamos la tuya: Gemini 3, Gemini Pro y más.",
    "buy": "Comprar ahora",
    "contact": "Contactar soporte",
    "tags": ["Cuentas Gemini 3 listas", "Recarga Gemini Pro", "Factura disponible", "Soporte 9:00–04:00", "Entrega casi inmediata"],
    "sec_h": "Cuenta oficial y opción espejo",
    "sec_p": "Las oficiales las abre soporte; el espejo ofrece experiencia todo-en-uno",
    "c1_badge": "Cuenta oficial",
    "c1_name": "Gemini Pro", "c1_tier": "18 meses",
    "c1_desc": "Enlace de canje Gemini Pro con Google One 5TB, unos 18 meses.",
    "c1_period": "/ 18 meses",
    "c1_feats": ["Enlace de canje Gemini Pro", "Incluye Google One 5TB", "Validez ~18 meses", "Soporte técnico postventa"],
    "c2_badge": "Popular",
    "c2_name": "Sitio espejo", "c2_tier": "Sin VPN",
    "c2_desc": "Integra GPT, Claude, Gemini, Grok… sin límites de IP/región/pago oficiales.",
    "c2_period": "/ mes desde",
    "c2_feats": ["Cubre Gemini 3 Pro", "Móvil y PC acceso directo", "GPT + Claude + Gemini + Grok", "95%+ paridad oficial"],
    "c2_btn": "Comprar pase espejo",
    "note": "Productos virtuales no reembolsables tras la compra—confirma antes de pedir",
    "why_h": "Por qué GPTPro", "why_p": "Servicio de cuentas Gemini fiable",
    "why": [
        ("⚡", "Entrega casi inmediata", "Envío auto o apertura manual en segundos."),
        ("💰", "Pago en CNY", "Alipay, WeChat Pay… sin tarjeta extranjera."),
        ("🛠", "Cobertura postventa", "Soporte 9:00–04:00; escribe si hay problemas."),
        ("🏢", "Listo para empresas", "Pedidos masivos, transferencia corporativa, facturas."),
    ],
    "cs_h": "¿Más dudas?",
    "cs_sub": "Solemos responder en 5 minutos: presupuestos, contratos, facturas y soporte técnico",
    "corp": "Transferencia corporativa / tarjeta de empresa",
},
"ru": {
    "title": "GPTPro – Аккаунты Google Gemini и пополнение",
    "desc": "Готовые аккаунты Google Gemini и пополнение. Gemini 3 / Pro без зарубежной карты. Поддержка 9:00–04:00, почти мгновенная выдача.",
    "logo_sub": "Аккаунты и пополнение Gemini",
    "cta": "Пополнить сейчас",
    "badge": "Официальные аккаунты Gemini и зеркало",
    "h1": "Готовые аккаунты Google Gemini и пополнение",
    "hero": "Фокус на готовых аккаунтах Gemini и пополнении. После заказа — аккаунт для входа или пополнение вашего: Gemini 3, Gemini Pro и др.",
    "buy": "Купить сейчас",
    "contact": "Связаться с поддержкой",
    "tags": ["Готовые аккаунты Gemini 3", "Пополнение Gemini Pro", "Счёт-фактура", "Поддержка 9:00–04:00", "Почти мгновенно"],
    "sec_h": "Официальный аккаунт и зеркало",
    "sec_p": "Официальные открывает поддержка; зеркало — всё в одном",
    "c1_badge": "Официальный аккаунт",
    "c1_name": "Gemini Pro", "c1_tier": "18 месяцев",
    "c1_desc": "Ссылка обмена Gemini Pro с Google One 5TB, около 18 месяцев.",
    "c1_period": "/ 18 мес",
    "c1_feats": ["Ссылка обмена Gemini Pro", "Включает Google One 5TB", "~18 месяцев", "Техподдержка"],
    "c2_badge": "Хит",
    "c2_name": "Зеркало", "c2_tier": "Без VPN",
    "c2_desc": "GPT, Claude, Gemini, Grok… без лимитов IP/региона/оплаты сайта.",
    "c2_period": "/ мес от",
    "c2_feats": ["Gemini 3 Pro", "Телефон и ПК напрямую", "GPT + Claude + Gemini + Grok", "95%+ как у официала"],
    "c2_btn": "Купить пропуск зеркала",
    "note": "Цифровые товары не возвращаются после покупки — уточните потребности заранее",
    "why_h": "Почему GPTPro", "why_p": "Надёжный сервис аккаунтов Gemini",
    "why": [
        ("⚡", "Почти мгновенно", "Автовыдача или ручное открытие за секунды."),
        ("💰", "Оплата в CNY", "Alipay, WeChat Pay… без зарубежной карты."),
        ("🛠", "Послепродажная поддержка", "Онлайн 9:00–04:00; пишите при проблемах."),
        ("🏢", "Для бизнеса", "Опт, корпоративный перевод, счета."),
    ],
    "cs_h": "Остались вопросы?",
    "cs_sub": "Обычно отвечаем за 5 минут: сметы, договоры, счета и техподдержка",
    "corp": "Корп. перевод / карта компании",
},
}


def build_gemini(code: str) -> str:
    u = UI[code]
    g = GEMINI[code]
    t = {**u, "logo_sub": g["logo_sub"]}
    _, _, html_lang, _ = locale_by_code(code)
    tags = "\n".join(f'                <span class="tag">{x}</span>' for x in g["tags"])
    f1 = "\n".join(f"                        <li>{x}</li>" for x in g["c1_feats"])
    f2 = "\n".join(f"                        <li>{x}</li>" for x in g["c2_feats"])
    why = "\n".join(
        f"""                <div class="why-us-card">
                    <div class="why-us-icon">{icon}</div>
                    <h3>{h}</h3>
                    <p>{p}</p>
                </div>"""
        for icon, h, p in g["why"]
    )
    return f"""{head_common(g['title'], g['desc'], html_lang, 'gemini/')}
<body>
{nav_html(code, 'gemini/', t, 'gemini', 'https://wzyp.cn/item/yuvhhb', g['cta'])}

    <div class="container">
        <section class="hero">
            <div class="hero-badge">{g['badge']}</div>
            <h1 class="hero-title"><img class="hero-brand-mark" src="{ICON['gemini']}" width="40" height="40" alt="" aria-hidden="true"> {g['h1']}</h1>
            <p class="hero-desc">{g['hero']}</p>
            <div class="hero-actions">
                <a href="https://wzyp.cn/item/yuvhhb" target="_blank" class="btn-primary">{g['buy']}</a>
                <a href="#contact" class="btn-secondary">{g['contact']}</a>
            </div>
            <div class="hero-tags">
{tags}
            </div>
        </section>

        <section class="pricing-section" id="pricing">
            <div class="section-header">
                <h2>{g['sec_h']}</h2>
                <p>{g['sec_p']}</p>
            </div>
            <div class="pricing-grid">
                <div class="pricing-card">
                    <div class="pricing-badge">{g['c1_badge']}</div>
                    <div class="pricing-title-row">
                        <img class="product-mark" src="{ICON['gemini']}" width="28" height="28" alt="" aria-hidden="true">
                        <h3><span class="product-name">{g['c1_name']}</span> <span class="product-tier">{g['c1_tier']}</span></h3>
                    </div>
                    <p class="pricing-desc">{g['c1_desc']}</p>
                    <div class="pricing-price">
                        <span class="price-currency">&yen;</span>
                        <span class="price-amount">49</span>
                        <span class="price-period">{g['c1_period']}</span>
                    </div>
                    <ul class="pricing-features">
{f1}
                    </ul>
                    <a href="https://wzyp.cn/item/yuvhhb" target="_blank" class="btn-primary btn-block">{g['buy']}</a>
                </div>
                <div class="pricing-card featured">
                    <div class="pricing-badge hot">{g['c2_badge']}</div>
                    <div class="pricing-title-row">
                        <img class="product-mark" src="{ICON['gemini']}" width="28" height="28" alt="" aria-hidden="true">
                        <h3><span class="product-name">{g['c2_name']}</span> <span class="product-tier">{g['c2_tier']}</span></h3>
                    </div>
                    <p class="pricing-desc">{g['c2_desc']}</p>
                    <div class="pricing-price">
                        <span class="price-currency">&yen;</span>
                        <span class="price-amount">82</span>
                        <span class="price-period">{g['c2_period']}</span>
                    </div>
                    <ul class="pricing-features">
{f2}
                    </ul>
                    <a href="https://momoai.czvip.cn/products/m22" target="_blank" rel="noopener noreferrer" class="btn-primary btn-block">{g['c2_btn']}</a>
                </div>
            </div>
            <div class="pricing-note"><p>{g['note']}</p></div>
        </section>

        <section class="why-us-section">
            <div class="section-header">
                <h2>{g['why_h']}</h2>
                <p>{g['why_p']}</p>
            </div>
            <div class="why-us-grid">
{why}
            </div>
        </section>

        <section class="customer-service" id="contact">
            <h2>{g['cs_h']}</h2>
            <p class="cs-subtitle">{g['cs_sub']}</p>
            <div class="service-info">
                <div class="service-item">
                    <span class="service-label">{u['cs_qq']}</span>
                    <span class="service-value">1002569303</span>
                </div>
                <div class="service-note">
                    <p>{g['corp']}</p>
                    <p>{u['hours_full']}</p>
                </div>
            </div>
        </section>
    </div>

{footer_html(code, t)}

    <script src="/script.js"></script>
</body>
</html>
"""
# fix typo price-period -> price-period in output via replace after

# ---- GROK ----
GROK = {
"en": {
    "title": "GPTPro – SuperGrok 1-Month CDK + X Premium+",
    "desc": "SuperGrok 1-month CDK self top-up with matching X Premium+. Official iOS $50/mo subscription. New and existing accounts; early renewal supported.",
    "logo_sub": "SuperGrok top-up",
    "cta": "Buy CDK",
    "badge": "Official iOS payment · 30-day warranty",
    "h1": "SuperGrok 1-Month CDK",
    "hero": "One code unlocks a full month of SuperGrok and matching X Premium+. Official iOS $50/mo subscription—no password needed. New and existing accounts welcome.",
    "buy": "Buy CDK",
    "self": "Self top-up",
    "tags": ["SuperGrok + X Premium+", "Official iOS top-up", "New & existing accounts", "Unused codes never expire", "24/7 self-service"],
    "cap_h": "Grok capabilities", "cap_p": "xAI’s next-gen AI—live web, deep reasoning, native image generation",
    "caps": [
        ("Realtime info", "Pulls live X (Twitter) data for news and trend analysis."),
        ("Deep reasoning", "Think mode walks complex problems step by step."),
        ("Image generation", "Built-in Aurora engine turns text into high-quality images."),
        ("Long context", "Huge context window for long docs and code reviews."),
        ("Coding help", "Strong code understanding and generation across languages."),
        ("Witty tone", "Grok’s personality keeps chats engaging."),
    ],
    "sec_h": "SuperGrok + X Premium+ plan",
    "sec_p": "Official iOS $50/mo. After buying the CDK, self top-up anytime within 24h availability",
    "card_name": "SuperGrok", "card_tier": "1-mo CDK",
    "card_desc": "Subscribe on your own X account for full SuperGrok plus matching X Premium+. Follow the self-service site—submit account ID or token only; never your password.",
    "meta": [("Duration", "1 month"), ("Method", "CDK self-service"), ("Subscription", "iOS paid $50/mo"), ("Warranty", "30 days")],
    "feats": [
        "Full SuperGrok and X Premium+ together",
        "New or existing accounts; early renewal OK",
        "Early renewal replaces current period (no stacking)",
        "Unused codes never expire; submit 24/7",
    ],
    "btn": "Buy CDK now",
    "note": "Used virtual goods can’t be resold; after-sales covers unusable CDKs only",
    "why_h": "Read before topping up", "why_p": "Confirm account conditions and warranty limits",
    "why": [
        ("🔒", "Use one code only", "If top-up fails, retry later or contact support—don’t burn multiple codes on one account."),
        ("💰", "Account risk", "Bulk signup, sharing, IP hopping, or abuse can get accounts banned."),
        ("⚡", "Bans outside warranty", "Bans from fraud, reverse proxies, or policy violations aren’t covered by the 30-day warranty."),
        ("🛠", "Protect credentials", "Only submit what’s asked on the official self-service page—don’t share tokens."),
    ],
    "cs_h": "Still stuck?",
    "cs_sub": "If top-up fails, retry later; if it persists, contact support",
    "note2": "Scan to add WeCom if the site goes offline",
    "note3": "Support hours 9:00–04:00; please wait if we don’t reply instantly",
},
"zh-tw": {
    "title": "GPTPro代儲 - SuperGrok 1月 CDK + X Premium+",
    "desc": "SuperGrok 1月 CDK 自助儲值，包含同時長 X Premium+，正規 iOS 50美元/月訂閱，支援新舊帳號與提前續費。",
    "logo_sub": "SuperGrok 儲值",
    "cta": "購買 CDK",
    "badge": "正規 iOS 實付 · 質保 30 天",
    "h1": "SuperGrok 1月 CDK",
    "hero": "一張卡密同時開通 1 個月滿血 SuperGrok 與 X Premium+。採用 iOS 50 美元/月正規訂閱，無需提供帳號密碼，新號、舊號均可自助儲值。",
    "buy": "購買 CDK",
    "self": "自助儲值",
    "tags": ["SuperGrok + X Premium+", "正規 iOS 儲值", "新舊帳號均可", "未使用卡密永久有效", "24 小時自助"],
    "cap_h": "Grok 能力一覽", "cap_p": "xAI 打造的下一代 AI，即時聯網、深度推理、原生圖像生成",
    "caps": [
        ("即時資訊", "接入 X（Twitter）即時資料，獲取最新資訊與熱點分析。"),
        ("深度推理", "支援 Think 深度思考模式，複雜問題也能層層推導。"),
        ("圖像生成", "內建 Aurora 圖像引擎，文字描述即可生成高品質圖片。"),
        ("超長上下文", "支援超長對話上下文，適合長文分析、程式碼審查。"),
        ("程式碼能力", "強大的程式碼理解與生成，支援多種語言。"),
        ("幽默風趣", "Grok 獨特個性回覆，讓 AI 對話不再枯燥。"),
    ],
    "sec_h": "SuperGrok + X Premium+ 儲值方案",
    "sec_p": "正規 iOS 50 美元/月訂閱，購買 CDK 後 24 小時可自助儲值",
    "card_name": "SuperGrok", "card_tier": "1月 CDK",
    "card_desc": "在您自己的 X 帳號上完成訂閱，同時獲得滿血 SuperGrok 與同時長 X Premium+。下單後按自助站提示提交帳號 ID 或所需 Token，無需提供帳號密碼。",
    "meta": [("權益時長", "1 個月"), ("儲值方式", "CDK 自助"), ("訂閱方式", "iOS 實付 $50/月"), ("質保期限", "30 天")],
    "feats": [
        "同時開通滿血 SuperGrok 與 X Premium+",
        "新號、舊號均可充，也可提前續費",
        "提前續費會覆蓋當前時間，時長不累計",
        "未使用卡密永久有效，24 小時可自助提交",
    ],
    "btn": "立即購買 CDK",
    "note": "虛擬商品使用後無法二次銷售；售後僅處理 CDK 無法使用，其他問題不在售後範圍內",
    "why_h": "儲值前請仔細閱讀", "why_p": "確認帳號條件與售後邊界，避免影響權益",
    "why": [
        ("🔒", "僅使用一張卡密", "如遇儲值失敗，請稍後重試或聯絡客服，不要用多張卡密反覆儲值同一帳號。"),
        ("💰", "帳號風險提示", "批量註冊、帳號共享、頻繁更換 IP 或違規使用均可能導致封號。"),
        ("⚡", "封號不在質保內", "因欺詐、反向代理或其他違規行為導致的封號，不在 30 天質保範圍內。"),
        ("🛠", "保護帳號資訊", "僅在指定自助站按頁面提示提交必要資訊，請勿將 Token 發送給無關人員。"),
    ],
    "cs_h": "還有其他疑問？",
    "cs_sub": "儲值失敗可稍後再次提交；如仍有問題，請及時聯絡客服",
    "note2": "如有問題或防止後續網站失聯，請掃碼添加企業微信諮詢",
    "note3": "客服在線時間：9:00 - 翌日 4:00；未及時回覆請耐心等待",
},
"ja": {
    "title": "GPTPro – SuperGrok 1ヶ月 CDK + X Premium+",
    "desc": "SuperGrok 1ヶ月 CDK セルフチャージ。同期間の X Premium+ 付き。正規 iOS $50/月。新旧アカウント・前倒し更新対応。",
    "logo_sub": "SuperGrok チャージ",
    "cta": "CDKを購入",
    "badge": "正規 iOS 実払い · 保証30日",
    "h1": "SuperGrok 1ヶ月 CDK",
    "hero": "1枚のコードで満額 SuperGrok と X Premium+ を1ヶ月同時開通。iOS $50/月の正規購読。パスワード不要。新旧アカウント対応。",
    "buy": "CDKを購入",
    "self": "セルフチャージ",
    "tags": ["SuperGrok + X Premium+", "正規 iOS チャージ", "新旧アカウント対応", "未使用コードは無期限", "24時間セルフ"],
    "cap_h": "Grok の能力", "cap_p": "xAI の次世代 AI — リアルタイム、深い推論、画像生成",
    "caps": [
        ("リアルタイム情報", "X（Twitter）のライブデータで最新ニュースを分析。"),
        ("深い推論", "Think モードで複雑な問題を段階的に解く。"),
        ("画像生成", "Aurora エンジンでテキストから高品質画像。"),
        ("長いコンテキスト", "長文解析やコードレビューに強い。"),
        ("コーディング", "多言語の理解と生成で開発を加速。"),
        ("ユーモア", "Grok らしい個性的な返答。"),
    ],
    "sec_h": "SuperGrok + X Premium+ プラン",
    "sec_p": "正規 iOS $50/月。CDK購入後、セルフでチャージ可能",
    "card_name": "SuperGrok", "card_tier": "1ヶ月 CDK",
    "card_desc": "ご自身の X アカウントで購読し、満額 SuperGrok と同期間の X Premium+ を取得。セルフサイトの案内に従い ID / Token のみ提出。パスワード不要。",
    "meta": [("期間", "1ヶ月"), ("方法", "CDK セルフ"), ("購読", "iOS 実払い $50/月"), ("保証", "30日")],
    "feats": [
        "満額 SuperGrok と X Premium+ を同時開通",
        "新旧アカウント可、前倒し更新も可",
        "前倒し更新は現行期間を上書き（加算なし）",
        "未使用コードは無期限、24時間提出可",
    ],
    "btn": "今すぐ CDK を購入",
    "note": "使用済みデジタル商品の再販不可。アフターは CDK 不能のみ対応",
    "why_h": "チャージ前にお読みください", "why_p": "アカウント条件と保証範囲を確認",
    "why": [
        ("🔒", "コードは1枚だけ", "失敗時は再試行かサポートへ。同一アカウントに複数コードを使わないでください。"),
        ("💰", "アカウントリスク", "大量登録・共有・IP 頻繁変更・規約違反は凍結の原因に。"),
        ("⚡", "凍結は保証外", "詐欺・リバースプロキシ等による凍結は30日保証の対象外。"),
        ("🛠", "情報を守る", "指定セルフサイトの指示のみに従い、Token を他人に渡さない。"),
    ],
    "cs_h": "ほかにご質問は？",
    "cs_sub": "失敗時は後で再提出。解決しない場合はサポートへ",
    "note2": "サイト不通に備え、企業微信の追加もご検討ください",
    "note3": "対応時間 9:00〜翌4:00。返信が遅れてもお待ちください",
},
"ko": {
    "title": "GPTPro – SuperGrok 1개월 CDK + X Premium+",
    "desc": "SuperGrok 1개월 CDK 셀프 충전, 동일 기간 X Premium+ 포함. 정식 iOS $50/월. 신규·기존 계정, 조기 갱신 지원.",
    "logo_sub": "SuperGrok 충전",
    "cta": "CDK 구매",
    "badge": "정식 iOS 실결제 · 보증 30일",
    "h1": "SuperGrok 1개월 CDK",
    "hero": "한 장의 코드로 풀 SuperGrok과 X Premium+를 1개월 동시 개통. iOS $50/월 정식 구독. 비밀번호 불필요. 신규·기존 계정 가능.",
    "buy": "CDK 구매",
    "self": "셀프 충전",
    "tags": ["SuperGrok + X Premium+", "정식 iOS 충전", "신규·기존 계정", "미사용 코드 무기한", "24시간 셀프"],
    "cap_h": "Grok 기능", "cap_p": "xAI 차세대 AI — 실시간, 심층 추론, 이미지 생성",
    "caps": [
        ("실시간 정보", "X(Twitter) 실시간 데이터로 뉴스·트렌드 분석."),
        ("심층 추론", "Think 모드로 복잡한 문제를 단계적으로 해결."),
        ("이미지 생성", "Aurora 엔진으로 텍스트→고품질 이미지."),
        ("긴 컨텍스트", "장문 분석·코드 리뷰에 적합."),
        ("코딩", "다양한 언어 이해·생성으로 개발 가속."),
        ("유머", "Grok만의 개성 있는 답변."),
    ],
    "sec_h": "SuperGrok + X Premium+ 요금제",
    "sec_p": "정식 iOS $50/월. CDK 구매 후 셀프 충전",
    "card_name": "SuperGrok", "card_tier": "1개월 CDK",
    "card_desc": "본인 X 계정에서 구독해 풀 SuperGrok과 동일 기간 X Premium+ 획득. 셀프 사이트 안내에 따라 ID/Token만 제출. 비밀번호 불필요.",
    "meta": [("기간", "1개월"), ("방식", "CDK 셀프"), ("구독", "iOS 실결제 $50/월"), ("보증", "30일")],
    "feats": [
        "풀 SuperGrok과 X Premium+ 동시 개통",
        "신규·기존 계정 가능, 조기 갱신 OK",
        "조기 갱신은 현재 기간을 덮어씀(누적 없음)",
        "미사용 코드 무기한, 24시간 제출 가능",
    ],
    "btn": "지금 CDK 구매",
    "note": "사용한 가상상품 재판매 불가. 애프터는 CDK 사용 불가만 처리",
    "why_h": "충전 전 꼭 읽으세요", "why_p": "계정 조건과 보증 범위를 확인",
    "why": [
        ("🔒", "코드는 한 장만", "실패 시 재시도 또는 문의. 한 계정에 여러 코드 사용 금지."),
        ("💰", "계정 위험", "대량 가입·공유·IP 잦은 변경·위반 사용은 정지 원인."),
        ("⚡", "정지는 보증 외", "사기·리버스 프록시 등으로 인한 정지는 30일 보증 제외."),
        ("🛠", "정보 보호", "지정 셀프 사이트 안내만 따르고 Token을 공유하지 마세요."),
    ],
    "cs_h": "다른 궁금한 점이 있나요?",
    "cs_sub": "실패 시 나중에 다시 제출. 계속되면 고객지원에 연락",
    "note2": "사이트 접속 불능에 대비해 기업 WeChat 추가를 권장",
    "note3": "응대 9:00–익일 4:00. 답변이 늦어도 기다려 주세요",
},
"es": {
    "title": "GPTPro – SuperGrok CDK 1 mes + X Premium+",
    "desc": "CDK SuperGrok 1 mes con X Premium+ del mismo periodo. Suscripción iOS oficial $50/mes. Cuentas nuevas y existentes; renovación anticipada.",
    "logo_sub": "Recarga SuperGrok",
    "cta": "Comprar CDK",
    "badge": "Pago iOS oficial · garantía 30 días",
    "h1": "SuperGrok CDK 1 mes",
    "hero": "Un código activa un mes completo de SuperGrok y X Premium+. Suscripción iOS oficial $50/mes—sin contraseña. Cuentas nuevas y existentes.",
    "buy": "Comprar CDK",
    "self": "Autoservicio",
    "tags": ["SuperGrok + X Premium+", "Recarga iOS oficial", "Cuentas nuevas y existentes", "Códigos sin usar no caducan", "Autoservicio 24/7"],
    "cap_h": "Capacidades de Grok", "cap_p": "IA de nueva generación de xAI: tiempo real, razonamiento e imágenes",
    "caps": [
        ("Info en tiempo real", "Datos en vivo de X (Twitter) para noticias y tendencias."),
        ("Razonamiento profundo", "Modo Think para problemas complejos paso a paso."),
        ("Generación de imágenes", "Motor Aurora: texto a imágenes de alta calidad."),
        ("Contexto largo", "Ventana amplia para docs largos y code review."),
        ("Código", "Comprensión y generación en varios lenguajes."),
        ("Tono ingenioso", "La personalidad de Grok hace el chat ameno."),
    ],
    "sec_h": "Plan SuperGrok + X Premium+",
    "sec_p": "iOS oficial $50/mes. Tras comprar el CDK, autoservicio",
    "card_name": "SuperGrok", "card_tier": "CDK 1 mes",
    "card_desc": "Suscríbete en tu propia cuenta X para SuperGrok completo y X Premium+ del mismo periodo. Sigue el sitio de autoservicio—solo ID o token; nunca la contraseña.",
    "meta": [("Duración", "1 mes"), ("Método", "CDK autoservicio"), ("Suscripción", "iOS pagado $50/mes"), ("Garantía", "30 días")],
    "feats": [
        "SuperGrok completo y X Premium+ juntos",
        "Cuentas nuevas o existentes; renovación anticipada OK",
        "La renovación anticipada reemplaza el periodo actual",
        "Códigos sin usar no caducan; envío 24/7",
    ],
    "btn": "Comprar CDK ahora",
    "note": "Bienes virtuales usados no se revenden; postventa solo CDK inutilizable",
    "why_h": "Lee antes de recargar", "why_p": "Confirma condiciones y límites de garantía",
    "why": [
        ("🔒", "Usa un solo código", "Si falla, reintenta o contacta soporte—no gastes varios códigos en una cuenta."),
        ("💰", "Riesgo de cuenta", "Altas masivas, compartir, cambiar IP o abusos pueden banear."),
        ("⚡", "Bans fuera de garantía", "Fraude, proxies inversos u otras violaciones no cubiertas en 30 días."),
        ("🛠", "Protege credenciales", "Solo envía lo pedido en el sitio oficial—no compartas tokens."),
    ],
    "cs_h": "¿Más dudas?",
    "cs_sub": "Si falla, reintenta luego; si persiste, contacta soporte",
    "note2": "Escanea WeCom por si el sitio queda offline",
    "note3": "Horario 9:00–04:00; espera si no respondemos al instante",
},
"ru": {
    "title": "GPTPro – SuperGrok CDK на 1 месяц + X Premium+",
    "desc": "CDK SuperGrok на 1 месяц с X Premium+ на тот же срок. Официальная подписка iOS $50/мес. Новые и старые аккаунты; досрочное продление.",
    "logo_sub": "Пополнение SuperGrok",
    "cta": "Купить CDK",
    "badge": "Официальная оплата iOS · гарантия 30 дней",
    "h1": "SuperGrok CDK на 1 месяц",
    "hero": "Один код открывает полный месяц SuperGrok и X Premium+. Официальная подписка iOS $50/мес — пароль не нужен. Новые и существующие аккаунты.",
    "buy": "Купить CDK",
    "self": "Самообслуживание",
    "tags": ["SuperGrok + X Premium+", "Официальное iOS", "Новые и старые аккаунты", "Неиспользованные коды бессрочны", "Самообслуживание 24/7"],
    "cap_h": "Возможности Grok", "cap_p": "ИИ нового поколения от xAI — онлайн, рассуждение, изображения",
    "caps": [
        ("Данные в реальном времени", "Живые данные X (Twitter) для новостей и трендов."),
        ("Глубокое рассуждение", "Режим Think для сложных задач по шагам."),
        ("Генерация изображений", "Движок Aurora: текст → качественные картинки."),
        ("Длинный контекст", "Большое окно для документов и code review."),
        ("Код", "Понимание и генерация на многих языках."),
        ("Юмор", "Характер Grok делает диалог живым."),
    ],
    "sec_h": "Тариф SuperGrok + X Premium+",
    "sec_p": "Официальный iOS $50/мес. После покупки CDK — самообслуживание",
    "card_name": "SuperGrok", "card_tier": "CDK 1 мес",
    "card_desc": "Подпишитесь на своём X-аккаунте: полный SuperGrok и X Premium+ на тот же срок. Следуйте сайту самообслуживания — только ID/токен, не пароль.",
    "meta": [("Срок", "1 месяц"), ("Способ", "CDK самообсл."), ("Подписка", "iOS $50/мес"), ("Гарантия", "30 дней")],
    "feats": [
        "Полный SuperGrok и X Premium+ вместе",
        "Новые и старые аккаунты; досрочное продление OK",
        "Досрочное продление заменяет текущий период",
        "Неиспользованные коды бессрочны; подача 24/7",
    ],
    "btn": "Купить CDK сейчас",
    "note": "Использованные цифровые товары не перепродаются; поддержка только по нерабочим CDK",
    "why_h": "Прочитайте перед пополнением", "why_p": "Уточните условия аккаунта и границы гарантии",
    "why": [
        ("🔒", "Только один код", "При сбое повторите позже или напишите в поддержку — не тратьте несколько кодов на один аккаунт."),
        ("💰", "Риск аккаунта", "Массовая регистрация, шаринг, смена IP или нарушения могут привести к бану."),
        ("⚡", "Баны вне гарантии", "Мошенничество, reverse proxy и т.п. не покрываются 30-дневной гарантией."),
        ("🛠", "Защита данных", "Отправляйте только запрошенное на официальном сайте — не делитесь токенами."),
    ],
    "cs_h": "Остались вопросы?",
    "cs_sub": "При сбое повторите позже; если не помогло — в поддержку",
    "note2": "Добавьте WeCom на случай недоступности сайта",
    "note3": "Часы 9:00–04:00; подождите, если ответ не мгновенный",
},
}


def _caps_html(caps):
    # reuse first 6 capability SVG paths from Chinese via emoji-free simple cards - use same SVG block simplified
    svgs = [
        '<svg viewBox="0 0 24 24" focusable="false"><circle cx="12" cy="12" r="9.5"></circle><path d="M2.5 12h19M12 2.5c2.5 2.6 3.7 5.8 3.7 9.5s-1.2 6.9-3.7 9.5c-2.5-2.6-3.7-5.8-3.7-9.5S9.5 5.1 12 2.5Z"></path><path d="M4.4 7.1h15.2M4.4 16.9h15.2"></path></svg>',
        '<svg viewBox="0 0 24 24" focusable="false"><path d="M12 5a3 3 0 1 0-6 .1A4 4 0 0 0 5 13.5V14a4 4 0 0 0 4 4h1a2 2 0 1 0 4 0h1a4 4 0 0 0 4-4v-.5a4 4 0 0 0-1-2.9A3 3 0 1 0 12 5Z"></path><path d="M12 5v13M9 13a2 2 0 0 1-2-2M15 13a2 2 0 0 0 2-2M9 9h.01M15 9h.01"></path></svg>',
        '<svg viewBox="0 0 24 24" focusable="false"><rect x="3" y="3" width="18" height="18" rx="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><path d="m21 15-5-5L5 21"></path></svg>',
        '<svg viewBox="0 0 24 24" focusable="false"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"></path><path d="M14 2v6h6M8 13h8M8 17h6"></path></svg>',
        '<svg viewBox="0 0 24 24" focusable="false"><rect x="3" y="4" width="18" height="13" rx="2"></rect><path d="M2 20h20M8 9l-2 2 2 2M16 9l2 2-2 2M13 8l-2 6"></path></svg>',
        '<svg viewBox="0 0 24 24" focusable="false"><circle cx="12" cy="12" r="9.5"></circle><path d="M8 14s1.5 2 4 2 4-2 4-2M9 9h.01M15 9h.01"></path></svg>',
    ]
    parts = []
    for i, (h, p) in enumerate(caps):
        parts.append(f"""                <div class="capability-card">
                    <span class="capability-icon" aria-hidden="true">{svgs[i]}</span>
                    <h3>{h}</h3>
                    <p>{p}</p>
                </div>""")
    return "\n".join(parts)


def build_grok(code: str) -> str:
    u = UI[code]
    g = GROK[code]
    t = {**u, "logo_sub": g["logo_sub"]}
    _, _, html_lang, _ = locale_by_code(code)
    tags = "\n".join(f'                <span class="tag">{x}</span>' for x in g["tags"])
    meta = "\n".join(
        f"""                        <div class="meta-item">
                            <span class="meta-label">{k}</span>
                            <span class="meta-value">{v}</span>
                        </div>"""
        for k, v in g["meta"]
    )
    feats = "\n".join(f"                        <li>{x}</li>" for x in g["feats"])
    why = "\n".join(
        f"""                <div class="why-us-card">
                    <div class="why-us-icon">{icon}</div>
                    <div class="why-us-content">
                        <h3>{h}</h3>
                        <p>{p}</p>
                    </div>
                </div>"""
        for icon, h, p in g["why"]
    )
    return f"""{head_common(g['title'], g['desc'], html_lang, 'grok/')}
<body>
{nav_html(code, 'grok/', t, 'grok', 'https://wzyp.cn/shop/maynorai/gyx7gn', g['cta'])}

    <div class="container">
        <section class="hero">
            <div class="hero-badge">{g['badge']}</div>
            <h1 class="hero-title"><img class="hero-brand-mark" src="{ICON['grok']}" width="40" height="40" alt="" aria-hidden="true"> {g['h1']}</h1>
            <p class="hero-desc">{g['hero']}</p>
            <div class="hero-actions">
                <a href="https://wzyp.cn/shop/maynorai/gyx7gn" target="_blank" rel="noopener noreferrer" class="btn-primary">{g['buy']}</a>
                <a href="https://quickplus.vip/public/x_plus/" target="_blank" rel="noopener noreferrer" class="btn-secondary">{g['self']}</a>
            </div>
            <div class="hero-tags">
{tags}
            </div>
        </section>

        <section class="capabilities-section" id="capabilities">
            <div class="section-header">
                <h2>{g['cap_h']}</h2>
                <p>{g['cap_p']}</p>
            </div>
            <div class="capabilities-grid">
{_caps_html(g['caps'])}
            </div>
        </section>

        <section class="pricing-section" id="pricing">
            <div class="section-header">
                <h2>{g['sec_h']}</h2>
                <p>{g['sec_p']}</p>
            </div>
            <div class="pricing-grid single">
                <div class="pricing-card featured">
                    <div class="pricing-title-row">
                        <img class="product-mark" src="{ICON['grok']}" width="28" height="28" alt="" aria-hidden="true">
                        <h3><span class="product-name">{g['card_name']}</span> <span class="product-tier">{g['card_tier']}</span></h3>
                    </div>
                    <p class="pricing-desc">{g['card_desc']}</p>
                    <div class="pricing-meta">
{meta}
                    </div>
                    <ul class="pricing-features">
{feats}
                    </ul>
                    <a href="https://wzyp.cn/shop/maynorai/gyx7gn" target="_blank" rel="noopener noreferrer" class="btn-primary btn-block">{g['btn']}</a>
                </div>
            </div>
            <div class="pricing-note"><p>{g['note']}</p></div>
        </section>

        <section class="why-us-section">
            <div class="section-header">
                <h2>{g['why_h']}</h2>
                <p>{g['why_p']}</p>
            </div>
            <div class="why-us-grid">
{why}
            </div>
        </section>

        <section class="customer-service" id="contact">
            <h2>{g['cs_h']}</h2>
            <p class="cs-subtitle">{g['cs_sub']}</p>
            <div class="service-info">
                <div class="service-item">
                    <span class="service-label">{u['cs_qq']}</span>
                    <span class="service-value">1002569303</span>
                </div>
                <div class="service-note">
                    <p>{g['note2']}</p>
                    <p>{g['note3']}</p>
                </div>
            </div>
        </section>
    </div>

{footer_html(code, t)}

    <script src="/script.js"></script>
</body>
</html>
"""

# ---- CLAUDE ----
CLAUDE = {
"en": {
    "title": "GPTPro – Claude Pro / Max Official Top-up",
    "desc": "Claude Mail accounts, Claude Pro codes, Claude Max official monthly cards. No foreign card—Alipay & WeChat Pay. Support QQ 1002569303.",
    "logo_sub": "Claude Pro / Max top-up",
    "cta": "Order now",
    "badge": "Claude Mail / Pro / Max · pay in CNY",
    "h1_pre": "", "h1_accent": "Claude Pro", "h1_post": " Professional Top-up",
    "hero": "No foreign credit card. Simple checkout with Alipay and WeChat Pay. Official channels, clear rules—reach QQ support for after-sales.",
    "tags": ["No foreign credit card", "Alipay / WeChat Pay", "Mail / Pro / Max", "Invoice available", "Enterprise bulk top-up"],
    "sec_h": "Official plans available now",
    "sec_p": "Current products for sale. Contact support if stock is low.",
    "cards": [
        {"badge": "Claude Mail account", "name": "Claude Mail standard", "desc": "Auto delivery. Stock and usage notes follow the checkout page.", "price": "15", "period": "/ account",
         "feats": ["Mail account auto delivery", "See checkout page for details", "Contact support if out of stock"]},
        {"badge": "Popular", "hot": True, "name": "Claude Pro official code", "desc": "Official top-up codes. Confirm with support when stock is low.", "price": "199", "period": "/ mo",
         "feats": ["Claude Pro official code", "Self top-up, transparent flow", "Pay in CNY—no foreign card", "After-sales via QQ support"]},
        {"badge": "Claude Max official", "name": "Claude Max 5x monthly", "desc": "Invoice-ready iOS US Claude Max 5x monthly. Official paid, 30-day subscription warranty.", "price": "980", "period": "/ mo",
         "feats": ["iOS US official paid", "30-day subscription warranty", "Invoice available", "Best if you value after-sales"]},
        {"badge": "Claude Max official", "name": "Claude Max 20x monthly", "desc": "Invoice-ready iOS US Claude Max 20x monthly. Official paid card, invoices OK.", "price": "1720", "period": "/ mo",
         "feats": ["Higher Max monthly quota", "iOS US official paid", "Invoice available", "Confirm with support before ordering"]},
    ],
    "note": "Enterprise: bulk top-up or corporate pay—contact support. Confirm account status and rules first. Support QQ: 1002569303",
    "why_h": "Why our Claude top-up?",
    "why_p": "Clear answers for payment, activation, and after-sales common in CN/APAC",
    "why": [
        ("💳", "No foreign card", "Pay in CNY—no overseas card or complex tools."),
        ("🔒", "Official channels", "Clear paths: Claude Mail, Pro codes, Max official monthly cards."),
        ("📞", "Fast after-sales", "Billing, rules, or issues—QQ support helps directly."),
        ("📄", "Transparent flow", "Prices, product notes, and support links in one place."),
    ],
    "cs_h": "Still have questions?",
    "cs_sub": "Confirm payment, timing, warranty—or ask about enterprise bulk and corporate pay",
    "corp": "Corporate transfer / company card accepted",
},
"zh-tw": {
    "title": "GPTPro代儲 - Claude Pro / Max 官方儲值",
    "desc": "Claude Mail 郵箱、Claude Pro 卡密、Claude Max 官方儲值月卡。無需境外信用卡，支援支付寶與微信支付，客服 QQ 1002569303。",
    "logo_sub": "Claude Pro / Max 儲值服務",
    "cta": "立即下單",
    "badge": "Claude Mail / Pro / Max · 人民幣付款",
    "h1_pre": "", "h1_accent": "Claude Pro", "h1_post": " 專業代儲服務",
    "hero": "無需境外信用卡，付款流程簡單，支援支付寶、微信支付。官方正規渠道儲值，規則清晰，售後問題可直接聯絡 QQ 客服處理。",
    "tags": ["無需境外信用卡", "支付寶 / 微信支付", "Mail / Pro / Max", "支援開票", "企業批量儲值"],
    "sec_h": "當前可購買的官方儲值套餐",
    "sec_p": "以下為當前可購買的商品。庫存不足時請聯絡客服確認。",
    "cards": [
        {"badge": "Claude Mail 郵箱帳號", "name": "Claude Mail 郵箱普號", "desc": "自動出貨，庫存及商品使用說明以下單頁為準。", "price": "15", "period": "/ 帳號",
         "feats": ["郵箱普號自動出貨", "以下單頁說明為準", "庫存不足請聯絡客服"]},
        {"badge": "推薦", "hot": True, "name": "Claude Pro 官方儲值卡密", "desc": "官方儲值發的卡密。庫存不足時請聯絡客服確認。", "price": "199", "period": "/ 月",
         "feats": ["Claude Pro 官方儲值卡密", "自助儲值，流程透明", "人民幣付款，無需境外卡", "售後可聯絡 QQ 客服"]},
        {"badge": "Claude Max 官方儲值", "name": "Claude Max 5x 月卡", "desc": "可開發票 iOS 美區 Claude Max 5x 月卡。官方儲值，質保訂閱 30 天，正規實付。", "price": "980", "period": "/ 月",
         "feats": ["iOS 美區官方實付", "質保訂閱 30 天", "可開發票", "適合更看重售後保障"]},
        {"badge": "Claude Max 官方儲值", "name": "Claude Max 20x 月卡", "desc": "可開發票 iOS 美區 Claude Max 20x 月卡。官方儲值月卡，正規實付，可開發票。", "price": "1720", "period": "/ 月",
         "feats": ["更高額度 Max 月卡", "iOS 美區官方實付", "可開發票", "下單前可聯絡客服確認"]},
    ],
    "note": "企業服務：支援批量儲值或對公支付，具體請聯絡客服。下單前請先確認帳號狀態、商品規則及售後規則。客服 QQ：1002569303",
    "why_h": "為什麼選擇我們的 Claude 儲值服務？",
    "why_p": "針對常見的支付、開通和售後問題做了集中說明",
    "why": [
        ("💳", "無需境外信用卡", "直接人民幣付款即可完成儲值，不用額外準備海外信用卡。"),
        ("🔒", "官方渠道儲值", "商品路徑清晰，覆蓋 Claude Mail 郵箱、Pro 卡密和 Max 官方儲值月卡。"),
        ("📞", "售後響應及時", "遇到帳、規則確認或售後問題，都可以直接聯絡 QQ 客服。"),
        ("📄", "流程透明明瞭", "價格、商品說明和客服入口集中展示，下單前資訊更透明。"),
    ],
    "cs_h": "還有其它疑問？",
    "cs_sub": "確認付款方式、處理時效、售後規則，或諮詢企業批量儲值與對公支付",
    "corp": "支援對公轉帳 / 公司卡付款",
},
"ja": {
    "title": "GPTPro – Claude Pro / Max 公式チャージ",
    "desc": "Claude Mail、Claude Pro コード、Claude Max 公式月カード。海外クレカ不要。Alipay / WeChat Pay。サポート QQ 1002569303。",
    "logo_sub": "Claude Pro / Max チャージ",
    "cta": "今すぐ注文",
    "badge": "Claude Mail / Pro / Max · 人民元決済",
    "h1_pre": "", "h1_accent": "Claude Pro", "h1_post": " プロチャージ",
    "hero": "海外クレカ不要。Alipay / WeChat Pay で簡単決済。公式チャネル、ルール明確。アフターは QQ サポートへ。",
    "tags": ["海外クレカ不要", "Alipay / WeChat Pay", "Mail / Pro / Max", "請求書対応", "法人まとめチャージ"],
    "sec_h": "購入可能な公式プラン",
    "sec_p": "現在販売中の商品。在庫不足時はサポートへ。",
    "cards": [
        {"badge": "Claude Mail アカウント", "name": "Claude Mail 標準", "desc": "自動発送。在庫と使い方は注文ページに準拠。", "price": "15", "period": "/ アカウント",
         "feats": ["メールアカウント自動発送", "注文ページの説明に準拠", "在庫不足時はサポートへ"]},
        {"badge": "おすすめ", "hot": True, "name": "Claude Pro 公式コード", "desc": "公式チャージのコード。在庫不足時は確認を。", "price": "199", "period": "/ 月",
         "feats": ["Claude Pro 公式コード", "セルフチャージ、透明な流れ", "人民元決済・海外カード不要", "アフターは QQ サポート"]},
        {"badge": "Claude Max 公式", "name": "Claude Max 5x 月カード", "desc": "請求書対応の iOS 米区 Claude Max 5x。公式実払い、購読保証30日。", "price": "980", "period": "/ 月",
         "feats": ["iOS 米区公式実払い", "購読保証30日", "請求書対応", "アフター重視の方向け"]},
        {"badge": "Claude Max 公式", "name": "Claude Max 20x 月カード", "desc": "請求書対応の iOS 米区 Claude Max 20x。公式月カード。", "price": "1720", "period": "/ 月",
         "feats": ["より高枠の Max 月カード", "iOS 米区公式実払い", "請求書対応", "注文前にサポート確認可"]},
    ],
    "note": "法人：まとめチャージや対公支払いはサポートへ。注文前にアカウント状態とルールを確認。QQ：1002569303",
    "why_h": "Claude チャージを選ぶ理由",
    "why_p": "決済・開通・アフターのよくある疑問を整理",
    "why": [
        ("💳", "海外クレカ不要", "人民元で完結。複雑な海外決済ツールは不要。"),
        ("🔒", "公式チャネル", "Mail / Pro コード / Max 公式月カードをカバー。"),
        ("📞", "迅速なアフター", "課金・ルール・トラブルは QQ サポートが対応。"),
        ("📄", "透明な流れ", "価格・説明・サポート入口を一箇所に。"),
    ],
    "cs_h": "ほかにご質問は？",
    "cs_sub": "決済方法・処理時間・保証、または法人まとめ・対公について",
    "corp": "対公振込／会社カード対応",
},
"ko": {
    "title": "GPTPro – Claude Pro / Max 공식 충전",
    "desc": "Claude Mail, Claude Pro 코드, Claude Max 공식 월카드. 해외 카드 불필요. Alipay / WeChat Pay. QQ 1002569303.",
    "logo_sub": "Claude Pro / Max 충전",
    "cta": "바로 주문",
    "badge": "Claude Mail / Pro / Max · 위안화 결제",
    "h1_pre": "", "h1_accent": "Claude Pro", "h1_post": " 전문 충전",
    "hero": "해외 카드 불필요. Alipay / WeChat Pay로 간편 결제. 공식 채널, 규칙 명확. 애프터는 QQ 고객지원.",
    "tags": ["해외 카드 불필요", "Alipay / WeChat Pay", "Mail / Pro / Max", "세금계산서 가능", "기업 대량 충전"],
    "sec_h": "현재 구매 가능한 공식 요금제",
    "sec_p": "판매 중인 상품. 재고 부족 시 고객지원에 확인.",
    "cards": [
        {"badge": "Claude Mail 계정", "name": "Claude Mail 일반", "desc": "자동 발송. 재고·사용법은 주문 페이지 기준.", "price": "15", "period": "/ 계정",
         "feats": ["메일 계정 자동 발송", "주문 페이지 설명 기준", "재고 부족 시 문의"]},
        {"badge": "추천", "hot": True, "name": "Claude Pro 공식 코드", "desc": "공식 충전 코드. 재고 부족 시 확인.", "price": "199", "period": "/ 월",
         "feats": ["Claude Pro 공식 코드", "셀프 충전, 투명한 절차", "위안화 결제·해외 카드 불필요", "애프터 QQ 지원"]},
        {"badge": "Claude Max 공식", "name": "Claude Max 5x 월카드", "desc": "세금계산서 가능 iOS 미구역 Claude Max 5x. 공식 실결제, 구독 보증 30일.", "price": "980", "period": "/ 월",
         "feats": ["iOS 미구역 공식 실결제", "구독 보증 30일", "세금계산서 가능", "애프터를 중시할 때"]},
        {"badge": "Claude Max 공식", "name": "Claude Max 20x 월카드", "desc": "세금계산서 가능 iOS 미구역 Claude Max 20x. 공식 월카드.", "price": "1720", "period": "/ 월",
         "feats": ["더 높은 Max 월 한도", "iOS 미구역 공식 실결제", "세금계산서 가능", "주문 전 확인 가능"]},
    ],
    "note": "기업: 대량 충전·법인 이체는 고객지원에. 주문 전 계정 상태와 규칙 확인. QQ: 1002569303",
    "why_h": "Claude 충전을 선택하는 이유",
    "why_p": "결제·개통·애프터 관련 자주 묻는 점을 정리",
    "why": [
        ("💳", "해외 카드 불필요", "위안화로 완료. 복잡한 해외 결제 도구 불필요."),
        ("🔒", "공식 채널", "Mail / Pro 코드 / Max 공식 월카드 커버."),
        ("📞", "빠른 애프터", "결제·규칙·문제는 QQ 고객지원이 도움."),
        ("📄", "투명한 절차", "가격·설명·지원 입구를 한곳에."),
    ],
    "cs_h": "다른 궁금한 점이 있나요?",
    "cs_sub": "결제 방식·처리 시간·보증, 또는 기업 대량·법인 이체 문의",
    "corp": "법인 이체 / 회사 카드 가능",
},
"es": {
    "title": "GPTPro – Recarga oficial Claude Pro / Max",
    "desc": "Cuentas Claude Mail, códigos Claude Pro, tarjetas mensuales Claude Max oficiales. Sin tarjeta extranjera—Alipay y WeChat Pay. QQ 1002569303.",
    "logo_sub": "Recarga Claude Pro / Max",
    "cta": "Pedir ahora",
    "badge": "Claude Mail / Pro / Max · pago en CNY",
    "h1_pre": "", "h1_accent": "Claude Pro", "h1_post": " Recarga profesional",
    "hero": "Sin tarjeta extranjera. Pago simple con Alipay y WeChat Pay. Canales oficiales, reglas claras—soporte QQ para postventa.",
    "tags": ["Sin tarjeta extranjera", "Alipay / WeChat Pay", "Mail / Pro / Max", "Factura disponible", "Recarga empresarial"],
    "sec_h": "Planes oficiales disponibles",
    "sec_p": "Productos a la venta. Contacta soporte si hay poco stock.",
    "cards": [
        {"badge": "Cuenta Claude Mail", "name": "Claude Mail estándar", "desc": "Entrega automática. Stock y uso según la página de pedido.", "price": "15", "period": "/ cuenta",
         "feats": ["Cuenta mail auto entrega", "Ver página de pedido", "Contactar si no hay stock"]},
        {"badge": "Popular", "hot": True, "name": "Código oficial Claude Pro", "desc": "Códigos de recarga oficial. Confirma con soporte si falta stock.", "price": "199", "period": "/ mes",
         "feats": ["Código oficial Claude Pro", "Autoservicio transparente", "Pago en CNY—sin tarjeta extranjera", "Postventa por QQ"]},
        {"badge": "Claude Max oficial", "name": "Claude Max 5x mensual", "desc": "Tarjeta mensual iOS US Claude Max 5x con factura. Pago oficial, garantía 30 días.", "price": "980", "period": "/ mes",
         "feats": ["Pago oficial iOS US", "Garantía de suscripción 30 días", "Factura disponible", "Ideal si valoras postventa"]},
        {"badge": "Claude Max oficial", "name": "Claude Max 20x mensual", "desc": "Tarjeta mensual iOS US Claude Max 20x con factura. Pago oficial.", "price": "1720", "period": "/ mes",
         "feats": ["Mayor cuota Max mensual", "Pago oficial iOS US", "Factura disponible", "Confirma con soporte antes"]},
    ],
    "note": "Empresas: recarga masiva o pago corporativo—contacta soporte. Confirma estado y reglas antes. QQ: 1002569303",
    "why_h": "¿Por qué nuestra recarga Claude?",
    "why_p": "Respuestas claras sobre pago, activación y postventa",
    "why": [
        ("💳", "Sin tarjeta extranjera", "Paga en CNY—sin tarjetas ni herramientas complejas."),
        ("🔒", "Canales oficiales", "Mail, códigos Pro y tarjetas Max oficiales."),
        ("📞", "Postventa rápida", "Facturación o dudas—soporte QQ ayuda directo."),
        ("📄", "Flujo transparente", "Precios, notas y enlaces de soporte en un lugar."),
    ],
    "cs_h": "¿Más dudas?",
    "cs_sub": "Confirma pago, plazos, garantía—o pregunta por empresas y pago corporativo",
    "corp": "Transferencia corporativa / tarjeta de empresa",
},
"ru": {
    "title": "GPTPro – Официальное пополнение Claude Pro / Max",
    "desc": "Claude Mail, коды Claude Pro, официальные месячные карты Claude Max. Без зарубежной карты — Alipay и WeChat Pay. QQ 1002569303.",
    "logo_sub": "Пополнение Claude Pro / Max",
    "cta": "Оформить заказ",
    "badge": "Claude Mail / Pro / Max · оплата в CNY",
    "h1_pre": "", "h1_accent": "Claude Pro", "h1_post": " Профессиональное пополнение",
    "hero": "Без зарубежной карты. Простая оплата Alipay и WeChat Pay. Официальные каналы, понятные правила — QQ поддержка для постпродаж.",
    "tags": ["Без зарубежной карты", "Alipay / WeChat Pay", "Mail / Pro / Max", "Счёт-фактура", "Корп. опт"],
    "sec_h": "Доступные официальные тарифы",
    "sec_p": "Товары в продаже. При дефиците свяжитесь с поддержкой.",
    "cards": [
        {"badge": "Аккаунт Claude Mail", "name": "Claude Mail стандарт", "desc": "Автовыдача. Наличие и инструкции — на странице заказа.", "price": "15", "period": "/ аккаунт",
         "feats": ["Автовыдача mail-аккаунта", "См. страницу заказа", "При отсутствии — в поддержку"]},
        {"badge": "Хит", "hot": True, "name": "Официальный код Claude Pro", "desc": "Коды официального пополнения. При дефиците уточните у поддержки.", "price": "199", "period": "/ мес",
         "feats": ["Официальный код Claude Pro", "Самообслуживание, прозрачный процесс", "Оплата в CNY — без зарубежной карты", "Постпродажа через QQ"]},
        {"badge": "Claude Max официально", "name": "Claude Max 5x месяц", "desc": "Месячная карта iOS US Claude Max 5x со счётом. Официальная оплата, гарантия подписки 30 дней.", "price": "980", "period": "/ мес",
         "feats": ["Официальная оплата iOS US", "Гарантия подписки 30 дней", "Счёт-фактура", "Если важна постпродажа"]},
        {"badge": "Claude Max официально", "name": "Claude Max 20x месяц", "desc": "Месячная карта iOS US Claude Max 20x со счётом. Официальная оплата.", "price": "1720", "period": "/ мес",
         "feats": ["Более высокий лимит Max", "Официальная оплата iOS US", "Счёт-фактура", "Можно уточнить перед заказом"]},
    ],
    "note": "Бизнес: опт или корп. оплата — в поддержку. Перед заказом уточните статус и правила. QQ: 1002569303",
    "why_h": "Почему наше пополнение Claude?",
    "why_p": "Понятные ответы по оплате, активации и постпродаже",
    "why": [
        ("💳", "Без зарубежной карты", "Оплата в CNY — без сложных зарубежных инструментов."),
        ("🔒", "Официальные каналы", "Mail, коды Pro и официальные месячные Max."),
        ("📞", "Быстрая постпродажа", "Счета, правила, проблемы — QQ поддержка поможет."),
        ("📄", "Прозрачный процесс", "Цены, описания и ссылки на поддержку в одном месте."),
    ],
    "cs_h": "Остались вопросы?",
    "cs_sub": "Уточните оплату, сроки, гарантию — или спросите про опт и корп. оплату",
    "corp": "Корп. перевод / карта компании",
},
}


def build_claude(code: str) -> str:
    u = UI[code]
    g = CLAUDE[code]
    t = {**u, "logo_sub": g["logo_sub"]}
    _, _, html_lang, _ = locale_by_code(code)
    tags = "\n".join(f'                <span class="tag">{x}</span>' for x in g["tags"])
    cards_html = []
    for c in g["cards"]:
        hot = ' hot' if c.get("hot") else ""
        featured = " featured" if c.get("hot") else ""
        feats = "\n".join(f"                        <li>{x}</li>" for x in c["feats"])
        cards_html.append(f"""                <div class="pricing-card{featured}">
                    <div class="pricing-badge{hot}">{c['badge']}</div>
                    <div class="pricing-title-row">
                        <img class="product-mark" src="{ICON['claude']}" width="28" height="28" alt="" aria-hidden="true">
                        <h3><span class="product-name">{c['name']}</span></h3>
                    </div>
                    <p class="pricing-desc">{c['desc']}</p>
                    <div class="pricing-price">
                        <span class="price-currency">&yen;</span>
                        <span class="price-amount">{c['price']}</span>
                        <span class="price-period">{c['period']}</span>
                    </div>
                    <ul class="pricing-features">
{feats}
                    </ul>
                    <a href="https://wzyp.cn/item/ahu0j7" target="_blank" rel="noopener noreferrer" class="btn-primary btn-block">{g['cta']}</a>
                </div>""")
    why = "\n".join(
        f"""                <div class="why-us-card">
                    <div class="why-us-icon">{icon}</div>
                    <h3>{h}</h3>
                    <p>{p}</p>
                </div>"""
        for icon, h, p in g["why"]
    )
    return f"""{head_common(g['title'], g['desc'], html_lang, 'claude/')}
<body>
{nav_html(code, 'claude/', t, 'claude', 'https://wzyp.cn/item/ahu0j7', g['cta'])}

    <div class="container">
        <section class="hero">
            <div class="hero-badge">{g['badge']}</div>
            <h1 class="hero-title"><img class="hero-brand-mark" src="{ICON['claude']}" width="40" height="40" alt="" aria-hidden="true"> {g['h1_pre']}<span class="hero-title-accent">{g['h1_accent']}</span>{g['h1_post']}</h1>
            <p class="hero-desc">{g['hero']}</p>
            <div class="hero-actions">
                <a href="https://wzyp.cn/item/ahu0j7" target="_blank" rel="noopener noreferrer" class="btn-primary">{g['cta']}</a>
                <a href="#pricing" class="btn-secondary">{u['view_plans']}</a>
            </div>
            <div class="hero-tags">
{tags}
            </div>
        </section>

        <section class="pricing-section" id="pricing">
            <div class="section-header">
                <h2>{g['sec_h']}</h2>
                <p>{g['sec_p']}</p>
            </div>
            <div class="pricing-grid quad">
{chr(10).join(cards_html)}
            </div>
            <div class="pricing-note"><p>{g['note']}</p></div>
        </section>

        <section class="why-us-section">
            <div class="section-header">
                <h2>{g['why_h']}</h2>
                <p>{g['why_p']}</p>
            </div>
            <div class="why-us-grid">
{why}
            </div>
        </section>

        <section class="customer-service" id="contact">
            <h2>{g['cs_h']}</h2>
            <p class="cs-subtitle">{g['cs_sub']}</p>
            <div class="service-info">
                <div class="service-item">
                    <span class="service-label">{u['cs_qq']}</span>
                    <span class="service-value">1002569303</span>
                </div>
                <div class="service-note">
                    <p>{g['corp']}</p>
                    <p>{u['hours_full']}</p>
                </div>
            </div>
        </section>
    </div>

{footer_html(code, t)}

    <script src="/script.js"></script>
</body>
</html>
"""
