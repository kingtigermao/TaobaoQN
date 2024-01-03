import tkinter as tk
from configparser import ConfigParser

def save_data():
    config = ConfigParser()
    config['Settings'] = {
        'Textbox1': entry1.get(),
        'Textbox2': entry2.get()
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def load_data():
    config = ConfigParser()
    config.read('config.ini')

    # 设置默认值为1和2
    textbox1_default = config.get('Settings', 'Textbox1', fallback='1')
    textbox2_default = config.get('Settings', 'Textbox2', fallback='2')

    entry1.delete(0, tk.END)
    entry1.insert(tk.END, textbox1_default)

    entry2.delete(0, tk.END)
    entry2.insert(tk.END, textbox2_default)

# 创建主窗口
root = tk.Tk()
root.title('配置文件示例')

# 创建文本框和标签
label1 = tk.Label(root, text='文本框1:')
label1.grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text='文本框2:')
label2.grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

# 创建保存按钮
save_button = tk.Button(root, text='保存', command=save_data)
save_button.grid(row=2, column=0, columnspan=2, pady=10)

# 加载数据
load_data()

# 运行主循环
root.mainloop()
