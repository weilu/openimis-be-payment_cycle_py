from core.services import BaseService
from core.signals import register_service_signal
from payment_cycle.models import PaymentCycle
from payment_cycle.validations import PaymentCycleValidation
from tasks_management.services import UpdateCheckerLogicServiceMixin, CreateCheckerLogicServiceMixin


class PaymentCycleService(BaseService, UpdateCheckerLogicServiceMixin, CreateCheckerLogicServiceMixin):
    OBJECT_TYPE = PaymentCycle

    def __init__(self, user, validation_class=PaymentCycleValidation):
        super().__init__(user, validation_class)

    @register_service_signal('payment_cycle_service.create')
    def create(self, obj_data):
        return super().create(obj_data)

    @register_service_signal('payment_cycle_service.update')
    def update(self, obj_data):
        return super().update(obj_data)

    @register_service_signal('payment_cycle_service.delete')
    def delete(self, obj_data):
        return super().delete(obj_data)
