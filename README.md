>   这个代码仓库是一个完整项目的预览版本。仅部分内容在这个代码仓库中。
>
>   本项目完全适用于个人的爬虫需求，不接受任何的商业化需求联系。本项目的源代码已全部在 gitee 和 pypi 开源，由于 github 网络情况限制，未在 github 托管。需要



# 这个项目能做什么?



#### 对于普通用户：

>   更好地爬取抖音、小红书、微博、知乎、tiktok、youtube、百度等网站和部分客户端如B站、wallPaperEngine 等的内容，并管理数据；保存一般类型网页的内容；使用时钟事件提醒、日记记录等功能

#### 对于开发者：

>   快速开发基于 selenium 的软件；一套开箱即用的 python 语法糖盒；

#### 对于学习者：

>   理解 python 的高级特性；感受一个框架从0到1的设计过程；



>   总地来说，这个项目是为了保存网页内容以及用自动化方案解决个人电脑办公、生活使用的一些痛点而存在的。这个项目主要是为了解决个人使用场景的需求，而不是为了企业级和商业及目的而实现的。



## 效果展示

*按住ctrl，单击鼠标左键以在新窗口查看*

[用户列表](./link-md/douyin/douyin_users.txt)

[douyin1](./link-md/douyin/douyin-crawled-sample.png)

[douyin2](./link-md/douyin/douyin-storage.png)

## 运行这个项目需要怎么做？

>   这个项目的运行环境即是一般的个人电脑。

#### 你必须具备：

-   基本的 python 使用经验



#### 我们建议你：

-   具备一定的包括其它语言在内的编程能力
-   使用 ChatGPT 来学习和阅读 ，以省去不必要的时间
-   使用 windows 操作系统电脑，而不是 macOS 等其它操作系统
-   一般的运行环境是在 IDE 中的。使用命令行不是推荐的做法。
-   使用 PyCharm ，而不是 VSCode 。当然，这不是必须的，如果你不在意繁琐的设置的情况下
-   从一个爬虫业务代码文件开始阅读，即能够快速理解87%的业务过程和代码风格



#### 关于项目设计的一些信息，以便于你理解：

-   每个实际业务几乎不会用到超过三个代码文件：

```
CyberU/__init__.py (which contains hundreds util funcs)
*give douyin as an example
抖音/douyin_detect.py (which import douyin_utils.py)
```

-   项目的函数不断在根据需求而调整更新，每个业务代码中的函数和用法可能不是最新的，但几乎不会有什么变化



## 这个项目完整吗？



>   这个项目始终仍在个人开发阶段，目前的（包括前文全部提到的全部网站）每一版功能是完整可用的。存在部分推送时的代码是未经测试的，同时git branch唯一，因此实际代码仓库版本的内容可能存在问题。



## 后续有什么开发计划？

-   [ ] 继续深耕浏览器自动化
-   [ ] 寻找浏览器自动化的替代方案
-   [ ] 跨端探索
-   [ ] 设计一套与 ChatGPT 交互的数据格式和自然语言库
-   [ ] 探索更美观、更高效、更定制化的生活应用