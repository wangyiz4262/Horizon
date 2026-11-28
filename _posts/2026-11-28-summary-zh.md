---
layout: default
title: "Horizon Summary: 2026-11-28 (ZH)"
date: 2026-11-28
lang: zh
---

> 从 13 条内容中筛选出 6 条重要资讯。

---

**科技新闻**
1. [Google DeepCrossAttention 通过跨层注意力机制实现最高 3 倍提速](#item-tech-news-1) ⭐️ 8.0/10
2. [Unkernel：将真正的 Linux 内核编译为 WebAssembly](#item-tech-news-2) ⭐️ 8.0/10
3. [Carbon 仅凭单个提示在 103 分钟内生成 43 页数学证明](#item-tech-news-3) ⭐️ 8.0/10
4. [利用 WebRTC 的信用卡窃取脚本在热门购物网站被发现](#item-tech-news-4) ⭐️ 7.0/10
5. [Convex 技能在未明确告知用户的情况下将应用构思发送至远程服务器](#item-tech-news-5) ⭐️ 7.0/10
6. [前沿人工智能实验室的代码训练数据采购与排他协议市场](#item-tech-news-6) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Google DeepCrossAttention 通过跨层注意力机制实现最高 3 倍提速](https://research.google/blog/supercharging-transformer-residual-connections/) ⭐️ 8.0/10

Google 研究人员推出了 DeepCrossAttention（DCA）技术，通过在模型层深度方向应用注意力机制来替代传统的残差连接。该方法允许每个 Token 查询所有先前层嵌入的动态加权组合，在保持模型质量的同时，将训练和推理速度提升最多 3 倍。这项架构创新旨在解决传统 Transformer 模型在扩展注意力时面临的计算瓶颈。

hackernews · ComputedCamp995 · 11月27日 23:06 · [社区讨论](https://news.ycombinator.com/item?id=50672565)

**「背景」** 传统的 Transformer 模型通常依赖简单的残差连接（即直接将前几层的输出相加），但这可能会导致关键信息在深层传递时被稀释。

**「影响」** 开发人员和研究人员未来有望在训练和部署 Transformer 模型时获得显著的延迟降低和吞吐量提升，同时不牺牲模型质量。

**「社区讨论」** 评论者对这种深度交叉注意力机制表示了浓厚兴趣，讨论了它是否有助于解决大语言模型的某些长期痛点，并对这种底层架构改进能否带来亚秒级的实际 AI 交互延迟充满期待。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2502.06785">DeepCrossAttention : Supercharging Transformer Residual ...</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#machine learning`, `#transformers`, `#deep learning`, `#computer systems`

---

<a id="item-tech-news-2"></a>
### [Unkernel：将真正的 Linux 内核编译为 WebAssembly](https://unkernel.dev/) ⭐️ 8.0/10

Unkernel 成功将真正的 Linux 内核编译到了 WebAssembly，从而实现了极快的启动速度并在浏览器中直接运行 Linux 环境。该项目具备高性能的客户端环境（如在浏览器中直接运行 Wayland 合成器），为无需后端服务器基础设施的浏览器端 Linux 部署带来了新的可能。

hackernews · nreece · 11月28日 03:19 · [社区讨论](https://news.ycombinator.com/item?id=50674218)

**「背景」** WebAssembly（Wasm）是一项旨在让二进制代码在浏览器内以接近原生速度运行的开放标准。过去，在浏览器中模拟操作系统通常依赖于基于 JavaScript 的仿真器，其性能和启动速度受到较大限制。

**「社区讨论」** 评论者认为该项目启动速度极快且 Wayland 合成器性能惊人，还有人指出这能为教育平台提供极大的便利，让每个学生都能在浏览器中获得独立的 Linux 环境且无需服务器基础设施成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://unkernel.dev/">A real Linux kernel , compiled to WebAssembly . It boots to a shell in...</a></li>
<li><a href="https://github.com/pithings/unkernel">pithings/ unkernel : A real Linux kernel , compiled to WebAssembly .</a></li>

</ul>
</details>

**标签**: `#WebAssembly`, `#Linux Kernel`, `#Browser`, `#Systems Engineering`

---

<a id="item-tech-news-3"></a>
### [Carbon 仅凭单个提示在 103 分钟内生成 43 页数学证明](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&amp;mid=2652745576&amp;idx=3&amp;sn=a49245a39f77280484e491ad288684d2) ⭐️ 8.0/10

Carbon 系统仅凭单个提示词，在 103 分钟内成功生成了一份 43 页的数学证明，表现超越了此前未能攻克该题的 Astra 和 Fable 等系统。这一成果展示了自动化推理系统在处理复杂数学问题上的最新进展。

rss · 新智元 · 11月28日 04:06

**「背景」** 在概率论与统计物理的研究中，研究人员通常会面临复杂的数学猜想求解任务。在此之前，前沿 AI 模型 Astra 和 Fable 曾反复尝试求解相关猜想但未能成功。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geekfan.net/rgzn/1128339448.html">Astra、Fable轮番没拿下的题，Carbon一个提示，103分钟交出43页证明_...</a></li>

</ul>
</details>

**标签**: `#Artificial Intelligence`, `#Automated Reasoning`, `#Machine Learning`, `#Research`

---

<a id="item-tech-news-4"></a>
### [利用 WebRTC 的信用卡窃取脚本在热门购物网站被发现](https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer) ⭐️ 7.0/10

安全研究人员发现有信用卡窃取脚本利用 WebRTC 从热门购物网站外泄数据，以此规避传统的检测方法。这类新型网络威胁向量在购物旺季期间针对电子商务网站展开攻击。研究指出该方法通过不常被监控的技术来传输窃取的数据。

hackernews · scanr · 11月27日 15:40 · [社区讨论](https://news.ycombinator.com/item?id=50668145)

**「背景」** 网络安全中常见的信用卡窃取程序通常依赖传统的 HTTP 请求将窃取到的支付数据发送到远程服务器。WebRTC 是一项原本设计用于浏览器之间进行实时音视频通信的技术。

**「影响」** 在线零售商和使用第三方脚本的网站面临更隐蔽的数据窃取风险，传统的网络监控手段可能无法及时发现利用 WebRTC 进行的异常数据外传。

**「社区讨论」** 评论者指出，这种攻击并不是利用了 WebRTC 本身的漏洞，而是因为它较少受到恶意行为监控，并且主要针对移动设备以躲避检测。还有观点认为，根本问题在于允许第三方脚本在浏览器中运行以及现代网页架构的设计缺陷。

**标签**: `#cybersecurity`, `#webrtc`, `#web development`, `#threat intelligence`

---

<a id="item-tech-news-5"></a>
### [Convex 技能在未明确告知用户的情况下将应用构思发送至远程服务器](https://github.com/convex/convex-backend-skill/issues/64) ⭐️ 7.0/10

GitHub 上的一个公开问题和随后的讨论显示，Convex 的一项技能在未明确警告用户的情况下，将用户的应用程序构思发送到了远程服务器。该功能用于支持 Convex 的快速上手（quickstart）特性，这引发了社区对 AI 开发工具透明度和数据隐私的广泛关注。

hackernews · MickyTheMouse · 11月27日 18:02 · [社区讨论](https://news.ycombinator.com/item?id=50669765)

**「背景」** Convex 是一个用于构建和托管软件的完整平台，提供数据与代码存储服务以及供开发者使用的 AI 网关。随着第三方 AI 技能和插件在开发流程中的广泛应用，工具在本地与远程服务器之间传输数据的可见性成为了一个关键的信任问题。

**「社区讨论」** Convex 首席执行官 Jamie 现身说明该提示词上传用于“quickstart”功能，并提及此前已关闭端到端 vibe-coding 产品 Convex Chef。多位评论者指出，核心问题并非数据流向本身，而是开发者在不知情的情况下数据被发送出本地，呼吁为第三方技能引入类似移动应用的显式权限许可机制。

**标签**: `#artificial intelligence`, `#security`, `#software engineering`, `#developer tools`, `#privacy`

---

<a id="item-tech-news-6"></a>
### [前沿人工智能实验室的代码训练数据采购与排他协议市场](https://latent.space/p/ainews-inside-the-exploding-coding-data-market/) ⭐️ 7.0/10

前沿人工智能实验室正在构建专门的代码训练数据采购与管理市场，以提升模型编程能力。G2i 创始人 Gabe Greenberg 在 AI Engineer CODE 会议上透露，实验室在采购数据时需要在独占权限和价格折扣之间做出选择：支付更高费用以获取独占训练数据，或者接受与其他实验室共享数据的折扣方案。这些采购通常从小型试点订单开始，并根据效果逐步扩大规模。

rss · Latent Space · 11月28日 03:45

**「背景」** 随着大语言模型在软件工程领域的应用日益深入，高质量的代码训练数据已成为决定模型性能的核心资产。各大人工智能实验室为了在代码生成和理解能力上取得优势，持续在数据采集、清洗和版权采购方面投入大量资源。

**标签**: `#artificial intelligence`, `#machine learning`, `#data market`, `#software engineering`

---