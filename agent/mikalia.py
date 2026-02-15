"""
Mikalia — Autonomous AI Agent for Mikata AI
============================================
Generates bilingual blog posts (EN/ES) using Claude API,
formats them for Hugo, and publishes to GitHub Pages.

Usage:
    python mikalia.py "Topic or prompt for the post"
    python mikalia.py --interactive
"""

import argparse
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import anthropic
from dotenv import load_dotenv

# Paths
AGENT_DIR = Path(__file__).parent
PROJECT_ROOT = AGENT_DIR.parent
CONTENT_DIR = PROJECT_ROOT / "content" / "blog"
MIKALIA_PROMPT = PROJECT_ROOT / "MIKALIA.md"

# Load environment
load_dotenv(AGENT_DIR / ".env")


def load_system_prompt():
    """Load MIKALIA.md as the system prompt."""
    if not MIKALIA_PROMPT.exists():
        print("Error: MIKALIA.md not found at project root.")
        sys.exit(1)
    return MIKALIA_PROMPT.read_text(encoding="utf-8")


def slugify(title: str) -> str:
    """Convert a title to a URL-friendly slug."""
    slug = title.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def generate_post(client: anthropic.Anthropic, system_prompt: str, topic: str) -> dict:
    """Generate a blog post in English using Claude."""
    user_prompt = f"""Write a blog post about the following topic:

"{topic}"

Follow your content structure guidelines from your system prompt exactly:
1. Title — Clear, engaging, not clickbait
2. Hook — Opening paragraph that grabs attention (2-3 sentences)
3. Body — Well-structured content with headers and examples
4. Opinion — Your personal take (remember: 力 Chikara, be bold)
5. Takeaway — What the reader should remember or do next
6. Signature — *Stay curious~ ✨* — **Mikalia**

IMPORTANT FORMAT RULES:
- Respond ONLY with the blog post content in Markdown
- Do NOT include Hugo front matter (I'll add that separately)
- Start directly with the first ## heading (the hook)
- Use ## for main sections and ### for subsections
- Aim for 800-1500 words (standard post length)
- End with your signature block
"""

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=4000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
    )

    content = response.content[0].text

    # Generate title separately for clean front matter
    title_response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=100,
        system="You generate concise blog post titles. Respond with ONLY the title, nothing else. No quotes.",
        messages=[
            {
                "role": "user",
                "content": f"Generate a clear, engaging title for a blog post about: {topic}",
            }
        ],
    )
    title = title_response.content[0].text.strip().strip('"').strip("'")

    # Generate description
    desc_response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=200,
        system="You generate SEO-friendly blog post descriptions. Respond with ONLY the description (1-2 sentences), nothing else.",
        messages=[
            {
                "role": "user",
                "content": f"Generate a brief description for a blog post titled '{title}' about: {topic}",
            }
        ],
    )
    description = desc_response.content[0].text.strip()

    # Generate tags
    tags_response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=100,
        system='You generate relevant blog tags. Respond with ONLY a comma-separated list of 3-5 lowercase tags. Example: ai, machine-learning, tutorial',
        messages=[
            {
                "role": "user",
                "content": f"Generate tags for a blog post about: {topic}",
            }
        ],
    )
    tags = [t.strip().strip('"') for t in tags_response.content[0].text.strip().split(",")]

    return {
        "title": title,
        "description": description,
        "content": content,
        "tags": tags,
    }


def translate_post(client: anthropic.Anthropic, system_prompt: str, post: dict) -> dict:
    """Translate the post to Spanish, adapting tone (not literal translation)."""
    translate_prompt = f"""Translate the following blog post to Spanish.

IMPORTANT: This is NOT a literal translation. Adapt idioms, references, and expressions
so they feel natural in Spanish. Maintain Mikalia's personality and the Four Pillars tone.
The Spanish version should feel like it was originally written in Spanish.

Title: {post['title']}

Content:
{post['content']}

Respond with ONLY the translated content in Markdown. Do NOT include front matter.
Start directly with the first ## heading.
"""

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=4000,
        system=system_prompt,
        messages=[{"role": "user", "content": translate_prompt}],
    )

    # Translate title
    title_response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=100,
        system="Translate blog post titles to natural Spanish. Respond with ONLY the translated title.",
        messages=[
            {"role": "user", "content": f"Translate this title to Spanish: {post['title']}"}
        ],
    )

    # Translate description
    desc_response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=200,
        system="Translate descriptions to natural Spanish. Respond with ONLY the translated description.",
        messages=[
            {
                "role": "user",
                "content": f"Translate to Spanish: {post['description']}",
            }
        ],
    )

    return {
        "title": title_response.content[0].text.strip().strip('"').strip("'"),
        "description": desc_response.content[0].text.strip(),
        "content": response.content[0].text,
        "tags": post["tags"],
    }


def build_front_matter(post: dict, date: str) -> str:
    """Build Hugo front matter for a post."""
    tags_str = ", ".join(f'"{tag}"' for tag in post["tags"])
    return f"""---
title: "{post['title']}"
date: {date}
draft: false
description: "{post['description']}"
tags: [{tags_str}]
categories: ["blog"]
series: ["Mikalia Writes"]
showHero: true
heroStyle: "big"
---

{post['content']}
"""


def save_post(en_post: dict, es_post: dict, slug: str, date: str) -> Path:
    """Save both EN and ES posts to the content directory."""
    post_dir = CONTENT_DIR / slug
    post_dir.mkdir(parents=True, exist_ok=True)

    en_file = post_dir / "index.md"
    es_file = post_dir / "index.es.md"

    en_file.write_text(build_front_matter(en_post, date), encoding="utf-8")
    es_file.write_text(build_front_matter(es_post, date), encoding="utf-8")

    return post_dir


def ethical_check(post: dict) -> bool:
    """Run the ethical content filter from MIKALIA.md."""
    checks = [
        ("Provides value to reader", True),  # Assumed if generated from valid topic
        ("No harmful content", not any(
            word in post["content"].lower()
            for word in ["hate", "discriminat", "harass", "attack"]
        )),
        ("Has signature", "stay curious" in post["content"].lower()),
    ]

    print("\n  Ethical Filter:")
    all_pass = True
    for name, passed in checks:
        status = "PASS" if passed else "FAIL"
        icon = "+" if passed else "!"
        print(f"    [{icon}] {name}: {status}")
        if not passed:
            all_pass = False

    return all_pass


def git_publish(post_dir: Path, title: str):
    """Commit and push the new post to GitHub."""
    try:
        subprocess.run(
            ["git", "add", str(post_dir)],
            cwd=str(PROJECT_ROOT),
            check=True,
            capture_output=True,
        )

        commit_msg = f'blog: [EN/ES] "{title}"\n\nGenerated by Mikalia\nReviewed: auto'

        subprocess.run(
            ["git", "commit", "-m", commit_msg],
            cwd=str(PROJECT_ROOT),
            check=True,
            capture_output=True,
        )

        subprocess.run(
            ["git", "push"],
            cwd=str(PROJECT_ROOT),
            check=True,
            capture_output=True,
        )

        return True
    except subprocess.CalledProcessError as e:
        print(f"\n  Git error: {e.stderr.decode()}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Mikalia — AI Blog Post Generator for Mikata AI"
    )
    parser.add_argument(
        "topic",
        nargs="?",
        help="Topic or prompt for the blog post",
    )
    parser.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="Interactive mode — prompts for topic",
    )
    parser.add_argument(
        "--no-publish",
        action="store_true",
        help="Generate post without committing/pushing to git",
    )
    parser.add_argument(
        "--draft",
        action="store_true",
        help="Save as draft (draft: true in front matter)",
    )

    args = parser.parse_args()

    # Get topic
    if args.interactive or not args.topic:
        print("\n  Mikalia — Blog Post Generator")
        print("  ================================")
        topic = input("\n  What should I write about?\n  > ").strip()
        if not topic:
            print("  No topic provided. Exiting.")
            sys.exit(0)
    else:
        topic = args.topic

    # Check API key
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("\n  Error: ANTHROPIC_API_KEY not set.")
        print("  Copy agent/.env.example to agent/.env and add your key.")
        sys.exit(1)

    # Initialize
    client = anthropic.Anthropic(api_key=api_key)
    system_prompt = load_system_prompt()
    date = datetime.now().strftime("%Y-%m-%d")

    print(f"\n  Topic: {topic}")
    print(f"  Date: {date}")
    print("\n  [1/4] Generating English post...")

    # Generate EN
    en_post = generate_post(client, system_prompt, topic)
    print(f"    Title: {en_post['title']}")
    print(f"    Tags: {', '.join(en_post['tags'])}")

    # Ethical check
    print("\n  [2/4] Running ethical filter...")
    if not ethical_check(en_post):
        print("\n  Content did NOT pass ethical filter. Aborting.")
        sys.exit(1)

    # Translate to ES
    print("\n  [3/4] Translating to Spanish...")
    es_post = translate_post(client, system_prompt, en_post)
    print(f"    Titulo: {es_post['title']}")

    # Save files
    slug = slugify(en_post["title"])
    post_dir = save_post(en_post, es_post, slug, date)
    print(f"\n  [4/4] Saved to: {post_dir.relative_to(PROJECT_ROOT)}")

    # Handle draft mode
    if args.draft:
        # Rewrite with draft: true
        for f in post_dir.iterdir():
            content = f.read_text(encoding="utf-8")
            content = content.replace("draft: false", "draft: true", 1)
            f.write_text(content, encoding="utf-8")
        print("    Mode: DRAFT (will not appear on site)")

    # Publish
    if not args.no_publish and not args.draft:
        print("\n  Publishing to GitHub...")
        if git_publish(post_dir, en_post["title"]):
            print("  Published! Deploy will trigger automatically.")
        else:
            print("  Failed to publish. Files are saved locally.")
    else:
        print("\n  Skipping publish (--no-publish or --draft flag).")

    print(f"\n  Done! Post: {en_post['title']}")
    print("  Stay curious~ -- Mikalia\n")


if __name__ == "__main__":
    main()
