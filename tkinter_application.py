import tkinter as tk
from tkinter import ttk

class FacultyConfigApp:
    def __init__(self, root):
        self.root = root
        self.root.title("University Faculty Configuration")

        # Creating notebook for tabs
        self.notebook = ttk.Notebook(root)

        # Tab for adding and updating faculty
        self.faculty_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.faculty_tab, text="Faculty Management")

        # Adding notebook to the main window
        self.notebook.pack(expand=1, fill="both")

        # Initialize variables
        self.faculty_list = []
        self.selected_index = None

        # Adding faculty tab widgets
        self.faculty_widgets()

    def faculty_widgets(self):
        # Frame for entry widgets
        entry_frame = ttk.Frame(self.faculty_tab)
        entry_frame.pack(padx=10, pady=10)

        # Label and Entry for Employee Id
        tk.Label(entry_frame, text="Employee Id:").grid(row=0, column=0, padx=5, pady=5)
        self.employee_id_entry = tk.Entry(entry_frame)
        self.employee_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Label and Entry for Employee Name
        tk.Label(entry_frame, text="Employee Name:").grid(row=1, column=0, padx=5, pady=5)
        self.employee_name_entry = tk.Entry(entry_frame)
        self.employee_name_entry.grid(row=1, column=1, padx=5, pady=5)

        # Label and Entry for Mobile
        tk.Label(entry_frame, text="Mobile:").grid(row=2, column=0, padx=5, pady=5)
        self.mobile_entry = tk.Entry(entry_frame)
        self.mobile_entry.grid(row=2, column=1, padx=5, pady=5)

        # Label and Entry for Salary
        tk.Label(entry_frame, text="Salary:").grid(row=3, column=0, padx=5, pady=5)
        self.salary_entry = tk.Entry(entry_frame)
        self.salary_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons for operations
        tk.Button(entry_frame, text="Add", command=self.add_faculty).grid(row=4, column=0, pady=10)
        tk.Button(entry_frame, text="Update", command=self.update_faculty).grid(row=4, column=1, pady=10)
        tk.Button(entry_frame, text="Delete", command=self.delete_faculty).grid(row=4, column=2, pady=10)

        # Treeview to display faculty information
        self.faculty_tree = ttk.Treeview(self.faculty_tab, columns=("Employee Id", "Employee Name", "Mobile", "Salary"), show="headings")
        self.faculty_tree.heading("Employee Id", text="Employee Id")
        self.faculty_tree.heading("Employee Name", text="Employee Name")
        self.faculty_tree.heading("Mobile", text="Mobile")
        self.faculty_tree.heading("Salary", text="Salary")
        self.faculty_tree.pack(padx=10, pady=10)

        # Binding treeview click event
        self.faculty_tree.bind("<ButtonRelease-1>", self.on_tree_click)

        # Update the Treeview with initial data
        self.update_faculty_tree()

    def add_faculty(self):
        # Get values from entry widgets
        employee_id = self.employee_id_entry.get()
        employee_name = self.employee_name_entry.get()
        mobile = self.mobile_entry.get()
        salary = self.salary_entry.get()

        # Add faculty to the list
        self.faculty_list.append({"Employee Id": employee_id, "Employee Name": employee_name, "Mobile": mobile, "Salary": salary})

        # Clear entry widgets
        self.employee_id_entry.delete(0, tk.END)
        self.employee_name_entry.delete(0, tk.END)
        self.mobile_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)

        # Update the Treeview
        self.update_faculty_tree()

    def update_faculty(self):
        # Check if a faculty record is selected
        if self.selected_index is not None:
            # Get values from entry widgets
            employee_id = self.employee_id_entry.get()
            employee_name = self.employee_name_entry.get()
            mobile = self.mobile_entry.get()
            salary = self.salary_entry.get()

            # Update the selected faculty record
            self.faculty_list[self.selected_index] = {"Employee Id": employee_id, "Employee Name": employee_name, "Mobile": mobile, "Salary": salary}

            # Clear entry widgets and reset selected_index
            self.employee_id_entry.delete(0, tk.END)
            self.employee_name_entry.delete(0, tk.END)
            self.mobile_entry.delete(0, tk.END)
            self.salary_entry.delete(0, tk.END)
            self.selected_index = None

            # Update the Treeview
            self.update_faculty_tree()

    def delete_faculty(self):
        # Check if a faculty record is selected
        if self.selected_index is not None:
            # Delete the selected faculty record
            del self.faculty_list[self.selected_index]

            # Clear entry widgets and reset selected_index
            self.employee_id_entry.delete(0, tk.END)
            self.employee_name_entry.delete(0, tk.END)
            self.mobile_entry.delete(0, tk.END)
            self.salary_entry.delete(0, tk.END)
            self.selected_index = None

            # Update the Treeview
            self.update_faculty_tree()

    def on_tree_click(self, event):
        # Get the selected item in the Treeview
        selected_item = self.faculty_tree.selection()
        
        if selected_item:
            # Get the index of the selected item
            index = self.faculty_tree.index(selected_item[0])

            # Display the selected faculty record in entry widgets
            faculty = self.faculty_list[index]
            self.employee_id_entry.delete(0, tk.END)
            self.employee_id_entry.insert(0, faculty["Employee Id"])
            self.employee_name_entry.delete(0, tk.END)
            self.employee_name_entry.insert(0, faculty["Employee Name"])
            self.mobile_entry.delete(0, tk.END)
            self.mobile_entry.insert(0, faculty["Mobile"])
            self.salary_entry.delete(0, tk.END)
            self.salary_entry.insert(0, faculty["Salary"])

            # Update the selected_index
            self.selected_index = index

    def update_faculty_tree(self):
        # Clear existing items in the Treeview
        for item in self.faculty_tree.get_children():
            self.faculty_tree.delete(item)

        # Insert new faculty information into the Treeview
        for faculty in self.faculty_list:
            self.faculty_tree.insert("", "end", values=(faculty["Employee Id"], faculty["Employee Name"], faculty["Mobile"], faculty["Salary"]))

if __name__ == "__main__":
    root = tk.Tk()
    app = FacultyConfigApp(root)
    root.mainloop()
