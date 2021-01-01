# a-present-of-shit
一份(粪)礼物电脑版
##编译帮助
首先安装pyinstaller:
  pip install pyinstaller
然后下载本仓库:
  git clone https://github.com/zjkwdy/a-present-of-shit.git
cd进入本仓库,然后执行:
  pyinstaller -F -w yflw.py
编辑生成的yflw.spec，大概第九行找到datas=[]
修改为:
  datas=[('0.mp3','.')]
保存并退出。
执行
  pyinstaller -F yflw.spec
完成后可以在dist目录找到
  yflw.exe
双击打开即可。也可以使用命令：
  yflw.exe 休眠秒数
来延迟执行。
