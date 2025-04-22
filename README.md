# 运维管理面板

这是一个基于Flask的运维管理Web面板，包含控制面板、运维管理、监控和小工具等功能。

## 功能特点
- 响应式布局，适配不同设备
- 智能文件对比工具：
  - 支持左右分栏对比
  - 自动检测文件编码(UTF-8/GBK/UTF-16等)
  - 差异高亮显示
- 简洁直观的运维管理界面
- 模块化代码结构

## 部署要求
1. Python 3.6+
2. Flask 2.0+
3. 浏览器支持：Chrome/Firefox/Edge等现代浏览器

## 安装步骤
```bash
# 克隆仓库
git clone https://github.com/xiaohui-git-web/test.git

# 进入项目目录
cd test

# 安装依赖
pip install flask
```

## 运行方法
```bash
python web-qd.py
```

## 访问地址
http://localhost:8100/

## 注意事项
1. 默认端口为8100，如需修改请编辑web-qd.py
2. 文件对比功能需要两个文件内容才能工作
3. 上传文件大小限制为浏览器默认限制
4. 生产环境建议：
   - 使用WSGI服务器（如Gunicorn）
   - 配置Nginx反向代理
   - 启用HTTPS

## 文件说明
- web-qd.py: Flask主程序
- index.html: 主界面
- control.html: 控制面板
- operation.html: 运维管理
- monitor.html: 监控页面
- tools.html: 小工具页面