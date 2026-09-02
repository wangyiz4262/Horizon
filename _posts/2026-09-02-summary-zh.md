---
layout: default
title: "Horizon Summary: 2026-09-02 (ZH)"
date: 2026-09-02
lang: zh
---

> 从 54 条内容中筛选出 18 条重要资讯。

---

**科技新闻**
1. [Anthropic 发布 Claude Fable 5.1 与 Mythos 5.1](#item-tech-news-1) ⭐️ 8.0/10
2. [训练 1.5 小时的小型 Transformer 超越许多 LLM](#item-tech-news-2) ⭐️ 8.0/10
3. [Python 3.15.0 候选版 2 发布，呼吁维护者准备 wheels](#item-tech-news-3) ⭐️ 8.0/10
4. [Virtualizor 更新链遭 BGP 劫持，恶意更新植入 root 后门](#item-tech-news-4) ⭐️ 8.0/10
5. [Dan Luu 审视 Ed Zitron 的 AI 怀疑论预测准确度](#item-tech-news-5) ⭐️ 7.0/10
6. [Jujutsu 版本控制系统创建者 Martin 加入 ERSC](#item-tech-news-6) ⭐️ 7.0/10
7. [在 48GB Mac 上以约 12 tok/s 运行 104GB Qwen3.8-Flash-Next](#item-tech-news-7) ⭐️ 7.0/10
8. [韩国万亿美元主权 AI 投资：英伟达受益，SK 海力士受损](#item-tech-news-8) ⭐️ 7.0/10
9. [TontaubeV1：2.9B 参数开源 TTS 模型，专注长文本生成](#item-tech-news-9) ⭐️ 7.0/10
10. [EvoUndo：面向 LLM 智能体自进化的可恢复性约束框架](#item-tech-news-10) ⭐️ 7.0/10

**财经新闻**
1. [全国光伏装机首超煤电，成第一大电源](#item-finance-news-1) ⭐️ 9.0/10
2. [美联储理事巴尔称若通胀未见缓和将支持加息](#item-finance-news-2) ⭐️ 8.0/10
3. [财政部、税务总局：外籍个人取得外商投资企业股息红利按 20%缴个税](#item-finance-news-3) ⭐️ 8.0/10
4. [日本放宽加班上限：45 小时不再强制](#item-finance-news-4) ⭐️ 8.0/10
5. [财报后：戴尔、GitLab 大涨，MongoDB 跌 12%](#item-finance-news-5) ⭐️ 7.0/10
6. [高通宣布 2026 年 9 月 1 日后出货芯片涨价两位数](#item-finance-news-6) ⭐️ 7.0/10
7. [《微短剧发展管理办法》今起施行](#item-finance-news-7) ⭐️ 7.0/10
8. [三部门发布汽车行业境外竞争与合规指引](#item-finance-news-8) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Anthropic 发布 Claude Fable 5.1 与 Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1) ⭐️ 8.0/10

Anthropic 发布了 Claude Fable 5.1 和 Claude Mythos 5.1 两个模型，主要改进包括更自然的写作风格、可选的思考投入级别，以及缓存读取价格从每百万 token 1 美元降至 0.25 美元。官方文档和系统卡已经上线。此次更新也被认为是 Anthropic 对模型定价策略的一次重要调整。

hackernews · denysvitali · 9月1日 17:53 · [社区讨论](https://news.ycombinator.com/item?id=49525378)

**「背景」** Anthropic 在 2026 年 6 月 9 日推出 Claude Fable 5 和 Mythos 5，并于 2026 年 9 月 1 日发布后续版本 Fable 5.1 与 Mythos 5.1，两个新模型均支持 100 万 token 的上下文窗口。Fable 5.1 改进写作风格、提供更多思考强度档位，并将缓存读取价格从每百万 token 1 美元降至 0.25 美元（降幅 75%），同时带来破坏性 API 变更。Mythos 5.1 面向经过审核的网络安全防御者和生命科学研究者放宽部分安全过滤，目前仅向部分美国组织开放，尚未公布更广泛的开放时间。

**「影响」** Anthropic 将 Fable 5.1 的缓存读取定价从每百万输入 token 1.00 美元降至 0.25 美元，降幅达 75%，这对以缓存命中为主的 Claude Code 和智能体循环工作负载最直接地降低了成本；列表价格仍为每百万输入 token 10 美元、每百万输出 token 50 美元，与 Fable 5 相同。Fable 5.1 于 2026 年 9 月 1 日正式可用。

**「社区讨论」** Anthropic 员工 felixrieseberg 称 Fable 5.1 的写作风格显著改进、更少模板化且更可靠地遵循风格指令；simonw 测试了 low、medium、high、xhigh 和 max 的思考投入级别，max 一次生成耗时近 14 分钟并在修复工具后效果明显更好。GodelNumbering 指出缓存读取降价使 Fable 5.1 的缓存读取成本仅为 Opus 的一半，并认为若不看 Terminal-Bench-Science 结果则很难看到整体提升；exabrial 则批评该发布是“削弱 Fable”和把 Mythos 当营销手段，并反对移除思考痕迹。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.marktechpost.com/2026/09/01/anthropic-releases-claude-fable-5-1-and-claude-mythos-5-1-52-6-on-terminal-bench-science-and-75-cheaper-cache-reads/">Anthropic Releases Claude Fable 5.1 and Claude Mythos 5.1: 52.6% on Terminal-Bench-Science and 75% Cheaper Cache Reads - MarkTechPost</a></li>
<li><a href="https://tech-ish.com/2026/09/01/anthropic-releases-claude-fable-5-1-and-mythos-5-1-here-is-what-changed/">Anthropic releases Claude Fable 5.1 and Mythos 5.1. Here is what changed - tech-ish</a></li>
<li><a href="https://www.kucoin.com/news/flash/anthropic-launches-claude-fable-5-1-and-mythos-5-1-for-enterprise-ai-tasks">Anthropic Launches Claude Fable 5.1 and Mythos 5.1 for Enterprise AI Tasks | KuCoin</a></li>
<li><a href="https://llm-stats.com/blog/research/claude-fable-5-1-launch">Claude Fable 5.1: Same Sticker, Cheaper Cache - llm-stats.com</a></li>
<li><a href="https://venturebeat.com/technology/anthropics-claude-fable-5-1-and-mythos-5-1-arrive-with-a-75-cost-reduction-for-fable-cache-reads">Anthropic&#x27;s Claude Fable 5.1 and Mythos 5.1 arrive with a 75% ...</a></li>
<li><a href="https://aireiter.com/blog/claude-fable-5-1-api-pricing">Claude Fable 5.1 API Pricing: Cache Math (2026) - aireiter.com</a></li>

</ul>
</details>

**标签**: `#Claude`, `#Anthropic`, `#LLM`, `#AI model release`, `#pricing`

---

<a id="item-tech-news-2"></a>
### [训练 1.5 小时的小型 Transformer 超越许多 LLM](https://mvakde.github.io/blog/44-on-arc-1/) ⭐️ 8.0/10

一位开发者在 Hacker News 上分享，他仅用 1.5 小时从头训练了一个小型自回归 Transformer，并报告其在 ARC 基准上超过许多大型语言模型。作者强调这不是 LLM，而是一个专用小模型，目的是说明极其复杂的问题不一定需要 LLM 和巨大的训练成本。得分提升主要来自现代架构（如 SwiGLU 和 RMSNorm）、更多样的数据与更好的混洗，以及将层数从 4 层扩展到 8 层。针对“在评估谜题上训练”的批评，作者澄清 ARC 是元学习基准，评估谜题本应用作学习材料，且并未训练测试标签。该结果引发了关于样本效率、模型规模和“挤柠檬”式调优的技术讨论。

hackernews · porridgeraisin · 9月1日 09:52 · [社区讨论](https://news.ycombinator.com/item?id=49519939)

**「背景」** ARC-AGI（Abstraction and Reasoning Corpus）是 François Chollet 于 2019 年提出的基准测试，旨在衡量 AI 系统的流体智能与抽象推理能力，而非单纯的语言或知识记忆。该基准由大量视觉推理谜题组成，要求模型从少量示例中归纳规则，因此也被视为一个元学习基准。本文作者 Mithil Vakde 在一张租用的 RTX 5090（约 0.67 美元成本）上从零训练了一个小型自回归 Transformer，耗时约 1.5 小时，在 ARC-AGI-1 公共评估集上达到 44% 的准确率，与 TRM/HRM 相当，并声称超过许多大型语言模型，同时在 ARC-2 上获得 7% 的成绩。

**「影响」** 对资源有限的 AI 研究者和工程师而言，这提供了一条低成本、可复现的路径：在特定推理基准上，小型专用 Transformer 也能以极小算力取得有竞争力的结果，但应谨慎将其推广为通用大模型的替代方案。

**「社区讨论」** 作者在 Hacker News 评论中回应质疑，指出该工作不是 LLM，并澄清 ARC 作为元学习基准允许使用评估谜题作为学习材料，且从未训练测试标签。讨论中，有评论者认为这类调优属于“挤柠檬”式的最后手段，并建议先证明方法本身能在不做这些调整的情况下接近最先进水平。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi">ARC Prize - What is ARC-AGI?</a></li>
<li><a href="https://arcprize.org/arc-agi/1">ARC-AGI-1</a></li>
<li><a href="https://mvakde.github.io/blog/44-on-arc-1/">44% on ARC-AGI-1 in 67 cents - Mithil Vakde’s Homepage</a></li>
<li><a href="https://github.com/mvakde/mdlARC/tree/main/">44% on ARC-AGI-1: trained from scratch for just ~$0.67</a></li>

</ul>
</details>

**标签**: `#transformer`, `#ARC benchmark`, `#efficient training`, `#deep learning`, `#small models`

---

<a id="item-tech-news-3"></a>
### [Python 3.15.0 候选版 2 发布，呼吁维护者准备 wheels](https://simonwillison.net/2026/Sep/1/python-315-rc-2/) ⭐️ 8.0/10

Python 3.15.0 发布了第二个候选版，发布经理 Hugo van Kemenade 宣布这是最终候选版，正式版预计在 10 月发布。进入候选版阶段后，只允许经过审查的明确 bug 修复变更。官方强烈鼓励第三方项目维护者在此期间为 3.15 做好准备，在 PyPI 上发布 Python 3.15 的 wheels；针对候选版构建的二进制 wheels 将兼容未来的 Python 3.15 版本。目前该候选版尚未可用于 GitHub Actions，但可以通过 actions/setup-python@v7 的 allow-prereleases 和 check-latest 标志自动测试候选版。Simon Willison 提醒大家在候选版期间运行测试套件，以免重蹈他在 Python 3.10 时期因未测试 RC 而导致 bug 随正式版发布的覆辙。

rss · Simon Willison · 9月1日 14:59

**「背景」** Python 在正式发布前会经历多个候选版阶段，候选版之后通常只接受明确的 bug 修复，不再引入新功能。构建 wheels 的第三方项目需要针对候选版进行测试，以确保正式版发布时兼容性；此次官方明确表示针对候选版构建的 wheels 可以用于未来的 3.15 版本，因此提前测试是安全且必要的。

**「影响」** Python 第三方库维护者应尽快构建并发布针对 Python 3.15.0 候选版的 wheels，并测试其项目兼容性，以便在 10 月正式版发布时无缝支持新版本。使用 GitHub Actions 的项目可以在矩阵中加入 3.15 并启用 allow-prereleases 和 check-latest，从而自动从 RC1 切换到 RC2，再切换到正式版。

**标签**: `#python`, `#release-candidate`, `#software-engineering`, `#open-source`, `#programming-language`

---

<a id="item-tech-news-4"></a>
### [Virtualizor 更新链遭 BGP 劫持，恶意更新植入 root 后门](https://www.virtualizor.com/blog/security-incident-bgp-hijacking/) ⭐️ 8.0/10

Virtualizor 的更新基础设施在 2026 年 8 月 28 日至 30 日期间遭到 BGP 路由劫持，攻击者利用有效 TLS 证书投递了恶意更新包，可在受影响系统上安装 root 后门。官方确认仅在更新窗口期内执行更新的少量安装受到影响，并强调这不是软件代码漏洞，而是分发链路被劫持。独立取证显示，恶意包会写入 root SSH 密钥、安装 Java 载荷并建立持久化服务；AlbaHost 在 34 台 hypervisor 中发现 5 台存在入侵指标。Softaculous 表示目前没有证据表明其他产品受到影响。

telegram · zaihuapd · 9月1日 06:05

**「背景」** BGP（边界网关协议）劫持是指攻击者通过操纵互联网路由公告，将原本流向特定 IP 段的流量重定向到自己的服务器；Virtualizor 及其母公司 Softaculous 的更新基础设施在 2026 年 8 月 28 日至 30 日期间遭到此类劫持，期间检查更新的 Virtualizor 安装可能从攻击者服务器收到恶意更新包。由于攻击者能够控制请求的接收路径，合法的 TLS 证书也无法防止恶意载荷被分发。这类攻击属于供应链投毒，用户即使保持软件更新也可能中招，需要检查系统是否被植入 SSH 密钥、Java 载荷或持久化服务。

**「影响」** 在 2026 年 8 月 28 日至 30 日窗口期内更新过 Virtualizor 的用户，应立即检查系统是否出现未知的 root SSH 授权密钥、Java 载荷及持久化服务，并将受影响主机视为已失陷。AlbaHost 已在 34 台 hypervisor 中确认 5 台存在危害指标，其他使用该窗口期更新的环境也应进行同等排查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.virtualizor.com/blog/security-incident-bgp-hijacking/">Security Incident – BGP Hijacking – Virtualizor</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/hackers-push-malicious-virtualizor-update-in-bgp-hijacking-attack/">Hackers push malicious Virtualizor update in BGP hijacking attack</a></li>

</ul>
</details>

**标签**: `#security`, `#BGP hijacking`, `#supply chain`, `#Virtualizor`, `#malware`

---

<a id="item-tech-news-5"></a>
### [Dan Luu 审视 Ed Zitron 的 AI 怀疑论预测准确度](https://danluu.com/zitron/) ⭐️ 7.0/10

Dan Luu 发表分析文章，逐条审视 Ed Zitron 过去对 AI 行业的怀疑论预测，并以具体文本和后续事实判断其准确程度。该文出现在围绕 AI 投资泡沫和模型进展的激烈争论中，为评估知名批评者的说法提供了文本层面的参考。由于原始内容未提供细节，目前无法确知 Luu 对每条预测的判定结论，但文章本身以“预测是否成真”为核心。此类核查有助于区分事实与夸大宣传，尤其在 Zitron 的批评和 AI 高管宣传都经常被指过度的情况下。

hackernews · jatins · 9月1日 18:35 · [社区讨论](https://news.ycombinator.com/item?id=49526069)

**「背景」** 埃德·齐特龙（Ed Zitron）是一位广受引用的 AI 怀疑论者，经常公开预测 AI 行业的发展走向，包括对 AI 技术进步、公司增长和市场结果的判断。丹·鲁（Dan Luu）出于对“最广泛引用的 AI 怀疑论者”预测准确性的好奇，专门查阅了齐特龙公开预测的实际结果，并撰文进行了评估。丹·鲁在文中披露自己并未强烈支持或反对 AI 进步，以保持中立立场。相关讨论还指出，齐特龙的预测记录存在反复出错的情况，但其强力言论仍可能在受众将自信视为证据时继续产生影响。

**「社区讨论」** 评论中既有共识也有分歧：有观点认为 Zitron 已成为他所嘲讽的 AI 鼓吹者的镜像，因受众期待而无法承认错误；另一些评论则提醒不应把自己的预测投射到 Zitron 原话上。还有人指出文章未讨论超大规模云厂商通过 Anthropic、OpenAI 股权估值上升计入“其他收入”的现象。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://danluu.com/zitron/">How accurate have Ed Zitron&#x27;s AI skeptic predictions been?</a></li>
<li><a href="https://news.lavx.hu/article/how-accurate-have-ed-zitron-s-ai-skeptic-predictions-been">How accurate have Ed Zitron&#x27;s AI skeptic predictions been?</a></li>

</ul>
</details>

**标签**: `#AI`, `#skepticism`, `#predictions`, `#Dan Luu`, `#technology analysis`

---

<a id="item-tech-news-6"></a>
### [Jujutsu 版本控制系统创建者 Martin 加入 ERSC](https://ersc.io/blog/martin-joins-ersc) ⭐️ 7.0/10

Jujutsu（jj）版本控制系统的创建者 Martin 已加入开发平台公司 ERSC，ERSC 官方博客发布了这一消息。Jujutsu 是一款与 Git 兼容的现代版本控制工具，以强大的撤销能力、更简单的命令模型和灵活的分支操作而受到关注。Martin 的加入可能会影响 jj 的后续演进方向，也让 ERSC 在代码托管与版本控制领域获得技术背书。目前公告尚未披露具体职位或路线图。

hackernews · steveklabnik · 9月1日 17:46 · [社区讨论](https://news.ycombinator.com/item?id=49525297)

**「背景」** East River Source Control（ERSC）宣布任命 Jujutsu 版本控制系统创作者 Martin von Zweigbergk 为首席技术官，负责领导公司下一代版本控制平台的工程工作。von Zweigbergk 于 2019 年末将 Jujutsu 作为副业项目开始，后来在 Google 将其转为全职工作。ERSC 的目标是解决基于 Git 的远程代码托管在扩展性上的限制。

**「社区讨论」** Hacker News 上的评论意见分歧：一些用户称赞 jj 的撤销机制和整体体验，认为它是“更好、更智能的 Git”，但也有用户表示 Git 已足够用，并质疑 ERSC 作为 GitHub 竞争对手尚未说明如何解决 GitHub 的缺点以及自身的差异化价值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ersc.io/blog/martin-joins-ersc">East River Source Control Names Jujutsu Creator Martin von ...</a></li>

</ul>
</details>

**标签**: `#jujutsu`, `#version-control`, `#open-source`, `#developer-news`, `#ERSC`

---

<a id="item-tech-news-7"></a>
### [在 48GB Mac 上以约 12 tok/s 运行 104GB Qwen3.8-Flash-Next](https://github.com/carloslfu/slotstream) ⭐️ 7.0/10

开发者 carloslfu 发布了 Slotstream，一个基于 MLX 和 Swift 的 macOS 原生开源工具，通过专家卸载（expert offloading）和 SSD 流式加载，让低内存 Mac（最低 16GB）运行 125B 参数的 Qwen3.8-Flash-Next 4-bit 模型；在 48GB Mac 上实测约 12 tok/s。该模型文件约 104GB，通常需要 100GB+ 内存，Slotstream 的 auto-mode 可在内存占用与速度间取舍。项目安装/更新简单，下一步计划移植 MTP 模块以支持投机解码。该方案的价值在于让内存受限的 Mac 用户本地运行大型 MoE 模型，但速度与 16GB 档位表现仍需结合具体硬件验证。

hackernews · carloslfu · 9月1日 16:42 · [社区讨论](https://news.ycombinator.com/item?id=49524447)

**「背景」** Qwen3.8-Flash-Next 是 Qwen 系列的混合专家（MoE）模型，总参数为 125B，但每次推理只激活约 6B 参数：512 个专家中通常只有 10 个被路由、另加 1 个共享专家，因此单 token 的计算量接近小模型。不过完整权重仍需驻留内存，4-bit 量化后也要 100GB 以上，16GB 或 48GB 统一内存的 Mac 无法整体加载。MLX 是苹果芯片上的机器学习框架；Slotstream 的思路是利用专家卸载和 SSD 流式加载，只把当前需要的专家权重调入内存，从而在低内存 Mac 上以 MLX 和 Swift 原生方式运行该模型。

**「影响」** 对 16–48GB 统一内存 Mac 用户而言，这提供了一条无需高配硬件即可本地运行 125B 级 MoE 模型的可行路径，实际可用性仍取决于 SSD 速度与散热/内存压力。

**「社区讨论」** 评论中有人质疑 16GB Mac 上 5 tok/s 的可行性，称即使优化也会遇到热警告；另一些用户希望提高上下文窗口，并期待 32GB M6 能借助此类工作具备本地实用性。README 的可读性也被指需要清理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ollama.com/library/qwen3.8-flash-next:125b-mlx">qwen3.8-flash-next:125b-mlx</a></li>
<li><a href="https://ollama.com/orcarouter/Qwen3.8-Flash-Next-Uncensored:125b-a6b-mlx-4bit">orcarouter/Qwen3.8-Flash-Next-Uncensored:125b-a6b-mlx-4bit</a></li>

</ul>
</details>

**标签**: `#llm-inference`, `#model-offloading`, `#machine-learning`, `#mlx`, `#local-llm`

---

<a id="item-tech-news-8"></a>
### [韩国万亿美元主权 AI 投资：英伟达受益，SK 海力士受损](https://newsletter.semianalysis.com/p/koreas-trillion-dollar-sovereign) ⭐️ 7.0/10

据 Semianalysis 分析，韩国正推进一项万亿美元级的主权 AI 投资计划，并举办名为“国家 AI 锦标赛”的竞赛（被比作“鱿鱼游戏”）来筛选模型，其中最佳的非中国开源模型被淘汰。分析认为，英伟达是这一投资格局的最大赢家，而 SK 海力士则面临不利影响，三星也受到波及。文章还探讨了英伟达为何需要开源模型，以及该主权 AI 竞赛对 HBM 等存储芯片供应链的潜在影响。这些动态凸显主权 AI 支出正重塑全球半导体竞争格局。

rss · Semianalysis · 9月1日 20:14

**「背景」** 韩国正大举推进主权 AI 投资：据外部报道，三星电子和 SK 海力士等企业将在韩国西南部建设 4 座新晶圆厂，并由 SK 集团、GS 集团、Naver 等公司计划投资约 3550 亿美元，在 2029 年前建设 8.4GW 的 AI 数据中心容量。同时，三星电子和 SK 海力士已参与 Anthropic 的 H 轮融资，投资数万亿韩元，试图从半导体供应商向设计者角色延伸。这些动向是理解韩国 AI 竞赛以及 NVIDIA、SK 海力士、三星在该产业中赢家与输家判断的背景。

**「影响」** 对 SK 海力士和三星电子而言，尽管与英伟达、博通等客户锁定了总价值约 9500 亿美元的高带宽内存（HBM）供应协议，覆盖至 2030 年的供货，但市场投资者对 AI 硬件支出及定价的担忧导致两家公司股价在相关消息后显著下跌，并拖累 Kospi 指数走弱。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.chosun.com/english/market-money-en/2026/06/22/F7ERLXEIBREDHJIWFCQNRI327E/">Wall Street Boosts Samsung , SK Hynix Targets</a></li>
<li><a href="https://www.linkedin.com/posts/brunellalupano_southkorea-trillion-investment-activity-7478817061687902208-jpTN">#southkorea # trillion # investment #semiconductor # ai #datacenter...</a></li>
<li><a href="https://phoue.co.kr/en/posts/samsung-skhynix-anthropic-investment-ai-semiconductor-strategy/">Silicon&#x27;s Pledge: The Real Reason Samsung and SK Hynix Bet on...</a></li>
<li><a href="https://siliconanalysts.com/market/nvidia-sk-hynix-samsung-broadcom-lock-in-950b-hbm-supply-agreements-securing-nex-2026-07-25">Nvidia-SK Hynix &amp; Samsung-Broadcom Lock In $950B HBM Supply ...</a></li>
<li><a href="https://www.techtimes.com/articles/321554/20260725/samsung-sk-hynix-lock-ai-chip-supply-through-2030-950b-us-deals.htm">Samsung and SK Hynix Lock In AI Chip Supply Through 2030 With ...</a></li>
<li><a href="https://nai500.com/blog/2026/06/nvidia-nvda-seals-hbm-pact-as-sk-hynix-samsung-slump/">Nvidia NVDA seals HBM pact as SK Hynix, Samsung slump</a></li>

</ul>
</details>

**标签**: `#AI investment`, `#semiconductors`, `#Nvidia`, `#SK Hynix`, `#open source AI`

---

<a id="item-tech-news-9"></a>
### [TontaubeV1：2.9B 参数开源 TTS 模型，专注长文本生成](https://www.reddit.com/r/MachineLearning/comments/1w4afjn/we_released_tontaubev1_a_characterlevel_tts_model/) ⭐️ 7.0/10

作者发布了 TontaubeV1，一个 2.9B 参数的开源权重 TTS 模型，专注于表现力语音、长文本生成/旁白和低延迟本地推理，主要面向英语和德语，支持从最多一分钟参考音频进行零样本语音克隆。它基于 DualCodec 多码本离散音频编解码器，在 7 种语言约 20 万小时音频上训练。模型采用字符级分词，从 Qwen3-1.7B 检查点开始训练语义码本模型，并设计了分块和位置方案以保持上下文有界。当前版本需要至少 24GB 显存（低显存/均衡配置）或 32GB 显存（高吞吐配置）。在 400 段文本的 LLM 作为评判的基准中，其韵律得分为 50.1%，优于 ElevenLabs Flash v2.5，并比 Fish Audio S2 Pro、Gradium 和 Cartesia Sonic 3 更受青睐。

reddit · r/MachineLearning · /u/EAVDR · 9月1日 12:23

**「背景」** 文本到语音（TTS）模型将文本转换为自然语音，而基于大语言模型（LLM）的 TTS 通常使用原始分词器并预测音频 token。长文本生成面临上下文长度和音频拼接问题，字符级分词可以将字符到声音的映射简化，但可能影响语言理解。

**「影响」** 该模型让开发者和创作者能够在本地 GPU 上运行开源的、具有表现力的长文本 TTS，并支持零样本语音克隆，尽管至少需要 24GB 显存。

**标签**: `#TTS`, `#open-source`, `#machine learning`, `#audio generation`, `#character-level tokenization`

---

<a id="item-tech-news-10"></a>
### [EvoUndo：面向 LLM 智能体自进化的可恢复性约束框架](https://www.reddit.com/r/MachineLearning/comments/1w4m0hq/evoundo_recoverabilityconstrained_selfevolution/) ⭐️ 7.0/10

EvoUndo 提出了一个用于 LLM 智能体自进化可恢复性问题的框架，能够表示、综合、诊断并独立验证模型生成的自我修改在反事实状态下的可恢复性。在 600 个未见过的单次自进化任务中，该框架识别出 197 个未通过可恢复性验证的能力改进型突变。在原始恢复表示下，常规修复策略仅能恢复其中 0 个；确定性的 oracle 分析在原始恢复语言 L0 下恢复 48 个，而在扩展恢复演算下经验 oracle 恢复提升至 191 个。一项协议锁定的 2×2 接地-表达力干预实验分离了两个瓶颈：当原始语言足够时，精确状态地址接地将恢复成功率从 0/48 提升至 38/48（79.2%），而扩展恢复语言使 oracle 定义的 S1 层故障恢复率达 142/143（99.3%）。在 gpt-oss-120b 主干上，向更丰富语言添加精确地址诊断后恢复率降至 133/143（93.0%）；Qwen3.8-27B 复现实验保留了接地和表达力效应，但未复现这种负向交互，表明后者依赖模型。结果表明，可靠的智能体自进化需要验证、状态接地、见证语义和恢复语言表达力的协同设计，而非仅依赖迭代提示。

reddit · r/MachineLearning · /u/AccomplishedLeg1508 · 9月1日 19:17

**「背景」** LLM 智能体在运行时越来越多地修改自身的提示、工具、中间件、资源和执行框架，这种自进化可能提升能力，但成功的突变可能在不同于其创建状态的状态下留下无法安全逆转的持久影响。EvoUndo 正是针对这一可恢复性问题，通过显式建模和验证自我修改的可逆性，试图解决自进化中的安全性短板。

**「影响」** 对研究可恢复自进化 LLM 智能体的开发者而言，EvoUndo 的量化结果明确表明，仅靠迭代提示无法修复自然发生的可恢复性失败，必须在恢复语言表达力和状态接地方面进行协同设计，为构建可靠的自修改智能体提供了关键指导。

**标签**: `#LLM agents`, `#self-evolution`, `#recoverability`, `#machine learning research`, `#AI safety`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [全国光伏装机首超煤电，成第一大电源](https://content-static.cctvnews.cctv.com/) ⭐️ 9.0/10

据央视新闻，截至 2026 年 7 月底，全国光伏发电装机达 12.86 亿千瓦，占总装机的 31.5%，首次超过煤电成为我国第一大电源；2026 年 1 至 7 月光伏发电量约 8024 亿千瓦时，同比增长 15.5%，相当于每 8 度电中约有 1 度来自光伏。

telegram · zaihuapd · 9月1日 02:42

**「背景」** “光伏”即太阳能发电，“装机”指发电设备的额定发电能力；此前煤电长期是我国第一大电源，此次光伏在装机规模上首次反超煤电，反映电力结构出现标志性变化。

**标签**: `#太阳能`, `#能源转型`, `#中国电力`, `#光伏发电`, `#清洁能源`

---

<a id="item-finance-news-2"></a>
### [美联储理事巴尔称若通胀未见缓和将支持加息](https://www.cnbc.com/2026/09/01/fed-governor-barr-says-hell-support-rate-hike-if-inflation-doesnt-ease.html) ⭐️ 8.0/10

美联储理事迈克尔·巴尔周二表示，如果通胀没有缓和，他将支持加息；据 CME FedWatch 工具，市场目前定价本月加息概率约 66%。

rss · CNBC Finance · 9月1日 14:01

**「背景」** 此前美联储 7 月决定将基准利率维持在 3.5%-3.75%不变，而通胀率已近五年半高于 2%目标；作为理事，巴尔是利率决策机构 FOMC 的永久投票成员。主席沃什上周讲话被市场解读为倾向加息，下周公布的 CPI 和 PPI 将是下次会议前最后的通胀参考。

**标签**: `#monetary policy`, `#Federal Reserve`, `#interest rates`, `#inflation`, `#rate hike`

---

<a id="item-finance-news-3"></a>
### [财政部、税务总局：外籍个人取得外商投资企业股息红利按 20%缴个税](https://m.cnfin.com/wx/share?url=//m.cnfin.com/yw-lb//zixun/20260901/4463424_1.html) ⭐️ 8.0/10

财政部、税务总局发布公告，外籍个人从外商投资企业取得的股息红利所得，须按“利息、股息、红利所得”缴纳 20%个人所得税，自 2026 年 9 月 1 日起执行；此前依据财税字〔1994〕20 号享受的免税待遇同时废止。

telegram · zaihuapd · 9月1日 09:33

**「背景」** 此前，依据财税字〔1994〕20 号，外籍个人从外商投资企业取得的股息、红利暂免征收个人所得税；新公告废止了相关免税条款。外商投资企业向外籍个人支付股息红利时，应代扣代缴税款，并在支付所得次月 15 日内申报纳税。

**「影响」** 受影响的是在华外商投资企业及取得股息红利的外籍个人：企业需履行代扣代缴义务，外籍个人取得股息的实际税负将增加。

**标签**: `#tax policy`, `#China`, `#foreign individuals`, `#dividend income`, `#individual income tax`

---

<a id="item-finance-news-4"></a>
### [日本放宽加班上限：45 小时不再强制](https://www.orientaldaily.com.my/news/international/2026/09/01/844683) ⭐️ 8.0/10

日本 9 月 1 日起放宽加班规定，劳动标准监察机构不再强制企业遵守每月 45 小时加班上限，约 40%企业目前允许每月最多加班 100 小时。新规来自首相高市早苗政府 7 月通过的成长策略，批评者担忧“工作狂”文化回归。

telegram · zaihuapd · 9月1日 12:56

**「背景」** 2019 年日本实施工作方式改革相关法律，原则上规定每月加班上限为 45 小时、每年 360 小时，并设有罚则；厚生劳动省将每月加班超过 80 小时视为过劳死风险线。此次新规是首相高市早苗政府 7 月通过的成长策略的一部分，将 45 小时上限改为非强制。

**「影响」** 新规可能提高日本劳动者过劳风险；官员提醒，每月加班超过 45 小时会增加过劳死风险，工会批评此举背离缩短工时的改革。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Japanese_labour_law">Japanese labour law - Wikipedia</a></li>
<li><a href="https://mainichi.jp/english/articles/20251022/p2a/00m/0na/005000c">Japan&#x27;s new PM looks to lift upper limits on overtime hours - The Mainichi</a></li>

</ul>
</details>

**标签**: `#Japan`, `#labor policy`, `#overtime regulation`, `#economy`, `#workplace rules`

---

<a id="item-finance-news-5"></a>
### [财报后：戴尔、GitLab 大涨，MongoDB 跌 12%](https://www.cnbc.com/2026/09/01/stocks-making-the-biggest-moves-after-hours-dell-mdb-gtlb-and-more.html) ⭐️ 7.0/10

多只科技股在盘后因最新财报而大幅波动：戴尔上调 2027 财年预测，股价涨近 9%；GitLab 因盈利和全年指引超预期涨近 20%；MongoDB 虽然第二季度每股收益 1.90 美元和营收 7.72 亿美元均高于分析师预期，仍跌 12%。

rss · CNBC Finance · 9月1日 20:52

**「背景」** 这些公司在美国股市盘后公布季度业绩，投资者将其与分析师预测（如 LSEG 汇总的数据）比较，业绩和指引的好坏会立即反映在股价上。

**标签**: `#Earnings`, `#After-hours movers`, `#Dell Technologies`, `#MongoDB`, `#GitLab`

---

<a id="item-finance-news-6"></a>
### [高通宣布 2026 年 9 月 1 日后出货芯片涨价两位数](https://www.macrumors.com/2026/08/31/qualcomm-chip-price-increase/) ⭐️ 7.0/10

高通将对 2026 年 9 月 1 日后出货的全系列芯片涨价，涨幅达两位数，具体比例将与客户逐一协商。CEO Cristiano Amon 表示，公司无法继续自行承担不断上升的供应商成本；苹果仍为 iPhone 17 系列采购高通调制解调器芯片。

telegram · zaihuapd · 9月1日 04:10

**「背景」** 高通在 2026 年 7 月已预先通知客户，将从 9 月 1 日起对出货芯片提价。此次涨价涉及全系列芯片，幅度为两位数百分比，具体涨幅将与客户逐一协商。高通 CEO Cristiano Amon 称，公司无法继续自行承担不断上升的供应商成本。

**「影响」** 芯片涨价已开始推高 Android 手机售价，厂商要么提价要么削减配置；苹果 6 月已上调 Mac 和 iPad 价格，未来新款 iPhone 也可能更贵。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.macrumors.com/2026/08/31/qualcomm-chip-price-increase/">Qualcomm Raising Chip Prices Starting Tomorrow - MacRumors</a></li>
<li><a href="https://www.techtimes.com/articles/326200/20260901/android-phone-prices-begin-climbing-today-qualcomm-snapdragon-hike-takes-effect.htm">Android Phone Prices Begin Climbing Today as Qualcomm ...</a></li>
<li><a href="https://www.aroged.com/2026/09/01/qualcomm-chip-double-digit-price-increase-smartphone-industry-begins-price-increase-today/">Qualcomm chip double-digit price increase : Smartphone ... - Aroged</a></li>
<li><a href="https://www.macrumors.com/roundup/iphone-18/">iPhone 18: Rumors and Release Date</a></li>

</ul>
</details>

**标签**: `#Qualcomm`, `#chip pricing`, `#supply chain`, `#Apple`, `#semiconductors`

---

<a id="item-finance-news-7"></a>
### [《微短剧发展管理办法》今起施行](https://content-static.cctvnews.cctv.com/snow-book/index.html?item_id=13099489542770738243) ⭐️ 7.0/10

国家广播电视总局公布的《微短剧发展管理办法》今天正式施行。办法按投资额度和题材属性将微短剧分为三类并设置不同备案审核要求，同时规定使用人工智能生成、制作的微短剧须在每集明显位置添加提示标识。

telegram · zaihuapd · 9月1日 05:19

**「背景」** 这是我国首部针对微短剧领域的专项部门规章，法律效力层级高于此前行业指引类规范性文件。

**标签**: `#regulation`, `#China`, `#media`, `#micro-drama`, `#AI content`

---

<a id="item-finance-news-8"></a>
### [三部门发布汽车行业境外竞争与合规指引](https://weibo.com/1664176597/Rg5PKzXXE) ⭐️ 7.0/10

商务部、工业和信息化部、市场监管总局联合发布《汽车行业境外竞争行为与合规建设指引》，要求中国车企在海外市场依法制定价格、不得低价倾销，并加强与当地产业链合作。

telegram · zaihuapd · 9月1日 08:15

**「背景」** 商务部、工业和信息化部、市场监管总局于 9 月 1 日印发《汽车行业境外竞争行为与合规建设指引》，写明供工作中参考，属于引导性文件而非强制性法规，目的是推动汽车行业健康有序国际化发展、深化产业链供应链国际合作。

**「影响」** 对计划或已在海外经营的中国汽车企业，该指引意味着更明确的定价合规与本地化经营要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.stcn.com/article/detail/4167297.html">三部门发布《汽车行业境外竞争行为与合规建设指引》</a></li>

</ul>
</details>

**标签**: `#汽车行业`, `#境外竞争`, `#合规指引`, `#中国政策`, `#企业出海`

---