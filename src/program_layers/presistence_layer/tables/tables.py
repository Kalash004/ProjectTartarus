from src.program_layers.presistence_layer.SimpleSQL.package_src import Base, Param, Types, Constraints, Reference


# TODO: Create a method which will create after init settings for acrus


class admin_users(Base):
    table_name = "admin_users"
    admin_id = Param(Types.INT, Constraints.PK)
    name = Param(Types.STRING, Constraints.NOT_NULL)
    surename = Param(Types.STRING, Constraints.NOT_NULL)
    password = Param(Types.STRING, Constraints.NOT_NULL)


class office_users(Base):
    table_name = "office_users"
    users_id = Param(Types.INT, Constraints.PK)
    name = Param(Types.STRING, Constraints.NOT_NULL)
    surename = Param(Types.STRING, Constraints.NOT_NULL)
    password = Param(Types.STRING, Constraints.NOT_NULL)


class days(Base):
    table_name = "days"
    days_id = Param(Types.INT, Constraints.PK)
    date = Param(Types.DATE, Constraints.NOT_NULL, Constraints.UNIQUE)


class system_messages(Base):
    table_name = "system_messages"
    messages_id = Param(Types.INT, Constraints.PK)
    text = Param(Types.STRING, Constraints.NOT_NULL)
    f_days_id = Param(Types.INT, Constraints.NOT_NULL, references=Reference(days, "days_id"))
    f_admin_id = Param(Types.INT, Constraints.NOT_NULL, references=Reference(admin_users, "admin_id"))


class system_log_ins(Base):
    table_name = "system_log_ins"
    system_log_id = Param(Types.INT, Constraints.PK)
    days_id = Param(Types.INT, Constraints.NOT_NULL, references=Reference(days, "days_id"))
    f_admin_id = Param(Types.INT, references=Reference(admin_users, "admin_id"))
    f_user_id = Param(Types.INT, references=Reference(office_users, "users_id"))


class enterences_to_office(Base):
    table_name = "enterences_to_office"
    enterences_id = Param(Types.INT, Constraints.PK)
    f_user_id = Param(Types.INT, references=Reference(office_users, "users_id"))
    days_id = Param(Types.INT, Constraints.NOT_NULL, references=Reference(days, "days_id"))


class all_tables:
    all_talbes = [admin_users, office_users, days, system_messages, system_log_ins, enterences_to_office]

