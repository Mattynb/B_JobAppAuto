import PySimpleGUI as sg

def GUI():
    sg.theme('Dark Amber')
    # Create the layout
    layout = [
        [sg.Text('Email:'), sg.Input(default_text= "...@gmail.com", key='email')],
        [sg.Text('Password:'), sg.Input(key='password', password_char='*', default_text='1234567890')],
        [sg.Text('Phone:'), sg.Input(key='phone', default_text='1234567890')],
        [sg.Button('Submit'), sg.Button('Cancel')]
    ]

    # Create the window
    window = sg.Window('Automatic Linkedin Job Search', layout)

    # Run the event loop to process user input
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break

        if event == 'Submit':
            # Process the user's email and password
            email = values['email']
            password = values['password']
            phone = values['phone']
            break

    # Close the window
    window.close()
    
    return email, password, phone



if __name__ == '__main__':
    GUI()