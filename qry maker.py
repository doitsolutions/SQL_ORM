# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 17:41:18 2023

@author: bearjew
"""

from psycopg2 import sql
 

example_sql_values = {
    'select' : 'col_name as alias, col_2',
    'from_table' : 'table_name',
    'into' : 'table_name',
    'where' : "col_name LIKE '%soft%'",
    'group_by' : 'col_name,col_2',
    'order_by' : 'col_name,col_2',
    'delete_from' : 'table_name',
    'insert_into' :  'table_name  (col_name,col_2)',
    'values' : "'test_val_1','test_val_2'",
    'alter_table' : 'table_name',
    'add_col' : 'col_name varchar(255)',
    'drop_col' : 'col_name',
    'rename_col' : ' col_nme to new_name;',
    'alter_column' : 'col_name varchar(100)',
    'modify_column' : 'col_name varchar(100)',
    'limit' : '5',
    'update' : 'table_name',
    'set_val' : "col_name = 'test_val', col_2 = 'test_val_2'" 
    }



qry = {
       'alter_table' : 'table_name',
       'drop_col' : 'col_name',
       }


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
        }
    
    
    key_list = list(sql_dict.keys())
    query= ''

    sql_terms= {
    'select' : 'SELECT {select}',   #dont validate
    'from_table' : 'FROM {from_tbale}', #str
    'into' : 'INTO {into}',  #list
    'where' : 'WHERE {where}', #dont validate
    'group_by' : 'GROUP BY {group_by}', #list
    'order_by' : 'ORDER BY {order_by}', #list
    'delete_from' : 'DELETE FROM {delete_from}', #str
    'insert_into' : 'INSERT INTO {insert_into}', #str
    'values' : 'VALUES ({values})', #list
    'alter_table' : 'ALTER TABLE {alter_table}', #str
    'add_col' : 'ADD {add_col}', #list
    'drop_col' : 'DROP COLUMN {drop_col}', #list
    'rename_col' : 'RENAME COLUMN {rename_col}', #tuple
    'alter_column' : 'ALTER COLUMN {alter_column}', #tuple
    'modify_column' : 'MODIFY COLUMN {modify_column}', #tuple
    'limit' : 'LIMIT {limit}', #int
    'update' : 'UPDATE {update}', #str
    'set_val' : 'SET {set_val} ' #tuple
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
    
    query = sql.SQL(query).format(
        select=sql.Literal(sql_dict.get("select")),
        from_table=sql.Literal(sql_dict.get("from_table")),
        into=sql.Literal(sql_dict.get("into")),
        where=sql.Literal(sql_dict.get("where")),
        group_by=sql.Literal(sql_dict.get("group_by")),
        order_by=sql.Literal(sql_dict.get("order_by")),
        delete_from=sql.Literal(sql_dict.get("delete_from")),
        insert_into=sql.Literal(sql_dict.get("insert_into")),
        values=sql.Literal(sql_dict.get("values")),
        alter_table=sql.Literal(sql_dict.get("alter_table")),
        add_col=sql.Literal(sql_dict.get("add_col")),
        drop_col=sql.Literal(sql_dict.get("drop_col")),
        rename_col=sql.Literal(sql_dict.get("rename_col")),
        alter_column=sql.Literal(sql_dict.get("alter_column")),
        modify_column=sql.Literal(sql_dict.get("modify_column")),
        limit=sql.Literal(sql_dict.get("limit")),
        update=sql.Literal(sql_dict.get("update")),
        set_val=sql.Literal(sql_dict.get("set_val"))
        )
    
        
    return(query)
    
    
test=sql_builder(qry)
print(test)    
        
    


