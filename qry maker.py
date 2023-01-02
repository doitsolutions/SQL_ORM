# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 17:41:18 2023

@author: bearjew
"""

qry = {"where":"table_name_col","from_table":"test part func",
       "select": "test=val", "group_by":"go","order_by": "group_by test"}


def sql_builder(sql_dict):
    
    val_dict = {
        "select" : 0,
        "from_table" : 2,
        "into" : 1,
        "where" : 3,
        "group_by":5,
        "order_by":6,
        "delete_from": 0,
        "insert_into" : 0,
        "values": 1,
        "alter_table": 0,
        "add_col": 1,
        "drop_col": 1,
        "rename_col": 1,
        "alter_column": 1,
        "modify_column": 1,
        "limit" : 7,
        "update": 0,
        "set_val": 1,
        "over" : 4
        }
    
    
    key_list = list(sql_dict.keys())
    query= ''

    sql_terms= {
    'select' : 'SELECT %s',
    'over' : 'OVER (PARTITION BY %s) AS %s',
    'from_table' : 'FROM %s',
    'into' : 'INTO %s',
    'where' : 'WHERE %s',
    'group_by' : 'GROUP BY %s',
    'order_by' : 'ORDER BY %s',
    'delete_from' : 'DELETE FROM %s',
    'insert_into' : 'INSERT INTO %s (%s)',
    'values' : 'VALUES (%s)',
    'alter_table' : 'ALTER TABLE %s',
    'add_col' : 'ADD %s %s',
    'drop_col' : 'DROP COLUMN %s;',
    'rename_col' : 'RENAME COLUMN %s to %s;',
    'alter_column' : 'ALTER COLUMN %s %s',
    'modify_column' : 'MODIFY COLUMN %s %s',
    'limit' : 'LIMIT %s',
    'update' : 'UPDATE %s',
    'set_val' : 'SET %s : %s'
    }

    user_query = {}
    for i in key_list:
        if  val_dict.get(i) in list(user_query.values()):
            return(-1)
            
        user_query[i] = val_dict.get(i)
        if user_query[i] == None:
          return(-1)
    sorted_by_val = {k:v for k,v  in sorted(user_query.items(), key= lambda v: v[1])}
    
    for i in sorted_by_val.keys():
        query = query + sql_terms.get(i) + " \n" 
    
    return(query)
        
    
    


    
