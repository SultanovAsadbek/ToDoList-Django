from django import forms
from ToDoApp.models import ToDoList
from django.utils.translation import gettext_lazy as _


class SelectStatus(forms.Form):
    """_summary_

    Args:
        forms (_type_): _description_
    """

    status = forms.ChoiceField(
        choices=(
            ("", _("Статус задачи")),
            ("not_started", _("Не завершено")),
            ("in_progress", _("В процессе")),
            ("completed", _("Завершено")),
        ),
        widget=forms.Select(attrs={"class": "selectST"}),
    )
