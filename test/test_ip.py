from bs4 import BeautifulSoup
import random
import urllib.request


def get_proxy_list():
    target = 'http://www.xicidaili.com/nn/' + str(random.randint(0, 100))
    try:
        opener = urllib.request.build_opener()
        # header可以选自己浏览器的
        # 样例：[('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) ''AppleWebKit/537.36 (KHTML, like Gecko)Chrome/56.0.2924.87 Safari/537.36')]
        opener.addheaders = self.headers
        urllib.request.install_opener(opener)
        html = urllib.request.urlopen(target).read().decode('utf-8')
        tr = BeautifulSoup(html, 'lxml').find_all('tr')
        p = re.compile('<[^>]+>')
        for tag in tr:
            td_list = tag.find_all('td')
            if len(td_list) > 0:
                if str(td_list[5]) == '<td>HTTP</td>':
                    # 将爬到的代理IP存到列表里面
                    self.proxy_list.append(p.sub('', str(td_list[1])) + ':' + p.sub('', str(td_list[2])))
    except Exception as b:
        self.logger.exception(b)

def init_urllib():
        # 这个函数用来初始化urllib的参数
        length = len(self.proxy_list)
        if length == 0:
            get_proxy_list()
        # 随机得到一个IP
        ip = random.choice(self.proxy_list)
        self.proxy_list.remove(ip)
        proxy = {'http': ip}
        proxy_support = urllib.request.ProxyHandler(proxy)
        # 加载代理
        opener = urllib.request.build_opener(proxy_support)
        opener.addheaders = self.headers
        # 初始化urllib
        urllib.request.install_opener(opener)

def connect(uri):
        html = ''
        flag = 20
        while flag > 0:
            try:
                html = urllib.request.urlopen(uri).read().decode('utf-8')
                break
            except Exception as b:
                # 这里可以将异常细化，由于是简单实现就不做具体实现了
                self.logger.exception(b)
                # 实现更换IP重新请求
                flag -= 1
                init_urllib()
        return BeautifulSoup(
            html,
            'lxml')