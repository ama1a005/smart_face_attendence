import tkinter as tk 
import util
import cv2
from PIL import Image,ImageTk
import os
import subprocess
import face_recognition 
import datetime


class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x520+350+100")

        self.login_button_main_window = util.get_button(self.main_window,"login","green",self.login)
        self.login_button_main_window.place(x=750,y = 300)


        self.register_user_main_window = util.get_button(self.main_window,"register new user","grey",self.register_new_user,fg = "black")
        self.register_user_main_window.place(x=750,y=400)

        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10,y=0,width=700,height=500)

        self.add_webcam(self.webcam_label)
        self.db_dir = "./db"
        self.logs = "./log.txt"

        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

    def add_webcam(self,label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)

        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret,frame =  self.cap.read()
        self.most_recent_capture_arr = frame

        img_ = cv2.cvtColor(self.most_recent_capture_arr,cv2.COLOR_BGR2RGB)

        self.most_recent_capture_pil = Image.fromarray(img_)

        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)

        self._label.imgtk = imgtk
        self._label.configure(image = imgtk)


        self._label.after(20,self.process_webcam)


    def login(self):
       
       unknown_img_path = './.tmp.jpg'
       cv2.imwrite(unknown_img_path, self.most_recent_capture_arr)
       output = subprocess.check_output(['face_recognition', '--tolerance', '0.5', self.db_dir, unknown_img_path])

       
       #output =  subprocess.check_output(['face_recognition',self.db_dir,unknown_img_path])
       output_str = output.decode('utf-8')
       output_str = output_str.strip()
       output_list = output_str.split(',')
       output_name =output_list[-1].replace("\r","").replace("\n","")
       print(output_name)
       os.remove(unknown_img_path)

       if output_name in ['unknown_person','no_persons_found']:
           util.msg_box("Sorry","Unknown user found...Try again or Register new user")
       else :
           util.msg_box("Login Successfull","Welcome {}".format(output_name))
           with open(self.logs,'a') as f:
               f.write("{},{} \n".format(output_name,datetime.datetime.now()))
               f.close()
           
       
    def register_new_user(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window.geometry("1200x520+350+100")


        self.accept_button_register_new_user = util.get_button(self.register_new_user_window,"Accept","Green",self.accept_register_new_user,fg='white')
        self.accept_button_register_new_user.place(x=750,y=300)

        self.try_again_button_register_new_user = util.get_button(self.register_new_user_window,"Try Again","Red",self.try_again_register_new_user,fg = "white")
        self.try_again_button_register_new_user.place(x=750,y=400)

        self.capture_label = util.get_img_label(self.register_new_user_window)
        self.capture_label.place(x=10,y=0,width=700,height=500)

        self.add_image_to_label(self.capture_label)

        self.entry_text_register_new_user = util.get_entry_text(self.register_new_user_window)
        self.entry_text_register_new_user.place(x=750,y=150)
        self.text_label_register_new_user = util.get_text_label(self.register_new_user_window,"Please enter your Name:")
        self.text_label_register_new_user.place(x=750,y=100)


    #putting the frame captured into the label created the registered user
    def add_image_to_label(self,label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image = imgtk)

        self.register_new_user_capture = self.most_recent_capture_arr.copy()

        self.register_new_user_capture


    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()

    def accept_register_new_user(self):
        name = self.entry_text_register_new_user.get(1.0,"end-1c")

        cv2.imwrite(os.path.join(self.db_dir,'{}.jpg'.format(name)),self.register_new_user_capture)
        util.msg_box('Success!',"User was registered successfully")

        self.register_new_user_window.destroy()

    def start(self):
        self.main_window.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
