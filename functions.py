import os
import pandas as pd
import numpy as np

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


def remove_fluff_dfs_from_master_list(master_list):
	new_master = []
	for index, df in enumerate(master_list):
		if 'Vitalidad Movement Arts Center' not in df.iloc[0][0]:
			new_master.append(df)
	return new_master


def remove_totals_dfs_from_master_list(master_list):
	new_master = []
	for index, df in enumerate(master_list):
		if 'Total for' not in df.iloc[0][0] \
				and '# Clients' not in df.columns\
				and 'Grand total' not in df.iloc[0][0]:
			new_master.append(df)

	return new_master


def move_header_row_to_top_of_data_frame(master_list, group):
	list_length = len(group)
	for i in range(0, list_length-1):
		df = master_list[group[i]]
		new_header = df.iloc[-1]
		df.columns = new_header
		df.drop(df.tail(2).index, inplace=True)


def append_instructor_name_as_column(master_list, group, instructor_name):
	list_length = len(group)
	for i in range(0, list_length):
		df = master_list[group[i]]
		df = df.assign(Instructors=instructor_name)
		master_list[group[i]] = df


# def write_group_to_csv(master_list, group, instructor_name):

def write_master_list_to_csv(master_list):
	for df in master_list:
		if os.path.isfile("%s%s.csv" % ('output/', '00-01-Class-All')):
			mode = "a"
			include_header = False
		else:
			mode = "w"
			include_header = True
		df.to_csv("%s%s.csv" % ('output/', '00-01-Class-All'), mode=mode, header=include_header, index=False)


# creates the [folder] inside the /output/ folder
def create_folder(folder):
    if not os.path.exists('output/'):
        os.mkdir('output/')
    if not os.path.exists(folder):
        os.mkdir(folder)


def format_column_headers(df):
    df.columns = [c.strip() for c in df.columns]
    df.columns = [c.replace(' ', '_') for c in df.columns]
    df.columns = [c.replace('.', '') for c in df.columns]
    df.columns = [c.replace('"', '') for c in df.columns]
    df.columns = [c.replace('Appointment', 'Class') for c in df.columns]
    df.columns = [c.replace('Appt', 'Class') for c in df.columns]
    return df


def format_client_name(df):
    df.Client_Name = df.Client_Name.str.replace(" ", "")
    return df


def sort_by_date_time(df):
    df.Class_Date = pd.to_datetime(df.Class_Date)
    return df.sort_values(by=['Class_Date', 'Class_Time'])

def remove_quotes(df):
    df = df.apply(lambda x: x.str.strip())
    return df.apply(lambda x: x.str.strip('"'))


def drop_nan_columns(df):
	df = df.dropna(axis='columns', how='all')

	# for idx in df.columns._nan_idxs:
	# 	df = df.drop([1, idx])
	return df

def drop_unnecessary_columns(df):
	if "Unnamed:_5" in df.columns:
		df = df.drop(columns=["Unnamed:_5"])
	if "Earnings_per_Client" in df.columns:
		df = df.drop(columns=["Earnings_per_Client"])
	if "Earnings" in df.columns:
		df = df.drop(columns=["Earnings"])
	if "Revenue" in df.columns:
		df = df.drop(columns=["Revenue"])
	if "Rev_per_Session" in df.columns:
		df = df.drop(columns=["Rev_per_Session"])
	return df