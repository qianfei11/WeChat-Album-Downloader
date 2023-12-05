#!/usr/bin/env python3
import requests
import json
from typing import List
import argparse

MAX_COUNT = 20
URL = "https://mp.weixin.qq.com/mp/appmsgalbum"


class Downloader:
    def __init__(self, album_id: str, biz_id: str) -> None:
        self.sess = None
        self.url = URL
        self.params = {
            "action": "getalbum",
            "__biz": biz_id,  # 公众号的唯一标识 (Compass Lab)
            "album_id": album_id,  # 文章合集的唯一标识
            "count": MAX_COUNT,
            "is_reverse": 1,  # 为倒叙也就是从第一篇文章开始
            "uin": "",
            "key": "",
            "pass_ticket": "",
            "wxtoken": "",
            "devicetype": "",
            "clientversion": "",
            "appmsg_token": "",
            "x5": 0,
            "f": "json",  # 返回json格式的数据
        }

    def fetch_data(self) -> List:
        assert requests.sessions.Session == type(self.sess)
        articles = []
        counter = 0
        response = self.sess.get(url=self.url, params=self.params)
        if 200 == response.status_code:
            data = json.loads(response.text)
            # print(data)
            article_count = int(data["getalbum_resp"]["base_info"]["article_count"])
            # print(article_count)
            album = data["getalbum_resp"]["article_list"]
            for i in range(len(album)):
                articles.append([album[i]["pos_num"], album[i]["title"], album[i]["url"]])
            counter += len(album)
            # print(album)
            last_msgid = album[-1]["msgid"]
        while True:
            self.params["begin_msgid"] = last_msgid
            # print(last_msgid)
            self.params["begin_itemidx"] = 1
            response = self.sess.get(url=self.url, params=self.params)
            if 200 == response.status_code:
                data = json.loads(response.text)
                # print(data)
                album = data["getalbum_resp"]["article_list"]
                # print(album)
                if 0 == len(album):
                    break
                elif dict == type(album):
                    articles.append([album["pos_num"], album["title"], album["url"]])
                    counter += 1
                    break
                elif len(album) < MAX_COUNT:
                    for i in range(len(album)):
                        articles.append([album[i]["pos_num"], album[i]["title"], album[i]["url"]])
                    counter += len(album)
                    break
                else:
                    for i in range(len(album)):
                        articles.append([album[i]["pos_num"], album[i]["title"], album[i]["url"]])
                    counter += len(album)
                last_msgid = album[-1]["msgid"]
        assert counter == article_count
        return articles

    def process_data(self, data) -> None:
        for item in data:
            pos_num = item[0]
            title = item[1]
            url = item[2]
            print(f"- [{pos_num}. {title}]({url})")

    def run(self) -> None:
        self.sess = requests.Session()
        data = self.fetch_data()
        if data is not None:
            self.process_data(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download the articles in the album.")
    parser.add_argument("--album_id", type=str, help="The album id.")
    parser.add_argument("--biz_id", type=str, help="The biz id.")
    args = parser.parse_args()
    if args.album_id is None and args.biz_id is None:
        print("Please specify the album id and biz id.")
    d = Downloader(album_id=args.album_id, biz_id=args.biz_id)
    d.run()
