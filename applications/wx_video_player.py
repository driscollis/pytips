import wx
import wx.media

class VideoPlayer(wx.Frame):
    def __init__(self):
        super(VideoPlayer, self).__init__(None, title='Video Player')
        self.media_ctrl = wx.media.MediaCtrl(self, style=wx.SIMPLE_BORDER,)
        self.media = '/path/to/video.mp4'
        self.media_ctrl.Bind(wx.media.EVT_MEDIA_LOADED, self.play)
        self.media_ctrl.Bind(wx.media.EVT_MEDIA_FINISHED, self.quit)
        if self.media_ctrl.Load(self.media):
            pass
        else:
            print("Media not found")
            self.quit(None)

    def play(self, event):
        self.media_ctrl.Play()

    def quit(self, event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.App()
    Frame = VideoPlayer()
    Frame.Show()
    app.MainLoop()