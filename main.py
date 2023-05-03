from flask import Flask, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route('/download', methods=['POST'])
def download():
  link = request.form.get('link')
  cookies = {
    '__cflb': '02DiuEcwseaiqqyPC5qrDCss6XuWcthYNdwem4Wv523aT',
  }

  headers = {
    'authority':
    'ssstik.io',
    'accept':
    '*/*',
    'accept-language':
    'en-US,en;q=0.9',
    'content-type':
    'application/x-www-form-urlencoded; charset=UTF-8',
    'hx-current-url':
    'https://ssstik.io/en',
    'hx-request':
    'true',
    'hx-target':
    'target',
    'hx-trigger':
    '_gcaptcha_pt',
    'origin':
    'https://ssstik.io',
    'referer':
    'https://ssstik.io/en',
    'sec-ch-ua':
    '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile':
    '?0',
    'sec-ch-ua-platform':
    '"Windows"',
    'sec-fetch-dest':
    'empty',
    'sec-fetch-mode':
    'cors',
    'sec-fetch-site':
    'same-origin',
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68',
  }

  params = {
    'url': 'dl',
  }

  data = {
    'id': link,
    'locale': 'en',
    'tt': 'ZUNzUkxl',
  }

  response = requests.post('https://ssstik.io/abc',
                           params=params,
                           cookies=cookies,
                           headers=headers,
                           data=data)
  downloadSoup = BeautifulSoup(response.text, "html.parser")
  downloadLink = downloadSoup.a["href"]
  return {'download_link': downloadLink}


if __name__ == '__main__':
  app.run(host="1.0.0.0", port=8000)
