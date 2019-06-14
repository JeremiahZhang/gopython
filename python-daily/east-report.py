#! /usr/bin/python3
import sys
import webbrowser

# 输入股票代码, 打开东方财富网信息披露页
stock_code = sys.argv[1]
url = 'http://data.eastmoney.com/notices/stock/' + stock_code + '.html' # company notices in easy money

webbrowser.open(url)
