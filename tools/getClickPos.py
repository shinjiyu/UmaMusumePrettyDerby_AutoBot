from tkinter import *
from PIL import Image, ImageTk
import pyperclip

# 创建窗口
root = Tk()
root.title("点击坐标示例")

image_path = "../workspace/16416/tmp.png"
# 打开图片并创建一个Image对象
image = Image.open(image_path)

# 创建一个PhotoImage对象，用于在Tkinter中显示图片
photo = ImageTk.PhotoImage(image)

# 创建一个标签，显示图片
label = Label(root, image=photo)
label.pack()

def reload_image(event):
    global photo  # 使用global关键字来修改全局变量
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)

# 定义一个点击事件处理函数
def on_click(event):
    x, y = event.x, event.y
    print(f"点击坐标：({x}, {y})")
    click_coordinates = f"{x}, {y}"
    pyperclip.copy(click_coordinates)

# 绑定鼠标左键点击事件到标签上
label.bind("<Button-1>", on_click)


# 绑定键盘事件，按下'R'键重新加载图片
root.bind("r", reload_image)
# 运行Tkinter主循环
root.mainloop()