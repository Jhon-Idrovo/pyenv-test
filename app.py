import customtkinter
import os
import json
from customtkinter import filedialog
class Setup:
	def __init__(self,main_frame:customtkinter.CTkFrame, close_adding_setup):
		self.main_frame = main_frame
		self.close_adding_setup = close_adding_setup

		name_input_label = customtkinter.CTkLabel(self.main_frame, text='Workbench Name')
		name_input_label.pack()

		self.name_input = customtkinter.CTkEntry(self.main_frame)
		self.name_input.pack()

		self.apps_list_render = customtkinter.CTkFrame(self.main_frame)
		self.apps_list_render.pack()

		add_app_button = customtkinter.CTkButton(self.main_frame, text='Add App', command=self.add_app)
		add_app_button.pack()

		finish_adding_setup_button = customtkinter.CTkButton(self.main_frame, text='Finish Adding Setup', command=self.finish_adding_setup)
		finish_adding_setup_button.pack()

		self.apps = []

	def add_app(self):
		filename = filedialog.askopenfilename(title='Select app executable', filetypes=(('executables', '*.app'),('All files', '*.*')))
		self.apps.append(filename)
		app_label = customtkinter.CTkLabel(self.apps_list_render, text=filename)
		app_label.pack()
	
	def finish_adding_setup(self):
		print(self.name_input.keys)
		print(self.name_input._state)
		setup_to_add = {'name':self.name_input._state,'apps':self.apps}
		if os.path.isfile('data.json'):
			with open('data.json','+r') as f:
				data = f.read()
				json_setups = json.loads(data)
				self.setups = json_setups['setups']
				self.setups
		self.close_adding_setup()


class App(customtkinter.CTk):
	def __init__(self):
		super().__init__()

		self.title("Workbench Setup")
		self.geometry('350x700')

		# Configure grid layout
		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(1, weight=0)
		self.grid_columnconfigure(0, weight=1)

		# Create main frame
		self.main_frame = customtkinter.CTkFrame(self)
		self.main_frame.grid(column=0, row=0, sticky=customtkinter.NSEW)
		self.build_setups()

		# Create footer frame
		self.footer_frame = customtkinter.CTkFrame(self)
		self.footer_frame.grid(column=0, row=1, sticky=customtkinter.EW)

		# Create options for the footer
		self.add_setup_button = customtkinter.CTkButton(self.footer_frame, text='Add', width=self.winfo_vrootwidth(), corner_radius=0,command=self.add_setup)
		self.cancel_add_setup_button = customtkinter.CTkButton(self.footer_frame, width=self.winfo_vrootwidth(), corner_radius=0, text='Cancel', command=self.cancel_adding_setup)

		# Start the footer with the add button
		self.add_setup_button.pack()
		self.selected_frame_by_name = 'setups'
	def build_setups(self):
		if os.path.isfile('data.json'):
			with open('data.json','r') as f:
				data = f.read()
				print(data)
				self.setups = json.loads(data)['setups']

		self.setups_grid = customtkinter.CTkFrame(self.main_frame, fg_color='transparent', width=self.winfo_vrootwidth(), corner_radius=0)
		self.setups_grid.grid_columnconfigure(0, weight=1, pad=10)
		self.setups_grid.grid_columnconfigure(1, weight=1, pad=10)
		self.setups_grid.grid_rowconfigure(0, weight=1, pad=10)
		rows = [[]]
		for setup in self.setups:
			setup_button = customtkinter.CTkButton(self.setups_grid, text=setup['name'], height=140)
			row_index = len(rows)-1
			row = rows[row_index]
			if len(row)==2:
				row[0].grid(column=0, row=row_index)
				row[1].grid(column=1, row=row_index)
				self.setups_grid.grid_rowconfigure(row_index+1, weight=1, pad=10)
				rows.append([setup_button])
			else:
				row.append(setup_button)
		# Attach the last row items
		last_row = rows[len(rows)-1]
		for x in range(len(last_row)):
			last_row[x].grid(column=x, row=len(rows)-1)

		self.setups_grid.pack()
		print(rows)
	def add_setup(self):
		# Update main frame
		self.setups_grid.pack_forget()
		print(self.main_frame.winfo_width(), self.main_frame.winfo_screenwidth())
		addSetupFrame = customtkinter.CTkFrame(self.main_frame,width=self.main_frame.winfo_width(),height=self.main_frame.winfo_height())
		setup = Setup(addSetupFrame, self.cancel_adding_setup)
		addSetupFrame.pack()

		# Update footer
		self.add_setup_button.pack_forget()
		self.cancel_add_setup_button.pack()

	def cancel_adding_setup(self):
		pass
if __name__ == "__main__":
    app = App()
    app.mainloop()