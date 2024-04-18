from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.__utils.SingletonMeta import SingletonMeta
from src.program_layers.database_layer.RequestToDbObjMapper import RequestToDbObjMapper
from src.program_layers.database_layer.SimpleSQL.package_src import Base
from src.program_layers.database_layer.factory.OrmFactory import OrmFactory
from src.program_layers.database_layer.tables.tables import all_tables


class DbAccess(metaclass=SingletonMeta):
    """This class works with an ORM to interact with the database."""

    def __init__(self, initialize=False):
        """
        Initializes the DbAccess object.

        Args:
        - initialize (bool): If True, initializes the ORM.
        """
        if initialize:
            self.orm = OrmFactory().produce()  # Initializes the ORM
            self.mapper = RequestToDbObjMapper()  # Initializes the mapper
            self.start_orm()  # Starts the ORM

    def start_orm(self):
        """Starts the ORM."""
        for table in all_tables.all_talbes:  # Note: 'all_talbes' should be 'all_tables'
            table(skip_setup=True)  # Initializes each table
        self.orm.start()  # Starts the ORM

    def read_all(self, parsed_request: ParsedRequest):
        """
        Reads all data from the database corresponding to the parsed request.

        Args:
        - parsed_request (ParsedRequest): The parsed request object.

        Returns:
        - list: List of database records.
        """
        obj = self.mapper.get_request_obj_type(parsed_request)  # Gets the database object type
        return self.orm.select_all_from(obj)  # Selects all data from the database

    def select_where(self, parsed_request: ParsedRequest, arg):
        """
        Selects data from the database based on a condition.

        Args:
        - parsed_request (ParsedRequest): The parsed request object.
        - arg: The condition for selection.

        Returns:
        - list: List of database records.
        """
        obj = self.mapper.get_request_obj_type(parsed_request)  # Gets the database object type
        resp = self.orm.select_data_where(obj, arg)  # Selects data based on the condition
        return resp

    def get_last_index(self, parsed_request: ParsedRequest):
        """
        Gets the last inserted index from the database.

        Args:
        - parsed_request (ParsedRequest): The parsed request object.

        Returns:
        - int: The last inserted index.
        """
        obj = self.mapper.get_request_obj_type(parsed_request)  # Gets the database object type
        resp: Base = self.orm.last_inserted_instance(obj)  # Gets the last inserted instance
        if resp is None:
            return -1
        return resp.find_primary_key_val()  # Returns the primary key value of the last inserted instance

    def insert(self, parsed_req):
        """
        Inserts data into the database.

        Args:
        - parsed_req: The parsed request object.

        Returns:
        - bool: True if successful, False otherwise.
        """
        objs: [Base] = self.mapper.request_to_obj(parsed_req)  # Converts parsed request to database objects
        obj: Base
        new_id = -1
        for obj in objs:
            if obj.find_primary_key_val().lower() == "none":
                # Sets primary key value if it's None
                last_id = self.get_last_index(parsed_request=parsed_req)
                if last_id > new_id:
                    new_id = last_id
                new_id += 1
                obj.set_primary_key_val(new_id)
        resp = self.orm.insert_data(objs)  # Inserts data into the database
        return resp

    def delete(self, parsed_request: ParsedRequest, obj_id):
        """
        Deletes data from the database.

        Args:
        - parsed_request (ParsedRequest): The parsed request object.
        - obj_id: The id of the object to delete.

        Returns:
        - bool: True if successful, False otherwise.
        """
        obj = self.mapper.get_request_obj_type(parsed_request)  # Gets the database object type
        resp = self.orm.delete_data_id(obj, obj_id)  # Deletes data from the database
        return resp

    def update(self, parsed_request: ParsedRequest):
        """
        Updates data in the database.

        Args:
        - parsed_request (ParsedRequest): The parsed request object.

        Returns:
        - bool: True if successful, False otherwise.
        """
        obj = self.mapper.request_to_obj(parsed_request)[0]  # Converts parsed request to database object
        resp = self.orm.update_data(obj)  # Updates data in the database
        return resp
