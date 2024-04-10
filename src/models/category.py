class Category:
    def __init__(self, id, name, parent_category_id=None):
        self.id = id
        self.name = name
        self.parent_category_id = parent_category_id