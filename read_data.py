"""Declaring Global Variables"""
PART_SEPARATOR = ' '
ROW_SEPARATOR = '\n'

process_records = []

def load_data(file_name):
    """Function to read data from a file"""
    try:
        with open(file_name, 'r') as process_infos:
            for process_info in process_infos:
                records={}
                single_row = process_info.replace(ROW_SEPARATOR, "")
                single_data = single_row.strip().split(PART_SEPARATOR)
                records['sequence'] = int(single_data[0])
                records['size'] = int(single_data[1])
                records['priority'] = single_data[2]
                if records['priority'] == 'HIGH':
                    records['priority'] = 2
                elif records['priority'] == 'MEDIUM':
                    records['priority'] = 1
                elif records['priority'] == 'LOW':
                    records['priority'] = 0
                process_records.append(records)
    except FileNotFoundError:
        pass
    return process_records
