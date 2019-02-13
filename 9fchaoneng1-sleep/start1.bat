@echo off
for /l %%a in (1,1,1) do (
echo "run case "%%a
pybot "E:\9fchaoneng\测试用例\新增工单.txt"
)