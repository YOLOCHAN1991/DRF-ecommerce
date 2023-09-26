from django.db import models
from django.core import checks
from django. core.exceptions import ObjectDoesNotExist


class OrderField(models.PositiveIntegerField):
    description = "Order field for sorting"

    def __init__(self, unique_for_field=None, *args, **kwargs):
        self.unique_for_field = unique_for_field
        super().__init__(*args, **kwargs)

    def check(self, **kwargs):
        return [*super().check(**kwargs), *self.check_for_field_attribute(**kwargs)]

    def check_for_field_attribute(self, **kwargs):
        if self.unique_for_field is None:
            return [
                checks.Error(
                    "OrderField must have a unique_for_field attribute.",
                    obj=self,
                    id="fields.E121",
                )
            ]
        elif self.unique_for_field not in [
            field.name for field in self.model._meta.fields
        ]:
            return [
                checks.Error(
                    f"OrderField has invalid unique_for_field attribute: {self.unique_for_field}",
                    obj=self,
                    id="fields.E122",
                )
            ]

        return []

    def pre_save(self, model_instance, add):
        
        if getattr(model_instance, self.attname) is None:
            qs = self.model.objects.all()
            try:
                qs = qs.filter(
                    **{
                        self.unique_for_field: getattr(
                            model_instance, self.unique_for_field
                        )
                    }
                ).exclude(pk=model_instance.pk)
                last_item = qs.latest(self.attname)
                print(last_item)
                value = last_item.order + 1
            except ObjectDoesNotExist:
                value = 1
            return value
        else:
            return super().pre_save(model_instance, add)
