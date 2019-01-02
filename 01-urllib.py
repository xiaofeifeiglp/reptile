# 导入模块
import urllib.request
import requests

class url_test(object):
    def url_response(self):
        # 1.发送请求获取响应
        url = 'http://baidu.com'
        response = urllib.request.urlopen(url)
        # 2. 处理响应
        with open('01-urlliib.html', 'wb') as f:
            f.write(response.read())

class url_test1(object):
    def url_response1(self):
        # 1.发送请求获取响应
        url = 'http://baidu.com'
        headers = {
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
        }
        # 定义请求对象
        request = urllib.request.Request(
            url=url,
            headers=headers
        )
        response = urllib.request.urlopen(request)
        # 2.处理响应
        with open('02-urllib.html', 'wb') as f:
            f.write(response.read())

class url_test2(object):
    def url_response2(self):
        # 1.发送请求获取响应
        url = 'http://www.baidu.com/s?wd='
        wd = input('请输入查询内容')
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
        }
        # 定义请求对象
        request = urllib.request.Request(
            # quote去空格
            url = url + urllib.parse.quote(wd),
            headers=headers
        )
        print(url + urllib.parse.quote(wd))
        response = urllib.request.urlopen(request)

        # 2.处理响应
        with open('03-urllib.html', 'wb') as f:
            f.write(response.read())

class url_test3(object):
    def url_response3(self):
        # 1.发送请求获取响应
        url = 'https://www.baidu.com/s?wd='
        wd = input('请输入查询内容')
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
        }
        # 定义请求对象
        request = urllib.request.Request(
            url = url + urllib.parse.quote(wd),
            headers=headers
        )
        print(url + urllib.parse.quote(wd))
        response = urllib.request.urlopen(request)

        # 返回bytes
        content = response.read()

        # 把bytes数据转换成字符串
        # python内存中字符串是unicode
        content_string = content.decode('utf-8')

        # 2.处理响应
        with open('04-urllib.html', 'w', encoding='utf-8') as f:
            f.write(content_string)

class url_test4(object):
    def url_response4(self):
        # 1.发送请求获取响应
        url = 'http://baidu.com'
        response = requests.get(url)
        # print(response, type(response))
        # 2.处理响应内容
        with open('06_requests基本使用.html', 'wb') as f:
            f.write(response.content)

class url_test5(object):
    def url_response5(self):
        # 发送请求获取响应
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        url = 'http://baidu.com'
        response = requests.get(
            url=url,
            headers=headers
        )
        # 处理响应内容
        with open('07_requests.html', 'wb') as f:
            f.write(response.content)

class url_test6(object):
    def url_response6(self):
        # 1.发送请求获取响应
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        wd = input('请输入查询内容')
        url = 'https://www.baidu.com/s'
        params = {
            'wd': wd
        }
        response = requests.get(
            url=url,
            headers=headers,
            params=params
        )
        # 2.处理响应内容
        with open('08_requests.html', 'wb') as f:
            f.write(response.content)

class url_test7(object):
    def url_response7(self):
        # 发送请求获取响应
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        url = "http://docs.python-requests.org/zh_CN/latest/_static/requests-sidebar.png"
        response = requests.get(
            url=url,
            headers=headers
        )
        # 处理响应内容
        with open('09_requests.png', 'wb') as f:
            f.write(response.content)

class url_test8(object):
    def url_response8(self):
        # 发送请求获取响应
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        url = 'http://baidu.com'
        response = requests.get(
            url=url,
            headers=headers
        )
        print(response.url)
        print('----')
        print(response.headers)
        print('----')
        print(response.status_code)
        print('----')
        content = response.content
        print(content)
        print(type(content))
        # print('----')
        # print(response.text)

        # 方式1
        print(response.content.decode('utf-8'))
        print('----')
        # 方式二
        print(str(response.content,encoding='utf-8'))
        print('----')
        # 方式3
        # 设置编码方式
        response.encoding = 'utf-8'
        print(response.text)

# request的cookies操作
class url_test9(object):
    def url_response9(self):
        '''request的cookies操作'''
        # 发送请求获取响应
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        url = 'http://www.baidu.com'
        response = requests.get(
            url=url,
            headers=headers
        )
        # 处理响应
        print(response.cookies)
        print(requests.utils.dict_from_cookiejar(response.cookies))

# 豆瓣热门电影爬虫
class url_test10(object):
    def url_response10(self):
        '''
        分析：

        url
        https://movie.douban.com/j/search_subjects
        请求方式
        GET
        请求参数
        type: movie
        tag: 热门
        sort: recommend
        page_limit: 20
        page_start: 40  (发生变化)

        请求头
        Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36

        '''
        # 发送请求获取响应
        url = 'https://movie.douban.com/j/search_subjects'
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        for page_start in range(0, 100000, 20):
            params = {
                'type': 'movie',
                'tag': '热门',
                'sort': 'recommend',
                'page_limit': 20,
                'page_start': page_start
            }
            response = requests.get(
                url=url,
                headers=headers,
                params=params
            )
            # 处理响应
            result = response.json()
            if len(result['subjects']) == 0:
                break

            for movie in result['subjects']:
                print(movie['title'],':', movie['rate'])

# 百度贴吧
class url_test11(object):
    '''
    分析:

    url
        https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&ie=utf-8&pn=18228250
    请求方式

    请求参数

    kw: 贴吧名
    ie: utf-8
    pn: 页数 每 50 页增长 最大数 18228250

    请求头
    User-Agent
    '''
    def __init__(self, kw, max_pn):
        self.base_url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        self.kw = kw
        self.max_pn = max_pn

    def get_url_list(self):
        '''
        url_list = []
        for pn in range(0, self.max_pn + 1, 50):
            url = self.base_url.format(self.kw, pn)
            url_list.append(url)
        return url_list
        '''
        return [self.base_url.format(self.kw, pn) for pn in range(0, self.max_pn + 1, 50)]

    def get_content(self, url):
        '''
        发送请求获取内容
        '''
        response = requests.get(
            url=url,
            headers=self.headers
        )
        return response.content

    def get_items(self, content, idx):
        with open('13-{}.html'.format(idx), 'wb') as f:
            f.write(content)

    def save_items(self, items):
        pass

    def run(self):
        # 1.获取url列表
        url_list = self.get_url_list()
        for url in url_list:
            # 2.发送请求获取响应
            content = self.get_content(url)
            # 3.从响应中提取数据
            items = self.get_items(content, url_list.index(url) + 1)
            # 4.报存数据
            self.save_items(items)

# 百度翻译
class url_test12(object):
    '''
    分析：
        https://fanyi.baidu.com/v2transapi
    请求方式
        POST
    请求参数
    from: en
    to: zh
    query: as
    transtype: translang
    simple_means_flag: 3
    sign: 812117.558948
    token: 2cdd6c87b82da4160c25cad0bb7b0831

    请求头

    遭遇问题:
    通过查询内容动态生成  sign,token,auth等等

    处理这类问题有3中方式
    1. 切换到手机移动端看看接口的变化
    2. selenium 通过浏览器提取数据（性能非常慢）（爬虫底线）
    3. js 逆向（爬虫进阶）

    '''
    # def url_response12(self):
    #     url = 'https://fanyi.baidu.com/v2transapi'
    #     # url = 'https://fanyi.baidu.com/basetrans'
    #     headers = {
    #         # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    #         # "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    #         'Referer': 'https://fanyi.baidu.com/?aldtype=85',
    #         'Cookie': 'BAIDUID=90E3CE8E3815EA321128F6A2EF878C71:FG=1; BIDUPSID=90E3CE8E3815EA321128F6A2EF878C71; PSTM=1540695856; BDUSS=ZvZkJpVXhocFh-SnVlTHh4Y0djUFdKdVdpOTg5MWFlbWJTY251ZUxpQkpXUDFiQVFBQUFBJCQAAAAAAAAAAAEAAAC7sNJW06O7qMDLwv6438rWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEnL1VtJy9VbcF; BDSFRCVID=F74OJeCmHmUCzAO95pmLUO5QvmKK0gOTHlxUPYCrMGj2i9PVJeC6EG0Ptf8g0KubhnKPogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tJIDoIL2JC_3qn5zqROHhRIJhpo-KnLXKKOLV-TFBp7keq8CD6r85b-hjGutBRt8Qm8tb4QE2DQHKq72y5jHbfFX5fcnBf50-JnKQbrLtUTpsIJMbtDWbT8U5fKL2lOzaKviaKJHBMb1jpODBT5h2M4qMxtOLR3pWDTm_q5TtUt5OCF4DjtbejJBeaRLet5Q2CvMX6rJabC3MKjqKU6qLUtbQNbZb45qfRTw5bObXK36o-3t54nNQqTXjntDJMIEtRk8oI-5tIvMqRjnbDIhDtIe-mT22-usbHvlQhcH0hOWsIOmhb7oejLr3H5uJ4Dq3IQ8VpAEKq5Mj-T5DUC0jTJQDN_fJ5nfb5kXWnjja-K_Hn7zepbh5JtpbtbmhU-eJ5TiLDIaLUnmjlbmX5b204_d0nnO3RJLQJ7ZVD_2tD0MhDP6ePbHKCCVMqOK-R3yHD7yWCvxyIbcOR5JhfA-D60TqHt8tROQWGT9_xjKalvvhb3O3M7S2b8IyMAqBbOGBCjxVUQF5l8-sq0x0bOte-bQypoaaP6iLIOMahkM5h7xOKQoQlPK5JkgMx6MqpQJQeQ-5KQN3KJmhpFuj6_BejcbjHRf-b-X2I6yWRjVKbnqKROvhjRIjq4gyxomtjjCQCOQ_JuXJ4JVjM5OjqQ-5TcLKt7BLUkqKmKqQto7-t36jtPGDl7N54L8QttjQnoOfIkja-KEtDnvJJ7TyU42bf47yMRm0q4Hb6b9BJcjfU5MSlcNLTjpQT8rDPCEJj0HJbPDVI0QKbjKKRoY5-Qh5-RH-UnLqMKfJgOZ0lOEWn6lEPcqXTuhK-uT3tPtQR5LW20j0h7mWnRWSfJXLn5YQPTXMHrTLfT-0bc4KKJxbnLWeIJo5t5shxPrhUJiB5OMBan7_qvIXKohJh7FM4tW3J0ZyxomtfQxtN4eaDcJ-J8XMC-4e5QP; delPer=0; PSINO=5; BDRCVFR[nnelRoIzZZm]=mk3SLVN4HKm; H_WISE_SIDS=126126_126708_114553_127233_127532_128065_127492_128145_120164_123018_127301_118887_118862_118838_118818_118790_127182_128457_107314_128037_126995_127771_127568_126797_127769_117333_126792_117429_128450_126784_128402_127836_127808_127024_128328_128447_126684_128247_126959_126773_126180_126720_126092_127872_125873_128239_124030_128342_110085_124865_121265_126973_123289_127379_127399_128195; FEED_SIDS=528979_1230_20; H_PS_PSSID=; ZD_ENTRY=baidu; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; locale=zh; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1546432612,1546433076; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1546433076'
    #     }
    #     query = input('请输入查询内容')
    #     # 1.获取请求并获取响应
    #     # 定义数据
    #     data = {
    #         'from': 'en',
    #         'to': 'zh',
    #         'query': query,
    #         'transtype': 'translang',
    #         'simple_means_flag': '3',
    #         'sign': '922689.718704',
    #         'token': '1b8715021bde71d0a3ba7ff842977d0b',
    #     }
    #     # 2.处理响应
    #     # get 使用params
    #     # post 使用data
    #     response = requests.post(
    #         url=url,
    #         headers=headers,
    #         # 设置post请求参数
    #         data=data
    #     )
    #
    #     # print('翻译结果为:', response.json()['trans'][0]['dst'])
    #     print('翻译结果为:', response.json())

    def url_response12(self):
        url = "https://fanyi.baidu.com/basetrans"

        headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
        }

        query = input("请输入查询内容:")

        # 重要的知识点，requests 模拟post请求
        # 1. 定义数据
        data = {
            "from": "en",
            "to": "zh",
            "query": query
        }

        # 2. 发送post请求
        # get 使用 params
        # post 使用 data
        response = requests.post(
            url=url,
            headers=headers,
            # 设置post请求参数
            data=data
        )
        print("翻译结果为:", response.json()["trans"][0]["dst"])

if __name__ == '__main__':
    # 创建对象并调用函数
    # user11 = url_test11(kw='魔兽世界', max_pn=150)
    # user11.run()
    user12 = url_test12()
    user12.url_response12()


