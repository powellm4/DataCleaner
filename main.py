import pandas
from functions import *

create_folder('csvs')
initial_read = pandas.read_html('Payroll Report 7-15-2019 - 7-31-2019.xls')
master_list = remove_fluff_dfs_from_master_list(initial_read)
initial_read = None
instructor_df_groups = group_data_frames_by_instructor(master_list)

for group in instructor_df_groups:
	instructor_name = get_instructor_name_for_group(master_list, group)
	move_header_row_to_top_of_data_frame(master_list, group)
	append_instructor_name_as_column(master_list, group, instructor_name)
	# write_group_to_csv(master_list, group, instructor_name)


master_list = remove_totals_dfs_from_master_list(master_list)


for index, df in enumerate(master_list):
	df = drop_nan_columns(df)
	df = format_column_headers(df)
	df = drop_unnecessary_columns(df)
	df = remove_quotes(df)
	df = format_client_name(df)
	df = sort_by_date_time(df)
	master_list[index] = df
	write_df_to_csv(df)

write_master_list_to_csv(master_list)

print('x')






'''

  pattern is:
	classes (with header row as last row)
	Vitalidad Movement Arts Center Total:
	Total for Instructor

	
		
	for each df list
		-X-last data frame in list has instr name, get from there
		-X-remove the VMAC Total df
		-X-move header from bottom to top of dataframe
		-X-prepend new column = instructor name
		-X-remove Total df from master_list
		-X-write master list to one csv
		-X-combine all group df's into 1 dataframe 
		-X-create file in format -> 01-Class-instructor.csv
		---look up pandas read html for colspan=3 causing 3 duplicate columns
		

		
'''

