import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    stats = actor_director.groupby(['actor_id','director_id']).agg(count=('director_id','count')).reset_index()
    return stats[(stats['count'] >= 3)] [['actor_id','director_id']]



def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    return(
        pd.merge(employees, employee_uni,how = 'left' , on = 'id')[['unique_id', 'name']]
    )


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    left_table = pd.merge(students,subjects,how='cross').sort_values(['student_id', 'subject_name'])
    subject_count = examinations.groupby(['student_id','subject_name']).agg(attended_exams = ('subject_name','count')).reset_index()
    final =  pd.merge(left_table, subject_count, how='left', on=['student_id','subject_name'])
    final['attended_exams'] = final['attended_exams'].fillna(0)
    return final


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
        mgr = employee.groupby('managerId').agg(reportees = ('id', 'count')).reset_index()
        mgr_5 = mgr[mgr['reportees'] >=5]['managerId']
        return(employee[employee['id'].isin(mgr_5)][['name']])


def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    order_comp = pd.merge(orders,company,how='left',on='com_id')
    red_sales_id = order_comp[order_comp['name'] == 'RED']['sales_id']
    names = sales_person[~sales_person['sales_id'].isin(red_sales_id)][['name']]
    return(names)


