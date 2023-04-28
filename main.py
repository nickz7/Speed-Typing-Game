from tkinter import*
import random
from  tkinter import messagebox
# Functions #################################################################

def label_slider():
    global count,word_snap
    text = "Typing Speed Game"
    if (count >= len(text)):
        count=0
        word_snap=''
    word_snap += text[count]
    count+=1
    win_label.configure(text=word_snap)
    win_label.after(200,label_slider)

def time_lff():
    global time_left,hit,miss,score
    if time_left >=11:
        pass
    else:
        time_left_lb.configure(fg="red")
    if time_left > 0:
        time_left -= 1
        time_left_lb.configure(text=time_left)
        time_left_lb.after(1000,time_lff)
    else:
        game_play_detail_label.configure(text='Hit {} | Miss {} | Total Score {}'.format(hit,miss,score),fg="red")
        msgbox = messagebox.askretrycancel('Notification','For Play Again Hit Retry')
        if msgbox == True:
            time_left=60
            hit=0
            miss=0
            score=0
            time_left_lb.configure(text=time_left,fg="blue")
            word_label.configure(text=words[0])
            score_counter.configure(text=score)

def startgame(event):
    global score,miss,hit
    if time_left==60:
        time_lff()

    game_play_detail_label.configure(text="")

    if (wordEntry.get() == word_label['text']):

        score += 10
        hit+=1
        score_counter.configure(text=score)

    else:
        miss += 1

    random.shuffle(words)
    word_label.configure(text=words[0])
    wordEntry.delete(0,END)

# Windows Main Frame #########################################################

windows_frame=Tk()
windows_frame.geometry('600x400+350+90')
windows_frame.configure(bg="pink")
windows_frame.title("Typing Speed Game")
windows_frame.iconbitmap("id.ico")

# Variables ###################################################################

words=['Apple','Mango','banana','door','Black Board','pea','white','black','blue','red','orange','pine apple','bule book','astrology',
       'space','universe','star','sky','moon','zebra','hero','film','website','computer','hacker','web camera','camera',
       'mobile','phone','apps','windows','windows xp','windows vista','windows 7','windows 8','windows 8.1','windows 10',
       'samsung','iphone','machine','keypad','keyboard','enter','desktop','god','galaxy','black hole','pycharm','delete',
       'this','that','world','nick z','loard','lock','knock','known','ghost','mantra','tantra','tratak','eye','new',
       'python','java','java script','html','php','plate','tree','sun','moon','bank','credit card','tor','and','or','not',
       'nand','nor','x or','power up','shut down','news paper','black bottle','nice one','water','type','game','speed',
       'dell','cmd','batch','pdf','youtube','cd','pen drive','sd card','rom','ram','hardware','software','blue star',
       'king','queen','friend','good','bad','luck','good luck','height','right','wrong','word','tab','shift','bharat',
       'india','mango man','hacker','facebook','instagram','google chrome','rise','rice','kite','vivo','english','hindi',
       'maths','science','school','money','more','set','weight']
score=0
time_left=60
count=0
word_snap=''
miss = 0
hit=0
# Labels ######################################################################

win_label = Label(windows_frame,text="",font=('arial',21,'italic bold'),bg="pink",fg="red")
win_label.pack(side=TOP)
label_slider()
random.shuffle(words)
word_label=Label(windows_frame,text=words[0],font=('arial',27,'italic bold'),bg="pink")
word_label.place(x=240,y=130)

score_label=Label(windows_frame,text="Your Score : : ",font=('arial',16,'italic bold'),bg="pink",fg="purple").place(x=10,y=70)

score_counter=Label(windows_frame,text=score,font=('arial',16,'italic bold'),bg="pink",fg="blue")
score_counter.place(x=160,y=70)

time_counter=Label(windows_frame,text="Time Left :: ",font=('arial',16,'italic bold'),bg="pink",fg="blue").place(x=400,y=70)

time_left_lb=Label(windows_frame,text=time_left,font=('arial',16,'italic bold'),bg="pink",fg="blue")
time_left_lb.place(x=530,y=70)

game_play_detail_label=Label(windows_frame,text="Type Word And Hit Enter",font=('arial',16,'italic bold'),bg="pink",fg="white")
game_play_detail_label.place(x=180,y=270)

# Entry Box #####################################################################

wordEntry = Entry(windows_frame,font=('arial',18,'italic bold'),bg="powder blue",fg="blue",relief="ridge",justify="center")
wordEntry.place(x=170,y=200)
wordEntry.focus_set()

# Key's Binding ##################################################################

windows_frame.bind('<Return>',startgame)

windows_frame.mainloop()