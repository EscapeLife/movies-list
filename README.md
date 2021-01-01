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

| 类型转换器 | 作用                 |
| ---------- | -------------------- |
| 缺省       | 字符型；但不能有斜杠 |
| `path:`    | 字符型；可有斜杠     |
| `int:`     | 整型                 |
| `float:`   | 浮点型               |

```python
from flask import Flask
from flask.helpers import url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Welcome to watch list!'

@app.route('/user/<name>')
def user_page(name):
    return f'User page: {name}.'

@app.route('/user/<int:user_id>')
def get_user(user_id):
    return f'User id: {user_id}'

@app.route('/test')
def test_url_for():
    print(url_for('hello'))                    # /
    print(url_for('test_url_for'))             # /test
    print(url_for('user_page', name='peter'))  # /user/peter
    print(url_for('test_url_for', num=2))      # /test?num=2
    return "Test page."
```

---

## 2. 模板使用

### 2.1 基本语法

> **介绍 Jinja2 模板的简单使用！**

按照默认的设置，`Flask` 会从程序实例(`app.py`)所在模块同级目录的 `templates` 文件夹中寻找模板。

- **`{# ... #}`** => 用来书写注释
- **`{{ ... }}`** => 用来标记变量 => 在渲染的时候传递进去
- **`{% ... %}`** => 用来标记语句 => `if` 语句或 `for` 语句

```jinja2
<h1>{{ username }}的个人主页</h1>
{% if bio %}
<p>{{ bio }}</p>
{% else %}
<p>自我介绍为空。</p>
{% endif %}
```

---

### 2.2 模板渲染

> **介绍模板渲染的基本方式！**

使用 `render_template()` 函数可以把模板渲染出来，必须传入的参数为模板文件名（相对于 `templates` 根目录的文件路径），这里即 `index.html` 文件。为了让模板正确渲染，我们还要把模板内部使用的变量通过关键字参数传入这个函数。

`render_template()` 函数在调用时会识别并执行 `index.html` 里所有的 `Jinja2` 语句，返回渲染好的模板内容。在返回的页面中，变量会被替换为实际的值（包括定界符），语句及定界符则会在执行后被移除，同时注释也会一并移除。

```python
from flask import Flask, render_template
from data import movies, name
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)
```

---

### 2.3 过滤器

> **过滤器包括 Jinja2 库中定义的内置过滤器，当然我们也可以自定义过滤器！**

- **[内置过滤器的列表](https://jinja.palletsprojects.com/en/2.10.x/templates/#list-of-builtin-filters)**

![Flask入门指南 - 过滤器](/docs/images/hello-flask-jinjia2-filters.png)

---

### 2.4 继承

`Flask` 的 `Jinja2` 模板支持模板继承功能，可以帮助我们省去了很多重复的代码。

- **layout.html**

```jinja2
<!doctype html>
<title>Hello Sample</title>
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
<div class="page">
    {% block body %}
    {% endblock %}
</div>
```

- **hello.html**

```jinja2
{% extends "layout.html" %}

{% block body %}
{% if name %}
<h1>Hello {{ name }}!</h1>
{% else %}
<h1>Hello World!</h1>
{% endif %}
{% endblock %}
```
