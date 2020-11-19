import json
import  xlrd

def openSheet(filepath,clo,row):
 '''
 :param filepath: 接口测试文件名
 :param clo: 列位置
 :param row: 行位置
 :return:  返回值
 '''
 findfile=xlrd.open_workbook(filename=filepath)
 sheet=findfile.sheet_by_index(0)
 rowResult=sheet.cell_value(colx=clo,rowx=row)
 rowvalue=json.loads(rowResult)
 return rowvalue



if __name__=="__main__":
   openSheet(filepath='E:\\DevWorkSpace\\pythonstudio\\yj_application_apiTest\\data\\接口测试模板-登录.xlsx',clo=9,row=2)
  # sheettools(filepath='E:\\DevWorkSpace\\pythonstudio\\yj_application_apiTest\\data\\接口测试模板-登录.xlsx')


