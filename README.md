# Flask 入门指南

> **李辉(GreyLi) - Flask 入门教程**

使用 `Python` 和 `Flask` 开发你的第一个 `Web` 程序！

- [flask-tutorial](https://github.com/greyli/flask-tutorial)

---

## 1. 入门指南

## 1.1 准备工作

> **记录安装 Flask 需要依赖的相关库及其作用！**

```bash
# 安装
$ pip install flask

# 依赖
$ pip list --format=columns
Package      Version
------------ -------
Flask        1.1.2
click        7.1.2   # 命令行
itsdangerous 1.1.0   # 签名模块
Jinja2       2.11.2  # 模板语言
MarkupSafe   1.1.1   # 模板加速
Werkzeug     1.0.1   # WSGI
```

---

## 1.2 示例代码剖析

> **剖析示例 Flask 代码的相关参数和对应介绍！**

- **第 1-2 行**
  - 从 `flask` 包导入 `Flask` 类，通过实例化这个类，创建一个程序对象 `app`。
  - 其中给 `Flask` 类传入的 `__name__` 是
- **第 4-6 行**
  - 注册一个视图函数，用于处理请求。
  - 使用 `app.route()` 装饰器来为这个函数绑定对应的 `URL`，当用户在浏览器访问这个 `URL` 的时候，就会触发这个函数，获取返回值并把返回值显示到浏览器窗口。

```python
# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to watch list!'
```

```bash
# 默认为production的运行环境
➜ flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [31/Dec/2020 15:42:11] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [31/Dec/2020 15:42:12] "GET /favicon.ico HTTP/1.1" 404 -
```

---

## 1.3 程序发现机制

> **Flask 中引入环境变量的原因！**

如果我们将上述的示例代码的文件名称修改为其他名称，接着执行 `flask run` 命令会返回一个错误提示。这是因为 `Flask` 默认会假设你把程序存储在名为 `app.py` 或 `wsgi.py` 的文件中。如果你使用了其他名称，就要设置系统环境变量 `FLASK_APP` 来告诉 `Flask` 你要启动哪个程序。这也是为什么 `Flask` 中存在大量环境变量的原因。

`Flask` 通过读取这个环境变量值对应的模块寻找要运行的程序实例，你可以把它设置成下面这些值：**模块名**、**Python 导入路径**和**文件目录路径**。

- **FLASK_APP**
  - 用来设置程序运行入口
- **FLASK_ENV**
  - 用来设置程序运行的环境，默认值为 `production` 环境。
  - 如果需要开启调试模式的话，可以将其值设置为 `development` 即可开启。
  - 调试模式中可以显示错误信息，以及在代码发生变动之后，程序会自动重载。
- **python-dotenv**
  - 通过安装 `python-dotenv` 专业的工具，来管理系统的环境变量。
  - 其中 `.env` 则用来存储敏感数据，不应该提交进 `Git` 仓库。
  - 其中 `.flaskenv` 用来存储 `Flask` 命令行系统相关的公开环境变量。

```bash
# 安装
$ pip install python-dotenv
```

---

## 1.4 视图函数

> **介绍视图函数的作用和使用方式！**

**视图函数**的名字是自由定义的，和 `URL` 规则无关。和定义其他函数或变量一样，只需要让它表达出所要处理页面的含义即可。

除此之外，它还有一个重要的作用：作为代表某个路由的**端点**(`endpoint`)，同时用来生成 `URL`。对于程序内的 `URL`，为了避免手写，`Flask` 提供了一个 `url_for` 函数来生成 `URL`，它接受的第一个参数就是端点值，默认为视图函数的名称。

```python
from flask import Flask
from flask.helpers import url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to watch list!'

@app.route('/user/<name>')
def user_page(name):
    return f'User page: {name}.'

@app.route('/test')
def test_url_for():
    print(url_for('hello'))                    # /
    print(url_for('test_url_for'))             # /test
    print(url_for('user_page', name='peter'))  # /user/peter
    print(url_for('test_url_for', num=2))      # /test?num=2
    return "Test page."
```
