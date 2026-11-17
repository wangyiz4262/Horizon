---
layout: default
title: "Horizon Summary: 2026-11-17 (ZH)"
date: 2026-11-17
lang: zh
---

> 从 27 条内容中筛选出 12 条重要资讯。

---

**科技新闻**
1. [卡耐基梅隆大学在 YouTube 上免费公开计算机科学课程](#item-tech-news-1) ⭐️ 8.0/10
2. [Optimizely 遭入侵并通过 Zoom 和 GitLab 分发恶意软件](#item-tech-news-2) ⭐️ 8.0/10
3. [Jiff 1.0 发布：面向 Rust 的全新日期时间库](#item-tech-news-3) ⭐️ 8.0/10
4. [Black Forest Labs 探讨从像素、运动与声音构建视觉智能](#item-tech-news-4) ⭐️ 8.0/10
5. [神秘域名 w2rt6byl5nf1opmc-a.com 的来源与调查](#item-tech-news-5) ⭐️ 7.0/10
6. [微软将重大电子邮件故障归咎于 7 月修复中引入的软件缺陷](#item-tech-news-6) ⭐️ 7.0/10
7. [Perplexity 实现了 10 亿美元的年化收入运行率](#item-tech-news-7) ⭐️ 7.0/10

**财经新闻**
1. [美国科技公司面临日益严峻的中国业务困境](#item-finance-news-1) ⭐️ 8.0/10
2. [美联储主席谈人工智能的经济影响](#item-finance-news-2) ⭐️ 8.0/10
3. [伯克希尔哈撒韦三季度增持达美航空并减持美国银行](#item-finance-news-3) ⭐️ 7.0/10
4. [美国原油价格因中东出口恢复而下跌](#item-finance-news-4) ⭐️ 7.0/10

**科学新闻**
1. [珍贵人类活体大脑样本助力神经科学研究](#item-science-news-1) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [卡耐基梅隆大学在 YouTube 上免费公开计算机科学课程](https://www.cs.cmu.edu/learn/) ⭐️ 8.0/10

卡耐基梅隆大学推出了 CS Learn 项目，开始在 YouTube 上免费发布完整学期的计算机科学课程讲座。首批课程于本周逐日首播，更多课程计划于 1 月份推出。该项目由学生开发的工具支持，旨在将学校的计算机科学教学资源向公众开放。

hackernews · pcompeau · 11月16日 20:43 · [社区讨论](https://news.ycombinator.com/item?id=50522980)

**「背景」** 长期以来，包括麻省理工学院（MIT）在内的高等院校一直在探索通过网络公开课的形式向全球学习者分享优质教育资源，而卡耐基梅隆大学此次则是通过系统性发布全学期讲座来扩充这一领域的资源。

**「影响」** 软件工程和人工智能领域的学习者与开发者可以免费获取卡耐基梅隆大学的高水平计算机科学课程。不过，评论中也有用户指出部分视频存在麦克风收音不佳导致音频质量受影响的问题。

**「社区讨论」** 社区讨论普遍对这一开源举措表示欢迎，认为扎实的计算机科学基础有助于更好地驾驭人工智能工具。同时，也有校友和学习者指出部分视频录音质量有待提升，并表达了对未来上线更多特定高阶课程的期待。

**标签**: `#Computer Science`, `#Education`, `#Open Source`, `#Artificial Intelligence`, `#Software Engineering`

---

<a id="item-tech-news-2"></a>
### [Optimizely 遭入侵并通过 Zoom 和 GitLab 分发恶意软件](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/) ⭐️ 8.0/10

Optimizely 遭遇安全妥协，其第三方脚本被利用在 Zoom 和 GitLab 等知名平台上分发恶意软件。攻击者通过 Optimizely 的系统直接向客户及官方自身网站（包括 www.optimizely.com 与 login.optimizely.com）注入了恶意代码片段。此次事件凸显出现代网络供应链与第三方脚本管理中存在的重大安全风险。

hackernews · kristjansson · 11月16日 23:00 · [社区讨论](https://news.ycombinator.com/item?id=50524767)

**「背景」** 现代网站普遍通过第三方 JavaScript 脚本或标签管理平台来加载营销、分析及实验工具，这种架构使得供应商系统一旦遭遇供应链攻击，嵌入其脚本的众多下游大型网站便会同步受到牵连。

**「影响」** 使用 Optimizely 第三方脚本的各大知名平台及用户面临恶意软件感染的严重威胁，组织需要重新评估并收紧对第三方代码和脚本加载的管控。

**「社区讨论」** 评论者指出，这类事件暴露了通过谷歌标签管理器等工具随意加载第三方脚本的架构隐患，呼吁行业对第三方供应商缺乏问责机制和内部安全管控不足的问题进行反思。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50524767">Optimizely compromised , served malware on Zoom , GitLab</a></li>
<li><a href="https://gizmodo.com/sprawling-malware-attack-reportedly-affects-zoom-cnn-fox-news-peacock-and-170-others-2000840831">Sprawling Malware Attack Reportedly Affects Zoom and Other Major...</a></li>

</ul>
</details>

**标签**: `#security`, `#supply-chain`, `#web-development`, `#vulnerability`

---

<a id="item-tech-news-3"></a>
### [Jiff 1.0 发布：面向 Rust 的全新日期时间库](https://burntsushi.net/jiff/) ⭐️ 8.0/10

开发者 burntsushi 推出了 Jiff 1.0 版，这是一个全新的 Rust 日期时间库，旨在解决现有同类库中的常见 API 和易用性痛点。该版本通过精心的设计和对边界情况的处理，为 Rust 生态系统提供了一个更具现代感的时间处理替代方案。

hackernews · burntsushi · 11月16日 16:53 · [社区讨论](https://news.ycombinator.com/item?id=50519744)

**「背景」** 在 Jiff 出现之前，Rust 生态系统中处理日期和时间主要依赖 Chrono 等老牌库，但这些库常常因历史包袱而面临 API 设计不够优雅或改进阻力大的问题。

**「社区讨论」** 前 Chrono 维护者回顾了因旧有 API 改进受阻而导致的维护倦怠，并对作者 burntsushi 编写 Jiff 表示感谢。其他评论者则赞赏该项目明确界定适用范围的专业态度，并期待其能在更广泛的生态系统中逐步普及。

**标签**: `#Rust`, `#Datetime`, `#Open Source`, `#Software Engineering`

---

<a id="item-tech-news-4"></a>
### [Black Forest Labs 探讨从像素、运动与声音构建视觉智能](https://latent.space/p/bfl/) ⭐️ 8.0/10

Black Forest Labs 的创始人 Andreas Blattmann 和 Dustin Podell 在访谈中探讨了他们构建视觉智能的方法。该团队阐述了如何通过像素、运动和声音来发展通用人工智能（AGI）。访谈深入剖析了他们在生成式 AI 领域的底层技术路线与研究方向。

rss · Latent Space · 11月16日 21:38

**「背景」** Black Forest Labs 的研究人员此前曾参与共同设计潜空间扩散模型（Latent Diffusion Models）以及改进高分辨率图像生成的 SDXL 等基础生成式架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.alphaxiv.org/@andreas-blattmann">Andreas Blattmann | alphaXiv</a></li>
<li><a href="https://openreview.net/profile?id=~Dustin_Podell1">openreview.net/profile?id=~ Dustin _ Podell 1</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#machine learning`, `#computer vision`, `#generative ai`

---

<a id="item-tech-news-5"></a>
### [神秘域名 w2rt6byl5nf1opmc-a.com 的来源与调查](https://jack.cab/blog/siterate) ⭐️ 7.0/10

技术博客 jack.cab 发布了一项针对神秘域名 w2rt6byl5nf1opmc-a.com 的调查，该域名频繁出现在各种网络爬虫与流量日志中。分析显示，该域名在长期处于未注册状态的情况下，曾于 10 月 5 日起进入 Majestic 的前 1 万名排行并飙升至第 8 位，随后于 2026 年 11 月 11 日通过 Cloudflare 被注册。

hackernews · dverlaeckt80 · 11月16日 13:51 · [社区讨论](https://news.ycombinator.com/item?id=50517602)

**「背景」** 网络爬虫和自动化流量分析经常会遇到各种原因不明的异常域名或引用来源，需要通过日志分析和域名注册信息来追溯其根源。

**「社区讨论」** 评论区讨论了该域名可能与 Cloudflare 的机器人对抗模式（Bot Fight mode）或 Turnstile 相关功能有关，并指出其在被注册前曾长期作为未注册域名出现在各大引用统计中。

**标签**: `#web scraping`, `#domain analysis`, `#cloudflare`, `#cybersecurity`

---

<a id="item-tech-news-6"></a>
### [微软将重大电子邮件故障归咎于 7 月修复中引入的软件缺陷](https://www.theregister.com/saas/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026) ⭐️ 7.0/10

微软将近期发生的重大电子邮件服务中断归咎于在 7 月份的错误修复中无意引入的一个软件缺陷。该缺陷导致系统在面对正常负载时出现异常，从而引发了大规模的服务故障。

hackernews · Bender · 11月16日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=50517321)

**「背景」** 微软提供包括云端基础设施、电子邮件服务以及操作系统在内的企业与消费者计算产品。

**「社区讨论」** 评论者认为大型企业出现此类严重故障并不令人意外，并讨论了诸如人工智能在代码编写中的潜在影响、为何系统在面对高负载时未能采取主动限流措施，以及关键网络基础设施所使用操作系统等问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.microsoft.com/">Microsoft – AI, Cloud, Productivity, Computing, Gaming &amp; Apps</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#Cloud Infrastructure`, `#Reliability`, `#Software Engineering`, `#Outage`

---

<a id="item-tech-news-7"></a>
### [Perplexity 实现了 10 亿美元的年化收入运行率](https://latent.space/p/ainews-perplexity-hits-a-1b-revenue-run-rate-up-4x-in-2026/) ⭐️ 7.0/10

Perplexity 的年化收入运行率达到了 10 亿美元，在 2026 年实现了四倍增长。该公司还同时推出了全新的监控 API（Monitor API），并在同期发布了多项行业更新。

rss · Latent Space · 11月17日 09:24

**「背景」** 随着生成式人工智能和对话式搜索服务的普及，各大 AI 初创公司正在积极探索商业化路径，并通过推出面向开发者和企业的 API 服务来拓展收入来源。

**标签**: `#Artificial Intelligence`, `#Perplexity`, `#Industry News`, `#APIs`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [美国科技公司面临日益严峻的中国业务困境](https://www.cnbc.com/2026/11/17/us-tech-firms-china-ties-political-pressure.html) ⭐️ 8.0/10

由于出口管制收紧、地缘政治紧张局势以及供应链风险，英伟达和苹果等美国科技公司在中国的业务面临越来越大的战略困境。大中华区约占苹果销售额的 15%，而美国政府于周一进一步收紧了对中国企业远程访问美国先进芯片的限制。

rss · CNBC Finance · 11月17日 08:52

**「背景」** 自 20 世纪 80 年代中国重新向外国企业开放以来，美国跨国公司纷纷进入中国市场以寻求庞大的消费需求和制造能力，但近期的双边贸易摩擦与关键矿产控制使这一运营模式变得复杂。

**「影响」** 由于中国掌控了关键矿产和稀土供应，相关供应链的不确定性使依赖这些材料的全球制造商面临零部件短缺和生产受阻的风险。

**标签**: `#technology`, `#geopolitics`, `#regulation`, `#semiconductors`, `#trade`

---

<a id="item-finance-news-2"></a>
### [美联储主席谈人工智能的经济影响](https://www.cnbc.com/2026/11/16/fed-ai-task-force-kevin-warsh.html) ⭐️ 8.0/10

美联储主席凯文·沃尔什于 2026 年 11 月 16 日表示，人工智能（官方称“超级智能”）有望推动生产力增长，但也可能带来失业风险或因回报不及预期而导致市场失望。

rss · CNBC Finance · 11月16日 18:46

**「背景」** 美联储为此组建了专门的生产力与就业任务组，旨在评估新兴技术对美国宏观经济和货币政策的长期影响。

**「影响」** 相关言论提醒投资者关注人工智能技术在资本开支和股价大涨后的潜在回调风险，这可能对未来权益资产估值和经济增速产生影响。

**标签**: `#Federal Reserve`, `#Artificial Intelligence`, `#Monetary Policy`, `#Productivity`, `#Economy`

---

<a id="item-finance-news-3"></a>
### [伯克希尔哈撒韦三季度增持达美航空并减持美国银行](https://www.cnbc.com/2026/11/16/berkshire-hathaway-raised-its-stake-in-delta-air-in-the-third-quarter.html) ⭐️ 7.0/10

在第三季度中，由首席执行官格雷格·阿贝尔领导的伯克希尔哈撒韦公司将其持有的达美航空股份增加了 12%（即买入 713 万股，期末持仓价值达 53.7 亿美元），同时将其美国银行持股削减了近 6%（出售了价值超过 16 亿美元的股票）。

rss · CNBC Finance · 11月16日 23:01

**「背景」** 由于美国与伊朗战争导致喷气燃料价格上涨，达美航空股价在第三季度下跌了 11%；而由于利率飙升、通货膨胀居高不下以及美联储货币政策趋紧的预期，美国银行股价在同期下跌了超过 4%。

**标签**: `#Berkshire Hathaway`, `#Delta Air Lines`, `#Bank of America`, `#Investment Portfolio`

---

<a id="item-finance-news-4"></a>
### [美国原油价格因中东出口恢复而下跌](https://www.cnbc.com/2026/11/16/us-crude-oil-declines-to-87-a-barrel-on-recovering-middle-east-exports.html) ⭐️ 7.0/10

由于中东出口恢复，美国西得克萨斯中质原油期货在周一收盘下跌 3.58%，至每桶 85.39 美元。

rss · CNBC Finance · 11月16日 22:19

**「背景」** 国际能源署此前预测，由于中东出口恢复速度快于全球需求，2026 年第四季度全球供应将出现过剩。

**「影响」** 原油价格的下跌有助于降低企业和家庭的能源及燃油成本。

**标签**: `#Oil Prices`, `#Energy Markets`, `#Middle East Exports`, `#International Energy Agency`, `#Goldman Sachs`

---

## 科学新闻

<a id="item-science-news-1"></a>
### [珍贵人类活体大脑样本助力神经科学研究](https://www.nature.com/articles/d41586-026-03711-x) ⭐️ 7.0/10

研究人员通过获取并研究极为罕见的人类活体大脑样本，直接观测人类神经元在其自然环境中的行为。这项工作借助高精度的实验操作，为探索人类大脑的细胞特性与生物学功能提供了独特视角。

rss · Nature · 11月17日 00:00

**「背景」** 长期以来，了解人类神经元的真实行为需要依靠罕见的、来自活动人体的脑样本以及极其精细的实验操作。

**「科学意义」** 直接分析人类活体脑组织能够突破传统动物模型和死后脑标本的局限，深化科学家对人类大脑复杂神经机制的理解，并为相关神经系统疾病的研究与治疗开辟新途径。

**标签**: `#Neuroscience`, `#Brain Samples`, `#Human Biology`, `#Research`

---