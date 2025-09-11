<img src="icon.png" alt="Xgoat Logo" width="120">

Xgoat 是一款简洁的服务器管理工具，支持以下功能：

- 文件同步（支持自动/手动模式）  
- MySQL 数据库管理（创建/删除库和表，执行 SQL）  
- 一键安装 MySQL（支持 5.7 / 8.0 等版本）  
- SSH 远程连接，支持密码和私钥登录  

使用方法

1. 下载发布页的编译版本（Windows）  
2. 启动后输入服务器连接信息  
3. 选择文件进行同步，或进入 **数据库管理** 标签页操作 MySQL  
4. 注意：第一次连接服务器时，会在服务器根目录下生成一个 `Xgoat` 文件夹  
   - 用于托管接口文件等和客户端交互的文件  
   - 仅托管在 `Xgoat` 文件夹中，方便管理和调试  

开源说明

- 本仓库开源 **UI 层代码**，核心逻辑通过编译产物提供。  

---

Xgoat (English)

Xgoat is a lightweight server management tool with the following features:

- File synchronization (supports automatic/manual modes)  
- MySQL database management (create/drop databases and tables, execute SQL)  
- One-click MySQL installation (supports versions 5.7 / 8.0)  
- SSH remote connection with both password and private key login  

Usage

1. Download the compiled release (Windows) from the release page  
2. Start the program and enter your server connection info  
3. Select files for synchronization, or switch to the **Database Management** tab to manage MySQL  
4. Note: On the first connection, a `Xgoat` folder will be created in the server root directory  
   - Used to store interface files for client-server interaction  
   - Restricted to `Xgoat` folder only for easier management and debugging  

Open Source Notice

- This repository only open-sources the **UI layer code**.  
- Core logic is provided through compiled binaries.  

---

MIT License
