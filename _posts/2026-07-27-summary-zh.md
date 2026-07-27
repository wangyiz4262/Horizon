---
layout: default
title: "Horizon Summary: 2026-07-27 (ZH)"
date: 2026-07-27
lang: zh
---

> 从 32 条内容中筛选出 21 条重要资讯。

---

1. [vLLM v0.26.0 新增 Inkling 支持并优化 DeepSeek-V4](#item-1) ⭐️ 9.0/10
2. [Anthropic 阐明对开源 AI 模型及强制安全测试的立场](#item-2) ⭐️ 9.0/10
3. [3 万亿参数 Kimi-K3 模型在 HuggingFace 发布](#item-3) ⭐️ 9.0/10
4. [阿里推出“千问办公”AI 平台，可生成文档并操控电脑](#item-4) ⭐️ 9.0/10
5. [Fastjson2 远程代码执行漏洞披露，尚无官方修复](#item-5) ⭐️ 9.0/10
6. [中方驳斥美方拟制裁中国 AI 企业，强调模型蒸馏是行业普遍做法](#item-6) ⭐️ 9.0/10
7. [中国开始量产国产 DUV 光刻机](#item-7) ⭐️ 9.0/10
8. [法官驳回谷歌阻止 SerpAPI 抓取其搜索结果的 DMCA 主张](#item-8) ⭐️ 8.0/10
9. [Misago 项目用 Htmx 替代 React.js 实现 UI 交互](#item-9) ⭐️ 8.0/10
10. [Paged Out #9 发布：深度技术与黑客探索数字杂志](#item-10) ⭐️ 8.0/10
11. [微软在 MDASH 平台推出 MAI-Cyber-1-Flash 网络安全 AI 模型](#item-11) ⭐️ 8.0/10
12. [Libsm64：将马力欧 64 角色物理引擎封装为可复用库](#item-12) ⭐️ 8.0/10
13. [Bun 的 Rust 重写进展顺利，v1.4 因 Node.js 兼容性而推迟](#item-13) ⭐️ 8.0/10
14. [AI 行业从聊天机器人转向代理系统，Mollick 指南更新](#item-14) ⭐️ 8.0/10
15. [纯 PyTorch 从零构建 Transformer 实现英泰机器翻译](#item-15) ⭐️ 8.0/10
16. [新评估揭示前沿大型语言模型普遍存在左倾偏见](#item-16) ⭐️ 8.0/10
17. [提议在 MLOps 中为训练数据质量设置“通过/不通过”门禁](#item-17) ⭐️ 8.0/10
18. [小米澎程将于 7 月 30 日发布昆仑架构及新款 SUV](#item-18) ⭐️ 8.0/10
19. [长鑫科技科创板首秀创纪录，股价飙升](#item-19) ⭐️ 8.0/10
20. [华为被指筹建 DRAM 工厂以保障 AI 芯片供应](#item-20) ⭐️ 8.0/10
21. [谷歌透露 Gemini 4 为迄今最雄心预训练，预计年底发布](#item-21) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.26.0 新增 Inkling 支持并优化 DeepSeek-V4](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 9.0/10

vLLM v0.26.0 版本全面支持新的 Inkling 模型家族，在多种硬件平台上为 DeepSeek-V4 模型带来了显著的性能优化，并通过支持 fp32 `lm_head` 提升了生成准确性。此版本还包括 KV 卸载、灵活的注意力后端以及 Rust 前端方面的重大改进。 这些更新对大型语言模型（LLM）推理生态系统至关重要，因为它们扩展了模型兼容性，显著提高了 DeepSeek-V4 等流行模型的效率，并确保了模型输出的更高准确性。这直接通过实现更快、更可靠、更具成本效益的大模型部署，使开发者和用户受益。 Inkling 模型家族现在拥有完整的支持堆栈，包括分段 CUDA 图支持、Hopper FA4 相对注意力以及 NVFP4 量化。DeepSeek-V4 的优化包括专用路由内核和 `fused_topk_bias`，可实现 1.5-2 倍的内核加速，同时还有针对 ROCm 和 XPU 的特定增强功能。

github · khluu · 7月27日 01:06

**背景**: Inkling 模型家族是 Thinking Machines Lab 最近发布的一个专家混合（MoE）Transformer 模型，拥有 9750 亿总参数，支持高达 100 万个 token 的上下文窗口，并经过 45 万亿 token 的文本、图像、音频和视频数据预训练。分段 CUDA 图（Piecewise CUDA Graph, PCG）是一种将模型计算图分解成更小片段的技术，将每个片段捕获为独立的 CUDA 图，以消除动态形状的内核启动开销。Hopper FA4 相对注意力指的是专门为 NVIDIA Hopper 架构 GPU 设计的注意力机制优化，它基于 FlashAttention 3 (FA3) 等进步，显著提高了大型语言模型的速度和内存效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>
<li><a href="https://docs.sglang.io/advanced_features/piecewise_cuda_graph.html">Piecewise CUDA Graph - SGLang Documentation</a></li>
<li><a href="https://www.digitalocean.com/community/tutorials/flashattention-4-llm-inference-optimization">FlashAttention 4: Faster, Memory-Efficient Attention for... | DigitalOcean</a></li>

</ul>
</details>

**标签**: `#LLM Inference`, `#vLLM`, `#Machine Learning`, `#Performance Optimization`, `#GPU Computing`

---

<a id="item-2"></a>
## [Anthropic 阐明对开源 AI 模型及强制安全测试的立场](https://www.anthropic.com/news/position-open-weights-models) ⭐️ 9.0/10

Anthropic 发布声明，阐明其对开源 AI 模型的立场，主张所有足够强大的模型，无论是开源还是闭源，都应进行强制性安全测试，同时否认支持彻底禁止开源模型。 这一声明意义重大，因为它来自一家领先的 AI 实验室，将影响当前关于 AI 安全、监管以及开源 AI 未来发展的持续辩论。它可能塑造政策讨论和 AI 模型的运营格局。 Anthropic 的声明强调他们不主张禁止开源模型，而是支持对所有足够强大的模型（无论是开源还是闭源）进行强制性安全测试。然而，社区质疑此类测试的实际影响，特别是其成本、管理以及通过严格要求或拒绝认证而可能造成的实际禁令。

hackernews · surprisetalk · 7月27日 22:03 · [社区讨论](https://news.ycombinator.com/item?id=49076057)

**背景**: 开源 AI 模型是指其核心组件，特别是经过训练的权重和偏差，被公开发布的人工智能模型，允许任何人下载、检查、修改并在自己的基础设施上运行。这种方法与闭源模型形成对比，闭源模型的这些组件是专有的，并且通常与软件开发中的开源运动相关联。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://www.microsoft.com/en-us/corporate-responsibility/topics/open-weight/">Open Weights and American AI Leadership</a></li>

</ul>
</details>

**社区讨论**: 社区表达了强烈的怀疑态度，认为 Anthropic 呼吁强制性安全测试可能构成对开源模型的实际禁令，并对测试成本、管理以及拒绝认证的可能性表示担忧。许多人还指出，否认支持禁令与倡导打击模型蒸馏或限制芯片销售等措施之间存在明显的矛盾。

**标签**: `#AI Policy`, `#Open-source AI`, `#AI Safety`, `#AI Regulation`, `#Large Language Models`

---

<a id="item-3"></a>
## [3 万亿参数 Kimi-K3 模型在 HuggingFace 发布](https://huggingface.co/moonshotai/Kimi-K3) ⭐️ 9.0/10

3 万亿参数的 Kimi-K3 语言模型已在 HuggingFace 上发布，并附带了技术报告。此次发布使得如此规模的模型变得可访问，引发了广泛的社区讨论。 此次发布意义重大，因为它使一个前沿的 3 万亿参数模型公开可用，可能为初创公司和研究人员普及先进的 AI 能力。这可能会推动定制 AI 应用的创新，并为模型部署和成本效益设定新的基准。 Kimi-K3 模型，具体而言是一个 2.8 万亿参数模型，具有 100 万 token 的上下文窗口和原生视觉能力，以 mxfp4 格式托管大约需要 1.5TB 的显存。该许可证还包含一项针对年收入超过 2000 万美元的模型即服务业务的收入条款，并且用户观察到它最初将自己描述为“Claude，一个由 Anthropic 创建的 AI 助手”。

hackernews · nateb2022 · 7月27日 06:18 · [社区讨论](https://news.ycombinator.com/item?id=49065752)

**背景**: 在大型语言模型（LLM）中，“参数”指的是模型在训练过程中学习到的内部变量或权重，它们本质上定义了模型的知识和能力。参数数量越多，通常意味着模型越复杂，潜力也越大。HuggingFace 是一个流行的平台，提供机器学习工具、数据集和预训练模型，促进 AI 模型的共享和部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openlm.ai/kimi-k3/">Kimi K3 - openlm.ai</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/what-are-llm-parameters/">LLM Parameters - GeeksforGeeks</a></li>

</ul>
</details>

**社区讨论**: 社区正在积极讨论托管如此大型模型的高昂成本，估计需要大约 1.5TB 的显存，以及初创公司进行定制和实现 IP 主权的巨大潜力。此外，人们还关注缺乏合适的专业消费级硬件，以及一个有趣的发现：该模型最初将自己识别为“Claude”。

**标签**: `#Large Language Models`, `#AI/ML`, `#HuggingFace`, `#Model Deployment`, `#Deep Learning`

---

<a id="item-4"></a>
## [阿里推出“千问办公”AI 平台，可生成文档并操控电脑](https://qwenwork.cn/) ⭐️ 9.0/10

阿里巴巴推出了“千问办公”AI 平台测试版，覆盖网页、Windows 和 macOS 客户端，并接入钉钉，用户可通过自然语言生成和编辑文档、表格、PPT、网页、代码及多媒体内容。其桌面端还具备跨应用控制和浏览器自动化功能，能够执行点击、输入、数据提取等操作。 此次发布标志着 AI 驱动生产力迈出了重要一步，提供了一套全面的解决方案，有望改变个人和企业与办公软件的交互方式并自动化复杂任务。跨应用控制和浏览器自动化功能的整合，使“千问办公”在 AI 代理和办公自动化市场中具有潜在的颠覆性。 桌面客户端支持 macOS 14 以上系统及 64 位 Windows 10 以上系统，官网部分功能目前仍标注“敬请期待”。阿里巴巴提醒，电脑操控功能可能会截取屏幕内容或执行不可撤销的操作，默认会在操作前征求用户确认。

telegram · zaihuapd · 7月27日 05:45

**背景**: AI 电脑操控功能指的是 AI 系统能够通过与人类相同的界面与软件和操作系统进行交互，通过“查看”屏幕并解释用户指令来执行点击或输入等操作。AI 代理的跨应用控制是指 AI 代理能够在多个不同的软件应用程序之间操作和协调行动，从而实现更复杂的工作流程。AI 浏览器自动化则涉及 AI 系统控制网页浏览器执行导航网站、提取数据和与网页元素交互等任务，将 AI 的能力扩展到广泛的基于网络的服。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sidecar.ai/blog/how-ai-learned-to-use-your-computer-and-why-that-changes-everything">How AI Learned to Use Your Computer (And Why That Changes Everything)</a></li>
<li><a href="https://n8n.io/ai-agents/">Build Custom AI Agents With Logic & Control | n8n Automation Platform</a></li>
<li><a href="https://axiom.ai/">browser automation for humans and AI | axiom. ai</a></li>

</ul>
</details>

**标签**: `#AI Productivity`, `#Office Automation`, `#Generative AI`, `#Agentic AI`, `#Alibaba`

---

<a id="item-5"></a>
## [Fastjson2 远程代码执行漏洞披露，尚无官方修复](https://mp.weixin.qq.com/s/LJaul1jNjK9pXRAkoUiMEA) ⭐️ 9.0/10

长亭科技于 7 月 27 日披露了 Fastjson2 的一个远程代码执行（RCE）漏洞，攻击者可通过恶意 JSON 数据绕过 AutoType 类型校验并执行代码，影响所有当前版本，包括 2.0.62 及以前版本。项目维护者已确认此安全问题，但目前尚未发布官方补丁，建议用户暂时禁用 AutoType 进行缓解。 这是 Fastjson2 中一个关键的远程代码执行漏洞，Fastjson2 是一个广泛使用的 Java JSON 库，对处理不可信 JSON 数据的应用程序构成重大风险。由于所有当前版本都缺乏官方补丁，开发者需要立即采取缓解措施以防止潜在的系统入侵。 该漏洞允许攻击者通过精心构造的 JSON 数据绕过 AutoType 机制实现代码执行，影响所有 Fastjson2 版本，包括 2.0.62 及以前版本。尽管问题已确认，但完整的漏洞细节和永久补丁尚未公开，且相关的拉取请求（#7695）已被关闭且未合并。

telegram · zaihuapd · 7月27日 10:31

**背景**: Fastjson2 是阿里巴巴开发的一个高性能 Java JSON 库，广泛用于将 Java 对象序列化为 JSON 格式，以及将 JSON 反序列化回 Java 对象。AutoType 特性最初旨在简化反序列化过程中复杂对象类型的恢复，但历史上一直是反序列化漏洞的来源，若未正确保护，可能导致恶意代码执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jxausea.medium.com/spring-boot-integrated-fastjson2-quick-start-demo-d3c359a3f33b">Spring Boot integrated fastjson2 quick start demo | by HBLOG | Medium</a></li>
<li><a href="https://medium.com/@pa2sw0rd/deep-dive-into-fastjson-deserialization-vulnerabilities-from-principles-to-practical-defense-c3be134ec8a6">Deep Dive into Fastjson Deserialization Vulnerabilities ... | Medium</a></li>

</ul>
</details>

**标签**: `#Software Security`, `#Vulnerability`, `#Java`, `#Fastjson2`, `#RCE`

---

<a id="item-6"></a>
## [中方驳斥美方拟制裁中国 AI 企业，强调模型蒸馏是行业普遍做法](https://www.mofcom.gov.cn/syxwfb/art/2026/art_7f1622463a7c48ef9fad600ce0ef702f.html) ⭐️ 9.0/10

商务部于 7 月 27 日正式驳斥美方关于中国 AI 企业“蒸馏”美国模型并窃取知识产权的指控，声明这些指控缺乏事实和法律依据。中方强调模型蒸馏是行业广泛使用的技术，美国企业也在使用中国模型，并警告美方不要实施制裁。 这一官方声明加剧了中美之间持续的科技竞争，预示着美国可能对 AI 领域实施新的制裁，并可能扰乱全球 AI 研究与合作。它凸显了地缘政治紧张局势对全球先进 AI 技术开发和可及性的影响。 中国商务部明确指出，“模型蒸馏”是行业广泛使用的技术，并非窃取知识产权，并提到近 200 家美国初创企业已呼吁政府不要限制访问中国开源模型。商务部还警告称，如果中方利益受到实质性损害，将采取必要措施进行反制。

telegram · zaihuapd · 7月27日 11:01

**背景**: 模型蒸馏，或称知识蒸馏，是一种机器学习技术，它将来自更大、更复杂的“教师”模型的知识转移到一个更小、更高效的“学生”模型中。这个过程使较小的模型能够在特定任务上达到与较大模型相当的性能，通常以更低的计算成本，是 AI 开发中优化模型部署的常见做法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://openai.com/index/api-model-distillation/">Model Distillation in the API - OpenAI</a></li>

</ul>
</details>

**标签**: `#AI Policy`, `#Geopolitics`, `#US-China Tech Rivalry`, `#AI Industry`, `#Sanctions`

---

<a id="item-7"></a>
## [中国开始量产国产 DUV 光刻机](https://www.theinformation.com/articles/china-starts-mass-producing-homegrown-duv-chipmaking-tools-advance-local-chip-industry) ⭐️ 9.0/10

中国已开始大规模生产自主研发的浸没式 DUV 光刻机，上海一家国企计划今年生产约 5 台，到 2027 年生产约 20 台，将交付给中芯国际和华虹半导体等国内芯片制造商。 这标志着中国在半导体自给自足方面迈出了重要一步，可能改变全球芯片供应链格局，并对 ASML 在中国市场的地位构成挑战，尤其是在西方进一步收紧出口管制的情况下。 尽管国产 DUV 光刻机主要使用国产零部件，但部分关键部件仍来自日本，且其性能和可靠性目前仍落后于 ASML，芯片制造商需要数月时间进行测试才能将其投入量产。

telegram · zaihuapd · 7月27日 14:10

**背景**: DUV（深紫外）光刻是半导体制造中的一项核心技术，它利用 DUV 光（通常来自准分子激光器）将电路图案投射到硅晶圆上，从而制造微芯片结构。浸没式光刻则通过在投影物镜和晶圆之间引入液体介质来进一步增强这一工艺，从而提高分辨率并允许印刷更精细的特征。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Photolithography">Photolithography - Wikipedia</a></li>
<li><a href="https://www.zeiss.com/semiconductor-manufacturing-technology/inspiring-technology/duv-lithography.html">DUV lithography for chip manufacturing | ZEISS SMT</a></li>
<li><a href="https://eureka.patsnap.com/article/immersion-lithography-why-water-boosts-resolution-in-193-nm-systems">Immersion Lithography : Why water boosts resolution in 193 nm...</a></li>

</ul>
</details>

**标签**: `#Semiconductor Manufacturing`, `#DUV Lithography`, `#China Tech`, `#Geopolitics`, `#Supply Chain`

---

<a id="item-8"></a>
## [法官驳回谷歌阻止 SerpAPI 抓取其搜索结果的 DMCA 主张](https://www.techdirt.com/2026/07/27/judge-rejects-googles-attempt-to-dmca-its-way-out-of-being-scraped/) ⭐️ 8.0/10

一名法官驳回了谷歌试图通过数字千年版权法案（DMCA）主张来阻止 SerpAPI 抓取其搜索结果的法律尝试，这标志着谷歌遭遇了一次重大的法律挫折。 这一裁决为数据访问和行业竞争树立了重要先例，可能使小型公司和研究人员能够利用公开数据，而无需面对科技巨头提出的广泛 DMCA 规避主张。 该裁决表明，仅仅抓取通常包含事实数据的公开搜索结果，不一定构成数字千年版权法案第 1201 条下对受版权保护作品的技术保护措施的规避。这与法律解释相符，即针对抓取者的 DMCA 主张需要与实际的版权侵权行为相关联才能成功。

hackernews · cdrnsf · 7月27日 18:15 · [社区讨论](https://news.ycombinator.com/item?id=49073513)

**背景**: 数字千年版权法案（DMCA）第 1201 条禁止规避控制受版权保护作品访问的技术措施。然而，法院通常要求规避行为与实际的版权侵权之间存在直接联系，尤其当抓取的数据由不受版权保护的事实组成时。SerpApi 是一个实时 API 服务，通过处理代理和验证码等技术挑战，提供来自谷歌等搜索引擎的结构化数据，从而简化了网络抓取。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mccarthylg.com/variations-in-legal-interpretations-of-the-dmca/">Variations in Legal Interpretations of the DMCA - McCarthy Law Group</a></li>
<li><a href="https://capstonedc.com/insights/why-dmca-claims-against-web-scrapers-face-long-odds/">Why DMCA Claims Against Web Scrapers Face Long Odds - Capstone DC</a></li>
<li><a href="https://serpapi.com/">SerpApi: Google Search API</a></li>

</ul>
</details>

**社区讨论**: 社区讨论主要批评谷歌对小型实体的霸凌行为，并指出由于谷歌停用了其官方搜索 API，抓取行为变得必要。评论者还讨论了美国和欧盟在数据库版权保护方面的细微差异，并强调了抓取对于识别广告诈骗的公共利益。

**标签**: `#Web Scraping`, `#Legal Tech`, `#Copyright Law`, `#Google`, `#Data Access`

---

<a id="item-9"></a>
## [Misago 项目用 Htmx 替代 React.js 实现 UI 交互](https://misago-project.org/t/removing-reactjs-from-the-codebase-and-adapting-htmx-for-ui-interactivity/1267/) ⭐️ 8.0/10

Misago 项目决定从其代码库中移除 React.js，并采用 Htmx 来实现用户界面交互，标志着其转向更简单的服务器渲染网络应用。这一改变旨在通过利用 Htmx 的超媒体驱动方法来简化前端开发。 这一举动凸显了网络开发中日益增长的趋势，即转向更简单、由超媒体驱动的架构，例如“HTML over the wire”，挑战了复杂客户端框架的主导地位，并可能为某些应用类型带来性能和开发简易性方面的优势。它可能会影响其他考虑类似架构转变的项目。 该项目决定用 Htmx 替代 React.js，旨在通过利用 Htmx 扩展 HTML 的自定义属性来实现 AJAX，从而简化 UI 交互，无需大量 JavaScript 即可实现动态更新。这种方法特别适合主要提供非交互式内容的应用程序，例如论坛软件。

hackernews · Ralfp · 7月27日 09:58 · [社区讨论](https://news.ycombinator.com/item?id=49067301)

**背景**: React.js 是一个流行的用于构建用户界面的 JavaScript 库，以其基于组件的架构和虚拟 DOM 而闻名，这使得高效的客户端渲染和复杂的单页应用（SPA）成为可能。Htmx 则是一个轻量级的 JavaScript 库，它通过属性扩展 HTML，允许直接进行 AJAX 请求和 DOM 操作，从而推广一种“HTML over the wire”架构，即服务器发送 HTML 片段进行更新。这种“HTML over the wire”方法通过动态更新页面部分而无需完全重新加载，将服务器端渲染的简单性与类似 SPA 的响应能力结合起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Htmx">Htmx</a></li>
<li><a href="https://htmx.org/">htmx - high power tools for html</a></li>
<li><a href="https://bountyplz.xyz/bugbounty/2023/07/30/HTML-Over-The-Wire.html">HTML Over the Wire | ~ryan</a></li>

</ul>
</details>

**社区讨论**: 社区讨论反映了复杂的情绪，一些用户赞扬 Htmx 的简单性及其对服务器渲染应用（特别是论坛软件）的适用性，以及它创建类似 PWA 体验的能力。然而，一位用户报告称，在处理可过滤产品列表等复杂交互元素时遇到了性能问题，因为发送大型 HTML 响应变得缓慢。另一位用户推荐 Pyview 作为服务器端渲染页面并进行 DOM 补丁的替代方案。

**标签**: `#Web Development`, `#Frontend Architecture`, `#HTMX`, `#React.js`, `#Web Frameworks`

---

<a id="item-10"></a>
## [Paged Out #9 发布：深度技术与黑客探索数字杂志](https://pagedout.institute/download/PagedOut_009.pdf) ⭐️ 8.0/10

深度技术和黑客探索数字杂志 Paged Out 发布了其最新一期 #9，其中包含多篇文章，深入探讨了子像素渲染和可计算平铺等主题。 此次发布对技术社区意义重大，因为 Paged Out 以其深入的内容而备受推崇，为复杂的计算机科学和系统工程主题提供了宝贵的见解，让人联想到历史上的黑客出版物。 本期杂志收录了关于子像素渲染的“子像素动物园”等文章，以及一篇关于可计算平铺的文章，有评论指出后者是对王浩在 1960 年代将多米诺骨牌问题与停机问题联系起来的研究的未注明出处的重新发现。

hackernews · laurensr · 7月27日 14:22 · [社区讨论](https://news.ycombinator.com/item?id=49070138)

**背景**: 子像素渲染是一种显示技术，尤其在 LCD 屏幕中，通过单独调整构成每个完整像素的红、绿、蓝子像素，来提高文本清晰度和感知分辨率。可计算平铺，也称为多米诺骨牌问题，涉及确定是否可以使用给定的一组有限瓦片类型来铺满无限平面，王浩曾著名地证明该问题等同于停机问题的不可判定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huaxianjing.com/what-is-subpixel-rendering-and-how-is-it-implemented-in-small-lcd-modules/">What is subpixel rendering and how is it implemented in small LCD...</a></li>
<li><a href="https://www.math.univ-toulouse.fr/~msablik/article/2012-JAC-Fernique-Sablik-weak_effective.pdf">Local Rules for Computable Planar Tilings</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-0-387-09680-3_13">Computability of Tilings | Springer Nature Link</a></li>

</ul>
</details>

**社区讨论**: 社区对 Paged Out #9 给予了高度评价，因其深度的技术内容和“黑客探索”的性质，将其与 2600 和 Phrack 等经典黑客杂志相提并论。其中，“子像素动物园”和关于可计算平铺的文章因其技术深度以及与既定计算机科学问题的有趣联系而受到特别关注。

**标签**: `#Computer Science`, `#Systems Engineering`, `#Graphics`, `#Low-level Programming`, `#Technical Publication`

---

<a id="item-11"></a>
## [微软在 MDASH 平台推出 MAI-Cyber-1-Flash 网络安全 AI 模型](https://microsoft.ai/news/introducing-mai-cyber-1-flash-inside-mdash/) ⭐️ 8.0/10

微软推出了 MAI-Cyber-1-Flash，这是一款专为网络安全设计的新型 AI 模型，并已集成到其 MDASH 平台中。该模型声称能以领先模型 50%的成本提供世界级的性能，并在 CyberGym 基准测试中取得了 96%的分数。 这一进展意义重大，因为它利用人工智能增强了应对日益复杂威胁的网络防御能力，可能使先进的安全解决方案对组织而言更易获得且更具成本效益。这也突显了微软在漏洞发现和修复方面对代理式 AI 系统的战略推进。 MAI-Cyber-1-Flash 是微软首个专用的网络安全 AI 模型，在 MDASH 内部运行，MDASH 被描述为用于大规模漏洞发现的多模型代理式扫描工具。该模型声称与竞争对手相比具有显著的性能和成本效益，并与 Perception 代理式安全系统一同首次亮相。

hackernews · migmartri · 7月27日 16:52 · [社区讨论](https://news.ycombinator.com/item?id=49072361)

**背景**: MDASH，即微软安全多模型代理式扫描工具，是一个由 AI 驱动的漏洞发现系统，旨在自动化跨各种环境的大规模代码审计。像 MDASH 这样的代理式 AI 系统利用多个 AI 代理协同工作，以实现复杂目标，例如大规模识别和修复安全漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://microsoft.ai/news/introducing-mai-cyber-1-flash-inside-mdash/">Introducing MAI-Cyber-1-Flash inside MDASH | Microsoft AI</a></li>
<li><a href="https://runtimewire.com/article/microsoft-mai-cyber-1-flash-mdash-launch">Microsoft launches MAI-Cyber-1-Flash, a cost‑efficient AI ...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论主要围绕微软在网络安全领域的数据优势展开，一些人质疑该模型是否主要有利于微软自身产品。同时，社区也对模型的可用性和可访问性表示担忧，并普遍对微软过去 AI 产品的一致性和命名规范持怀疑态度。

**标签**: `#AI`, `#Machine Learning`, `#Cybersecurity`, `#Microsoft`, `#Security`

---

<a id="item-12"></a>
## [Libsm64：将马力欧 64 角色物理引擎封装为可复用库](https://github.com/libsm64/libsm64) ⭐️ 8.0/10

Libsm64 是一个新库，它提取了《超级马力欧 64》的角色物理和动画，允许开发者将这些标志性机制集成到外部游戏引擎中。该项目为模组制作和创造新的游戏体验开辟了独特的可能性。 这项发展意义重大，因为它使经典游戏的核心机制得以普及，为模组制作者和开发者提供了前所未有的创作自由，无需从头开始即可构建新体验。它通过允许跨游戏集成和在全新环境中重新构想深受喜爱的角色来促进创新。 Libsm64 专注于将原版 N64 游戏中马力欧的移动、碰撞检测和动画逻辑封装成一个可移植的库。这种设计使其与特定引擎无关，允许其在各种游戏引擎和自定义环境中使用，超越了原始游戏。

hackernews · klaussilveira · 7月27日 10:04 · [社区讨论](https://news.ycombinator.com/item?id=49067352)

**背景**: 游戏开发中的逆向工程涉及分析现有软件以了解其内部工作原理，通常是为了创建模组、确保兼容性或学习专有系统。像 Libsm64 这样的项目利用逆向工程技术来提取特定的游戏组件，例如角色物理和动画，以便在新环境中复用，从而延长了经典游戏的生命周期和创作潜力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/yeauxdejuan/reverse-engineering-in-the-gaming-industry-k7o">Reverse engineering in the gaming industry - DEV Community</a></li>
<li><a href="https://github.com/kovidomi/game-reversing">GitHub - kovidomi/game-reversing: Beginner learning materials ... How Do Gamers Reverse-Engineer Games? - thegamersmag.com Beginners Guide to Reverse Engineering (Retro Games) GitHub - dsasmblr/game-hacking: Tutorials, tools, and more as ... The Role of Static Reverse Engineering in Game Cheating</a></li>

</ul>
</details>

**社区讨论**: 社区对 Libsm64 表达了强烈热情，称其“不可思议”，并通过马力欧出现在《半条命 2》等例子突出了其潜力。评论者还将其与“元宇宙”和可互换游戏资产的承诺进行比较，指出 Libsm64 在没有相关炒作或依赖区块链技术的情况下实现了这一点。

**标签**: `#Game Development`, `#Reverse Engineering`, `#Libraries`, `#Modding`, `#Software Engineering`

---

<a id="item-13"></a>
## [Bun 的 Rust 重写进展顺利，v1.4 因 Node.js 兼容性而推迟](https://lockwood.dev/ai/2026/07/27/how-is-the-bun-rewrite-in-rust-going.html) ⭐️ 8.0/10

Bun 的创建者 Jarred Sumner 证实，Rust 重写进展顺利，并已在一个多月前在 Claude Code 中发布。然而，Bun v1.4 版本因未能达到特定数量的 Node.js 兼容性测试要求而被推迟发布，预计将于下周二发布。 此次更新意义重大，因为 Rust 重写旨在提升 Bun 的性能和稳定性，而对 Node.js 兼容性的承诺对于其在更广泛的 JavaScript 生态系统中作为无缝替代品的普及至关重要。 Bun v1.4 的延迟具体是因为尚未达到承诺的新增通过的 Node.js 测试数量，尽管相关的拉取请求已准备好但尚未合并。值得注意的是，Rust 重写已在 AI 辅助软件开发工具 Claude Code 中投入生产使用。

hackernews · tomlockwood · 7月27日 11:12 · [社区讨论](https://news.ycombinator.com/item?id=49067854)

**背景**: Bun 是一个快速、一体化的 JavaScript 运行时、包管理器和测试运行器，旨在作为 Node.js 的替代品，它使用 Safari 的 JavaScriptCore 引擎。Claude Code 是 Anthropic 开发的一款代理式编码工具，旨在帮助开发者理解代码库、编辑文件和运行命令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://bun.sh/">Bun — A fast all-in-one JavaScript runtime</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**社区讨论**: 社区讨论包括 Jarred Sumner 澄清重写在 Claude Code 中的成功以及 v1.4 延迟的具体原因。其他用户讨论了重大重构后预期的开发速度放缓，对 LLM 驱动开发表示怀疑，并将 Bun 的情况与一个声称无需完全重写即可修复原始问题的 Zig 替代方案进行了比较。

**标签**: `#Bun`, `#Rust`, `#JavaScript Runtime`, `#Software Development`, `#Compatibility`

---

<a id="item-14"></a>
## [AI 行业从聊天机器人转向代理系统，Mollick 指南更新](https://simonwillison.net/2026/Jul/27/an-opinionated-guide-to-which-ai-to-use-to-do-stuff/#atom-everything) ⭐️ 8.0/10

Ethan Mollick 更新的 AI 使用指南强调了从 ChatGPT、Claude 和 Gemini 等基本聊天界面向能够执行大量、耗时数小时的人类工作的“代理系统”的重大转变。谷歌的 Gemini 已显著跌出推荐榜单，因为其代理产品 Gemini Spark 仍在发展中。 这种向代理 AI 系统的转变标志着人工智能的关键演进，它能实现更自主、更复杂的任务执行，从而显著提高生产力并重塑个人和企业利用 AI 的方式。这一发展对于寻求理解和实施尖端 AI 应用的从业者和研究人员尤为重要。 该指南阐明，AI 公司提供了“计算机访问”模式，如 ChatGPT Work 和 Claude Cowork，这些模式与桌面应用程序版本（ChatGPT Work/Codex，Claude Cowork/Code）不同，后者可以访问用户的计算机。值得注意的是，ChatGPT 移动版的“Work”模式使其 Code Interpreter 能够访问互联网，这是代理任务的一项重要能力。

rss · Simon Willison · 7月27日 21:55

**背景**: 代理 AI 系统是先进的人工智能模型，能够自主感知、推理和行动，在有限的人工监督下实现特定目标，超越了简单的对话响应。OpenAI Codex 是 OpenAI 开发的一套 AI 驱动的编码代理，旨在自动化软件工程任务。Code Interpreter 是 ChatGPT 等 AI 模型中的一个工具，允许它们在沙盒环境中编写和执行代码，以解决问题或处理数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained | MIT Sloan</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-ai">What is Agentic AI? | IBM</a></li>
<li><a href="https://grokipedia.com/page/OpenAI_Codex">OpenAI Codex</a></li>

</ul>
</details>

**标签**: `#AI Tools`, `#Agentic AI`, `#Large Language Models`, `#AI Applications`, `#Productivity`

---

<a id="item-15"></a>
## [纯 PyTorch 从零构建 Transformer 实现英泰机器翻译](https://www.reddit.com/r/MachineLearning/comments/1v86qo9/built_trained_a_transformer_from_scratch_in_pure/) ⭐️ 8.0/10

一位作者基于原始的《Attention Is All You Need》论文，使用纯 PyTorch 的`torch.nn`原语从零开始实现并训练了一个完整的 Transformer 架构，用于英泰机器翻译，并提供了详细的数学和代码解析。 该项目通过提供一个透明的实践实现，为理解作为现代自然语言处理核心以及许多大型语言模型基础的 Transformer 架构，提供了宝贵的教育资源。 该模型在 Kaggle 上使用双 NVIDIA T4 GPU，利用`gopi30/english-tamil`平行翻译数据集进行训练，随附的博客文章和 GitHub 仓库提供了涵盖每个方程、张量形状转换和 PyTorch 模块的逐步教程。

reddit · r/MachineLearning · /u/imrancoder · 7月27日 17:17

**背景**: Transformer 是一种深度学习架构，由 Ashish Vaswani 及其 Google Brain 的同事于 2017 年在其开创性论文《Attention is All You Need》中提出。它通过完全依赖自注意力机制来高效处理和生成序列，捕获长距离依赖关系，从而彻底改变了序列建模，并成为当今许多大型语言模型的基础模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Transformer_(deep_learning)">Transformer (deep learning) - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Transformer_deep_learning_architecture">Transformer (deep learning architecture)</a></li>
<li><a href="https://arxiv.org/abs/1706.03762">Abstract page for arXiv paper 1706.03762: Attention Is All You Need</a></li>

</ul>
</details>

**标签**: `#Machine Learning`, `#Deep Learning`, `#Transformers`, `#PyTorch`, `#NLP`

---

<a id="item-16"></a>
## [新评估揭示前沿大型语言模型普遍存在左倾偏见](https://www.reddit.com/r/MachineLearning/comments/1v8fnzw/evaluated_6_frontier_llms_gpt54_claude_sonnet_46/) ⭐️ 8.0/10

一项独立评估项目对包括 GPT-5.4 和 Claude Opus 4.7 在内的六个前沿大型语言模型进行了基准测试，使用了八个偏见/公平性数据集，结果显示大多数模型存在一致的左倾政治偏见，并且部分模型在种族相关问题上表现出显著的拒绝回答率。该研究特别测试了 Gemini Pro/Flash 和 Grok 4.3 等模型在政治、性别和种族偏见方面的表现，使用了大约 20,600 个示例。 这项评估对负责任的 AI 发展至关重要，因为它揭示了领先大型语言模型中固有的偏见，这些偏见可能影响各种应用中的信息传播和决策制定。理解这些偏见对于减轻潜在危害和确保全球部署的 AI 系统公平性至关重要。 该研究使用了包括 WinoBias 和 BBQ Race/Ethnicity 在内的八个既定偏见/公平性数据集，值得注意的是，Grok 4.3 虽然自称右倾，但在其他政治偏见基准测试中表现出左倾行为。GPT-5.4 在 BBQ 种族相关数据上的拒绝回答率最高（20.3%），但该项目为独立且未经同行评审，且每个任务仅使用单一提示模板。

reddit · r/MachineLearning · /u/marggggggggg · 7月27日 22:37

**背景**: 大型语言模型（LLM）是强大的 AI 系统，通过海量文本数据训练而成，这可能导致它们无意中学习并延续数据中存在的社会偏见。WinoBias、BBQ（Bias Benchmark for QA）和 SeeGULL 等基准测试数据集是关键工具，旨在系统地识别和衡量这些偏见，分别侧重于性别刻板印象、问答中的社会偏见以及地理文化刻板印象。这些评估有助于研究人员了解偏见如何在 AI 输出中体现，并努力开发更公平、更道德的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kaggle.com/datasets/thedevastator/winobias-coreference-dataset">WinoBias Coreference Dataset | Kaggle</a></li>
<li><a href="https://github.com/nyu-mll/BBQ">GitHub - nyu-mll/BBQ: Repository for the Bias Benchmark for ... BBQ Dataset: Benchmark for QA Social Bias - emergentmind.com HiTZ/bbq · Datasets at Hugging Face BBQ (Bias Benchmark for QA) - AI Wiki BBQ: Bias Benchmark for QA - emergentmind.com BBQ: Bias Benchmark for Question Answering – Inspect Evals</a></li>
<li><a href="https://arxiv.org/pdf/2305.11840">SeeGULL : A Stereotype Benchmark with Broad Geo-Cultural Coverage</a></li>

</ul>
</details>

**标签**: `#LLM Bias`, `#AI Ethics`, `#Benchmarking`, `#Large Language Models`, `#Responsible AI`

---

<a id="item-17"></a>
## [提议在 MLOps 中为训练数据质量设置“通过/不通过”门禁](https://www.reddit.com/r/MachineLearning/comments/1v8a3nu/training_data_needs_a_real_gonogo_gate_before/) ⭐️ 8.0/10

一项新提议主张为训练数据引入一个专门的、可复现的“通过/不通过”门禁系统，以在模型训练前严格审计训练数据工件的质量、完整性和相关性，包括检查数据泄露和溯源。该系统旨在根据明确的证据提供清晰的判断（通过、警告、失败、安全失败），而非仅仅依赖人工判断或聚合分数。 这项提议意义重大，因为它解决了当前 MLOps 流程中一个关键的薄弱环节，即训练前数据验证通常缺乏一个健壮、可复现和集中的控制层。实施这样一个门禁系统，通过在训练前确保数据质量和完整性，可以显著提高机器学习模型的可靠性和可信度，从而减轻数据泄露等风险并增强整体 AI 安全性。 提议的系统强调可复现性，确保相同的工件、目标和配置能产生相同的结果，并明确指出大型语言模型不会决定最终的判断。它旨在提供修复计划，并将批准的更改应用于派生副本，同时保留原始数据，但一个潜在的局限性是数据质量的上下文性，如果透明度不足，可能会产生虚假的安全感。

reddit · r/MachineLearning · /u/jesusmjk · 7月27日 19:13

**背景**: MLOps（机器学习运维）是一种工程文化，旨在简化机器学习生命周期，将持续集成（CI）实践扩展到包括数据和模型的验证。MLOps 中的一个关键挑战是数据泄露，即训练数据集之外的信息在无意中被用于构建模型，导致模型性能评估出现误导性的高估。数据溯源，即在整个机器学习管道中追踪数据的来源和转换的能力，对于确保数据完整性和可复现性至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ml-ops.org/content/mlops-principles">MLOps Principles</a></li>
<li><a href="https://medium.com/learning-data/the-silent-killer-in-machine-learning-how-data-leakage-destroys-model-credibility-83402572b94f">Data leakage : The hidden risk in your predictive model | Medium</a></li>
<li><a href="https://zenithlaw.com/data-provenance-ml-lifecycle-traceability-graph-methods-ten-lessons">Data Provenance in Machine Learning : Traceability, Graph Met</a></li>

</ul>
</details>

**标签**: `#MLOps`, `#Data Quality`, `#Machine Learning`, `#Data Validation`, `#AI Safety`

---

<a id="item-18"></a>
## [小米澎程将于 7 月 30 日发布昆仑架构及新款 SUV](https://weibo.com/4073292684/RazBkqQXm) ⭐️ 8.0/10

小米澎程宣布将于 2026 年 7 月 30 日举行技术发布会，正式揭晓“小米昆仑技术架构”，包括昆仑平台、昆仑超级增程和昆仑全域安全，同时还将推出两款智能增程 SUV 车型：N90 Max 和 N70 Max。 此次发布标志着小米在竞争激烈的电动汽车市场中深化其战略承诺，推出全面的技术架构和新款增程 SUV 车型，这可能对行业格局和消费者选择产生重大影响。 “昆仑技术架构”包括昆仑平台、昆仑超级增程和昆仑全域安全，其中 N90 Max 定位为大七座旗舰增程 SUV，N70 Max 为大五座四驱增程 SUV。小米于 2023 年初开始从零开发昆仑架构。

telegram · zaihuapd · 7月27日 01:02

**背景**: 增程式电动汽车（EREV）结合了用于驱动的电动机和作为发电机为电池充电的小型内燃机，可在电池电量耗尽时延长车辆续航里程。在汽车领域，“技术架构”指的是支撑一系列车辆的基础设计和集成系统，涵盖硬件、软件、安全和动力总成技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.globalchinaev.com/post/xiaomi-to-unveil-skynomad-n90-max-n70-max-suvs-at-july-30-event">Xiaomi to unveil SkyNomad N90 Max, N70 Max SUVs at July 30 event</a></li>
<li><a href="https://cnevpost.com/2026/07/27/xiaomi-debut-sky-nomad-suvs-jul-30/">Xiaomi to debut first two Sky Nomad SUVs on July 30 - CnEVPost</a></li>
<li><a href="https://eletric-vehicles.com/xiaomi/xiaomi-to-launch-first-hybrid-models-under-sky-nomad-series-on-july-30/">Xiaomi to Debut First Hybrid Models Under Sky Nomad Series on July...</a></li>

</ul>
</details>

**标签**: `#Electric Vehicles`, `#Automotive Technology`, `#Xiaomi`, `#Technical Architecture`, `#Product Launch`

---

<a id="item-19"></a>
## [长鑫科技科创板首秀创纪录，股价飙升](https://www.stcn.com/article/detail/4042119.html) ⭐️ 8.0/10

7 月 27 日，中国存储巨头长鑫科技（CXMT）正式登陆上海证券交易所科创板，首日开盘价较发行价上涨 471.59%至每股 49.5 元，实际募集资金约 579 亿元人民币。此次 IPO 有望超越中芯国际此前的纪录，成为科创板史上最大规模的首次公开募股。 此次创纪录的 IPO 对长鑫科技及更广泛的中国半导体产业而言是一个重要的金融里程碑，它增强了国内在存储技术方面的能力，并可能重塑全球科技供应链。巨额的资金注入以及预计到 2026 年上半年实现盈利，表明中国在关键领域推动自给自足和提高竞争力的决心。 长鑫科技的首次公开募股发行价为每股 8.66 元，首日开盘价报 49.5 元，涨幅高达 471.59%。公司实际募集资金约 579.19 亿元人民币，若超额配售选择权全额行使，预计募资总额可达 666.07 亿元人民币，并预计在 2026 年上半年实现归母净利润 500 亿至 570 亿元人民币。

telegram · zaihuapd · 7月27日 01:29

**背景**: 科创板，即上海证券交易所科创板，于 2019 年设立，旨在支持中国的科技创新型企业，常被视为中国的“纳斯达克”。长鑫科技（CXMT）是中国领先的动态随机存取存储器（DRAM）芯片制造商，DRAM 是计算机和电子设备中的关键组件，长鑫科技在中国减少对外国存储供应商依赖的努力中扮演着重要角色。

**标签**: `#Semiconductor Industry`, `#IPO`, `#Memory Technology`, `#China Tech`, `#Financial News`

---

<a id="item-20"></a>
## [华为被指筹建 DRAM 工厂以保障 AI 芯片供应](https://www.xda-developers.com/huawei-is-building-its-own-dram-fab-and-it-could-reshape-ram-prices-for-everyone/) ⭐️ 8.0/10

华为被指正与深圳存储芯片企业昇维旭合作，在中国建设一座规划月产能约 14 万片晶圆的 12 英寸 DRAM 晶圆厂，尽管华为已否认相关说法。 这一举动（如果属实）旨在保障华为昇腾 AI 芯片的内存供应，并降低对外部供应商的依赖，可能对全球半导体供应链和中国本土芯片产业产生深远的长期影响。 该规划中的工厂是一座 12 英寸 DRAM 晶圆厂，月产能目标为 14 万片晶圆，但分析人士指出，新工厂的建设和量产需要较长时间，短期内难以显著影响消费级内存价格。

telegram · zaihuapd · 7月27日 03:17

**标签**: `#Semiconductor Manufacturing`, `#DRAM`, `#Supply Chain`, `#Huawei`, `#AI Hardware`

---

<a id="item-21"></a>
## [谷歌透露 Gemini 4 为迄今最雄心预训练，预计年底发布](https://9to5google.com/2026/07/26/google-gemini-4-teases/) ⭐️ 8.0/10

谷歌 CEO Sundar Pichai 宣布，下一代大模型 Gemini 4 已投入训练，这是该公司迄今为止最具雄心的预训练项目，专注于前沿 AGI 研发，预计将于今年年底（可能在 11 月或 12 月）发布。 这一声明标志着谷歌在引领人工智能前沿方面的承诺进一步加强，可能推出一个高度先进的模型，从而显著影响更广泛的人工智能生态系统并加速 AGI 的发展。 Pichai 强调谷歌将优先把算力分配给 Gemini 4 的前沿 AGI 研发，同时 Gemini 3.x Flash 系列将保持几乎每月一次的迭代频率，重点提升智能编码等能力。

telegram · zaihuapd · 7月27日 04:06

**背景**: “前沿 AGI”指的是通用人工智能（Artificial General Intelligence）研究的最前沿，旨在开发在广泛任务中具备类人认知能力的 AI 模型，通常超越当前在推理、编码和多模态方面的能力。而 Gemini Flash 系列是谷歌 Gemini 模型系列中轻量级、高效的模型，专为需要效率和智能的高吞吐量任务而优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.turing.com/blog/how-frontier-agi-becomes-enterprise-impact">How Frontier AGI Becomes Enterprise Impact</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/">Gemini 3.5: frontier intelligence with action</a></li>
<li><a href="https://lmmarketcap.com/google-gemini-models">All Gemini Models - Pro, Ultra, Flash (2026) | LM Market Cap</a></li>

</ul>
</details>

**标签**: `#AI`, `#Large Language Models`, `#Google Gemini`, `#AGI`, `#Machine Learning`

---