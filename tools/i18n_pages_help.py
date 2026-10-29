# -*- coding: utf-8 -*-
"""FAQ, check, support page builders."""
from i18n_common import head_common, nav_html, footer_html, locale_by_code, page_url
from i18n_ui import UI

FAQ = {
"en": {
    "title": "GPTPro FAQ | ChatGPT Plus / Gemini / Grok Top-up",
    "desc": "Answers on safety, pricing, top-up flow, and warranty for GPTPro AI top-up services.",
    "logo_sub": "ChatGPT Plus top-up",
    "cta": "Top up now",
    "h1": "Frequently asked questions",
    "hero": "Safety, pricing, top-up steps, and after-sales—answers to what users ask most.",
    "cats": [
        ("Safety & accounts", [
            ("Is top-up safe? Can my account get banned?",
             "Very safe. We use official iOS channels—the most reliable way to top up ChatGPT Plus. No customer has been banned solely due to our top-up. Ban rate is under 0.1%."),
            ("How does assisted top-up differ from official?",
             "Lower price; official channels; no foreign card; simple flow. We complete the same official top-up for you—the result matches doing it yourself."),
            ("Do I need to share my password?",
             "No. Neither Plus nor Pro requires your password. Plus is mostly code/session self-service; Pro follows official login guidance without handing over passwords."),
            ("How many users have you served?",
             "We have served 13,000+ ChatGPT Plus users with high satisfaction. Failed top-ups are 100% refunded."),
        ]),
        ("Pricing & payment", [
            ("Why cheaper than the official $20? What is your margin?",
             "Bulk purchasing lowers cost—no card fees. Savings go to you. Our margin comes from scale and service fees."),
            ("Which payment methods?",
             "Alipay, WeChat Pay, QQ Pay and other CN methods—no virtual or USD cards needed."),
            ("Can I avoid fees by paying support directly?",
             "Yes. Transfer via support QQ to skip third-party fees. Online 9:00–04:00."),
            ("Can I renew Plus long-term? Are prices stable?",
             "Yes. We adjust quotes with cost and post updates on-site. Bookmark or ask support for channel news."),
        ]),
        ("Top-up flow", [
            ("How long does top-up take?",
             "Usually 1–3 minutes. Plus activates right after success."),
            ("How do I renew next month?",
             "Same as first purchase. Bookmark the site, buy a new code when due, repeat the steps."),
            ("Do codes expire?",
             "Unused codes do not expire—they invalidate only after a successful top-up. Buy anytime."),
            ("What should I watch during top-up?",
             "Do not close the page until success. Keep a stable network for the typical 1–3 minutes."),
        ]),
        ("Warranty", [
            ("What if top-up fails?",
             "Confirm membership expired and network is stable. Retry a few times or contact support. Failures are 100% refunded."),
            ("Do you refund?",
             "If we cause a failed top-up, full code refund. Within 30-day warranty, dropped subscriptions are compensated per day."),
            ("Enterprise / team bulk? Invoices?",
             "Yes—bulk top-up, corporate transfer, invoices. Many schools and AI teams use us. Ask support."),
            ("Same warranty for Gemini and Grok?",
             "Gemini ready accounts/mirrors are virtual—non-refundable after purchase. SuperGrok CDK has 30-day warranty for unusable codes; bans from account abuse are not covered."),
        ]),
    ],
    "cs_h": "Still have questions?",
    "cs_sub": "We typically reply within 5 minutes to help you finish top-up",
    "cs_note": "Use the bottom-right chat or QQ—online 9:00–04:00",
    "cs_note2": "Corporate transfer and invoices supported",
},
"zh-tw": {
    "title": "GPTPro代儲 - 常見問題解答 | ChatGPT Plus / Gemini / Grok 儲值",
    "desc": "GPTPro代儲 儲值服務常見問題，包含安全性、價格、儲值流程與售後。",
    "logo_sub": "ChatGPT Plus 儲值服務",
    "cta": "立即儲值",
    "h1": "常見問題解答",
    "hero": "我們整理了用戶最關心的安全、價格、儲值流程與售後問題。",
    "cats": [
        ("安全與帳號", [
            ("儲值服務安全嗎？帳號會被封嗎？", "非常安全。我們採用正規 iOS 儲值渠道，至今沒有客戶因儲值被封號。封號概率低於 0.1%。"),
            ("代儲和官方儲值有什麼區別？", "價格更優惠；正規通道；無需國外信用卡。本質上是透過正規渠道幫您完成儲值，效果與自行儲值一致。"),
            ("儲值需要提供帳號密碼嗎？", "不需要。Plus 和 Pro 都不需要提供帳號密碼，按頁面或客服指引完成即可。"),
            ("有多少用戶使用過你們的服務？", "已為 1.3 萬+ 用戶提供 ChatGPT Plus 儲值，失敗 100% 退款。"),
        ]),
        ("價格與支付", [
            ("為什麼比官方 20 美元便宜？", "批量採購降低成本，無需開卡費，優惠返還用戶。利潤來自規模與服務費。"),
            ("支援哪些支付方式？", "支付寶、微信支付、QQ 等，免去虛擬卡或美元信用卡。"),
            ("聯絡客服轉帳可以免手續費嗎？", "可以。直接聯絡客服 QQ 轉帳可免第三方手續費。9:00 - 翌日 4:00。"),
            ("Plus 可以長期續費嗎？", "可以。依成本調整報價並在站內公告。收藏本站或聯絡客服即可。"),
        ]),
        ("儲值流程", [
            ("整個流程需要多長時間？", "通常 1–3 分鐘即可完成，Plus 立即生效。"),
            ("下個月如何續費？", "與首次購買相同。到期後購買新卡密並重複步驟。"),
            ("卡密有有效期嗎？", "未使用卡密無期限，僅在儲值成功後失效。"),
            ("儲值期間注意什麼？", "成功提示前請勿關閉頁面，保持網路穩定。"),
        ]),
        ("售後保障", [
            ("儲值失敗怎麼辦？", "確認會員已過期與網路穩定，多試幾次或聯絡客服。失敗 100% 全額退款。"),
            ("是否支援退款？", "因我們問題導致失敗提供全額退款。質保 30 天內掉訂閱按天賠付。"),
            ("企業可批量儲值、開票嗎？", "支援批量、對公、發票，詳情諮詢客服。"),
            ("Gemini 和 Grok 保障相同嗎？", "Gemini 成品/鏡像購買後不退不換；SuperGrok CDK 30 天質保僅處理無法使用的 CDK，違規封號不在質保內。"),
        ]),
    ],
    "cs_h": "還有其他疑問？",
    "cs_sub": "我們會在 5 分鐘內回應，協助完成儲值",
    "cs_note": "右下角或 QQ 諮詢，客服在線 9:00 - 翌日 4:00",
    "cs_note2": "支援對公轉帳、企業開票",
},
"ja": {
    "title": "GPTPro よくある質問 | ChatGPT Plus / Gemini / Grok",
    "desc": "安全性、価格、チャージ手順、保証についての FAQ。",
    "logo_sub": "ChatGPT Plus チャージ",
    "cta": "今すぐチャージ",
    "h1": "よくある質問",
    "hero": "安全性・価格・手順・アフターなど、よくある疑問をまとめました。",
    "cats": [
        ("安全とアカウント", [
            ("チャージは安全？凍結される？", "非常に安全。正規 iOS チャネル使用。チャージ単体での凍結事例なし。凍結率 0.1% 未満。"),
            ("代行と公式の違いは？", "より安価・正規・海外クレカ不要。結果は自分で公式チャージした場合と同じ。"),
            ("パスワードは必要？", "不要。Plus / Pro ともパスワード不要。案内に従うだけ。"),
            ("利用者数は？", "ChatGPT Plus で 1.3万+。失敗時は 100% 返金。"),
        ]),
        ("価格と支払い", [
            ("公式 $20 より安い理由は？", "まとめ仕入れでコスト削減。利益は規模とサービス料から。"),
            ("支払い方法は？", "Alipay / WeChat Pay / QQ など。仮想・ドルカード不要。"),
            ("サポート振込で手数料ゼロ？", "可能。QQ へ直接振込。9:00〜翌4:00。"),
            ("長期更新は？", "可能。コストに応じて更新しサイトで告知。"),
        ]),
        ("チャージ手順", [
            ("所要時間は？", "通常 1〜3 分。成功後すぐに Plus が有効。"),
            ("翌月の更新は？", "初回と同じ。期限後に新しいコードを購入。"),
            ("コードの有効期限は？", "未使用に期限なし。成功後に無効化。"),
            ("注意点は？", "成功までページを閉じない。安定回線で 1〜3 分。"),
        ]),
        ("保証", [
            ("失敗したら？", "期限切れと回線を確認し再試行かサポートへ。失敗は 100% 返金。"),
            ("返金は？", "当方原因の失敗は全額返金。30日保証内の購読落ちは日割り補償。"),
            ("法人まとめ・請求書は？", "対応。詳細はサポートへ。"),
            ("Gemini / Grok も同じ？", "Gemini は購入後返品不可。SuperGrok CDK は不能時 30日保証。規約違反凍結は対象外。"),
        ]),
    ],
    "cs_h": "ほかにご質問は？",
    "cs_sub": "通常5分以内に返信しチャージ完了までサポート",
    "cs_note": "右下または QQ。対応 9:00〜翌4:00",
    "cs_note2": "対公振込・請求書対応",
},
"ko": {
    "title": "GPTPro FAQ | ChatGPT Plus / Gemini / Grok 충전",
    "desc": "안전, 가격, 충전 절차, 보증에 대한 FAQ.",
    "logo_sub": "ChatGPT Plus 충전",
    "cta": "지금 충전",
    "h1": "자주 묻는 질문",
    "hero": "안전·가격·절차·애프터 등 자주 묻는 질문을 정리했습니다.",
    "cats": [
        ("안전 & 계정", [
            ("충전이 안전한가요?", "매우 안전. 정식 iOS 채널. 충전만으로 정지된 사례 없음. 정지율 0.1% 미만."),
            ("대행과 공식의 차이는?", "더 저렴하고 정식·해외 카드 불필요. 결과는 직접 공식 충전과 동일."),
            ("비밀번호가 필요하나요?", "불필요. Plus/Pro 모두 안내대로 진행."),
            ("이용자 수는?", "ChatGPT Plus 1.3만+. 실패 시 100% 환불."),
        ]),
        ("가격 & 결제", [
            ("공식 $20보다 싼 이유는?", "대량 구매로 비용 절감. 이익은 규모와 서비스 수수료."),
            ("결제 수단은?", "Alipay / WeChat Pay / QQ 등."),
            ("고객지원 이체로 수수료 면제?", "가능. QQ 직접 이체. 9:00–익일 4:00."),
            ("장기 갱신?", "가능. 비용에 맞춰 조정하고 사이트에 공지."),
        ]),
        ("충전 절차", [
            ("얼마나 걸리나요?", "보통 1–3분. 성공 후 Plus 즉시 적용."),
            ("다음 달 갱신은?", "첫 구매와 동일. 만료 후 새 코드 구매."),
            ("코드 유효기간은?", "미사용 코드는 무기한. 성공 후에만 무효."),
            ("주의할 점은?", "성공까지 페이지를 닫지 마세요."),
        ]),
        ("보증", [
            ("실패하면?", "만료·네트워크 확인 후 재시도 또는 문의. 실패 100% 환불."),
            ("환불은?", "당사 사유 실패 시 전액 환불. 30일 보증 내 구독 중단은 일할 보상."),
            ("기업 대량·세금계산서?", "지원. 자세한 내용은 문의."),
            ("Gemini / Grok도 같나요?", "Gemini는 구매 후 환불 불가. SuperGrok CDK는 사용 불가 시 30일 보증."),
        ]),
    ],
    "cs_h": "다른 궁금한 점이 있나요?",
    "cs_sub": "보통 5분 내 응답하며 충전 완료까지 도와드립니다",
    "cs_note": "우측 하단 또는 QQ. 응대 9:00–익일 4:00",
    "cs_note2": "법인 이체·세금계산서 지원",
},
"es": {
    "title": "GPTPro FAQ | Recarga ChatGPT Plus / Gemini / Grok",
    "desc": "Respuestas sobre seguridad, precios, flujo de recarga y garantía.",
    "logo_sub": "Recarga ChatGPT Plus",
    "cta": "Recargar ahora",
    "h1": "Preguntas frecuentes",
    "hero": "Seguridad, precios, pasos y postventa—lo que más preguntan los usuarios.",
    "cats": [
        ("Seguridad y cuentas", [
            ("¿Es segura la recarga?", "Muy segura. Canales iOS oficiales. Tasa de ban <0.1%."),
            ("¿En qué se diferencia del oficial?", "Más barato; canal oficial; sin tarjeta extranjera. Mismo resultado."),
            ("¿Necesito la contraseña?", "No. Ni Plus ni Pro la requieren."),
            ("¿Cuántos usuarios?", "Más de 13.000. Fallos 100% reembolsados."),
        ]),
        ("Precios y pago", [
            ("¿Por qué más barato que $20?", "Compra al por mayor sin comisiones de tarjeta."),
            ("¿Métodos de pago?", "Alipay, WeChat Pay, QQ…"),
            ("¿Evitar comisiones con soporte?", "Sí. Transferencia por QQ. 9:00–04:00."),
            ("¿Renovación larga?", "Sí. Ajustamos con el coste y avisamos en el sitio."),
        ]),
        ("Flujo de recarga", [
            ("¿Cuánto tarda?", "Suele ser 1–3 minutos."),
            ("¿Cómo renuevo?", "Igual que la primera vez."),
            ("¿Caducan los códigos?", "Los no usados no caducan."),
            ("¿Qué cuidar?", "No cierres la página hasta el éxito."),
        ]),
        ("Garantía", [
            ("¿Si falla?", "Reintenta o contacta soporte. Fallos 100% reembolsados."),
            ("¿Reembolsos?", "Si fallamos nosotros, reembolso total. En 30 días, compensación diaria."),
            ("¿Empresas / facturas?", "Sí. Pregunta a soporte."),
            ("¿Igual para Gemini y Grok?", "Gemini no reembolsable tras compra. SuperGrok CDK: garantía 30 días por CDK inutilizable."),
        ]),
    ],
    "cs_h": "¿Más dudas?",
    "cs_sub": "Solemos responder en 5 minutos",
    "cs_note": "Chat o QQ—en línea 9:00–04:00",
    "cs_note2": "Transferencia corporativa y facturas",
},
"ru": {
    "title": "GPTPro FAQ | Пополнение ChatGPT Plus / Gemini / Grok",
    "desc": "Ответы о безопасности, ценах, процессе пополнения и гарантии.",
    "logo_sub": "Пополнение ChatGPT Plus",
    "cta": "Пополнить сейчас",
    "h1": "Частые вопросы",
    "hero": "Безопасность, цены, шаги и постпродажа — ответы на главные вопросы.",
    "cats": [
        ("Безопасность и аккаунты", [
            ("Безопасно ли?", "Очень безопасно. Официальные каналы iOS. Доля банов <0.1%."),
            ("Чем отличается от официального?", "Дешевле; официальный канал; без зарубежной карты. Тот же результат."),
            ("Нужен ли пароль?", "Нет. Ни Plus, ни Pro не требуют пароля."),
            ("Сколько пользователей?", "13 000+. Неудачи — 100% возврат."),
        ]),
        ("Цены и оплата", [
            ("Почему дешевле $20?", "Оптовые закупки без комиссий за карты."),
            ("Какие способы оплаты?", "Alipay, WeChat Pay, QQ…"),
            ("Можно без комиссии через поддержку?", "Да. Перевод на QQ. 9:00–04:00."),
            ("Долгое продление?", "Да. Корректируем по себестоимости и публикуем на сайте."),
        ]),
        ("Процесс пополнения", [
            ("Сколько занимает?", "Обычно 1–3 минуты."),
            ("Как продлить?", "Как в первый раз."),
            ("Коды сгорают?", "Неиспользованные бессрочны."),
            ("На что смотреть?", "Не закрывайте страницу до успеха."),
        ]),
        ("Гарантия", [
            ("Если не удалось?", "Повторите или напишите в поддержку. Неудачи — 100% возврат."),
            ("Возвраты?", "Если сбой по нашей вине — полный возврат. В 30 дней — подённая компенсация."),
            ("Бизнес / счета?", "Да. Спросите поддержку."),
            ("То же для Gemini и Grok?", "Gemini после покупки не возвращается. SuperGrok CDK: гарантия 30 дней на нерабочий код."),
        ]),
    ],
    "cs_h": "Остались вопросы?",
    "cs_sub": "Обычно отвечаем за 5 минут",
    "cs_note": "Чат или QQ — онлайн 9:00–04:00",
    "cs_note2": "Корп. перевод и счета",
},
}


def build_faq(code):
    u = UI[code]
    g = FAQ[code]
    t = dict(u)
    t["logo_sub"] = g["logo_sub"]
    _, _, html_lang, _ = locale_by_code(code)
    sections = []
    for cat, items in g["cats"]:
        lis = []
        for q, a in items:
            lis.append(
                '                    <div class="faq-item">\n'
                '                        <button class="faq-question">\n'
                '                            <span>' + q + '</span>\n'
                '                            <span class="faq-arrow">+</span>\n'
                '                        </button>\n'
                '                        <div class="faq-answer">\n'
                '                            <p>' + a + '</p>\n'
                '                        </div>\n'
                '                    </div>'
            )
        sections.append(
            '            <div class="faq-category">\n'
            '                <h2 class="faq-category-title">' + cat + '</h2>\n'
            '                <div class="faq-list">\n'
            + '\n'.join(lis) + '\n'
            '                </div>\n'
            '            </div>'
        )
    return (
        head_common(g['title'], g['desc'], html_lang, 'faq/') + '\n'
        '<body>\n'
        + nav_html(code, 'faq/', t, 'faq', 'https://wzyp.cn/item/bp1jdo', g['cta']) + '\n\n'
        '    <div class="container">\n'
        '        <section class="hero hero-sm">\n'
        '            <h1 class="hero-title">' + g['h1'] + '</h1>\n'
        '            <p class="hero-desc">' + g['hero'] + '</p>\n'
        '        </section>\n'
        '        <section class="faq-full">\n'
        + '\n'.join(sections) + '\n'
        '        </section>\n'
        '        <section class="customer-service">\n'
        '            <h2>' + g['cs_h'] + '</h2>\n'
        '            <p class="cs-subtitle">' + g['cs_sub'] + '</p>\n'
        '            <div class="service-info">\n'
        '                <div class="service-item">\n'
        '                    <span class="service-label">' + u['cs_qq'] + '</span>\n'
        '                    <span class="service-value">1002569303</span>\n'
        '                </div>\n'
        '                <div class="service-note">\n'
        '                    <p>' + g['cs_note'] + '</p>\n'
        '                    <p>' + g['cs_note2'] + '</p>\n'
        '                </div>\n'
        '            </div>\n'
        '        </section>\n'
        '    </div>\n'
        + footer_html(code, t) + '\n'
        '    <script src="/script.js"></script>\n'
        '</body>\n'
        '</html>\n'
    )

CHECK = {
"en": {
    "title": "ChatGPT Account Check | GPTPro",
    "desc": "Paste chatgpt.com/api/auth/session JSON to see plan and whether Plus can be opened or renewed. Read-only; session not stored.",
    "logo_sub": "ChatGPT account check",
    "cta": "Contact support",
    "badge": "Read-only · session not stored · no order needed",
    "h1a": "Can this account", "h1b": "be opened?",
    "sub": "Paste the full JSON from <code>chatgpt.com/api/auth/session</code> (must include <strong>accessToken</strong>). In seconds see the plan and whether you can open / upgrade / renew.",
    "waiting": "Waiting for paste",
    "open_session": "Open Session",
    "copy_link": "Copy link",
    "label": "Paste Session JSON",
    "placeholder": "Open Session while logged in → Ctrl/Cmd+A → copy → paste here",
    "hint": "Long full-page content is normal",
    "run": "Start check",
    "paste": "Paste from clipboard",
    "step1": "Open Session in a browser logged into ChatGPT",
    "step2": "Select all and copy the full JSON",
    "step3": "Paste, then click Start check",
    "privacy": "Read-only subscription info; session used only for this check and not stored. After checking, refresh the Session page so the pasted copy expires.",
    "verdict_wait": "Waiting for check",
    "again": "Check another account",
    "pricing": "View top-up prices",
    "qq": "QQ support 1002569303",
    "cs_h": "Not sure about the result?",
    "cs_sub": "Send account details or the verdict to support to confirm eligibility",
    "open_qq": "Open QQ chat",
    "or_add": "(or add QQ 1002569303)",
    "see_support": "Or visit the",
    "support_center": "Support Center",
    "for_faq": "for common Q&A.",
},
"zh-tw": {
    "title": "ChatGPT 帳號檢測 | GPTPro代儲",
    "desc": "貼上 chatgpt.com/api/auth/session 完整 JSON，查看套餐與是否可開通 Plus / 升級續費。只讀檢測，不儲存 Session。",
    "logo_sub": "ChatGPT 帳號檢測",
    "cta": "聯絡客服",
    "badge": "只讀 · 不存 Session · 不用下單",
    "h1a": "這個號", "h1b": "能不能開？",
    "sub": "貼上 <code>chatgpt.com/api/auth/session</code> 整頁 JSON（須含 <strong>accessToken</strong>），幾秒看清套餐，以及能不能開通 / 升級續費。",
    "waiting": "等待貼上",
    "open_session": "打開 Session",
    "copy_link": "複製連結",
    "label": "貼上 Session JSON",
    "placeholder": "在已登入的瀏覽器打開 Session 頁 → Ctrl/Cmd+A 全選 → 複製 → 貼到這裡",
    "hint": "內容很長、佔滿整頁是正常的",
    "run": "開始檢測",
    "paste": "從剪貼簿貼上",
    "step1": "已登入 ChatGPT 的瀏覽器裡打開 Session",
    "step2": "全選並複製整頁 JSON",
    "step3": "貼上後點「開始檢測」",
    "privacy": "只讀訂閱資訊，不改動帳號；Session 僅用於本次檢測、不落庫。查完建議回 Session 頁重新整理，剛貼的這份會失效。",
    "verdict_wait": "等待檢測",
    "again": "檢測另一個號",
    "pricing": "查看代儲價格",
    "qq": "QQ 客服 1002569303",
    "cs_h": "檢測結果拿不準？",
    "cs_sub": "把帳號情況或檢測結論發給客服，幫你確認能不能充",
    "open_qq": "點此打開 QQ 會話",
    "or_add": "（或添加 QQ 1002569303）",
    "see_support": "也可前往",
    "support_center": "客服中心",
    "for_faq": "查看常見問答。",
},
"ja": {
    "title": "ChatGPT アカウント確認 | GPTPro",
    "desc": "chatgpt.com/api/auth/session の JSON を貼り付け、プランと Plus 開通／更新可否を確認。読み取り専用、Session は保存しません。",
    "logo_sub": "ChatGPT アカウント確認",
    "cta": "サポートに連絡",
    "badge": "読み取り専用 · Session 非保存 · 注文不要",
    "h1a": "このアカウントは", "h1b": "開けますか？",
    "sub": "<code>chatgpt.com/api/auth/session</code> の全文 JSON（<strong>accessToken</strong> 必須）を貼り付け。数秒でプランと開通／アップグレード／更新可否が分かります。",
    "waiting": "貼り付け待ち",
    "open_session": "Session を開く",
    "copy_link": "リンクをコピー",
    "label": "Session JSON を貼り付け",
    "placeholder": "ログイン済みブラウザで Session を開く → Ctrl/Cmd+A → コピー → ここに貼り付け",
    "hint": "全文が長いのは正常です",
    "run": "確認開始",
    "paste": "クリップボードから貼り付け",
    "step1": "ChatGPT にログインしたブラウザで Session を開く",
    "step2": "全文 JSON を全選択してコピー",
    "step3": "貼り付けて「確認開始」をクリック",
    "privacy": "購読情報の読み取りのみ。Session は今回の確認のみに使用し保存しません。確認後は Session ページを更新してください。",
    "verdict_wait": "確認待ち",
    "again": "別のアカウントを確認",
    "pricing": "チャージ価格を見る",
    "qq": "QQ サポート 1002569303",
    "cs_h": "結果が分かりにくい？",
    "cs_sub": "アカウント状況や判定をサポートに送り、可否を確認できます",
    "open_qq": "QQ チャットを開く",
    "or_add": "（または QQ 1002569303 を追加）",
    "see_support": "または",
    "support_center": "サポートセンター",
    "for_faq": "で FAQ を確認。",
},
"ko": {
    "title": "ChatGPT 계정 확인 | GPTPro",
    "desc": "chatgpt.com/api/auth/session JSON을 붙여 요금제와 Plus 개통/갱신 가능 여부를 확인. 읽기 전용, Session 미저장.",
    "logo_sub": "ChatGPT 계정 확인",
    "cta": "고객지원 문의",
    "badge": "읽기 전용 · Session 미저장 · 주문 불필요",
    "h1a": "이 계정,", "h1b": "개통 가능한가요?",
    "sub": "<code>chatgpt.com/api/auth/session</code> 전체 JSON(<strong>accessToken</strong> 필수)을 붙여넣으세요. 몇 초 만에 요금제와 개통/업그레이드/갱신 가능 여부를 봅니다.",
    "waiting": "붙여넣기 대기",
    "open_session": "Session 열기",
    "copy_link": "링크 복사",
    "label": "Session JSON 붙여넣기",
    "placeholder": "로그인한 브라우저에서 Session 열기 → Ctrl/Cmd+A → 복사 → 여기에 붙여넣기",
    "hint": "내용이 길고 페이지를 가득 채우는 것은 정상입니다",
    "run": "확인 시작",
    "paste": "클립보드에서 붙여넣기",
    "step1": "ChatGPT에 로그인한 브라우저에서 Session 열기",
    "step2": "전체 JSON 선택 후 복사",
    "step3": "붙여넣은 뒤 「확인 시작」 클릭",
    "privacy": "구독 정보만 읽습니다. Session은 이번 확인에만 쓰이며 저장되지 않습니다. 확인 후 Session 페이지를 새로고침하세요.",
    "verdict_wait": "확인 대기",
    "again": "다른 계정 확인",
    "pricing": "충전 가격 보기",
    "qq": "QQ 고객지원 1002569303",
    "cs_h": "결과가 애매한가요?",
    "cs_sub": "계정 상황이나 판정을 고객지원에 보내 가능 여부를 확인하세요",
    "open_qq": "QQ 채팅 열기",
    "or_add": "(또는 QQ 1002569303 추가)",
    "see_support": "또는",
    "support_center": "고객센터",
    "for_faq": "에서 FAQ를 확인하세요.",
},
"es": {
    "title": "Comprobar cuenta ChatGPT | GPTPro",
    "desc": "Pega el JSON de chatgpt.com/api/auth/session para ver el plan y si se puede abrir o renovar Plus. Solo lectura; no se guarda la sesión.",
    "logo_sub": "Comprobar cuenta ChatGPT",
    "cta": "Contactar soporte",
    "badge": "Solo lectura · sesión no guardada · sin pedido",
    "h1a": "¿Se puede", "h1b": "abrir esta cuenta?",
    "sub": "Pega el JSON completo de <code>chatgpt.com/api/auth/session</code> (debe incluir <strong>accessToken</strong>). En segundos verás el plan y si puedes abrir / mejorar / renovar.",
    "waiting": "Esperando pegado",
    "open_session": "Abrir Session",
    "copy_link": "Copiar enlace",
    "label": "Pegar Session JSON",
    "placeholder": "Abre Session con sesión iniciada → Ctrl/Cmd+A → copia → pega aquí",
    "hint": "Que ocupe toda la página es normal",
    "run": "Empezar comprobación",
    "paste": "Pegar del portapapeles",
    "step1": "Abre Session en un navegador con ChatGPT iniciado",
    "step2": "Selecciona y copia todo el JSON",
    "step3": "Pega y pulsa Empezar comprobación",
    "privacy": "Solo lectura de la suscripción; la sesión se usa solo en esta comprobación y no se guarda. Después, actualiza la página Session.",
    "verdict_wait": "Esperando comprobación",
    "again": "Comprobar otra cuenta",
    "pricing": "Ver precios de recarga",
    "qq": "Soporte QQ 1002569303",
    "cs_h": "¿No te queda claro el resultado?",
    "cs_sub": "Envía el estado o el veredicto a soporte para confirmar elegibilidad",
    "open_qq": "Abrir chat QQ",
    "or_add": "(o añade QQ 1002569303)",
    "see_support": "O visita el",
    "support_center": "Centro de soporte",
    "for_faq": "para preguntas frecuentes.",
},
"ru": {
    "title": "Проверка аккаунта ChatGPT | GPTPro",
    "desc": "Вставьте JSON chatgpt.com/api/auth/session, чтобы увидеть план и возможность открыть/продлить Plus. Только чтение; сессия не сохраняется.",
    "logo_sub": "Проверка аккаунта ChatGPT",
    "cta": "Связаться с поддержкой",
    "badge": "Только чтение · сессия не хранится · заказ не нужен",
    "h1a": "Можно ли", "h1b": "открыть этот аккаунт?",
    "sub": "Вставьте полный JSON с <code>chatgpt.com/api/auth/session</code> (нужен <strong>accessToken</strong>). За секунды увидите план и можно ли открыть / апгрейд / продлить.",
    "waiting": "Ждём вставку",
    "open_session": "Открыть Session",
    "copy_link": "Копировать ссылку",
    "label": "Вставить Session JSON",
    "placeholder": "Откройте Session в браузере с входом → Ctrl/Cmd+A → копировать → вставить сюда",
    "hint": "Длинный текст на всю страницу — это нормально",
    "run": "Начать проверку",
    "paste": "Вставить из буфера",
    "step1": "Откройте Session в браузере, где вы вошли в ChatGPT",
    "step2": "Выделите и скопируйте весь JSON",
    "step3": "Вставьте и нажмите «Начать проверку»",
    "privacy": "Только чтение подписки; сессия используется только для этой проверки и не сохраняется. После проверки обновите страницу Session.",
    "verdict_wait": "Ожидание проверки",
    "again": "Проверить другой аккаунт",
    "pricing": "Смотреть цены пополнения",
    "qq": "QQ поддержка 1002569303",
    "cs_h": "Неясен результат?",
    "cs_sub": "Отправьте статус или вердикт в поддержку, чтобы подтвердить возможность",
    "open_qq": "Открыть чат QQ",
    "or_add": "(или добавьте QQ 1002569303)",
    "see_support": "Или откройте",
    "support_center": "Центр поддержки",
    "for_faq": "для частых вопросов.",
},
}


def build_check(code):
    u = UI[code]
    g = CHECK[code]
    t = dict(u)
    t["logo_sub"] = g["logo_sub"]
    _, _, html_lang, _ = locale_by_code(code)
    home = page_url(locale_by_code(code)[1], "")
    support = page_url(locale_by_code(code)[1], "support/")
    return (
        head_common(g['title'], g['desc'], html_lang, 'check/') + '\n'
        '<body>\n'
        + nav_html(code, 'check/', t, 'check', support, g['cta']) + '\n\n'
        '    <div class="container">\n'
        '        <section class="check-hero">\n'
        '            <div class="hero-badge">' + g['badge'] + '</div>\n'
        '            <h1 class="hero-title">' + g['h1a'] + '<span class="hero-title-accent">' + g['h1b'] + '</span></h1>\n'
        '            <p class="check-hero-sub">' + g['sub'] + '</p>\n'
        '        </section>\n'
        '        <section class="check-panel" id="check-panel">\n'
        '            <div class="check-panel-head">\n'
        '                <div class="check-source">\n'
        '                    <span class="check-source-dot" aria-hidden="true"></span>\n'
        '                    <span class="check-source-name">ChatGPT Session</span>\n'
        '                    <span class="check-status-pill" id="check-status-pill">' + g['waiting'] + '</span>\n'
        '                </div>\n'
        '                <div class="check-helpers">\n'
        '                    <a class="check-helper-link" id="check-open-session" href="https://chatgpt.com/api/auth/session" target="_blank" rel="noopener noreferrer">' + g['open_session'] + '</a>\n'
        '                    <button type="button" class="check-helper-btn" id="check-copy-link-btn">' + g['copy_link'] + '</button>\n'
        '                </div>\n'
        '            </div>\n'
        '            <label class="check-label" for="check-session-input">' + g['label'] + '</label>\n'
        '            <div class="check-field">\n'
        '                <textarea id="check-session-input" class="check-textarea" rows="9" spellcheck="false" autocomplete="off" placeholder="' + g['placeholder'] + '"></textarea>\n'
        '                <div class="check-field-hint" id="check-field-hint">' + g['hint'] + '</div>\n'
        '            </div>\n'
        '            <div class="check-actions">\n'
        '                <button type="button" class="btn-primary check-run-btn" id="check-run-btn">' + g['run'] + '</button>\n'
        '                <button type="button" class="btn-secondary check-paste-btn" id="check-paste-btn">' + g['paste'] + '</button>\n'
        '            </div>\n'
        '            <ol class="check-steps">\n'
        '                <li><span>1</span>' + g['step1'] + '</li>\n'
        '                <li><span>2</span>' + g['step2'] + '</li>\n'
        '                <li><span>3</span>' + g['step3'] + '</li>\n'
        '            </ol>\n'
        '            <p class="check-privacy" id="check-idle-note">' + g['privacy'] + '</p>\n'
        '        </section>\n'
        '        <section class="check-result" id="check-result" hidden>\n'
        '            <div class="check-result-card" id="check-result-card">\n'
        '                <div class="check-result-top">\n'
        '                    <span class="check-verdict-pill" id="check-verdict-pill">—</span>\n'
        '                    <span class="check-checked-at" id="check-checked-at"></span>\n'
        '                </div>\n'
        '                <h2 class="check-verdict-title" id="check-verdict-title">' + g['verdict_wait'] + '</h2>\n'
        '                <p class="check-verdict-msg" id="check-verdict-msg"></p>\n'
        '                <dl class="check-meta" id="check-meta"></dl>\n'
        '                <div class="check-cta" id="check-cta">\n'
        '                    <button type="button" class="check-again" id="check-again-btn">' + g['again'] + '</button>\n'
        '                    <a class="btn-primary" href="' + home + '#pricing" id="check-pricing-btn" hidden>' + g['pricing'] + '</a>\n'
        '                    <a class="btn-secondary" href="https://wpa.qq.com/msgrd?v=3&amp;uin=1002569303&amp;site=qq&amp;menu=yes" target="_blank" rel="noopener noreferrer" id="check-qq-btn" hidden>' + g['qq'] + '</a>\n'
        '                </div>\n'
        '            </div>\n'
        '        </section>\n'
        '        <section class="customer-service check-cs">\n'
        '            <h2>' + g['cs_h'] + '</h2>\n'
        '            <p class="cs-subtitle">' + g['cs_sub'] + '</p>\n'
        '            <div class="service-info">\n'
        '                <div class="service-item">\n'
        '                    <span class="service-label">' + u['cs_qq'] + '</span>\n'
        '                    <span class="service-value">1002569303</span>\n'
        '                </div>\n'
        '                <div class="service-note">\n'
        '                    <p><a class="inline-qq" href="https://wpa.qq.com/msgrd?v=3&amp;uin=1002569303&amp;site=qq&amp;menu=yes" target="_blank" rel="noopener noreferrer">' + g['open_qq'] + '</a> ' + g['or_add'] + '</p>\n'
        '                    <p>' + g['see_support'] + ' <a href="' + support + '">' + g['support_center'] + '</a> ' + g['for_faq'] + '</p>\n'
        '                </div>\n'
        '            </div>\n'
        '        </section>\n'
        '    </div>\n'
        + footer_html(code, t) + '\n'
        '    <script src="/script.js"></script>\n'
        '    <script src="/js/check.js"></script>\n'
        '</body>\n'
        '</html>\n'
    )

SUPPORT = {
"en": {
    "title": "Support Center · QQ 1002569303 | GPTPro",
    "desc": "GPTPro support: common top-up and Codex Q&A, human support via QQ 1002569303. No third-party chat plugins.",
    "logo_sub": "Support Center",
    "cta": "Talk to human",
    "badge": "QQ human support · quick on-site answers",
    "h1": "Support Center",
    "hero": "Tap a common question on the left for a quick answer; if that does not help, reach human support QQ <strong>1002569303</strong>.",
    "chat_title": "On-site quick answers",
    "chat_sub": "Preset replies · not a live LLM chat",
    "online": "Online",
    "hello": "Hi, I am the GPTPro on-site assistant. Tap a question below for a quick answer; for a human agent use «Talk to human QQ» on the right.",
    "qs": [
        ("recharge", "How do I top up Plus / Pro?"),
        ("codex", "How do I download Codex?"),
        ("reset", "When does quota reset?"),
        ("fail", "What if top-up fails?"),
        ("pay", "Which payment methods?"),
        ("human", "Talk to human QQ"),
    ],
    "contact_label": "Human support QQ",
    "contact_hint": "Support hours: 9:00–04:00. When messaging, include order ID / account email (masked OK) / screenshots for faster help.",
    "open_qq": "Open QQ chat",
    "open_client": "Open in QQ client",
    "topics": ["Top-up delivery & code issues", "Codex install & login", "Enterprise bulk / corporate pay"],
    "links_h": "Quick links",
    "link_radar": "Quota reset radar",
    "link_radar_d": "Friend link · reset schedule",
    "link_codex": "Codex download",
    "link_codex_d": "Store & install tips",
    "link_faq": "FAQ",
    "link_faq_d": "Safety, pricing, warranty",
    "link_home": "Top-up home",
    "link_home_d": "Plus / Pro pricing",
    "link_check": "Account check",
    "link_check_d": "See if Plus can be opened",
},
"zh-tw": {
    "title": "客服中心 · QQ 1002569303 | GPTPro代儲",
    "desc": "GPTPro代儲客服中心：常見儲值與 Codex 問答、轉人工 QQ 1002569303。",
    "logo_sub": "客服中心",
    "cta": "轉人工",
    "badge": "QQ 人工客服 · 站內速答",
    "h1": "客服中心",
    "hero": "點左側常見問題可快速查看說明；解決不了再轉人工 QQ <strong>1002569303</strong>。",
    "chat_title": "站內速答",
    "chat_sub": "預設回覆 · 非大模型即時對話",
    "online": "在線",
    "hello": "你好，我是 GPTPro代儲 站內助手。點下面常見問題可快速查看說明；需要人工時請右側「轉人工 QQ」。",
    "qs": [
        ("recharge", "如何儲值 Plus / Pro？"),
        ("codex", "Codex 怎麼下載？"),
        ("reset", "額度什麼時候重置？"),
        ("fail", "儲值失敗怎麼辦？"),
        ("pay", "支援哪些支付方式？"),
        ("human", "轉人工 QQ"),
    ],
    "contact_label": "人工客服 QQ",
    "contact_hint": "客服在線時間：9:00 - 翌日 4:00。留言時附上訂單號 / 帳號郵箱（可打碼）/ 問題截圖，方便更快處理。",
    "open_qq": "轉人工 QQ",
    "open_client": "用 QQ 客戶端打開",
    "topics": ["儲值到帳與卡密問題", "Codex 客戶端安裝與登入", "企業批量 / 對公諮詢"],
    "links_h": "快捷入口",
    "link_radar": "額度重置雷達",
    "link_radar_d": "友鏈 · 重置時間參考",
    "link_codex": "Codex 下載",
    "link_codex_d": "商店與安裝說明",
    "link_faq": "常見問題",
    "link_faq_d": "安全、價格、售後",
    "link_home": "儲值首頁",
    "link_home_d": "Plus / Pro 報價",
    "link_check": "帳號檢測",
    "link_check_d": "看能不能開 Plus",
},
"ja": {
    "title": "サポートセンター · QQ 1002569303 | GPTPro",
    "desc": "GPTPro サポート：チャージと Codex の FAQ、人工対応 QQ 1002569303。",
    "logo_sub": "サポートセンター",
    "cta": "有人サポート",
    "badge": "QQ 有人サポート · サイト内クイック回答",
    "h1": "サポートセンター",
    "hero": "左のよくある質問をタップして確認。解決しない場合は有人 QQ <strong>1002569303</strong> へ。",
    "chat_title": "サイト内クイック回答",
    "chat_sub": "定型返信 · リアルタイム LLM ではありません",
    "online": "オンライン",
    "hello": "こんにちは。GPTPro サイト内アシスタントです。下の質問をタップして確認。有人は右側「有人 QQ」へ。",
    "qs": [
        ("recharge", "Plus / Pro のチャージ方法は？"),
        ("codex", "Codex のダウンロードは？"),
        ("reset", "枠はいつリセット？"),
        ("fail", "チャージ失敗したら？"),
        ("pay", "支払い方法は？"),
        ("human", "有人 QQ"),
    ],
    "contact_label": "有人サポート QQ",
    "contact_hint": "対応時間 9:00〜翌4:00。注文番号・メール（マスク可）・スクショを添えると早いです。",
    "open_qq": "QQ チャットを開く",
    "open_client": "QQ クライアントで開く",
    "topics": ["チャージ反映・コード問題", "Codex インストールとログイン", "法人まとめ / 対公"],
    "links_h": "クイックリンク",
    "link_radar": "枠リセットレーダー",
    "link_radar_d": "友リンク · リセット目安",
    "link_codex": "Codex ダウンロード",
    "link_codex_d": "ストアと導入",
    "link_faq": "FAQ",
    "link_faq_d": "安全・価格・保証",
    "link_home": "チャージホーム",
    "link_home_d": "Plus / Pro 料金",
    "link_check": "アカウント確認",
    "link_check_d": "Plus 開通可否",
},
"ko": {
    "title": "고객센터 · QQ 1002569303 | GPTPro",
    "desc": "GPTPro 고객센터: 충전·Codex FAQ, 상담 QQ 1002569303.",
    "logo_sub": "고객센터",
    "cta": "상담원 연결",
    "badge": "QQ 상담 · 사이트 빠른 답변",
    "h1": "고객센터",
    "hero": "왼쪽 자주 묻는 질문을 눌러 확인하세요. 해결되지 않으면 상담 QQ <strong>1002569303</strong>.",
    "chat_title": "사이트 빠른 답변",
    "chat_sub": "미리 준비된 답변 · 실시간 LLM 아님",
    "online": "온라인",
    "hello": "안녕하세요. GPTPro 사이트 도우미입니다. 아래 질문을 눌러 확인하세요. 상담은 오른쪽 「상담 QQ」.",
    "qs": [
        ("recharge", "Plus / Pro 충전 방법?"),
        ("codex", "Codex 다운로드는?"),
        ("reset", "할당량은 언제 초기화?"),
        ("fail", "충전 실패 시?"),
        ("pay", "결제 수단은?"),
        ("human", "상담 QQ"),
    ],
    "contact_label": "상담 QQ",
    "contact_hint": "응대 9:00–익일 4:00. 주문번호·이메일(마스킹 가능)·스크린샷을 첨부하면 더 빠릅니다.",
    "open_qq": "QQ 채팅 열기",
    "open_client": "QQ 클라이언트로 열기",
    "topics": ["충전 반영·코드 문제", "Codex 설치·로그인", "기업 대량 / 법인 결제"],
    "links_h": "바로가기",
    "link_radar": "할당량 초기화 레이더",
    "link_radar_d": "우호 링크 · 초기화 참고",
    "link_codex": "Codex 다운로드",
    "link_codex_d": "스토어·설치",
    "link_faq": "FAQ",
    "link_faq_d": "안전·가격·보증",
    "link_home": "충전 홈",
    "link_home_d": "Plus / Pro 요금",
    "link_check": "계정 확인",
    "link_check_d": "Plus 개통 가능 여부",
},
"es": {
    "title": "Centro de soporte · QQ 1002569303 | GPTPro",
    "desc": "Soporte GPTPro: FAQ de recarga y Codex, humano por QQ 1002569303.",
    "logo_sub": "Centro de soporte",
    "cta": "Hablar con humano",
    "badge": "Soporte QQ · respuestas rápidas en el sitio",
    "h1": "Centro de soporte",
    "hero": "Pulsa una pregunta a la izquierda; si no basta, contacta QQ <strong>1002569303</strong>.",
    "chat_title": "Respuestas rápidas",
    "chat_sub": "Respuestas predefinidas · no es un LLM en vivo",
    "online": "En línea",
    "hello": "Hola, soy el asistente de GPTPro. Pulsa una pregunta abajo; para humano usa «Hablar con humano QQ» a la derecha.",
    "qs": [
        ("recharge", "¿Cómo recargo Plus / Pro?"),
        ("codex", "¿Cómo descargo Codex?"),
        ("reset", "¿Cuándo se reinicia la cuota?"),
        ("fail", "¿Si falla la recarga?"),
        ("pay", "¿Métodos de pago?"),
        ("human", "Hablar con humano QQ"),
    ],
    "contact_label": "Soporte humano QQ",
    "contact_hint": "Horario 9:00–04:00. Incluye nº de pedido / email (puede ir enmascarado) / capturas.",
    "open_qq": "Abrir chat QQ",
    "open_client": "Abrir en cliente QQ",
    "topics": ["Entrega y códigos", "Instalación y login Codex", "Empresas / pago corporativo"],
    "links_h": "Enlaces rápidos",
    "link_radar": "Radar de cuota",
    "link_radar_d": "Enlace amigo · reinicio",
    "link_codex": "Descarga Codex",
    "link_codex_d": "Tienda e instalación",
    "link_faq": "FAQ",
    "link_faq_d": "Seguridad, precios, garantía",
    "link_home": "Inicio de recarga",
    "link_home_d": "Precios Plus / Pro",
    "link_check": "Comprobar cuenta",
    "link_check_d": "Ver si se puede abrir Plus",
},
"ru": {
    "title": "Центр поддержки · QQ 1002569303 | GPTPro",
    "desc": "Поддержка GPTPro: FAQ по пополнению и Codex, человек через QQ 1002569303.",
    "logo_sub": "Центр поддержки",
    "cta": "Связаться с человеком",
    "badge": "QQ поддержка · быстрые ответы на сайте",
    "h1": "Центр поддержки",
    "hero": "Нажмите вопрос слева; если не помогло — QQ <strong>1002569303</strong>.",
    "chat_title": "Быстрые ответы",
    "chat_sub": "Готовые ответы · не живой LLM",
    "online": "Онлайн",
    "hello": "Здравствуйте, я помощник GPTPro. Нажмите вопрос ниже; для человека — «QQ» справа.",
    "qs": [
        ("recharge", "Как пополнить Plus / Pro?"),
        ("codex", "Как скачать Codex?"),
        ("reset", "Когда сбрасывается квота?"),
        ("fail", "Если пополнение не удалось?"),
        ("pay", "Какие способы оплаты?"),
        ("human", "Связаться с человеком QQ"),
    ],
    "contact_label": "Поддержка QQ",
    "contact_hint": "Онлайн 9:00–04:00. Укажите номер заказа / email (можно маскировать) / скриншоты.",
    "open_qq": "Открыть чат QQ",
    "open_client": "Открыть в клиенте QQ",
    "topics": ["Доставка и коды", "Установка и вход Codex", "Бизнес / корп. оплата"],
    "links_h": "Быстрые ссылки",
    "link_radar": "Радар сброса квоты",
    "link_radar_d": "Дружеская ссылка",
    "link_codex": "Скачать Codex",
    "link_codex_d": "Магазин и установка",
    "link_faq": "FAQ",
    "link_faq_d": "Безопасность, цены, гарантия",
    "link_home": "Главная пополнения",
    "link_home_d": "Цены Plus / Pro",
    "link_check": "Проверка аккаунта",
    "link_check_d": "Можно ли открыть Plus",
},
}


def build_support(code):
    u = UI[code]
    g = SUPPORT[code]
    t = dict(u)
    t["logo_sub"] = g["logo_sub"]
    loc = locale_by_code(code)
    _, prefix, html_lang, _ = loc
    home = page_url(prefix, "")
    faq = page_url(prefix, "faq/")
    check = page_url(prefix, "check/")
    btns = "\n".join(
        '                    <button type="button" data-q="' + k + '">' + lab + '</button>'
        for k, lab in g["qs"]
    )
    topics = "\n".join("                        <li>" + x + "</li>" for x in g["topics"])
    return (
        head_common(g['title'], g['desc'], html_lang, 'support/') + '\n'
        '<body>\n'
        + nav_html(code, 'support/', t, 'support', '#cs-contact', g['cta']) + '\n\n'
        '    <div class="container">\n'
        '        <section class="support-hero">\n'
        '            <div class="hero-badge">' + g['badge'] + '</div>\n'
        '            <h1 class="hero-title">' + g['h1'] + '</h1>\n'
        '            <p class="support-hero-sub">' + g['hero'] + '</p>\n'
        '        </section>\n'
        '        <section class="cs-layout" id="cs-panel">\n'
        '            <div class="cs-chat card-panel" id="cs-chat">\n'
        '                <div class="cs-chat-header">\n'
        '                    <div>\n'
        '                        <strong>' + g['chat_title'] + '</strong>\n'
        '                        <span class="cs-chat-sub">' + g['chat_sub'] + '</span>\n'
        '                    </div>\n'
        '                    <span class="cs-online-badge">' + g['online'] + '</span>\n'
        '                </div>\n'
        '                <div class="cs-chat-log" id="cs-chat-log" aria-live="polite">\n'
        '                    <div class="cs-bubble bot">' + g['hello'] + '</div>\n'
        '                </div>\n'
        '                <div class="cs-quick-replies" id="cs-quick-replies">\n'
        + btns + '\n'
        '                </div>\n'
        '            </div>\n'
        '            <aside class="cs-side" id="cs-contact">\n'
        '                <div class="cs-contact-card">\n'
        '                    <p class="cs-contact-label">' + g['contact_label'] + '</p>\n'
        '                    <p class="cs-contact-qq">1002569303</p>\n'
        '                    <p class="cs-contact-hint">' + g['contact_hint'] + '</p>\n'
        '                    <a class="btn-primary btn-block" href="https://wpa.qq.com/msgrd?v=3&amp;uin=1002569303&amp;site=qq&amp;menu=yes" target="_blank" rel="noopener noreferrer">' + g['open_qq'] + '</a>\n'
        '                    <a class="btn-secondary btn-block" href="tencent://message/?uin=1002569303">' + g['open_client'] + '</a>\n'
        '                    <ul class="cs-contact-topics">\n'
        + topics + '\n'
        '                    </ul>\n'
        '                </div>\n'
        '                <div class="cs-links-card card-panel">\n'
        '                    <h2>' + g['links_h'] + '</h2>\n'
        '                    <div class="links-grid compact">\n'
        '                        <a class="link-card" href="https://codexinstall.asia/zh/codex-reset/" target="_blank" rel="noopener noreferrer">\n'
        '                            <span class="link-icon">📡</span>\n'
        '                            <span class="link-title">' + g['link_radar'] + '</span>\n'
        '                            <span class="link-desc">' + g['link_radar_d'] + '</span>\n'
        '                        </a>\n'
        '                        <a class="link-card" href="/download-codex/">\n'
        '                            <span class="link-icon">⬇️</span>\n'
        '                            <span class="link-title">' + g['link_codex'] + '</span>\n'
        '                            <span class="link-desc">' + g['link_codex_d'] + '</span>\n'
        '                        </a>\n'
        '                        <a class="link-card" href="' + faq + '">\n'
        '                            <span class="link-icon">❓</span>\n'
        '                            <span class="link-title">' + g['link_faq'] + '</span>\n'
        '                            <span class="link-desc">' + g['link_faq_d'] + '</span>\n'
        '                        </a>\n'
        '                        <a class="link-card" href="' + home + '">\n'
        '                            <span class="link-icon">💳</span>\n'
        '                            <span class="link-title">' + g['link_home'] + '</span>\n'
        '                            <span class="link-desc">' + g['link_home_d'] + '</span>\n'
        '                        </a>\n'
        '                        <a class="link-card" href="' + check + '">\n'
        '                            <span class="link-icon">🔍</span>\n'
        '                            <span class="link-title">' + g['link_check'] + '</span>\n'
        '                            <span class="link-desc">' + g['link_check_d'] + '</span>\n'
        '                        </a>\n'
        '                    </div>\n'
        '                </div>\n'
        '            </aside>\n'
        '        </section>\n'
        '    </div>\n'
        + footer_html(code, t) + '\n'
        '    <script src="/script.js"></script>\n'
        '    <script src="/js/support.js"></script>\n'
        '</body>\n'
        '</html>\n'
    )
