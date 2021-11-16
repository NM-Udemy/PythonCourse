# urllib

import urllib.request

page_url = 'https://aaa.bb.cc/'
req = urllib.request.Request(page_url)
# 音声、画像
urllib.request.urlretrive('http://aaaa.gga.cc/sample.jpg', 'aa.jpg')
# with urllib.request.urlopen(req) as r:
#     try:
#         print(r.headers)
#     except urllib.error.URLError as e:
#         print(e.reason)
#     except urllib.error.HTTPError as e:
#         print(e.reason)

    # with open('site.html', mode='wb') as fh:
    #     fh.write(r.read())

