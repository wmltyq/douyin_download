from tkinter import Tk, Label, W, S, E, Text, Button, END
import re
from console import main


class GUI:
    def __init__(self, mainwin):
        self.mainwin = mainwin
        self.hight = 465
        self.width = 210
        self.setup()
        self.urls = []

    def setup(self):
        self.mainwin.geometry('%sx%s' % (self.hight, self.width))
        # 冻结窗口大小
        self.mainwin.resizable(0, 0)
        self.mainwin.title('抖音视频下载器')

        copy_label = Label(self.mainwin, text='粘贴分享链接↓')
        copy_label.grid(row=0, column=0, padx=5, pady=5, sticky=W + S)
        self.copy_text = Text(self.mainwin, height=10, width=20)
        self.copy_text.grid(row=1, column=0, padx=5, pady=0)
        # self.copy_text.bind('<Return>', self.extract_url)

        extract_label = Label(self.mainwin, text='提取到短连接↓')
        extract_label.grid(row=0, column=1, padx=5, pady=5, sticky=W + S)
        self.extract_text = Text(self.mainwin, height=10, width=20)
        self.extract_text.grid(row=1, column=1, padx=5, pady=0)

        download_label = Label(self.mainwin, text='下载视频进度↓')
        download_label.grid(row=0, column=2, padx=5, pady=5, sticky=W + S)
        self.download_text = Text(self.mainwin, height=10, width=20)
        self.download_text.grid(row=1, column=2, padx=5, pady=0)

        download_btn = Button(self.mainwin, text='下载', command=self.download)
        download_btn.grid(row=2, column=2, padx=5, pady=5, sticky=E + S)

    def extract_url(self):
        copy_text = self.copy_text.get(1.0, END)
        for text in copy_text.split('\n'):
            print(text)

            if text:
                url = re.search('http://(.+)/', text)
                print(url.group())
                self.urls.append(url.group())
                self.extract_text.insert(END, url.group() + '\n')

    def download(self):
        self.urls = []
        self.extract_text.delete(0.0, 'end')
        self.download_text.delete(0.0, 'end')

        self.extract_url()
        for url in self.urls:
            main(url, download_text=self.download_text)


if __name__ == '__main__':
    mainwin = Tk()
    GUI(mainwin)
    mainwin.mainloop()
