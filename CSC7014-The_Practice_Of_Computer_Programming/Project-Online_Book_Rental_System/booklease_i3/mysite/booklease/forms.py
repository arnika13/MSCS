from django import forms
from .models import BookLeaseUser, Book, BookRequests, BorrowedBook, Reviews
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SigninForm(forms.Form):
	username = forms.CharField(max_length=15,required=True)
	password = forms.CharField(max_length=15,required=True)
	
class MyRegistrationForm(UserCreationForm):
	GENDER_CHOICES=[('M','Male'), ('F','Female')]
	
	email = forms.EmailField()
	firstname = forms.CharField(max_length=30)
	lastname = forms.CharField(max_length=30)
	email = forms.EmailField()
	address = forms.CharField(max_length=50)
	city = forms.CharField(max_length=60)
	state = forms.CharField(max_length=30)
	zipcode = forms.CharField(max_length=15)
	phonenumber = forms.CharField(max_length=30)
	gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
	school = forms.CharField(max_length=30)
	work = forms.CharField(max_length=30)
	description = forms.CharField(max_length=200,widget=forms.Textarea)
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'firstname', 'lastname', 'address', 'city', 'state', 'zipcode', 'phonenumber', 'gender', 'school', 'work', 'description')
		
		def save(self, commit=True):
			user = super(MyRegistrationForm, self).save(commit=False)
			user.email = self.cleaned_data['email']
        
			if commit:
				user.save()

			return user

class BookLeaseUserCreationForm(forms.ModelForm):

	class Meta:
		model = BookLeaseUser
		fields = '__all__'
		
		
class BookForm(forms.ModelForm):
	
	class Meta:
	    
		model = Book
		fields = ('book_name', 'book_author', 'edition', 'isbn', 'price')

class BookFormFull(forms.ModelForm):
	
	class Meta:
		model = Book
		fields = '__all__'
		
class EditProfileForm(forms.ModelForm):
	description = forms.CharField(max_length=200,widget=forms.Textarea)	
	class Meta:
		model = BookLeaseUser
		fields = ('firstname', 'lastname', 'address', 'city', 'state', 'zipcode', 'phonenumber', 'school', 'work', 'description')
		
class EditBookStatusForm(forms.ModelForm):
	BOOK_STATUS=[
		('AV', 'Available'),
		]

	book_status = forms.ChoiceField(choices=BOOK_STATUS)
	start_date = forms.DateTimeField(required=True)
	end_date = forms.DateTimeField(required=True)
	
	class Meta:
		model = Book
		fields = ('book_status',)

class BookRequestsForm(forms.ModelForm):

	class Meta:
		model = BookRequests
		fields = '__all__'

class BorrowedBookForm(forms.ModelForm):

	class Meta:
		model = BorrowedBook
		fields = '__all__'

class ReviewForm(forms.ModelForm):
	
	class Meta:
		model = Reviews
		fields = '__all__'