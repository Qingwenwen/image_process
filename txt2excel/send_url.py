import urllib
url = 'http://console.oceanstack.slancer.com/account/alipay/notify_url'
url_data = 'seller_email=ghxw686868%40163.com' \
           '&sign=9f6a323e4219648b3e49b4a607e51d27' \
           '&subject=%E8%B4%A6%E6%88%B7%E5%85%85%E5%80%BC' \
           '&is_total_fee_adjust=N' \
           '&gmt_create=2018-06-22+11%3A37%3A41' \
           '&out_trade_no=9b4999fa311e0fdb9addb0a3829ad4f2' \
           '&sign_type=MD5' \
           '&price=85.00' \
           '&buyer_email=180%2A%2A%2A%2A7329' \
           '&discount=0.00' \
           '&trade_status=TRADE_SUCCESS' \
           '&gmt_payment=2018-06-22+11%3A37%3A48' \
           '&trade_no=2018062221001004200521029599' \
           '&seller_id=2088311276421285' \
           '&use_coupon=N' \
           '&payment_type=1' \
           '&total_fee=85.00' \
           '&notify_time=2018-06-22+13%3A01%3A13' \
           '&buyer_id=2088902256897202' \
           '&notify_id=6c612c946d1581636d1c99ecb316bf4hjp' \
           '&notify_type=trade_status_sync' \
           '&quantity=1'
print urllib.urlopen(url, url_data).read()
