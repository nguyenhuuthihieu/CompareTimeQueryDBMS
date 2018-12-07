select_mysql = """
    UPDATE customers SET customerName = 'abc' WHERE customerNumber = 1;
"""

update_mysql = """
    UPDATE customers SET customerName = 'abc' WHERE customerNumber = 1;
"""

select_arangodb = """
    FOR doc IN film FIlTER doc.id <5 RETURN doc
"""