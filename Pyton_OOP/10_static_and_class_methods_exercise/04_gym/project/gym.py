from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    def add_customer(self, customer: Customer) -> None:
        self.__add_object(self.customers, customer)

    def add_trainer(self, trainer: Trainer) -> None:
        self.__add_object(self.trainers, trainer)

    def add_equipment(self, equipment: Equipment) -> None:
        self.__add_object(self.equipment, equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        self.__add_object(self.plans, plan)

    def add_subscription(self, subscription: Subscription) -> None:
        self.__add_object(self.subscriptions, subscription)

    def subscription_info(self, subscription_id: int) -> str | None:
        subscription = self.__search_by_id(self.subscriptions, subscription_id)

        if subscription is None:
            return None

        customer = self.__search_by_id(self.customers, subscription.customer_id)
        trainer = self.__search_by_id(self.trainers, subscription.trainer_id)
        plan = self.__search_by_id(self.plans, subscription.exercise_id)

        if plan is None:
            return None

        equipment = self.__search_by_id(self.equipment, plan.equipment_id)
        if subscription and customer and trainer and plan and equipment:
            return '\n'.join([repr(subscription), repr(customer), repr(trainer),
                              repr(equipment), repr(plan)])
        return None

    @staticmethod
    def __add_object(objects: list, some_object) -> None:
        if some_object not in objects:
            objects.append(some_object)

    @staticmethod
    def __search_by_id(objects, object_id, attribute="id"):
        return next((o for o in objects if getattr(o, attribute, None) == object_id), None)
