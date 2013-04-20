from django import forms
from django.utils.translation import ugettext_lazy as _

from tasks.models import TaskProposal


class TaskProposalForm(forms.ModelForm):
    class Meta:
        model = TaskProposal

    def __init__(self, *args, **kwargs):
        super(TaskProposalForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = _('You name*')
        self.fields['email'].label = _('You email')
        self.fields['text'].label = _('Task description*')