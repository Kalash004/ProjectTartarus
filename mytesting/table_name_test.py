from src.program_layers.database_layer.tables.tables import all_tables

if __name__ == "__main__":
    for t in all_tables.all_talbes:
        print(t.table_name)