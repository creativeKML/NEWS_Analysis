from newspaper import Article


def clean_text(text):

    if not text:
        return ""

    return (
        text.replace("\n", " ")
            .replace("\r", " ")
            .strip()
    )


def parse_article(url):

    try:

        article = Article(url)

        article.download()
        article.parse()

        parsed_result = {
            "title": article.title,
            "url": url,
            "publish_date": article.publish_date,
            "authors": ", ".join(article.authors),
            "text": clean_text(article.text)
        }

        return parsed_result

    except Exception as e:

        print(f"[ERROR] 기사 파싱 실패: {url}")
        print(e)

        return None