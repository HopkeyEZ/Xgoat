import tkinter as tk
from tkinter import ttk, messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Xgoat (UI Demo)")
        self.geometry("800x500")

        # 样式
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TButton", padding=6)

        # 左侧：连接信息
        left = ttk.LabelFrame(self, text="连接信息", padding=10)
        left.pack(side="left", fill="y", padx=10, pady=10)

        ttk.Label(left, text="服务器 IP").pack(anchor="w")
        self.ip = ttk.Entry(left)
        self.ip.pack(fill="x")

        ttk.Label(left, text="用户名").pack(anchor="w", pady=(6,0))
        self.user = ttk.Entry(left)
        self.user.pack(fill="x")

        ttk.Label(left, text="密码").pack(anchor="w", pady=(6,0))
        self.pwd = ttk.Entry(left, show="•")
        self.pwd.pack(fill="x")

        ttk.Button(left, text="测试连接", command=self.not_implemented).pack(pady=(12,0), fill="x")
        ttk.Button(left, text="断开连接", command=self.not_implemented).pack(pady=(6,0), fill="x")

        # 右侧：Notebook（文件同步 / 数据库管理）
        nb = ttk.Notebook(self)
        nb.pack(side="right", expand=True, fill="both", padx=10, pady=10)

        tab_sync = ttk.Frame(nb)
        tab_db = ttk.Frame(nb)
        nb.add(tab_sync, text="文件同步")
        nb.add(tab_db, text="数据库管理")

        ttk.Label(tab_sync, text="这里是文件同步面板（示意）").pack(padx=20, pady=20)
        ttk.Label(tab_db, text="这里是数据库管理面板（示意）").pack(padx=20, pady=20)

    def not_implemented(self):
        messagebox.showinfo("提示", "该功能仅在闭源核心中提供。")

if __name__ == "__main__":
    app = App()
    app.mainloop()
