import pandas as pd
import datetime 

# Excel row format:
# A = Company, B = Job Name, C = location, = application date
filename = 'assets\Application_Tracker.xlsx'

def add_to_xcell(job_id=1234567890, job_name='job2', company_name='company', location = 'place 01920192'):
    # Read an Excel file into a DataFrame
    df = pd.read_excel(filename)

    # add the new row then save
    df = df.append({
        'Job_Id': job_id,
        'Job': job_name, 
        'Company': company_name,
        'Location': location,
        'App Date':  datetime.datetime.now().strftime("%m/%d/%Y")
    }, ignore_index=True)
    df.to_excel(filename, index=False)


    # Auto-adjust column width
    writer = pd.ExcelWriter(filename) 
    df.to_excel(writer, sheet_name='sheetName', index=False, na_rep='NaN')
    for column in df:
        column_length = max(df[column].astype(str).map(len).max(), len(column))
        col_idx = df.columns.get_loc(column)
        writer.sheets['sheetName'].set_column(col_idx, col_idx, column_length + 5)
    writer.save()

def contains(job_id=1234567890, job_name='job', company_name='company', location = 'place 01920192'):
    df = pd.read_excel(filename)
    return df[(df['Job'] == job_name) & (df['Company'] == company_name) & (df['Location'] == location)].any().any()

if __name__ == '__main__':
    print(contains())
    