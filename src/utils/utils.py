
def center_window(window, width, height):
    # Calculate the position to center the window
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (width / 2))
    y_coordinate = int((screen_height / 2) - (height / 2))

    # Set the window's position and size
    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")