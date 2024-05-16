import customtkinter
from tkinter import filedialog, Text
import os


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.geometry('505x739')


appsGroups = []





while root.winfo_viewable:
	activeScreen = 'main'
	def setActiveScreen(screen):
		activeScreen=screen
	print(activeScreen)
	match activeScreen:
		case 'main':
			frame = customtkinter.CTkFrame(master=root)
			frame.pack_configure(expand=True, fill='both')
			frame.pack()
			def addApps():
				frame.destroy()
				setActiveScreen('add')
			addAppsButton = customtkinter.CTkButton(bg_color='#111010', text_color='#5A63B6',corner_radius=10, command=addApps, master=frame)
			addAppsButton.pack()

			
		case 'add':
			apps = []
			def addApp():
				filename = filedialog.askopenfilename(initialdir='/Applications',filetypes=(('executables', '*.app')), title='Select app to add')
				apps.append(filename)

			frame = customtkinter.CTkFrame(master=root)
			frame.pack_configure(expand=True, fill='both')
			frame.pack()
		case _:
			print('screen is not set', activeScreen)



root.mainloop()









