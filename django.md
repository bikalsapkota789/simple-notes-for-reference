# Basic working structures

## start a new project
```
django-admin.py startproject <project-name>
```
(This command must be written within your project directory)

## start a project in virtual environment
```
 virtualenv projectname-env
 projectname-env/bin/activate
```

## start a new app 
```
python manage.py startapp <app-name>
```
(put your <app-name> in INSTALLED_APPS list within <project-name>/settings.py file)

## create superuser(i.e. admin)
```
python manage.py createsuperuser
```

## run server
```
python manage.py runserver
```

## migrations 
```
python manage.py migrate
python manage.py makemigrations
```
(do everytime after updating models.py from within your <project-name> directory)







# |browser| --> |server| --> |urls.py| --> |views.py| --> |templates.html|

![django-workflow](C:\Users\Dell\Desktop\django-workflow1.png "workflow")

##  Changing in views 
go to <your-app>/views.py and make changes
```
def function(request):				# def blog_list(request)
	name-to-display = name-wherer-it-lies.object.all()		# post = Post.objects.all()
	context = {
	'function':name-to-display			# 'blog_list': post
	}
	return render(request, "<app-name>/function.html",context)		#
```


## now make a new urls.py within <your-project>/<your-app>/ directory and make changes as below
```
from django .urls import path 
from .views import function		# from .views import blog_list

urlpatterns = [
	path('',functions)			# path ('',blog_list)
]

```
now make changes to $<your-project>$/urls.py and import  include and make a change to 'urlpatterns'. Then add the path to your app URLs through include. Also, when users route through 'posts/' then, it gets directed to our 'blog.urls(ie. blog/urls.py).'

## templates 
lets make a templates named folder to hold your 'HTML' and contains their own templating language called '**Jinja2**'. the folder need to name '<your-project>/<your-app>/<functions-of-views>.html' (i.e. templates/blog/blog_list.html) which is a convention


