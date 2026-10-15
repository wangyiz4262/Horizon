---
layout: default
title: "Horizon Summary: 2026-10-15 (ZH)"
date: 2026-10-15
lang: zh
---

> 从 17 条内容中筛选出 9 条重要资讯。

---

**科技新闻**
1. [OpenCode 2.0 发布：架构升级与客户端/服务端模型重构](#item-tech-news-1) ⭐️ 8.0/10
2. [Liquid AI 发布 LFM2.5-24B-A2B 模型](#item-tech-news-2) ⭐️ 7.0/10
3. [Go 1.27 引入了更好的 HTTP/1 连接复用机制](#item-tech-news-3) ⭐️ 7.0/10
4. [OpenAI 与 Anthropic 在金融领域 AI 代理中平衡自主性与安全控制](#item-tech-news-4) ⭐️ 7.0/10
5. [Leash Bio 利用 DNA 编码文库数据训练 AI 代理并评估模型](#item-tech-news-5) ⭐️ 7.0/10

**财经新闻**
1. [中国表示将继续向欧洲供应稀土](#item-finance-news-1) ⭐️ 8.0/10
2. [美国银行花费数亿美元雇佣外包人员修补软件漏洞](#item-finance-news-2) ⭐️ 8.0/10
3. [摩根士丹利第三季度业绩超预期](#item-finance-news-3) ⭐️ 7.0/10
4. [美国银行三季度利润下滑](#item-finance-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenCode 2.0 发布：架构升级与客户端/服务端模型重构](https://anoma.ly/notes/opencode-2-0/) ⭐️ 8.0/10

OpenCode 2.0 正式发布，带来了架构层面的改进、自动插件重新加载以及重构后的客户端/服务端模型。该版本修复了许多一代的痛点，支持后台任务、子会话通信优化，并采用了基于 Effect 的循环架构。此次更新受到了开发者的广泛好评，许多原先需要自行开发的变通方案现在已成为原生功能。

hackernews · gmays · 10月14日 20:48 · [社区讨论](https://news.ycombinator.com/item?id=50094994)

**「背景」** OpenCode 是一个开源的 AI 编程智能体，在此次 2.0 版本更新前，其早期版本主要通过插件和客户端/服务端架构来支持开发者的日常编码任务。

**「社区讨论」** 社区用户普遍反映 2.0 版本显著提升了易用性，解决了旧版本中的许多烦恼，特别是自动重新加载插件和内置的配置编辑技能。不过，也有用户对自动化权限模式（如类似 Claude Code 的自动模式）表达了需求，认为当前的“yolo 模式”存在风险，而手动批准每条命令又会打断开发流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opencode.ai/">OpenCode | The open source AI coding agent</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#software engineering`, `#developer tools`, `#open source`

---

<a id="item-tech-news-2"></a>
### [Liquid AI 发布 LFM2.5-24B-A2B 模型](https://www.liquid.ai/blog/lfm2-5-24b-a2b) ⭐️ 7.0/10

Liquid AI 发布了全新模型 LFM2.5-24B-A2B，专为速度极快的端侧智能体设计。官方宣称其在端侧运行速度比同类混合专家模型（MoE）快高达 1.7 倍，在 Apple M5 Max 上可达每秒 184 个 Token，在单块 NVIDIA B300 GPU 上最高可达每秒 21,000 个输出 Token。不过，该模型的许可证包含一条令人费解且难以执行的非商业使用条款。

hackernews · gmays · 10月14日 23:59 · [社区讨论](https://news.ycombinator.com/item?id=50097369)

**「背景」** 在此之前，Liquid AI 推出了采用混合稀疏 MoE 架构的 LFM 2.5-8B-A1B，主要面向浏览器端工具调用和端侧部署场景。

**「社区讨论」** 社区用户对该模型的速度表现印象深刻，但也对其推理能力和实际效用提出了质疑。部分用户指出其在实际编码测试中表现糟糕、陷入循环错误，甚至有人戏称其“速度极快但不够聪明”，同时也有人注意到了其许可证中含糊不清的非商业条款。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.webbrain.one/blog/liquid-lfm25-tool-calling">Liquid LFM 2 . 5 -8 B - A 1B on browser tool calling: an... — WebBrain Blog</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#machine learning`, `#edge computing`, `#open source`

---

<a id="item-tech-news-3"></a>
### [Go 1.27 引入了更好的 HTTP/1 连接复用机制](https://go.dev/blog/http-connection-reuse) ⭐️ 7.0/10

Go 1.27 标准库在其 \`net/http\` 包中引入了改进的 HTTP/1 连接复用机制。这一变更为使用 Go 构建网络服务和客户端的开发者提供了直接的性能提升。

hackernews · allddd · 10月14日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=50090369)

**「背景」** 长期以来，在 Go 语言的 net/http 客户端中，如果开发者未完全读取并关闭 HTTP/1 响应体，底层 TCP 连接往往无法被复用，从而引发频繁的三次握手开销。

**「社区讨论」** 评论者探讨了标准库何时会加入 HTTP/3 支持，并讨论了连接关闭、响应体读取以及可能导致连接无法正常复用的边缘情况（例如使用 JSON Decoder 读取带有换行符的响应）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://uproger.com/go-1-27-http1/">Go 1 . 27 ускорил HTTP /1 почти... - UPROGER | Программирование</a></li>
<li><a href="https://groups.google.com/g/golang-nuts/c/IZ2p1sHkeBQ">TCP connection reuse when doing HTTP</a></li>

</ul>
</details>

**标签**: `#Go`, `#Networking`, `#HTTP`, `#Software Engineering`, `#Standard Library`

---

<a id="item-tech-news-4"></a>
### [OpenAI 与 Anthropic 在金融领域 AI 代理中平衡自主性与安全控制](https://www.latent.space/p/crossing-the-threshold) ⭐️ 7.0/10

在纽约 AI 工程大会上，前沿实验室与金融机构共同探讨了如何在赋予 AI 代理实用自主性的同时，将重大决策控制在安全范围内。OpenAI 与 Anthropic 正在金融高风险场景中评估如何平衡自主操作与安全风控机制。此次讨论聚焦于实际部署中的风险管理，但尚未公布具体的版本发布、兼容性或可用性细节。

rss · Latent Space · 10月14日 21:40

**「背景」** 随着大语言模型能力向多步骤任务代理（Agent）演进，如何在保证系统安全可控的前提下将其部署到高 stakes、强监管的金融行业，已成为各大前沿实验室和企业的关键课题。

**标签**: `#Artificial Intelligence`, `#Autonomous Agents`, `#AI Safety`, `#Fintech`, `#Software Engineering`

---

<a id="item-tech-news-5"></a>
### [Leash Bio 利用 DNA 编码文库数据训练 AI 代理并评估模型](https://www.latent.space/p/lab-in-the-loop-at-compute-speed) ⭐️ 7.0/10

Leash Bio 正在利用从 DNA 编码文库（DEL）中获取的数据来训练 AI 代理，并以此评估机器学习模型的有效性。这种数据管线旨在改善生物技术领域的模型训练方式，并帮助识别和纠正模型中的欺骗行为。该方法为 AI 代理模拟化学家思维提供了适用的实验数据支撑。

rss · Latent Space · 10月14日 20:35

**「背景」** DNA 编码文库（DEL）技术允许研究人员同时合成和筛选数百万到数十亿个小分子化合物，但其产生的大规模复杂数据在传统处理和分析上面临着巨大挑战。机器学习模型常被用于加速药物发现，但在处理高通量生化测定数据时容易出现泛化能力不足或过拟合等问题。

**「影响」** 生物技术和药物发现领域的开发者可以利用这些高质量的 DEL 数据来校准其机器学习模型，减少模型在虚拟筛选中的盲目性。

**标签**: `#artificial intelligence`, `#machine learning`, `#biotechnology`, `#data science`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [中国表示将继续向欧洲供应稀土](https://www.cnbc.com/2026/10/15/china-rare-earth-exports-europe.html) ⭐️ 8.0/10

中国商务部发言人束珏婷表示，无论中美贸易协议是否在 1 月到期，中国都将继续向欧洲出口稀土。

rss · CNBC Finance · 10月15日 09:02

**「背景」** 稀土是一组对制造电子产品和新能源设备至关重要的金属元素。此前，中美两国曾同意将一项涉及贸易限制的停火协议延长至 1 月。

**「影响」** 这一表态有助于缓解欧洲相关制造业和供应链企业对关键原材料断供的担忧。

**标签**: `#international trade`, `#rare earths`, `#supply chain`, `#China policy`, `#EU economy`

---

<a id="item-finance-news-2"></a>
### [美国银行花费数亿美元雇佣外包人员修补软件漏洞](https://www.cnbc.com/2026/10/14/anthropic-mythos-bank-of-america-hiring-cost.html) ⭐️ 8.0/10

美国银行首席执行官布莱恩·莫伊尼汉表示，该行在第二季度雇佣了 1,000 名外部合同工，并花费了数亿美元用于修补由人工智能模型（如 Anthropic 的 Mythos）暴露出的软件漏洞。

rss · CNBC Finance · 10月14日 20:06

**「背景」** 随着能够发现并利用旧代码漏洞的高级人工智能模型问世，各大企业正面临保护内部系统安全的巨大压力。

**「影响」** 这一安全应对措施给银行带来了沉重的短期运营成本，并促使金融机构加速防范由人工智能技术带来的新型网络安全风险。

**标签**: `#Banking`, `#Artificial Intelligence`, `#Cybersecurity`, `#Corporate Earnings`

---

<a id="item-finance-news-3"></a>
### [摩根士丹利第三季度业绩超预期](https://www.cnbc.com/2026/10/14/morgan-stanley-ms-q3-2026-earnings.html) ⭐️ 7.0/10

摩根士丹利公布的 2026 年第三季度财报显示，每股收益为 3.03 美元，高于 LSEG 调查预期的 2.91 美元；总营收为 20.34 亿美元，高于 19.95 亿美元的预期。公司表示，这一表现主要受股票交易业务营收同比增长 41%至 58 亿美元的强劲推动，该项数据比分析师预期高出约 9.09 亿美元。

rss · CNBC Finance · 10月14日 20:22

**「背景」** 股票交易业务是摩根士丹利的核心传统业务之一，其季度业绩通常反映出华尔街金融机构在面对地缘政治与宏观经济波动时的整体表现。

**「影响」** 该银行好于预期的盈利表现为投资者评估大型金融机构在第四季度市场环境中的韧性提供了重要参考。

**标签**: `#Morgan Stanley`, `#Earnings`, `#Equities Trading`, `#Banking`

---

<a id="item-finance-news-4"></a>
### [美国银行三季度利润下滑](https://www.cnbc.com/2026/10/14/bank-of-america-bac-q3-2026-earnings.html) ⭐️ 7.0/10

受 12 亿美元美国监管罚款及债券交易业务疲软影响，美国银行公布 2026 年第三季度利润同比下降 17%至 69.3 亿美元，其 301.2 亿美元的实际营业收入低于伦敦证券交易所集团（LSEG）预测的 306.9 亿美元，导致股价在周三下跌近 5%。

rss · CNBC Finance · 10月14日 20:20

**「背景」** 此次监管罚款源于美国监管机构称该行未能报告数十亿美元的可疑交易，而该行的交易业务表现也逊于首席执行官布莱恩·莫伊尼汉（Brian Moynihan）上个月预测的持平水平。

**标签**: `#Bank of America`, `#Earnings`, `#Regulatory Penalty`, `#Banking Sector`, `#Trading Revenue`

---