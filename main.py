import pandas

list = pandas.read_html('Payroll Report 7-15-2019 - 7-31-2019.xls')
for df in list:
    new_header = df.iloc[-1:]
    print(new_header)
    '''

  pattern is:
    classes (with header row as last row)
    Vitalidad Movement Arts Center Total:
    Total for Instructor

    loop through list of dfs
    create new list of dfs for each instructor
        - while 'Total for' not in df[0,0], add to list
        
    for each df list
        last data frame in list has instr name, get from there
        remove the VMAC Total df
        prepend new column = instructor name
        determine whether public or private?
        create file in format -> 00-Class-instructor .csv
        
'''

print('x')
