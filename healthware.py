from playwright.sync_api import Playwright, sync_playwright
import sys
import time

username = sys.argv[1]
password = sys.argv[2]

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://my.zcst.edu.cn/_web/sopplus/sopplus/index.html
    page.goto("https://my.zcst.edu.cn/_web/sopplus/sopplus/index.html")
    # Go to https://authserver.zcst.edu.cn/cas/login?service=https%3A%2F%2Fmy.zcst.edu.cn%2FportalRedirect.jsp%3F_p%3DYXM9MSZwPTEmbT1OJg__
    page.goto("https://authserver.zcst.edu.cn/cas/login?service=https%3A%2F%2Fmy.zcst.edu.cn%2FportalRedirect.jsp%3F_p%3DYXM9MSZwPTEmbT1OJg__")
    # Click [placeholder="用户名/手机号/邮箱"]
    page.click("[placeholder=\"用户名/手机号/邮箱\"]")
    # Fill [placeholder="用户名/手机号/邮箱"]
    page.fill("[placeholder=\"用户名/手机号/邮箱\"]", username)
    # Click [placeholder="密码"]
    page.click("[placeholder=\"密码\"]")
    # Fill [placeholder="密码"]
    page.fill("[placeholder=\"密码\"]", password)
    # Click text=登 录
    page.click("text=登 录")
    # assert page.url == "https://my.zcst.edu.cn/_web/sopplus/sopplus/index.html"
    # Click text=健康卡填报10427人收藏
    with page.expect_popup() as popup_info:
        page.click("text=健康卡填报")
    page1 = popup_info.value
    time.sleep(5)
    # Click text=我要办理
    with page1.expect_popup() as popup_info:
        page1.click("text=我要办理")
    page2 = popup_info.value
    time.sleep(5)
    # Click text=为了全力做好学校新型冠状病毒感染的肺炎疫情防控工作，我承诺以下内容填写属实。 30s 已阅读并同意 >> ins
    page2.click("text=为了全力做好学校新型冠状病毒感染的肺炎疫情防控工作，我承诺以下内容填写属实。 30s 已阅读并同意 >> ins")
    # Click text=下一步
    page2.click("text=下一步")
    # Click text=本人承诺登记后、到校前不再前往其他地区 >> ins
    page2.click("text=本人承诺登记后、到校前不再前往其他地区 >> ins")
    # Click button:has-text("提交")
    page2.click("button:has-text(\"提交\")")
    # Click a:has-text("确定")
    page2.click("a:has-text(\"确定\")")
    # Close page
    page2.close()
    print("Successfully!")
    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)
