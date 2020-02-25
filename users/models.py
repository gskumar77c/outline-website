from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,AbstractUser



class UserManager(BaseUserManager):
	def create_user(self, email, password=None):
		"""
		Creates and saves a User with the given email and password.
		"""
		if not email:
			raise ValueError('Users must have an email address')
		

		user = self.model(
			email=self.normalize_email(email),
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_staffuser(self, email, password):
		"""
		Creates and saves a staff user with the given email and password.
		"""
		user = self.create_user(
			email,
			password=password,
		)
		user.staff = True
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		"""
		Creates and saves a superuser with the given email and password.
		"""
		user = self.create_user(
			email,
			password=password,
		)
		user.staff = True
		user.admin = True
		user.save(using=self._db)
		return user


class User(AbstractBaseUser):
	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True,
	)
	active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False) # a admin user; non super-user
	admin = models.BooleanField(default=False) # a superuser
	# notice the absence of a "Password field", that is built in.
	is_student = models.BooleanField(default=False)
	is_faculty = models.BooleanField(default=False)
	is_gsadmin  = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = [] # Email & Password are required by default.

	objects = UserManager()

	def get_full_name(self):
		# The user is identified by their email address
		return self.email

	def get_short_name(self):
		# The user is identified by their email address
		return self.email

	def __str__(self):              # __unicode__ on Python 2
		return self.email

	def has_perm(self, perm, obj=None):
		#"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		if self.is_active :
			return True
		else :
			return False

	def has_module_perms(self, app_label):
		#"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		#"Is the user a member of staff?"
		return self.staff

	@property
	def is_admin(self):
		#"Is the user a admin member?"
		return self.admin

	@property
	def is_active(self):
		#"Is the user active?"
		return self.active



class student(models.Model):
	user  = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)


class faculty(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)


class gsadmin(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)




'''

class UserManager(BaseUserManager):

	def create_user(self,email,fullname,password=None):
		if not email :
			raise ValueError('email is necessary')
		elif not password:
			raise ValueError('password is necessary')
		user = self.model(
			email = self.normalize_email(email),
			fullname = fullname
			)
		user.set_password(password)
		user.save(using = self._db)
		return user


	def create_student(self,email,fullname,password=None):
		user = self.create_user(email,password=password,fullname=fullname)
		user.student = True
		user.save(using=self._db)
		return user

	def create_staff(self,email,fullname,password=None):
		user = self.create_user(email,password=password,fullname=fullname)
		user.student=False
		user.staff = True
		user.save(using = self._db)
		return user

	def create_faculty(self,email,fullname,password=None):
		user = self.create_user(email,password=password,fullname=fullname)
		user.student = False
		user.faculty = True
		user.save(using=self._db)
		return user

	def create_superuser(self,email,fullname,password=None):
		user = self.create_user(email,password=password,fullname=fullname)
		user.student = False
		user.admin = True
		user.save(using=self._db)
		return user

	def create_crossfaculty(self,email,fullname,password=None):
		user = self.create_user(email,password=password,fullname=fullname)
		user.student = False
		user.crossfaculty = True
		user.save(using=self._db)
		return user


class User(AbstractBaseUser):
	email = models.EmailField(verbose_name = 'email address', max_length=255,unique = True)

	is_student = models.BooleanField(default=True)
	is_faculty = models.BooleanField(default=False)
	is_crossfaculty = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_admin   = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_fullname = models.CharField(max_length=200)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['fullname']

	objects = UserManager()

	def get_fullname(self):
		return self.fullname

	def __str__(self):
		return self.email

	def has_perm(self,perm,obj=None):

		return True

	def has_module_perms(self,app_label):

		return True

	@property
	def is_faculty(self):
		return self.is_faculty
	
	@property
	def is_staff(self):
		return self.is_staff

	@property
	def is_crossfaculty(self):
		return self.is_crossfaculty

	@property
	def is_admin(self):
		return self.admin

	@property
	def is_student(self):
		return self.student

	@property
	def is_active(self):
		return self.active
'''