Intro
====

shell profile online.
>实现云端shell profile 功能.

## install 
>安装

`pip install urmem`






## Usage
>用法

```shell
usage: urmem [-h] [-r REPO] [-b BRANCH] [-f FILENAME] NAME

shell profile online

positional arguments:
  NAME         UR github username

optional arguments:
  -h, --help   show this help message and exit
  -r REPO      UR repo name
  -b BRANCH    UR branch name
  -f FILENAME  UR file name
```

### example: download [UR] github [repo] [branch] [filename] to local .$(SHELL)_profile 
>例子: 下载[你的]github[仓库]下面[不同分支][不同文件]添加到SHELL启动配置文件

`urmem doomzhou -f default -r urmem -b master`

or

`urmem doomzhou`
