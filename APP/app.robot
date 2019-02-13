*** Settings ***
Library           AppiumLibrary
Library           AutoItLibrary

*** Test Cases ***
test1
    #app6.0英文版本下的创建联系人
    Open Application    http://localhost:4723/wd/hub    platformName=Android    platform Version=6.0    deviceName=192.168.64.101:5555    appPackage=com.android.contacts    appActivity=.activities.PeopleActivity
    Click Element    name=Create a new contact
    Click Element    name=Add account
    Input Text    name=Email address    123456@qq.com
    Click Element    name=Next
    Input Text    id=com.android.email:id/regular_password    123456
    Click Element    name=Next
    Click Element    name=Next
    Close Application

真机oppo测试
    Open Application    http://localhost:4723/wd/hub    platformName=Android    platform Version=5.1    deviceName=EATGNJCYBADAGEU8    appPackage=com.jiufu.heyuanwanka    appActivity=.ui.activity.StartLoadingActivity
    sleep    15
    Comment    Wait Until Element Is Visible    name=我的
    Click Element    name=我的
    Click Element    name=点击登录
    Input Text    name=手机号码/世纪佳缘账号    15626513325
    Input Text    id=com.jiufu.heyuanwanka:id/et_psd_numb    123456
    Click Element    id=com.jiufu.heyuanwanka:id/btn_confirm
    sleep    10
    Click Element    name=首页
    Close Application
