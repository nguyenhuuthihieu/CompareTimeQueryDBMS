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
SELECT * FROM user
ORDER BY name LIMIT 5;
"""

sort_arangodb = """
FOR user IN user
    SORT user.name
LIMIT 0, 5
RETURN user
"""

update_mysql = """
UPDATE user
SET name = "John Smith"
WHERE id = 1;
"""

update_arangodb = """
UPDATE { _key: "1" }
WITH { name: "John Smith" }
IN user
"""

delete_mysql = """
DELETE FROM user
    WHERE id = 1;
"""

delete_arangodb = """
REMOVE { _key:"1" }
    IN user
"""

join_mysql = """
SELECT u.*, f.* FROM user u
JOIN user_film uf ON u.id = uf.user_id
JOIN film f ON f.id = uf.film_id
WHERE u.id = 500000;
"""

join_arangodb = """
FOR u IN user
LET rent = (
FOR fim IN OUTBOUND u user_film
RETURN {
    film: fim
}
)
FILTER rent != [] AND u._key == '500000'
RETURN {
user: u,
rental: rent
}
"""


