from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category) -> None:
        self.__add_object(category, self.categories)

    def add_topic(self, topic: Topic) -> None:
        self.__add_object(topic, self.topics)

    def add_document(self, document: Document) -> None:
        self.__add_object(document, self.documents)

    def edit_category(self, category_id: int, new_name: str) -> None:
        self.__edit_object(self.categories, category_id, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        self.__edit_object(self.topics, topic_id, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        self.__edit_object(self.documents, document_id, new_file_name)

    def delete_category(self, category_id: int) -> None:
        self.__delite_object(self.categories, category_id)

    def delete_topic(self, topic_id: int) -> None:
        self.__delite_object(self.topics, topic_id)

    def delete_document(self, document_id: int) -> None:
        self.__delite_object(self.documents, document_id)

    def get_document(self, document_id: int) -> Document | Category | Topic | None:
        return self.__find_instance(self.documents, document_id)

    def __repr__(self) -> str:
        return '\n'.join(repr(d) for d in self.documents)

    @staticmethod
    def __add_object(some_object, objects) -> None:
        if some_object not in objects:
            objects.append(some_object)

    @staticmethod
    def __find_instance(instances, search_id) -> Category | Topic | Document | None:
        return next((i for i in instances if i.id == search_id), None)

    def __edit_object(self, objects, object_id, *new_value):
        found_object = self.__find_instance(objects, object_id)
        if found_object:
            found_object.edit(*new_value)

    def __delite_object(self, objects, object_id) -> None:
        curr_object = self.__find_instance(objects, object_id)
        if object:
            objects.remove(curr_object)
