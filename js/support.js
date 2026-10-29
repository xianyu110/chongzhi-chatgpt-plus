(function () {
    var replies = {
        recharge: {
            q: '如何充值 Plus / Pro？',
            a: '打开首页选择套餐下单，支持支付宝 / 微信 / QQ。卡密按发货说明兑换；直充按客服指引操作。企业批量请直接转人工 QQ。'
        },
        codex: {
            q: 'Codex 怎么下载？',
            a: 'Windows 优先用 Microsoft Store 搜索 ChatGPT（OpenAI）。本站「Codex下载」页有商店链接；买号后官方登录看 /blog/codex-direct/ 直连教程。若走 API/中转再看 doc.momoai 中转站教程。请勿使用篡改 API 的第三方安装器。'
        },
        reset: {
            q: '额度什么时候重置？',
            a: '请查看友链「额度重置雷达」（codexinstall.asia/zh/codex-reset/）。最终以账号内配额为准。'
        },
        fail: {
            q: '充值失败怎么办？',
            a: '保留订单号与支付截图，稍后重试；仍失败请转人工 QQ 1002569303，说明套餐与报错信息，我们会协助处理。'
        },
        pay: {
            q: '支持哪些支付方式？',
            a: '主流支持支付宝、微信、QQ。联系客服转账有时可免平台手续费；对公支付请备注企业信息后咨询 QQ。'
        },
        human: {
            q: '转人工 QQ',
            a: '请添加或点击右侧打开客服 QQ：1002569303。人工客服在线时间 9:00 - 次日 4:00。留言时附上订单号与问题截图会更快。'
        }
    };

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
