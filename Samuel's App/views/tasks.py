import ttkbootstrap as tb
from views.helper import View
from K import *
from json import dumps
import requests as req

class TasksView(View):
    def __init__(self, app):
        super().__init__(app)
        # type = epic common rare legendary
        self.columns = ('title','id','complete','type','description')
        self.create_widgets()

    def create_widgets(self):
        # Add code to display a list of tasks here
        tb.Label(self.frame, 'Welcome to your list', bootstyle= 'secondary', columns=self.columns, show=HEADINGS)

        self.tasks_tree = tb.Treeview(self.frame, bootstyle='info', columns=self.columns, show=HEADINGS)
        self.tasks_tree.pack(expand=TRUE, fill=X, padx=PL, pady=PL)
        self.tasks_tree.heading('title', text="Title")
        self.tasks_tree.heading('id', text="ID")
        self.tasks_tree.heading('complete', text="Completion")
        self.tasks_tree.heading('priority', text="Priority")
        self.tasks_tree.heading('description', text="Description")



        tb.Button(self.frame, text="Tasks List", command=self.get_tasks, bootstyle='info').pack(side=LEFT, padx=10, pady=10)
        tb.Button(self.frame, text="Task Details", command=self.app.show_task_view, bootstyle='info').pack(side=LEFT, padx=10, pady=10)
        tb.Button(self.frame, text="Create Task", command=self.app.show_create_task_view, bootstyle="dark").pack(side=RIGHT, padx=10, pady=10)
        tb.Button(self.frame, text="Update Task", command=self.app.show_update_task_view, bootstyle="success").pack(side=RIGHT, padx=10, pady=10)


    def get_tasks(self):
        self.tasks_tree.



class TaskView(View):
    def __init__(self, app):
        super().__init__(app)
        self.create_widgets()

    def create_widgets(self):
        tb.Label(self.frame, text="Task Manager").pack()
        tb.Button(self.frame, text="Back to View Tasks", command=self.app.show_tasks_view).pack()


class CreateTaskView(View):
    def __init__(self, app):
        super().__init__(app)
        self.task_name_var = tb.StringVar()
        self.task_description_var = tb.StringVar()
        self.create_widgets()

    def create_widgets(self):
        tb.Label(self.frame, text="Task Name:").pack()
        tb.Entry(self.frame, textvariable=self.task_name_var).pack()
        tb.Label(self.frame, text="Description:").pack()
        tb.Entry(self.frame, textvariable=self.task_description_var).pack()

        tb.Button(self.frame, text="Create Task", command=self.create_task).pack()
        tb.Button(self.frame, text="Back", command=self.app.show_task_view).pack()

    def create_task(self):
        # Add your code to create a task here
        task_name = self.task_name_var.get()
        task_description = self.task_description_var.get()

        self.create_toast("Task Created", f"Task '{task_name}' created successfully")

        # After creating the task, show the task page
        self.app.show_task_view()


class TaskApp(tb.Window):
    def __init__(self):
        super.__init__()
        self.title('Task Manager')
        self.geometry('400x300')

        self.authenticated = True
        self.email = tb.StringVar()
        self.token = dict{}

        self.current_view = None
        self.header_frame = None
        self.views = {
            'login' = login.LoginView

        }
