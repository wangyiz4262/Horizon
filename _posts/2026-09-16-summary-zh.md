---
layout: default
title: "Horizon Summary: 2026-09-16 (ZH)"
date: 2026-09-16
lang: zh
---

> 从 42 条内容中筛选出 22 条重要资讯。

---

**科技新闻**
1. [Google 发布 Gemini 3.8 Live 及 Extended Thinking 模型](#item-tech-news-1) ⭐️ 8.0/10
2. [Strix 自动化代理在 25 分钟内获取 Baseten 生产环境 GitHub 管理权限](#item-tech-news-2) ⭐️ 8.0/10
3. [开发者从零训练 44M 三值量化大模型，内存占用仅 19.8 MB 且 CPU 推理极快](#item-tech-news-3) ⭐️ 8.0/10
4. [Prior Labs 发布全新表格基础模型 TabPFN-3.5](#item-tech-news-4) ⭐️ 8.0/10
5. [联发科发布天玑 9600 Pro 移动芯片](#item-tech-news-5) ⭐️ 8.0/10
6. [astral-sh/uv 发布 0.12.14 版本](#item-tech-news-6) ⭐️ 7.0/10
7. [Typesafe.ai 推出的 System One Models 与 Jev 系统](#item-tech-news-7) ⭐️ 7.0/10
8. [一款能聆听鸟鸣并绘制 19 世纪风格插图的开源电子墨水相框](#item-tech-news-8) ⭐️ 7.0/10
9. [互联网档案馆发布关于 Wayback Machine 访问问题与防护措施的更新](#item-tech-news-9) ⭐️ 7.0/10
10. [开发者历时一个月为 M4 Mac Mini 构建 Linux GPU 驱动](#item-tech-news-10) ⭐️ 7.0/10
11. [GEFS 在 OpenBSD 上的早期预览](#item-tech-news-11) ⭐️ 7.0/10
12. [数据隐私担忧促使英伟达与博思艾伦等企业限制外部 AI 模型使用](#item-tech-news-12) ⭐️ 7.0/10
13. [工信部与发改委印发电子信息制造业十五五规划](#item-tech-news-13) ⭐️ 7.0/10
14. [桑德斯等议员提法案拟永久禁止超级智能 AI](#item-tech-news-14) ⭐️ 7.0/10
15. [谷歌授权全体工程师在内部平台使用 Anthropic Claude 编程模型](#item-tech-news-15) ⭐️ 7.0/10
16. [OpenAI 被曝雇用合同工人工阅读 ChatGPT 聊天记录](#item-tech-news-16) ⭐️ 7.0/10

**科技博客**
1. [Training the Fastest Kimi K3 DSpark Speculator Using GB300 NVL72](#item-tech-blog-1) ⭐️ 8.0/10
2. [向 AI 代理解释原因而非过程](#item-tech-blog-2) ⭐️ 7.0/10

**财经新闻**
1. [中国八月零售额增长放缓且投资下滑加剧](#item-finance-news-1) ⭐️ 8.0/10
2. [共享单车服务规范新国标发布](#item-finance-news-2) ⭐️ 7.0/10
3. [华为与赛力斯调整合作模式](#item-finance-news-3) ⭐️ 7.0/10
4. [字节跳动 2026 上半年净利润下降](#item-finance-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Google 发布 Gemini 3.8 Live 及 Extended Thinking 模型](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/) ⭐️ 8.0/10

谷歌正式发布了 Gemini 3.8 Live 以及 Gemini 3.8 Live Extended Thinking，带来了先进的实时语音交互和推理功能。早期用户对其赞赏有加，认为其在语音自然度、口音适应能力和延迟表现上均有出色表现，并支持了工作区（Workspace）账号的访问。尽管部分用户对其在特定付费群体中的推出节奏表达了遗憾，但整体反响显示出其在同类实时语音模型中的强大竞争力。

hackernews · leumon · 9月15日 17:38 · [社区讨论](https://news.ycombinator.com/item?id=49715947)

**「背景」** 随着大语言模型技术的快速发展，各大 AI 实验室正积极推进模型向多模态、实时语音及深度推理方向演进。谷歌持续通过 Gemini 系列模型在实时交互和复杂推理领域进行迭代更新。

**「影响」** 该模型的发布显著提升了用户在多语言对话和即兴语音学习方面的体验，同时改善了 Workspace 用户的账户可用性。

**「社区讨论」** 社区用户普遍对 Gemini 3.8 Live 的语音自然度、低延迟以及对小语种（如南非荷兰语）和厚重口音的处理能力给予了高度好评，部分用户甚至认为其体验优于同类竞品的语音功能。不过，也有用户对部分账号层级的发布延迟表示了微词。

**标签**: `#artificial intelligence`, `#machine learning`, `#large language models`, `#voice interaction`, `#google`

---

<a id="item-tech-news-2"></a>
### [Strix 自动化代理在 25 分钟内获取 Baseten 生产环境 GitHub 管理权限](https://www.strix.ai/blog/baseten-harbor-github-pat-takeover) ⭐️ 8.0/10

安全分析公司 Strix 利用自动化代理，在公开的 Docker 镜像构建历史记录中发现了泄露的 GitHub 个人访问令牌（PAT），并在 25 分钟内取得了 Baseten 生产环境仓库的管理权限。该令牌拥有对 Baseten 主产品仓库、集群 GitOps 仓库及 Homebrew tap 的管理员和推送权限，以及对其他私有仓库的读写权限。Baseten 在 7 月 13 日晚间收到报告后，于次日下午将 Harbor 项目设为私有并撤销了该令牌。此事件凸显了人工智能与基础设施初创企业在供应链及密钥管理方面面临的严重安全隐患。

hackernews · bearsyankees · 9月15日 18:11 · [社区讨论](https://news.ycombinator.com/item?id=49716476)

**「背景」** 容器镜像在构建时若未清理凭证，其历史层常会残留敏感的私密信息，自动化渗透测试工具能够利用这类配置疏漏快速发起攻击链。现代开发与部署流程中广泛依赖的各类个人访问令牌（PAT），如果未严格限制权限范围或及时轮换，极易成为供应链攻击的突破口。

**「影响」** 此次漏洞暴露促使开发团队必须彻底审查容器镜像构建历史，以防止敏感凭据随编译产物一同泄露。

**「社区讨论」** 社区讨论主要集中在两点：一方面认可 Baseten 的快速响应和良好处理态度，另一方面则批评 Strix 在公开案例中直接点名受害者将其作为营销手段的做法是否妥当。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.strix.ai/blog/baseten-harbor-github-pat-takeover">We wanted to use Baseten for inference. We ended up with admin access to their GitHub - Strix</a></li>
<li><a href="https://vuink.com/post/fgevk-d-dnv/blog/baseten-harbor-github-pat-takeover">We wanted to use Baseten for inference. We ended up with admin access to their GitHub | Vuink.com</a></li>
<li><a href="https://github.com/usestrix/strix">GitHub - usestrix/strix: Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.</a></li>

</ul>
</details>

**标签**: `#security`, `#github`, `#docker`, `#secrets management`, `#artificial intelligence`

---

<a id="item-tech-news-3"></a>
### [开发者从零训练 44M 三值量化大模型，内存占用仅 19.8 MB 且 CPU 推理极快](https://www.reddit.com/r/MachineLearning/comments/1wgzpli/i_trained_a_44m_parameter_quantized_llm_from/) ⭐️ 8.0/10

独立研究者使用 45B Token 从零训练了一个名为 SHADOW-50M 的 44M 参数三值量化（\{-1,0,+1\}）大语言模型。该模型完整文件大小仅 19.8 MB，在笔记本电脑 CPU 上可达到每秒约 1,900 Token 的推理速度，运行时内存占用约为 41 MB，并支持编译为 WebAssembly 在浏览器标签页中以约 500 Token/s 的速度运行。该模型采用固定 512 位指纹替代传统训练嵌入（Embedding）来表示 73,880 个词表 Token，并集成了用于算术、日期、排序等操作的外部电路计算机制，同时通过内存映射和 1 比特注意力状态存储实现了高效的外部持久化记忆检索。

reddit · r/MachineLearning · /u/Final-Data-1410 · 9月15日 12:59

**「背景介绍」** 极小型语言模型与三值量化技术旨在通过大幅压缩模型参数规模和权重精度，使复杂的语言理解能力得以在资源极度受限的边缘设备甚至单片机上运行。传统的嵌入层通常需要大量参数来进行训练，而通过固定指纹和外部计算模块则能绕过部分传统模型的资源瓶颈。

**「影响评估」** 该实验展示了通过创新的架构设计，让极小体积的本地模型在特定任务和计算检索场景中具备极高执行效率与可行性的潜力。不过由于通用知识单薄和创造性写作能力不足，它目前仍属于技术概念验证阶段，尚不能完全替代通用大语言模型。

**标签**: `#Machine Learning`, `#Large Language Models`, `#Model Optimization`, `#Quantization`, `#Edge AI`

---

<a id="item-tech-news-4"></a>
### [Prior Labs 发布全新表格基础模型 TabPFN-3.5](https://www.reddit.com/r/MachineLearning/comments/1wh4xhy/tabpfn35_is_released_as_the_next_sota_tabular/) ⭐️ 8.0/10

Prior Labs 于近期发布了全新的表格基础模型 TabPFN-3.5，在 TabArena 和 BeyondArena 基准测试中登顶，支持高达 100 万行和 20 万个特征的数据。该版本推出了三款新变体：处于 alpha 阶段的 TabPFN-3.5-Fast 运行速度较基础模型提升 6 倍，通过 API 提供的 TabPFN-3.5-Thinking 允许通过增加计算量来换取更高准确率，同时还包含 TabPFN-3.5-Plus。在 BeyondArena 测试中，该模型在文本丰富、高基数和高维度数据上表现优异，其 Elo 评分比较强的上一代基线高出 250 分，比此前整体领先者高出 150 分，其中 Thinking 变体在 BeyondArena 和 TabArena 上分别比基础模型提升了 20 和 44 个 Elo 积分。

reddit · r/MachineLearning · /u/tuanacelik · 9月15日 16:18

**「背景」** 表格基础模型（Tabular Foundation Models）是一类旨在通过预训练直接对各种表格数据集进行预测的机器学习模型，免去了传统机器学习方法中复杂的特征工程和逐个模型调参过程。Prior Labs 先前开发了 TabPFN 模型，利用先验拟合网络（Prior-Data Fitted Networks）在小型表格数据预测上取得了突破。

**「影响」** 该模型的发布显著提升了大规模、高维度及文本丰富表格数据的自动化预测性能，为开发者和企业用户在复杂表格场景中提供了高效且高精度的全新选择。

**标签**: `#artificial intelligence`, `#machine learning`, `#tabular data`, `#foundation models`, `#benchmarks`

---

<a id="item-tech-news-5"></a>
### [联发科发布天玑 9600 Pro 移动芯片](https://www.reuters.com/business/media-telecom/mediatek-launches-new-mobile-chip-using-tsmcs-most-advanced-technology-2026-09-15/) ⭐️ 8.0/10

联发科于 2026 年 9 月 15 日推出旗舰手机芯片天玑 9600 Pro，采用台积电 2 纳米制程打造，成为该公司首款运用该先进制程的手机处理器，并同步发布了采用 3 纳米制程的天玑 9600M。天玑 9600 Pro 配备了专用 AI 处理器，在处理用户提示词以及启动模型生成前的性能表现较上一代产品提升了 51%。联发科表示，搭载这两款芯片的首批智能手机产品将很快投放市场。

telegram · zaihuapd · 9月15日 08:57

**「背景」** 移动芯片制程的不断微缩是提升智能手机性能与能效比的关键技术路径，台积电的先进制程在近年来的旗舰芯片制造中占据核心地位。随着终端侧人工智能需求的快速增长，专用 AI 处理器逐渐成为旗舰移动芯片的标准配置。

**「影响」** 天玑 9600 Pro 的发布使联发科得以在先进制程和终端侧 AI 性能上进一步缩小与竞争对手的差距。首批搭载该芯片的终端上市后将直接提升移动设备在本地大模型和提示词处理方面的性能上限。

**标签**: `#hardware`, `#semiconductors`, `#mobile`, `#artificial intelligence`

---

<a id="item-tech-news-6"></a>
### [astral-sh/uv 发布 0.12.14 版本](https://github.com/astral-sh/uv/releases/tag/0.12.14) ⭐️ 7.0/10

于 2026 年 9 月 15 日发布的 astral-sh/uv 0.12.14 版本引入了多项重要改进。新版本支持通过 HTTP Range 请求恢复中断的下载，优化了包操作的诊断信息和退出码，并为工具升级操作提供了增强的提示。此外，该版本还通过并发任务和后台工作线程加速了依赖项解析，并修复了长路径支持及 Python 解释器发现等多个缺陷。

github · astral-releases-bot\[bot\] · 9月15日 02:19

**「背景介绍」** uv 是由 Astral 开发的、采用 Rust 编写的高性能 Python 包管理与项目管理工具，旨在提供极快的依赖解析和安装体验。它替代了传统的 pip、virtualenv 和 poetry 等工具的部分功能，广泛应用于现代 Python 和人工智能开发生态中。

**「影响与演进」** 这些改进显著提升了 Python 开发者在复杂网络和大型项目环境下的包管理效率与容错能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/astral-sh/uv">GitHub - astral-sh/uv: An extremely fast Python package and project manager, written in Rust. · GitHub</a></li>
<li><a href="https://docs.astral.sh/uv/">uv - Astral Docs</a></li>

</ul>
</details>

**标签**: `#python`, `#package-management`, `#developer-tools`, `#open-source`

---

<a id="item-tech-news-7"></a>
### [Typesafe.ai 推出的 System One Models 与 Jev 系统](https://typesafe.ai/blog/introducing-system-one-models-and-jev) ⭐️ 7.0/10

Typesafe.ai 推出了 System One Models 和 Jev，旨在将通用文本生成替换为专注于快速、类型化推理以及结构化输出的系统。该方法放弃了通用代码或文本生成能力，转而针对分类和评分等任务提供更快的执行速度和严格的数据结构。技术社区对这种架构的权衡及其与传统编码器模型的区别展开了深入讨论。

hackernews · albelfio · 9月15日 19:25 · [社区讨论](https://news.ycombinator.com/item?id=49717558)

**「背景」** 近年来，大型语言模型在通用文本生成方面取得了显著进展，但其在生产环境中往往面临推理速度慢、成本高以及难以保证结构化输出等挑战。为此，业界开始探索专注于快速类型化推理和结构化输出的替代架构，以满足大规模可靠工作流的需求。

**「影响」** 开发人员在处理分类、评分以及需要严格结构化输出的任务时，可以获得更快的推理速度，但这也牺牲了通用图灵完备文本生成的灵活性。

**「社区讨论」** 社区成员认为该系统的核心在于用通用生成能力换取类型化的快速推理，并探讨了它与传统编码器模型以及契约设计模式的异同与实际应用价值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds">Mini-Vibe Check: TypeSafe&#x27;s Jev Judged Everything I’ve Written in 0.7 Seconds</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#machine learning`, `#structured output`, `#inference`

---

<a id="item-tech-news-8"></a>
### [一款能聆听鸟鸣并绘制 19 世纪风格插图的开源电子墨水相框](https://github.com/arnegiacomo/fugleramme) ⭐️ 7.0/10

开源创客项目 ArneGiacomo/fugleramme 推出了一款创新设备，它结合了电子墨水屏、音频分类技术以及嵌入式硬件，能够聆听周围的鸟鸣声，并将其自动渲染为 19 世纪风格的精美插图。该项目借助传统的神经网络音频分类模型 BirdNET 来识别鸟类品种，完美融合了现代机器学习与复古的艺术呈现形式。开发者 Arne Munthe-Kaas 推出的这件硬件艺术品在开源社区中获得了极高的关注与赞赏。

hackernews · arnemunthekaas · 9月15日 12:31 · [社区讨论](https://news.ycombinator.com/item?id=49711544)

**「背景」** 电子墨水屏由于其功耗极低、在强光下可读性好等特点，常被用于低功耗的智能家居展示设备。而 BirdNET 则是用于鸟类声音识别的传统深度学习生态系统，能够通过音频特征精准分类各种鸟鸣声。

**「影响」** 该项目为硬件开发者和鸟类爱好者提供了一个兼具实用性与趣味性的开源制作范例，激发了社区关于将低功耗显示屏与环境音频识别相结合的更多创意。

**「社区讨论」** Hacker News 社区用户对该项目给予了极高评价，认为它完美融合了多种创意并带来了魔幻般的体验，同时讨论了其底层使用的 BirdNET 模型以及电子墨水屏在物联网设备中的超长续航优势。

**标签**: `#hardware`, `#embedded systems`, `#machine learning`, `#open source`, `#maker`

---

<a id="item-tech-news-9"></a>
### [互联网档案馆发布关于 Wayback Machine 访问问题与防护措施的更新](https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/) ⭐️ 7.0/10

互联网档案馆（Internet Archive）近日针对 Wayback Machine 遭遇的大规模自动化流量与抓取行为发布了更新，并说明了为维持服务运行而实施的保护措施。由于许多爬虫试图通过 Wayback Machine 绕过对源站的访问限制，导致这一关键的非营利互联网基础设施承受了沉重负载，部分网站也因此选择退出。社区成员对此类恶意抓取行为表示谴责，并担忧 AI 军备竞赛引发的滥用会给免费公开资源带来毁灭性打击。同时，也有用户反映在使用时遇到了 429 访问限制错误。

hackernews · ChrisArchitect · 9月15日 17:52 · [社区讨论](https://news.ycombinator.com/item?id=49716176)

**「背景」** Wayback Machine 是由互联网档案馆运营的数字档案馆，致力于为公众提供互联网历史网页的存档与查阅服务。近年来，该服务在应对高强度自动化抓取以及新闻出版商的访问限制时面临着巨大的技术和运营压力。

**「影响」** 高强度的自动化抓取不仅导致 Wayback Machine 出现服务不稳定和部分用户的访问受阻，还促使更多网站选择退出归档，进一步威胁到全球互联网历史记录的自由访问。

**「社区讨论」** 社区讨论普遍谴责了利用 Wayback Machine 进行大规模抓取的行为，认为这是受 AI 军备竞赛驱动的恶意滥用，并对互联网档案馆在巨大压力下仍坚持维护开放访问表达了敬意和担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wayback_Machine">Wayback Machine - Wikipedia</a></li>
<li><a href="https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/">September | 2026 | Internet Archive Blogs</a></li>
<li><a href="https://blog.archive.org/2026/06/01/keep-the-news-in-the-wayback-machine/">Keep the News in the Wayback Machine | Internet Archive Blogs</a></li>

</ul>
</details>

**标签**: `#Internet Archive`, `#Wayback Machine`, `#web scraping`, `#infrastructure`, `#open source`

---

<a id="item-tech-news-10"></a>
### [开发者历时一个月为 M4 Mac Mini 构建 Linux GPU 驱动](https://codyho.dev/blog/gpu-driver/) ⭐️ 7.0/10

一名开发者在短短一个月内尝试为搭载 M4 芯片的 Mac Mini 构建 Linux GPU 驱动程序。这一进展凸显了使用大语言模型辅助逆向工程复杂硬件的潜力，从而绕过了传统方案中长达数年的开发周期。然而，该项目的实现方式以及开发者的背景在开源社区中引发了广泛的讨论与争议。

hackernews · ADevWithAnIdea · 9月15日 19:30 · [社区讨论](https://news.ycombinator.com/item?id=49717638)

**「背景」** 苹果 Apple Silicon 芯片由于缺乏官方文档，其 GPU 在 Linux 下的原生加速支持长期依赖逆向工程。Asahi Linux 项目一直是该领域的主要推进者，但其对新一代芯片的图形驱动支持仍在开发中。

**「影响」** 尽管该驱动技术上展示了加速 M3 及更新芯片的可能性，但由于涉及大语言模型的使用以及开发者的苹果前员工身份，其代码合并至 Linux 内核或 Asahi Linux 主线面临严格的合规与政策障碍。

**「社区讨论」** 社区评论对该驱动的开发速度表示惊叹，并探讨了 LLM 在逆向工程中的应用价值，但同时也对代码的知识产权合规性、前苹果员工身份带来的潜在利益冲突以及 Asahi Linux 项目的严格无 AI 政策表达了强烈的担忧。

**标签**: `#Linux`, `#GPU Drivers`, `#Apple Silicon`, `#Reverse Engineering`, `#LLM`

---

<a id="item-tech-news-11"></a>
### [GEFS 在 OpenBSD 上的早期预览](https://marc.info/?l=openbsd-tech&amp;m=178948744271633&amp;w=2) ⭐️ 7.0/10

OpenBSD 邮件列表近期发布了 GEFS 文件系统的早期预览，该文件系统此前已在 9front 操作系统中得到应用并经过了夜间构建的测试。GEFS 专注于快照一致性，并通过在块指针中包含数据哈希来提供数据完整性检查，从而在底层存储介质返回损坏数据或程序写入垃圾数据时能够及时检测并报告。这一进展引发了系统程序员和 BSD 社区的广泛关注，部分讨论还将其与 DragonFly BSD 的 HAMMER2 文件系统进行了对比。

hackernews · sippingabonedry · 9月15日 17:12 · [社区讨论](https://news.ycombinator.com/item?id=49715590)

**「背景简介」** GEFS（Good Enough File System）最初是为 Plan 9 操作系统设计的，它基于复制-写入（COW）树状结构构建，旨在提供崩溃安全、支持快照、具备数据损坏检测以及实现相对简单快速的文件系统。该文件系统此前已在 9front 操作系统中得到应用和测试。-1-1, tool-1-2

**「影响」** 这一进展为 OpenBSD 社区提供了一个注重数据完整性和快照一致性的新兴文件系统选项，丰富了操作系统的存储技术生态。

**「社区讨论」** 社区成员对作者的工作表示尊重，并分享了关于 GEFS 设计文档、EuroBSDCon 相关演讲以及 9front 测试情况的链接，同时也有开发者表达了对 DragonFly BSD 的 HAMMER2 文件系统移植到 OpenBSD 的兴趣。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.lavx.hu/article/gefs-aims-to-make-file-corruption-easier-to-survive">GEFS aims to make file corruption easier to survive | LavX News</a></li>
<li><a href="https://orib.dev/gefs.pdf">PDF GEFS, A Good Enough File System</a></li>

</ul>
</details>

**标签**: `#OpenBSD`, `#file systems`, `#operating systems`, `#storage`

---

<a id="item-tech-news-12"></a>
### [数据隐私担忧促使英伟达与博思艾伦等企业限制外部 AI 模型使用](https://www.theinformation.com/articles/anthropic-data-fears-prompt-nvidia-palantir-booz-allen-restrict-model-use) ⭐️ 7.0/10

英伟达、Palantir 和博思艾伦等大型企业开始限制或减少使用 Anthropic 等公司的外部 AI 模型，并要求供应商提供不滥用客户数据的保证。由于担心 AI 公司可能利用客户的知识产权进行模型学习，数据保留与隐私风险正促使涉密或涉及敏感业务的企业全面重新评估其 AI 模型使用策略。

telegram · zaihuapd · 9月15日 01:02

**「背景」** 随着企业级生成式 AI 的普及，第三方大模型在训练和推理过程中对用户数据的收集与保留引发了广泛的安全合规担忧。许多涉及核心知识产权和国防敏感业务的公司开始收紧对外部模型的访问权限，以防范潜在的数据泄露与合规风险。

**「影响」** 此举表明大型企业对数据安全的要求正在改变企业级 AI 市场格局，促使 AI 供应商必须提供更严格的数据隐私保护承诺。

**标签**: `#artificial intelligence`, `#data privacy`, `#enterprise software`, `#security`

---

<a id="item-tech-news-13"></a>
### [工信部与发改委印发电子信息制造业十五五规划](https://www.secrss.com/articles/93961) ⭐️ 7.0/10

中国工业和信息化部与国家发展改革委联合印发了《电子信息制造业发展“十五五”规划》，部署了提高先进制程能力、突破高端手机核心芯片与 PC 高性能芯片等 17 项重点任务。规划明确提出，到 2030 年规模以上企业营业收入将突破 30 万亿元，产业研发投入强度达到 3.5%，并大力推进开源鸿蒙操作系统搭载、RISC-V、人工智能芯片及北斗等领域的发展。

telegram · zaihuapd · 9月15日 03:10

**「背景」** 电子信息制造业是国民经济的战略性、基础性和先导性支柱产业，中国政府通过制定并实施五年规划来引导该行业的技术升级、产业链安全和国产化替代进程。

**「影响」** 该规划将直接指导中国电子信息制造业在未来数年内的技术攻关与产业布局，加速国内半导体、芯片设计及国产操作系统生态的商业化落地。

**标签**: `#semiconductors`, `#hardware`, `#operating systems`, `#public policy`, `#RISC-V`

---

<a id="item-tech-news-14"></a>
### [桑德斯等议员提法案拟永久禁止超级智能 AI](https://www.techspot.com/news/113831-new-bernie-sanders-bill-would-ban-superintelligent-ai.html) ⭐️ 7.0/10

美国参议员伯尼·桑德斯与众议员亚历山大·奥卡西奥-科尔特斯联合提出了《禁止人工超级智能法案》，旨在永久禁止开发和部署超级智能 AI，并在联邦监管机构制定出安全规则前暂停先进 AI 的开发。该法案还致力于推动达成国际协议以在全球范围内阻止超级智能的出现，并计划设立内阁级机构来监视和清除前沿 AI 系统的危险能力。违反该法案的个人将面临最高 20 年的监禁，涉事企业则可能遭受公司解散等严厉处罚。

telegram · zaihuapd · 9月15日 04:26

**「背景」** 随着生成式人工智能和前沿 AI 技术的快速发展，社会各界对其潜在的失控风险和安全隐患日益关注。立法者和政策制定者开始尝试通过法律手段对人工智能的研发边界和安全标准进行监管。

**「影响」** 如果该法案最终通过，将对整个人工智能产业的研发节奏、合规成本以及前沿技术的全球布局产生深远影响。

**标签**: `#artificial intelligence`, `#AI regulation`, `#government policy`, `#superintelligence`

---

<a id="item-tech-news-15"></a>
### [谷歌授权全体工程师在内部平台使用 Anthropic Claude 编程模型](https://www.businessinsider.com/google-finally-lets-all-engineers-use-anthropics-claude-2026-9) ⭐️ 7.0/10

谷歌已正式允许全公司工程师在内部 Antigravity 开发平台上使用 Anthropic 最强的编程模型 Claude（Opus 5）作为 Gemini 的补充。过去谷歌严格限制员工使用外部编程工具，此次开放按每位员工配额提供。尽管谷歌是 Anthropic 的投资者并计划投入最多 40 万万美元，此举仍被视为对竞争压力的直接回应。

telegram · zaihuapd · 9月15日 05:31

**「背景」** 科技巨头通常强制内部员工优先使用自研 AI 模型以保障技术独立性与安全性。谷歌此前由于拥有 Gemini 且对 Anthropic 进行了重大投资，在内部开发工具的外部模型准入上采取了严格限制。

**「影响」** 此举为谷歌工程师提供了更灵活的 AI 辅助编程选项，并在内部实际验证了多模型并存的技术路线。

**标签**: `#Artificial Intelligence`, `#Software Engineering`, `#Google`, `#Anthropic`, `#Developer Tools`

---

<a id="item-tech-news-16"></a>
### [OpenAI 被曝雇用合同工人工阅读 ChatGPT 聊天记录](https://www.404media.co/inside-project-lily-the-humans-reading-your-chatgpt-chats/) ⭐️ 7.0/10

根据 404 Media 的报道，OpenAI 正在雇用数百名合同工手动阅读用户的 ChatGPT 提示词和完整对话内容，以便为模型回复评分并提出修改意见。虽然 OpenAI 表示会在审核前尽量剥离个人信息，但其承认敏感细节仍有可能被审核员看到，这引发了外界对 AI 训练中用户隐私安全的担忧。同时，另一家 AI 公司 Anthropic 也确认使用了类似的人工审核流程来改进其模型。

telegram · zaihuapd · 9月15日 11:56

**「背景」** 在大语言模型的开发和对齐过程中，人工标注和评估（如基于人类反馈的强化学习 RLHF）一直是提升模型回复质量和安全性的常见方法。然而，由于用户经常在聊天中输入包含个人身份信息、财务数据或企业机密等敏感内容，如何在模型训练需求与用户隐私保护之间取得平衡长期受到行业关注。

**「影响」** 这一情况提醒广大用户在与 ChatGPT 等 AI 交互时应避免输入敏感的个人或机密信息。

**标签**: `#OpenAI`, `#ChatGPT`, `#AI Privacy`, `#Data Security`, `#Artificial Intelligence`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [Training the Fastest Kimi K3 DSpark Speculator Using GB300 NVL72](https://vllm.ai/blog/2026-09-15-kimi-k3-dspark) ⭐️ 8.0/10

rss · vLLM Blog · 9月15日 00:00

**「背景」** 作者指出，虽然 DSpark 等区块级 speculative decoding 算法能提升生成速度，但训练拥有 2.8T 参数的 frontier 模型（如 Kimi K3）会面临严峻的硬件显存限制，且单节点架构无法满足大规模隐状态（hidden states）的提取需求。

**「方案」** 为了解决这一难题，作者团队利用 GB300 NVL72 硬件与 vLLM 的 Speculators 训练库，开发了 MooncakeHiddenStatesConnector，通过 Mooncake 传输引擎在多节点间异步流式传输目标模型的隐状态。该系统将控制路径与隐状态数据路径分离，采用两节点推理加一节点训练的拓扑结构，配合五层五亿参数的草稿模型，在维持极低首字延迟的同时实现了卓越的并发吞吐量。

**「启示」** 作者证明了借助高性能硬件与解耦的隐状态传输架构，开源训练库完全能够支撑超大规模前沿模型的复杂投机解码方案，从而显著提升大模型推理的交互速度与吞吐能力。

**标签**: `#speculative-decoding`, `#vllm`, `#distributed-training`, `#hardware-acceleration`, `#llm-inference`

---

<a id="item-tech-blog-2"></a>
### [向 AI 代理解释原因而非过程](https://seangoedecke.com/tell-agents-the-why/) ⭐️ 7.0/10

rss · Sean Goedecke · 9月15日 00:00

**「背景」** 早期 AI 代理容易犯错，因此用户需要提供精确的代码实现步骤。然而，随着前沿模型的性能大幅提升，它们往往因为不了解用户的真实意图和优先级而做出错误的假设。

**「方案」** 作者肖恩·戈德克（Sean Goedecke）指出，给 AI 代理编写提示词时，应当传达整体目标、技术价值观以及相对优先级，而不是仅仅罗列死板的规范。例如，在实际项目中明确告知模型硬件约束、长期目标以及各项质量指标的取舍权衡，从而让聪明的模型自主寻找更优解。作者认为，仅仅提供具体技术规范的做法类似于“XY 问题”，会限制模型发挥其真正的价值。

**「启示」** 与现代 AI 代理协作时，分享广阔的上下文与优先级比寻找所谓的“完美魔法提示词”更为有效。这有助于充分发挥模型的潜力，避免陷入僵化的技术细节。

**标签**: `#ai agents`, `#prompt engineering`, `#developer workflow`, `#llm`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [中国八月零售额增长放缓且投资下滑加剧](https://www.cnbc.com/2026/09/15/china-august-retail-sales-industrial-output-investment-exports-.html) ⭐️ 8.0/10

中国国家统计局周二公布的数据显示，8 月零售额同比实际增长 0.4%，较 7 月的 0.6%进一步放缓且低于市场预期；同时，今年前八个月城镇固定资产投资同比下降 7.2%，跌幅比前七个月有所加深。

rss · CNBC Finance · 9月15日 09:46

**「背景情况」** 由于国内供需失衡以及房地产市场低迷持续拖累经济，今年第二季度中国经济增速放缓至 4.3%，创下三年多来的最弱水平。

**「市场影响」** 疲软的经济数据加大了市场对北京推出更具力度的财政刺激政策以提振国内需求的预期。

**标签**: `#China economy`, `#retail sales`, `#macroeconomics`, `#fiscal policy`, `#economic growth`

---

<a id="item-finance-news-2"></a>
### [共享单车服务规范新国标发布](https://ysxw.cctv.cn/article.html?toc_style_id=feeds_default&amp;amp;t=1789434965546&amp;amp;item_id=10192909235938930936&amp;amp;channelId=1119) ⭐️ 7.0/10

中国国家市场监督管理总局发布了共享单车服务的新国家标准，对运营企业的车辆投放、租还车服务、用户信息安全及人员管理等全流程提出规范要求，并将于 2026 年 11 月正式实施。

telegram · zaihuapd · 9月15日 02:40

**「背景」** 随着共享单车行业快速发展，为了解决过去部分城市出现的乱停放、运维不及时及用户信息安全隐患等问题，国家出台了这一全新的统一服务标准。

**「影响」** 新标准将促使国内共享单车运营企业升级车辆智能终端和管理系统，并利用电子围栏等技术引导市民规范停车。

**标签**: `#regulatory policy`, `#shared mobility`, `#market regulation`, `#transportation`

---

<a id="item-finance-news-3"></a>
### [华为与赛力斯调整合作模式](https://www.cls.cn/detail/2483113) ⭐️ 7.0/10

知情人士称，华为与赛力斯的智选车合作模式预计于本周调整为轻资产模式，产品和运营主导权由华为转交给赛力斯。

telegram · zaihuapd · 9月15日 03:30

**「背景」** 智选车模式是指华为深度参与产品定义、设计和营销等环节的汽车业务合作方式。

**「影响」** 鸿蒙智行将集中资源推动智界、享界、尊界和尚界等其他合作品牌的发展。

**标签**: `#Automotive`, `#Partnership`, `#Corporate Strategy`, `#Huawei`, `#Seres`

---

<a id="item-finance-news-4"></a>
### [字节跳动 2026 上半年净利润下降](https://finance.sina.com.cn/jjxw/2026-09-15/doc-inirxpiq6857286.shtml) ⭐️ 7.0/10

据外媒报道，受人工智能领域大规模投入影响，字节跳动 2026 年上半年净利润降至约 200 亿美元且同比下滑，净利润率降至 16.7% 左右，字节跳动未对以上数据置评。

telegram · zaihuapd · 9月15日 15:59

**「背景」** 同期字节跳动营收同比增长 30%，海外收入在 TikTok 等海外业务推动下占比突破三成。

**标签**: `#ByteDance`, `#Artificial Intelligence`, `#Corporate Earnings`, `#Tech Sector`, `#Financial Performance`

---