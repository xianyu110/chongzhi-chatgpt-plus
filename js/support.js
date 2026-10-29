(function () {
    var LANG = (document.documentElement.lang || 'zh-CN').toLowerCase();
    function pick() {
        if (LANG.indexOf('zh-tw') === 0 || LANG.indexOf('zh-hk') === 0) return 'zh-TW';
        if (LANG.indexOf('zh') === 0) return 'zh-CN';
        if (LANG.indexOf('ja') === 0) return 'ja';
        if (LANG.indexOf('ko') === 0) return 'ko';
        if (LANG.indexOf('es') === 0) return 'es';
        if (LANG.indexOf('ru') === 0) return 'ru';
        return 'en';
    }
    var L = pick();

    var ALL = {
        'zh-CN': {
            recharge: { q: '如何充值 Plus / Pro？', a: '打开首页选择套餐下单，支持支付宝 / 微信 / QQ。卡密按发货说明兑换；直充按客服指引操作。企业批量请直接转人工 QQ。' },
            codex: { q: 'Codex 怎么下载？', a: 'Windows 优先用 Microsoft Store 搜索 ChatGPT（OpenAI）。本站「Codex下载」页有商店链接；买号后官方登录看 /blog/codex-direct/ 直连教程。若走 API/中转再看 doc.momoai 中转站教程。请勿使用篡改 API 的第三方安装器。' },
            reset: { q: '额度什么时候重置？', a: '请查看友链「额度重置雷达」（codexinstall.asia/zh/codex-reset/）。最终以账号内配额为准。' },
            fail: { q: '充值失败怎么办？', a: '保留订单号与支付截图，稍后重试；仍失败请转人工 QQ 1002569303，说明套餐与报错信息，我们会协助处理。' },
            pay: { q: '支持哪些支付方式？', a: '主流支持支付宝、微信、QQ。联系客服转账有时可免平台手续费；对公支付请备注企业信息后咨询 QQ。' },
            human: { q: '转人工 QQ', a: '请添加或点击右侧打开客服 QQ：1002569303。人工客服在线时间 9:00 - 次日 4:00。留言时附上订单号与问题截图会更快。' }
        },
        'zh-TW': {
            recharge: { q: '如何儲值 Plus / Pro？', a: '打開首頁選擇套餐下單，支援支付寶 / 微信 / QQ。卡密按發貨說明兌換；直充按客服指引操作。企業批量請直接轉人工 QQ。' },
            codex: { q: 'Codex 怎麼下載？', a: 'Windows 優先用 Microsoft Store 搜尋 ChatGPT（OpenAI）。本站「Codex下載」頁有商店連結；買號後官方登入看 /blog/codex-direct/ 直連教學。請勿使用篡改 API 的第三方安裝器。' },
            reset: { q: '額度什麼時候重置？', a: '請查看友鏈「額度重置雷達」（codexinstall.asia/zh/codex-reset/）。最終以帳號內配額為準。' },
            fail: { q: '儲值失敗怎麼辦？', a: '保留訂單號與支付截圖，稍後重試；仍失敗請轉人工 QQ 1002569303，說明套餐與報錯資訊。' },
            pay: { q: '支援哪些支付方式？', a: '主流支援支付寶、微信、QQ。聯絡客服轉帳有時可免平台手續費；對公支付請備註企業資訊後諮詢 QQ。' },
            human: { q: '轉人工 QQ', a: '請添加或點右側打開客服 QQ：1002569303。人工客服在線 9:00 - 翌日 4:00。留言附訂單號與截圖會更快。' }
        },
        en: {
            recharge: { q: 'How do I top up Plus / Pro?', a: 'Open the home page, pick a plan and order. Alipay / WeChat / QQ OK. Redeem codes per delivery notes; direct top-up follows support. For enterprise bulk, go straight to human QQ.' },
            codex: { q: 'How do I download Codex?', a: 'On Windows prefer Microsoft Store → ChatGPT (OpenAI). See our Codex download page for store links; after buying, use the official login /blog/codex-direct/ guide. Do not use third-party installers that patch the API.' },
            reset: { q: 'When does quota reset?', a: 'See the friend-link Quota Reset Radar (codexinstall.asia/zh/codex-reset/). Final truth is your in-account quota.' },
            fail: { q: 'What if top-up fails?', a: 'Keep order ID and payment screenshot, retry later; if still failing, human QQ 1002569303 with plan and error details.' },
            pay: { q: 'Which payment methods?', a: 'Alipay, WeChat, QQ mainly. Paying support directly may skip platform fees; corporate pay—note company info then ask QQ.' },
            human: { q: 'Talk to human QQ', a: 'Add or open support QQ 1002569303. Hours 9:00–04:00. Include order ID and screenshots for faster help.' }
        },
        ja: {
            recharge: { q: 'Plus / Pro のチャージ方法は？', a: 'ホームでプランを選び注文。Alipay / WeChat / QQ 対応。コードは案内どおり；直充はサポート指示。法人まとめは有人 QQ へ。' },
            codex: { q: 'Codex のダウンロードは？', a: 'Windows は Microsoft Store で ChatGPT（OpenAI）を優先。Codex ダウンロードページにリンクあり。第三者の改変インストーラは使わないでください。' },
            reset: { q: '枠はいつリセット？', a: '友リンク「枠リセットレーダー」（codexinstall.asia/zh/codex-reset/）を参照。最終はアカウント内枠。' },
            fail: { q: 'チャージ失敗したら？', a: '注文番号と支払スクショを残し再試行。続く場合は QQ 1002569303 へプランとエラーを。' },
            pay: { q: '支払い方法は？', a: '主に Alipay / WeChat / QQ。サポート振込で手数料回避の場合あり。対公は企業情報を添えて QQ へ。' },
            human: { q: '有人 QQ', a: 'サポート QQ 1002569303。対応 9:00〜翌4:00。注文番号とスクショがあると早いです。' }
        },
        ko: {
            recharge: { q: 'Plus / Pro 충전 방법?', a: '홈에서 요금제 선택 후 주문. Alipay / WeChat / QQ 지원. 코드는 안내대로; 직충은 고객지원 안내. 기업 대량은 상담 QQ.' },
            codex: { q: 'Codex 다운로드는?', a: 'Windows는 Microsoft Store에서 ChatGPT(OpenAI) 우선. Codex 다운로드 페이지 링크 참고. API를 변조한 타사 설치 프로그램은 사용하지 마세요.' },
            reset: { q: '할당량은 언제 초기화?', a: '우호 링크 할당량 초기화 레이더(codexinstall.asia/zh/codex-reset/) 참고. 최종은 계정 내 할당량.' },
            fail: { q: '충전 실패 시?', a: '주문번호와 결제 캡처를 보관하고 재시도. 계속되면 QQ 1002569303에 요금제·오류를 보내세요.' },
            pay: { q: '결제 수단은?', a: '주로 Alipay / WeChat / QQ. 고객지원 이체로 수수료 면제 가능. 법인 결제는 기업 정보와 함께 QQ 문의.' },
            human: { q: '상담 QQ', a: 'QQ 1002569303. 응대 9:00–익일 4:00. 주문번호와 스크린샷을 첨부하면 더 빠릅니다.' }
        },
        es: {
            recharge: { q: '¿Cómo recargo Plus / Pro?', a: 'En la portada elige un plan y pide. Alipay / WeChat / QQ. Códigos según entrega; recarga directa con soporte. Empresas: QQ humano.' },
            codex: { q: '¿Cómo descargo Codex?', a: 'En Windows prefer Microsoft Store → ChatGPT (OpenAI). Página Codex download tiene enlaces. No uses instaladores de terceros que parchean la API.' },
            reset: { q: '¿Cuándo se reinicia la cuota?', a: 'Ver el radar amigo (codexinstall.asia/zh/codex-reset/). La cuota en la cuenta manda.' },
            fail: { q: '¿Si falla la recarga?', a: 'Guarda nº de pedido y captura, reintenta; si sigue, QQ 1002569303 con plan y error.' },
            pay: { q: '¿Métodos de pago?', a: 'Alipay, WeChat, QQ. Transferir a soporte puede evitar comisiones; pago corporativo: datos de empresa + QQ.' },
            human: { q: 'Hablar con humano QQ', a: 'QQ 1002569303. Horario 9:00–04:00. Incluye nº de pedido y capturas.' }
        },
        ru: {
            recharge: { q: 'Как пополнить Plus / Pro?', a: 'На главной выберите план и оформите заказ. Alipay / WeChat / QQ. Коды по инструкции; прямое пополнение — через поддержку. Бизнес — сразу к QQ.' },
            codex: { q: 'Как скачать Codex?', a: 'На Windows предпочтителен Microsoft Store → ChatGPT (OpenAI). Ссылки на странице Codex. Не используйте сторонние установщики с патчем API.' },
            reset: { q: 'Когда сбрасывается квота?', a: 'См. радар (codexinstall.asia/zh/codex-reset/). Истина — квота в аккаунте.' },
            fail: { q: 'Если пополнение не удалось?', a: 'Сохраните номер заказа и скрин оплаты, повторите; иначе QQ 1002569303 с планом и ошибкой.' },
            pay: { q: 'Какие способы оплаты?', a: 'Alipay, WeChat, QQ. Перевод поддержке может без комиссии; корп. оплата — данные компании + QQ.' },
            human: { q: 'Связаться с человеком QQ', a: 'QQ 1002569303. Онлайн 9:00–04:00. Укажите номер заказа и скриншоты.' }
        }
    };
    var replies = ALL[L] || ALL.en;

    var log = document.getElementById('cs-chat-log');
    var buttons = document.querySelectorAll('#cs-quick-replies button');
    if (!log || !buttons.length) return;

    function addBubble(text, who) {
        var div = document.createElement('div');
        div.className = 'cs-bubble ' + who;
        div.textContent = text;
        log.appendChild(div);
        log.scrollTop = log.scrollHeight;
    }

    buttons.forEach(function (btn) {
        btn.addEventListener('click', function () {
            var key = btn.getAttribute('data-q');
            var item = replies[key];
            if (!item) return;
            buttons.forEach(function (b) { b.classList.remove('is-active'); });
            btn.classList.add('is-active');
            addBubble(item.q, 'user');
            setTimeout(function () {
                addBubble(item.a, 'bot');
                if (key === 'human') {
                    var contact = document.getElementById('cs-contact');
                    if (contact) contact.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                }
            }, 180);
        });
    });
})();
