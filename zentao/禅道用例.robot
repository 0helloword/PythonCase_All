*** Settings ***
Resource          基础关键字.txt
Resource          业务流程关键字.txt

*** Test Cases ***
01添加需求和任务
    循环创建需求任务    添加需求和任务

02添加任务
    循环创建需求任务    添加任务
