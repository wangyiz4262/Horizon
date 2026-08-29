---
layout: default
title: "Horizon Summary: 2026-08-29 (ZH)"
date: 2026-08-29
lang: zh
---

> 从 34 条内容中筛选出 13 条重要资讯。

---

**科技新闻**
1. [Htmx 4.0 发布：超媒体驱动 JavaScript 库迎来主要更新](#item-tech-news-1) ⭐️ 8.0/10
2. [漏洞传闻足以变成可利用漏洞](#item-tech-news-2) ⭐️ 8.0/10
3. [腾讯混元发布 Hy4 preview：770B 参数、1M 上下文，盲测略胜 GLM-5.3 与 Kimi K3](#item-tech-news-3) ⭐️ 8.0/10
4. [智谱开源 GLM-5.3：聚焦智能体编程与网络防御](#item-tech-news-4) ⭐️ 8.0/10
5. [OpenAI 宣布 SpaceX 收购 Cursor 后的模型访问决定](#item-tech-news-5) ⭐️ 7.0/10
6. [美国制裁意大利托管商 Autistici/Inventati 引担忧](#item-tech-news-6) ⭐️ 7.0/10
7. [在 RP2350 微控制器上运行微型图像生成模型](#item-tech-news-7) ⭐️ 7.0/10

**财经新闻**
1. [两部门将个人住房贷款期限上限由 30 年延长至 40 年](#item-finance-news-1) ⭐️ 8.0/10
2. [玉米和小麦期货价格升至三年多来最高水平](#item-finance-news-2) ⭐️ 7.0/10
3. [美上诉法院：体育赛事合约非联邦监管掉期，或上诉至最高法院](#item-finance-news-3) ⭐️ 7.0/10
4. [沃什鹰派讲话后，市场预计美联储 9 月加息概率约 56%](#item-finance-news-4) ⭐️ 7.0/10
5. [美联储主席沃什将在杰克逊霍尔发表讲话，市场关注政策信号](#item-finance-news-5) ⭐️ 7.0/10
6. [美元兑日元重回 160，日美干预效果回撤](#item-finance-news-6) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Htmx 4.0 发布：超媒体驱动 JavaScript 库迎来主要更新](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released) ⭐️ 8.0/10

Htmx 4.0 正式发布，这是广受欢迎的 hypermedia 驱动 JavaScript 库的一次主要版本更新。发布中包含了对 Alpine.js 兼容性的改进（如 hx-alpine-compat），并继续坚持服务端渲染与超媒体优先的设计理念。社区反馈显示，部分开发者认为它简化了 Go 和 SQLite 等轻量技术栈的开发，但也有熟悉 .NET 与 Angular 的开发者指出，使用 HTMX 需要将展示逻辑移回后端，增加了混合关注点的复杂度。总体而言，这一版本被视为对前端过度复杂化的一次正面回应。

hackernews · rmsaksida · 8月28日 13:28 · [社区讨论](https://news.ycombinator.com/item?id=49478178)

**「背景」** htmx 是一个使用超媒体（HTML 片段）理念的 JavaScript 库，开发者通过类属性（如 hx-get）在浏览器端发起异步请求，并用返回的 HTML 响应直接更新页面，无需编写大量复杂的前端 JavaScript。htmx 4.0 是该库的一次重大版本升级，根据官方公告于 2026 年 8 月 28 日发布，主要变化包括从 XMLHttpRequest 切换到现代 fetch\(\) API、引入显式属性继承的 :inherited 修饰符，以及原生流式支持。理解这些背景有助于把握 htmx 在服务端渲染与 Web 开发中的定位，以及这次升级带来的技术基础变化。

**「社区讨论」** 社区反响总体积极：HTMX CEO 表示期待新版本，有开发者称“htmx 带来快乐”，并将其与 Go、SQLite 搭配使用。但也存在不同看法：熟悉 .NET 和 Angular 的开发者认为 HTMX 迫使后端混合展示与业务逻辑，而另一些开发者则推荐更轻量的替代方案如 alpine-ajax。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released">htmx 4 . 0 .0 has been released ! ~ htmx</a></li>
<li><a href="https://daily.dev/posts/announcing-htmx-4-0-embracing-the-fetch-api-and-modern-enhancements-mxhcluue6">Announcing htmx 4 . 0 : Embracing the Fetch API and Modern...</a></li>

</ul>
</details>

**标签**: `#htmx`, `#web development`, `#hypermedia`, `#JavaScript`, `#open source`

---

<a id="item-tech-news-2"></a>
### [漏洞传闻足以变成可利用漏洞](https://anil.recoil.org/notes/rumour-is-the-exploit) ⭐️ 8.0/10

这篇文章认为，借助 AI 工具，安全研究人员如今仅需一条漏洞传闻，就能快速生成可用的漏洞利用程序；维护者也证实 AI 生成的安全报告数量大幅增加。rclone 维护者 nickcw 表示，项目成立的前 10 年通过 GitHub 收到约 20 份安全披露，而最近一个月就收到 40 多份，其中约 75%包含需要关注的问题，占用了大量维护时间。评论中还提到有人构建了监控提交并尝试检测静默 bug 修复的工具，认为 AI 让漏洞研究和批量利用的规模与门槛都发生了显著变化。

hackernews · avsm · 8月28日 15:58 · [社区讨论](https://news.ycombinator.com/item?id=49480466)

**「背景」** 过去，从一句模糊的漏洞传闻发展出可用的安全攻击通常依赖研究者的深厚经验和对补丁、提交信息的逆向分析，门槛较高。如今，基于大语言模型的代理式漏洞利用系统（如文中提到的通过 Claude Fable 发现的报告）只需一个漏洞传闻即可快速生成攻击代码，而公开代码仓库的自动化监控者会在数分钟内对可疑修改发起探测，例如该网站发布笔记约十分钟后就收到针对百分号编码路径遍历序列的探测。这使得漏洞利用的开发与投递周期大幅压缩，也导致开源维护者收到的安全披露数量激增，例如 rclone 项目过去十年约收到 20 份，而最近一个月就超过 40 份。

**「影响」** 开源维护者正面临安全披露数量激增、质量参差不齐的局面，AI 工具虽能辅助分类和修复，但修复意愿不足以及部署和供应链更新缓慢会放大实际风险。

**「社区讨论」** 评论者普遍认同 AI 降低了漏洞利用开发的门槛，但也有人认为这并非全新现象，只是被大规模、民主化地用于低价值目标。另有讨论强调，即使 AI 能更快发现和修复 bug，缺乏修复意愿以及部署和供应链问题仍是关键瓶颈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://anil.recoil.org/notes/rumour-is-the-exploit">Just a rumour of a bug is enough to find a security exploit these ...</a></li>
<li><a href="https://simonwillison.net/2026/Aug/28/just-a-rumour-of-a-bug/">Just a rumour of a bug is enough to find a security exploit these ...</a></li>

</ul>
</details>

**标签**: `#AI security`, `#LLMs`, `#vulnerability research`, `#open source`, `#exploit development`

---

<a id="item-tech-news-3"></a>
### [腾讯混元发布 Hy4 preview：770B 参数、1M 上下文，盲测略胜 GLM-5.3 与 Kimi K3](https://mp.weixin.qq.com/s/ymr3X878B8oa2XP15CH8TQ) ⭐️ 8.0/10

2026 年 8 月 28 日，腾讯发布开源模型 Hy4 preview，总参数量 770B、活跃参数 49B、上下文窗口 1M token，主攻长周期软件工程、文档办公与科学研究，已上线腾讯云、GitHub、HuggingFace、ModelScope、AtomGit、OpenRouter 等渠道。在 203 个工程任务的盲评中，Hy4 preview 以 2.99 分略胜 GLM 5.3（2.92）与 Kimi K3（2.94）；API 定价为每 1M tokens 输入 0.834 美元、输出 2.501 美元。该模型是腾讯迄今最强开源模型，并在多个平台上开放获取。

telegram · zaihuapd · 8月28日 06:11

**「背景」** 腾讯混元是腾讯推出的大语言模型系列，此前已发布多代开源版本。本次发布的 Hy4 preview 采用了混合专家（MoE）架构，总参数量为 770B，但每次推理仅激活 49B 参数，从而在扩大模型规模的同时控制计算成本。模型上下文长度达到 1M token，可处理超长文本，并已同步开源至 HuggingFace、GitHub、ModelScope 等主流平台，支持在腾讯云和 OpenRouter 等渠道调用。

**「影响」** 对于需要长上下文与工程任务处理的开发者与研究人员，Hy4 preview 提供了可获取的 1M 上下文开源选择，并通过 API 以指定价格直接使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tencent.com/zh-cn/tencent-releases-and-open-sources-tencent-hy4-preview/">腾讯发布并开源Hy4 preview - Tencent</a></li>
<li><a href="https://www.chinaz.com/ainews/30694.shtml">腾讯混元发布开源旗舰模型Hy4preview，总参数770B、上下文1M</a></li>
<li><a href="https://www.bilibili.com/video/BV1D4tN6TEZU/">腾讯混元 Hy4 preview 正式开源！770B总参/49B激活、1M上下文，主攻代码、办公、游戏与科研_哔哩哔哩_bilibili</a></li>

</ul>
</details>

**标签**: `#open-source LLM`, `#Tencent`, `#large language models`, `#AI benchmarks`, `#software engineering`

---

<a id="item-tech-news-4"></a>
### [智谱开源 GLM-5.3：聚焦智能体编程与网络防御](http://z.ai/) ⭐️ 8.0/10

智谱 AI 已开源 GLM-5.3，权重开放下载、运行和定制，主打智能体编程与网络防御场景。该模型与 GLM-5.2 共用同一基础模型，全部提升来自后训练，复杂编程和长周期任务能力明显增强：Terminal Bench 2.1 得分 88.2，DeepSWE 得分 66.9，均大幅领先 GLM-5.2。GLM-5.3 采用自定义 GLM-5.3 License，个人与中小企业可自由使用、微调与商用，但连续 12 个月营收超 100 亿美元且对外提供模型即服务的公司，须先通过 Z.AI 安全审查。

telegram · zaihuapd · 8月28日 15:32

**「背景」** 智能体编程指让模型自主完成多步骤编码任务，网络防御则涉及识别和应对安全威胁；这两类场景对模型的长周期推理和工具调用能力要求很高。后训练是在预训练基础模型之上进行微调和对齐的过程，可以显著改善特定任务表现，而无需重新训练基础模型。

**「影响」** 开发者与中小企业和个人可直接获得 GLM-5.3 的开放权重用于微调和商用，而年营收超 100 亿美元并提供模型即服务的大型企业需先通过 Z.AI 安全审查。

**标签**: `#open-source`, `#LLM`, `#GLM`, `#agentic programming`, `#Z.AI`

---

<a id="item-tech-news-5"></a>
### [OpenAI 宣布 SpaceX 收购 Cursor 后的模型访问决定](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/) ⭐️ 7.0/10

OpenAI 宣布了关于 Cursor 的决定，因为 Cursor 被 SpaceX 收购。该决定很可能限制 Cursor 对 OpenAI 模型的访问，反映出模型提供商对 API 转售和模型蒸馏的担忧。此举延续了 Anthropic 此前因类似服务条款违规而禁止 xAI 的先例，也表明前沿 AI 竞争正在加剧。目前具体的限制范围、生效时间和受影响模型尚未披露，对依赖 Cursor 工具链访问多家模型的开发者来说，这一变化具有重要影响。

hackernews · meetpateltech · 8月29日 01:47 · [社区讨论](https://news.ycombinator.com/item?id=49486172)

**「背景」** Cursor 是一款 AI 编程工具，此前通过转售 OpenAI、Anthropic 等模型向开发者提供服务。SpaceX 已与 Cursor 达成收购协议，但交易尚未完成，仍需监管批准；OpenAI 随即通知 SpaceX，计划终止向 Cursor 提供 OpenAI 模型的合同，拟议的关闭日期为 2026 年 11 月 12 日。这一背景涉及 AI 模型提供方与被收购的第三方工具之间的合同关系与准入调整。

**「影响」** OpenAI 在官方声明中确认，其针对 Cursor 被 SpaceX 收购后的决定将影响依赖 Cursor 中 OpenAI 模型的开发者，并明确表示这些开发者是受此决定影响最大的群体。

**「社区讨论」** 评论区普遍认为 Cursor 转售第三方 API 的业务模式本就脆弱，即使 OpenAI 不主动断供，也难以与各家的补贴计划竞争。有用户指出 Anthropic 此前已因服务条款违规封禁 xAI，OpenAI 这次只是跟进；一些用户表示将转向 Anthropic 或干脆只使用 Grok 和 Composer，对 OpenAI 模型不再抱有期待。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/">Our decision on Cursor following its acquisition by SpaceX | OpenAI</a></li>
<li><a href="https://www.wired.com/story/can-cursor-remain-an-open-platform-inside-of-spacex/">Can Cursor Remain a Platform for OpenAI and Anthropic’s Models Inside SpaceX? | WIRED</a></li>
<li><a href="https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/">Our decision on Cursor following its acquisition by SpaceX | OpenAI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Cursor`, `#AI regulation`, `#model access`, `#tech industry`

---

<a id="item-tech-news-6"></a>
### [美国制裁意大利托管商 Autistici/Inventati 引担忧](https://www.inventati.org/) ⭐️ 7.0/10

美国政府将意大利托管服务商 Autistici/Inventati 及其旗下博客平台 noblogs.org 列为“全球恐怖分子”并实施制裁，导致 autistici.org 无法访问、noblogs.org 部分功能失效。该组织长期为匿名博客、开源项目和公民社会提供基础设施，并与意大利 Indymedia 及 2001 年热那亚 G8 抗议活动有关。这是对互联网基础设施服务商前所未有的直接制裁，引发社区担忧：若托管“激进团体”内容即被定性为恐怖分子，I2P、Monero、Signal 等项目及其用户或开发者可能成为下一个目标。评论者还指出，目前缺乏公开证据表明该组织直接支持或托管过 PKK 相关内容。

hackernews · exiguus · 8月28日 12:58 · [社区讨论](https://news.ycombinator.com/item?id=49477854)

**「背景」** Autistici/Inventati（A/I Collective）是一个总部位于意大利的志愿者运营技术团体，长期为活动人士、个人和组织提供电子邮件、博客托管等数字服务，例如托管 noblogs.org。2026 年 8 月，美国财政部以涉嫌支持巴勒斯坦行动等左翼团体为由，对其施加金融制裁。A/I 否认这些指控，在声明中称自己是一个依赖捐赠运行的小型技术集体，提供“数字自卫”工具和通信服务。

**「影响」** 受制裁直接影响是 Autistici/Inventati 的托管服务中断（autistici.org 下线、noblogs.org 部分不可用），依赖其基础设施的匿名博客和项目用户访问受阻。同时，这一先例可能让更多基础设施提供者因用户内容而面临法律和政策风险。

**「社区讨论」** 评论区普遍认为这是打击基础设施服务商的危险先例，有用户引用该组织参与热那亚 G8 抗议媒体中心的史料，也有用户因链接失效而对组织性质表示困惑。另一些评论质疑制裁与 PKK 的关联缺乏可查证的第三方证据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/feed/update/urn:li:activity:7498405566512406528/">US sanctions this morning against an Italian IT developer that...</a></li>
<li><a href="https://www.aljazeera.com/news/2026/8/26/us-imposes-sanctions-on-palestine-action-and-other-left-wing-groups">US imposes sanctions on Palestine Action and other... | Al Jazeera</a></li>
<li><a href="https://www.zerohedge.com/markets/us-sanctions-3-groups-accused-supporting-far-left-terrorism">US Sanctions 3 Groups Accused Of Supporting Far-Left... | ZeroHedge</a></li>

</ul>
</details>

**标签**: `#sanctions`, `#internet-freedom`, `#hosting`, `#open-source`, `#policy`

---

<a id="item-tech-news-7"></a>
### [在 RP2350 微控制器上运行微型图像生成模型](https://www.reddit.com/r/MachineLearning/comments/1w10tax/i_implemented_a_very_tiny_image_generation_model/) ⭐️ 7.0/10

一位开发者实现了一种仅 240 万至 400 万参数的 int8 量化潜在流变换器，可在 RP2350 微控制器上完全运行，约 20 秒生成 128×128 人脸图像。模型包含 12 层，使用 AdaLN-Zero 条件化，并支持 CFG 以提升图像质量。推理引擎通过 DMA 从闪存流式加载权重，同时计算上一层，并利用 ReLU²激活带来的稀疏性跳过部分计算。经过大量消融实验后，作者对如此少的参数能达到的效果感到惊讶。这一成果展示了边缘端低功耗设备运行图像生成模型的可行性。

reddit · r/MachineLearning · /u/cpldcpu · 8月28日 19:48

**「背景信息」** RP2350 是树莓派公司于 2024 年 8 月发布的低成本微控制器，常见于树莓派 Pico 2 开发板，售价约 5 美元，批量价格低至 0.80 美元。它采用双核 Arm Cortex-M33 处理器，主频 150MHz，提供硬件浮点和 DSP 指令。传统图像生成模型通常需要大型 GPU，因此在这种微控制器上运行量化后的生成模型是边缘 AI 领域的重要探索。

**「影响」** 对于嵌入式和边缘 AI 开发者，该实现证明量化后的生成式变换器可在资源受限的微控制器上运行，为低功耗离线图像生成提供了可行路径，但约 20 秒的生成时间表明目前仅限于静态或慢速场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RP2350">RP2350 - Wikipedia</a></li>
<li><a href="https://www.raspberrypi.com/products/rp2350/">Buy an RP2350 – Raspberry Pi</a></li>

</ul>
</details>

**标签**: `#edge-ai`, `#model-quantization`, `#embedded-systems`, `#image-generation`, `#transformer`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [两部门将个人住房贷款期限上限由 30 年延长至 40 年](https://news.ifeng.com/c/8vxm6huJOMR) ⭐️ 8.0/10

中国人民银行与国家金融监督管理总局近日联合印发意见，将个人住房贷款期限上限由最长 30 年延长至最长 40 年；具体期限由购房人与商业银行协商确定。

telegram · zaihuapd · 8月28日 12:16

**「背景」** 此前个人住房贷款期限上限为 30 年。中国人民银行与国家金融监督管理总局近日联合印发意见，将这一上限延长至 40 年，具体期限由购房人同商业银行协商确定，以支持加快构建房地产发展新模式。

**「影响」** 对新申请房贷的购房者而言，在同等贷款金额和利率下，选择更长期限可降低每月还款压力，但总利息支出会相应增加；商业银行也获得更大贷款期限灵活度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.sina.cn/2026-08-28/detail-inipwnxp9017299.d.html?vt=4">重磅！个人住房贷款期限由最长30年延长至最长40年|中国人民银行|国家金融监督管理总局|房屋抵押贷款|房地产信贷|商业银行_手机新浪网</a></li>
<li><a href="https://finance.sina.com.cn/money/bank/bank_hydt/2026-08-28/doc-inipwnxp9005397.shtml">两部门：将个人住房贷款期限由最长30年延长至最长40年_新浪财经_新浪网</a></li>

</ul>
</details>

**标签**: `#中国房地产`, `#住房贷款`, `#金融监管`, `#按揭政策`, `#房地产信贷`

---

<a id="item-finance-news-2"></a>
### [玉米和小麦期货价格升至三年多来最高水平](https://www.cnbc.com/2026/08/28/corn-and-wheat-prices-jump-to-highest-prices-in-more-than-three-years.html) ⭐️ 7.0/10

受美国玉米供应预期下调、欧洲干旱和乌克兰出口受阻影响，玉米和小麦期货周五双双升至三年多来最高：小麦收涨 3.1%至每蒲式耳 784 美分，本周累计上涨 12.1%；玉米收涨 0.6%至每蒲式耳 536.5 美分，8 月迄今上涨 15.6%。

rss · CNBC Finance · 8月28日 20:00

**「背景」** 美国农业部 8 月报告将玉米单产预估下调至每英亩 180.7 蒲式耳，降幅超过交易员预期；欧洲夏季高温干旱也影响产量。小麦方面，俄罗斯和乌克兰合计占全球小麦出口超过四分之一，黑海地区出口设施受损让市场担心供应中断。

**「影响」** 欧洲玉米减产可能促使当地更多使用小麦作饲料并减少出口，从而进一步收紧国际谷物供应。

**标签**: `#corn`, `#wheat`, `#commodities`, `#supply disruptions`, `#agriculture`

---

<a id="item-finance-news-3"></a>
### [美上诉法院：体育赛事合约非联邦监管掉期，或上诉至最高法院](https://www.cnbc.com/2026/08/28/appeals-court-rules-against-prediction-markets-tees-up-scotus-fight.html) ⭐️ 7.0/10

美国第九巡回上诉法院裁定，押注体育比赛结果的“事件合约”不是受美国商品期货交易委员会（CFTC）独家监管的掉期（一种衍生品），而是体育博彩，因此拒绝了 Kalshi、Crypto.com 和 Robinhood 阻止内华达州监管的请求。

rss · CNBC Finance · 8月29日 02:23

**「背景」** 此前今年 4 月第三巡回上诉法院曾裁定只有 CFTC 有管辖权，两法院结论相反形成“巡回法院分歧”，使该问题很可能上诉至最高法院。

**「影响」** 这一裁决意味着 Kalshi、Crypto.com 和 Robinhood 的体育赛事事件合约可能要遵守各州博彩法规；消息公布后 DraftKings 和 Flutter Entertainment 股价分别上涨约 7%和逾 6%。

**标签**: `#prediction markets`, `#CFTC`, `#state vs federal regulation`, `#court ruling`, `#event contracts`

---

<a id="item-finance-news-4"></a>
### [沃什鹰派讲话后，市场预计美联储 9 月加息概率约 56%](https://www.cnbc.com/2026/08/28/-september-fed-decision-now-a-coin-flip-as-rate-hike-odds-increase.html) ⭐️ 7.0/10

美联储主席沃什在杰克逊霍尔发表鹰派讲话后，CME FedWatch 显示市场认为 9 月 16 日加息 25 个基点的概率约为 56%，接近“抛硬币”水平。

rss · CNBC Finance · 8月28日 15:22

**「背景」** 此前 7 月非农就业报告弱于预期、通胀有所回落，曾让 9 月加息概率下降；7 月会议已有三名 FOMC 成员反对维持利率不变，主张加息。沃什在讲话中表示，夏季通胀读数好转并不代表潜在趋势已明显改善，并重申抗通胀承诺。

**标签**: `#Federal Reserve`, `#Interest Rates`, `#Monetary Policy`, `#Market Expectations`, `#Jackson Hole`

---

<a id="item-finance-news-5"></a>
### [美联储主席沃什将在杰克逊霍尔发表讲话，市场关注政策信号](https://www.cnbc.com/2026/08/27/fed-chairman-kevin-warsh-delivers-his-key-jackson-hole-speech-friday.html) ⭐️ 7.0/10

美联储主席凯文·沃什将于周五在杰克逊霍尔发表主旨演讲，市场关注他是否会就利率路径给出明确信号。美国银行策略师预计，若沃什只讨论生产力等广泛结构主题，30 年期美债收益率可能升至 5.5%以上。

rss · CNBC Finance · 8月28日 11:39

**「背景」** 沃什自 5 月上任以来较少提供前瞻指引，更倾向于让市场自行解读数据，并成立了五个工作组从“第一原则”审视美联储职能。

**标签**: `#Federal Reserve`, `#Monetary Policy`, `#Jackson Hole`, `#Kevin Warsh`, `#Treasury Yields`

---

<a id="item-finance-news-6"></a>
### [美元兑日元重回 160，日美干预效果回撤](https://www.reuters.com/world/asia-pacific/dollar-flat-near-one-week-high-investors-await-warshs-jackson-hole-debut-2026-08-28/) ⭐️ 7.0/10

美元兑日元重新升破 160，回吐了日美联合干预汇市带来的升值成果；此前干预曾令汇率从接近 164 回落至 158 附近，最新直接催化剂是美联储主席沃什在杰克逊霍尔发表偏鹰讲话，市场对 9 月加息预期升温。

telegram · zaihuapd · 8月29日 01:53

**「背景」** 此前日美在 7 月底联合干预汇市支撑日元，这是自 1998 年以来美国首次参与联合行动，当时美元兑日元一度从接近 164 回落至 158 附近。近期美联储主席沃什在杰克逊霍尔发表偏鹰讲话，重申 2%通胀目标并对当前通胀水平表示担忧，市场因此提高 9 月加息预期，推动美元上行，日元再度走弱。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.foxbusiness.com/economy/what-warshs-jackson-hole-speech-signals-about-where-interest-rates-headed">Kevin Warsh outlines hawkish PCE inflation stance at Jackson Hole | Fox Business</a></li>
<li><a href="https://wolfstreet.com/2026/08/03/why-the-us-japan-joint-intervention-to-prop-up-the-yen-fear-of-treasury-yields-blowing-out-if-japan-becomes-a-forced-seller/">Why the US-Japan Joint Intervention to Prop Up the Yen? Fear of Treasury Yields Blowing Out if Japan Becomes a Forced Seller | Wolf Street</a></li>
<li><a href="https://www.cnbc.com/2026/08/03/japan-yen-intervention-us-treasurys-euros-.html">Japan yen intervention: why the U.S. stepped in</a></li>

</ul>
</details>

**标签**: `#forex`, `#USD/JPY`, `#currency intervention`, `#Federal Reserve`, `#monetary policy`

---