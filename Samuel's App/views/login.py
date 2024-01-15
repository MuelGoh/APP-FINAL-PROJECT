import ttkbootstrap as tb
from K import *
import requests as req
from views.helper import View




class LoginView(View):
    def __init__(self, app):
        super().__init__(app)
        self.email_var = tb.StringVar()
        self.password_var = tb.StringVar()
        self.create_widgets()

    def create_widgets(self):
        email = tb.Label(self.frame, text="Email:")
        email.pack()

        email_entry=tb.Entry(self.frame, textvariable=self.email_var)
        email_entry.pack()

        password = tb.Label(self.frame, text="Password:")
        password.pack()

        password_entry= tb.Entry(self.frame, textvariable=self.password_var, show="#")
        password_entry.pack()

        login_button = tb.Button(self.frame, text="Login", command=self.login, bootstyle=SUCCESS)
        login_button.pack()

    def login(self):
        # Your authentication would need to be implemented here
        email = self.email_var.get()
        password = self.password_var.get()

        auth = req.post(f'{self.app.url}/token', {'username':email, 'password':password}).json()

        if auth.get('access_token'):
            self.app.authenticated = TRUE
            self.app.token = {"access_token": auth.get('access_token'), "token_type": "bearer"}
            self.app.email = email
            self.password_var.set("")
            self.app.show_tasks_view()
        else:
            self.create_toast("401 Error", "Bad Credentials")













