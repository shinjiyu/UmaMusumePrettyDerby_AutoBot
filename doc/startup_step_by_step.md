### 用法说明

#### 需要安装的库 
 * pillow
 * pyperclip
 * opencv-python


#### 新帐号导入
在NewData/newAccount.txt中保存新帐号。
运行tools/importNewAccount.py

#### task管理流程
1. 在deviceManager.py中的start函数中，会启动所有的设备任务。
2. 如果设备当前没有任务，会运行登录任务。
3. 如果设备当前的任务已经完成，会继续下一个任务。
4. 在deviceAgent.py中，可以通过initialTasks函数初始化任务。
5. 可以通过addTask函数添加新的任务。
6. 在main.py中，会设置账户信息，并保存账户数据。
7. 最后，会启动deviceManager开始任务。
