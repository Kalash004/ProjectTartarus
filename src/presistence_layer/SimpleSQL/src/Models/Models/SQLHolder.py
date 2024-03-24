class SimpleSQLHolder:
    def __init__(self, table_name, table_builder_DDL, references, insert, select, update, delete):
        self.table_name = table_name
        self.table_builder_DDL = table_builder_DDL
        self.references = references
        self.insert = insert
        self.select = select
        self.update = update
        self.delete = delete
