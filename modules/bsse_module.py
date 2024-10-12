# base_module.py

class BaseContentProvider:
    def get_content(self):
        raise NotImplementedError("Subclasses must implement get_content method")