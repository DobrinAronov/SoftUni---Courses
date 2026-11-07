class IDMixin:
    id: int = 1

    @classmethod
    def get_next_id(cls):
        return cls.id

    @classmethod
    def increase_id(cls) -> None:
        cls.id += 1
