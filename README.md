# 2022-Ecole-practice - Web Crawling

1014-1015


## 📝내용📝
   서울대 빅데이터 혁신 공유대학 야마다 아키히코 박사님의 강의 들은 후 실습
   검색 키워드 변경 : big data -> airpods pro
   감정 분석 결과와 cleaned_tweet_str를 django를 이용하여 웹사이트에 띄움

## ⭐코드⭐
    < 야마다 박사님의 코드를 참고하였습니다 >
    ![Image](webScreen.png)
    
    x = []
    x.append(cleaned_tweet_str)
    for topic_topwords in lda_model.print_topics():
        x.append(topic_topwords)
    return HttpResponse(x)
    
### 참조
- https://lucky516.tistory.com/52?category=1010534
- 야마다 아키히고 박사님의 소스 코드

