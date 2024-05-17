import customtkinter

class App(customtkinter.CTk):
	def __init__(self):
		super().__init__()

		self.title("Workbench Setup")
		self.geometry('300x700')

		# Configure grid layout
		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(1, weight=1)
		self.grid_columnconfigure(0, weight=1)

		# Create main frame
		self.main_frame = customtkinter.CTkFrame(self)
		self.main_frame.grid(column=0, row=0, sticky=customtkinter.NSEW)
		
		# Create footer frame
		self.footer_frame = customtkinter.CTkFrame(self)
		self.footer_frame.grid(column=0, row=1)

		# Create options for the footer
		self.add_setup_button = customtkinter.CTkButton(self.footer_frame, corner_radius=10, text='Add')
		self.cancel_add_setup_button = customtkinter.CTkButton(self.footer_frame, corner_radius=10, text='Cancel')

		# Start the footer with the add button
		self.add_setup_button.pack()