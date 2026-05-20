from gdeltdoc import GdeltDoc, Filters
import time


def get_news_metadata():

    for attempt in range(3):

        try:

            filters = Filters(
                start_date="2024-03-20",
                end_date="2024-03-25",
                num_records=250,
                keyword="nvidia",
                domain="cnn.com",
                country="US"
            )

            gd = GdeltDoc()

            articles = gd.article_search(filters)

            return articles

        except Exception as e:

            print(f"[ERROR] GDELT 뉴스 검색 실패 (시도 {attempt + 1}/3)")
            print(e)

            time.sleep(5)

    return []