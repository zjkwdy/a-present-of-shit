import win32api,threading,time,pygame,sys,os
#获取资源文件路径，pyinstaller打包用
def resource_path(filaeName):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filaeName)
    return os.path.join(filaeName)
resPath = resource_path('0.mp3')#获取野兽声音路径
def Main():
    WM_APPCOMMAND = 0x319
    APPCOMMAND_VOLUME_MAX = 0x0a#最大音量
    def maxSound():
        while True:
            win32api.SendMessage(-1, WM_APPCOMMAND, 0x30292, APPCOMMAND_VOLUME_MAX * 0x10000)#调整音量为最大
            time.sleep(1)#太快电脑会卡死
    def PlaySound():
        pygame.mixer.init()
        pygame.mixer.music.load(resPath)
        while True:
            if pygame.mixer.music.get_busy() == False: #检查是否正在播放音乐
                pygame.mixer.music.play() #开始播放音乐流
    threading.Thread(target=maxSound).start()#启动音量调整线程
    threading.Thread(target=PlaySound).start()#启动播放声音线程
try:
    time.sleep(int(sys.argv[1]))#可以使用yflw.py 休眠秒数来延时执行
    Main()
except:
    Main()