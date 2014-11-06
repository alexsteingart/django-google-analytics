from distutils.core import setup

setup(name='google_analytics',
      version='0.2',
      description='A Django application to integrate Google Analytics into your projects plus some analytics on collected data',
      author='Alex Steingart',
      author_email='alexsteingart@gmail.com',
      url='http://github.com/alexsteingart/django-google-analytics/tree/master',
      packages=['google_analytics','google_analytics.templatetags','google_analytics.migrations'],
      package_data={'google_analytics': ['templates/google_analytics/*.html']},
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
