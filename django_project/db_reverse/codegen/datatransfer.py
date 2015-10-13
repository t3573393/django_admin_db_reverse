#coding:utf8


def transfer_to_render_data(all_table_info):
    result = []

    for table_name, table_info in all_table_info.items():
        temp = dict()
        temp['model_name'] = table_name.title()
        temp['table_name'] = table_name
        temp['column_names'] =[a_column['COLUMN_NAME'] for a_column in table_info['columns']]
        primary_keys = list()
        # find the primary key, no find use the UNIQUE
        for a_constraint in table_info['constraints']:
            if a_constraint['CONSTRAINT_TYPE'] == 'PRIMARY KEY':
                primary_keys.append(a_constraint['COLUMN_NAME'])

        unique_indexs = dict()
        for a_constraint in table_info['constraints']:
            if a_constraint['CONSTRAINT_TYPE'] == 'UNIQUE':
                name = a_constraint['CONSTRAINT_NAME']
                if name not in unique_indexs:
                    unique_indexs[name] = list()
                unique_indexs[name].append(a_constraint['COLUMN_NAME'])

        temp['primary_keys'] = primary_keys if primary_keys else unique_indexs[unique_indexs.keys()[0]]
        temp['unique_keys'] = unique_indexs
        result.append(temp)
    return result