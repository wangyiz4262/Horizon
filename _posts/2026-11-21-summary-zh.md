---
layout: default
title: "Horizon Summary: 2026-11-21 (ZH)"
date: 2026-11-21
lang: zh
---

> 从 18 条内容中筛选出 8 条重要资讯。

---

**科技新闻**
1. [Terence Tao 讨论无外力纳维-斯托克斯奇点与广义黎曼猜想的形式化验证进展](#item-tech-news-1) ⭐️ 10.0/10
2. [Levent Alpöge 发布广义黎曼猜想的 Lean 形式化证明](#item-tech-news-2) ⭐️ 10.0/10
3. [Inkling 2 Mini 发布：面向本地优化的开源循环 Transformer 模型](#item-tech-news-3) ⭐️ 8.0/10
4. [国产超算团队时隔五年再次斩获超算国际大奖](#item-tech-news-4) ⭐️ 8.0/10
5. [AI 与 Lean 定理证明器携手推动形式化验证自动化](#item-tech-news-5) ⭐️ 8.0/10
6. [语言模型权重自修改研究引发技术与安全讨论](#item-tech-news-6) ⭐️ 7.0/10
7. [谷歌新论文披露内部实现递归自我改进与高级记忆技术](#item-tech-news-7) ⭐️ 7.0/10

**科技博客**
1. [为什么输出缓存无法奏效](#item-tech-blog-1) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Terence Tao 讨论无外力纳维-斯托克斯奇点与广义黎曼猜想的形式化验证进展](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/) ⭐️ 10.0/10

数学家 Terence Tao 在其博客中讨论了关于无外力纳维-斯托克斯奇点和广义黎曼猜想的突破性形式化验证结果。社区讨论指出，相关证明已通过两个独立内核的验证，这表明其证明在技术上得到了严格检查。

hackernews · archon1410 · 11月20日 17:21 · [社区讨论](https://news.ycombinator.com/item?id=50578358)

**「背景」** 黎曼猜想预测了特定函数零点的位置，从而决定了素数的分布规律；而广义黎曼猜想则对一整类相关函数作出了相同的预测。

**「社区讨论」** 社区成员对这些复杂数学进展结合形式化验证工具（如 Lean）的应用表达了混合着兴奋与不安的情绪，并探讨了如何确保庞大的形式化代码库确实证明了所预期的数学命题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vibeleaderboard.ai/intel/41749517-b4de-426d-8cd7-943f3706ffed">Unforced Navier-Stokes Singularity and the… | VibeLeaderboard</a></li>

</ul>
</details>

**标签**: `#mathematics`, `#formal verification`, `#navier-stokes`, `#riemann hypothesis`, `#research`

---

<a id="item-tech-news-2"></a>
### [Levent Alpöge 发布广义黎曼猜想的 Lean 形式化证明](https://alpo.ge/remark.pdf) ⭐️ 10.0/10

数学家 Levent Alpöge 发布了一份长达约 1500 万行代码、体积达 1.3GB 的 Lean 形式化证明，宣称证明了广义黎曼猜想。该工作目前已通过相关链接提供下载，等待数学界的进一步同行评议与验证。

hackernews · iamronaldo · 11月20日 14:16 · [社区讨论](https://news.ycombinator.com/item?id=50574968)

**「背景」** 黎曼猜想是数学中最著名的未解难题之一，几个世纪以来吸引了无数数学家探索其奥秘。Levent Alpöge 是一位从事数论和算术统计研究的数学家，此前曾加入人工智能公司 Anthropic 担任技术人员。辅助数学定理机器验证的 Lean 形式化定理证明器近年来在数学界受到了越来越多的关注。

**「社区讨论」** 评论者讨论了该证明惊人的体量（分 14 部分压缩包、约 1500 万行代码），并翻出了 Alpöge 在 2014 年本科毕业时曾将解决黎曼猜想设为人生目标的采访记录。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Levent_Alp%C3%B6ge">Levent Alpöge - Wikipedia</a></li>
<li><a href="https://www.nacionale.com/en/articles/has-riemann-hypothesis-been-proved-levent-alpoge-claude-anthropic-claim-lean">Riemann hypothesis proof claimed with Claude, unverified</a></li>

</ul>
</details>

**标签**: `#mathematics`, `#formal verification`, `#lean`, `#number theory`

---

<a id="item-tech-news-3"></a>
### [Inkling 2 Mini 发布：面向本地优化的开源循环 Transformer 模型](https://thinkingmachines.ai/news/inkling-2-mini/) ⭐️ 8.0/10

Thinking Machines 推出了 Inkling 2 Mini，这是一款专为本地运行优化的开源权重循环 Transformer 模型。该模型采用端到端 nvfp4 训练，在保持较小体积的同时，旨在达到与更大模型相匹敌的性能。

hackernews · jasondavies · 11月20日 20:12 · [社区讨论](https://news.ycombinator.com/item?id=50581260)

**「背景」** 循环 Transformer（Looped Transformer）是一种通过在网络中重复使用层来增加有效计算深度而不按比例增加显式参数或可见推理 token 的模型架构。Thinking Machines Lab 此前发布过标准模型，而 Inkling 2 Mini 是其首次引入循环架构的开源权重模型。

**「影响」** 本地用户和开发者能够在消费级硬件上高效运行该模型，社区成员报告在部分硬件上配合特定补丁可实现显著的解码速度提升，但也指出在部分复杂任务中仍存在表现不稳定的情况。

**「社区讨论」** Hacker News 评论区对该模型的循环架构与端到端 nvfp4 训练表现出高度关注。多位用户分享了本地测试结果，其中有人称赞其编码能力与运行速度，但也有人指出其在特定复杂提示词下会出现无限循环或幻觉输出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/thinkingmachines/Inkling-2-Mini">thinkingmachines/ Inkling - 2 - Mini · Hugging Face</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#machine learning`, `#open source`, `#hardware`

---

<a id="item-tech-news-4"></a>
### [国产超算团队时隔五年再次斩获超算国际大奖](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&amp;mid=2652744315&amp;idx=1&amp;sn=d46f87fe5c3d67fafd150d6db59c8bad) ⭐️ 8.0/10

中国国产超算团队在时隔五年后再次夺得国际超算领域的重大奖项。此次获奖标志着我国在高性能计算领域的研发与应用能力再次获得国际认可。

rss · 新智元 · 11月21日 03:52

**「背景」** 超算领域的国际奖项通常用于表彰在高性能计算架构、应用性能或系统设计上取得突破性进展的团队或个人。

**标签**: `#supercomputing`, `#high-performance computing`, `#technology industry`, `#hardware`

---

<a id="item-tech-news-5"></a>
### [AI 与 Lean 定理证明器携手推动形式化验证自动化](https://latent.space/p/formal-verification/) ⭐️ 8.0/10

人工智能与 Lean 定理证明器正在共同降低形式化验证的门槛，帮助自动化原本需要专业人员才能完成的代码数学正确性证明。这项发展将形式化验证从传统的繁琐人工过程推向更高效的自动化方向，为软件工程领域的可靠性保证提供了新途径。

rss · Latent Space · 11月20日 21:18

**「背景」** 形式化验证长期以来一直依靠数学方法来证明软件的正确性，但由于需要高度专业化的劳动而难以在业界广泛普及。Lean 作为一种现代定理证明器，为机器辅助的数学推理提供了基础环境。

**标签**: `#formal verification`, `#artificial intelligence`, `#software engineering`, `#Lean`

---

<a id="item-tech-news-6"></a>
### [语言模型权重自修改研究引发技术与安全讨论](https://arxiv.org/abs/2611.21885) ⭐️ 7.0/10

一项关于“语言模型能够通过自身推理重写自身权重”的研究在学术界与技术社区引发关注。研究探讨了模型在无需传统梯度下降训练的情况下修改自身权重的可能性。

hackernews · lwhsiao · 11月20日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=50577265)

**「背景」** 大语言模型的自我优化与离线调整一直是人工智能领域探索的方向，此前相关研究主要集中在通过外部反馈、强化学习或特定框架（如睡眠阶段的权重更新）来调整模型行为。

**「社区讨论」** 评论指出，该研究中模型实际的自我提升局限于缩短推理轨迹以避免达到 Token 上限，类似于其他权重空间编程实验。部分评论员还表达了对模型自主移除安全对齐机制等 AI 安全隐患的担忧。

**标签**: `#artificial intelligence`, `#machine learning`, `#language models`, `#ai safety`, `#research`

---

<a id="item-tech-news-7"></a>
### [谷歌新论文披露内部实现递归自我改进与高级记忆技术](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&amp;mid=2652744315&amp;idx=2&amp;sn=acf4991da5cf22769949784e84cb0518) ⭐️ 7.0/10

谷歌发布的一项新研究论文显示，其内部已实现递归自我改进（RSI），并为 Gemini 模型引入了先进的记忆技术。该研究借鉴了 Claude Opus 的相关经验，旨在增强人工智能系统的持续进化与记忆能力。目前该进展主要体现于研究论文与内部实现阶段。

rss · 新智元 · 11月21日 03:52

**「背景」** 递归自我改进是人工智能领域探索的方向之一，旨在让大语言模型能够利用自身生成的输出和经验来不断优化后续版本，而长效记忆机制则是解决大模型上下文遗忘和连续推理的重要技术手段。

**「影响」** 这项技术若全面落地，将大幅提升 Gemini 等大语言模型的长期任务处理能力与自主进化效率。

**标签**: `#artificial intelligence`, `#machine learning`, `#google`, `#ai research`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [为什么输出缓存无法奏效](https://seangoedecke.com/why-output-caching-doesnt-work/) ⭐️ 7.0/10

rss · Sean Goedecke · 11月21日 00:00

**「背景」** 大语言模型的推理经济主要依赖于输入缓存来避免重复计算，但作者肖恩·戈德克（Sean Goedecke）指出，试图通过缓存输出来减少冗余文本的思路在实践中并不可行。

**「方案」** 作者分析认为，尽管智能体在生成 PR、引用证据文档或重复代码片段时会产生大量显而易见的重复文本，且输出 Token 的生成成本远高于输入 Token，但输出缓存却无法带来实质性的成本节约。根据作者的观察，可见的输出仅占模型总输出 Token 的大约 6%，而其余的 94%则由 50%的推理 Token 和 44%的工具调用组成。因此，受阿姆达尔定律（Amdahl&\#x27;s law）的制约，即便能够将可见输出的 Token 削减三分之二，也只能节省总输出 Token 的 4%左右。为了真正节省输出 Token，关键在于减少不可见的推理和工具调用，而这主要取决于模型本身的智能水平；更聪明的模型虽然单价更高，但能以更少的总 Token 数解决问题，从而实现总体成本的降低。

**「启示」** 作者得出结论，优化可见输出的重复毫无意义，因为推理和工具调用占据了绝大部分输出 Token 开销。降低 LLM 推理成本的根本出路在于提升模型和系统的整体智能，而非依赖输出缓存。

**标签**: `#llm-inference`, `#cost-optimization`, `#token-economics`, `#ai-agents`

---