# 我的配置

因个别原因，我在另一台计算机的win10系统上走一遍 Tango with Django, Python Version

- 系统：win10
- python 版本

`$ python --version`

```
Python 2.7.13 |Anaconda 4.3.0 (64-bit)| (default, Dec 19 2016, 13:29:36) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
```

使用anacoda包装后的.

我不知道使用Anacoda, 还要不要设置路径, 我暂时就没有设置. 若以后有问题, 可以参考[Test drive — Conda documentation](https://conda.io/docs/test-drive.html#managing-environments)

如果新安装Python了, 可以按照此[win70设置系统路径方法](http://stackoverflow.com/questions/14224756/window-add-java-to-path/14224786#14224786)进行

# Virtual Environments

> A Virtual Environment is a tool to keep the dependencies required by different projects in separate places, by creating virtual Python environments for them. It solves the “Project X depends on version 1.x but, Project Y needs 4.x” dilemma, and keeps your global site-packages directory clean and manageable

虚拟环境是一个工具, 在进行项目的时候非常有用, 多个项目就像一个个互相独立工作室, 里面的工具包(packages)版本是相互独立的, 互不影响彼此项目.

在win10上 设置 Virtual Environmens

## virtualenv 

在目录`C:\Users\we`下

`$ pip install virtualenv` #  windows 默认安装在 `C:\Users\we` 下的

> In Windows, the default path for WORKON_HOME is %USERPROFILE%Envs

## virtualenvwrapper

> virtualenvwrapper provides **a set of commands** which makes working with virtual environments much more pleasant. It also places all your virtual environments in one place.

安装前需要确认已经安装 *virtualenv*

`$ pip install virtualwrapper-win` # 因为系统是windows 所以使用该包

`$ pip install virtualwrapper` # Linux/UNIX basd OS
`$ source virtualenvwrapper.sh` # Linux/UNIX basd OS

- 1 建立一个虚拟环境 rango：

`$ mkvirtualenv rango` # 虚拟环境下建立 rango 项目

*rango* 文件夹在 ~/Envs 下

- 2 work on 虚拟环境 rango

`$ workon rango` # active 虚拟环境 rango 项目

下面就可以用pip 在 rango 下安装想要安装的工具包(packages).

关于 virtualenv 和 virtualwrapper-win 可参考 [Virtual Environments — The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/dev/virtualenvs/#id3)

- 3 deactivate 关闭激活状态 就是不用这个 rango 环境

`$ deactivate`

可参考 [Command Reference — virtualenvwrapper 4.7.3.dev7 documentation](http://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html#managing-environments).

---

## conda test drive 

因为我使用的 Anaconda 的Python封装包, 我想还是使用conda的 test drive 来配置环境.

因此我参考[Test drive — Conda documentation](https://conda.io/docs/test-drive.html#managing-environments)下的[Managing environments](https://conda.io/docs/test-drive.html#managing-environments)来进行环境配置。我初步猜测这样和之前使用*virtualenv* package 一样.（注：可以 参见[Create virtual environments for python with conda](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/)）

使用:

`$ conda create --name rango python=2 django`

创建环境, name: rango, 同时安装 *python 2* 和 *django*.

其中 `--name` 可缩写为 `-n`, conda 缩写例如前面所示.

outputs:

```
Fetching package metadata ...........
Solving package specifications: .

Package plan for installation in environment D:\ProgramData\Anaconda2\envs\rango:

The following NEW packages will be INSTALLED:

    django:         1.10.5-py27_0
    pip:            9.0.1-py27_1
    python:         2.7.13-0
    setuptools:     27.2.0-py27_1
    vs2008_runtime: 9.00.30729.5054-0
    wheel:          0.29.0-py27_0

Proceed ([y]/n)? y

django-1.10.5- 100% |###############################| Time: 0:00:25 160.36 kB/s
#
# To activate this environment, use:
# > activate rango
#
# To deactivate this environment, use:
# > deactivate rango
#
# * for power-users using bash, you must source
#
```

可以看出不仅安装 *django*, 还有 *pip* 等

现在我来看看所有的 environments

`$ conda info --envs`

outputs:

```
# conda environments:
#
rango                    D:\ProgramData\Anaconda2\
root                  *  D:\ProgramData\Anaconda2
```

conda 列出所有 environments, *root* 是原本的 environments, *rango* 是我之前刚创建的.可以看到一个星号 asterisk `*`在 *root* environment 中, 就说明，当前激活的 environment 是 *root*, 那么我该如何转换到 *rango* 环境呢?

使用:

`$ activate rango`

再看:

`$ conda info --envs`

环境信息:

```
# conda environments:
#
rango                    D:\ProgramData\Anaconda2\envs\rango
root                  *  D:\ProgramData\Anaconda2
```

没有从 *root* 改到 *rango* 去嘛

我想之前也安装了 *virtualenv* 和 *virtualenvwrapper-win*, 所以我先卸载它们两.

`$ pip uninstall virtualenvwrapper-win`
`$ pip uninstall virtualenv`


outputs

```
Successfully uninstalled virtualenvwrapper-win-1.2.1
Successfully uninstalled virtualenv-15.1.0
```

`$ conda info --envs` 

输出结果和之前一样啊！！！

```
# conda environments:
#
rango                    D:\ProgramData\Anaconda2\envs\rango
root                  *  D:\ProgramData\Anaconda2
```

还是在 *root* 啊, 该怎么办呢？

查看：

- [python - How to activate an Anaconda environment - Stack Overflow](http://stackoverflow.com/questions/20081338/how-to-activate-an-anaconda-environment)
- [python - Does anaconda create a separate PYTHONPATH variable for each new environment? - Stack Overflow](http://stackoverflow.com/questions/17386880/does-anaconda-create-a-separate-pythonpath-variable-for-each-new-environment)
- [Conda env not activated in windows power shell · Issue #661 · conda/conda](https://github.com/conda/conda/issues/661) 这个最准确

发现和 路径 PATH 有关。

解决：

> 在 powershell 中 `activate rango` 是无效的, 但是使用 CMD 命令行, 执行 就可以更改.

在 cmd 中: `$ activate rango`

再看: `$ conda info --envs` 

```
# conda environments:
#
rango                 *  D:\ProgramData\Anaconda2\envs\rango
root                     D:\ProgramData\Anaconda2
```

可以看到星号 在 *rango* 环境下了。 但是在 powershell 显示还是以前的. 看来还是要在cmd使用才行。这个问题就可以参考:

- [Liquidmantis/PSCondaEnvs: Drop in replacement scripts that replicate Conda's activate/deactivate commands in Powershell.](https://github.com/Liquidmantis/PSCondaEnvs)

下载 放入 conda 安装路径 的 Scripts 文件夹下 无用. powershell 禁止运行. 还是使用CMD吧。

使用 [A hacky powershell function to activate anaconda environments since the inbuilt method does not work](https://gist.github.com/arvindch/409802ab2f6c4b5aa48a36078e39587e) 代码, 放入 conda 安装路径 的 Scripts 文件夹下也无用.

```
Register-conda : 无法加载文件 D:\ProgramData\Anaconda2\Scripts\Register-conda.ps1，因为在此系统上禁止运行脚本。有关详细
信息，请参阅 http://go.microsoft.com/fwlink/?LinkID=135170 中的 about_Execution_Policies。
所在位置 行:1 字符: 1
+ Register-conda
+ ~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) []，PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

这回我认真看了 [about_Execution_Policies](https://technet.microsoft.com/zh-CN/library/hh847748.aspx) 只要以管理员的身份运行 powershell, 修改设置 执行策略。

`$ GetSet-ExecutionPolicy`

得到我当前的执行策略是 
**Restricted**

`$ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`

修改为 **RemoteSigned** 执行策略。

之后在 powershell 中 使用 - [Liquidmantis/PSCondaEnvs: Drop in replacement scripts that replicate Conda's activate/deactivate commands in Powershell.](https://github.com/Liquidmantis/PSCondaEnvs) 的 `activate` 和 `deactivate` 命令就可以啦。

### managing packages

既然我已经可以使用 `activate` 和 `deactivate`命令, 那么我们进入 *rango* 环境 看看安装了那些packages

继续 powershell(PS) 下：(以后默认在window键入命令使用PS)

`$ conda list`
outputs:

```
# packages in environment at D:\ProgramData\Anaconda2\envs\rango:
#
django                    1.10.5                   py27_0
pip                       9.0.1                    py27_1
python                    2.7.13                        0
setuptools                27.2.0                   py27_1
vs2008_runtime            9.00.30729.5054               0
wheel                     0.29.0                   py27_0
```

我想继续安装其他 package 比如 *beautifulsoup4*怎么办?

看我的执行:

`$ conda install --name rango beautifulsoup4`
`$ conda list`

outputs:

```
# packages in environment at D:\ProgramData\Anaconda2\envs\rango:
#
beautifulsoup4            4.5.3                    py27_0
django                    1.10.5                   py27_0
pip                       9.0.1                    py27_1
python                    2.7.13                        0
setuptools                27.2.0                   py27_1
vs2008_runtime            9.00.30729.5054               0
wheel                     0.29.0                   py27_0
```

看到, 在当前环境 *rango* 中已经有 *beautifulsoup4*.

---

# end

本次是记录折腾 环境配置 的过程. 

教训: 命令行提示的错误信息一定要认真看, 不想看就读出来.

    @Anifacc
    2017-04-17