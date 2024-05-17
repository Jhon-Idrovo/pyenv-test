import customtkinter

class Setup:
	def __init__(self,setup_name,setup_apps):
		self.name = setup_name
		self.apps = setup_apps
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
		self.add_setup_button = customtkinter.CTkButton(self.footer_frame, text='Add', width=self.winfo_vrootwidth(), corner_radius=0)
		self.cancel_add_setup_button = customtkinter.CTkButton(self.footer_frame, corner_radius=00, text='Cancel')

		# Start the footer with the add button
		self.add_setup_button.pack()
		self.selected_frame_by_name = 'setups'
	def build_setups(self):
		dummy_setups = [{'name':'Test Setup', 'apps':['/Users/jhonidrovo/Applications/Loom.app']},{'name':'Test Setup 2', 'apps':['/Users/jhonidrovo/Applications/Loom.app']}, {'name':'Test Setup 3', 'apps':['/Users/jhonidrovo/Applications/Loom.app']}]
		self.setups_grid = customtkinter.CTkFrame(self.main_frame, fg_color='transparent', width=self.winfo_vrootwidth(), corner_radius=0)
		self.setups_grid.grid_columnconfigure(0, weight=1, pad=10)
		self.setups_grid.grid_columnconfigure(1, weight=1, pad=10)
		self.setups_grid.grid_rowconfigure(0, weight=1, pad=10)
		rows = [[]]
		for setup in dummy_setups:
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

if __name__ == "__main__":
    app = App()
    app.mainloop()