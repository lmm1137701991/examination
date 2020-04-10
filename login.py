
#手动测试用例 （该账号已注册）
#（1）在小米云官网，点击使用小米账号登录          验证：页面是否能跳转到小米账号登录界面
#（2）输入之前注册的手机号或邮箱或小米ID          验证：是否正确的展示了账号
#（3）输入密码（密码输入正确和密码输入错误）       验证：是否可以登陆成功
#（4）未注册账号                                验证：是否提示，未注册信息
#（5）密码或账号输入错误                         验证：是否提示并是否可以登录成功
#（6）点击立即注册                              验证：页面是否跳转到注册界面
#（7）点击手机短信登录                           验证 ：页面是否跳转到获取验证码登录
#（8）点击忘记密码                              验证：页面是否跳转到重置密码界面
#（9）登录成功后                                验证：查看个人信息，是否与登录账号一致
#（10)登录成功后复制连接                         验证：关掉当前浏览器，在另外浏览器打开后，是否也进入到了登录界面
#（11）登录界面                                 验证整体UI
#（12）复制连接地址                             验证：浏览器兼容性

#（13）在验证码界面点击用户名密码登录             验证：页面跳转到账号密码登录
#（14）输入密码                                 验证：密码是否 以******展示
#（15）多次输入错误密码                          验证：是否提示找回密码 



#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time      :2019-12-26 17:20
# Author    :"2394790776"
from selenium import webdriver
import unittest,time
import HTMLTestRunner
from selenium.webdriver.common.action_chains import ActionChains

class logintestcase(unittest.TestCase):
    def setUp(self):
        print('*******Test start*******')
        self.driver = webdriver.firefox()
        self.driver.get("https://i.mi.com/#/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def tearDown(self):
        print('*******End of test*******')
        self.driver.quit()
    def test_login(self):
        u'用户登录测试用例'
        driver = self.driver
        driver.find_element_by_class_name('login-text-sSOcf').click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id('username').send_keys("2394790776")
        driver.find_element_by_id('pwd').clear()
        driver.find_element_by_id('pwd').send_keys('LMM123456')
        driver.find_element_by_xpath('//*[@id="login-button"]').click()
        try:
            user_name = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[2]/div[2]/span').text
        except:
            '''登录失败'''
            driver.get_screenshot_as_file('./' + "error.png")
        '''判断是否登录成功'''
        self.assertEqual(user_name, '2394790776（普通用户）', msg='登录失败')

Suite = unittest.TestSuite()
'''执行usertestcaseone('test_login')'''
Suite.addTest(logintestcase('test_login'))

'''verbosity参数可以控制执行结果的输出，0是简单，1是一般报告（默认），2是详细报告'''
runner = unittest.TextTestRunner(verbosity=1)
'''python3测试报告模板使用,下面的时间不能用%H:%M:%S代替，否则无法出报告'''
now_time = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
'''使用当前时间拼接字符串为测试报告名称'''
fp = open('./'+now_time+"_result.html",'wb')
run = HTMLTestRunner.HTMLTestRunner(stream=fp,title='测试报告',description='测试用例执行情况')
run.run(Suite)
fp.close()