React example in Python, using views

'''
	REACT_ROUTES = [
	    'login',
	    'signup',
	    'password-reset',
	    'password-change',
	    'about',
	    ...
	]

	# urls.py
	from django.conf import settings

	react_routes = getattr(settings, 'REACT_ROUTES', [])

	for route in react_routes:
	    urlpatterns += [
	        path('{}'.format(route), TemplateView.as_view(template_name='index.html'))
	    ]
'''