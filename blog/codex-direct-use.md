# 买号后直连使用 Codex：官方 ChatGPT 客户端登录指南（非中转站）

> **路径说明（请先看清）**  
> - **本文**：在 [GPTPro代充](https://chongzhi.chatgpt-plus.top/)（`chongzhi.chatgpt-plus.top`）购买 **ChatGPT Plus / GPT Pro** 或具备 Codex 能力的账号后，用 **官方 ChatGPT / Codex 客户端登录账号直连**。  
> - **另一条路（API / 中转站）**：若你走国内中转、API Key、cc-switch 配置，请看：  
>   [Codex 国内站｜中转站教程](https://doc.momoai.asia/blog/codex-china-gpt-5-6-launch)  
> 两条线不要混用：直连靠 **ChatGPT 账号订阅登录**；中转靠 **API Key + 中转域名**。

客服 QQ：**1002569303** · [客服中心](https://chongzhi.chatgpt-plus.top/support/) · [额度重置雷达](https://codexinstall.asia/zh/codex-reset/)

---

## 这篇写给谁？

适合已经在 **GPTPro代充 / chongzhi** 完成购买，希望尽快用上官方 Codex 的用户，例如：

- 购买了 **独享 ChatGPT Plus 账号**，或完成 Plus 代充 / 续费  
- 购买了 **GPT Pro**（5X / 20X / 50X 等）月卡充值  
- 账号本身已具备 Codex 使用资格，想用 **官方桌面端** 写代码、改项目  

不适合：只想免魔法、走 API 中转、用 cc-switch 填 `gpt-6-astra` 那一套——那是[中转站文章](https://doc.momoai.asia/blog/codex-china-gpt-5-6-launch)的路径。

---

## 直连 vs 中转：一眼分清

| 对比项 | 本文 · 买号后直连 | 中转站 / API 路径 |
| --- | --- | --- |
| 登录方式 | ChatGPT 账号（邮箱等，按发货说明） | API Key + 中转 Base URL |
| 客户端 | 官方 Microsoft Store / chatgpt.com / Mac 官方包 | 可配合 cc-switch 等 |
| 是否改 API 地址 | **不要改**，用官方登录 | 按中转教程配置 |
| 网络 | 需能正常访问官方 ChatGPT / OpenAI 服务 | 国内中转站强调免魔法 |
| 文档入口 | 本文 + [客户端下载页](https://chongzhi.chatgpt-plus.top/download-codex/) | [doc.momoai 中转教程](https://doc.momoai.asia/blog/codex-china-gpt-5-6-launch) |

---

## 第一步：确认你手上有可用的 Plus / Pro 账号

在 [GPTPro代充首页](https://chongzhi.chatgpt-plus.top/) 下单后，请以 **订单发货说明 / 客服消息** 为准，常见两类：

1. **独享账号**：客服或自动发货会给出登录所需信息（通常含邮箱等）。用发货信息登录官方客户端即可。  
2. **自有账号代充 / 直充**：你本来就有 ChatGPT 账号，站点完成 Plus / Pro 充值后，仍用 **你自己的邮箱** 登录；站点 FAQ 写明正规通道 **不需要你交出密码**（多为 session / 卡密流程）。

**请勿**：

- 在任何第三方「一键安装器」里粘贴密码或 API Key  
- 把直连账号的密码当成中转站 API Key 去填 cc-switch  
- 自行编造或猜测登录方式——发货方式以订单与客服 QQ **1002569303** 为准  

额度重置可参考友链 [额度重置雷达](https://codexinstall.asia/zh/codex-reset/)（手工观测数据，非伪装分钟级第三方接口）。

---

## 第二步：安装官方 Windows / Mac 客户端

优先官方渠道，安装细节与商店链接见：[Windows Codex / ChatGPT 客户端下载教程](https://chongzhi.chatgpt-plus.top/download-codex/)。

备用：**网盘下载**（夸克，Windows 本地包，提取码 `rTQw`）：https://pan.quark.cn/s/0f1763fe2ac9?pwd=rTQw

### Windows（推荐微软商店 .msix）

1. 打开系统自带 **Microsoft Store**。  
2. 搜索 **ChatGPT**（发布者 **OpenAI**），或打开 [商店详情页](https://apps.microsoft.com/detail/9plm9xgg6vks)。  
3. 点击「获取 / 安装」，等待官方 **.msix** 完成。  
4. 也可从 [chatgpt.com/download](https://chatgpt.com/download/) 进入官方下载页。  
5. 开始菜单打开 **ChatGPT**。新版桌面端集成 Chat、Work 与 **Codex**。

无商店环境可参考下载页中的 `winget` 备选说明；仍失败请联系 QQ 客服，**不要下载未签名「绿色破解版」**。

### macOS

1. 阅读 [OpenAI 学习中心 · App 文档](https://learn.chatgpt.com/docs/app)。  
2. 从 [chatgpt.com/download](https://chatgpt.com/download/) 或官方文档给出的渠道安装。  
3. 安装后用同一 ChatGPT 账号登录，再进入 Codex。

---

## 第三步：用已购账号登录（官方 Sign in with ChatGPT）

按 [官方认证说明](https://learn.chatgpt.com/docs/auth)：

1. 打开 ChatGPT 桌面端，在未登录界面选择 **Continue / 使用 ChatGPT 登录**。  
2. 浏览器会弹出登录页：用 **订单发货的账号** 或 **你自己完成代充的邮箱** 完成登录（密码、验证码等以 OpenAI 登录页与发货说明为准）。  
3. 浏览器授权成功后会回到客户端。  
4. 在个人资料 / 账户信息中确认套餐为 **Plus** 或 **Pro**（或客服告知的对应档位）。

**直连场景下：**

- 选 **Sign in with ChatGPT（订阅登录）**，而不是随便找一个第三方 Key。  
- 若你误选了「用 API Key 登录」，那是另一条计费与权限体系；想走中转请改看[中转站教程](https://doc.momoai.asia/blog/codex-china-gpt-5-6-launch)，不要把两套配置拧在一起。

---

## 第四步：第一次打开 Codex，核对模型与额度

1. 在桌面端切换到 **Codex**（或按官方文档：选择 Codex → **New chat**）。  
2. 开一个小任务试水，例如：  
   `帮我列出当前文件夹结构，并写一段 README 大纲。`  
3. 确认能正常回复、能读写你选择的工作区文件。  
4. 在账户 / 用量相关入口查看是否仍有 Codex 额度；额度节奏可对照 [雷达页](https://codexinstall.asia/zh/codex-reset/)。  
5. Plus 适合每周若干次集中编程；Pro 额度更高，适合更重度日常开发——以你购买的套餐为准。

---

## 常见坑（直连用户最容易踩）

### 1. 地区 / 网络打不开官方登录页

直连依赖官方 ChatGPT / OpenAI 服务可达。若浏览器登录页一直转圈、超时，先检查本机能否打开 [chatgpt.com](https://chatgpt.com/)。  
若你更希望「免魔法、走国内中转」，请改用 [中转站教程](https://doc.momoai.asia/blog/codex-china-gpt-5-6-launch)，而不是强行给官方客户端塞第三方 Endpoint。

### 2. 账号不是 Plus / Pro，Codex 额度很紧或功能不全

Codex 虽在多档计划有入口，但稳定编程额度通常需要 **Plus / Pro**（或企业档）。请确认代充已到账、客户端显示的套餐正确。未到账先查订单或找 QQ **1002569303**。

### 3. 第三方假安装包 / 会改 API 的「Codex 安装器」

部分不明 exe / 脚本会改写 API Endpoint、注入代理或窃取密钥。  
**只认**：Microsoft Store、chatgpt.com 官方下载、学习中心文档。详见[下载页安全提示](https://chongzhi.chatgpt-plus.top/download-codex/)。

### 4. 把直连和中转 API Key 搞混

| 错误做法 | 正确做法 |
| --- | --- |
| 买了 Plus 账号，却去填 momoai API Key | 官方客户端用账号登录即可 |
| 中转 Key 填进「官方订阅」流程 | 中转请跟中转文走 cc-switch |
| 同时开着错误代理 + 官方登录 | 先决定走哪条路径，再清掉冲突配置 |

### 5. 登录后找不到 Codex

确认已更新到集成 Codex 的 ChatGPT 桌面端；旧版独立 Codex 用户可按官网提示升级到 ChatGPT 后再打开 Codex。仍没有入口：截图发给客服 QQ **1002569303**。

---

## 推荐上手流程（收藏）

```text
在 GPTPro代充 购买 Plus / Pro（或完成代充）
→ 按发货说明确认可登录账号
→ 微软商店 / 官方页安装 ChatGPT 客户端
→ Sign in with ChatGPT（官方登录，不要乱填第三方 Key）
→ 打开 Codex → 小任务试跑
→ 对照雷达看额度重置；有问题找 QQ 1002569303
```

若中途改走 API / 中转：  
→ [Codex 国内站｜中转站完整教程](https://doc.momoai.asia/blog/codex-china-gpt-5-6-launch)

---

## 相关链接

- 本站首页（购买 Plus / Pro）：https://chongzhi.chatgpt-plus.top/  
- 客户端下载速览：https://chongzhi.chatgpt-plus.top/download-codex/  
- 额度重置雷达：https://codexinstall.asia/zh/codex-reset/  
- 客服中心：https://chongzhi.chatgpt-plus.top/support/  
- 客服 QQ：1002569303  
- 官方下载：https://chatgpt.com/download/  
- 官方 App 文档：https://learn.chatgpt.com/docs/app  
- **若你走 API / 中转（另一条路径）**：https://doc.momoai.asia/blog/codex-china-gpt-5-6-launch  

---

## 总结

买号 / 代充完成后，**直连 Codex** 的核心只有三件事：装官方客户端、用发货或自有账号完成 **Sign in with ChatGPT**、在应用内打开 Codex 做小任务验证。

这不是中转站那条线。中转站解决的是 API Key、国内域名与 cc-switch；本文解决的是 **Plus / Pro 账号 → 官方桌面端 → 原生 Codex**。

选错路径时，回到本页顶部的对照表，或直接问客服 QQ **1002569303**。
