## 使用说明
* 命令行模式

通过抖音APP将想要下载的视频分享到微信中获取到短地址，将短地址配置到console.py的urls中然后运行程序文件即可下载。

* GUI模式

![示例](https://github.com/wmltyq/douyin_download/blob/master/img/sample.png)

将分享链接文本粘贴到“粘贴分享链接↓”下面的文本框中，多个分享链接之间需换行，然后点击下载即可下载分享链接中的视频和封面。

## 项目局限
只有公开访问的视频才能通过分享获取到短地址，而“好友可见”的视频因为不能对外分享，所有获取不到短地址，也就无法下载了。当然也不是完全无法下载，只要能看到视频通过手机抓包，还是可以获取的，而该项目只是简单的下载短地址中的视频和封面。