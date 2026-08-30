from pathlib import Path

import feedparser


FEED_URL = "https://honeyinfo7.tistory.com/rss"
README_PATH = Path(__file__).with_name("README.md")
START_MARKER = "<!-- BLOG-POST-LIST:START -->"
END_MARKER = "<!-- BLOG-POST-LIST:END -->"
MAX_POSTS = 7


def render_posts() -> str:
    feed = feedparser.parse(FEED_URL)
    posts = []

    for entry in feed.entries[:MAX_POSTS]:
        title = entry.get("title", "Untitled").replace("[", "\\[").replace("]", "\\]")
        link = entry.get("link", "#")
        posts.append(f"- [{title}]({link})")

    return "\n".join(posts) if posts else "_No recent posts available._"


def update_readme() -> None:
    readme = README_PATH.read_text(encoding="utf-8")

    if START_MARKER not in readme or END_MARKER not in readme:
        raise RuntimeError("README blog post markers are missing")

    before, remainder = readme.split(START_MARKER, maxsplit=1)
    _, after = remainder.split(END_MARKER, maxsplit=1)
    updated = f"{before}{START_MARKER}\n{render_posts()}\n{END_MARKER}{after}"
    README_PATH.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    update_readme()
