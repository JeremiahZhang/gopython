# gitbook #

- 1 [搜索到教程](http://www.chengweiyang.cn/gitbook/index.html)
- 2 直接用github登入gitbook
- 3 [官方文档git](https://github.com/GitbookIO/gitbook)

目标：

- what 我想干嘛? 知道该如何在gitbook写书 嗯 
	- 在线 先在线
	- 本地 
- when 现在10/1/2015 9:25:30 PM 
- how gitbook online editor
	- ok to do try

google了很多 惨烈 还是先直接去 gitbook 尝试写作  
嗯 尝试了GitBook在线写作 还在在MarkdownPad中写作舒服 

- 上面的目标达成  在线编辑完成[Leiyu Py 入门指南](https://www.gitbook.com/book/jeremiahzhang/pybeginner/details)介绍
- 然而本地Gitbook还没有熟悉

10/1/2015 10:02:14 PM 

## gitbook editor ##

- [入门使用](http://tonydeng.github.io/gitbook-zh/gitbook-howtouse/index.html)

### 安装 ###

- [x] [Node.js網頁應用程式開發環境](http://blogger.gtwang.org/2013/12/install-node-js-in-windows-mac-os-x-linux.html) 检测 cmd 中 node -v
- [x] [gitbook安装](http://tonydeng.github.io/gitbook-zh/gitbook-howtouse/howtouse/gitbookinstall.html)在cmd中直接npm install gitbook -g 出错 用git bash 也是出错 初步断定
	- **纠错中** 文件路径 姿势不对
		- change workdir in nodejs file 还是错误
		- 嗯 version 陈旧 2.14.4 OK 更新 [github issue](https://github.com/npm/npm/pull/9743) 失败
		- 继续执行 cmd 下 [Gitbook Library and cmd utility to generate GitBooks](https://www.npmjs.com/package/gitbook)
			> npm install gitbook-cli -g  
			> 依然 failure 文件夹不在node.js所在的文件
		- D:
		- CD <node.js所在文件名>
		- 执行 npm install gitbook-cli -g 
			- this time it is OK 
			- gitbook -V 版本为 0.3.6
	- 参考[简明教程](http://colobu.com/2014/10/09/gitbook-quickstart/) gitbook serve ./repository
		- cmd 将 一个 repo作为一本书 failure
	- 嗯 新建一文件夹 npm install gitbook -g 成功
	- 但是 gitbook 之后 出现要我 npm uninstall -g gitbook 然后 npm install -g gitbook-cli
	- ok 按照上面的完成
	- 执行 gitbook 显示OK
	- 之后按照[gitbook 2.0](http://samwhelp.github.io/blog/read/platform/gitbook2/diff/) 成功安装 Gitbook2.4.3
	- [建立.gitignore](http://samwhelp.github.io/blog/read/platform/gitbook/start/)
	- 再按上文的流程来 建立 README.md SUMMARY.md
		> touch README.md SUMMARY.md  


### 总 ###

#### 安装gitbook ####

自挖很多坑 总结起来 主要几步 尤其在

- 在所<node.js所在文件名> cmd 执行 npm install gitbook-cli -g
- $ gitbook 查看安装是否成功
- $ gitbook -V 查看version
- $ gitbook versions:install lastest 安装最新版本的 gitbook

之后安装好 babun 进行gitbook的设置

-  git config --global user.name "github用户名" 
-  git config --global user.email github登录邮箱地址 以上2步是git设置 暂时无关紧要

#### 我的新书 ####

-  建立「.gitignore」 [参考folder](https://github.com/GitbookIO/gitbook#ignoring-files--folders) 非必要 可以不建立

		wget -c https://raw.githubusercontent.com/github/gitignore/master/GitBook.gitignore -O .gitignore
	上面这段代码 直接在win cmd中是无效的 用babun直接就解决了
- 建立「README.md」，「SUMMARY.md」 文档  
	- $ touch README.md  SUMMARY.md
- $ gitbook serve 可以查看书籍网址 在浏览器中键入 就可以查看了
- $ echo "# bookname" > README.md 修改书名

主要参考文章 [快速使用gitbook](http://samwhelp.github.io/blog/read/platform/gitbook/start/)

----------

## Build 使用GIT更新 ##

使用gitbook editor的 [另外的参考](https://ilmvfx.wordpress.com/2015/09/30/gitbook-introduction-and-test-drive-maya-houdini-scripts-cookbook/)  
[Issues](https://github.com/GitbookIO/gitbook/issues/660)

我先参考的这篇[Update your book using GIT](http://help.gitbook.com/build/push.html) 然后按照里面非方法 遇到坑了

- 第一没有在Gitbook上建立相应的书籍 gitbookguide
- 第二没有Git pull 直接就push了

		git remote add gitbook https://username:apitoken@git.gitbook.com/marshallshen/ruby-api-best-practices.git
		git push -u gitbook master
刚开始就是这样 不成功

纠正：

		git remote rm gitbook
		git remote add gitbook https://username:apitoken@git.gitbook.com/marshallshen/ruby-api-best-practices.git
		git branch --track gitbook master
		git pull gitbook master
在本地库中 稍作修改有些内容合并了   
然后再进行Push 就成功了 

----------

## Link Github ##

- 目标
	- 直接在Github的repo中进行修改 然后直接同步到Gitbook  
- 发现 [Link a book and a GitHub repository](http://help.gitbook.com/github/index.html)
	- **同步**从 Github-》》》 Gitbook 可直接在Github修改repo内容 编辑gitbook
	- **同步不可逆 **以上不可逆 在gitbook的builds不会改变Github远程库repo的内容
> **Caution:** When you specify a GitHub repository in your book's settings, it will take priority over GitBook's git repository, this means that the editor will directly edit content on GitHub.  
> 
**The sync is unidirectional,** only changes made on GitHub will trigger builds on GitBook, GitBook will not update your GitHub repository with any content written before.

- 执行 参考[Transferring content to GitHub](http://help.gitbook.com/github/transferring_to_github.html)
	- 进入Gitbook网站 gitbook与github帐号连接
	- 选择书籍 进入 setting --》》 Github --》》 Export to Github 
		- 因为我现在Gitbook编辑了 所以Export to Github
		- 如果先在Github上有书籍Repo 可以直接 Link
			- 我可以将本地book的working dir与Github中repo连接 然后直接选择此处的 Link
	- 进入 Github Importer --》》 check url 
	- 因为之前我已经Pull了Gitbook的repo then 我直接push到上面所建立的Github Repo 但是发现不可行

			git remote add gbhub git@github.com:<...>.git
			git branch --track gbhub master
			git pull gbhub master 

		> fatal: 'gthub' does not appear to be a git repository
		fatal: Could not read from remote repository.
		
		- 出错 我也明白 我之间就将本地repo与gitbook 进行关联了 
		- 所以尝试另外建立一个文件夹 git pull 这个文件夹 但是我想直接在gitbook本地repo进行修改 不想再建 那么我就尝试 去掉本地repo与gitbook的关联 直接让本地repo与书籍github库进行关联 因上面也提到改变github repo可以直接改变gitbook 【这个想法我没有去尝试】
		- 我将github repo clone到本地 
			- 本地新建文件目录（文件夹）
			- $ git init
			- $ git clone https://github.com/JeremiahZhang/gitbookguide.git
			- $ git remote add 
			- $ git push 这里只推到了github repo
		- 经历以上折腾后 不成功 哪里不成功
			- 1 push 到github后 gitbook 无反应
			- 这时候想到可能要双推 gitbook要推 github也要推
		-  这时候突然想起了 OMOOC.py的[double push](https://openmindclub.gitbooks.io/omooc-py/content/support/dpush.html)
- 嗯 走了这么多弯路 最后发现

> - 我已经有了local repo 因为我之前就是在本地local repo 编辑图书 之后push 到gitbook的   
> - 那么我在gitbook网页用GithubImporter与Github连接之后 
> - 我可以直接将local repo 推送到 Github repo 之前不用进行Pull了
> - 只要进行双推就OK了   
> 因为相信Gitbookhelp文档说的 只要github repo更新 Gitbook自动同步 嗯 我试过了 不行

- 结果
	- 用double push解决了问题 现在理解了为什么double push Gitbook help中说的github同步gitbook 是个坑啊

## 写在最后 ##

阅读源文档为先 随时注意 注意条理  
执行任务之前 请尽量5W1H

- What 清晰目标 问题是什么
- How 如何执行 解决问题
- 结果如何

本篇文档 是作者2天内探索gitbook制书的过程 遗漏和盲点在所难免  
若您发现 或有更好的解决方法 请与作者联系 
联系邮箱zhangleisuda@gmail.com

10/3/2015 9:10:29 PM 