# 1.Managing conda

`conda --version`: 查看 conda 版本
`conda update conda`: 更新 conda
`conda <command-name> --help`: conda 下查看 任意 conda command-name 命令的帮助文档

# 2.Managing environments

> 建立新的环境 

`conda create --name <new-environment-name> <3rd-package>`: 建立新的环境名字为 new-environment-name, 同时安装 第三方包 3rd-package. 比如

example：

`conda create --name rango django`: 新建了 rango 环境, 并在次此环境下安装 Django

注: `--name` == `-n`, `--help` == `-h`, `--envs` == `-e` 等等依次类似的简化.

> 激活环境

- Linux, OSX: `source activate <new-environment-name>`
- Windows: `activate <new-environment-name>`

example:

- 类 unix 系统: `source activate rango`
- Windows 系统: `activate rango`

激活 `rango` 环境

> 再建立第二个环境

`conda create --name <2nd-environment-name> python=2 <3rd-package>`: 建立第二个新的环境, 名字为 `2nd-environment-name`, `python` 版本为`2.x` 第三方包为 `3rd-package`.

例子:

`conda create --name djangotutor python=2 django`:  

- 新建 djangotutor 环境
- 使用的开发语言是 python 2
- 安装第三方包为 django

> 显示所有环境

`conda info --envs` or ` conda info -e`: 

- 查看所有的环境
- or 查看当前所在的环境

> 转换到另外一个环境

- Linux, OS X: `source activate rango`
- windows: `activate rango`

deactivate:

- Linux, OS X: `source deactivate`
- windows: `deactivate`

> 复制一个环境

`conda create --name rango-copy --clone rango`: 将之前建立的 rango 环境 copy 并建立另外一个新的环境 rango-copy.

> 删除环境

`conda remove --name rango --all`: 删除环境 rango

# 3 Managing Python

> 查看 python 版本

`conda search --full-name python`

> 安装不同版本的python

`conda create --name rango python=3`

---

# 4 管理 安装包

> 查看当前环境下 conda 安装好的包:

`conda list`

> 搜索包:

`conda search django`

> 安装新的包:

`conda install --name rango beautifulsoup4`: 
在 `rango` 环境下 安装 `beautifulsoup4` 包

# 5 删除包 环境

> 删除包:

`conda remove --name rango django`: 删除rango 环境中的 django 包

> 删除环境

`conda remove --name rango --all`

---

```
@anifacc
2017-04-24
```