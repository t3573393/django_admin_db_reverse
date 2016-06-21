#coding:utf8


def transfer_to_render_data(all_table_info):
    result = list()

    for table_name, table_info in all_table_info.items():
        temp = dict()
        temp['model_name'] = table_name.title().replace('_', '')
        temp['table_name'] = table_name
        temp['comment'] = table_info['comment'] if table_info['comment'] else table_name
        temp['column_names'] = [a_column['COLUMN_NAME'] for a_column in table_info['columns']]
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

        # set the column field
        column_list = list()
        for a_column in table_info['columns']:
            temp_dict = {
                'name': a_column['COLUMN_NAME'],
                'comment': a_column['COLUMN_COMMENT'],
                'null': True if a_column['IS_NULLABLE'] == 'YES' else False,
                'primary_key': True if a_column['COLUMN_NAME'] in primary_keys else False
            }
            if a_column['DATA_TYPE'] in ['int', 'tinyint']:
                temp_dict['data_type'] = 'int'
                temp_dict['precision'] = a_column['NUMERIC_PRECISION']
            elif a_column['DATA_TYPE'] == 'bigint':
                temp_dict['data_type'] = 'bigint'
                temp_dict['precision'] = a_column['NUMERIC_PRECISION']
            elif a_column['DATA_TYPE'] == 'datetime':
                temp_dict['data_type'] = 'datetime'
            elif a_column['DATA_TYPE'] == 'date':
                temp_dict['data_type'] = 'date'
            elif a_column['DATA_TYPE'] == 'varchar':
                temp_dict['data_type'] = 'varchar'
                temp_dict['max_length'] = a_column['CHARACTER_MAXIMUM_LENGTH']
            elif a_column['DATA_TYPE'] == 'decimal':
                temp_dict['data_type'] = 'decimal'
                temp_dict['precision'] = a_column['NUMERIC_PRECISION']
                temp_dict['scale'] = a_column['NUMERIC_SCALE']
            else:
                temp_dict['data_type'] = a_column['DATA_TYPE']
            column_list.append(temp_dict)
        temp['columns'] = column_list
        result.append(temp)
    return result