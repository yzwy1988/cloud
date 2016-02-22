# -*- coding: utf-8 -*-


import wx
import wx.html
import urllib
import thread
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')


# ----------------------------------------------------------------------

class TestFrame(wx.Frame):
    def __init__(self, parent, ):
        wx.Frame.__init__(self, parent, -1, "天气预报",
                          style=
                          wx.FRAME_SHAPED
                          | wx.SIMPLE_BORDER
                          | wx.FRAME_NO_TASKBAR
                          )
        self.count = 0
        self.weatherInfo = ''  # 天气信息
        self.hasShape = False
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMouseMove)
        self.delta = (0, 0)
        self.bmp = wx.Image('bg.png', wx.BITMAP_TYPE_PNG, -1).ConvertToBitmap()
        self.w, self.h = self.bmp.GetWidth(), self.bmp.GetHeight()  # 获取图片背景长宽
        self.bmp.SetMask(wx.Mask(self.bmp, wx.BLACK))
        self.SetClientSize((self.w, self.h))
        self.SetWindowShape()
        self.html = wx.html.HtmlWindow(self, -1, (self.w - 230, 50), (200, 150))  # 天气信息显示区域
        self.initCloseButton()  # 初始化关闭按键
        self.initimg()  # 初始化天气图片
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        thread.start_new_thread(self.getWeatherInfo, (1, 2))  # 开启获取天气线程

    def initCloseButton(self):
        self.closebmp = wx.Image('no.png', wx.BITMAP_TYPE_PNG, -1).ConvertToBitmap()
        self.closebmp.SetMask(wx.Mask(self.closebmp, wx.BLACK))
        button = wx.BitmapButton(self, -1, self.closebmp, style=wx.NO_BORDER, pos=(self.w - 30, 20))
        button.SetDefault()
        self.Bind(wx.EVT_BUTTON, self.onButtonClick, button)

    def getWeatherInfo(self, no, interval):
        web = urllib.urlopen('http://m.weather.com.cn/data/101190101.html')
        self.weatherInfo = web.read()
        web.close()
        print
        self.weatherInfo
        self.updateText()

    def updateText(self):
        weatherinfo = eval(self.weatherInfo)['weatherinfo']
        for i in weatherinfo:
            print
            i, weatherinfo[i]
        city = weatherinfo['city'].decode('utf-8')
        print
        city
        strs = '<font  color="#444444">城市——%s</font>&nbsp;&nbsp;&nbsp;&nbsp;<font   color="red" size="1">%s</font><br> \
             <font color="#444444">气温：%s<br>天气：%s</font><br>\
             <font color="#444444">风向：%s</font><br><br>\
             <font color="#444444">  </font>' % (weatherinfo['city'].decode('utf-8')
                                                                , weatherinfo['week'].decode('utf-8')
                                                                , weatherinfo['temp1'].decode('utf-8')
                                                                , weatherinfo['weather1'].decode('utf-8')
                                                                , weatherinfo['wind1'].decode('utf-8'))
        self.html.SetPage(strs)
        imgno = weatherinfo['img2']
        imgno = re.findall(r'\d', imgno)
        print
        imgno[0]
        self.bmp2 = wx.Image('images/w%s.png' % imgno[0], wx.BITMAP_TYPE_PNG, -1).ConvertToBitmap()  # 更改天气图片
        self.Refresh()  # 刷新窗口

    def initimg(self):
        self.bmp2 = wx.Image('images/w0.png', wx.BITMAP_TYPE_PNG, -1).ConvertToBitmap()

    def SetWindowShape(self, *evt):
        r = wx.RegionFromBitmap(self.bmp)
        self.hasShape = self.SetShape(r)

    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp, 0, 0, True)
        dc.DrawBitmap(self.bmp2, 10, 20, True)

    def onButtonClick(self, evt):
        print
        '按键点击'
        self.Destroy()

    def OnLeftDown(self, evt):
        self.CaptureMouse()
        x, y = self.ClientToScreen(evt.GetPosition())
        originx, originy = self.GetPosition()
        dx = x - originx
        dy = y - originy
        self.delta = ((dx, dy))

    def OnLeftUp(self, evt):
        if self.HasCapture():
            self.ReleaseMouse()

    def OnMouseMove(self, evt):
        if evt.Dragging() and evt.LeftIsDown():
            x, y = self.ClientToScreen(evt.GetPosition())
            fp = (x - self.delta[0], y - self.delta[1])
            self.Move(fp)

            # ----------------------------------------------------------------------


app = wx.PySimpleApp()
win = TestFrame(None)
win.Show(True)
app.MainLoop()
