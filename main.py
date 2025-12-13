# Modules
from guizero import App, Text, Box, ListBox, TextBox, Combo, ButtonGroup, Slider, Drawing
import os 
# Functions + variables
def draw_text_recolor():
    global text_entry
    global color_entry
    global x_entry
    global y_entry
    global font_entry
    global sticker_entry
    global image_entry
    global canvas
    global canvas_2
    canvas.clear()
    txt = text_entry.value
    colr = color_entry.value.lower()
    x = int(x_entry.value)
    y = int(y_entry.value)
    fon = font_entry.value
    imgae = image_entry.value
    canvas.image(x, y, image = imgae, width = 300, height = 300)
    canvas.text(x, y, text = txt, color = colr, font = fon)


    if sticker_entry.value == "Oval":
        canvas.oval(x + 50, y + 50, x + 80, y + 80)
    elif sticker_entry.value == "Triangle":
        canvas.polygon(x + 50, y + 100, x + 100, y, x + 150,y + 100, color="black")
    else:
        canvas.rectangle(x + 30, y + 30, x + 50, y + 50)

def import_png():
    global image_entry
    image_entry.clear()  # prevents duplicates!

    for file in os.listdir():
        if file.lower().endswith(".png") or file.lower().endswith(".jpg"):
            image_entry.append(file)

# GUI part
window = App(title = "Meme Editor")

text_editor_box = Box(window, layout = "grid", border = 5)
text_editor_box.bg = "lightblue"
txt1 = Text(text_editor_box, text = "Enter text: ", grid = [0, 0])
text_entry = TextBox(text_editor_box, width = 30, grid = [1, 0], command = draw_text_recolor)
txt2 = Text(text_editor_box, text = "Select text color: ", grid = [0, 1])
color_entry = Combo(text_editor_box, options = ["Black", "Red", "Blue", "Green"], grid = [1, 1], command = draw_text_recolor)
txt3 = Text(text_editor_box, text = "Select font", grid = [0, 2])
font_entry = ButtonGroup(text_editor_box, options = ["Times New Roman", "Arial", "Courier"], grid = [1, 2], command = draw_text_recolor)

meme_sticker_box = Box(window, layout = "grid", border = 5)
meme_sticker_box.bg = "orange"
txt4 = Text(meme_sticker_box, text = "Select meme sticker: ", grid = [0, 0])
sticker_entry = Combo(meme_sticker_box, options = ["Oval", "Triangle", "Rectangle"], grid = [1, 0], command = draw_text_recolor)
txt5 = Text(meme_sticker_box, text = "X: ", grid = [0, 1])
x_entry = Slider(meme_sticker_box, start = 0, end = 250, grid = [1, 1], command = draw_text_recolor)
txt6 = Text(meme_sticker_box, text = "Y: ", grid = [0, 2])
y_entry = Slider(meme_sticker_box, start = 0, end = 250, grid = [1, 2], command = draw_text_recolor)

canvas_box = Box(window, layout = "grid")
image_entry = ListBox(canvas_box, grid = [0, 0], items = [], command = draw_text_recolor)
import_png()

canvas = Drawing(canvas_box, grid =[1, 0], width = 300, height = 300)

window.display()