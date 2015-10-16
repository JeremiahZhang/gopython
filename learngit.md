# Learn Git #

- Version Control 版本控制

## Version Control ##

- 什么是[版本控制](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)

> -  Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later. 

版本控制是记录文件内容变化的系统 可以帮助我在将来某一天都能查看以前某个文件某个版本的修订情况

- 举个例子 
	- 从2015年9月1日开始 我每天写硕士论文 直到今天 嗯 我是在word中写的
	- 每一天写完一点 我都保存好了 但是还是在原来的文件在保存的 直接`ctrl+s`
	- 假如我想知道我每天写的不用内容 我就得每日都另存为`ctrl+shift+s`一个版本 并命名时间2015-09-30版什么的 这样30天下来 我就有30个不同版本的硕士论文 查看我每一天所写的内容
	- 但有了版本控制系统 我只要用几个简单的命令 就可以记录那30个不同的论文版本 并且最终的文件 还是只有1个而已 我想回溯到30天内任何一天的写作内容 都可以 

以上只是一个简单的例子 
版本控制还有很多有用之处呢

----------

## Git ##

- 什么是[Git](https://git-scm.com/)
> Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency

Git是一个免费且开源的[分布式版本控制系统](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control#Distributed-Version-Control-Systems) 

![分布式版本控制](https://git-scm.com/book/en/v2/book/01-introduction/images/distributed.png)

如图 分布式版本控制系统中 服务器中的文件库(远程库)如同"大树树根"一样 树枝A和B(本地电脑A-B)可以从"树根"获取远程库内容 并在本地修改之后 再次传输给“树根” 而A-B可以同时对同一个文件库中的内容进行操作 A-B也可以进行互相协作

### Git Basic ###

3大区

- 工作区 working directory 
	- 你可以认为是 本地仓库 Local Repository
	- 也是-本地目录-本地文件夹 
	- 在其中可进行操作：如我在一个文件夹中建立一个md文档等等
- 暂存区 staging area
	- 这个区 可以看作是一个虚拟区 
- .git directory (Remote Reposiroty 远程仓库)
	- 代表着 [Github](https://github.com/) 远程仓库

### 配置工具 ###

- 注册github
	- 用户名
	- 邮箱地址

首先下载Git全平台版 [http://git-scm.com](http://git-scm.com) 

- 配置所有本地仓库的用户信息 (相当于配置确认你本地计算的用户ID 可以与远程仓库进行联通)
	- `$ git config --global username`
	- `$ git config --global email_address`
	- 说明 
		+ username 是 我在github上注册的 用户名
		+ email_address 是 我在github注册 用户名 时的 邮箱地址
- 这样设置好 我就可以和Github 远程库 进行自由联通了 怎么联通 请继续看

### 本地与远程库联通 ###

- 创建远程库 gopython
	- creat a new repo 新建完库之后 注意出现的代码 尤其是ssh连接
	- copy the SSH of the new repo 也可以使用其url 后面会使用
- 在本地文件夹中创建一个新的仓库
	+ 我在D盘中创建一个文件夹名为 gopython
	+ 我右击gopython文件夹名 再点击`git bash here` 我就对gopython文件夹进行git bash 命令行操作了
	+ `$ git init` git 默认此时branch为master
	+ 在【gopython文件夹】中添加 README.md和 SUMMARY.md 文件
- 远程仓库设置
	- `git add --a`
	- `git commit -m "1st commit"`
	- `git remote add name [the gopyhon SSH 或url 任选一]`注意`[]`不需要的 `name` 自定义远程库的名字
	- `git push -u name master` 将远程库内容