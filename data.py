select_mysql = """
    SELECT * FROM film WHERE id = 50000
"""

select_arangodb = """
    FOR fi IN film
    FILTER fi._key == '50000'
    RETURN fi
"""

select2_mysql = """
    SELECT * FROM film WHERE name = 'film50000'
"""

select2_arangodb = """
    FOR fi IN film
    FILTER fi.name == 'film50000'
    RETURN fi
"""

sort_mysql = """
    SELECT * FROM film WHERE id = 50000
"""

sort_arangodb = """
    FOR fi IN film
    FILTER fi._key == '50000'
    RETURN fi
"""

update_mysql = """
    SELECT * FROM film WHERE id = 50000
"""

update_arangodb = """
    FOR fi IN film
    FILTER fi._key == '50000'
    RETURN fi
"""

delete_mysql = """
    SELECT * FROM film WHERE id = 50000
"""

delete_arangodb = """
    FOR fi IN film
    FILTER fi._key == '50000'
    RETURN fi
"""

join_mysql = """
SELECT u.*, f.* FROM user u
JOIN user_film uf ON u.id = uf.user_id
JOIN film f ON f.id = uf.film_id;
"""

join_arangodb = """
FOR u IN user
LET rent = (
FOR fim IN OUTBOUND u user_film
RETURN {
    film: fim
}
)
FILTER rent != []
RETURN {
user: u,
rental: rent
}
"""


