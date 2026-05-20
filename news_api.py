from gdeltdoc import GdeltDoc, Filters

print("gdeltdoc import 성공")

def get_news_metadata():

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