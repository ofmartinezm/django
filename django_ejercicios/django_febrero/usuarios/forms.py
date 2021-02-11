from django import forms 
from .models import Usuario


class UserForm(forms.Form):
    GENEROS= [('H','Hombre'),('F','Mujer'),('O','Otros')]
    username= forms.CharField(label='Nombre de Usuario',max_length=100)
    email= forms.EmailField(label='Correo de Usuario', max_length=50)
    genero= forms.ChoiceField(label='Genero', choices=GENEROS)

    passw = forms.CharField(label='ContraleÃ±a', max_length=20, 
            widget=forms.PasswordInput)
    comentarios =  forms.CharField(label='Comentarios', max_length=400,
            widget=forms.Textarea)
    gender2 = forms.MultipleChoiceField(label='Genero', choices=GENEROS,
        widget=forms.CheckboxSelectMultiple) 
    gender3 = forms.ChoiceField(label='Genero', choices=GENEROS,
        widget=forms.RadioSelect)



class UserFornM(forms.ModelForm):
    class Meta:
        model =  Usuario
        fields =['username', 'mail', 'gender']
        labels = { 'username':'Nombre Usuario ', 'mail': 'Correo', 'gender': 'Genero'}