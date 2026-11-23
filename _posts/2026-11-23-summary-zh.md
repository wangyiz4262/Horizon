---
layout: default
title: "Horizon Summary: 2026-11-23 (ZH)"
date: 2026-11-23
lang: zh
---

> 从 20 条内容中筛选出 9 条重要资讯。

---

**科技新闻**
1. [GLM-5.4 发布：采用首款循环 Transformer 架构解决推理内存瓶颈](#item-tech-news-1) ⭐️ 8.0/10
2. [使用大语言模型生成数百万行 Lean 证明代码引发讨论](#item-tech-news-2) ⭐️ 8.0/10
3. [模型困惑度与智能的显著关联引发讨论](#item-tech-news-3) ⭐️ 8.0/10
4. [Riemann 假设 Lean 形式化证明可视化树状图发布](#item-tech-news-4) ⭐️ 7.0/10
5. [XNU Linux：在 Linux 上运行完整的 macOS 图形用户空间](#item-tech-news-5) ⭐️ 7.0/10
6. [GL.iNet 发布安全公告披露云服务漏洞与未经授权的访问风险](#item-tech-news-6) ⭐️ 7.0/10
7. [UIUC 等机构首提智能体“记忆税”，复杂记忆架构表现或不及原始 RAG](#item-tech-news-7) ⭐️ 7.0/10

**科技博客**
1. [在模糊与不确定中探索的“盲目乱撞”策略](#item-tech-blog-1) ⭐️ 7.0/10
2. [Sean Goedecke 对 OpenAI 困惑度图表的解读笔记](#item-tech-blog-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [GLM-5.4 发布：采用首款循环 Transformer 架构解决推理内存瓶颈](https://z.ai/blog/glm-5.4) ⭐️ 8.0/10

GLM-5.4 引入了全新的“循环 Transformer”（Loop Transformer）架构，旨在解决大语言模型推理过程中的内存带宽瓶颈。该技术旨在优化从高带宽内存（HBM）向芯片搬运权重数据的传统流程，从而提升推理效率。官方将其定位为迈向广义编程的重要一步，但具体性能和实际部署效果仍有待验证。

hackernews · foohis · 11月23日 10:06 · [社区讨论](https://news.ycombinator.com/item?id=50609685)

**「背景」** 在此之前，Z.ai 的主力模型为 2026 年 8 月推出的 GLM-5.3，其上下文长度达到 100 万 token 并开放了权重。本次发布的 GLM-5.4 则作为 Coding 计划的升级版推出，在维持相同上下文长度的基础上引入了循环架构。

**「社区讨论」** 评论者对该技术的实际效用存在分歧。支持者解释称循环 Transformer 能够优化传统大模型每次生成 Token 时都需要搬运整层权重的内存带宽瓶颈；而怀疑者则认为这类模型的实际缺点明显（例如需要固定循环次数导致服务化变难），且其“ marathon thinking”式的长时间思考机制在处理简单任务时会显著增加完成时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://teamorouter.com/blogs/glm-5-4">GLM - 5 . 4 Released: Vision, Stronger Coding, and When the API Arrives</a></li>
<li><a href="https://www.orcarouter.ai/blog/glm-5-4-vs-glm-5-3">GLM - 5 . 4 vs GLM - 5 .3: What the Upgrade Actually Adds</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#machine learning`, `#computer systems`, `#transformers`, `#hardware`

---

<a id="item-tech-news-2"></a>
### [使用大语言模型生成数百万行 Lean 证明代码引发讨论](https://micjm.com/blog/yes-17m-lines-of-lean-is-a-lot/) ⭐️ 8.0/10

围绕使用自动化方法和大语言模型生成数百万行 Lean 形式化证明代码的现象，社区展开了对其可读性、机器验证以及未来数学发展影响的讨论。评论指出，如此庞大的生成代码规模几乎无法由人类进行逐行审查，且可能面临仅适合由其他 AI 读取和处理的问题。

hackernews · seizethecheese · 11月23日 05:00 · [社区讨论](https://news.ycombinator.com/item?id=50607668)

**「背景」** Lean 是一个常用于形式化数学证明的交互式定理证明器，其代码库通常规模较小；近期有公开的 Lean 证明档案库达到了约 1700 万行的规模并宣称用于证明特定数学猜想。

**「社区讨论」** 社区成员讨论了 AI 生成内容难以保持人类可读性的原因，并担忧超大规模、无人审查的证明代码可能带来的潜在风险。同时，有评论者分享了用于运行和验证这些 Lean 代码的独立项目及进展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://micjm.com/blog/yes-17m-lines-of-lean-is-a-lot/">Yes , 17 m lines of Lean is a lot | micjm</a></li>
<li><a href="https://www.youtube.com/watch?v=aDl7-MWFLVc">17 Million Lines Claim to Prove Riemann. We Ran Them. - YouTube</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#formal verification`, `#software engineering`, `#mathematics`

---

<a id="item-tech-news-3"></a>
### [模型困惑度与智能的显著关联引发讨论](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 8.0/10

一篇新分析探讨了语言模型困惑度与智能之间清晰且令人惊讶的关联趋势。微软等机构随后参与了基座模型困惑度的测量与公开，Mustafa Suleyman 的推文显示 MAI-2 Base 模型在共同保留评估集上的 log-perplexity 为 0.819。

hackernews · acossta · 11月22日 17:06 · [社区讨论](https://news.ycombinator.com/item?id=50601525)

**「背景」** 困惑度（perplexity）是衡量语言模型预测下一个词时所产生不确定性或惊讶程度的经典指标。在深度学习领域，模型通常通过交叉熵损失（cross-entropy loss）进行训练，而困惑度正是该损失值的指数形式，长期以来被用作评估自回归语言模型的基础方法。

**「社区讨论」** 评论者指出困惑度本质上衡量了模型预测下一个 token 时的惊喜程度，其最佳情况为 1。有用户对在广泛使用强化学习后交叉熵损失依然如此重要感到意外，并认为通过预测率捕获世界模型符合信息论逻辑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/perplexity-and-intelligence/">Perplexity and Intelligence - OpenAI</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#machine learning`, `#language models`, `#research`

---

<a id="item-tech-news-4"></a>
### [Riemann 假设 Lean 形式化证明可视化树状图发布](https://pengowray.github.io/riemann-zeta-proof-visualizer/) ⭐️ 7.0/10

开发者 pengowray 推出了 Riemann 假设在 Lean 定理证明器中形式化证明的可视化树状图探索工具。该工具通过图形化界面展示了庞大代码库的依赖结构与体量分布，帮助分析证明的内部组成与模块规模。

hackernews · pengowray · 11月23日 01:50 · [社区讨论](https://news.ycombinator.com/item?id=50606499)

**「背景」** Lean 是一个广泛用于数学定理形式化证明与验证的交互式定理证明器。大型数学命题的形式化项目通常包含数百万行代码以及复杂的模块间依赖关系。

**「社区讨论」** 评论者认为该可视化工具直观地表明了代码库庞大的主因是包含了大量早已证明的基础定理（例如代数模块占了较大比例），而非代码质量问题；还有人将其视觉效果比作 CPU 布局图，并讨论了通过更短证明来简化代码的可能性。

**标签**: `#formal verification`, `#mathematics`, `#lean`, `#visualization`

---

<a id="item-tech-news-5"></a>
### [XNU Linux：在 Linux 上运行完整的 macOS 图形用户空间](https://github.com/AFK-surf/xnulinux) ⭐️ 7.0/10

名为 XNU Linux 的开源项目旨在让用户在 Linux 系统上运行 macOS 的用户空间和图形用户界面元素。该项目引发了技术社区关于跨平台兼容性、系统调用接口以及硬件限制的讨论。

hackernews · mmastrac · 11月23日 03:49 · [社区讨论](https://news.ycombinator.com/item?id=50607261)

**「背景」** 长期以来，跨平台运行专有操作系统环境一直是系统工程领域的一个探索方向，类似于通过兼容层在 Linux 上运行 Windows 应用程序的技术。

**「社区讨论」** Hacker News 评论者指出，由于 macOS 缺乏稳定的系统调用接口且应用程序依赖动态链接库，这类项目面临着独特的挑战与硬件限制；也有人将其与 Wine 运行 Windows 图形界面的实践进行了对比。

**标签**: `#operating systems`, `#linux`, `#macos`, `#open source`, `#systems engineering`

---

<a id="item-tech-news-6"></a>
### [GL.iNet 发布安全公告披露云服务漏洞与未经授权的访问风险](https://www.gl-inet.com/en-us/blogs/blog/glinet-security-notice-2026-11-20) ⭐️ 7.0/10

GL.iNet 于 2026 年 11 月 20 日发布安全公告，披露了与其硬件设备云服务相关的漏洞及未经授权的访问问题。该公告旨在向用户通报相关风险，并提供排查和应对指导，引发了社区关于网络硬件云连接安全与厂商响应的广泛讨论。

hackernews · gregsadetsky · 11月22日 23:06 · [社区讨论](https://news.ycombinator.com/item?id=50604988)

**「背景」** GL.iNet 确认黑客利用其云远程管理服务中的漏洞，在客户的路由器和 KVM 设备上安装了自定义恶意软件，部分受影响的用户报告设备出现了后门和反向 Shell 以获取远程访问权限。

**「社区讨论」** 社区用户对 GL.iNet 清晰的沟通和指引给予了正面评价，但也有评论指出此类事件凸显了设备依赖云服务所带来的潜在风险，并建议直接禁用或移除网络设备的云端连接功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/hackers-exploit-glinet-cloud-flaw-to-infect-routers-kvm-devices/">Hackers exploit GL . iNet cloud flaw to infect routers, KVM devices</a></li>

</ul>
</details>

**标签**: `#network-security`, `#hardware`, `#vulnerabilities`, `#cloud-services`

---

<a id="item-tech-news-7"></a>
### [UIUC 等机构首提智能体“记忆税”，复杂记忆架构表现或不及原始 RAG](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&amp;mid=2652744575&amp;idx=3&amp;sn=30dd0cb196f30092f2c09b3c8552c0f5) ⭐️ 7.0/10

来自 UIUC 等机构的研究人员首次提出了 AI 智能体的“记忆税”概念，研究表明复杂的记忆架构在某些场景下的表现甚至不如基础的 RAG（检索增强生成）系统。这一发现揭示了当前智能体记忆机制中存在的性能损耗与开销问题，为开发者在设计和优化 AI 智能体系统时提供了新的评估视角。

rss · 新智元 · 11月22日 23:02

**「背景」** 检索增强生成（RAG）技术常用于向大模型外部提供知识支持。随着智能体技术的发展，研究人员开始为系统引入复杂的持久化记忆架构，试图超越传统的直接检索方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/papers/2610.34073">Paper page - Memory Tax : Dissecting the Net Value of Agent Memory</a></li>

</ul>
</details>

**标签**: `#Artificial Intelligence`, `#Machine Learning`, `#RAG`, `#AI Agents`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [在模糊与不确定中探索的“盲目乱撞”策略](https://seangoedecke.com/when-in-doubt-flail-about/) ⭐️ 7.0/10

rss · Sean Goedecke · 11月23日 00:00

**「背景」** 当面对缺乏明确指导或方向不明的复杂技术与组织局势时，许多人倾向于采取谨慎观望态度，但作者 Sean Goedecke 指出，这种传统做法往往效率低下。

**「方案」** 作者认为最有效的策略是“盲目乱撞”，即通过尝试大量不同方案、密切关注来自现实与专家的反馈、并无情地放弃失败点来快速获取认知。这种方法适用于三种典型场景：一是产品层面，在缺乏产品市场契合度时通过多方测试寻找真正具有粘性的创新种子；二是工程层面，在面对过于庞大复杂的系统时通过投机性改动来观察成效，而非试图彻底理清全局；三是组织层面，通过主动尝试自动化、接手任务或提出长远规划来打破团队间的沟通僵局。虽然这种从内部感受来看如同不断碰壁的盲目尝试会带来心理压力，但只要保持对反馈的高度敏感并及时止损，就能穿透迷雾。

**「启示」** 在面对高不确定性的难题时，承认并接受内心的混乱感，通过高频次的试错与敏锐的纠错来代替盲目等待，是突破技术与组织困境的高效路径。

**标签**: `#software engineering`, `#career advice`, `#problem solving`, `#product management`

---

<a id="item-tech-blog-2"></a>
### [Sean Goedecke 对 OpenAI 困惑度图表的解读笔记](https://seangoedecke.com/notes-on-openais-perplexity-reveal/) ⭐️ 7.0/10

rss · Sean Goedecke · 11月23日 00:00

**「背景」** 作者 Sean Goedecke 探讨了 OpenAI 最新发布的、展示其历代模型困惑度（perplexity）变化的图表，分析了这项前沿实验室罕见公开的内部训练指标数据。

**「方案」** 作者指出困惑度因依赖特定测试集而难以跨实验室直接对比，且它作为仅适用于预训练的指标，无法反映占总训练量相当比例的强化学习效果。图表显示多数模型拥有不同的预训练基础，o3 与 4.1 共享基础却表现悬殊，而 GPT-4.5 之后预训练进展一度停滞，但从 GPT-5.2 开始展现出明显的困惑度下降加速。这种技术路线的演进说明预训练基础仍在快速改进，驳斥了行业认为大厂已全面放弃预训练的常见观点。在对齐与安全性方面，虽然研究人员多年来一直在呼吁此类透明度，但若没有公开未发布模型的具体测试集或数据，外部实验室很难仅凭此设定有效的安全阈值。作者还提到，图表中的困惑度跳跃与模型实际体验之间存在一定偏差，例如 o3 和 GPT-5.3-Codex 带来的强烈体验跳跃并未完全在困惑度曲线上体现，这或许是因为强化学习在激发思维链及纠正谄媚等能力上发挥了关键作用。

**「启示」** OpenAI 公开的困惑度图表为了解前沿模型的内部训练轨迹提供了独特视角，表明预训练仍在快速推进，但它与强化学习的结合依然是决定模型实际能力的关键。

**标签**: `#Large Language Models`, `#Model Training`, `#OpenAI`, `#AI Research`, `#Evaluation`

---