from pages.login_page import LoginPage
from framework.utils.excel_loader import load_excel_kv


def test_login(driver, config):
    """
    测试数据来源：data/testdata.xlsx（key/value 两列）
    期望 key（示例）：
      - login.username
      - login.password
      - login.url   （可选：不填就用 config.yaml 的 project.base_url）
    """
    data = load_excel_kv(config["paths"]["data"])

    username = data["login.username"]
    password = data["login.password"]
    url = data.get("login.url", config["project"]["base_url"])

    page = LoginPage(driver, config["locator_loader"])
    page.open(url)
    page.login(username, password)

    # 这里按你自己的校验方式来（id/xpath 你自己搞定）
    # 示例：登录后断言某个元素存在 / url 变化 / title 等
    # assert "Dashboard" in driver.title
