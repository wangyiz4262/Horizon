<div align="center">
<h1>🌅 Horizon</h1>

<p><strong>Enjoy the News itself. Leave others to Horizon</strong></p>

📡 Your own AI-powered news radar. Generates daily briefings in English & Chinese. | 构建你专属的 AI 新闻雷达

[📖 Live Demo](https://horizon.pages.wangyizhe.net/) · [📋 Configuration Guide](https://thysrael.github.io/Horizon/configuration) · [Docs](https://www.horizon1123.top/)

</div>

## Supported Sources

| Source          | What it fetches                              | Comments             |
| --------------- | -------------------------------------------- | -------------------- |
| **Hacker News** | Top stories by score                         | Yes (top N comments) |
| **RSS / Atom**  | Any RSS or Atom feed                         | —                    |
| **Reddit**      | Subreddits + user posts                      | Yes (top N comments) |
| **Telegram**    | Public channel messages                      | —                    |
| **Twitter / X** | User timelines + keyword searches (Apify)    | Yes (top N replies)  |
| **GitHub**      | User events & repo releases                  | —                    |
| **OpenBB**      | Financial company news by watchlist/provider | —                    |
| **OSS Insight** | Trending open-source repositories            | —                    |
| **GDELT**       | News matching a search query                 | —                    |
| **Google News** | News search via RSS                          | —                    |

## Where Your Briefing Goes

Horizon can publish or deliver the generated briefing in several ways:

| Channel                     | What it does                                                                                               |
| --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **GitHub Pages Daily Site** | Copies generated Markdown into `docs/` so GitHub Pages can publish a daily-updated briefing site           |
| **Email Subscription**      | Sends the daily briefing to subscribers and handles subscribe/unsubscribe requests through SMTP/IMAP       |
| **Webhook Notification**    | Pushes success or failure results to Feishu/Lark, DingTalk, Slack, Discord, or any custom webhook endpoint |
| **WeChat Notification**     | Sends briefings through iLink Bot after QR login and a message from you; WeChat reply limits apply         |

For delivery setup, see the [Configuration Guide](docs/configuration.md). To run pipeline stages from an AI assistant, use the **MCP Server**: [tools](src/mcp/README.md) · [client setup](src/mcp/integration.md).
