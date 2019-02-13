*** Settings ***
Library           RequestsLibrary
Library           Collections
Library           XML
Library           D:/Users/test/Desktop/response.py
Resource          1.txt
Library           Selenium2Library

*** Test Cases ***
case1
    Create Session    api    http://localhost:8000
    ${addr}    Get Request    api    users/1
    Should Be Equal As Strings    ${addr.status_code}    200
    Log    ${addr.content}
    ${responsedata}    To Json    ${addr.content}
    ${keys}    Get Dictionary Keys    ${responsedata}
    ${items}    Get Dictionary Items    ${responsedata}
    ${values}    Get Dictionary Values    ${responsedata}
    ${str}    Get From Dictionary    ${responsedata}    1
    ${addr}    Get Request    api    users/5
    Should Be Equal As Strings    ${addr.status_code}    404
    Log    ${addr.content}
    ${responsedata}    To Json    ${addr.content}
    ${keys}    Get Dictionary Keys    ${responsedata}
    ${items}    Get Dictionary Items    ${responsedata}
    ${values}    Get Dictionary Values    ${responsedata}
    ${str}    Get From Dictionary    ${responsedata}    message
    Delete All Sessions

case2
    Create Session    api    http://localhost:8000
    ${addr}    Get Request    api    hello/qitao
    Comment    Should Be Equal As Strings    ${addr.status_code}    200
    Log    ${addr.content}
    ${responsedata}    To Json    ${addr.content}
    ${keys}    Get Dictionary Keys    ${responsedata}
    ${items}    Get Dictionary Items    ${responsedata}
    ${values}    Get Dictionary Values    ${responsedata}
    ${str}    Get From Dictionary    ${responsedata}    hello
    #xml方式
    ${dict}    Create Dictionary    accept=application/xml
    ${addr}    Get Request    api    hello/qitao    ${dict}
    Comment    Should Be Equal As Strings    ${addr.status_code}    200
    Log    ${addr.content}
    ${responsedata}    Set Variable    ${addr.content}
    ${body}    Get Element Text    ${responsedata}    hello
    ${hello}    Get Element    ${responsedata}    hello
    Log    ${hello.text}
    ${responsedata}    Add Element    ${responsedata}    <new id="3">test</new>
    ${new}    Get Element Attribute    ${responsedata}    id    new
    Log    ${new}
    ${a}    Element To String    ${responsedata}
    Delete All Sessions

case3
    #用户密码
    ${auth}    Create List    ok    python
    Create Session    api    http://localhost:8000    \    \    ${auth}
    ${addr}    Get Request    api    401
    Comment    Should Be Equal As Strings    ${addr.status_code}    200
    Log    ${addr.content}
    ${responsedata}    To Json    ${addr.content}
    ${keys}    Get Dictionary Keys    ${responsedata}
    ${items}    Get Dictionary Items    ${responsedata}
    ${values}    Get Dictionary Values    ${responsedata}
    ${str}    Get From Dictionary    ${responsedata}    pass
    Delete All Sessions

case4
    ${dict}    Create Dictionary    Content-Type=application/x-www-form-urlencoded
    Create Session    api    http://localhost:8000    ${dict}
    ${data}    Create Dictionary    username=qitao    password=qt
    ${addr}    Post Request    api    post    data=${data}
    Comment    Should Be Equal As Strings    ${addr.status_code}    200
    Log    ${addr.content}
    Log    ${addr.json()}
    ${responsedata}    To Json    ${addr.content}
    ${keys}    Get Dictionary Keys    ${responsedata}
    ${items}    Get Dictionary Items    ${responsedata}
    ${values}    Get Dictionary Values    ${responsedata}
    ${str}    Get From Dictionary    ${responsedata}    username
    Delete All Sessions

case
    ${a}    compare_primary_data    {"balance":51.00,"bank_name":0","bank_name":"0","bill_date":"2017-08-01","bill_id":"e9af3a27-6c5e-4518-b665-66f789efc014","bill_month":"2017-08","bill_type": "DONE","cash_limit": 0,"credit_limit": 0,"installments": [],"interest":0}    {"balance":51.00,"bank_name":0","bank_name":"0","bill_date":"2017-08-01","bill_id":"e9af3a27-6c5e-4518-b665-66f789efc014","bill_month":"2017-08","bill_type": "DONE","cash_limit": 0,"credit_limit": 0,"installments": [],"interest":0}
    Comment    ${b1}    Set Variable    {"balance": 511.00,"bank_name": "111"}
    Comment    ${b2}    to_structure_from_str    {"balance": 511.00,"bank_name": "111"}
    Comment    ${c}    compare_primary_dict    {"balance": 511.00,"bank_name": "111"}    {"balance": 511.00,"bank_name": "111"}
    Comment    ${d}    compare_primary_list    {"balance": 511.00,"bank_name": "1111"}    {"balance": 511.00,"bank_name": "111"}

case6
    open browser    file:///D:/Users/test/Desktop/1_card_1.html    chrome
    Sleep    2
    ${a}    Get Text    xpath=/html/body/ul[1]/li[1]
    ${b}    Get Text    xpath=/html/body/ul[1]/li[2]
    ${b}    Get Text    xpath=/html/body/div/span
    Close browser
    [Teardown]    Close browser

1
    读取excel数据
    open browser    file:///D:/Users/test/Desktop/1_card_acount.html    chrome
    Sleep    2
    ${a}    Get Text    jquery=div ul li>a:contains('可用额度')>span
    ${b}    Get Text    jquery=div ul li>a:contains('信用额度')>span
    ${c}    Get Text    jquery=div ul li>a:contains('预借现金额度')>span
    open browser    file:///D:/Users/test/Desktop/1_card.html    chrome
    Sleep    2
    ${d}    Get Text    jquery=div>ul>li>a:contains('卡')
    Comment    ${e}    Get Text    jquery=div p>span:contains('**')
    ${f}    Get Text    jquery=div p:contains('（')
    Close All browsers
    [Teardown]    close browser

2
    读取excel数据
