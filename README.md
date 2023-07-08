![發抖](https://images.plurk.com/5Ru1OwkKWw3re32Mj4UKyv.png)

# 各位好，這裡是棄麻機器人

---

## 綜合更新日誌
- 200716 新增patchnote函數

## Todo

Trello 連結 -> N/A CC


> ~~許願區~~
>
> > 拒絕 PM 從你我做起
> > 自由接單

- 主程式
  - 本地端測試的方法
  - 把 .font 搬到 web/
  - 把 favicon.ico 搬到 web/
  - .buildpacks 跟 Procfile 是幹什麼用的
- app
  - base_app
    - keyword 表示式產生對應的 re 表示，自動 check
  - meme
    - 需要接上資料庫
    - 輸入多組文字的功能
  - icon
    - 次數統計跟淘汰機制
  - todo
    - 希望有可以從 line 新增 todo 到這裡的功能
    - 接個資料庫做留言板，然後在放到這個區塊顯示
    - 可以新增留言
  - search
    - 第一個連結網址
    - google 翻譯、字典、單位轉換、貨幣換算
  - calculate
    - 匯率資料丟到資料庫，避免每次查詢幣值就爬一次

## 加入協作

> ~~雖然大家能看到這篇應該都是能進來了~~並沒有

- 申請[heroku](https://www.heroku.com/)帳號
- 提供信箱給仕延開權限
- 打開 heroku 頁面找到 jyanbot
- 剩下參考 deploy 標籤寫的

## 開發者

1. 將程式寫到 app/，最前面加上:

```python
   # -_- coding: utf-8 -_-
   from app.base_app import base_app

    class app(base_app):
   def **init**(self):
```

開始開發 app

2. class 裡面所有 method 第一個輸入變數要是 self，不然會出錯
3. self.\_keyword: 會顯示在 '指令' 中，可以是 list
4. self.check(): 檢查是某符合你 app 的條件，回傳 True、1、2 即會執行 self.run()，可回傳 list，記得保留狀態在 self 裡面，給 self.run() 使用
5. self.run(): 回傳文字，如果 self.check() 回傳的是 True、1 則會貼出那些文字，如果回傳的是 2 則會貼圖，可回傳 list 會一一對應 self.check() 的元素，記得保留資料給 self.web() 使用，self.web() 不會收到任何資料(目前)
6. self.\_url: webapp 的網址
7. self.\_host_url: 在 base_app 中已定義，回傳網址的時候記得回傳 self.\_host_url + self.\_url
8. self.web(): 回傳用戶點擊 self.\_url 的網址時，要顯示的網頁
9. self.\_repr: app 敘述，目前沒什麼用
10. self.check(), self.run(): 可以拿到的變數，最後面記得加上 \*\*kwargs 消化那些你沒用到的變數
    - msg: 使用者輸入的訊息
    - type: 訊息來源 'user': 一對一、'group': 群組
    - id: 說話者或是群組的 id
    - user_id: 說話者的 id
    - group_id: 說話群組的 id
    - app_info: 所有 app 的 keyword
    - app_patchnote: 所有 app 的 patchnote
11. self.\_run_once_at_begin: 一開始執行一次 self.run()
12. 套件安裝請放在 requirements.txt
13. html template 請放在 templates/
14. self.\_patchnote: 若APP開發者想要寫patchnote請在這裡輸入

## heroku 環境布置

### phantomJS

- 爬蟲功能需要的瀏覽器元件
- 注意由於這等於用了第二個 buildpack 所以還要再灌 multi-buildpacks  
   未來若新增其他功能也會用到 multi-buildpacks
- 基本上參考[這篇](https://medium.com/@op880623/%E5%9C%A8-heroku-%E4%BD%BF%E7%94%A8-phantomjs-d0592615b353)

### 中文字型

- 爬蟲功能若是要跟網頁互動會需要用到(否則會出現亂碼)
- 將字型檔放到.fonts 資料夾,注意要是 linux 支援的
- 參考[這篇](https://laplacetw.github.io/line-use-custom-fonts-in-heroku-apps/)

### 資料庫 plugin

@安杰
