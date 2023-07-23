import requests
keyword='oranges'
keyword = keyword.replace(' ','+')
cookie='_fbp=fb.1.1677429315931.1313864373;_pin_unauth=dWlkPU1ETmhOV1l3TUdRdE9HVmlNUzAwTURVNUxXSmtZamN0TXpNNVl6SmtObU5rWkROaQ;ajs_anonymous_id=84c5f7a7-f9d2-4bbe-97fa-5a49e09ab80a;_pin_unauth=dWlkPU1ETmhOV1l3TUdRdE9HVmlNUzAwTURVNUxXSmtZamN0TXpNNVl6SmtObU5rWkROaQ;ajs_anonymous_id=84c5f7a7-f9d2-4bbe-97fa-5a49e09ab80a;__stripe_mid=fd0e7b64-53a7-4e25-b07f-6388af276178ebcd3a;_gcl_au=1.1.1406692167.1686887871;__cf_bm=Fv2PUMiVEr87SrHVR.siTMTrN6s2rp7KCYv9HkRqIV4-1689609053-0-AZTud1JDASF20rvrVDfux3AP9M5KIw1RnzRtUM3oI5hVg1BSZGEmLR6AnR3xStwAu7Y9btpCr2J95jKnVbZHiIA=;AMCVS_68B620B35350F1650A490D45%40AdobeOrg=1;wfm.tracking.sessionStart=1689609053421;kndctr_68B620B35350F1650A490D45_AdobeOrg_identity=CiY3ODEyMTc0NzM0NTE4MTMxMjgwMTU3ODMwMzUyMzY4MDY1Mjg0NVIPCLyz0PToMBgBKgRJTkQx8AHWy7CkljE=;kndctr_68B620B35350F1650A490D45_AdobeOrg_cluster=ind1;_derived_epik=dj0yJnU9aXdudU4xSWYzdnBVRl90QVpZakJqUVdWVk1YMl9vbGUmbj14WG5LN1YxRlJvSkdvdjAxT2VHcTJBJm09MSZ0PUFBQUFBR1MxWTE0JnJtPTEmcnQ9QUFBQUFHUzFZMTQmc3A9NQ;wfmStoreId=16; at_check=true; s_loginSuccess=0; s_cc=true;wfm.modals.wfmCovidTooltip=1;dotcomSearchId=79dce3f4-41f0-480f-af6a-2b72406a374d;lux_uid=168960906329734040; wfm.tracking.x2p=1;AMCV_68B620B35350F1650A490D45%40AdobeOrg=179643557%7CMCIDTS%7C19556%7CMCMID%7C78121747345181312801578303523680652845%7CMCAAMLH-1690213863%7C12%7CMCAAMB-1690213863%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1689616263s%7CNONE%7CvVersion%7C5.5.0;_derived_epik=dj0yJnU9bU5MVVRkdVc4c3dnRzJzcW5QdVFHZWtZZWFYUlMwMFAmbj0zZGhWazVGS04zYm9HWHNSTFJMWlZRJm09MSZ0PUFBQUFBR1MxWTJnJnJtPTEmcnQ9QUFBQUFHUzFZMmcmc3A9NQ;at_check=true; __stripe_sid=53f2fb39-7289-4fce-8ec8-36cfcd000ed1abb062;gpv_pn=Search%20Results%3A%20oranges%20%7C%20Wegmans; s_ips=694;s_tp=6818; s_ppv=Search%2520Results%253A%2520oranges%2520%257C%2520Wegmans%2C10%2C10%2C694%2C1%2C9;_uetsid=b6818ed024b911eeacb7712d4cfbdcf0;_uetvid=7f3b48a0b78c11ed8587a33d8b5d2694;session-prd-weg=.eJwdjsGOgjAABf-lZ2MsggI3o0ZLLF3dSikXgrYuhYqGAgpm_33JHt5lDm_mA9JbLU0O_FumjZyA9Cnre1bJqgF-U7cjMdIY9ajS5lHKCvhA9kF-2V0VUQE6DwiGKvCmI4RXK-rHDVdLdxftPZM1WqBC5Lg4zzHV-sCCgux4E26QzXuo-CDKA-WvpDhpTlcOHrZz8o0MqqIhiYNbxo6KFNgO6fZNNj8WWb8UZ6cmY86_K7Z0iYpnK9jbHNZj1N1rJYOdiLEi1akX7GzQXedi7MCU22R0EbqC4X42ZZWMctyQbnx1trSNy5nNaIeXPAqx6xyNR76a2T4xyxWYgNbIOlUC-HPXgdB1F-7vH27XaUY.F5b0-g.Y7c7qkO6rvtVX3QH0Guyn5JFEOE;_dd_s=rum=0&expire=1689609983072;mbox=session#96aabcd293084f47a5cabe5611de2d59#1689610944|PC#96aabcd293084f47a5cabe5611de2d59.41_0#1752853868'

URL='https://shop.wegmans.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=false&allow_autocorrect=true&limit=60&offset=0&search_is_autocomplete=false&search_provider=ic&search_term='+keyword+'&secondary_results=true&sort=rank&unified_search_shadow_test_enabled=false'

HEADERS = {

    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie': cookie
}
response = requests.get(URL,headers=HEADERS)
data=response.json()
items = data['items']
for item in items:
    print('name:', item['name'])
    print('base_price:', item['base_price'])
    print('base_quantity:', item['base_quantity'])    