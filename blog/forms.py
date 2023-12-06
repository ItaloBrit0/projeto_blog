from django import forms

class ComentarioForm(forms.Form):
    autor = forms.CharField(
        max_length= 80,
        widget=forms.TextInput(
            attrs = {'class': 'form-control', 'placeholder': 'Seu nome'}
        ),
    )

    corpo = forms.CharField(

        widget= forms.Textarea(
            attrs= {'class': 'form-control', 'placeholder': 'Deixe um comentário!'},
                        
        )
    )

