from django.contrib.postgres.search import SearchVector
from django.shortcuts import render_to_response
from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import BookLeaseUser, Book, BookRequests, BorrowedBook, Reviews
from django.contrib.auth.forms import UserCreationForm
from booklease.forms import SigninForm, MyRegistrationForm, BookLeaseUserCreationForm, BorrowedBookForm, ReviewForm
from booklease.forms import BookForm, BookFormFull, EditProfileForm, EditBookStatusForm, BookRequestsForm
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
import datetime

# Create your views here.
def index(request):
	return render_to_response('booklease/index.html')

def signin(request):
	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		
		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('dashboard')
		else:
			return HttpResponseRedirect('invalid')
			#render(request, 'booklease/signin.html', {'form':user})
	else:
		form = SigninForm()
		return render(request, 'booklease/signin.html', {'form':form})

def register_success(request):
    return render(request, 'booklease/register_success.html')

def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		booklease_user_form = BookLeaseUserCreationForm(request.POST)

		if form.is_valid() and booklease_user_form.is_valid():
			form.save()
			booklease_user_form.save()
			return HttpResponseRedirect('register_success')
	
	else:
		form = MyRegistrationForm()
	
	args = {}
	args['form'] = form
	return render(request, 'booklease/register.html', args)

def dashboard(request):
	if request.user.is_authenticated() == False:
		form = SigninForm()
		return render(request, 'booklease/signin.html', {'form':form})
	
	args = {}
	if request.method == 'POST':
		requestType = request.POST.get('request_type')
		request_id = request.POST.get('booktorent','')
		end_date = request.POST.get('end_date','')
		if request_id != None:
			requestrec = BookRequests.objects.get(id=request_id)
			if requestType == 'accept':
				# Add a new record in table 'BorrowedBook' 
				# and change book status to 'Rented'
				bookrec = Book.objects.get(id=requestrec.book_id.pk)
				borrowedBookData = {'borrowed_book_owner': bookrec.book_owner.pk,
				'borrowed_book_id': bookrec.id,
				'book_borrowed_by': requestrec.borrower_username.pk,
				'start_date':datetime.datetime.now(),
				'end_date':datetime.datetime.strptime(end_date, "%m/%d/%Y")}
				borrowedbook = BorrowedBookForm(borrowedBookData)
				if borrowedbook.is_valid():
					borrowedbook.save()
					args['message'] = 'The book has been rented.'
				else:
					args['message'] = 'Error during updating borrowed book. '
					
				# Change Book Status to 'Rented'
				Book.objects.filter(id=bookrec.id).update(book_status='RE')
			else:
				args['message'] = 'Request declined'
				
			# Delete the request from the table 'BookRequests'
			BookRequests.objects.filter(id=request_id).delete()
			
	recs = BookRequests.objects.filter(bookowner_username=request.user.username)
	args['requests'] = recs
	return render(request, 'booklease/dashboard.html', args)

def invalid_login(request):
    return render(request, 'booklease/invalid_login.html')

def profile(request, profile_username=''):
	if request.user.is_authenticated() == False:
		form = SigninForm()
		return render(request, 'booklease/signin.html', {'form':form})
	
	args = {}
	if(profile_username != ''):
		# Validate the username found in the URL
		userrec = BookLeaseUser.objects.get(username=profile_username)
		if(userrec == None):
			# ERROR - The username does not exist
			args['errormessage'] = 'The username ' + profile_username + 'does not exist'
			profile_username = request.user.username
	else:
		profile_username = request.user.username
	
	if profile_username == request.user.username:
		args['logged_in_profile'] = True
	else:
		args['logged_in_profile'] = False
	
	userrec = BookLeaseUser.objects.get(username=profile_username)
	reviews = Reviews.objects.filter(review_for=profile_username)
	args['userprofile'] = userrec
	args['reviews'] = reviews
	return render(request, 'booklease/profile.html', args)
	
def booksowned(request):
	if request.user.is_authenticated() == False:
		form = SigninForm()
		return render(request, 'booklease/signin.html', {'form':form})
	
	if request.method == 'POST':
		booksToBeDeleted = request.POST.getlist('id')
		if len(booksToBeDeleted) > 0:
			for i in booksToBeDeleted:
				Book.objects.filter(id=i).delete()
	
	args = {}
	recs = Book.objects.filter(book_owner=request.user.username)
	args['booklist'] = recs
	return render(request, 'booklease/booksowned.html', args)
	
def rentedbooks(request):
	if request.user.is_authenticated() == False:
		form = SigninForm()
		return render(request, 'booklease/signin.html', {'form':form})

	currentBorrowedBooks = BorrowedBook.objects.filter(book_borrowed_by=request.user.username, returned=False)
	pastBorrowedBooks = BorrowedBook.objects.filter(book_borrowed_by=request.user.username, returned=True)
	args = {}
	args['books'] = currentBorrowedBooks
	args['pastbooks'] = pastBorrowedBooks
	return render(request, 'booklease/rentedbooks.html', args)
	
def addbook(request):
	username = None
	if request.user.is_authenticated() == False:
		form = SigninForm()
		return render(request, 'booklease/signin.html', {'form':form})
		
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			form_dict = form.cleaned_data
			form_dict['book_owner'] = request.user.username
			book_full_form = BookFormFull(form_dict)
			if(book_full_form.is_valid() == False):
				form.errors = book_full_form
			else:
				book_full_form.save(commit=True)
				return HttpResponseRedirect('addbook')
	
	else:
		form = BookForm()

	args = {}
	args['form'] = form
	return render(request, 'booklease/addbook.html', args)
	
def searchbook(request):
	if request.user.is_authenticated() == False:
		form = SigninForm()
		return render(request, 'booklease/signin.html', {'form':form})

	if request.method == 'POST':
		searchString = request.POST.get('searchString', '')
		#recs = Book.objects.annotate(search=SearchVector('book_name')).filter(search=searchString)
		#assert False, recs
		recs = Book.objects.filter(book_name__icontains=searchString).exclude(book_owner=request.user.username)
		args = {}
		args['books'] = recs
		return render(request, 'booklease/searchbook.html', args)
	
	return render(request, 'booklease/searchbook.html')

	
def editprofile(request):
	if request.user.is_authenticated() == False:
		form = SigninForm()
		return render(request, 'booklease/signin.html', {'form':form})
    
	if request.method == 'POST':
		instance = get_object_or_404(BookLeaseUser, username=request.user.username)
		form = EditProfileForm(request.POST, instance=instance)
		if form.is_valid():
			form.save()
			userrec = BookLeaseUser.objects.get(username=request.user.username)
			args = {}
			args['userprofile'] = userrec
			return render(request, 'booklease/profile.html', args)
	else:
		form = EditProfileForm

	args = {}
	args['form'] = form
	return render(request, 'booklease/editprofile.html', args)

def bookdetails(request,book_id):
	if request.user.is_authenticated() == False:
		form = SigninForm()
		return render(request, 'booklease/signin.html', {'form':form})
    
	ownername = ''

	recs = Book.objects.get(id=book_id)
	args = {}
	
	if request.method == 'POST' and 'requesttorent' in request.POST:
		# First check if the book has already been requested
		rec = BookRequests.objects.filter(borrower_username=request.user.username).filter(book_id=book_id)
		if len(rec) == 0:
			# Now send the email to the book owner
			userrec = BookLeaseUser.objects.get(username=request.user.username)
			emailBody = 'The user ' + request.user.username + ' has requested you to borrow the book, ' + recs.book_name + '.'
			emailBody = emailBody + '. Please contact the user at ' + userrec.phonenumber + '.'
			emailBody = emailBody + ' Please change the status of the book accordingly. '
			emailSubject = 'From: BookLease - Request to borrow book, ' + recs.book_name
			rec = BookLeaseUser.objects.get(username=recs.book_owner.pk)
			email = EmailMessage(emailSubject, emailBody, to=[rec.email])
			email.send()
			args['ownername'] = rec.firstname
			bookRequestData = {'borrower_username': request.user.username, 
			'book_id': book_id,
			'bookowner_username': rec.username}
			bookRequestForm = BookRequestsForm(bookRequestData)
			if bookRequestForm.is_valid():
				bookRequestForm.save()
		else:
			args['emailalreadysent'] = True
	
	if request.method == 'POST' and 'modifystatus' in request.POST:
		#return HttpResponseRedirect('/booklease/modifystatus/' + str(book_id))
		# 1. Modify the status of the book to 'Available' and
		# 2. Remove from the 'BorrowedBook' Table
		Book.objects.filter(id=book_id).update(book_status='AV')
		BorrowedBook.objects.filter(borrowed_book_id=book_id).update(returned=True)
		recs = Book.objects.get(id=book_id)
		
	pastBorrowedBooks = BorrowedBook.objects.filter(borrowed_book_id=book_id, borrowed_book_owner=request.user.username, returned=True)
	args['book'] = recs
	args['owner'] = False
	args['pastbooks'] = pastBorrowedBooks
	if(recs.book_owner.pk == request.user.username):
		args['owner'] = True
		
	if(recs.book_status == 'RE'):
		borrowed_book = BorrowedBook.objects.get(borrowed_book_id=book_id)
		args['borrowedbook'] = borrowed_book

	return render(request, 'booklease/bookdetails.html', args)

def modifystatus(request, book_id):
	if request.user.is_authenticated() == False:
		form = SigninForm()
		return render(request, 'booklease/signin.html', {'form':form})

	if request.method == 'POST':
		instance = get_object_or_404(Book, id=book_id)
		form = EditBookStatusForm(request.POST, instance=instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/booklease/bookdetails/' + str(book_id))
	else:
		form = EditBookStatusForm

	args = {}
	args['form'] = form
	return render(request, 'booklease/modifystatus.html', args)

def reviews(request, borrowed_book_transaction_id=0):
	if request.user.is_authenticated() == False:
		form = SigninForm()
		return render(request, 'booklease/signin.html', {'form':form})
	
	args = {}
	BorrowedBookTransactionRecord = BorrowedBook.objects.get(id=borrowed_book_transaction_id, returned=True)
	review_by = request.user.username
	if(request.user.username == BorrowedBookTransactionRecord.borrowed_book_owner.username):
		review_for = BorrowedBookTransactionRecord.book_borrowed_by.pk
	else:
		review_for = BorrowedBookTransactionRecord.borrowed_book_owner.pk
	
	args['review_for'] = review_for
	args['review_by'] = review_by
	if request.method == 'POST':
		reviewText = request.POST.get('reviewText', '')
		ReviewRecord = {'borrowed_book_transaction_id':borrowed_book_transaction_id,
		'review_by':review_by, 'review_for':review_for, 'review':reviewText}
		reviewform = ReviewForm(ReviewRecord)
		if reviewform.is_valid():
			reviewform.save()
		else:
			print(reviewform.errors)
		
	written_review = Reviews.objects.filter(borrowed_book_transaction_id=borrowed_book_transaction_id, review_by=request.user.username)
	received_review = Reviews.objects.filter(borrowed_book_transaction_id=borrowed_book_transaction_id, review_for=request.user.username)
	args['book'] = BorrowedBookTransactionRecord
	if(len(written_review) > 0):
		print('written_review id = ' + str(written_review[0].id))
		args['written_review'] = written_review[0].review

	
	if(len(received_review) > 0):
		print('received_review id = ' + str(received_review[0].id))
		args['received_review'] = received_review[0].review
	
	return render(request, 'booklease/review.html', args)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('signin')

