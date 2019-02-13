*** Settings ***
Library           Selenium2Library
Library           AutoItLibrary

*** Test Cases ***
总流程
    [Setup]
    打开浏览器    http://123.57.234.78:8700/wkWeb/index
    退出登录
    点击按键    确认
    选择菜单    登录
    文本框输入    身份证    420222198808281065
    文本框输入    姓名    曹阳俊
    点击按键    登录
    发送回车按键
    判断页面包含    token
    ${token}    Get Value    id=token
    log    ${token}
    选择菜单    额度审批状态查询
    文本框输入    用户身份证ID:    420222198808281065
    点击按键    查询
    sleep    2
    ${message}    Get Value    name=message
    ${appStatus}    Get Value    name=appStatus
    log    ${message} |${appStatus}
    选择菜单    个人信息
    文本框输入    姓名    曹阳俊
    文本框输入    身份证号    420222198808281065
    下拉框选择    行业    群众团体
    下拉框选择    职业    行政管理人员
    下拉框选择    学历    本科
    下拉框选择    婚姻    未婚
    文本框输入    手机号    15626513325
    文本框输入    常用邮箱    532720298@163.com
    文本框输入    公司名称    9f
    下拉框选择    关系    朋友
    文本输入    relativeName    黄婵
    文本输入    relativePhone    13689784524
    点击按键    下一步
    发送回车按键
    文本输入    realName    曹阳俊
    文本输入    idCardNo    420222198808281065
    点击按键    下一步
    发送回车按键
    选择菜单    信用授权
    click element    jquery=div:contains:('芝麻分授权')+a
    [Teardown]

登录
    打开浏览器    http://123.57.234.78:8700/wkWeb/index
    退出登录
    点击按键    确认
    选择菜单    登录
    文本框输入    身份证    420222198808281065
    文本框输入    姓名    曹阳俊
    点击按键    登录
    发送回车按键
    判断页面包含    token
    ${token}    Get Value    id=token
    log    ${token}
    关闭浏览器

额度审批状态查询
    登录操作
    选择菜单    额度审批状态查询
    文本框输入    用户身份证ID:    420222198808281065
    点击按键    查询
    sleep    2
    ${message}    Get Value    name=message
    ${额度审批状态:}    Get Value    name=appStatus
    log    ${message} |${额度审批状态:}
    关闭浏览器

个人信息
    登录操作
    选择菜单    个人信息
    文本框输入    姓名    曹阳俊
    文本框输入    身份证号    420222198808281065
    下拉框选择    行业    群众团体
    下拉框选择    职业    行政管理人员
    下拉框选择    学历    本科
    下拉框选择    婚姻    未婚
    文本框输入    手机号    15626513325
    文本框输入    常用邮箱    532720298@163.com
    文本框输入    公司名称    9f
    下拉框选择    关系    朋友
    文本输入    relativeName    黄婵
    文本输入    relativePhone    13689784524
    点击按键    下一步
    发送回车按键
    文本输入    realName    曹阳俊
    文本输入    idCardNo    420222198808281065
    点击按键    下一步
    发送回车按键
    关闭浏览器

额度查询接口测试
    登录操作
    选择菜单    额度查询接口测试
    文本框输入    身份证    420222198808281065
    点击按键    查询
    ${消息}    Get Value    name=message
    ${总额度}    Get Value    name=totalAmt
    ${信用额度}    Get Value    name=loanAmtPrimitive
    ${剩余额度}    Get Value    name=loanAmt
    log    ${消息} | ${总额度} |${信用额度} |${剩余额度}
    关闭浏览器

实名认证
    登录操作
    选择菜单    实名认证
    文本输入    realName    曹阳俊
    文本输入    idCardNo    420222198808281065
    点击按键    下一步
    发送回车按键
    关闭浏览器

代扣银行卡变更
    登录操作
    选择菜单    代扣银行卡变更
    input text    name=newbankcard    6222601310021811096
    input text    name=newphone    15626513325
    发送回车按键
    关闭浏览器

信用授权
    登录操作
    选择菜单    信用授权
    click element    xpath=(//a[contains(text(),'未授权')])[1]
    点击按键    同意授权

*** Keywords ***
文本框输入
    [Arguments]    ${name}    ${value}
    input text    jquery=div>label:contains(${name})+div>input    ${value}

点击按键
    [Arguments]    ${name}
    sleep    2
    click button    jquery=div button:contains(${name})

选择菜单
    [Arguments]    ${name}
    sleep    1
    click element    jquery=li>a:contains(${name})

打开浏览器
    [Arguments]    ${url}
    open browser    ${url}    chrome
    Maximize Browser Window
    sleep    2

退出登录
    click element    xpath=//div[1]/div/div[2]/ul/li[3]/a/i

发送回车按键
    sleep    1
    send    {Enter}

判断页面包含
    [Arguments]    ${text}
    sleep    2
    page should contain    ${text}

下拉框选择
    [Arguments]    ${name}    ${value}
    Wait Until Keyword Succeeds    10    2    Select From List    jquery=div>label:contains('${name}')+div>select    ${value}

文本输入
    [Arguments]    ${id}    ${value}
    input text    id=${id}    ${value}

登录操作
    打开浏览器    http://123.57.234.78:8700/wkWeb/index
    退出登录
    点击按键    确认
    选择菜单    登录
    文本框输入    身份证    420222198808281065
    文本框输入    姓名    曹阳俊
    点击按键    登录
    发送回车按键
    判断页面包含    token
    ${token}    Get Value    id=token
    log    ${token}

关闭浏览器
    Close Browser
