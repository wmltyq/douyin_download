import requests
import re
import os
import multiprocessing
from tkinter import END

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400'
}

# 下载存放路径
file_path = 'video'
if not os.path.exists(file_path):
    os.makedirs(file_path)

# 列出已经下载的所有文件
downloaded_file = os.listdir(file_path)


def get_addr(url):
    """
    根据短地址获取播放地址和封面地址
    :param url: 短地址
    :return: 视频地址，封面地址
    """
    resp = requests.head(url)
    original_addr = resp.headers.get('location')

    if original_addr:
        resp.encoding = 'urf-8'
        resp = requests.get(url, headers=headers)
        html = resp.text
        # 播放地址
        play_addr = re.search('playAddr: "(.+?)"', html).group(1)
        print('播放地址：{}'.format(play_addr))
        # 视频封面
        cover_addr = re.search('cover: "(.+?)"', html).group(1)
        print('封面地址：{}'.format(cover_addr))

        return play_addr, cover_addr


def download(addr, filename):
    """
    下载文件
    :param addr: 文件地址
    :param filename: 带后缀的文件名
    :return:
    """
    if filename in downloaded_file:
        print('{} 已下载'.format(filename))
        return '{} 已下载'.format(filename)
    else:
        resp = requests.get(addr, headers=headers)
        with open(os.path.join(file_path, filename), 'wb') as f:
            f.write(resp.content)

        print('{} 下载完成'.format(filename))
        return '{} 下载完成'.format(filename)


def main(url, download_text=None):
    addrs = get_addr(url)
    if addrs:
        play_addr, cover_addr = addrs
    else:
        print('短地址错误')

    # 将短地址后缀作为下载的文件名
    url_split = url.split('/')
    if url_split[-1] == '':
        filename = url_split[-2]
    else:
        filename = url_split[-1]

    if download_text:
        download_text.insert(END, download(play_addr, filename + '.mp4') + '\n')
        download_text.insert(END, download(cover_addr, filename + '.jpg') + '\n')
    else:
        download(play_addr, filename + '.mp4')
        download(cover_addr, filename + '.jpg')


if __name__ == '__main__':
    # 添加需要爬取的短地址
    urls = (
        'http://v.douyin.com/HRFV7r/',
        'http://v.douyin.com/HRnLHp/',
        'http://v.douyin.com/HRECJN/',
        'http://v.douyin.com/H8RXpt/',
        'http://v.douyin.com/H8LvD6/',
    )

    pool = multiprocessing.Pool(2)
    pool.map(func=main, iterable=urls)
    pool.close()
    pool.join()
