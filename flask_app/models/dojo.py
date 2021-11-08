from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja


class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        #empty list to be filled by ninjas

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        print("This is the data inside of the results from running the get all query: ", results)
        dojos = []
        #row is a dictionary
        for row in results:
            dojos.append(Dojo(row))
        return dojos

    # @classmethod
    # def get_one(cls, data):
    #     query = "SELECT * FROM dojos WHERE id = %(id)s;"
    #     results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    #     if len(results) == 0:
    #         return False
    #     return Dojo(results[0])

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id  WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        if len(results) ==0:
            return False

        dojo = Dojo(results[0])
        #dojo key containing dojo object
        print(results[0])
        for row_from_db in results:
            ninja_data = {
                "id" :          row_from_db["ninjas.id"],
                "dojo_id" :     row_from_db["dojo_id"],
                "first_name" :  row_from_db["first_name"],
                "last_name" :   row_from_db["last_name"],
                "age" :         row_from_db["age"],
                "created_at" :  row_from_db["ninjas.created_at"],
                "updated_at" :  row_from_db["ninjas.updated_at"]
            }
            print(ninja_data)
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo

    # @classmethod
    # def edit(cls, data):
    #     query = "UPDATE dojos SET name = %(name)s, updated_at = NOW() WHERE id = %(id)s;"
    #     return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    # @classmethod
    # def delete(cls,data):
    #     query = "DELETE FROM dojos WHERE id = %(id)s;"
    #     connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )