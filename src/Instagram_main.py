from instapy import InstaPy
from instapy import smart_run
from tkinter import *
import tkinter.messagebox

default_comments = ['Nice shot! @{}',
    'I love your profile! @{}',
    u'Your feed is an inspiration :thumbsup:',
    u'Just incredible :open_mouth:',
    'What camera did you use @{}?',
    'Love your posts @{}',
    'Looks awesome @{}',
    'Getting inspired by you @{}',
    u':raised_hands: Yes!',
    u'I can feel your passion @{} :muscle:']

def start(username,password,hashtag = [],comments = [],like_by_hashtag= 0,set_comment = False,set_like= False) :
    if comments[0] == '' :
        comments = default_comments
   
    session = InstaPy(username,password,headless_browser = False)
    with smart_run(session) :
        session.set_blacklist(enabled = True,campaign = 'blacklist')
        session.set_skip_users(skip_private= True,skip_no_profile_pic=True,no_profile_pic_percentage= 100 ,private_percentage = 100)
        
        if like_by_hashtag == 1 : 
            session.like_by_tags(hashtag,amount = 2,randomize = True, interact = True,media = 'Photo')
        if set_like == True : 
            session.set_user_interact(amount = 1 , randomize = True , percentage= 100 , media = 'Photo')
            session.set_do_like(enabled= True,percentage = 70)
        
        if set_comment == True : 
            session.set_comments(comments)
            session.set_do_comment(enabled = True,percentage = 100)


        session.set_dont_like(['#naked', '#sex', '#fight','#nude'])
        session.set_simulation(enabled= True)
        

        session.join_pods()


def main():
    root = Tk()
    root.title("Automating Instagram")
    root.geometry("516x547")
    top = Frame(root)
    top.pack()
    t=Label(top,text="Automating Tasks Instagram",font=("inconsolata",20))
    t.grid(row=0, column=0)

    useridlabel = Label(top,text = "User Id : ",fg="red" ,font=("Inconsolata", 12,'bold'))
    useridlabel.grid(column = 0,row = 2)
    passlabel = Label(top, text = "Password : ",fg="red" ,font=("Inconsolata", 12,'bold'))
    passlabel.grid(column = 0 , row = 3)

    getuserid = Entry(top  ,bg = 'white',bd=4,width = 40)
    getuserid.grid(column = 1,row= 2)
    getpassid = Entry(top, bg = 'white',bd=4,width = 40)
    getpassid.grid(column = 1, row = 3)

    #Text box for comments

    textboxcomment = Text(top,bd = 5, height = 7 , width = 40  )
    textboxcomment.grid(column = 1, row = 4,padx = 10, pady = 10 )
    textboxlabel = Label(top,text= "Comments ",font=("Inconsolata", 12,'bold'))
    textboxlabel.grid(column = 0 , row = 4)


    #text box for hashtags
    texthashtags = Text(top,bd = 5,height = 7 , width = 40 )
    texthashtags.grid(column = 1,row = 5,padx = 10, pady = 10 )

    text_hashtag_label = Label(top, text = "Hashtags ",font=("Inconsolata", 12,'bold'))
    text_hashtag_label.grid(column = 0, row = 5)

    #Menu button for selection for like and comment

    #variable for options
    likevar= BooleanVar()
    commentvar = BooleanVar()
    tagvar= BooleanVar()


    var= IntVar()


    #lets try frame work
    option = Frame(root)
    option.pack()
    radio_tag =Radiobutton(option,text = "Likes by Tags",variable = var,value = 1,font = ("Calibri",10))
    radio_tag.grid(column = 0 , row = 1)
    radio_menu = Radiobutton(option, text = "",variable= var, value = 2, font = ("Calibri",10))
    radio_menu.grid(column = 1, row = 1)
    mb=  Menubutton ( option, text="Options" )
    mb.grid(column = 2, row = 1)
    mb.menu = Menu(mb,tearoff= 0 )
    mb["menu"] = mb.menu
    mb.menu.add_checkbutton(label = "Like Post",variable  = likevar)
    mb.menu.add_checkbutton(label= "Comment on Post",variable= commentvar)




    def dumpstart() :
        hashtaggen= (texthashtags.get("1.0","end-1c").strip().strip().split("\n"))
        commentlist = (textboxcomment.get("1.0","end-1c").strip().split("\n") )

        start(getuserid.get(), getpassid.get() ,hashtag= hashtaggen,comments = commentlist,set_like = likevar.get(), set_comment=commentvar.get(),like_by_hashtag=var.get() )

    #Enter Button
    Enter_Button= Button(option, text ='Enter', activebackground ='red',background = "Green",font=('Calibri', 12, ),command=dumpstart)
    Enter_Button.grid(column = 1,row=10,padx = 10 ,pady=10)




    root.mainloop()


if __name__ == '__main__':
    main()
