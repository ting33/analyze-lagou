#给没有加column的数据加上column
import pandas as pd

def get_key_names():
    return ['positionId', 'city', 'companyShortName', 'companyId', 'companySize', 'createTime', 'education',
            'famousCompany', 'financeStage', 'industryField', 'salary', 'salaryMonth', 'workYear',
            'jobNature', 'positionAdvantage']

def get_key_list_names():
    return ['companyLabelList', 'hitags', 'positionLables']


def add_column_names(origin_data_path, column_names, save_data_path):
    data = pd.read_csv(origin_data_path, sep='\t', names=column_names)
    data.to_csv(save_data_path, sep='\t', index=False)


if __name__ == "__main__":
    origin_path = '/Users/zhouya/Documents/工作/mycode/analyze-lagou/data/jobList_全国.txt'
    save_path = '/Users/zhouya/Documents/工作/mycode/analyze-lagou/data/jobList_全国_1.txt'
    columns = get_key_names() + get_key_list_names()
    add_column_names(origin_path, columns, save_path)
    # a = [[1, 2]]
    # column = ['a', 'b']
    # data = pd.DataFrame(data=a, columns=column)
    # print(data)
