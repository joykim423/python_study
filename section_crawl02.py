# Section_crawl02
# 파이썬 크롤링 기초
# urlopen 함수 기초 사용법

import urllib.request as req
from urllib.error import URLError, HTTPError

# 다운로드 경로 및 파일명
path_list = ["/Users/kimgunwoo/Desktop/test1.jpg.", "/Users/kimgunwoo/Desktop/index.html."]

# 다운로드 리소스
target_url = ["https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAxMDhfMjQ1%2FMDAxNjEwMDk1NTM5NjU0.ATCIJitp5vBiadFMlc7XyUsIUcSt1joQ7uQiy7wN8KAg.uVVsWMNvRvE58LUHRYMqMSwVvRq0AWZ_bLdpeQIr-wUg.JPEG.dhkdtksqhtkf%2Flion-5815534_640.jpg&type=sc960_832", "http://google.com"]

for i, url in enumerate(target_url):
    # 예외 처리
    try:
        # 웹 수신 정보 읽기
        response = req.urlopen(url)

        # 수신 내용
        contents = response.read()

        print("-------------------------------")

        # 상태 정보 중간 출력
        print('Header Info-{} : {}'.format(i, response.info()))
        print('HTTP Status Code: {}'.format(response.getcode()))
        print()
        print("-------------------------------")
        
        with open(path_list[i], 'wb') as c:
            c.write(contents)

    except HTTPError as e:
        print("Download failed.")
        print("HTTPError Code : ", e.code)
    except URLError as e:
        print("Download failed.")
        print("URL Error Reason : ", e.reason)

    # 성공
    else:
        print()
        print("Download Succeed.")