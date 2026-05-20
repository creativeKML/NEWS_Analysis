from news_api import get_news_metadata
from article_parser import parse_article

import pandas as pd
from tqdm import tqdm
import time


def main():

    # 뉴스 메타데이터 검색
    articles = get_news_metadata()

    # 검색 결과 없을 경우
    if len(articles) == 0:

        print("검색된 뉴스가 없습니다.")
        return

    print(f"검색된 기사 수: {len(articles)}")

    parsed_articles = []

    # 기사 본문 파싱
    for _, row in tqdm(articles.iterrows(), total=len(articles)):

        url = row["url"]

        parsed_data = parse_article(url)

        if parsed_data:
            parsed_articles.append(parsed_data)

        time.sleep(0.3)

    # DataFrame 생성
    df = pd.DataFrame(parsed_articles)

    # CSV 저장
    output_file = "nvidia_cnn_articles.csv"

    df.to_csv(
        output_file,
        index=False,
        encoding="utf-8-sig"
    )

    # 저장 완료 출력
    print("\n저장 완료")
    print(f"파일명: {output_file}")
    print(f"저장된 기사 개수: {len(df)}")


if __name__ == "__main__":
    main()