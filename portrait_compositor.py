import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

# 创建UI界面
root = tk.Tk()
root.title("证件照生成UI")
root.geometry("400x300")

# 定义函数：导入背景图片
def import_background_image():
    global background_image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    background_image = Image.open(file_path)
    background_image = background_image.resize((1004, 1542))  # 调整背景图片的大小适应UI界面
    background_label.config(text="背景图片已导入")

# 定义函数：导入人像照片
def import_portrait_image():
    global portrait_image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    portrait_image = Image.open(file_path)
    portrait_image = portrait_image.resize((407, 554))  # 调整人像照片的大小为一寸大小
    portrait_label.config(text="人像照片已导入")

# 定义函数：导出合成图片
def export_image():
    name = name_entry.get()
    position = position_entry.get()
#     x = entry_x.get()
#     y = entry_y.get()

    output_image = background_image.copy()
    output_image.paste(portrait_image, (422, 600))  # 将人像照片固定位置放置在背景图片上 422 600
    
    draw = ImageDraw.Draw(output_image)

    # font_path = "/Users/geyaogang/Desktop/证件照批处理/arial.ttf"
    # font = ImageFont.truetype(font_path, size=16)  # 设置姓名和职务的字体和大小
    try:
        # Try loading the specified font
        font_path = "/Users/geyaogang/Desktop/证件照批处理/arial.ttf"
        font = ImageFont.truetype(font_path, size=20)
    except IOError:
        # Fallback to default font if specified font is not available
        font = ImageFont.load_default()


    draw.text((778.8, 1204), name, font=font)
    draw.text((778.8, 1274), position, font=font)

    output_image.save(f"{name}的证件照.png", "PNG")  # 导出合成图片
    export_label.config(text="图片已成功导出")

# 创建背景图片导入按钮
background_button = tk.Button(root, text="导入背景图片", command=import_background_image)
background_button.pack()

# 创建人像照片导入按钮
portrait_button = tk.Button(root, text="导入人像照片", command=import_portrait_image)
portrait_button.pack()


# 创建文本输入框和标签
name_label = tk.Label(root, text="姓名：")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

position_label = tk.Label(root, text="职务：")
position_label.pack()
position_entry = tk.Entry(root)
position_entry.pack()

# # 创建输入框和标签
# label_x = tk.Label(root, text="人像X坐标:")
# label_x.pack()
# entry_x = tk.Entry(root)
# entry_x.pack()

# label_y = tk.Label(root, text="人像Y坐标:")
# label_y.pack()
# entry_y = tk.Entry(root)
# entry_y.pack()

# 创建导出按钮
export_button = tk.Button(root, text="导出图片", command=export_image)
export_button.pack()

# 创建状态标签
background_label = tk.Label(root, text="未导入背景图片")
background_label.pack()

portrait_label = tk.Label(root, text="未导入人像照片")
portrait_label.pack()

export_label = tk.Label(root, text="")
export_label.pack()

root.mainloop()
