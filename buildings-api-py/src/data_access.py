
def db_buildings_all(cursor):
    """ Gets all buildings from the database
    """
    return cursor.execute("SELECT id, name, height, city, country FROM buildings")

def db_buildings_get(cursor, building_id):
    """ Gets a specific building from the database
    """
    return cursor.execute("SELECT id, name, height, city, country FROM buildings WHERE id = {}".format(building_id))
