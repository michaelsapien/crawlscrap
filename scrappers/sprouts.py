# import requests
# class Sprouts:
#     keyword = keyword.replace(' ','+')
#     cookie='__cf_bm=7AbL0S30Pcvo.s1Sq837WS3ZpUqdRbYUNdXraCW4dnY-1690104823-0-AX6GHYFKi6snTp/8Ws7BV2Jni+afSOvKeEv1llKXY4Hm9/S3Pn2CPiOiVT41Byuyu3OdWijmQ4WGLMYbgrTgkh4=; _gid=GA1.2.740156594.1690104827; _gat_UA-47434162-1=1; _pin_unauth=dWlkPU5ESXdNak5rTmpZdE4yTmhNQzAwWVRjM0xUZzBNalF0TVRSa056Z3lORGszWW1OaA; __stripe_mid=f4b3da89-409a-42d7-80f0-6eda7f0ab82415e077; __stripe_sid=2e74a8e1-4a54-4a93-81dc-163d48e6bdfe02a896; loyaltyID=null; _uetsid=065be950293c11ee99af59b79cc96389; _uetvid=065d9830293c11eea88c6971cae0553b; session-sprouts=.eJwdjstygjAAAP8lZ-sAVivcKvgIQ8LIICFcGIQA4akEFOj038v0sJe97P6AMO2YyIGWRpVgKxA-WFdHDWt6oPXdsBjBhOBtE_ZtyRqgATaZ-f0cc5ub8DZDGXNTXS9SjhVvWphjpXrdK_UR6HAHa69EhE7YhZPl0pnW1x6fgwrr0jYoToXlnnJaHD9xbZbYLUfMoYCNNwe-mUbkyu0CjsjIFFzEb1t_c0qcPiLb_5avVCUsHkNCRmHpy1StDozIr8RH3G6cKSE3AesqT5YP5NItMo5vbGQT3khrDg8oC4jnBFnqeB_fxiadRzq08qXzCX3OunpBh_4pmUyAFRgE60KeAE2Rpf1u9yXtf_8ABkNrAw.F56Fkg.q7pA-dIYq6UARSuYabDigOUaNB4; _ga=GA1.1.1532536929.1690104827; _ga_LPZ816BHL5=GS1.1.1690104827.1.1.1690104851.36.0.0; _dd_s=rum=1&id=9ac1f64a-bf16-4d50-9cc5-ff47fe7163d9&created=1690104828205&expire=1690105751571'

#     URL='https://shop.sprouts.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=false&allow_autocorrect=true&limit=60&offset=0&search_is_autocomplete=false&search_provider=ic&search_term='+keyword+'&secondary_results=true&sort=rank&unified_search_shadow_test_enabled=false'

#     HEADERS = {

#         'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
#         'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
#         'Cookie': cookie
#     }
#     response = requests.get(URL,headers=HEADERS)
#     data=response.json()
#     items = data['items']
#     for item in items:
#         print('name:', item['name'])
#         print('base_price:', item['base_price'])
#         print('base_quantity:', item['base_quantity'])    