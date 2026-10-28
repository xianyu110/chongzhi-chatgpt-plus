(function () {
    var DATA_URL = 'data/radar.json';
    var countdownTimer = null;

    function $(id) { return document.getElementById(id); }

    function formatDate(iso) {
        if (!iso) return '—';
        var d = new Date(iso);
        if (isNaN(d.getTime())) return iso;
        try {
            return new Intl.DateTimeFormat('zh-CN', {
                timeZone: 'Asia/Shanghai',
                year: 'numeric', month: '2-digit', day: '2-digit',
                hour: '2-digit', minute: '2-digit', hour12: false
            }).format(d) + ' (Asia/Shanghai)';
        } catch (e) {
            return d.toLocaleString('zh-CN');
        }
    }

    function pad(n) { return n < 10 ? '0' + n : String(n); }

    function renderCountdown(targetIso) {
        var el = $('radar-countdown');
        var hint = $('radar-next-hint');
        if (!el) return;
        function tick() {
            var target = new Date(targetIso).getTime();
            var now = Date.now();
            if (isNaN(target)) {
                el.textContent = '未设置';
                if (hint) hint.textContent = '请在 data/radar.json 填写 nextEstimate';
                return;
            }
            var diff = target - now;
            if (diff <= 0) {
                el.textContent = '已到预估点';
                if (hint) hint.textContent = '请刷新观测或更新 JSON；以账号内配额为准';
                return;
            }
            var sec = Math.floor(diff / 1000);
            var days = Math.floor(sec / 86400);
            sec %= 86400;
            var hours = Math.floor(sec / 3600);
            sec %= 3600;
            var mins = Math.floor(sec / 60);
            sec %= 60;
            el.textContent = (days > 0 ? days + '天 ' : '') + pad(hours) + ':' + pad(mins) + ':' + pad(sec);
            if (hint) hint.textContent = '预估时刻：' + formatDate(targetIso);
        }
        tick();
        if (countdownTimer) clearInterval(countdownTimer);
        countdownTimer = setInterval(tick, 1000);
    }

    function statusClass(status) {
        if (status === 'tight') return 'pill-warn';
        if (status === 'resetting') return 'pill-hot';
        return 'pill-ok';
    }

    function renderHistory(list) {
        var root = $('radar-history');
        if (!root) return;
        root.textContent = '';
        if (!list || !list.length) {
            var empty = document.createElement('li');
            empty.className = 'radar-timeline-item muted';
            empty.textContent = '暂无历史，请在 data/radar.json 的 history 中添加。';
            root.appendChild(empty);
            return;
        }
        list.forEach(function (item) {
            var li = document.createElement('li');
            li.className = 'radar-timeline-item';
            var time = document.createElement('time');
            time.textContent = formatDate(item.at);
            var h = document.createElement('h3');
            h.textContent = item.event || '观测记录';
            var p = document.createElement('p');
            p.textContent = item.detail || '';
            li.appendChild(time);
            li.appendChild(h);
            if (item.detail) li.appendChild(p);
            root.appendChild(li);
        });
    }

    function applyData(data) {
        var pill = $('radar-status-pill');
        if (pill) {
            pill.textContent = data.statusLabel || data.status || '观测中';
            pill.className = 'radar-pill ' + statusClass(data.status);
        }
        var updated = $('radar-updated');
        if (updated) updated.textContent = '数据更新：' + formatDate(data.updatedAt);
        var last = $('radar-last-reset');
        if (last) last.textContent = formatDate(data.lastResetAt);
        var next = $('radar-next-estimate');
        if (next) next.textContent = formatDate(data.nextEstimate);
        var tz = $('radar-tz');
        if (tz) tz.textContent = data.timezone || 'Asia/Shanghai';
        var note = $('radar-note');
        if (note) note.textContent = data.note || '';
        var btn = $('radar-source-btn');
        if (btn && data.sourceUrl) {
            btn.href = data.sourceUrl;
            btn.textContent = data.sourceLabel || '查看动态';
        }
        renderCountdown(data.nextEstimate);
        renderHistory(data.history || []);
    }

    function fail(msg) {
        var pill = $('radar-status-pill');
        if (pill) {
            pill.textContent = '数据未加载';
            pill.className = 'radar-pill pill-warn';
        }
        var hint = $('radar-next-hint');
        if (hint) hint.textContent = msg;
        var history = $('radar-history');
        if (history) {
            history.innerHTML = '';
            var li = document.createElement('li');
            li.className = 'radar-timeline-item muted';
            li.textContent = msg;
            history.appendChild(li);
        }
    }

    fetch(DATA_URL, { cache: 'no-store' })
        .then(function (res) {
            if (!res.ok) throw new Error('HTTP ' + res.status);
            return res.json();
        })
        .then(applyData)
        .catch(function () {
            fail('无法读取 data/radar.json，请确认文件已部署到 GitHub Pages。');
        });
})();
