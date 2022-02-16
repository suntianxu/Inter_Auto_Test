import pytest
import requests
import random
import flaky
import time
from tenacity import retry,wait_fixed,stop_after_attempt,stop_after_delay
class TestDemo:
    # @pytest.mark.sit
    # def test_demo01(self):
    #     body={
    #         'key':'d90e6b7ec48648f8d4381cd3b94d2d36',
    #         'city':'上海'
    #     }
    #     respot = requests.get(url='http://v.juhe.cn/historyWeather/province',params=body)
    #     assert '查询成功'==respot.json()['reason']
    #     print(respot.json())
    # @retry()
    # def test_retry(self):
    #     print('等待重试，重试无间隔执行·····')
    #     raise 1==2
    # @retry(wait = wait_fixed(2))
    # def test_retry(self):
    #     print('等待重试')
    #     raise 1==2

    # @retry(stop = stop_after_attempt(10000) | stop_after_delay(5))
    # def test_retry(self):
    #     time.sleep(1)
    #     print('等待重试')
    #     raise Exception



    # def test_demo02(self):
    #     assert 1==1
    #
    #
    # @pytest.mark.skip('用例跳过')
    # def test_demo03(self):
    #     assert 1==1
    #
    #
    # def test_demo04(self):
    #     assert 1==3


    def test_shengxiao(self):
        body={
            'men':'鼠',
            'women':'兔',
            'key':'8ee22d2c9a2c521e90fc61c1dabbb945'
        }
        url = 'http://apis.juhe.cn/sxpd/query'
        report = requests.get(url=url,params=body)

        assert 0==report.json()['error_code']
        print(report.json())