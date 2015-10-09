# Sublime Text 2 插件使用和Python环境设置 #

> [Sublime Text](http://www.sublimetext.com/)是一套跨平台的文本编辑器，支持基于Python的插件。Sublime Text 是专有软件，可通过包（Package）扩充本身的功能。大多数的包使用自由软件授权发布，并由社区建置维护。 [详见wiki](https://zh.wikipedia.org/wiki/Sublime_Text)

嗯 就是超级好用的文本编辑器 来看看英文版：

> Sublime Text is a sophisticated text editor for code, markup and prose.
You'll love the slick user interface, extraordinary features and amazing performance.

系统：win7  
之前就捣腾过 Py2.7.8 安装就不再进行了

- ST2 基础设置
- Package Control(插件管理 下载)
- ST2 中配置Python开发环境
- 我的常用快捷键
	+ `ctrl+shift+p` 去install package 
	+ `ctrl+alt+a` 对齐代码
	+ 本来 `ctrl + b` 可以进行编译 现在设置 `f5` 进行编译
	+ `ctrl+shift+c` Stop 终止程序

----------

## 基础设置 ##

- Sublime Text 2 进入 菜单 `Preferences -> Settings - User`
- 在编辑器窗口中编辑 进行我的相关配置

    `"draw_white_space": "all", // 显示空白字符, 比如 空格 tab`  
    `"font_size": 13.0, // 字体大小`  
    `"scroll_past_end": true,   // 当文件到末尾时还能继续滚动`  
    `"trim_automatic_white_space": false  // 关闭自动删除每行前后空格`  

----------

## Package Control ##

[Package Control](https://packagecontrol.io/installation#st2)用来管理 Sublime Text 2 插件的插件. 当然需要第一个安装

- 利用快捷键 ctrl+` or 点击菜单栏进入 
	+ `View > Show Console` 
- 直接去官网Copy 代码 paste the appropriate Python code for your version of Sublime Text into the console. 

 		import urllib2,os,hashlib; h = '2915d1851351e5ee549c20394736b442' + '8bc59f460fa1548d1514676163dafc88'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); os.makedirs( ipp ) if not os.path.exists(ipp) else None; urllib2.install_opener( urllib2.build_opener( urllib2.ProxyHandler()) ); by = urllib2.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); open( os.path.join( ipp, pf), 'wb' ).write(by) if dh == h else None; print('Error validating download (got %s instead of %s), please try manual install' % (dh, h) if dh != h else 'Please restart Sublime Text to finish installation')
- 重启生效 菜单下有 `Preferences -> Package Settings` 选项
- 以上亦可以手动设置 [参考官网](https://packagecontrol.io/installation#Manual)

### 使用Package control ###

[官网Usage](https://packagecontrol.io/docs/usage) 提供了相关描述

>  To open the palette, press ctrl+shift+p (Win, Linux) or cmd+shift+p (OS X). All Package Control commands begin with Package Control:, so start by typing Package.   
>  The command palette will now show a number of commands. Most users will be interested in the following:  

- windows下`ctrl+shift+p`快捷键进入Package Control 命令行
- 安装插件
	+ 输入`install package` 
	+ 输入我想要装的插件 如 [Alignment](http://wbond.net/sublime_packages/alignment) 选择安装
		* Alignment 这个插件用于对齐代码赋值语句 例如
		
				var name = "sublime"
				var version = "2.0.1"
				var title = "sublime text"
		* 按快捷键 可在`Preferences -> Package Settings -> Alignment -> Key Bindings defult` 中查看
		* 嗯 设置完之后 **请 restart 再使用快捷键** 这里我死后被坑了 一直找不到原因 后来 restart 就 ok 了 请注意 若设置好快捷键请 restart 嗯 Alignment 效果如下

				var name    = "sublime"
				var version = "2.0.1"
				var title   = "sublime text"

以上参考 [Sublime Text 常用插件和设置](https://wido.me/sunteya/sublime-text-packages-and-settings/)  

### 教训 ###

> - 嗯 Package 之后 直接去 官网进行查询相关插件 安装使用效率会比查别人高很多 吸取了教训   
> - 以后 多用官方文档
> - 比如 我要search markdown [PC markdown](https://packagecontrol.io/search/markdown) 就有许多插件了 安装可以直接看源文档的 更快捷高效

- 安装[Markdown Preview](https://packagecontrol.io/packages/Markdown%20Preview) 使用 一目了然 

----------

## 配置Python开发环境 ##

- 也就是如何在Sublime text 2中运行Python code
	+ `Tools -> Build System -> (choose) Python`
	+ 打开 `.py` Python代码文件
	+ `Ctrl + B` 运行 or 编译
- 如遇到死循环或中途需要停止程序 该如何操作
	+ `Ctrl + Break` or `Tools -> Cancel Build` 
	+ 我也可以自己设置 stop 快捷键 
		+ 进入菜单栏 `Preferences -> Key Bindings - User`
		+ 将如下代码贴入
		
				{"keys": ["ctrl+shift+c"], "command": "exec", "args": {"kill": true} }  
		+ 以上 就可以用 `ctrl+shift+c` 来代替 `Ctrl + Break` 终止程序运行

参考 [stack overflow](http://stackoverflow.com/questions/8551735/how-do-i-run-python-code-from-sublime-text-2)

### 问题 ###

- 我写了一段代码 如下

		name = raw_input('Enter your name: ')  
		print 'Are you really', name, '?'  
		print 'Are you really' + name + '?'  
- `Ctrl + B` 编译
- 显示 error

		name = raw_input('Enter your name: ')
		EOFError: EOF when reading a line

> 代码中如果使用了input等函数进行交互的时候，直接使用Ctrl+B进行编译时，运行信息栏内无法输入交互信息，程序会提示报错。

- 解决 安装插件
	+ [SublimeREPL](https://github.com/wuub/SublimeREPL) run an interpreter inside ST2 用来编译(运行)我的py程序 在工具栏 `Tools -> SublimeREPL -> python -> RUN current file`
	+ **优化之快捷键设置** SublimeREPL安装之后没有快捷键 每次运行程序必须用鼠标去点工具栏 增添效率 就给 SublimeREPL 添加快捷键 `Preferences -> Key Bindings - User`

			{"keys":["f5"],
    			"caption": "SublimeREPL: Python - RUN current file",
    			"command": "run_existing_window_command", "args":
    			{
        			"id": "repl_python_run",
        			"file": "config/Python/Main.sublime-menu"
    			}
			}
> - 注意 在添加快捷键的时候 因为我之前添加过一次快捷键 所以 再次添加时 需要在上一个快捷键代码行的最后加上一个 comma 而且要是 英文的comma 否则会出错 系统也会提示
> - 查看 SublimeREPL [所有Python方法的名称及id](https://github.com/wuub/SublimeREPL/blob/master/config/Python/Default.sublime-commands) 进行快捷键设置 我这里只设置了 `SublimeREPL: Python - RUN current file` 命令

- 果效 
	- `f5`键 可以快速进行调试和交互的程序了
	- 例如 `f5`键 运行起初的 `raw_input` 那段代码 可以进行交互 如图所示
![REPL](https://raw.githubusercontent.com/JeremiahZhang/pybeginner/master/_image/0-REPL.JPG)

----------

### 其他插件 ###

- [SublimeCodeIntel](https://github.com/SublimeCodeIntel/SublimeCodeIntel)
> SublimeCodeIntel 可以支持代码的自动补全以及成员/方法提示等功能，安装此插件后，Sublime Text 2就有点IDE的感觉了。

- [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter-for-ST2)
> SublimeLinter 是用来在写代码时做代码检查的，可以检查Python代码是否符合[PEP8](https://www.python.org/dev/peps/pep-0008/)的要求。

这两个可能太高级 嗯 入门阶段 暂时先不用这两个 虽然也装了

参考 [基于Sublime Text搭建Python IDE](http://loosky.net/2967.html)

----------

## 总 ##

当完成以上配置 并记录好后 才发现 大妈的模板是

- 现象
- 问题
- 分析
- 方案
- 执行

嗯 我看看自己的过程 总是没有大的框架在那 然后 走到随性而走 不好 得补这个缺

----------

## 进展

- 10/8/2015 雷雨创建