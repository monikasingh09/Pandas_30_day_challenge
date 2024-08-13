import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    return (
        employees
        .rename(columns={'event_day':'day'})
        .assign(total_time=employees['out_time'] - employees['in_time'])
        .groupby(['day', 'emp_id'])['total_time'].sum()
        .reset_index()
        )


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return (
        activity.groupby('player_id')['event_date'].min()
        .reset_index()
        .rename(columns = {'event_date' : 'first_login'})

    )


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return(
       teacher.groupby('teacher_id')['subject_id'].nunique()
       .reset_index()
       .rename(columns = {'subject_id' : 'cnt'} )
       )
    



def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
      data = courses.groupby('class')['student'].count().reset_index()
      return data.loc[(data['student'] >= 5) , ['class']]



def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return(
        orders['customer_number'].mode().to_frame()
    )



def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    return(
        activities.groupby('sell_date')['product']
        .agg([('num_sold', 'nunique'), 
        ('products', lambda x : ",".join(sorted(x.unique())))])
        .reset_index()
    )



def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return (daily_sales.groupby(['date_id', 'make_name'])
            .nunique().reset_index()
            .rename(columns={'lead_id': 'unique_leads','partner_id': 'unique_partners'})
        )
