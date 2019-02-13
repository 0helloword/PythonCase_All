#-*- coding: utf8 -*-

from os.path import join
from xlrd import open_workbook
from xlutils.copy import copy
import os,sys

class ReadAndWriteExcel:

    def __init__(self):
        self.FilePath='G:\\pythonCase\\1.xls'
        self.sheetName='Sheet1'
        self.rb=None

    def Set_ExcelPath(self,FilePath):
        self.FilePath=FilePath.replace('\\', '/')
        self.rb=open_workbook(self.FilePath,'r+b')

#д����
    def Write_Excel(self,sheetName,rowIndex,lineIndex,content):
        rbook=open_workbook(self.FilePath,'w')
        wb=copy(rbook)
        sheetIndex=rbook.sheet_names().index(sheetName)
        wb.get_sheet(int(sheetIndex)).write(int(rowIndex),int(lineIndex),content)
        wb.save(self.FilePath)
        print 'write file ok'

# ��ȡĳһ������
    def Get_RowIndexData_By_SheetName(self,sheetName,rowIndex):
        return self.rb.sheet_by_name(sheetName).row_values(int(rowIndex))

#��ȡĳһ������
    def Get_ColIndexData_By_SheetName(self,sheetName,colIndex):
        return self.rb.sheet_by_name(sheetName).col_values(int(colIndex))

#��ȡ������
    def Get_RowCount_By_SheetName(self,sheetName):
        return int(self.rb.sheet_by_name(sheetName).nrows)

# ��ȡ������
    def Get_columnCount_By_SheetName(self,sheetName):
        return int(self.rb.sheet_by_name(sheetName).ncols)

# ��ȡĳ����Ԫ���ֵ
    def Get_Cell_By_ColIndex_RowIndex(self,sheetName,rowIndex,colIndex):
        return self.rb.sheet_by_name(sheetName).cell_value(int(rowIndex),int(colIndex))
