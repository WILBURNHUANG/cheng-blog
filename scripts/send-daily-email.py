#!/usr/bin/env python3
"""
Send daily news digest email to subscribers.
Triggered by GitHub Actions when a new daily post is pushed.
"""

import os
import re
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path

import yaml


def parse_mdx_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from MDX file."""
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if match:
        return yaml.safe_load(match.group(1))
    return {}


def extract_key_takeaways(content: str) -> list[str]:
    """Extract key takeaways from the post content."""
    takeaways = []
    in_takeaways = False

    for line in content.split('\n'):
        if '## Key Takeaways' in line:
            in_takeaways = True
            continue
        if in_takeaways:
            if line.startswith('## '):
                break
            if line.startswith('- **'):
                # Extract the takeaway text
                match = re.match(r'- \*\*([^*]+)\*\*: (.+)', line)
                if match:
                    takeaways.append(f"{match.group(1)}: {match.group(2)}")

    return takeaways


def create_email_content(post_path: str, site_url: str) -> tuple[str, str]:
    """Create email subject and body from post file."""
    with open(post_path, 'r', encoding='utf-8') as f:
        content = f.read()

    frontmatter = parse_mdx_frontmatter(content)
    takeaways = extract_key_takeaways(content)

    title = frontmatter.get('title', 'Daily Tech & GNSS News')
    description = frontmatter.get('description', '')
    date = frontmatter.get('date', '')

    # Build post URL from filename
    filename = Path(post_path).stem  # e.g., 2026-01-13-daily-tech-gnss-news
    post_url = f"{site_url}/posts/{filename}"

    subject = title

    # Build email body
    body_parts = [
        f"# {title}",
        "",
        description,
        "",
        f"**Read the full article:** {post_url}",
        "",
        "---",
        "",
        "## Key Takeaways",
        "",
    ]

    for takeaway in takeaways:
        body_parts.append(f"• {takeaway}")

    body_parts.extend([
        "",
        "---",
        "",
        "You're receiving this because you subscribed to Tech & GNSS News updates.",
        "To unsubscribe, reply with 'unsubscribe'.",
    ])

    body = '\n'.join(body_parts)

    return subject, body


def send_email(
    sender: str,
    password: str,
    recipients: list[str],
    subject: str,
    body: str
) -> None:
    """Send email via Gmail SMTP."""

    # Create message
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = f"Tech & GNSS News <{sender}>"
    msg['To'] = ', '.join(recipients)

    # Plain text version
    text_part = MIMEText(body, 'plain')
    msg.attach(text_part)

    # HTML version (basic formatting)
    html_body = body.replace('\n', '<br>\n')
    html_body = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html_body)
    html_body = re.sub(r'# (.+?)<br>', r'<h1>\1</h1>', html_body)
    html_body = re.sub(r'## (.+?)<br>', r'<h2>\1</h2>', html_body)
    html_body = f"<html><body style='font-family: sans-serif;'>{html_body}</body></html>"
    html_part = MIMEText(html_body, 'html')
    msg.attach(html_part)

    # Send via Gmail SMTP
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, recipients, msg.as_string())

    print(f"✅ Email sent to {len(recipients)} recipient(s)")


def main():
    # Get environment variables
    gmail_user = os.environ.get('GMAIL_USER')
    gmail_password = os.environ.get('GMAIL_APP_PASSWORD')
    subscribers_str = os.environ.get('EMAIL_SUBSCRIBERS', '')
    post_file = os.environ.get('POST_FILE', '')
    site_url = os.environ.get('SITE_URL', 'https://techntrek.is-a.dev')

    # Validate required env vars
    if not gmail_user or not gmail_password:
        print("❌ Error: GMAIL_USER and GMAIL_APP_PASSWORD must be set")
        exit(1)

    if not subscribers_str:
        print("❌ Error: EMAIL_SUBSCRIBERS must be set")
        exit(1)

    if not post_file:
        print("❌ Error: POST_FILE must be set")
        exit(1)

    # Parse subscribers (comma-separated)
    subscribers = [email.strip() for email in subscribers_str.split(',') if email.strip()]

    if not subscribers:
        print("❌ Error: No valid subscribers found")
        exit(1)

    print(f"📧 Preparing email for: {post_file}")
    print(f"📬 Recipients: {len(subscribers)}")

    # Create and send email
    subject, body = create_email_content(post_file, site_url)
    send_email(gmail_user, gmail_password, subscribers, subject, body)


if __name__ == '__main__':
    main()
