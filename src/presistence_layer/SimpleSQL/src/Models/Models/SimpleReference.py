from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ... import Base


class SimpleReference:
    def __init__(self, ref_to_table: type[Base], attribute: str):
        self.table_struct = ref_to_table
        self.table_name: str = ref_to_table.table_name
        self.attribute_name: str = attribute
        if attribute not in ref_to_table.__dict__:
            raise Exception(
                f"Error at initiating SimpleReference for {self.table_name}.{attribute} : This atribute does not exist in the referenced table")
