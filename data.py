select_mysql = """
    SELECT film_id FROM film1 WHERE film_id = 500
"""

select_arangodb = """
    RETURN DOCUMENT('film/50000')
"""

update_mysql = """
    UPDATE film1 SET title = 'phim gi ay' WHERE film_id = 10;
"""

update_arangodb = """
    FOR doc IN film FIlTER doc.id <5 RETURN doc
"""

