# Section_crawl01
# 파이썬 크롤링 기초
# urllib 사용법 및 기본 스크랩핑

import urllib.request as req

# 파일 url
img_url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAzMzFfMjg4%2FMDAxNjE3MTE4MjY2MDMw.N7RFBwWfVE2zE58Uwd3DqQoEdeNHqlMVsFqNPplQmzsg.qQLIv2jfmwfC2KVofZJXQ_fO2BKaAOuD76EvNYrcwdkg.JPEG.rbflgg77_%2FIMG_2469.jpg&type=sc960_832'
html_url = 'http://www.google.com'

# 다운받을 경로
save_path1 = 'test1.jpg'
save_path2 = 'index.html'
import lxml

# 예외 처리
try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print('Download failed')
    print(e)
else:
    # Header 정보 출력
    print(header1)
    print(header2)
    
    # 다운로드 파일 정보
    print('Filename1 {}'.format(file1))
    print('Filename2 {}'.format(file2))
    print()

    # 성공
    print('Download Succeed')