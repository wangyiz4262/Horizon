---
layout: default
title: "Horizon Summary: 2026-08-24 (ZH)"
date: 2026-08-24
lang: zh
---

> 从 49 条内容中筛选出 10 条重要资讯。

---

**科技新闻**
1. [微软画图与照片为 AI 图片嵌入隐形 GUID 水印](#item-tech-news-1) ⭐️ 8.0/10
2. [整个旧金山变成网页游戏](#item-tech-news-2) ⭐️ 8.0/10
3. [seL4 在 AArch64 上完成安全证明](#item-tech-news-3) ⭐️ 8.0/10
4. [让你的可执行文件同时是 SQLite 数据库](#item-tech-news-4) ⭐️ 7.0/10
5. [Unbounded Labs 发布复古 LLM Bart](#item-tech-news-5) ⭐️ 7.0/10
6. [AI 作为空间软件生成器：可编程 3D 对象](#item-tech-news-6) ⭐️ 7.0/10
7. [小米发布三款玄戒芯片，O3 将首搭小米 18 Fold](#item-tech-news-7) ⭐️ 7.0/10
8. [字节合并 TRAE 与扣子入豆包，推统一办公品牌“豆包工作”](#item-tech-news-8) ⭐️ 7.0/10

**财经新闻**
1. [阿里巴巴 800 亿港元配售新股，港股股价大跌](#item-finance-news-1) ⭐️ 8.0/10
2. [Hugging Face 探索出售，潜在估值或达 130 亿美元](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [微软画图与照片为 AI 图片嵌入隐形 GUID 水印](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

微软画图（MS Paint）和照片（Photos）应用会在经 AI 编辑的图片中静默嵌入不可见的 GUID 水印，即使 AI 操作完全在本地完成并生成输出，用户也无法关闭这一隐形标识；官方提供了可关闭的可见水印选项，但隐形水印始终存在。该发现来自对微软工具的逆向工程，社区担心这一唯一标识可能被用于配合版权传票，将图片创作者与微软账户中的姓名、地址、邮箱、电话等个人信息关联，从而削弱互联网匿名性。另有用户报告水印可能被误触发，且微软此前在 Azure DevOps 提交上错误加盖 Copilot 标记，引发对其实现准确性的质疑。

hackernews · ComputerGuru · 8月24日 15:28 · [社区讨论](https://news.ycombinator.com/item?id=49421158)

**「背景」** 微软的画图（MS Paint）和照片（Photos）应用在 Copilot+ PC 上使用本地 Stable Diffusion 模型生成 AI 图像时，会先向 Microsoft Azure Front Door 端点发起一次强制性的远程内容审核请求，并从中获取一个服务器颁发的 16 字节 GUID。随后，这个 GUID 会被以不可见水印的形式嵌入到本地生成的图像像素中，整个过程在用户无感知的情况下静默完成。这项发现源于对应用行为的逆向工程分析，揭示了所谓“本地生成”的 AI 图像实际上仍包含与服务端关联的唯一标识符。

**「影响」** 使用微软画图或照片 AI 功能的用户，其本地生成或编辑的图片也会被嵌入不可见的 GUID 标识，且该标识无法关闭，可能被用于关联个人微软账户信息；具体触发范围（如是否仅限生成操作，还是也包括背景删除等编辑操作）尚不明确。

**「社区讨论」** 评论者普遍认为 AI 元素不是重点，真正的问题是微软在每张图片中秘密加入唯一标识，可能让版权传票轻易关联到用户真实身份；也有用户指出该功能存在误触发，并回顾微软曾在 Azure DevOps 提交上错误添加 Copilot 水印，因此对其实现准确性持怀疑态度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/">Microsoft Paint and Photos Embed Server-Issued GUIDs as ...</a></li>
<li><a href="https://mangodeveloper.com/articles/microsoft-paint-embeds-invisible-guid-watermarks-in-local-ai-images-via-remote-moderation-server">Microsoft Paint Embeds Invisible GUID Watermarks in Local AI ...</a></li>
<li><a href="https://news.linxi.com.au/news/microsoft-paint-and-photos-embed-server-issued-guids-in-local-ai-images">Microsoft Paint and Photos embed invisible GUID watermarks in ...</a></li>

</ul>
</details>

**标签**: `#privacy`, `#watermarking`, `#microsoft`, `#ai-image-editing`, `#reverse-engineering`

---

<a id="item-tech-news-2"></a>
### [整个旧金山变成网页游戏](https://sf.thijs.gg/) ⭐️ 8.0/10

Hacker News 上分享了一个名为 sf.thijs.gg 的网页游戏，它以可游玩的方式重现了旧金山全城，引发社区围绕 GIS 数据、程序化生成和用 LLM 生成资产的热烈讨论。玩家可以在类似 GTA 的环境中探索这座真实城市，一些前居民表示在虚拟漫游时产生了强烈的情感共鸣。该项目展示了借助现代工具（如 LLM）大幅降低 GIS 数据游戏开发门槛的可能性，不过官方缺乏深入的技术文档。社区成员也提到了类似项目（如费城的 City Rider）和更早的游戏（如 1989 年的 Vette）。

hackernews · centrosphere · 8月24日 17:05 · [社区讨论](https://news.ycombinator.com/item?id=49422784)

**「背景」** 这款名为《旧金山——游戏》的网页作品利用地理信息系统（GIS）数据（如建筑轮廓、高程和街道布局）在浏览器中实时重建了整座旧金山城，并通过程序化生成与流式加载实现可探索的 3D 城市。根据项目页面，游戏在浏览器中加载约 470 米的绘制距离，并流式加载城市街区，玩家可以传送、步行、奔跑和跳跃。这类项目通常依赖公开的 GIS 数据和低门槛的 AI 工具来辅助生成资产，从而大幅降低制作真实城市游戏场景的难度。

**「影响」** 该项目促使另一位开发者创建了类似的 GIS 城市游戏（费城的 City Rider），并让前旧金山居民在数字版熟悉地点中产生了强烈情感体验。

**「社区讨论」** 评论中有人分享了各自相似的项目（如费城的 City Rider），有人表达了对探索数字版旧金山的怀旧情感，还有人提出了构建从 GIS 和街景数据生成 GTA 风格城市管线的技术设想，并有人指出 1989 年的 Vette 等更早的先例。另有评论者询问页面底部的 Apple 版权与服务条款是否表明这是一个 Apple 产品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sf.thijs.gg/">San Francisco -- The Game</a></li>
<li><a href="https://progscrape.com/?search=sf.thijs.gg">progscrape: sf . thijs . gg</a></li>
<li><a href="https://dzen.ru/b/aoyhC-194WeQtImV">470 метров Сан-Франциско загружаются прямо в браузере San ...</a></li>

</ul>
</details>

**标签**: `#GIS`, `#game-development`, `#3D-mapping`, `#San-Francisco`, `#procedural-generation`

---

<a id="item-tech-news-3"></a>
### [seL4 在 AArch64 上完成安全证明](https://proofcraft.systems/news-2026/#2026-08-21) ⭐️ 8.0/10

seL4 微内核现已在 AArch64 架构上完成安全属性（如完整性与机密性）的形式化证明，这是 seL4 在高保障系统领域的一个重要里程碑。该证明目前仅覆盖单核（unicore）且非 MCS（混合关键性系统）的配置，尚不包含多核与 MCS 扩展。这意味着相关应用可以在 AArch64 上利用 seL4 的内核安全保证，但部署时需注意其适用范围。Proofcraft Systems 于 2026 年 8 月发布了这一消息，相关工作仍在持续扩展。

hackernews · snvzz · 8月24日 11:32 · [社区讨论](https://news.ycombinator.com/item?id=49418255)

**「背景」** seL4 是一个以形式化验证著称的微内核，其早期版本已在 32 位 Arm 和 x86 等架构上完成了功能正确性证明。本次公告标志着 seL4 在 AArch64（64 位 Arm）架构上的安全隔离证明也已正式完成，即证明了运行在其上的应用程序之间能够实现安全隔离，但该证明附带若干假设和限制条件（例如非 MCS 且单核）。

**「影响」** AArch64 上 seL4 的机密性证明现已完成，使得面向 ARMv8-A 的高可信系统开发者可以在单核、非 MCS 配置下获得经过形式化数学验证的内核机密性保证；但多核与混合关键性配置的同等保证仍待后续工作，且形式化验证带来的开发成本与改动速度影响仍是实际采用的重要考量。

**「社区讨论」** 评论中一些读者提醒称，这些安全证明并不涵盖时序侧信道攻击，另外也有人指出证明范围仅限于单核非 MCS。讨论还涉及哪些操作系统使用 seL4（例如 GenodeOS、LionsOS，以及一家中国汽车制造商将其用作汽车中的虚拟机监控程序），并有观点认为嵌入式与军工市场可能在可预见的未来继续资助该项目，但若想诚实地宣称其能力模型提升了系统安全性，仍需要原生的 seL4/Linux。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lists.sel4.systems/hyperkitty/list/announce@sel4.systems/thread/ZL6HYXH3PKI6XUVKMPTLIPKQMWJW7N7M/">seL 4 security proofs now complete on AArch 64 ... - lists. sel 4 .systems</a></li>
<li><a href="https://en.wikipedia.org/wiki/SeL4">seL4 - Wikipedia</a></li>
<li><a href="https://sel4.systems/">The seL4 Microkernel | seL4</a></li>

</ul>
</details>

**标签**: `#seL4`, `#formal verification`, `#AArch64`, `#security`, `#microkernel`

---

<a id="item-tech-news-4"></a>
### [让你的可执行文件同时是 SQLite 数据库](https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/) ⭐️ 7.0/10

Farid Zakaria 提出了一种 Linux 技巧，让 SQLite 数据库文件可以直接作为可执行二进制运行。其核心是将 SQLite 文件格式中第 68 字节处的 4 字节应用 ID（application ID）设为 SELF（Structured Executable &amp; Linkable Format），再把 ELF 可执行格式的各个组件组织到不同的 SQLite 表中。配套的 self-exec 解释器（C 代码）可以提取并执行这些组件。借助 Linux 的 binfmt\_misc 机制，可以注册一个模式，让内核在遇到匹配该二进制格式的文件时自动调用 self-exec；文中给出了在 NixOS 上使用该机制的示例，并提供了手动注册命令。这一设计实现了“同一个文件既是 SQLite 数据库又是 ELF 可执行程序”的效果。

rss · Simon Willison · 8月24日 11:38

**「背景」** ELF（Executable and Linkable Format）是 Linux 等系统上常见的可执行文件格式，而 SQLite 数据库文件在头部固定偏移处保存了一个应用 ID，通常用于标识文件类型。binfmt\_misc 是 Linux 内核提供的一种机制，允许通过文件内容模式将非原生格式的文件交给指定解释器执行，从而使任意文件只要匹配特定字节模式就能被当作可执行程序运行。

**「影响」** 这一技巧让 Linux 开发者和用户能够创建“既是可执行程序又是 SQLite 数据库”的单一文件，便于分发内嵌代码与数据的工具；不过实际使用需要先注册 binfmt\_misc 或显式调用 self-exec，因此兼容性和可移植性受限于系统配置。

**标签**: `#sqlite`, `#linux`, `#elf`, `#executables`, `#binfmt-misc`

---

<a id="item-tech-news-5"></a>
### [Unbounded Labs 发布复古 LLM Bart](https://www.reddit.com/r/MachineLearning/comments/1vx94er/bart_a_vintage_llm_r/) ⭐️ 7.0/10

Unbounded Labs 发布了 Bart，一个从零训练的 2.82B 参数“复古”大语言模型，训练数据为 20.1B 个 1931 年前英文 token，整个项目耗时约 3 个月、成本约 807 美元。团队公开了 Demo、技术文章、Hugging Face 权重、训练代码、评测与数据集，核心动机是回应 Demis Hassabis 提出的问题：LLM 是否可能独立得出过去伟大科学家的结论。为评估这类模型，他们创建了 Vintage CORE，首个包含 20 项复古 LLM 基准的评测套件，并称 Bart 在相同 token 预算下优于 GPT-1900。他们还把哈佛 Institutional Books 语料从 242B token 清洗到 23B token，并发布了约 416k 条基于 1930 年代前文本的 SFT 问答对；最终模型在一张 H100 上训练 5 天，平均保持约 60% MFU。文章还记录了数据清洗、基准构建、消融实验、训练和事后训练中的错误与教训，所有资源均开源。

reddit · r/MachineLearning · /u/soggydoggy8 · 8月24日 17:20

**「背景」** Demis Hassabis（Google DeepMind 联合创始人兼 CEO）曾提出一个有趣的 AGI 基准想法：如果让一个只接受 1911 年以前数据训练的 LLM 独立“重新发现”相对论，或许能检验模型是否具备真正的科学推理能力。Bart 项目正是这一思路的实践：它用 1931 年前的英语文本从头训练一个 2.82B 参数的模型，以考察 LLM 能否仅凭历史语料得出过去科学家曾得出的结论。

**「影响」** Bart 的发布为从事复古语料预训练、历史科学思想复现与 LLM 评测的研究者和开发者提供了可直接复用的 20 项基准、约 416k SFT 数据集、训练代码和模型权重，从而降低了该方向从头构建基础设施的门槛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Demis_Hassabis">Demis Hassabis - Wikipedia</a></li>
<li><a href="https://officechai.com/ai/someone-built-an-llm-to-test-out-demis-hassabis-agi-definition-of-pre-1900-science-discovering-relativity/">Someone Built An LLM To Test Out Demis Hassabis &#x27; AGI Definition...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#historical text`, `#training from scratch`, `#AI research`, `#open source`

---

<a id="item-tech-news-6"></a>
### [AI 作为空间软件生成器：可编程 3D 对象](https://www.reddit.com/r/MachineLearning/comments/1vxcc1h/r_using_ai_as_a_spatial_software_generator_to/) ⭐️ 7.0/10

论文共同作者发布了一项研究，展示利用大语言模型（LLM）通过空间编程生成 3D 对象，并提供了在线演示（nova3d.xyz）和开源代码仓库。与传统的单体网格（mesh）生成不同，这些 3D 对象以软件形式存在，从创建之初就具备可编程性、动画就绪能力，并能根据计算环境自动调整细节复杂度。作者还指出，这些对象可以在建模阶段就构建完整层级结构以及铰链/关节等机械连接。该方法在生成复杂有机形状方面仍落后于传统 AI 3D 生成器，但作者认为随着 LLM 空间编码能力提升，代码最终将覆盖所有 3D 内容，并可能颠覆工业设计、游戏开发、仿真和 AR/VR/XR 等行业。

reddit · r/MachineLearning · /u/mhb\_11 · 8月24日 19:10

**「背景」** 传统 AI 3D 生成器通常输出不可编辑的单体网格，难以直接用于动画或交互场景。空间编程则利用 LLM 生成描述 3D 对象结构和行为的程序代码，使对象由逻辑部件组成，而非单纯的几何形状。这种方法源于程序化生成（procedural generation）和 LLM 代码生成技术的结合。

**「影响」** 对于游戏开发、工业设计、仿真和 AR/VR/XR 的开发者而言，可编程 3D 对象有望减少动画绑定和适配成本，并支持自适应复杂度呈现；然而由于有机形态生成质量不足，短期内它难以替代传统 AI 生成器，实际采用可能仅限于机械结构或硬表面对象。

**标签**: `#3D generation`, `#LLMs`, `#spatial programming`, `#procedural generation`, `#computer graphics`

---

<a id="item-tech-news-7"></a>
### [小米发布三款玄戒芯片，O3 将首搭小米 18 Fold](https://mp.weixin.qq.com/s/ceIQbNnZrcNQqGywXCiXTQ) ⭐️ 7.0/10

小米发布新一代玄戒芯片，包括 AI 旗舰 SoC 玄戒 O3、高带宽 AI 加速芯片玄戒 O100，以及国内首款 3nm 智驾 AI 芯片玄戒 D100。玄戒 O3 采用十核全大核 CPU，多核跑分首破 15000 分，GPU 首发 G2-Ultra NX，性能提升 85%且功耗降低 64%，同时是全球首个支持 LPDDR6 的移动处理器，带宽 113.8GB/s，NPU 端侧 AI 性能提升 45%。玄戒 O100 采用行业首款 6nm 晶圆级垂直堆叠先进封装，通过 Hybrid Bonding 混合键合工艺实现 1.4 微米键合间距，提供 1.22TB/s 超高带宽（16 倍于传统旗舰手机），端侧推理速度最高可达 330TPS。玄戒 D100 集成 20 核 CPU 与 16 核 NPU，最高支持 160GB 统一内存，可本地部署 200B 参数量大模型，计划明年正式商用。三款芯片均完成回片验证，AI 旗舰 SoC 玄戒 O3 将首发搭载于小米 18 Fold，但这些性能指标尚未在真实设备上得到独立验证。

telegram · zaihuapd · 8月24日 07:18

**「背景」** 玄戒（Xuanjie/Xring）是小米自研芯片系列，此前小米曾推出澎湃（Surge）系列芯片，而此次发布的三款玄戒芯片旨在覆盖手机、汽车与智能家居等全生态的端侧 AI 算力需求。据外部报道，小米在芯片研发领域已投入超过 210 亿元人民币，并拥有近 3000 名相关研发人员；这三款芯片于 2026 年 8 月 24 日正式发布，均已完成回片验证，其中智驾芯片 D100 计划明年商用。

**「影响」** 如果官方数据可靠，小米手机用户与智驾车型将获得显著更高的端侧 AI 算力和内存带宽，开发者也能在小米生态中利用 LPDDR6 和超高带宽加速端侧推理；但这些宣称的性能仍需量产设备验证后才能确认实际影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kucoin.com/news/flash/xuanji-o3-o100-d100-chips-launched-by-xiaomi">Xiaomi Launches Xuanji O3, O100, and D100 Chips - KuCoin</a></li>
<li><a href="https://www.itbear.com/hardware/xiaomi-unveils-three-proprietary-chips-to-build-a-full-ecosystem-ai-computing-foundation/">Xiaomi Unveils Three Proprietary Chips to Build a Full ...</a></li>
<li><a href="https://cnevpost.com/2026/08/24/xiaomi-unveils-xring-d100-smart-driving-chip/">Xiaomi unveils 3-nm Xring D100 smart-driving chip, plans ...</a></li>

</ul>
</details>

**标签**: `#hardware`, `#AI chips`, `#Xiaomi`, `#SoC`, `#semiconductors`

---

<a id="item-tech-news-8"></a>
### [字节合并 TRAE 与扣子入豆包，推统一办公品牌“豆包工作”](https://mp.weixin.qq.com/s/ZgA2HZIgkNsE5HQkC40Sgw) ⭐️ 7.0/10

字节跳动完成办公 AI 产品团队整合，将 TRAE 和扣子（Coze）整体并入豆包体系，TRAE IDE 及 CLI 作为豆包旗下编程产品线继续发展，相关团队改向豆包产品负责人赵祺汇报。豆包最快本周内推出独立 AI 办公产品“豆包工作”，作为面向办公场景的统一产品与品牌，并与飞书深度整合。字节回应称，此次调整旨在协同产品和技术资源，现有用户权益不受影响。该消息由 36 氪报道。

telegram · zaihuapd · 8月24日 08:25

**「背景」** 字节跳动旗下豆包（Doubao）是其面向 AI 场景的统一品牌，此前已整合飞书产品团队；TRAE 是字节的 AI 编程平台，扣子（Coze）是智能体构建工具，两者并入豆包体系后，TRAE IDE 和 CLI 仍作为独立编程产品线保留。据外部报道，这一调整发生在 7 月 30 日飞书产品团队并入豆包的重组之后，原飞书“Aily 智能伙伴”也已更名为“豆包工作伙伴”。此次新推出的“豆包工作”是面向办公场景的统一 AI 产品与品牌，将与飞书深度整合，并提供超过 200 项技能。

**「影响」** 对使用 TRAE 和扣子的开发者而言，现有用户权益明确不受影响，但产品已划归豆包体系，团队汇报线转为豆包产品负责人，后续产品方向将与豆包和飞书深度绑定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aiweekly.co/node/10741">ByteDance Folds Trae and Coze Coding Tools Into Doubao, Preps ...</a></li>
<li><a href="https://eu.36kr.com/en/p/3953230805876099">Exclusive ByteDance AI Productivity Integration: TRAE &amp; Coze ...</a></li>
<li><a href="https://www.kucoin.com/news/flash/bytedance-integrates-trae-and-coze-into-doubao-launching-doubao-work">ByteDance integrates TRAE and Coze into DouBao ... - KuCoin</a></li>

</ul>
</details>

**标签**: `#ByteDance`, `#AI product`, `#office software`, `#TRAE`, `#Coze`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [阿里巴巴 800 亿港元配售新股，港股股价大跌](https://www.cnbc.com/2026/08/24/alibaba-share-placement-drop-ai-hong-kong.html) ⭐️ 8.0/10

阿里巴巴在香港以每股 112.7 港元配售 7.1 亿股新股，募资约 800 亿港元（102 亿美元），用于 AI 基础设施等投入；配售价较上周五收盘价 123 港元折让约 8.4%，港股周一盘中一度跌 10%。

rss · CNBC Finance · 8月24日 08:21

**「背景」** 阿里巴巴此前公布 6 月当季净利润同比跌 75%，同期资本开支同比增 75%至 677 亿元人民币；公司去年宣布未来三年拟投入至少 3800 亿元于云计算和 AI 基础设施。

**「影响」** 此次发行 7.1 亿股新股将稀释现有股东持股比例。

**标签**: `#Alibaba`, `#Share Placement`, `#AI Infrastructure`, `#Hong Kong Stocks`, `#Capital Expenditure`

---

<a id="item-finance-news-2"></a>
### [Hugging Face 探索出售，潜在估值或达 130 亿美元](https://www.bloomberg.com/news/articles/2026-08-23/hugging-face-gauging-interest-for-potential-sale-business-insider-says) ⭐️ 7.0/10

Hugging Face 正探索出售，据 Business Insider 援引知情人士，潜在估值或达 130 亿美元或更高；公司已与银行合作评估买家兴趣，目前尚未达成交易。该公司在 2023 年完成 2.35 亿美元融资后估值 45 亿美元。

telegram · zaihuapd · 8月24日 05:45

**「背景」** Hugging Face 是 AI 模型托管与协作平台，2023 年完成 2.35 亿美元 D 轮融资后估值达 45 亿美元，当年预估年度经常性收入约 7000 万美元，2024 年增至约 1.3 亿美元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://getlatka.com/companies/hugging-face">Hugging Face Revenue 2024: $130.1M Est. ARR, $4.5B Valuation</a></li>
<li><a href="https://sacra.com/c/hugging-face/">Hugging Face revenue, valuation &amp; funding | Sacra</a></li>

</ul>
</details>

**标签**: `#Hugging Face`, `#M&amp;A`, `#AI`, `#Valuation`, `#Funding`

---