import html
import re


def sanitize_text(text):

    if not text:
        return ""

    text = html.escape(text)

    text = re.sub(
        r"<script.*?>.*?</script>",
        "",
        text,
        flags=re.IGNORECASE
    )

    return text.strip()