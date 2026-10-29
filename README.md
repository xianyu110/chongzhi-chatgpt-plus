# GPT 代充公告页

这是 `chongzhi.chatgpt-plus.top` 的静态公告页，使用 GitHub Pages 发布。

## 最新公告

最新的 GPT 代充服务请联系 QQ 客服 **1002569303** 获取。请在确认服务内容、价格和售后规则后再进行交易。

## 本地预览

```bash
python3 -m http.server 8080
```

然后打开 <http://localhost:8080/>。

## 发布配置

- Pages 来源：`main` 分支根目录
- 自定义域名：<https://chongzhi.chatgpt-plus.top/>
- 客服 QQ：`1002569303`

## 页面（Clean URLs）

| URL | 说明 |
|-----|------|
| `/` | ChatGPT Plus / GPT Pro |
| `/en/` | English home |
| `/gemini/` | Gemini |
| `/grok/` | SuperGrok（购买入口主链 `https://wzyp.cn/item/6cegy9`，备用 `https://wzyp.cn/item/yfz403`） |
| `/claude/` | Claude Mail / Pro / Max（购买入口 `https://wzyp.cn/item/ahu0j7`） |
| `/faq/` | 常见问题 |
| `/check/` | ChatGPT 账号检测（Session → 可否开通/升级） |
| `/radar/` → `https://codexinstall.asia/zh/codex-reset/` | 额度重置雷达（友链跳转） |
| `/download-codex/` | Codex 下载教程 |
| `/support/` | 客服中心 |
| `/blog/codex-direct/` | 买号后直连 Codex |

旧的 `*.html` 路径保留薄跳转页，自动重定向到上述 clean URL。

## 品牌资源

- `/assets/icons/logo.svg`：导航栏图标
- `/assets/icons/favicon.svg` / `favicon.ico`：站点图标
- `/assets/icons/apple-touch-icon.png`：Apple touch icon
- `/assets/icons/og-icon.png`：OG 预览图
