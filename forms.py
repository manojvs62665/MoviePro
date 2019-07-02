from django import forms

class insertdata(forms.Form):
    movie_id = forms.IntegerField(
        label="Enter movie id",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Movie ID'
            }
        )
    )

    movie_name = forms.CharField(
        label="Enter Movie name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Movie Name'
            }
        )
    )

    movie_cast = forms.CharField(
        label="Enter Movie Cast",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Movie Cast'
            }
        )
    )

    movie_rating = forms.IntegerField(
        label="Enter movie rating",
        widget=forms.NumberInput(
            attrs={
                'class':'form-contol',
                'placeholder':'Movie Rating'
            }
        )
    )

    movie_feedback = forms.CharField(
        label="Enter Movie Feedback",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Movie Feedback'
            }
        )
    )

class updatedata(forms.Form):
    movie_id = forms.IntegerField(
        label="Enter Movie ID",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Id'
            }
        )
    )

    movie_rating = forms.IntegerField(
        label="Enter Movie Rating",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Movie Rating'
            }
        )
    )

class deletedata(forms.Form):
    movie_id = forms.IntegerField(
        label="Enter Movie Id",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Movie Id'
            }
        )
    )