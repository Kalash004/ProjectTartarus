from ... import Constraints, Types


class SimpleParam:

    def __init__(self, datatype: Types, *constraints: [Constraints], **other):
        self.datatype: Types = datatype
        self.constraints: [Constraints] = constraints
        try:
            self.references = other["references"]
            if not isinstance(self.references, type([])):
                self.references = [self.references]
        except Exception:
            # TODO: find exception that gets cought if other["references"] doesnt exist
            self.references = None
