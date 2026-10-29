(function () {
    var API_BASE = 'https://gptpro-account-check.chatgpt-plus.workers.dev';
    var ENDPOINT = API_BASE + '/api/v1/account-check';
    var SESSION_URL = 'https://chatgpt.com/api/auth/session';

    var VERDICT_LABEL = {
        open: '可以开通',
        upgrade: '可以升级/续费',
        expired: 'Session 已失效',
        blocked: '暂时无法开通',
        unknown: '无法判断'
    };

    var PLAN_ZH = {
        free: '免费版',
        plus: 'Plus',
        pro: 'Pro',
        team: 'Team',
        enterprise: 'Enterprise',
        go: 'Go',
        unknown: '未知'
    };

    function $(id) { return document.getElementById(id); }

    function maskEmail(email) {
        if (!email || typeof email !== 'string') return '';
        var at = email.indexOf('@');
        if (at < 1) return email[0] + '***';
        var local = email.slice(0, at);
        var domain = email.slice(at);
        if (local.length <= 2) return local[0] + '***' + domain;
        return local.slice(0, 2) + '***' + local.slice(-1) + domain;
    }

    function formatBeijing(iso) {
        if (!iso) return '—';
        var d = new Date(iso);
        if (isNaN(d.getTime())) return String(iso);
        try {
            return new Intl.DateTimeFormat('zh-CN', {
                timeZone: 'Asia/Shanghai',
                year: 'numeric', month: '2-digit', day: '2-digit',
                hour: '2-digit', minute: '2-digit', second: '2-digit',
                hour12: false
            }).format(d) + '（北京时间）';
        } catch (e) {
            return d.toLocaleString('zh-CN');
        }
    }

    function planLabel(plan) {
        if (!plan) return '';
        if (plan.kind && PLAN_ZH[plan.kind]) {
            var zh = PLAN_ZH[plan.kind];
            if (plan.title && plan.title !== zh && plan.kind !== 'free') {
                return zh + '（' + plan.title + '）';
            }
            return zh;
        }
        return plan.title || plan.id || '';
    }

    function setLoading(on) {
        var btn = $('check-run-btn');
        if (!btn) return;
        btn.disabled = !!on;
        btn.textContent = on ? '检测中…' : '开始检测';
    }

    function pillClass(answer) {
        if (answer === 'open' || answer === 'upgrade') return 'check-pill-ok';
        if (answer === 'expired' || answer === 'blocked') return 'check-pill-warn';
        return 'check-pill-muted';
    }

    function addRow(root, label, value) {
        if (value === null || value === undefined || value === '') return;
        var dt = document.createElement('dt');
        dt.textContent = label;
        var dd = document.createElement('dd');
        dd.textContent = String(value);
        root.appendChild(dt);
        root.appendChild(dd);
    }

    function renderMeta(data) {
        var root = $('check-meta');
        if (!root) return;
        root.textContent = '';
        addRow(root, '邮箱', data.email ? maskEmail(data.email) : '');
        addRow(root, '用户名', data.name || '');
        addRow(root, '套餐', planLabel(data.plan));
        addRow(root, '订阅渠道', data.channel || data.billing_channel || '');
        addRow(root, '开通方式', data.open_method || data.fulfillment || '');
        addRow(root, '账号创建时间', data.created_at ? formatBeijing(data.created_at) : '');
        if (typeof data.renew === 'boolean') {
            addRow(root, '自动续费', data.renew ? '开启' : '关闭');
        }
        addRow(root, '有效期至', data.until ? formatBeijing(data.until) : '');
        addRow(root, '区域', data.region || '');
        addRow(root, '检测时间', data.checked_at ? formatBeijing(data.checked_at) : '');
    }

    function showResult(data, isError) {
        var section = $('check-result');
        var pill = $('check-verdict-pill');
        var title = $('check-verdict-title');
        var msg = $('check-verdict-msg');
        var pricing = $('check-pricing-btn');
        var qq = $('check-qq-btn');
        var at = $('check-checked-at');
        if (!section) return;
        section.hidden = false;

        var answer = data && data.answer ? data.answer : 'unknown';
        if (pill) {
            pill.textContent = VERDICT_LABEL[answer] || answer;
            pill.className = 'check-verdict-pill ' + pillClass(answer);
        }
        if (title) title.textContent = VERDICT_LABEL[answer] || '检测结果';
        if (msg) {
            msg.textContent =
                (data && data.message) ||
                (isError ? '检测失败，请稍后重试。' : '');
        }
        if (at) {
            at.textContent = data && data.checked_at
                ? formatBeijing(data.checked_at)
                : '';
        }
        renderMeta(data || {});
        var showCta = answer === 'open' || answer === 'upgrade';
        if (pricing) pricing.hidden = !showCta;
        if (qq) qq.hidden = !showCta;
        try {
            section.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        } catch (e) { /* ignore */ }
    }

    function resetForAnother() {
        var input = $('check-session-input');
        if (input) {
            input.value = '';
            input.focus();
        }
        var section = $('check-result');
        if (section) section.hidden = true;
        try {
            $('check-panel').scrollIntoView({ behavior: 'smooth', block: 'start' });
        } catch (e) { /* ignore */ }
    }

    function clientValidate(raw) {
        var text = (raw || '').trim();
        if (!text) {
            return { ok: false, message: '请先粘贴完整的 Session JSON。' };
        }
        var obj;
        try {
            obj = JSON.parse(text);
        } catch (e) {
            return {
                ok: false,
                message: '内容不是合法 JSON。请在 Session 页面全选复制完整返回后再试。'
            };
        }
        if (!obj || typeof obj !== 'object' || Array.isArray(obj)) {
            return { ok: false, message: 'Session 应为 JSON 对象。' };
        }
        if (!obj.accessToken || typeof obj.accessToken !== 'string' || obj.accessToken.length < 20) {
            return {
                ok: false,
                message: '未找到 accessToken。请确认粘贴的是 chatgpt.com/api/auth/session 的完整内容。'
            };
        }
        return { ok: true, text: text };
    }

    function runCheck() {
        var input = $('check-session-input');
        var raw = input ? input.value : '';
        var v = clientValidate(raw);
        if (!v.ok) {
            showResult({
                answer: 'unknown',
                message: v.message,
                checked_at: new Date().toISOString()
            }, true);
            return;
        }

        setLoading(true);
        fetch(ENDPOINT, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ session_data: v.text })
        })
            .then(function (res) {
                return res.json().then(function (data) {
                    return { status: res.status, data: data };
                }).catch(function () {
                    return {
                        status: res.status,
                        data: {
                            answer: 'unknown',
                            message: '服务返回无法解析，请稍后重试。'
                        }
                    };
                });
            })
            .then(function (pack) {
                var data = pack.data || {};
                if (pack.status === 422 || pack.status === 429) {
                    showResult({
                        answer: data.answer || 'unknown',
                        message: data.message || '请求无效',
                        checked_at: new Date().toISOString()
                    }, true);
                    return;
                }
                if (!data.answer && data.message) {
                    data.answer = 'unknown';
                }
                showResult(data, pack.status >= 400);
            })
            .catch(function () {
                showResult({
                    answer: 'unknown',
                    message: '网络异常，无法连接检测服务。请稍后重试或联系客服 QQ 1002569303。',
                    checked_at: new Date().toISOString()
                }, true);
            })
            .finally(function () {
                setLoading(false);
            });
    }

    function copySessionLink() {
        var btn = $('check-copy-link-btn');
        function done(ok) {
            if (!btn) return;
            var prev = btn.textContent;
            btn.textContent = ok ? '已复制' : '复制失败';
            setTimeout(function () { btn.textContent = prev; }, 1600);
        }
        if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(SESSION_URL).then(function () {
                done(true);
            }).catch(function () {
                done(false);
            });
            return;
        }
        try {
            var ta = document.createElement('textarea');
            ta.value = SESSION_URL;
            document.body.appendChild(ta);
            ta.select();
            document.execCommand('copy');
            document.body.removeChild(ta);
            done(true);
        } catch (e) {
            done(false);
        }
    }

    var btn = $('check-run-btn');
    if (btn) btn.addEventListener('click', runCheck);
    var again = $('check-again-btn');
    if (again) again.addEventListener('click', resetForAnother);
    var copyBtn = $('check-copy-link-btn');
    if (copyBtn) copyBtn.addEventListener('click', copySessionLink);
})();
