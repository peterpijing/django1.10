#coding=utf-8
from django import forms

TOPIC_CHOICES = (
    ('general','General enquiry'),
    ('bug','Bug report'),
    ('suggestion','Suggestion'),

)

class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    #widget可是输入多行
    message = forms.CharField(widget=forms.Textarea())
    sender = forms.EmailField(required=False)

    #2.校验用户输入的字段
    def clean_message(self):
        message = self.cleaned_data.get('message','')
        num_words = len(message.split())

        if num_words < 4:
            raise forms.ValidationError("not enough words")
        return message
