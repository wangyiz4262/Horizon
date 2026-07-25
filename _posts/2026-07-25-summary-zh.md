---
layout: default
title: "Horizon Summary: 2026-07-25 (ZH)"
date: 2026-07-25
lang: zh
---

> 从 26 条内容中筛选出 15 条重要资讯。

---

1. [vLLM v0.26.0 发布，支持 Inkling 模型，优化 DeepSeek-V4 性能并提升精度](#item-1) ⭐️ 9.0/10
2. [SGLang v0.5.16 发布，通过 DSpark 和 Inkling 支持提升 LLM 推理](#item-2) ⭐️ 9.0/10
3. [开源权重 AI 模型迎来“Kubernetes 时刻”](#item-3) ⭐️ 9.0/10
4. [Anthropic 发布 Claude Opus 5，以半价领先 AI 排行榜](#item-4) ⭐️ 9.0/10
5. [AMD 通过激进的 AI 战略加剧对英伟达 CUDA 的挑战](#item-5) ⭐️ 9.0/10
6. [市场监管总局对携程滥用市场支配地位罚没 51.79 亿元](#item-6) ⭐️ 9.0/10
7. [高通宣布全线产品自 9 月 1 日起涨价](#item-7) ⭐️ 9.0/10
8. [苹果游说特朗普政府采用中国存储芯片，遭美光阻挠](#item-8) ⭐️ 9.0/10
9. [开发者发布 usbliter8 越狱方案，支持 iOS 15-16 的 iPhone 11 Pro](#item-9) ⭐️ 9.0/10
10. [AMD 确认 Zen 7 EPYC 处理器 2028 年推出，Zen 8 计划 2030 年登场](#item-10) ⭐️ 9.0/10
11. [Android 或将限制设备端 ADB 功能](#item-11) ⭐️ 8.0/10
12. [离网消息应用 Bitchat 现已托管于 Radicle](#item-12) ⭐️ 8.0/10
13. [Ruff v0.16.0 大幅增加默认代码检查规则，导致重大变更](#item-13) ⭐️ 8.0/10
14. [Anthropic Claude Opus 5 模型显著增强抗提示注入能力](#item-14) ⭐️ 8.0/10
15. [微软将利用 TPM 芯片打击盗版 Windows 激活](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.26.0 发布，支持 Inkling 模型，优化 DeepSeek-V4 性能并提升精度](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 9.0/10

vLLM v0.26.0 已发布，全面支持新的 Inkling 模型家族，显著优化了 DeepSeek-V4 在多种硬件上的性能，并通过 `fp32 lm_head` 提升了生成精度。 此次发布意义重大，因为 vLLM 是一个关键的 LLM 推理引擎，这些更新扩展了其模型兼容性，提升了在不同硬件上的部署效率，并改善了生成内容的质量，从而惠及更广泛的 LLM 生态系统。 主要技术细节包括对 Inkling 模型家族的全面支持，涵盖 Hopper FA4 相对注意力机制和 ModelOpt NVFP4 量化，以及通过专用内核和 AMD/XPU 上的 DSpark 推测解码对 DeepSeek-V4 进行的性能提升。此外，`fp32 lm_head` 提升了精度并扩展到 LoRA 路径，同时 KV 卸载和灵活的注意力后端也得到了显著改进。

github · khluu · 7月25日 10:38

**背景**: vLLM 是一个用于大型语言模型的高吞吐量、低延迟推理引擎，旨在优化 GPU 利用率。Inkling 模型家族指的是一系列新的多模态专家混合（MoE）模型。`fp32 lm_head` 指的是为语言模型头部使用 32 位浮点精度，这通常能提升输出精度。Hopper 是英伟达（NVIDIA）的 GPU 架构，而 Flash Attention 4 (FA4) 是一种为这些 GPU 设计的优化注意力机制内核，旨在提升性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.baseten.co/library/inkling/">Inkling | Model library</a></li>
<li><a href="https://build.nvidia.com/spark/nvfp4-quantization">NVFP4 Quantization | DGX Spark</a></li>
<li><a href="https://explainx.ai/blog/gemma-4-updates-flash-attention-tool-calling-july-2026">Gemma 4 Update: FA4, Tool Calling, Vision (July 2026)</a></li>

</ul>
</details>

**标签**: `#LLM Inference`, `#Deep Learning`, `#Performance Optimization`, `#AI Models`, `#GPU Acceleration`

---

<a id="item-2"></a>
## [SGLang v0.5.16 发布，通过 DSpark 和 Inkling 支持提升 LLM 推理](https://github.com/sgl-project/sglang/releases/tag/v0.5.16) ⭐️ 9.0/10

SGLang v0.5.16 推出了 DSpark，这是一种新颖的置信度驱动的推测解码算法，并增加了对 Inkling 的支持，Inkling 是一个拥有 9750 亿参数、100 万 token 上下文的多模态专家混合 (MoE) 模型。此次发布还包括其他模型支持、性能优化（如 UnifiedRadixTree 成为默认）以及 GLM-5.2 的内存改进。 这些进展意义重大，因为 DSpark 有望大幅提升大型语言模型 (LLM) 的推理速度，使其部署更高效、更具成本效益。Inkling 这一强大多模态 MoE 模型的集成，扩展了 SGLang 处理涉及文本、图像和音频的复杂任务的能力，从而推动了 LLM 能力的边界。 DSpark 在 DeepSeek-V4-Pro 上实现了 383.7 tok/s 的速度，接受长度约为 5，它采用置信度驱动的方法来确定验证窗口大小。Inkling 是一个拥有 9750 亿参数（其中 410 亿活跃参数）的 MoE 模型，它集成了滑动窗口、全注意力以及 Mamba2 线性注意力，并支持 NVFP4 MoE，在 Blackwell 上输入速度可达 71.7k tok/s。此外，UnifiedRadixTree 现已成为多种模型类型的默认设置，GLM-5.2 通过 DSA 缓存层拆分，将每个 rank 的 KV 内存减少了约 74%。

github · Qiaolin-Yu · 7月25日 00:13

**背景**: 推测解码是一种 LLM 推理优化技术，其中一个更小、更快的“草稿”模型会提前生成多个 token，然后由更大的“目标”模型并行验证这些 token，如果草稿准确，则可以显著加快生成速度。专家混合 (MoE) 是一种神经网络架构，其中不同的“专家”子网络专门处理输入或任务的不同部分，这使得模型能够扩展到非常大的规模，同时在每次推理时只激活一部分参数，从而提高效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.05147">[2607.05147] DSpark: Confidence-Scheduled Speculative ...</a></li>
<li><a href="https://models.dev/models/thinkingmachines/inkling/">Inkling pricing, providers, and specs | Models .dev</a></li>
<li><a href="https://www.redhat.com/en/topics/ai/mixture-of-experts">What is Mixture of Experts ( MoE )?</a></li>

</ul>
</details>

**标签**: `#LLM Inference`, `#Speculative Decoding`, `#Multimodal Models`, `#MoE`, `#Performance Optimization`

---

<a id="item-3"></a>
## [开源权重 AI 模型迎来“Kubernetes 时刻”](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/) ⭐️ 9.0/10

一篇最新文章指出，开源权重 AI 模型正经历一个变革性的“Kubernetes 时刻”，标志着 AI 行业的一个关键转折点，它将使 AI 技术普及化并促进广泛创新。 这一趋势意义重大，因为它可能从根本上重塑 AI 格局，使更广泛的开发者和企业更容易获得先进的 AI 技术并促进创新，就像 Kubernetes 彻底改变了云基础设施一样。它有望创建一个更具竞争力和多样性的 AI 生态系统，减少对少数专有模型的依赖。 开源权重 AI 的“Kubernetes 时刻”意味着向标准化、易于访问和广泛采用的基础 AI 组件转变，从专有、封闭系统转向更协作和分布式的开发模式。这一转变预计将为 AI 推理成本提供一个基准，为当前行业中波动的定价带来合理性。

hackernews · tknaup · 7月25日 14:49 · [社区讨论](https://news.ycombinator.com/item?id=49048034)

**背景**: 开源权重 AI 模型向公众发布其训练好的参数（权重），允许他人使用和修改，但它们与完全开源模型不同，后者还会提供训练代码和数据。“Kubernetes 时刻”指的是一项技术成为广泛采用的基础标准，从而普及了访问并实现了重大创新的时刻，就像 Kubernetes 对容器编排和云基础设施管理所做的那样。这种转变使得应用程序的部署更具可扩展性、弹性和可移植性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told – Open Source Initiative</a></li>
<li><a href="https://geotoolbox.ai/blog/open-weights-vs-open-source">Open Weights vs Open Source: The Real Difference (2026) | GEO Toolbox</a></li>
<li><a href="https://www.cncf.io/blog/2026/04/30/ai-sandboxing-is-having-its-kubernetes-moment/">AI sandboxing is having its Kubernetes moment | CNCF</a></li>

</ul>
</details>

**社区讨论**: 社区讨论强调了开源权重 AI 的实际和地缘政治挑战，质疑由于权重本质上是数字而按来源禁止模型的可能性。评论者还讨论了开源模型通过提供推理成本基线对 AI“代币经济学”的影响，呼吁发布具有对初创公司友好许可的前沿级开源权重模型，以及像 Linux 开发模式那样实现协作式、公开训练模型的长期愿景。

**标签**: `#Open-weight AI`, `#AI Industry`, `#Machine Learning`, `#Technology Trends`, `#AI Policy`

---

<a id="item-4"></a>
## [Anthropic 发布 Claude Opus 5，以半价领先 AI 排行榜](https://simonwillison.net/2026/Jul/24/introducing-claude-opus-5/#atom-everything) ⭐️ 9.0/10

Anthropic 正式发布了 Claude Opus 5，这是一款被描述为深思熟虑且积极主动的新型大型语言模型，目前在 Artificial Analysis 排行榜上名列前茅，并以其前身一半的价格提供接近 Claude Fable 5 的前沿智能。新模型定价与 Opus 4.8 相同，并提供一个价格是基础模型两倍的“快速模式”。 此次发布意义重大，Claude Opus 5 在 Artificial Analysis 排行榜上的领先地位，加上其以更低成本提供顶级智能的特点，标志着尖端大型语言模型在 AI 市场中变得更易获取且更具竞争力。其主动性能力，例如自主创建计算机视觉管道，可能会重新定义 AI 模型处理复杂多模态任务的方式。 Claude Opus 5 展现出“持续主动”的行为，例如在没有直接查看权限的情况下，能够自主创建计算机视觉管道来解释图纸以进行 3D 模型重建。尽管它在发现网络安全漏洞方面有了显著改进，但 Anthropic 故意没有对其进行漏洞利用方面的训练，因此在将漏洞转化为实际网络威胁方面仍落后于 Mythos 5。

rss · Simon Willison · 7月24日 23:48

**背景**: 大型语言模型（LLM）是经过大量文本数据训练的先进人工智能模型，能够理解、生成和处理人类语言，并执行写作、编码和解决问题等任务。Anthropic 是一家专注于 AI 安全和研究的公司，以开发 Claude 系列 LLM 而闻名，该系列模型与来自其他主要 AI 开发商的模型竞争。AI 排行榜，例如 Artificial Analysis 排行榜，根据各种性能指标对这些模型进行排名，帮助用户比较它们的能力和效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/">AI Model & API Providers Analysis | Artificial Analysis</a></li>
<li><a href="https://huggingface.co/spaces/ArtificialAnalysis/LLM-Performance-Leaderboard">LLM Performance Leaderboard - a Hugging Face Space by ArtificialAnalysis</a></li>

</ul>
</details>

**标签**: `#AI`, `#Large Language Models`, `#Anthropic`, `#Machine Learning`, `#LLM Release`

---

<a id="item-5"></a>
## [AMD 通过激进的 AI 战略加剧对英伟达 CUDA 的挑战](https://newsletter.semianalysis.com/p/can-amd-break-the-cuda-moat-amd-advancing) ⭐️ 9.0/10

AMD 正在实施激进的策略，包括可能高达 105%的折扣以及代理式内核生成等技术创新，以挑战英伟达在 AI 市场中 CUDA 的主导地位。 这一发展意义重大，因为它可能通过加剧与英伟达的竞争，从根本上重塑 AI 硬件和软件生态系统，并有望为 AI 开发带来更快的创新和更低的成本。 关键细节包括 AMD 对代理式内核生成和软件质量改进的关注，以及高达 105%折扣等激进市场策略，尽管其内部面临开发集群不稳定和 Helios MI455X 系统生产爬坡困难等挑战。

rss · Semianalysis · 7月25日 00:33

**背景**: 英伟达的 CUDA 是一个专有的并行计算平台和编程模型，为 GPU 加速计算，特别是在 AI 领域，建立了主导性的软件生态系统。代理式内核生成是一种先进的方法，它利用自主 AI 代理和大型语言模型自动创建、优化和验证高性能 GPU 内核，旨在简化复杂的编程任务。AMD 的 Helios MI455X 是 AMD 的机架级 AI 系统，配备 72 个 Instinct MI455X 加速器和 HBM4 内存，旨在直接挑战英伟达的高密度 AI 基础设施产品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2602.24286">[2602.24286] CUDA Agent: Large-Scale Agentic RL for High ... [2607.04395] NKI-Agent: Domain-Specific Fine-Tuning and ... qhy991/Awesome-LLM-Kernel-Agent - GitHub Awesome LLM-Driven Kernel Generation - GitHub KernelAgent: Hardware-Guided GPU Kernel Optimization via ... Agentic Kernel Generation - emergentmind.com</a></li>
<li><a href="https://www.storagereview.com/news/amd-mi455x-and-helios-432gb-hbm4-72-gpu-racks-and-a-real-answer-to-vera-rubin">AMD MI455X and Helios: 432GB HBM4, 72-GPU Racks, and a Real ...</a></li>
<li><a href="https://github.com/qhy991/Awesome-LLM-Kernel-Agent">qhy991/Awesome-LLM-Kernel-Agent - GitHub</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#AMD`, `#NVIDIA`, `#CUDA`, `#Market Strategy`

---

<a id="item-6"></a>
## [市场监管总局对携程滥用市场支配地位罚没 51.79 亿元](https://www.xinhuanet.com/fortune/20260725/693124245aa44d2bbc7520b7a0c244ea/c.html) ⭐️ 9.0/10

7 月 25 日，国家市场监督管理总局依据反垄断法，对携程集团有限公司滥用市场支配地位实施垄断行为作出行政处罚，罚没款合计 51.79 亿元，其中包括没收违法所得 16.58 亿元和罚款 35.21 亿元。监管部门还责令携程立即停止违法行为，退还强制扣除酒店经营者的订单储备金 1.22 亿元，并要求其全面整改。 对主要在线旅游平台携程处以巨额罚款，表明中国在科技领域持续加强反垄断执法，这强化了对平台企业市场行为的监管审查，并可能影响整个行业的商业惯例。此举也强调了政府致力于促进公平竞争和保护中小企业及消费者利益的决心。 此次总计 51.79 亿元的罚没款包括没收违法所得 16.58 亿元和罚款 35.21 亿元，同时携程还被责令退还强制扣除酒店经营者的订单储备金 1.22 亿元。携程已公开回应表示诚恳接受处罚决定，并将逐项推进并系统落实各项整改工作。

telegram · zaihuapd · 7月25日 02:24

**背景**: 中国于 2008 年颁布并近期修订的《反垄断法》旨在预防垄断行为、保护公平竞争并维护消费者利益。国家市场监督管理总局（SAMR）是负责执行该法律的主要政府机构，尤其关注电子商务和技术等平台主导地位日益突出的行业。

**标签**: `#Antitrust`, `#Regulatory Enforcement`, `#Online Travel`, `#China Tech`, `#Market Dominance`

---

<a id="item-7"></a>
## [高通宣布全线产品自 9 月 1 日起涨价](https://tw.news.yahoo.com/%E7%8D%A8%E5%AE%B6-%E9%AB%98%E9%80%9A%E6%BC%B2%E5%83%B9%E4%BF%A1%E6%9B%9D%E5%85%89-%E5%85%A8%E7%B7%9A%E7%94%A2%E5%93%819-1%E8%B5%B7%E8%AA%BF%E6%BC%B2-%E7%9B%B4%E8%A8%80-142730846.html) ⭐️ 9.0/10

高通于 2026 年 7 月 24 日向客户发出价格调整通知信，宣布自 9 月 1 日起，对当日或之后出货的全线产品调涨价格，具体新报价将由客户经理逐一提供。 作为主要的半导体供应商，高通此次全面涨价意义重大，它反映了制造成本上升和 AI/数据中心需求激增，预计将导致消费电子产品价格上涨或规格缩减，并影响更广泛的科技供应链。 高通将价格调整归因于晶圆制造、封装测试、先进封装和基板材料成本的持续上升，以及 AI 和数据中心需求激增对供应链产能的挤压，强调这并非短期波动，而是行业结构性转变。

telegram · zaihuapd · 7月25日 03:01

**背景**: 半导体先进封装是指将多个组件或芯片集成到单个封装中的创新技术，通过缩短信号路径和实现异构集成来提高性能和效率，这对于 AI 等先进应用至关重要。半导体基板材料通常是薄硅晶圆，是构建集成电路和其他微电子器件的基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Advanced_packaging_(semiconductors)">Advanced packaging (semiconductors)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wafer_(electronics)">Wafer (electronics) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Semiconductor Industry`, `#Supply Chain`, `#Pricing Strategy`, `#Consumer Electronics`, `#AI Impact`

---

<a id="item-8"></a>
## [苹果游说特朗普政府采用中国存储芯片，遭美光阻挠](https://www.wsj.com/tech/trump-apple-micron-china-chips-784bbd3d) ⭐️ 9.0/10

苹果公司正积极游说特朗普政府，希望允许其在销往美国以外市场的产品中使用中国长鑫存储（CXMT）和长江存储（YMTC）的存储芯片，以降低成本。此举遭到美国主要供应商美光科技的强烈反对，使特朗普政府陷入两家美国大公司之间的交锋。 这一进展意义重大，它凸显了一家美国主要科技公司的全球供应链战略与美国旨在限制中国半导体产业的地缘政治政策之间的直接冲突。其结果可能重塑全球科技供应链，影响美中贸易关系，并改变全球存储芯片制造商的竞争格局。 据报道，苹果首席执行官库克及多名高管近几周已向特朗普、商务部长卢特尼克和财政部长贝森特等人推销此方案，旨在采购长鑫存储（CXMT）和长江存储（YMTC）的存储芯片以降低成本。该计划专门针对销往美国以外市场的产品，表明苹果试图在优化全球运营的同时应对地缘政治紧张局势。

telegram · zaihuapd · 7月25日 04:02

**背景**: 长鑫存储技术有限公司（CXMT）是中国领先的 DRAM（动态随机存取存储器）芯片制造商，其产品用于手机和个人电脑等设备；而长江存储技术有限公司（YMTC）则专注于 NAND 闪存芯片。这两家公司均成立于 2016 年，获得政府投资，旨在减少中国对外国芯片技术的依赖，并推动其半导体自给自足。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cxmt.com/en/">About cxmt - cxmt</a></li>
<li><a href="https://en.wikipedia.org/wiki/Yangtze_Memory_Technologies">Yangtze Memory Technologies - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Geopolitics`, `#Supply Chain`, `#Semiconductor Industry`, `#US-China Relations`, `#Corporate Strategy`

---

<a id="item-9"></a>
## [开发者发布 usbliter8 越狱方案，支持 iOS 15-16 的 iPhone 11 Pro](https://github.com/34306/usbliter8-fun) ⭐️ 9.0/10

开发者 34306 发布了基于 usbliter8 漏洞的全新越狱方案，目前支持运行 iOS 15.0-16.x 的 iPhone 11 Pro 等 A11-A13 设备。该方案需要借助搭载 RP2350 芯片的 Raspberry Pi Pico 2，利用 SecureROM 漏洞将设备置入 PWN DFU 模式，并刷入定制固件。 此次越狱方案意义重大，因为它利用了 usbliter8 这一基于硬件的 SecureROM 漏洞，对此前被认为不受此类无法修补漏洞影响的 A12 和 A13 芯片实现了突破。这展示了 iOS 安全研究在较新硬件上实现深度系统访问的先进能力。 该方案涉及高级内核补丁，以绕过 USB 限制模式、沙盒执行限制和 AMFI (Apple Mobile File Integrity) 信任缓存检查。然而，它会带来严重副作用，包括抹除设备全部数据，并破坏 SEP、密码、WiFi、基带、蓝牙（部分可用）以及所有 Apple 服务。

telegram · zaihuapd · 7月25日 11:00

**背景**: SecureROM 是 Apple 设备处理器启动时执行的第一段代码，它位于芯片内部，因此无法通过软件更新进行修补。usbliter8 漏洞专门针对 Apple A12 和 A13 芯片 SecureROM 中的一个缺陷，通过 USB DFU 模式，在操作系统加载之前实现任意代码执行。Apple Mobile File Integrity (AMFI) 是一个内核扩展，用于强制执行所有可执行文件的代码签名验证，从而阻止未签名或恶意代码在 iOS 设备上运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/06/unpatchable-usbliter8-exploit-breaks.html">Unpatchable 'usbliter8' Exploit Breaks Apple A12 and A13 SecureROM ...</a></li>
<li><a href="https://hoploninfosec.com/usbliter8-exploit-apple-a12-a13-securerom-vulnerability">usbliter8 Exploit: Apple A12/A13 SecureROM Flaw Explained</a></li>

</ul>
</details>

**标签**: `#iOS Jailbreak`, `#Hardware Exploitation`, `#Apple Security`, `#SecureROM`, `#Systems Research`

---

<a id="item-10"></a>
## [AMD 确认 Zen 7 EPYC 处理器 2028 年推出，Zen 8 计划 2030 年登场](https://www.techspot.com/news/113233-amd-confirms-zen-7-epyc-florence-2028-previews.html) ⭐️ 9.0/10

AMD 已正式确认其 EPYC 服务器处理器的长期路线图，宣布采用 Zen 7“Florence”架构的处理器将于 2028 年推出，该架构将包含 AI 计算扩展并支持新型 MRDIMM 和 LPDDR 内存，随后 Zen 8“Ravenna”架构计划于 2030 年登场。 这一声明对数据中心和 AI 基础设施行业至关重要，它提供了主要 CPU 供应商的清晰长期愿景，使合作伙伴和客户能够规划未来的硬件投资和 AI 驱动的系统设计。AI 扩展和先进内存技术的集成表明了 AMD 对高性能计算和 AI 工作负载的承诺。 Zen 7“Florence”处理器将包含标准 Zen 7 和高密度 Zen 7c 核心，支持下一代 MRDIMM 和 LPDDR 内存，并将部署在 SP7 和 SP8 平台上，用于未来的“Ferrara”AI 机架系统。尽管 Zen 8“Ravenna”已确认于 2030 年推出，但其制造工艺、核心数量和内存规格等具体细节尚未公布。

telegram · zaihuapd · 7月25日 14:05

**背景**: MRDIMM（多路复用秩 DIMM）是一种先进的内存技术，它基于 DDR5 架构，旨在显著提高服务器内存容量和带宽，解决下一代 CPU 和 AI 应用的内存带宽瓶颈。Zen 7c 核心是 AMD Zen 7 架构的专用变体，针对高密度计算进行了优化，以在服务器处理器中实现更高的核心数量，作为标准 Zen 7 核心的补充。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.micron.com/products/memory/dram-modules/mrdimm">MRDIMM | Micron Technology Inc.</a></li>
<li><a href="https://lenovopress.lenovo.com/lp2028-introduction-to-mrdimm-memory-technology">Introduction to MRDIMM Memory Technology > Lenovo Press</a></li>
<li><a href="https://www.notebookcheck.net/AMD-Zen-7-Florence-leak-teases-288-core-Epyc-chips-and-major-laptop-efficiency-gains.1276390.0.html">AMD Zen 7 'Florence' leak teases 288-core Epyc chips and ...</a></li>

</ul>
</details>

**标签**: `#AMD`, `#Server Processors`, `#CPU Roadmap`, `#AI Hardware`, `#Data Center`

---

<a id="item-11"></a>
## [Android 或将限制设备端 ADB 功能](https://kitsumed.github.io/blog/posts/android-may-soon-restrict-on-device-adb/) ⭐️ 8.0/10

据报道，Google 正在考虑限制设备端 Android Debug Bridge (ADB) 功能，这一潜在的改变在开发者中引发了广泛的讨论。 这一潜在的限制意义重大，因为 ADB 是 Android 开发者和高级用户的重要工具，将影响应用程序调试、系统访问以及整体平台控制和开发者自由。 提议的更改旨在通过可能将远程 ADB 访问限制到特定接口或 IP 地址来增强安全性，而不是完全禁用它，目前只有在明确启用开发者设置和远程 ADB 的情况下才可能被利用。

hackernews · shscs911 · 7月25日 06:57 · [社区讨论](https://news.ycombinator.com/item?id=49045159)

**背景**: Android Debug Bridge (ADB) 是 Android SDK 中包含的一个多功能命令行工具，允许开发者和高级用户与 Android 设备进行通信。它有助于执行各种操作，例如安装和调试应用程序、传输文件和运行 shell 命令，常用于开发和高级设备管理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.android.com/tools/adb">Android Debug Bridge (adb) | Android Studio | Android Developers</a></li>
<li><a href="https://www.howtogeek.com/125769/how-to-install-and-use-abd-the-android-debug-bridge-utility/">How to Install and Use ADB, the Android Debug Bridge Utility</a></li>

</ul>
</details>

**社区讨论**: 社区讨论显示出复杂的情绪，一些人质疑限制 ADB 的安全益处，考虑到其小众的攻击向量，并建议采用更精细的控制（如 IP 限制）而非全面禁止。另一些人则担心这是 Google 扩大平台控制的更广泛策略的一部分，可能会限制开发者的自由，并迫使他们依赖开发者接口来完成基本任务。

**标签**: `#Android Development`, `#Mobile Security`, `#Platform Control`, `#Developer Tools`, `#Operating Systems`

---

<a id="item-12"></a>
## [离网消息应用 Bitchat 现已托管于 Radicle](https://radicle.network/nodes/rosa.radicle.network/rad%3Az2v9tRJz1oknFAqCSY5W5c76nVvm6) ⭐️ 8.0/10

离网消息应用 Bitchat 现已成功托管于去中心化代码协作平台 Radicle，标志着其在一个基于 Git 构建的主权代码锻造平台上的存在。 这一进展凸显了开源项目去中心化基础设施的增长趋势，为中心化平台提供了替代方案，并促进了代码协作和通信的弹性。 社区反馈表明 Bitchat 当前的实际使用密度较低，并且面临技术挑战，例如对 `libs.gms.location` 的依赖阻碍了其在 F-Droid 上的可用性，引发了对其可访问性和真正去中心化的担忧。

hackernews · h1watt · 7月25日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=49047365)

**背景**: Bitchat 是由 Jack Dorsey 开发的一款点对点加密消息应用，旨在利用低功耗蓝牙网状网络在离网环境下运行，无需互联网或蜂窝服务。而 Radicle 是一个基于 Git 构建的去中心化开源代码协作平台，它允许开发者以点对点的方式托管和管理代码仓库，不受中心化控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://radicle.dev/">Radicle: the sovereign forge</a></li>
<li><a href="https://www.linkedin.com/pulse/what-bitchat-how-does-function-offline-orexisdigitalmarketing-1er3c">What is BitChat , and how does it function offline?</a></li>

</ul>
</details>

**社区讨论**: 社区讨论显示出复杂的情绪，一些用户赞扬 Radicle 的设计和 Bitchat 离网消息的独特体验，而另一些用户则对 Bitchat 实际使用密度低、技术依赖阻碍 F-Droid 可用性以及其项目归属提出了关键担忧。

**标签**: `#Decentralized Systems`, `#Peer-to-Peer`, `#Off-grid Communication`, `#Open Source`, `#Radicle`

---

<a id="item-13"></a>
## [Ruff v0.16.0 大幅增加默认代码检查规则，导致重大变更](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 8.0/10

Astral 于 7 月 23 日发布了 Ruff v0.16.0 版本，该版本将默认启用的代码检查规则数量从 59 条大幅增加到 413 条，这可能导致现有 Python 项目的持续集成（CI）检查失败。 此次更新对使用 Ruff 的 Python 开发者来说意义重大，因为它要求立即关注并更新配置以解决新发现的问题，从而避免 CI 失败，同时通过默认强制执行更多最佳实践来提高整体代码质量。 Ruff 中的规则总数已从 708 条增加到 968 条，许多新的默认规则能够捕获语法错误和即时运行时错误等严重问题；开发者可以使用 `uvx ruff@latest check . --fix --unsafe-fixes` 自动解决其中许多问题，并且人工智能代理也已成功用于升级。

rss · Simon Willison · 7月25日 22:44

**背景**: 代码检查（Code Linting）是一种静态代码分析过程，它在不运行应用程序的情况下，自动检查源代码是否存在风格不一致、潜在错误和常见错误。Ruff 是一款速度极快的 Python 代码检查器和格式化工具，它借鉴了 Flake8、Pyflakes 和 Black 等多种工具的经验，旨在提高代码质量和一致性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/astral-sh/ruff">GitHub - astral-sh/ruff: An extremely fast Python linter and ...</a></li>
<li><a href="https://docs.astral.sh/ruff/linter/">The Ruff Linter | Ruff - Astral</a></li>
<li><a href="https://startup-house.com/glossary/code-linting">What is Code Linting - Startup-House.com | Startup House</a></li>

</ul>
</details>

**标签**: `#Python`, `#Linting`, `#Code Quality`, `#Developer Tools`

---

<a id="item-14"></a>
## [Anthropic Claude Opus 5 模型显著增强抗提示注入能力](https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything) ⭐️ 8.0/10

Anthropic 的 Boris Cherny 宣布，其最新模型 Claude Opus 5 在抗提示注入方面表现出显著增强，成为该公司迄今为止最不易受提示注入攻击的模型。 这一进展对人工智能安全和鲁棒性至关重要，因为它解决了可能导致大型语言模型应用程序出现意外行为和安全风险的关键漏洞。 这种增强的抗性在提示注入评估（PI evals）和人工智能红队演练中均有体现，更多详细信息可在 Claude Opus 5 系统卡第 73 页查阅。

rss · Simon Willison · 7月25日 00:42

**背景**: 提示注入是一种漏洞，恶意用户输入可以覆盖大型语言模型（LLM）的原始指令，导致其以非预期或有害的方式运行。人工智能红队演练是一种积极的安全实践，通过模拟对人工智能模型的对抗性攻击，以在部署前识别并缓解潜在漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://genai.owasp.org/llmrisk/llm01-prompt-injection/">LLM01:2025 Prompt Injection - OWASP Gen AI Security Project</a></li>
<li><a href="https://grokipedia.com/page/ai-red-teaming">AI red teaming</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#LLM Security`, `#Prompt Injection`, `#Anthropic Claude`, `#Generative AI`

---

<a id="item-15"></a>
## [微软将利用 TPM 芯片打击盗版 Windows 激活](https://www.techspot.com/news/113232-microsoft-using-tpm-chips-crack-down-pirated-windows.html) ⭐️ 8.0/10

微软宣布为其密钥管理服务 (KMS) 引入强制性的基于 TPM 芯片的硬件安全验证，即“TPM 证明”机制，以在处理批量激活请求前验证 KMS 服务器的硬件身份。此功能将从下一版 Windows Server 起强制执行，并自 2026 年 8 月起在 Windows Server 2025 中推送准备提示。 此举标志着微软在打击 Windows 盗版方面的重大升级，旨在封堵长期被攻击者和盗版用户滥用的伪造 KMS 激活手段。这可能会对 Windows 激活漏洞生态系统产生重大影响，并可能使许多当前的盗版工具失效。 “TPM 证明”机制将专门确认 KMS 服务器的硬件身份已获得微软认证且未被篡改，从而阻止未经授权的服务器处理激活请求。尽管此举旨在打击像 Massgrave 的 Online KMS 这种需要每半年续期的激活方式，但该盗版组织也推出了 TSforge 方法，声称可以绕过微软整个 DRM 激活架构。

telegram · zaihuapd · 7月25日 15:55

**背景**: 密钥管理服务 (KMS) 是一种合法的批量许可激活方法，供大型组织在其网络内激活多个微软产品（如 Windows 和 Office），而无需单独的产品密钥。可信平台模块 (TPM) 是一种安全的加密处理器，用于存储加密密钥并保护硬件免受篡改，而 TPM 证明是 TPM 以加密方式向远程实体验证系统或密钥的完整性和身份的过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys">Key Management Services ( KMS ) client activation... | Microsoft Learn</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/component-updates/tpm-key-attestation">TPM Key Attestation | Microsoft Learn</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#Windows`, `#Security`, `#TPM`, `#Anti-Piracy`

---