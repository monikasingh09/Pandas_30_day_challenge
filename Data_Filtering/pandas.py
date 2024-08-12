import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world['area'] >= 3000000) | (world ['population'] >= 25000000)]
    return df[['name','population','area']]



def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return df[['product_id']]


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers[~customers['id'].isin(orders['customerId'])]
    return df[['name']].rename(columns = {'name':'Customers'})


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]
    udf = df['author_id'].unique()
    udf = sorted(udf)
    return pd.DataFrame({'id':udf})

