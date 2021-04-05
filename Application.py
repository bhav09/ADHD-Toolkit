#dependencies
from tkinter import Label,Button,Entry,PhotoImage,Tk,Menu,Toplevel
import keyboard
from PIL import Image,ImageTk
from selenium import webdriver
import random
import time

def info():
    inf = Toplevel()
    inf.geometry('600x300')
    inf.resizable(0, 0)
    inf.configure(background='AntiqueWhite1')
    inf.title('Information')

    overview = Image.open('overview.JPG').convert('RGB')
    overview = overview.resize((int(260), int(250)), Image.ANTIALIAS)
    overview.save('overview.ppm', 'ppm')
    overview = PhotoImage(file='overview.ppm')

    cases = Image.open('cases.JPG').convert('RGB')
    cases = cases.resize((int(320), int(250)), Image.ANTIALIAS)
    cases.save('cases.ppm', 'ppm')
    cases = PhotoImage(file='cases.ppm')

    title = Label(inf,text='ADHD in BRIEF',bg='AntiqueWhite1',fg='black',font=('bold',12))
    title.place(x=260,y=10)

    label = Label(inf,image=overview)
    label.place(x=10,y=40)
    label.photo = overview

    case = Label(inf, image=cases)
    case.place(x=260, y=40)
    case.photo = cases

def download():
    global enter_city,doc,root
    city = enter_city.get()
    print(city)
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome('chromedriver.exe',options=option)
    #driver = webdriver.Chrome('chromedriver.exe')
    url = f'https://www.practo.com/{city}/doctors-for-attention-deficit-hyperactivity-disorder-adhd-treatment'
    driver.get(url)

    time.sleep(3)
    details = driver.find_elements_by_class_name('info-section')
    for detail in details:
        print(detail.text)
        print('----------------------------------------')
    driver.quit()
    doc.destroy()
    root.destroy()

def doctors():
    global enter_city,doc

    doc = Toplevel()
    doc.geometry('600x300')
    doc.resizable(0, 0)
    doc.configure(background='AntiqueWhite1')
    doc.title('Doctors')

    menu = Menu(root)
    option = Menu(menu, tearoff=0)
    option.add_command(label='Info', command=info)
    option.add_separator()
    option.add_command(label="Exit", command=root.quit)
    menu.add_cascade(label="About", menu=option)

    help = Menu(menu, tearoff=0)
    help.add_command(label='Doctor info', command=doctors)
    menu.add_cascade(label="Help", menu=help)
    root.config(menu=menu)

    doc_menu = Menu(doc)
    doc_option = Menu(doc_menu, tearoff=0)
    doc_option.add_command(label='Info', command=info)
    doc_option.add_separator()
    doc_option.add_command(label="Exit", command=doc.destroy)
    doc_menu.add_cascade(label="About", menu=doc_option)

    doc_help = Menu(doc_menu, tearoff=0)
    doc_help.add_command(label='Doctor info', command=doctors)
    doc_menu.add_cascade(label="Help", menu=doc_help)
    doc.config(menu=doc_menu)

    doc_img = Image.open('doctor.jpg').convert('RGB')
    doc_img = doc_img.resize((int(150), int(150)), Image.ANTIALIAS)
    doc_img.save('doc.ppm', 'ppm')
    doc_img = PhotoImage(file='doc.ppm')

    details = Label(doc,text='Download Details',font=('bold',15),bg='AntiqueWhite1',fg='black')
    details.place(x=230,y=20)

    label = Label(doc,image=doc_img)
    label.place(x=370,y=80)

    city = Label(doc,text='City',font=('bold',13),bg='AntiqueWhite1')
    city.place(x=70,y=120)
    enter_city = Entry(doc,bg='white',fg='black')
    enter_city.place(x=120,y=122)

    dload = Button(doc,text='Download',font=('bold',11),bg='white',fg='black',activebackground='orange',command=download)
    dload.place(x=85,y=150)

    doc.mainloop()

def result():
    global longest_sequence,scorecard
    scorecard += 1
    app()

def WhiteBoard():
    global count,correct,longest_sequence
    if count == 0:
        print(input('Press Enter to Continue:'))
    img1 = Image.open('blob.png').convert('RGB')
    img1 = img1.resize((int(650), int(400)), Image.ANTIALIAS)
    img1.save('board.ppm', 'ppm')
    white_board = PhotoImage(file='board.ppm')
    board = Label(root_test, image=white_board)
    board.place(x=120, y=80)
    board.photo = white_board
    x = random.randint(130, 650)
    y = random.randint(100, 400)
    pic = random.randint(1, 8)
    if pic == 1:
        img1 = Image.open(f'Images/{1}.jpg').convert('RGB')
        img1 = img1.resize((50, 50), Image.ANTIALIAS)
        ph = ImageTk.PhotoImage(img1)
    if pic == 2:
        img2 = Image.open(f'Images/{2}.jpg').convert('RGB')
        img2 = img2.resize((50, 50), Image.ANTIALIAS)
        ph = ImageTk.PhotoImage(img2)
    if pic == 3:
        img3 = Image.open(f'Images/{3}.jpg').convert('RGB')
        img3 = img3.resize((70, 70), Image.ANTIALIAS)
        ph = ImageTk.PhotoImage(img3)
    if pic == 4:
        img4 = Image.open(f'Images/{4}.jpg').convert('RGB')
        img4 = img4.resize((50, 50), Image.ANTIALIAS)
        ph = ImageTk.PhotoImage(img4)
    if pic == 5:
        img5 = Image.open(f'Images/{5}.jpg').convert('RGB')
        img5 = img5.resize((60, 60), Image.ANTIALIAS)
        ph = ImageTk.PhotoImage(img5)
    if pic == 6:
        img6 = Image.open(f'Images/{6}.jpg').convert('RGB')
        img6 = img6.resize((50, 50), Image.ANTIALIAS)
        ph = ImageTk.PhotoImage(img6)
    if pic == 7:
        img7 = Image.open(f'Images/{7}.jpg').convert('RGB')
        img7 = img7.resize((70, 70), Image.ANTIALIAS)
        ph = ImageTk.PhotoImage(img7)
    if pic == 8:
        img8 = Image.open(f'Images/{8}.jpg').convert('RGB')
        img8 = img8.resize((70, 50), Image.ANTIALIAS)
        ph = ImageTk.PhotoImage(img8)
    arrow = Label(root_test, image=ph,bg='white')
    arrow.place(x=x, y=y)
    arrow.photo = ph
    if pic % 2 == 0:
        #print('Left')
        if keyboard.read_key()=='a':
            print('Pressed A')
            correct += 1
        else:
            longest_sequence.append(correct)
            correct = 0
    elif pic % 2 != 0:
        #print('Right')
        if keyboard.read_key()=='l':
            print('Pressed L')
            correct += 1
        else:
            longest_sequence.append(correct)
            correct = 0
    count += 1
    if count < 40:
        root_test.after(400, WhiteBoard)
    if count >= 40:
        root_test.destroy()
        print('Sequence of correct Answers',longest_sequence)
        print('Max Score is:',max(longest_sequence))
        result()

def starttest():
    global root_test,count,correct, longest_sequence
    count,correct = 0,0
    longest_sequence = []
    if enter_age.get() != '' and enter_name.get() != '':
        print('Name is:',enter_name.get())
        print('Age is:',enter_age.get())
        root.destroy()
        root_test = Tk()
        root_test.geometry('900x600')
        root_test.configure(background='AntiqueWhite1')
        root_test.title('Test')
        root_test.resizable(0, 0)
        WhiteBoard()
        root_test.mainloop()

def app():
    global root,enter_age,enter_name,score
    #geomotry of the window
    root = Tk()
    root.geometry('900x600')
    root.configure(background='AntiqueWhite1')
    root.title('ADHD Toolkit')
    root.resizable(0,0)

    #main board iamge
    img1 = Image.open('blob.png')
    img1 = img1.resize((int(450), int(380)), Image.ANTIALIAS)
    img1.save('board.ppm', 'ppm')
    img1 = PhotoImage(file='board.ppm')

    #kid's image
    img2 = Image.open('kid.jpg')
    img2 = img2.resize((320, 320), Image.ANTIALIAS)
    img2.save('kid.ppm', 'ppm')
    img2 = PhotoImage(file='kid.ppm')

    #instructions board
    img3 = Image.open('instructions.png')
    img3 = img3.resize((300, 300), Image.ANTIALIAS)
    img3.save('ins.ppm', 'ppm')
    img3 = PhotoImage(file='ins.ppm')

    menu = Menu(root)
    option = Menu(menu, tearoff=0)
    option.add_command(label='Info',command=info)
    option.add_separator()
    option.add_command(label="Exit", command=root.destroy)
    menu.add_cascade(label="About", menu=option)

    help = Menu(menu, tearoff=0)
    help.add_command(label='Doctor info',command=doctors)
    menu.add_cascade(label="Help", menu=help)
    root.config(menu=menu)

    title = Label(text='ADHD Toolkit',fg='black',bg='AntiqueWhite1',font=('bold',17))
    title.place(x=385,y=15)

    name = Label(text='Name',bg='AntiqueWhite1',fg='black',font=('bold',14))
    name.place(x=20,y=75)
    enter_name = Entry(bg='white',fg='black')
    enter_name.place(x=80,y=80)

    age = Label(text='Age',bg='AntiqueWhite1',fg='black',font=('bold',14))
    age.place(x=20,y=115)
    enter_age = Entry(bg='snow',fg='black')
    enter_age.place(x=80,y=120)

    board_ins = Label(image=img3)
    board_ins.place(x=20,y=160)

    instruction = Label(text='Instructions',bg='white',fg='black',font=('bold',14))
    instruction.place(x=110,y=180)

    ins1 = Label(text='1. Press A for left arrow keys.',bg='white',fg='black',font=('bold',10))
    ins1.place(x=40,y=220)
    ins2 = Label(text='2. Press L for right arrow keys.',bg='white',fg='black',font=('bold',10))
    ins2.place(x=40,y=250)
    ins3 = Label(text='3. Test ends answered incorrectly, thrice.',bg='white',fg='black',font=('bold',10))
    ins3.place(x=40,y=280)
    ins4 = Label(text='4. Delayed answer will not be counted.',bg='white',fg='black',font=('bold',10))
    ins4.place(x=40,y=310)
    ins5 = Label(text='5. If Score<8, go to the help section.',bg='white',fg='black',font=('bold',10))
    ins5.place(x=40,y=340)
    ins6 = Label(text='6. Click on Start Test to begin the test.',bg='white',fg='black',font=('bold',10))
    ins6.place(x=40,y=370)
    ins7 = Label(text='7. Test would start only when you have \nentered the details.',bg='white',fg='black',font=('bold',10))
    ins7.place(x=40,y=400)

    test = Button(text='Start Test',bg='snow',fg='black',font=(11),activebackground='orange',command=starttest)
    test.place(x=100,y=490)

    board = Label(image=img1)
    board.place(x=375,y=80)

    kid = Label(image=img2,bg='white')
    kid.place(x=450,y=105)
    if scorecard != 0:
        img_score = Image.open('scoreboard.png')
        img_score = img_score.resize((452, 60), Image.ANTIALIAS)
        img_score.save('score.ppm', 'ppm')
        img_score = PhotoImage(file='score.ppm')
        scoreboard = Label(root, image=img_score,bg='white')
        scoreboard.place(x=375, y=470)
        score = Label(root, text=f'Score is {max(longest_sequence)}',bg='white',fg='black',font=('bold,13'))
        score.place(x=550,y=490)

    credits = Label(root,bg='AntiqueWhite1',fg='black',text='©Developed by Group 7',height=3,width=110,font=('bold',10))
    credits.place(x=0,y=550)
    root.mainloop()

if __name__ == '__main__':
    scorecard = 0
    print('Welcome to ADHD Tool Kit')
    app()