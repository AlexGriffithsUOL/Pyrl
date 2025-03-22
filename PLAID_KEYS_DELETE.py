PLAID_CLIENT_ID='679fb4ba99e8220024b9616e'
PLAID_TEST_KEY='19f259a1fe29ff0b53c6e15eb990cd'
SANDBOX_URL='https://sandbox.plaid.com/link/token/create'
import plaid.plaid
import requests

response = requests.get(SANDBOX_URL)
print(response.content)