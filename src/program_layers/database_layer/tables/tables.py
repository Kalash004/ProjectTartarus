from src.program_layers.database_layer.SimpleSQL.package_src import Base
from src.program_layers.database_layer.SimpleSQL.package_src import Constraints
from src.program_layers.database_layer.SimpleSQL.package_src import Param
from src.program_layers.database_layer.SimpleSQL.package_src import Reference
from src.program_layers.database_layer.SimpleSQL.package_src import Types


class admin_users(Base):
    table_name = "admin_users"
    admin_id = Param(Types.INT, Constraints.PK)
    name = Param(Types.STRING, Constraints.NOT_NULL)
    surename = Param(Types.STRING, Constraints.NOT_NULL)
    password = Param(Types.STRING, Constraints.NOT_NULL)

    def __repr__(self):
        return '{{"table": "{}", "admin_id": {}, "name": "{}", "surename": "{}", "password": "{}"}}'.format(
            self.table_name, self.admin_id, self.name, self.surename, self.password
        )


class office_users(Base):
    table_name = "office_users"
    users_id = Param(Types.INT, Constraints.PK)
    name = Param(Types.STRING, Constraints.NOT_NULL)
    surename = Param(Types.STRING, Constraints.NOT_NULL)
    password = Param(Types.STRING, Constraints.NOT_NULL)

    def __repr__(self):
        return '{{"table": "{}", "users_id": {}, "name": "{}", "surename": "{}", "password": "{}"}}'.format(
            self.table_name, self.users_id, self.name, self.surename, self.password
        )


class days(Base):
    table_name = "days"
    days_id = Param(Types.INT, Constraints.PK)
    date = Param(Types.DATE, Constraints.NOT_NULL, Constraints.UNIQUE)

    def __repr__(self):
        return '{{"table": "{}", "days_id": {}, "date": "{}"}}'.format(
            self.table_name, self.days_id, self.date
        )


class system_messages(Base):
    table_name = "system_messages"
    messages_id = Param(Types.INT, Constraints.PK)
    text = Param(Types.STRING, Constraints.NOT_NULL)
    f_days_id = Param(Types.INT, Constraints.NOT_NULL, references=Reference(days, "days_id"))
    f_admin_id = Param(Types.INT, Constraints.NOT_NULL, references=Reference(admin_users, "admin_id"))

    def __repr__(self):
        return '{{"table": "{}", "messages_id": {}, "text": "{}", "f_days_id": {}, "f_admin_id": {}}}'.format(
            self.table_name, self.messages_id, self.text, self.f_days_id, self.f_admin_id
        )


class system_log_ins(Base):
    table_name = "system_log_ins"
    system_log_id = Param(Types.INT, Constraints.PK)
    days_id = Param(Types.INT, Constraints.NOT_NULL, references=Reference(days, "days_id"))
    f_admin_id = Param(Types.INT, references=Reference(admin_users, "admin_id"))
    f_user_id = Param(Types.INT, references=Reference(office_users, "users_id"))

    def __repr__(self):
        return '{{"table": "{}", "system_log_id": {}, "days_id": {}, "f_admin_id": {}, "f_user_id": {}}}'.format(
            self.table_name, self.system_log_id, self.days_id, self.f_admin_id, self.f_user_id
        )


class enterences_to_office(Base):
    table_name = "enterences_to_office"
    enterences_id = Param(Types.INT, Constraints.PK)
    f_user_id = Param(Types.INT, references=Reference(office_users, "users_id"))
    days_id = Param(Types.INT, Constraints.NOT_NULL, references=Reference(days, "days_id"))

    def __repr__(self):
        return '{{"table": "{}", "enterences_id": {}, "f_user_id": {}, "days_id": {}}}'.format(
            self.table_name, self.enterences_id, self.f_user_id, self.days_id
        )


class all_tables:
    all_talbes = [admin_users, office_users, days, system_messages, system_log_ins, enterences_to_office]
