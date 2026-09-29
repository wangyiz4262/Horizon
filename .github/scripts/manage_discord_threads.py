import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
CHANNEL_ID = os.environ.get("DISCORD_CHANNEL_ID")

if not BOT_TOKEN or not CHANNEL_ID:
    print("Error: DISCORD_BOT_TOKEN and DISCORD_CHANNEL_ID must be set in the environment.")
    sys.exit(1)

# Calculate Monday of the current UTC week
now = datetime.now(timezone.utc)
monday = now - timedelta(days=now.weekday())
start_date_str = monday.strftime("%Y-%m-%d")

target_thread_name = f"Weekly Summary - {start_date_str}"

headers = {
    "Authorization": f"Bot {BOT_TOKEN}",
    "Content-Type": "application/json",
    "User-Agent": "GitHub-Workflow-Discord-Thread-Manager/1.0",
}


def make_request(url: str, method: str = "GET", data: dict | None = None) -> dict:
    req = urllib.request.Request(url, headers=headers, method=method)
    if data is not None:
        req.data = json.dumps(data).encode("utf-8")
    try:
        with urllib.request.urlopen(req) as res:
            return json.loads(res.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"HTTP Error {e.code} for {method} {url}: {error_body}")
        raise e


def main() -> None:
    # 1. Fetch channel info to get guild_id
    channel_url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}"
    channel_info = make_request(channel_url)
    guild_id = channel_info.get("guild_id")
    if not guild_id:
        print(f"Error: Could not retrieve guild_id for channel {CHANNEL_ID}")
        sys.exit(1)

    # 2. Fetch active threads in the guild and filter by target channel
    active_threads_url = f"https://discord.com/api/v10/guilds/{guild_id}/threads/active"
    response = make_request(active_threads_url)
    all_active_threads = response.get("threads", [])
    threads = [t for t in all_active_threads if str(t.get("parent_id")) == str(CHANNEL_ID)]

    thread_id = None
    obsolete_threads = []

    for t in threads:
        name = t.get("name", "")
        if name == target_thread_name:
            thread_id = t.get("id")
        elif name.startswith("Weekly Summary - "):
            date_part = name.replace("Weekly Summary - ", "").strip()
            try:
                thread_start_date = datetime.strptime(date_part, "%Y-%m-%d").replace(tzinfo=timezone.utc).date()
                # Archive threads whose start date is at least 30 days old
                if (now.date() - thread_start_date).days >= 30:
                    obsolete_threads.append(t)
            except ValueError:
                pass

    # 3. Archive weekly threads that are at least 30 days old
    for old_thread in obsolete_threads:
        old_id = old_thread.get("id")
        old_name = old_thread.get("name")
        print(f"Archiving thread older than 30 days: '{old_name}' (ID: {old_id})")
        archive_url = f"https://discord.com/api/v10/channels/{old_id}"
        make_request(archive_url, method="PATCH", data={"archived": True})

    # 4. Create target thread if missing
    if not thread_id:
        print(f"Target thread '{target_thread_name}' not found. Creating thread...")
        create_url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/threads"
        payload = {
            "name": target_thread_name,
            "auto_archive_duration": 10080,  # 7 days in minutes
            "type": 11,  # GUILD_PUBLIC_THREAD
        }
        thread_obj = make_request(create_url, method="POST", data=payload)
        thread_id = thread_obj.get("id")
        print(f"Created thread: '{target_thread_name}' (ID: {thread_id})")
    else:
        print(f"Found existing active thread: '{target_thread_name}' (ID: {thread_id})")

    # 5. Export thread_id to GITHUB_OUTPUT
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a") as f:
            f.write(f"thread_id={thread_id}\n")
    else:
        print(f"GITHUB_OUTPUT not set. Resolved thread_id={thread_id}")


if __name__ == "__main__":
    main()
