import pandas
from functions import *

initial_read = pandas.read_html('Payroll Report 7-15-2019 - 7-31-2019.xls')
master_list = remove_fluff_from_master_list(initial_read)
initial_read = None
instructor_df_groups = group_data_frames_by_instructor(master_list)

for group in instructor_df_groups:
	instructor_name = get_instructor_name_for_group(master_list, group)
	move_header_row_to_top_of_data_frame(master_list, group)
	# append_instructor_name_as_column(master_list, group)







'''

  pattern is:
	classes (with header row as last row)
	Vitalidad Movement Arts Center Total:
	Total for Instructor

	
		
	for each df list
		---last data frame in list has instr name, get from there
		---remove the VMAC Total df
		--move header from bottom to top of dataframe
		prepend new column = instructor name
		determine whether public or private?
		create file in format -> 00-Class-instructor .csv
		
		
	approach: no longer distinguish between public and private.
		add the instructor name as a new column at the begining of data frame
		every df goes into its own file
		do data column clean up here. replace appointment with class etc.
		
'''

print('x')
