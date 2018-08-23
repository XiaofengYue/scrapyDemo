import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()


def zhihu():
    browser.get('https://www.zhihu.com/signin')

    account = browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input')
    account.send_keys('15681953321')

    password = browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input')
    password.send_keys('wozhiai0')

    btn = browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/button')
    btn.click()

    time.sleep(5)
    browser.close()



from selenium.webdriver import ActionChains


def exampleAction():
    url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    source = browser.find_element_by_css_selector('#draggable')
    target = browser.find_element_by_css_selector('#droppable')
    actions = ActionChains(browser)
    actions.drag_and_drop(source, target)
    actions.perform()


from selenium.common.exceptions import NoSuchElementException

# 很多网页有Frame标签，这个可以涉及到切近Frame 和 切出Frame
# switch_to.parent_frame
# switch_to.frame


def frame():
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    source = browser.find_element_by_css_selector('#draggable')
    print(source)
    try:
        logo = browser.find_element_by_class_name('logo')
    except NoSuchElementException:
        print('NO LOGO')
    browser.switch_to.parent_frame()
    logo = browser.find_element_by_class_name('logo')
    print(logo)
    print(logo.text)

# 隐式等待
# 到了一定的时间发现元素还没有加载，则继续等待我们指定的时间，如果超过了我们指定的时间还没有加载就会抛出异常，如果没有需要等待的时候就已经加载完毕就会立即执行


def wait_showdown():
    browser.implicitly_wait(10)
    browser.get('https://www.zhihu.com/explore')
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input)


# 显示等待
# 指定一个等待条件，并且指定一个最长等待时间，会在这个时间内进行判断是否满足等待条件，如果成立就会立即返回，如果不成立，就会一直等待，直到等待你指定的最长等待时间，如果还是不满足，就会抛出异常，如果满足了就会正常返回
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_light():
    browser.get('https://www.taobao.com/')
    wait = WebDriverWait(browser, 10)
    input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    input.send_keys('杨佳林')
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
    button.click()
    time.sleep(4)
    print(input, button)
    browser.close()


def getcookie():
    browser.get('https://www.zhihu.com/explore')
    print(browser.get_cookies())
    browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'zhaofan'})
    print(browser.get_cookies())
    browser.delete_all_cookies()
    print(browser.get_cookies())


def qzone():
    browser.get('https://user.qzone.qq.com/')
    # 登录表单在页面的框架中，所以要切换到该框架
    browser.switch_to_frame('login_frame')
    browser.find_element_by_id('switcher_plogin').click()
    browser.find_element_by_id('u').clear()
    browser.find_element_by_id('u').send_keys('736659711')
    browser.find_element_by_id('p').send_keys('yxfxjj1997')
    browser.find_element_by_id('login_button').click()
    time.sleep(10)
    browser.get('https://user.qzone.qq.com/760712977/334')
    time.sleep(5)
    browser.close()


def zhihuLog():
    browser.get('https://www.zhihu.com/signin')
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').clear()
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').send_keys('15681953321')
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').clear()
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys('wozhiai0')
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/button').click()
    time.sleep(2)


zhihuLog()
