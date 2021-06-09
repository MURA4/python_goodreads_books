# -*- coding: utf-8 -*-
# pylint: disable=C0103
"""
Файл с настройками
Автор: Леванов И.

"""
import os
text_path = os.path.abspath(os.path.join(os.getcwd(), '..', 'Data'))
init_path = text_path+'/books.csv'
clean_data_path = text_path+'/clean_data.csv'
download_data = text_path+'/download_data.csv'
save_graph_path =  os.path.abspath(os.path.join(os.getcwd(), '..', 'Graphics'))
gui_width = 1200
gui_height = 700
reload_data_path = text_path+'/reload_data.csv'
table_columns = (
    "title", "authors", "average_rating", 'language_code', 'num_pages', \
    'ratings_count','text_reviews_count', 'publication_date',
    'publisher', 'pub_year', 'century')
