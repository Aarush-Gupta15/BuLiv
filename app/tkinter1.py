import tkinter as tk
from tkinter import ttk

def setText(text):
    
    text_field.focus_set()
    text_field.delete('1.0', tk.END)
    text_field.insert(tk.END,text)

def add():
    
    text_field.focus_set()
    global val
    val=text_field.get("1.0",tk.END)
    print(val)

def result():
    
    text_field.focus_set()
    val2=text_field.get("1.0",tk.END)
    result=0
    result = int(val) + int(val2)
    text_field.delete('1.0', tk.END)
    text_field.insert(tk.END,result)
    print(result)
    
    
# root window
root = tk.Tk()

root.geometry('500x500')
root.resizable(False, False)
root.title('Button Demo')

button1 = ttk.Button(root,text="1",command=lambda: setText("1"))
button2 = ttk.Button(root,text="2",command=lambda: setText("2"))
button3 = ttk.Button(root,text="+",command=lambda: add())
button4 = ttk.Button(root,text="=",command=lambda: result())
text_field = tk.Text(root, height = 5, width = 52)

button1.pack()
button2.pack()
button3.pack()
button4.pack()
text_field.pack()



# exit_button = ttk.Button(root,text='Exit',command=lambda: root.quit())

# text_field.pack()
# exit_button.pack()

root.mainloop()

