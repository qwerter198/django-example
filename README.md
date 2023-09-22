# Django-example

此範例建立一個簡單的django框架，用來呈現如何建立Django專案並且建立一個表單範例

1. 安裝Django
    
    ```bash
    pip install django
    ```
    
2. 利用django-admin創建專案(djangosite為你要的專案名稱)
    
    ```bash
    django-admin startproject djangosite
    ```
    
3. 建立完之後路徑如下
    
    ```markdown
    | djangosite          | 項目根目錄
    | ├── djangosite      | 項目名稱
    | │   ├── __init__.py | init文件，標識當前所在的項目目錄是一個 Python 包
    | │   ├── asgi.py     | 定義ASGI的介面資訊(ASGI是非同步Web伺服器和應用程式的python標準)
    | │   ├── settings.py | Django的專案設定檔(設定django相關設定，資料庫參數與python套件等)
    | │   ├── urls.py     | url路徑文件
    | │   └── wsgi.py     | 定義WSGI的介面資訊(用於其他Web伺服器整合)
    | └── manage.py       | 是Django用於管理本專案的命令列工具(之後進行網站執行、資料庫自動生成、靜態檔案收集等)

    ```
    
4. 建立應用(為了在專案符合MVC要建立Django應用，每個Django專案可以包含多個Django應用)
    
    ```bash
    cd djangosite
    python manage.py startapp app
    ```
    
5. 建立應用完成後路徑如下
    
    ```markdown
    | djangosite              | 項目根目錄
    | ├── app                 | 應用程式名稱
    | │   ├── migrations      | 数据模型迁移记录目录
    | │   │   └── __init__.py | init文件，標識當前所在的應用目錄是一個 Python 包
    | │   ├── __init__.py     | init文件，標識當前所在的應用目錄是一個 Python 包
    | │   ├── admin.py        | 管理網站模型的宣告檔案，預設為空
    | │   ├── apps.py         | 應用資訊定義檔案(類別AppConfig用於定義應用名等Meta資料)
    | │   ├── models.py       | 增加模型層資料類別的檔案
    | │   ├── tests.py        | 測試程式檔案 
    | │   └── views.py        | 定義URL回應函數
    | ├── djangosite          | 項目名稱 
    | │   ├── __init__.py     | init文件，標識當前所在的項目目錄是一個 Python 包
    | │   ├── asgi.py         | 定義ASGI的介面資訊(ASGI是非同步Web伺服器和應用程式的python標準)
    | │   ├── settings.py     | Django的專案設定檔(設定django相關設定，資料庫參數與python套件等)
    | │   ├── urls.py         | url路徑文件
    | │   └── wsgi.py         | 定義WSGI的介面資訊(用於其他Web伺服器整合)
    | └── manage.py           | 是Django用於管理本專案的命令列工具(之後進行網站執行、資料庫自動生成、靜態檔案收集等)
    ```
    
6. 新增測試網頁(在djangosite/app/viesw.py中建立一個路由回應函數)
    
    ```markdown
    | djangosite              | 項目根目錄
    | ├── app                 | 應用程式名稱
    | │   ├── migrations      | 数据模型迁移记录目录
    | │   │   └── __init__.py | inti文件，標識當前所在的應用目錄是一個 Python 包
    | │   ├── __init__.py     | inti文件，標識當前所在的應用目錄是一個 Python 包
    | │   ├── admin.py        | 管理網站模型的宣告檔案，預設為空
    | │   ├── apps.py         | 應用資訊定義檔案(類別AppConfig用於定義應用名等Meta資料)
    | │   ├── models.py       | 增加模型層資料類別的檔案
    | │   ├── tests.py        | 測試程式檔案
    | │   ├── urls.py         | 應用程式url路徑文件
    | │   └── views.py        | 定義URL回應函數
    | ├── djangosite          | 項目名稱
    | │   ├── __init__.py     | inti文件，標識當前所在的項目目錄是一個 Python 包
    | │   ├── asgi.py         | 定義ASGI的介面資訊(ASGI是非同步Web伺服器和應用程式的python標準)
    | │   ├── settings.py     | Django的專案設定檔(設定django相關設定，資料庫參數與python套件等)
    | │   ├── urls.py         | url路徑文件
    | │   └── wsgi.py         | 定義WSGI的介面資訊(用於其他Web伺服器整合)
    | └── manage.py           | 是Django用於管理本專案的命令列工具(之後進行網站執行、資料庫自動生成、靜態檔案收集等)
    ```
    
    ```python
    from django.shortcuts import render
    from django.http import HttpResponse
    
    # Create your views here.
    
    def welcome(request):
        return HttpResponse("<h1>Welcome to my project!</h1>")
    ```
    
7. 在djangosite/app中新增urls.py檔案
    
    ```python
    from django.urls import re_path
    from . import views
    
    # 應用程式的URL 需要incloud到djangosite.urls.py
    
    urlpatterns = [
        re_path(r'', views.welcome, name='first-url')
    ]
    ```
    
8. 在djangosite/urls.py中 incloud djangosite/app/urls.py
    
    ```python
    from django.contrib import admin
    from django.urls import path
    from django.conf.urls import include          #新增本行
    from django.urls import re_path               #新增本行
    
    urlpatterns = [
        re_path(r'^app/',include('app.urls')),     #新增本行
        path('admin/', admin.site.urls),
    ]
    ```
    
9. 執行測試web指令
    
    ```bash
    python manage.py runserver 0.0.0.0:8001
    ```
    
10. 執行成功後可至localhost:8001/app/看結果
    
    ```bash
    http://127.0.0.1:8001/app/
    ```
    
    
11. 設定專案INSTALLED_APPS(在djangosite/settings.py檔案中新增app的Config類別)
    
    ```python
    INSTALLED_APPS = [
        'app.apps.AppConfig',            #新增本行
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ```
    
12. 模型定義
    
    ```python
    class Moment(models.Model):
        content = models.CharField(max_length=200)
        user_name = models.CharField(max_length=20)
        kind = models.CharField(max_length=20)
    ```
    
13. 生成資料移植檔案
    
    ```bash
    python manage.py makemigrations app
    ```
    
14. 移植到資料庫
    
    ```python
    python manage.py migrate app
    ```
    
    將資料庫的欄位指定到特定版本
    
    ```bash
    python manage.py migrate app 0001_initial
    ```
    
    將資料庫退到最原來的版本
    
    ```bash
    python manage.py migrate app zero
    ```
    
15. 表單試圖，建立表單類別
    
    新增djangosite/app/froms.py定義表單類型
    
    ```python
    from django.forms import ModelForm
    from app.models import Moment
    
    class MomentForm(ModelForm):
        class Meta:
            model = Moment
            fields = '__all__'
            # fields=('content','user_name','kind')
    ```
    
16. 修改模型類別
    
    ```python
    from django.db import models
    
    # Create your models here.
    
    # 新增元祖用愈設定訊息類型列舉
    KIND_CHOICES = (
        ('Python技術', 'Python技術'),
        ('資料庫技術', '資料庫技術'),
        ('經濟學', '經濟學'),
        ('文體資訊', '文體資訊'),
        ('個人心情', '個人心情'),
        ('其他', '其他'),
    )
    
    class Moment(models.Model):
        content = models.CharField(max_length=300)
        user_name = models.CharField(max_length=20)
        # 修改kind定義，加入choices參數
        kind = models.CharField(
            max_length=20, choices=KIND_CHOICES, default=KIND_CHOICES[0])
    ```
    
17. 使用管理介面(將需要管理的模型類別增加到djangosite/app/admin.py)
    
    ```python
    from django.contrib import admin
    
    # Register your models here.
    from .models import Moment
    
    admin.site.register(Moment)
    ```
    
18. 第一次使用管理介面需要透過manage.py來見李管理使用者
    
    ```bash
    cd djangosite
    python manage.py createsuperuser
    ```
    
19. 常見的Django ORM 欄位類型
    1. **CharField**: 用於存儲短文本字符串，如標題或姓名。
    2. **TextField**: 適用於長文本內容，如文章內容或詳細描述。
    3. **IntegerField**: 用於存儲整數值，可以是正或負整數。
    4. **FloatField**: 用於存儲浮點數值，即帶有小數點的數字。
    5. **BooleanField**: 用於存儲布爾值（True或False）。
    6. **DateField**: 用於存儲日期（年-月-日）。
    7. **TimeField**: 用於存儲時間（時:分:秒）。
    8. **DateTimeField**: 用於存儲日期和時間的組合。
    9. **EmailField**: 用於存儲電子郵件地址，會進行基本的格式驗證。
    10. **URLField**: 用於存儲網址，會進行基本的格式驗證。
    11. **FileField**: 用於上傳文件，將文件保存在伺服器上的指定路徑。
    12. **ImageField**: 類似於FileField，但用於處理上傳的圖像文件，通常會檢查是否為有效的圖片格式。
    
    ### 參考書籍:
    
    Python網頁框架超集合