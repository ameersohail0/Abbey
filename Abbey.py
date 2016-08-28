import wikipedia
import wolframalpha
import wx

import pyttsx
import speech_recognition as sr

engine = pyttsx.init()
engine.setProperty('rate', 100)
voices = engine.getProperty('voices')
for voice in voices:
    if voice.gender == "female" :
        engine.setProperty('voice',voice.id)
        break

engine.say("Hello ameer")
engine.runAndWait()

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos = wx.DefaultPosition, size = wx.Size(450,100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
            wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title = "Abbey")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label = "Hello I am  Abbey, your personal digital assistant. How can i help you>")
        my_sizer.Add(lbl,0,wx.ALL,5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0 , wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self,event):
        input = self.txt.GetValue()
        input = input.lower()
        if input == '':
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                self.txt.SetValue(r.recognize_google(audio))
            except sr.UnknownValueError:
                print("I did not understand what you said")
                engine.say("I did not understand what you said")
                engine.runAndWait()
            except sr.RequestError as e:
                print("Something is not right at this moment {0}".format(e))
                engine.say("Something is not right at this moment")
                engine.runAndWait()
        try:
            
            
            try:
                #wolframalpha
                app_id =  "KQWU34-TP97W457G9"
                client = wolframalpha.Client(app_id)
                res = client.query(input)
                answer = next(res.results).text
                print answer
                engine.say(answer)
                engine.runAndWait()
            except:
                #wikipedia
                #print wikipedia.summary(input, sentences = 2)
                #print "wolf failed, i am wiki"
                summary = wikipedia.summary(input, sentences =  5)
                #print wikipedia.summary(input)
                print summary
                #summary = summary.encode('utf-8')
                #print summary
                sumarry = str(summary)
                #engine.say("Here is the wikipedia Summary")
                engine.say(summary)
                engine.runAndWait()
        except:

            engine.say("Check your internet connection! ")
            engine.runAndWait()
            print ("Check your internet connection! ")    

if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()




