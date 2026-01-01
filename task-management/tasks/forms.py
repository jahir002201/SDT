from django import forms
from tasks.models import Task, TaskDetail
from django.contrib.auth.models import User


class TaskForm(forms.Form):
    title = forms.CharField(max_length=250, label='Task Title')
    description = forms.CharField(widget=forms.Textarea, label='Task Description')
    due_date = forms.DateField(widget=forms.SelectDateWidget, label='Due Date')
    assigned_to = forms.ModelMultipleChoiceField(queryset=User.objects.none(), widget=forms.CheckboxSelectMultiple, label='Assigned To')

    def __init__(self, *args, **kwargs):
        users = kwargs.pop('users', None)
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].choices = [(user.id, user.username) for user in users]


class StyleFormMixin:
    default_classes = "border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            widget = field.widget

            if isinstance(widget, forms.TextInput):
                widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f'Enter {field.label.lower()}'
                })
            elif isinstance(widget, forms.Textarea):
                widget.attrs.update({
                    'class': f'{self.default_classes} resize-none',
                    'placeholder': f'Enter {field.label.lower()}',
                    'rows': 5
                })
            elif isinstance(widget, forms.SelectDateWidget):
                widget.attrs.update({'class': self.default_classes})
            elif isinstance(widget, forms.CheckboxSelectMultiple):
                widget.attrs.update({'class': "space-y-2"})
            else:
                widget.attrs.update({'class': self.default_classes})


class TaskModelForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'assigned_to']
        widgets = {
            'due_date': forms.SelectDateWidget(),
            'assigned_to': forms.CheckboxSelectMultiple()
        }


class TaskDetailModelForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = TaskDetail
        fields = ['priority', 'notes', 'asset']