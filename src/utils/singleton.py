class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
            instance.__init__(*args, **kwargs)  # Initialize it here
        return cls._instances[cls]
