---
layout: default
title: "Horizon Summary: 2026-09-30 (ZH)"
date: 2026-09-30
lang: zh
---

> 从 39 条内容中筛选出 18 条重要资讯。

---

**科技新闻**
1. [OpenAI 推出 GPT-6.1 Sol 模型，提供接近 Astra 的性能与更低价格](#item-tech-news-1) ⭐️ 8.0/10
2. [发布免费开源书籍《如何让你的模型跑得更快》](#item-tech-news-2) ⭐️ 8.0/10
3. [CoWindow 和 MassAlloc 注意力机制减少长上下文模型的计算冗余](#item-tech-news-3) ⭐️ 8.0/10
4. [德里如何将电力损耗从 50% 降至 5%](#item-tech-news-4) ⭐️ 7.0/10
5. [PS5 Relapse 漏洞利用引发关于 WebKit 与安全性的讨论](#item-tech-news-5) ⭐️ 7.0/10

**财经新闻**
1. [中国警告若欧盟实施贸易限制将坚决反击](#item-finance-news-1) ⭐️ 8.0/10
2. [高盛面临高层接班难题](#item-finance-news-2) ⭐️ 7.0/10
3. [盘前多只股票大幅波动](#item-finance-news-3) ⭐️ 7.0/10
4. [特朗普市政债券组合规模增至高达 10 亿美元](#item-finance-news-4) ⭐️ 7.0/10
5. [中国对人形机器人企业上市提出三项新标准](#item-finance-news-5) ⭐️ 7.0/10

**AI 创作者雷达**
1. [使用云端大模型做规划搭配本地 27B 模型写代码的成本实践](#item-ai-creator-1) ⭐️ 7.0/10
2. [Reddit 用户展示基于推测性工具的形变物理模拟](#item-ai-creator-2) ⭐️ 2.0/10
3. [OpenAI 价格调整传闻](#item-ai-creator-3) ⭐️ 1.0/10
4. [ChatGPT 信用分数提升讨论](#item-ai-creator-4) ⭐️ 1.0/10
5. [Reddit 用户分享关于 ChatGPT Plus 与 Claude Pro 的订阅额度与速度对比测试](#item-ai-creator-5) ⭐️ 1.0/10
6. [无效的 Reddit 帖子](#item-ai-creator-6) ⭐️ 0.0/10
7. [网传 GPT-6.1 Sol 将于今日发布](#item-ai-creator-7) ⭐️ 0.0/10
8. [空洞的 AGI 讨论贴](#item-ai-creator-8) ⭐️ 0.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenAI 推出 GPT-6.1 Sol 模型，提供接近 Astra 的性能与更低价格](https://openai.com/index/introducing-gpt-6-1-sol/) ⭐️ 8.0/10

OpenAI 推出了 GPT-6.1 Sol 模型，其定位为以五分之一的价格提供接近 Astra 级别的智能。该版本显著降低了缓存输入成本，旨在通过大幅削减的费用提升模型的性价比。

hackernews · crorella · 9月29日 17:06 · [社区讨论](https://news.ycombinator.com/item?id=49896586)

**「背景」** 在此之前，OpenAI 曾发布 GPT-6 相关的 Sol 系列模型，但近期版本在实际应用中曾因性能表现和某些回归问题遭到用户的广泛讨论与批评。

**「社区讨论」** 社区用户指出，缓存输入成本降至每百万 token 0.10 美元是本次更新的真正亮点，这将显著降低开发和使用成本。不过，部分用户对 OpenAI 此前的版本迭代表示失望，并对降价竞争背后引发的行业趋势保持审慎态度。

**标签**: `#artificial intelligence`, `#machine learning`, `#large language models`, `#openai`

---

<a id="item-tech-news-2"></a>
### [发布免费开源书籍《如何让你的模型跑得更快》](https://www.reddit.com/r/MachineLearning/comments/1wt6ns4/i_wrote_a_free_opensource_book_on_making_ml/) ⭐️ 8.0/10

作者 Usamah Z. 发布了一本名为《如何让你的模型跑得更快：高效机器学习的系统视角，从硅片到智能体》（How to Make Your Model Fast: A Systems View of Efficient Machine Learning, from Silicon to Agents）的免费开源书籍。该书采用系统工程视角，内容涵盖屋顶线模型分析、硬件、算子、编译器、量化、剪枝、视觉、端侧大语言模型、机器人、性能分析、模型服务及智能体。读者现可通过 GitHub 免费访问该书源码与内容。

reddit · r/MachineLearning · /u/SoloTiger\_ · 9月29日 10:35

**「背景」** 机器学习性能工程通常需要跨越硬件架构与软件算法之间的鸿沟，传统上开发人员往往仅关注减少浮点运算次数（FLOPs），而忽视了硬件带宽、内存及系统瓶颈对实际运行速度的制约。

**「影响」** 从事机器学习系统、模型推理、编译器、边缘人工智能及性能工程的开发者与工程师，现在可以免费获取这本开源参考书，以提升对模型硬件匹配度与系统级优化的判断能力。

**标签**: `#machine learning`, `#performance engineering`, `#hardware`, `#open source`, `#systems`

---

<a id="item-tech-news-3"></a>
### [CoWindow 和 MassAlloc 注意力机制减少长上下文模型的计算冗余](https://www.reddit.com/r/MachineLearning/comments/1wt1gbk/cowindow_and_massalloc_attention_collective/) ⭐️ 8.0/10

研究人员推出了 CoWindow 注意力（CoWA）和 MassAlloc 注意力（MALA）两种旨在减少长上下文 Transformer 模型中计算冗余的新方法，支持训练前向与反向传播以及推理的 Prefill 与 Decoding 阶段。CoWA 将远距离上下文分布在各个 KV 头中并共享局部与前缀汇聚窗口，在无需学习型路由器的前提下实现全因果历史覆盖；MALA 则利用 softmax 统计信息决定是否对分块执行后续计算。在 8 个 H100 GPU、TP=8、上下文长度为 128K 的测试中，相较于 FullAttn，CoWA 的注意力算子在前向、反向和解码阶段分别实现 7.4 倍、8.6 倍和 3.0 倍的加速，MALA 分别实现 2.2 倍、3.0 倍和 1.6 倍的加速。在 14B 模型、32K 上下文的持续训练中，CoWA 和 MALA 的总训练 FLOPs 分别减少了 28.5% 和 23.1%，且模型能力与 FullAttn 相当。

reddit · r/MachineLearning · /u/BitExternal4608 · 9月29日 05:16

**「背景」** 在处理长上下文时，传统的 Transformer 注意力机制随着序列长度的增加会带来显著的计算和内存开销，从而在训练和推理过程中产生大量的计算冗余。

**标签**: `#attention mechanisms`, `#long-context models`, `#machine learning research`, `#transformer optimization`, `#hardware efficiency`

---

<a id="item-tech-news-4"></a>
### [德里如何将电力损耗从 50% 降至 5%](https://spectrum.ieee.org/delhi-electricity-loss) ⭐️ 7.0/10

德里成功将电力传输与盗窃造成的损耗从 50% 大幅降低至 5%。这一成效不仅减少了技术和非技术性损耗，还解决了长期存在的严重偷电和电网管理问题。

hackernews · rbanffy · 9月29日 12:43 · [社区讨论](https://news.ycombinator.com/item?id=49892245)

**「背景」** 在 2002 年时，德里的电网由于严重的电力窃取和老旧的基建问题，损失了超过一半的电力供应。

**「社区讨论」** 评论者指出，除了减少电力损耗，消除频繁的无计划停电（拉闸限电）同样是一项革命性的改变。此外，有用户分享了为防止偷电而对电线进行绝缘改造的意外副作用，这反而使猴群更容易利用电线在街区和高层建筑间移动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.lavx.hu/article/how-delhi-cut-electricity-losses-from-50-to-5">How Delhi Cut Electricity Losses from 50% to 5% | LavX News</a></li>

</ul>
</details>

**标签**: `#infrastructure`, `#energy`, `#power systems`, `#grid management`

---

<a id="item-tech-news-5"></a>
### [PS5 Relapse 漏洞利用引发关于 WebKit 与安全性的讨论](https://github.com/ntfargo/Relapse-Exploit) ⭐️ 7.0/10

一个名为 Relapse 的 PlayStation 5 漏洞利用项目近期被公开分享，其核心是利用了 WebKit JavaScriptCore 中的潜在漏洞。该漏洞的出现引发了开发者和安全社区的技术讨论，焦点集中在控制台的攻击面以及索尼后续可能采取的防御措施上。

hackernews · therepanic · 9月29日 15:44 · [社区讨论](https://news.ycombinator.com/item?id=49895304)

**「背景」** 游戏主机通常依赖多层安全架构来阻止未授权代码的执行，而诸如 WebKit 等浏览器组件长期以来一直是各类设备获取初始代码执行权限的常见攻击目标。

**「影响」** 安全研究人员和开发者正在评估该漏洞对现有固件版本的潜在威胁，同时社区也在探讨索尼是否会通过禁用 JIT 等方式来缩小攻击面。

**「社区讨论」** 社区评论主要围绕该漏洞是否利用了 WebKit 的 JavaScriptCore 引擎展开，部分用户还对存档备份限制、游戏运行可能性以及未来可能出现的漏洞储备进行了讨论。

**标签**: `#security`, `#exploit`, `#hardware`, `#software engineering`, `#gaming`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [中国警告若欧盟实施贸易限制将坚决反击](https://www.cnbc.com/2026/09/30/china-warns-europe-increases-trade-pressure.html) ⭐️ 8.0/10

中国商务部在周二的一份声明中警告称，如果欧盟在贸易谈判期间对中国企业或产品实施限制，中国将采取坚决措施予以回应。

rss · CNBC Finance · 9月30日 02:49

**「背景」** 由于欧盟希望缩小对华创纪录的贸易逆差，双方今年夏季一直在进行贸易谈判，欧盟贸易专员预计将于下周访问北京。

**标签**: `#International Trade`, `#EU-China Relations`, `#Economic Policy`, `#Tariffs`, `#Global Economy`

---

<a id="item-finance-news-2"></a>
### [高盛面临高层接班难题](https://www.cnbc.com/2026/09/29/goldman-sachs-ceo-succession-planning.html) ⭐️ 7.0/10

据报道，高盛董事会正讨论最早于明年由总裁约翰·沃尔德伦接替现年 64 岁的首席执行官大卫·所罗门，但这一计划因所罗门的影响力及其强劲业绩而面临不确定性。

rss · CNBC Finance · 9月29日 20:50

**「背景」** 在大卫·所罗门自 2018 年担任首席执行官期间，高盛股价累计上涨超过 300%，并在近期受益于并购交易的回暖和人工智能热潮。

**标签**: `#Banking`, `#Corporate Governance`, `#Executive Succession`, `#Goldman Sachs`

---

<a id="item-finance-news-3"></a>
### [盘前多只股票大幅波动](https://www.cnbc.com/2026/09/29/stocks-making-the-biggest-moves-premarket-fair-isaac-spacex-amd-more.html) ⭐️ 7.0/10

费科公司（Fair Isaac）股价在盘前交易中暴跌 18%，此前美国联邦住房金融局局长比尔·普尔特宣布合并抵押贷款定价网格。同时，二手车零售商卡车斯（CarMax）第二季度每股收益达到 1.16 美元，营收为 7.88 亿元，均好于 FactSet 调查的分析师预期。

rss · CNBC Finance · 9月29日 12:03

**「背景介绍」** 在此之前，美国抵押贷款机构使用两套独立的定价网格来评估贷款风险。

**「市场影响」** 抵押贷款定价政策的变化直接影响了购房者以及相关金融服务企业的业务成本。

**标签**: `#Stocks`, `#Acquisitions`, `#Earnings`, `#Mortgage Policy`, `#Investments`

---

<a id="item-finance-news-4"></a>
### [特朗普市政债券组合规模增至高达 10 亿美元](https://www.cnbc.com/2026/09/29/trump-municipal-bond-portfolio.html) ⭐️ 7.0/10

据 CNBC 财务分析显示，美国总统唐纳德·特朗普的市政债券组合在 2025 年底至 2026 年期间增长至超过 1000 个头寸，估值在 3 亿美元至 10 亿美元之间，引发了外界对其个人投资与行政决策之间潜在政策重合的关注。CNBC 的报道指出，目前尚无证据表明特朗普及其投资管理人利用内幕信息进行交易。

rss · CNBC Finance · 9月29日 14:37

**「背景」** 市政债券是由城市、学校和公用事业等公共机构发行的债务工具。由于美国总统豁免于常规的利益冲突法律，特朗普的这些投资由独立金融机构在全权委托账户中进行管理，白宫和特朗普组织均表示相关人员无法直接干预投资决策。

**标签**: `#Municipal Bonds`, `#Conflicts of Interest`, `#White House`, `#Federal Policy`, `#Personal Finance`

---

<a id="item-finance-news-5"></a>
### [中国对人形机器人企业上市提出三项新标准](https://www.cnbc.com/2026/09/29/china-criteria-humanoid-robot-ipos.html) ⭐️ 7.0/10

中国证券监督管理机构对人形机器人初创企业的首次公开募股（IPO）提出了三项新标准，要求申请企业具备可持续收入、亏损收窄并拥有核心技术，此举可能将大多数拟上市企业挡在门外。

rss · CNBC Finance · 9月30日 02:50

**「背景介绍」** 此前，中国的人形机器人及具身智能（指将人工智能技术赋予实体机器以感知和行动能力）行业迎来了资金的大幅涌入，但市场对行业估值泡沫的担忧也随之加剧。

**「市场影响」** 更严格的监管标准预计将使大批寻求上市的人形机器人初创企业面临融资受阻，并促使投资者重新评估该板块过高的估值。

**标签**: `#Regulation`, `#IPO`, `#Robotics`, `#China`, `#Artificial Intelligence`

---

## AI 创作者雷达

<a id="item-ai-creator-1"></a>
### [使用云端大模型做规划搭配本地 27B 模型写代码的成本实践](https://www.reddit.com/r/ChatGPT/comments/1wtqp7l/using_gpt61_sol_only_as_the_planner_and_letting_a/) ⭐️ 7.0/10

有一位开发者在 2026 年 9 月 30 日分享了一项关于 AI 编程工作流的实验，测试了仅使用 Sol 6.1 模型、由 Sol 6.1 做规划加本地 Qwen 3.8 27B 模型写代码、以及仅使用本地模型三种方案开发三个小型 3D 游戏的表现。结果显示，将 Sol 6.1 仅作为架构师和规划师、本地 27B 模型负责写代码，能将 API 总费用从单独使用 Sol 的 0.75 美元降至 0.17 美元，降幅达到 77%。不过，该方案的总耗时从 6.6 分钟增加到了 43.4 分钟，且作者指出这仅代表 API 花费，未计入本地 RTX 3090 GPU 的电费成本。

reddit · r/ChatGPT · /u/GapNew4766 · 9月30日 00:22

**「当下价值」** 随着 Sol 6.1 模型的发布，开发者开始探讨在新型主模型下，“规划与编辑分离”的架构是否仍然具备成本优势。该实验为关注 AI 辅助编程和 API 成本控制的开发者提供了具体的实测数据与工作流参考。

**「内容切入」** 可做角度：从云端规划模型搭配本地编辑模型的 AI 编程工作流切入，探讨在牺牲一定开发速度的前提下，通过架构拆分来降低 API 费用的实际效果与局限性。

**标签**: `#AI编程`, `#工作流优化`, `#本地大模型`, `#成本控制`

---

<a id="item-ai-creator-2"></a>
### [Reddit 用户展示基于推测性工具的形变物理模拟](https://www.reddit.com/r/ChatGPT/comments/1wtq7rj/how_to_create_deformable_simulation_objects_with/) ⭐️ 2.0/10

一篇 Reddit 帖子讨论了使用被称为 GPT-6 Astra 和 RobotGym 的工具来创建可形变的物理模拟对象，展示了机器人挤压塑料水瓶的场景。帖文中提到使用了带有特定刚度和屈服强度的 PET 外壳材质参数，以及基于 GPU 的求解器来模拟塑性形变和流体粒子。由于涉及未发布或虚构的技术版本与工具，其实际背景和可验证性存疑。

reddit · r/ChatGPT · /u/rocky\_mountain12 · 9月30日 00:00

**「内容角度」** 可做角度：探讨 AI 社区中如何利用高级物理引擎与自研模拟参数来模拟复杂的机器人抓取与形变物体交互场景。

**标签**: `#Robot Simulation`, `#Physics Engine`, `#Speculation`, `#Reddit`

---

<a id="item-ai-creator-3"></a>
### [OpenAI 价格调整传闻](https://www.reddit.com/r/ChatGPT/comments/1wthna3/openai_just_launched_a_500month_plan_and_cut_the/) ⭐️ 1.0/10

有 Reddit 用户发帖称 OpenAI 推出了每月 500 美元的新订阅档位，并称 200 美元的 Pro 计划使用额度被减半。该说法目前仅来源于社交媒体讨论，缺乏官方公告或可靠信源证实。

reddit · r/ChatGPT · /u/Different-Mess4248 · 9月29日 18:14

**「内容切入」** 可做角度：梳理近期社交媒体上关于 AI 大模型订阅价格分层与使用额度变动的传闻，探讨高价专业版对重度开发者的实际影响及市场对阶梯定价的反应。

**标签**: `#OpenAI`, `#Pricing`, `#Rumor`, `#Reddit`

---

<a id="item-ai-creator-4"></a>
### [ChatGPT 信用分数提升讨论](https://www.reddit.com/r/ChatGPT/comments/1wtfdre/chatgpt_hidden_capabilities/) ⭐️ 1.0/10

一名 Reddit 用户发帖称，通过遵循 ChatGPT 的步骤、寄送信件并花费约 50 美元，其个人信用分数从 540 分提升至 704 分。该内容为用户的个人非正式经验分享，未提供具体的操作细节或官方功能证明。

reddit · r/ChatGPT · /u/CantStopRedPilling · 9月29日 16:50

**「内容切入」** 可做角度：梳理社群中关于利用 AI 辅助处理个人事务的讨论现状，并探讨此类个人经验分享的可信度与局限性。

**标签**: `#ChatGPT`, `#社群讨论`, `#个人经验`, `#噪音`

---

<a id="item-ai-creator-5"></a>
### [Reddit 用户分享关于 ChatGPT Plus 与 Claude Pro 的订阅额度与速度对比测试](https://www.reddit.com/r/ChatGPT/comments/1wtngdp/chatgpt_plus_20_vs_claude_pro_20_battle_is_gpt61/) ⭐️ 1.0/10

一名 Reddit 用户在 Hermes Agent 中对特定模型版本进行了 16 项固定任务的测试，对比 ChatGPT Plus 与 Claude Pro 在相同工作负载下的订阅额度消耗与运行速度。测试结果显示，在同等测试条件下，测试对象在 Codex 5 小时窗口中的消耗略高于 Claude 窗口，且 Claude 在运行速度上快 2.5 至 6 倍。该用户表示将保留 Claude Pro 并考虑取消 ChatGPT Plus 订阅。材料中涉及的模型版本与实际不符，存在虚构模型的可能性。

reddit · r/ChatGPT · /u/Background-Web-6312 · 9月29日 21:58

**「为什么值得关注」** 该测试尝试通过量化额度消耗和延迟来评估不同付费 AI 订阅的实际性价比，为预算有限的用户提供了一种可供参考的横向基准测试方法。不过，由于测试基于单账户、单次会话以及存在争议的模型命名，其实际普适性仍受到限制。

**「内容切入角度」** 可做角度：从个人用户的测试方法切入，探讨如何在实际的多模型工作流中评估订阅额度的性价比与任务执行效率。

**标签**: `#ChatGPT`, `#Claude`, `#Reddit`, `#AI Models`

---

<a id="item-ai-creator-6"></a>
### [无效的 Reddit 帖子](https://www.reddit.com/r/ChatGPT/comments/1wtqzq2/the_premium_experience/) ⭐️ 0.0/10

Reddit 上出现了一篇由用户/u/albanianspy 发布、题为“The premium experience”的帖子。经分析，该内容为空白提交占位符，未提供任何可验证的信息、事实细节或 AI 相关内容。受影响的人或场景暂不明确。

reddit · r/ChatGPT · /u/albanianspy · 9月30日 00:36

**标签**: `#reddit`, `#noise`, `#empty-content`

---

<a id="item-ai-creator-7"></a>
### [网传 GPT-6.1 Sol 将于今日发布](https://www.reddit.com/r/ChatGPT/comments/1wtgers/gpt61_sol_will_release_today/) ⭐️ 0.0/10

Reddit 上出现一则未经证实的传言，称 OpenAI 将于今日发布名为“GPT-6.1 Sol”的新模型。该材料缺乏官方公告或可靠来源支持。目前这仅属于网络猜测。

reddit · r/ChatGPT · /u/Vagottszemu · 9月29日 17:28

**「内容切入角度」** 可做角度：梳理近期关于 OpenAI 命名与发布传闻的现象，探讨社区对不存在版本的预测心理。

**标签**: `#Rumor`, `#OpenAI`, `#Noise`, `#Unverified`

---

<a id="item-ai-creator-8"></a>
### [空洞的 AGI 讨论贴](https://www.reddit.com/r/ChatGPT/comments/1wtey0w/ultimate_form_of_next_gen_agi/) ⭐️ 0.0/10

Reddit 上出现了一篇题为“Ultimate form of NEXT GEN AGI”的帖子，但该帖内容为空，未提供任何实质性细节、讨论价值或可验证的信息。受影响的场景为相关的在线社区讨论。

reddit · r/ChatGPT · /u/Informal-Device-8511 · 9月29日 16:34

**「内容切入角度」** 可做角度：分析当前网络社区中关于“下一代 AGI”的空洞讨论现象，探讨如何识别和过滤低质量信息。

**标签**: `#noise`, `#reddit`, `#unsubstantiated`

---