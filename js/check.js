(function () {
    var API_BASE = 'https://gptpro-account-check.chatgpt-plus.workers.dev';
    var ENDPOINT = API_BASE + '/api/v1/account-check';
    var SESSION_URL = 'https://chatgpt.com/api/auth/session';

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

    var I18N = {
        'zh-CN': {
            verdict: { open: '可以开通', upgrade: '可以升级/续费', expired: 'Session 已失效', blocked: '暂时无法开通', unknown: '无法判断' },
            plan: { free: '免费版', plus: 'Plus', pro: 'Pro', team: 'Team', enterprise: 'Enterprise', go: 'Go', unknown: '未知' },
            waiting: '等待粘贴', pasted: '已粘贴', checking: '检测中', checkingEllipsis: '检测中…', run: '开始检测',
            result: '检测结果', failRetry: '检测失败，请稍后重试。',
            email: '邮箱', name: '用户名', planL: '套餐', channel: '订阅渠道', openMethod: '开通方式',
            created: '账号创建时间', renew: '自动续费', renewOn: '开启', renewOff: '关闭',
            until: '有效期至', region: '区域', checkedAt: '检测时间', beijing: '（北京时间）',
            needJson: '请先粘贴完整的 Session JSON。',
            badJson: '内容不是合法 JSON。请在 Session 页面全选复制完整返回后再试。',
            needObj: 'Session 应为 JSON 对象。',
            needToken: '未找到 accessToken。请确认粘贴的是 chatgpt.com/api/auth/session 的完整内容。',
            badResp: '服务返回无法解析，请稍后重试。', badReq: '请求无效',
            netErr: '网络异常，无法连接检测服务。请稍后重试或联系客服 QQ 1002569303。',
            copied: '已复制', copyFail: '复制失败',
            noClip: '当前浏览器不支持读取剪贴板，请手动粘贴到输入框。',
            clipDenied: '无法读取剪贴板，请允许权限后重试，或手动粘贴。'
        },
        'zh-TW': {
            verdict: { open: '可以開通', upgrade: '可以升級/續費', expired: 'Session 已失效', blocked: '暫時無法開通', unknown: '無法判斷' },
            plan: { free: '免費版', plus: 'Plus', pro: 'Pro', team: 'Team', enterprise: 'Enterprise', go: 'Go', unknown: '未知' },
            waiting: '等待貼上', pasted: '已貼上', checking: '檢測中', checkingEllipsis: '檢測中…', run: '開始檢測',
            result: '檢測結果', failRetry: '檢測失敗，請稍後重試。',
            email: '郵箱', name: '用戶名', planL: '套餐', channel: '訂閱渠道', openMethod: '開通方式',
            created: '帳號建立時間', renew: '自動續費', renewOn: '開啟', renewOff: '關閉',
            until: '有效期至', region: '區域', checkedAt: '檢測時間', beijing: '（北京時間）',
            needJson: '請先貼上完整的 Session JSON。',
            badJson: '內容不是合法 JSON。請在 Session 頁面全選複製完整回傳後再試。',
            needObj: 'Session 應為 JSON 物件。',
            needToken: '未找到 accessToken。請確認貼上的是 chatgpt.com/api/auth/session 的完整內容。',
            badResp: '服務回傳無法解析，請稍後重試。', badReq: '請求無效',
            netErr: '網路異常，無法連線檢測服務。請稍後重試或聯絡客服 QQ 1002569303。',
            copied: '已複製', copyFail: '複製失敗',
            noClip: '目前瀏覽器不支援讀取剪貼簿，請手動貼到輸入框。',
            clipDenied: '無法讀取剪貼簿，請允許權限後重試，或手動貼上。'
        },
        en: {
            verdict: { open: 'Can open', upgrade: 'Can upgrade / renew', expired: 'Session expired', blocked: 'Temporarily blocked', unknown: 'Unknown' },
            plan: { free: 'Free', plus: 'Plus', pro: 'Pro', team: 'Team', enterprise: 'Enterprise', go: 'Go', unknown: 'Unknown' },
            waiting: 'Waiting for paste', pasted: 'Pasted', checking: 'Checking', checkingEllipsis: 'Checking…', run: 'Start check',
            result: 'Check result', failRetry: 'Check failed. Please try again later.',
            email: 'Email', name: 'Name', planL: 'Plan', channel: 'Billing channel', openMethod: 'Open method',
            created: 'Account created', renew: 'Auto-renew', renewOn: 'On', renewOff: 'Off',
            until: 'Valid until', region: 'Region', checkedAt: 'Checked at', beijing: ' (Beijing time)',
            needJson: 'Please paste the full Session JSON first.',
            badJson: 'Not valid JSON. Select all and copy the full Session page response.',
            needObj: 'Session should be a JSON object.',
            needToken: 'accessToken not found. Paste the full chatgpt.com/api/auth/session content.',
            badResp: 'Unreadable server response. Please retry later.', badReq: 'Invalid request',
            netErr: 'Network error. Retry later or contact QQ 1002569303.',
            copied: 'Copied', copyFail: 'Copy failed',
            noClip: 'This browser cannot read the clipboard. Paste manually.',
            clipDenied: 'Clipboard access denied. Allow permission or paste manually.'
        },
        ja: {
            verdict: { open: '開通可能', upgrade: 'アップグレード／更新可', expired: 'Session 失効', blocked: '一時的に不可', unknown: '判定不可' },
            plan: { free: '無料', plus: 'Plus', pro: 'Pro', team: 'Team', enterprise: 'Enterprise', go: 'Go', unknown: '不明' },
            waiting: '貼り付け待ち', pasted: '貼り付け済', checking: '確認中', checkingEllipsis: '確認中…', run: '確認開始',
            result: '確認結果', failRetry: '確認に失敗しました。後でもう一度お試しください。',
            email: 'メール', name: 'ユーザー名', planL: 'プラン', channel: '課金チャネル', openMethod: '開通方法',
            created: 'アカウント作成', renew: '自動更新', renewOn: 'オン', renewOff: 'オフ',
            until: '有効期限', region: '地域', checkedAt: '確認時刻', beijing: '（北京時間）',
            needJson: '先に Session JSON 全文を貼り付けてください。',
            badJson: 'JSON として不正です。Session ページで全文をコピーしてください。',
            needObj: 'Session は JSON オブジェクトである必要があります。',
            needToken: 'accessToken が見つかりません。chatgpt.com/api/auth/session の全文を貼り付けてください。',
            badResp: 'サーバー応答を解析できません。後で再試行してください。', badReq: '無効なリクエスト',
            netErr: 'ネットワークエラー。後で再試行するか QQ 1002569303 へ。',
            copied: 'コピー済', copyFail: 'コピー失敗',
            noClip: 'このブラウザはクリップボードを読めません。手動で貼り付けてください。',
            clipDenied: 'クリップボード権限がありません。許可するか手動で貼り付けてください。'
        },
        ko: {
            verdict: { open: '개통 가능', upgrade: '업그레이드/갱신 가능', expired: 'Session 만료', blocked: '일시적으로 불가', unknown: '판단 불가' },
            plan: { free: '무료', plus: 'Plus', pro: 'Pro', team: 'Team', enterprise: 'Enterprise', go: 'Go', unknown: '알 수 없음' },
            waiting: '붙여넣기 대기', pasted: '붙여넣음', checking: '확인 중', checkingEllipsis: '확인 중…', run: '확인 시작',
            result: '확인 결과', failRetry: '확인 실패. 나중에 다시 시도하세요.',
            email: '이메일', name: '사용자명', planL: '요금제', channel: '결제 채널', openMethod: '개통 방식',
            created: '계정 생성', renew: '자동 갱신', renewOn: '켜짐', renewOff: '꺼짐',
            until: '유효 기간', region: '지역', checkedAt: '확인 시각', beijing: ' (베이징 시간)',
            needJson: '먼저 전체 Session JSON을 붙여넣으세요.',
            badJson: '올바른 JSON이 아닙니다. Session 페이지에서 전체를 복사하세요.',
            needObj: 'Session은 JSON 객체여야 합니다.',
            needToken: 'accessToken이 없습니다. chatgpt.com/api/auth/session 전체 내용을 붙여넣으세요.',
            badResp: '서버 응답을 해석할 수 없습니다. 나중에 다시 시도하세요.', badReq: '잘못된 요청',
            netErr: '네트워크 오류. 나중에 재시도하거나 QQ 1002569303으로 문의하세요.',
            copied: '복사됨', copyFail: '복사 실패',
            noClip: '이 브라우저는 클립보드를 읽을 수 없습니다. 직접 붙여넣으세요.',
            clipDenied: '클립보드 권한이 없습니다. 허용하거나 직접 붙여넣으세요.'
        },
        es: {
            verdict: { open: 'Se puede abrir', upgrade: 'Se puede mejorar / renovar', expired: 'Session caducada', blocked: 'Temporalmente bloqueado', unknown: 'Desconocido' },
            plan: { free: 'Gratis', plus: 'Plus', pro: 'Pro', team: 'Team', enterprise: 'Enterprise', go: 'Go', unknown: 'Desconocido' },
            waiting: 'Esperando pegado', pasted: 'Pegado', checking: 'Comprobando', checkingEllipsis: 'Comprobando…', run: 'Empezar comprobación',
            result: 'Resultado', failRetry: 'Falló la comprobación. Inténtalo más tarde.',
            email: 'Correo', name: 'Nombre', planL: 'Plan', channel: 'Canal de facturación', openMethod: 'Método de apertura',
            created: 'Cuenta creada', renew: 'Renovación automática', renewOn: 'Sí', renewOff: 'No',
            until: 'Válido hasta', region: 'Región', checkedAt: 'Comprobado', beijing: ' (hora de Pekín)',
            needJson: 'Pega primero el Session JSON completo.',
            badJson: 'JSON no válido. Copia toda la respuesta de la página Session.',
            needObj: 'Session debe ser un objeto JSON.',
            needToken: 'No se encontró accessToken. Pega el contenido completo de chatgpt.com/api/auth/session.',
            badResp: 'Respuesta ilegible. Reintenta más tarde.', badReq: 'Solicitud inválida',
            netErr: 'Error de red. Reintenta o contacta QQ 1002569303.',
            copied: 'Copiado', copyFail: 'Error al copiar',
            noClip: 'Este navegador no puede leer el portapapeles. Pega manualmente.',
            clipDenied: 'Sin permiso de portapapeles. Permite o pega a mano.'
        },
        ru: {
            verdict: { open: 'Можно открыть', upgrade: 'Можно апгрейд / продлить', expired: 'Session истекла', blocked: 'Временно недоступно', unknown: 'Неизвестно' },
            plan: { free: 'Бесплатный', plus: 'Plus', pro: 'Pro', team: 'Team', enterprise: 'Enterprise', go: 'Go', unknown: 'Неизвестно' },
            waiting: 'Ждём вставку', pasted: 'Вставлено', checking: 'Проверка', checkingEllipsis: 'Проверка…', run: 'Начать проверку',
            result: 'Результат', failRetry: 'Проверка не удалась. Попробуйте позже.',
            email: 'Email', name: 'Имя', planL: 'План', channel: 'Канал оплаты', openMethod: 'Способ открытия',
            created: 'Аккаунт создан', renew: 'Автопродление', renewOn: 'Вкл.', renewOff: 'Выкл.',
            until: 'Действует до', region: 'Регион', checkedAt: 'Проверено', beijing: ' (время Пекина)',
            needJson: 'Сначала вставьте полный Session JSON.',
            badJson: 'Неверный JSON. Скопируйте полный ответ страницы Session.',
            needObj: 'Session должен быть JSON-объектом.',
            needToken: 'accessToken не найден. Вставьте полный ответ chatgpt.com/api/auth/session.',
            badResp: 'Ответ сервера не читается. Повторите позже.', badReq: 'Неверный запрос',
            netErr: 'Сетевая ошибка. Повторите или напишите QQ 1002569303.',
            copied: 'Скопировано', copyFail: 'Ошибка копирования',
            noClip: 'Браузер не читает буфер. Вставьте вручную.',
            clipDenied: 'Нет доступа к буферу. Разрешите или вставьте вручную.'
        }
    };
    var T = I18N[L] || I18N.en;
    var VERDICT_LABEL = T.verdict;
    var PLAN_ZH = T.plan;

    function $(id) { return document.getElementById(id); }

    function setStatus(kind, text) {
        var pill = $('check-status-pill');
        var dot = document.querySelector('.check-source-dot');
        if (pill) {
            pill.textContent = text;
            pill.classList.remove('is-ready', 'is-busy');
            if (kind === 'ready') pill.classList.add('is-ready');
            if (kind === 'busy') pill.classList.add('is-busy');
        }
        if (dot) {
            dot.classList.remove('is-ready', 'is-busy');
            if (kind === 'ready') dot.classList.add('is-ready');
            if (kind === 'busy') dot.classList.add('is-busy');
        }
    }

    function syncInputState() {
        var input = $('check-session-input');
        if (!input) return;
        var has = input.value.trim().length > 0;
        input.classList.toggle('has-content', has);
        var hint = $('check-field-hint');
        if (hint) hint.style.opacity = has ? '0' : '1';
        if (has) setStatus('ready', T.pasted);
        else setStatus('', T.waiting);
    }

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
        var loc = L === 'en' ? 'en-US' : (L === 'zh-TW' ? 'zh-TW' : (L === 'zh-CN' ? 'zh-CN' : L));
        try {
            return new Intl.DateTimeFormat(loc, {
                timeZone: 'Asia/Shanghai',
                year: 'numeric', month: '2-digit', day: '2-digit',
                hour: '2-digit', minute: '2-digit', second: '2-digit',
                hour12: false
            }).format(d) + T.beijing;
        } catch (e) {
            return d.toLocaleString(loc);
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
        var paste = $('check-paste-btn');
        if (!btn) return;
        btn.disabled = !!on;
        btn.textContent = on ? T.checkingEllipsis : T.run;
        if (paste) paste.disabled = !!on;
        if (on) setStatus('busy', T.checking);
        else syncInputState();
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
        addRow(root, T.email, data.email ? maskEmail(data.email) : '');
        addRow(root, T.name, data.name || '');
        addRow(root, T.planL, planLabel(data.plan));
        addRow(root, T.channel, data.channel || data.billing_channel || '');
        addRow(root, T.openMethod, data.open_method || data.fulfillment || '');
        addRow(root, T.created, data.created_at ? formatBeijing(data.created_at) : '');
        if (typeof data.renew === 'boolean') {
            addRow(root, T.renew, data.renew ? T.renewOn : T.renewOff);
        }
        addRow(root, T.until, data.until ? formatBeijing(data.until) : '');
        addRow(root, T.region, data.region || '');
        addRow(root, T.checkedAt, data.checked_at ? formatBeijing(data.checked_at) : '');
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
        if (title) title.textContent = VERDICT_LABEL[answer] || T.result;
        if (msg) {
            msg.textContent =
                (data && data.message) ||
                (isError ? T.failRetry : '');
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
            return { ok: false, message: T.needJson };
        }
        var obj;
        try {
            obj = JSON.parse(text);
        } catch (e) {
            return { ok: false, message: T.badJson };
        }
        if (!obj || typeof obj !== 'object' || Array.isArray(obj)) {
            return { ok: false, message: T.needObj };
        }
        if (!obj.accessToken || typeof obj.accessToken !== 'string' || obj.accessToken.length < 20) {
            return { ok: false, message: T.needToken };
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
                        data: { answer: 'unknown', message: T.badResp }
                    };
                });
            })
            .then(function (pack) {
                var data = pack.data || {};
                if (pack.status === 422 || pack.status === 429) {
                    showResult({
                        answer: data.answer || 'unknown',
                        message: data.message || T.badReq,
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
                    message: T.netErr,
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
            btn.textContent = ok ? T.copied : T.copyFail;
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

    var sessionInput = $('check-session-input');
    if (sessionInput) {
        sessionInput.addEventListener('input', syncInputState);
        sessionInput.addEventListener('paste', function () {
            window.setTimeout(syncInputState, 0);
        });
        syncInputState();
    }

    var pasteBtn = $('check-paste-btn');
    if (pasteBtn) {
        pasteBtn.addEventListener('click', function () {
            if (!navigator.clipboard || !navigator.clipboard.readText) {
                alert(T.noClip);
                return;
            }
            navigator.clipboard.readText().then(function (text) {
                var input = $('check-session-input');
                if (!input) return;
                input.value = text || '';
                syncInputState();
                input.focus();
            }).catch(function () {
                alert(T.clipDenied);
            });
        });
    }
})();
