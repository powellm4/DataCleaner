
def is_instructor_name_df(df):
	if 'Total for' in df.iloc[0][0]:
		return True


def group_data_frames_by_instructor(df_list):
	instructor_df_groups = []
	indices = []
	for index, df in enumerate(df_list):
		if is_instructor_name_df(df):
			indices.append(index)
			instructor_df_groups.append(indices)
			indices = []
		else:
			indices.append(index)
	return instructor_df_groups


def get_instructor_name_for_group(master_list, group):
	index = group[-1]
	df = master_list[index]
	name = df.iloc[0][0].replace('Total for', '').strip()
	return name


def remove_fluff_from_master_list(master_list):
	new_master = []
	for index, df in enumerate(master_list):
		if 'Vitalidad Movement Arts Center' not in df.iloc[0][0]:
			new_master.append(df)
	return new_master


def move_header_row_to_top_of_data_frames(master_list, group):
	list_length = len(group)
	for i in range(0, list_length-1):
		df = master_list[group[i]]
		new_header = df.iloc[-1]
		df.columns = new_header
		df.drop(df.tail(2).index, inplace=True)


def append_instructor_name_as_column(master_list, group, name):
	list_length = len(group)
	for i in range(0, list_length-1):
		group[i]
		df = master_list[group[i]]
		df.insert(loc=0, column='Instructor', value=name)

