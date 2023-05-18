# gceguide文件爬虫

本爬虫仅用于学习用途，针对GCE Guide提供的一些剑桥试题资源进行下载

## 1.安装python依赖
```bash
pip install -r requirements.txt
```

## 2.修改下载地址
修改 `main.py` 中的 `target_url` 为对应的GCE Guide的下载目录下的网页地址即可，需要注意的是，本python文件默认是只能深入到两层文件结构

## 3.运行
```bash
python main.py
```