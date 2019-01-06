import requests
import js2py
from retrying import retry
import json
import jsonpath
from pprint import pprint
import re

# 1直接使用已登录的Cookies发送请求
class url_test1(object):
    def url_response1(self):
        # 1.发送请求并获取响应
        url = 'https://github.com/settings/profile'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Cookie': '_ga=GA1.2.1955076383.1542020423; _octo=GH1.1.1441026884.1542020423; user_session=X97NdvBL6sfR291OLj7_48xRjBqkVb8aFuCXp1hRQt1rZdov; __Host-user_session_same_site=X97NdvBL6sfR291OLj7_48xRjBqkVb8aFuCXp1hRQt1rZdov; logged_in=yes; dotcom_user=xiaofeifeiglp; tz=Asia%2FShanghai; has_recent_activity=1; _gat=1; _gh_sess=UnhEakRHQkVFRURKUHQrUHJoU05HQlFQUlZIMzQyOSsvTFRaOGNjaTAyV2t6Yjk0ejN4ZXZEaHEyT2o4ZEZqczFHUjRzaXEvUUR5bC93M3p0ZDZXSEdlTE5JUnZsN09MQk1KUEN3Z016SXhGcVU5QkJEa3FOc3ZkTG8xdjl2TElSTlVON3NnYkppcGcwazhERkRRL0o0eTFybWd5VmtuNU9JMzFMSUNZK1Vkd2I1SXdEUXFibHVIZ0RHVnFiRDVBTktxTkl6S1pKTGNxY3NzZVp6RHFWUHl6QTZzVVhsWHI5aUNDS2xBdXF4WEdUUVJvMkVHMTBZRFFITjVrMHdnMC0tRmc4R0dkWWY5N1VkK202VkwvOWd0UT09--214907bdc5059aa2822f7ef2da122a32b3678f1d'
        }
        response = requests.get(url, headers=headers)
        # 2.处理响应
        with open('01_github.html', 'wb') as f:
            f.write(response.content)

# 2访问需要登录的页面方式2
class url_test2(object):
    def url_response2(self):
        '''
        1. 模拟浏览器登录
        2. 登录成功获取Cookie
        3. 再访问需要登录的页面直接携带Cookie

        分析登录:
        url
            https://github.com/session
        请求方式
            POST
        请求参数
            commit: Sign in
            utf8: ✓
            authenticity_token: l9bXPrSBCA8YwBbNGmm5QlPKeRv8PUP8q7e6uKhyPLUTfcLjhv+5mKJG8bXGpDN9sYyec+sZSO80vJ6EzLk3qg==
            login: czwspider
            password: qwer1234

        请求头
            User-Agent
        '''
        # 1.发送请求并获取响应
        url = 'https://github.com/session'
        data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': 'qyIJqSolDeB+gMX30PLo+5czFxRowGvml3iLgLdA/Cf/kI1xSH9bMHAJqnCRAAfELLvCehXoCLhqlxCGMpkj3w==',
            'login': 'xiaofeifeiglp',
            'password': 'baison8888'
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Referer': 'https://github.com/login?return_to=%2Fjoin',
            'Cookie': 'has_recent_activity=1; logged_in=no; _ga=GA1.2.1019431889.1546494146; _gat=1; tz=Asia%2FShanghai; _octo=GH1.1.848326696.1546494206; _gh_sess=OFdiYkZySkljeGhWSWMwOHlBd3IrMlIzRWJVRlExcC81dTJxVm0zazU2ajNvMkhzeFhvYU9TbUZCdXp2RFlHblFIUW1xdWYxUjlTcFluZ0tKcjdyTGZFbHE1ZjhDRlNSSGN0MWNnbnBHWHBLMzhpdEtxMDZnME00ekswTi9XNFEvTlo0T2J0aU96Q3FGYjVkQk5FU2h3eG5JenNmZFN4NHRtWFV0bU5sMmJJZmRVNVFqU2Zwbys0WkZsNXN2QmR4c0RsRkNxUWVaMFVseWxZaEh2VW1DKzBpRjNsc3M3a2VEL3BrZFNXWVZ1Z0NrRm9ReDdFaml2ZlNQdHdZNWdDTmZQVkpmTXFxT3RXdVR5eklwSmlndTROeGZHVlhVMUFEbHptSHJ2N1A2U1BqMWFKZ0JwRmREb0ZsTGtsWE10U1Z5SEMvZ3cxMTk1alZVWC9KWFhFOGFueTRaeHdUdHBKZzBpd1JHU3NVbXVmQzFvUityV2hzOEJGZnRZbzVNdFdVSzdMUFpzQUpvTVpHODY5d2hIQ0xwa1F4WGNRRzBOd1NqYXhLK2VTb0t2UERCM3graEM5SXFvQjdyVnYvcWROQlFyR3k4ZmpMVHBhVy9uQndIREN3VVJlN09TT1pxUkg3RW4rWDZXUUpVdjZncWFSMnIyVWNyczB3angvRHBDZHYtLVdZK2hJY2VSS1pKL0U4bzZWenJ0a3c9PQ%3D%3D--7faf3f398cf1584bd810ce07d97c0a71078afd30'
        }
        response = requests.post(
            url=url,
            headers=headers,
            data=data
        )

        # 2.获取已登录的Cookies
        cookies = response.cookies
        response2 = requests.get(
            url='https://github.com/settings/profile',
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            },
            cookies=cookies
        )
        with open('02_github.html', 'wb') as f:
            f.write(response2.content)

# 3访问需要登录的页面方式三
class url_test3(object):
    def url_response3(self):
        '''
        1. 模拟浏览器登录
        2. 利用 session 登录成功
        3. 利用 session 再访问需要登录的页面

        session 内部自动实现了 cookies 传递机制

        分析登录:
        url
            https://github.com/session
        请求方式
            POST
        请求参数
            commit: Sign in
            utf8: ✓
            authenticity_token: l9bXPrSBCA8YwBbNGmm5QlPKeRv8PUP8q7e6uKhyPLUTfcLjhv+5mKJG8bXGpDN9sYyec+sZSO80vJ6EzLk3qg==
            login: czwspider
            password: qwer1234

        请求头
            User-Agent
        '''
        # 1.构建session,发送请求并获取响应
        session = requests.session()
        url = 'https://github.com/session'
        data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': 'qyIJqSolDeB+gMX30PLo+5czFxRowGvml3iLgLdA/Cf/kI1xSH9bMHAJqnCRAAfELLvCehXoCLhqlxCGMpkj3w==',
            'login': 'xiaofeifeiglp',
            'password': 'baison8888'
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Referer': 'https://github.com/login?return_to=%2Fjoin',
            'Cookie': 'has_recent_activity=1; logged_in=no; _ga=GA1.2.1019431889.1546494146; _gat=1; tz=Asia%2FShanghai; _octo=GH1.1.848326696.1546494206; _gh_sess=OFdiYkZySkljeGhWSWMwOHlBd3IrMlIzRWJVRlExcC81dTJxVm0zazU2ajNvMkhzeFhvYU9TbUZCdXp2RFlHblFIUW1xdWYxUjlTcFluZ0tKcjdyTGZFbHE1ZjhDRlNSSGN0MWNnbnBHWHBLMzhpdEtxMDZnME00ekswTi9XNFEvTlo0T2J0aU96Q3FGYjVkQk5FU2h3eG5JenNmZFN4NHRtWFV0bU5sMmJJZmRVNVFqU2Zwbys0WkZsNXN2QmR4c0RsRkNxUWVaMFVseWxZaEh2VW1DKzBpRjNsc3M3a2VEL3BrZFNXWVZ1Z0NrRm9ReDdFaml2ZlNQdHdZNWdDTmZQVkpmTXFxT3RXdVR5eklwSmlndTROeGZHVlhVMUFEbHptSHJ2N1A2U1BqMWFKZ0JwRmREb0ZsTGtsWE10U1Z5SEMvZ3cxMTk1alZVWC9KWFhFOGFueTRaeHdUdHBKZzBpd1JHU3NVbXVmQzFvUityV2hzOEJGZnRZbzVNdFdVSzdMUFpzQUpvTVpHODY5d2hIQ0xwa1F4WGNRRzBOd1NqYXhLK2VTb0t2UERCM3graEM5SXFvQjdyVnYvcWROQlFyR3k4ZmpMVHBhVy9uQndIREN3VVJlN09TT1pxUkg3RW4rWDZXUUpVdjZncWFSMnIyVWNyczB3angvRHBDZHYtLVdZK2hJY2VSS1pKL0U4bzZWenJ0a3c9PQ%3D%3D--7faf3f398cf1584bd810ce07d97c0a71078afd30'
        }
        session.post(
            url=url,
            headers=headers,
            data=data
        )
        response2 = session.get(
            url='https://github.com/settings/profile',
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            }
        )
        # 2.处理响应
        with open('03_github.html', 'wb') as f:
            f.write(response2.content)

# 4人人网登录
class url_test4(object):
    def url_response4(self):
        '''
        分析登录

        url
            http://activity.renren.com/livecell/ajax/clog
        请求方式
            POST
        请求参数

        phoneNum: 18946536623
        password: a63c62ca06e466cccdd774afb309bdafcfd5a1e1c6bd9c6db96216c649e996c3
        c1: -100
        rKey: 2d7e7bd2a35ba797ab6075ffeb9a5000

        请求头
        '''
        context = js2py.EvalJs()
        # 1.发送请求并获取响应
        t = {
            'phoneNum': '18946536623',
            'password': 'wf834205116',
            'c1': '-100'
        }
        response = requests.get(
            url='http://activity.renren.com/livecell/rKey',
            headers={
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
            }
        )
        n = response.json()['data']
        context.n = n

        # with open('BigInt.js', 'r', encoding='utf-8') as f:
        #     context.execute(f.read())
        # with open('Barrett.js', 'r', encoding='utf-8') as f:
        #     context.execute(f.read())
        # with open('RSA.js', 'r', encoding='utf-8') as f:
        #     context.execute(f.read())
        # context.t = t
        # js_string = '''
        # t.password = t.password.split("").reverse().join("");
        # serMaxDigits(130);
        # '''

# 5js2py演练
class url_test5(object):
    def url_response5(self):
        # 创建上下文对象,承上(python)启下(js)
        # 只要是把变量挂载在context上python和js都可以访问到
        context = js2py.EvalJs()

        # 2.交互
        # 执行js
        context.execute('console.log("aaa")')

        # 2.1 python 执行js获取js内部的内容
        context.execute('var a = 5')
        context.execute("var b = 'abc'")
        context.execute("var c = ['q', 'w', 'e']")
        context.execute("var d = {'test': 'demo'}")
        print(context.a)
        print(context.b)
        print(context.c)
        print(context.d)

        # 2.2 python的内容传递给js使用
        context.a = 5
        context.b = 'abc'
        context.c = ['a', 'b', 'c']
        context.d = {
            'ccc': 'qqq'
        }
        context.execute('console.log(a)')
        context.execute('console.log(b)')
        context.execute('console.log(c)')
        context.execute('console.log(d)')

        # 3.高级演进
        # context.execute('function add(a, b){return a + b}')

        with open('test.js', 'r', encoding='utf-8') as f:
            context.execute(f.read())
        print(context.add(5, 6))

# 6代理服务器使用
class url_test6(object):
    def url_response6(self):
        # 1.发送请求并获取响应
        url = 'https://www.baidu.com'
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
        }
        proxies = {
            # key使用小写
            "http":"http://117.70.39.81:9999"
        }
        response = requests.get(
            url=url,
            headers=headers,
            proxies=proxies
        )
        print(response.text)

# 7超时
class url_test7(object):
    def url_response7(self):
        # 1.发送请求并获取响应
        url = 'https://www.baidu.com'
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
        }
        proxies = {
            # key使用小写
            "http":"http://117.70.39.81:9999"
        }
        response = requests.get(
            url=url,
            headers=headers,
            proxies=proxies,
            timeout=3
        )
        # 2.处理响应
        print(response.text)

# 8重试
class url_test8(object):
    @retry(stop_max_attempt_number=5)
    def url_response8(self, url):
        print('访问url')
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
        }
        proxies = {
            # key使用小写
            "http": "http://117.70.39.81:9999"
        }
        response = requests.get(
            url=url,
            headers=headers,
            proxies=proxies,
            timeout=5
        )
        return response.text

# 9json模块使用
class url_test9(object):
    def url_response9(self):
        # json.loads 把json字符串转成python对象
        # json_string = '''
        # {
        #     "a": "x",
        #     "b": "y"
        # }
        # '''
        # # print(json_string)
        # data = json.loads(json_string)
        # print(data)
        # print(type(data))
        #
        # # json.dumps 把 python 对象转json字符串
        # data = {
        #     "a": "x",
        #     "b": "y"
        # }
        # json_string = json.dumps(data)
        # print(json_string)
        # print(type(json_string))

        # 从json文件中获取数据
        # 读取字符串
        # with open('09-test.json', 'r', encoding='utf-8') as f:
        #     json_string = f.read()
        #     data = json.loads(json_string)
        #     print(data)
        #     print(type(data))

        # json.load 从json 文件中获取数据
        # with open('09-test.json', 'r', encoding='utf-8') as f:
        #     data = json.load(f)
        #     print(data)
        #     print(type(data))

        # json.dump 把python数据写入到json文件中
        data = {
            "a": "x",
            "b": "y",
            "parents": {
                "mother": "妈妈",
                "father": "爸爸"
            }
        }
        with open('09-test2.json', 'w', encoding='utf-8') as f:
            # indent 缩进
            # ensure_ascii 中文写入
            json.dump(data, f, indent=4, ensure_ascii=False)

# 10json模块演练
class url_test10(object):
    def url_response10(self):
        # 1.发送请求并获取响应
        url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        proxies = {
            # key使用小写
            "http": "http://117.70.39.81:9999"
        }
        response = requests.get(
            url=url,
            headers=headers,
            proxies=proxies
        )
        result = response.json()
        # # 2.使用jsonpath提取数据
        data = jsonpath.jsonpath(result, '$..name')
        pprint(data)

# 11正则DOTALL模式
class url_test11(object):
    def url_response11(self):
        string = '''
        abcd
        abcd
        aegwgwd
        '''
        # 相当于
        # 1.编译正则表达式
        # (.*)  贪婪匹配,尽可能多匹配直到无法匹配
        # (.*?) 非贪婪匹配,只要匹配到就返回
        # . 符号默认不包含换行符,DOTALL模式表示让 .符号匹配任何字符包括换行符
        # re.DOTALL == re.S == re.RegexFlag.DOTALL == re.RegexFlag.S

        # pattern = re.compile(r'a(.*)d',re.RegexFlag.S)
        # # 提取数据
        # result = pattern.findall(string)
        # print(result)

        pattern = re.compile(r'a(.*)d', re.RegexFlag.DOTALL)
        print(pattern)
        result = pattern.findall(string)
        print(result)

# 12正则忽略大小写
class url_test12(object):
    def url_response12(self):
        # 相当于
        # 1. 编译正则表达式
        # (.*)      贪婪匹配，尽可能多匹配直到无法匹配
        # (.*?)     非贪婪匹配，只要匹配到就返回
        #  . 符号默认不包含换行符，DOTALL模式表示让 . 符号匹配任何字符包括换行符
        # re.DOTALL == re.S == re.RegexFlag.DOTALL == re.RegexFlag.S
        # 忽略大小写
        # re.IGNORECASE == re.I == re.RegexFlag.IGNORECASE == re.RegexFlag.I
        # 忽略大小写并且支持 DOTALL模式 使用 |
        string = '''
        abcD
        abcD
        '''
        pattern = re.compile(r'a(.*)d', re.RegexFlag.IGNORECASE | re.DOTALL)
        # 提取数据
        result = pattern.findall(string)
        print(result)

# 13原始字符串
class url_test13(object):
    def url_response13(self):
        string = r'abc\nd'
        print(string)

        # 回退符
        string = "abcde\b\bfg"
        print(string)

# 14正则表达式四大检索方法
class url_test14(object):
    def url_response14(self):
        string = "1234abc123"
        pattern = re.compile('\d+')

        # match 开头匹配,只匹配一次
        # result = pattern.match(string)
        # print(result.group())

        # search 全局匹配,只匹配一次
        result = pattern.search(string)
        print(result.group())
        '''
        findall 优点：使用简单，缺点：必须把所有数据搜索返回再返回
        finditer 优点：找到就返回，可以边找边返回
        如果数据量小 使用 findall
        如果数据量大 使用 finditer
        '''
        # findall 匹配所有符号条件的数据，返回是 结果列表
        result = pattern.findall(string)
        print(result)

        # finditer 迭代对象,迭代Match对象
        results = pattern.finditer(string)
        for result in results:
            print(result.group())
        print(results)

# 15正则表达式分组替换
class url_test15(object):
    def url_response15(self):
        string = 'a;dj jkl,jj; j;sd'

        # split分组
        pattern = re.compile(r'[; ,]+')
        result = pattern.split(string)
        print(result)

        # sub交换
        string = 'hello worldl;sjd;ssdjkls;sdjklzhuwei cao'
        # 带空格的词组替换成 #
        pattern = re.compile(r'(\w+) (\w+)')

        # 把空格的词组 进行交换
        # result = pattern.sub(r"\2 \1", string)
        result = pattern.sub(r"\2 \1", string)

        print(result)

# 16html中常用的字符串提取
class url_test16(object):
    def url_response16(self):
        string = '<input type="submit" id="su" value="百度一下" class="bg s_btn">'
        pattern = re.compile(r'<input type="submit" id="(.*?)" value="(.*?)" class="bg s_btn">')
        result = pattern.findall(string)
        print(result)

# 17内涵8爬虫
class url_test17(object):
    def url_response17(self):
        pass

if __name__ == '__main__':
    # 创建对象并调用函数
    url_user = url_test16()
    url_user.url_response16()
