# WeChat Album Downloader

A downloader for articles in WeChat Album:

```bash
$ ./appmsgalbum_downloader.py -h
usage: appmsgalbum_downloader.py [-h] [--album_id ALBUM_ID] [--biz_id BIZ_ID]

Download the articles in the album.

optional arguments:
  -h, --help           show this help message and exit
  --album_id ALBUM_ID  The album id.
  --biz_id BIZ_ID      The biz id.
```

Example:

```bash
$ ./appmsgalbum_downloader.py --album_id "2147014109962256393" --biz_id "MzA3OTUzNDkwMA=="
- [1. Fuzzing File Systems via Two-Dimensional Input Space Exploration](http://mp.weixin.qq.com/s?__biz=MzA3OTUzNDkwMA==&mid=2247483767&idx=1&sn=05e5905a8013afaba5f02b73fac37e07&chksm=9fb34f2ca8c4c63a59b9203eb5a50d44d7a874398ca5accecb99d24cabe6702fae53166f65ee#rd)
- [2. 论文分享：研究区块可获取价值（BEV）攻击的影响](http://mp.weixin.qq.com/s?__biz=MzA3OTUzNDkwMA==&mid=2247483788&idx=1&sn=b33cee8321977a7e9a88b27eca8b0578&chksm=9fb34fd7a8c4c6c10bc6a450a3a9f97fea9ec56a2da2320b5a88eafc4252677ad95e866d1783#rd)
...
```

## 参考

[使用Python爬取公众号的合集](https://www.cnblogs.com/ZYPLJ/p/17609348.html)
