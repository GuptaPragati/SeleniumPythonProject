from playwright.sync_api import Playwright

order_payload={"orders":[{"country":"India","productOrderedId":"67a8dde5c0d3e6622a297cc8"}]}


class ApiUtils:

    def get_token(self, playwright:Playwright, user_creds:dict):
        login_payload = {"userEmail": user_creds['user_email'], "userPassword": user_creds['user_password']}
        api_req_context=playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response= api_req_context.post(url="api/ecom/auth/login", data=login_payload)
        assert response.ok
        return  response.json()["token"]

    def create_order(self, playwright:Playwright, user_creds:dict):
        token=self.get_token(playwright, user_creds)
        req_context=playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response= req_context.post(url="api/ecom/order/create-order",
                         headers={"Content-Type": "application/json",
                                  "authorization":token},data=order_payload)
        return response.json()["orders"][0]

