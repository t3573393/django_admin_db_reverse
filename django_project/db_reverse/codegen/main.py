#coding:utf8
from . import coderender, datatransfer, dbextract, filecompress

def generate_file(type=1):
    all_table_info = dbextract.get_db_all_info()
    transfer_data = datatransfer.transfer_to_render_data(all_table_info)

    if type == 1:
        models_str = coderender.render_models(transfer_data)
        admin_str = coderender.render_admin(transfer_data)
        filecompress.save_string_to_file('models.py', models_str)
        filecompress.save_string_to_file('admin.py', admin_str)
        filecompress.compress_in_folder()
    elif type == 2:
        markdown_str = coderender.render_markdown(transfer_data)
        filecompress.save_string_to_file('tables.md', markdown_str)
