import io
from distutils.core import setup
from setuptools import find_packages

#readme = io.open('README.rst', encoding='utf-8')
#readme_text = readme.read()
#readme.close()

#version = __import__('bootstrap_pagination').__version__
version = '1.0'

setup(
    name='django-bootstrap-pagination',
    version=version,
    keywords="django bootstrap pagination templatetag",
    author='Jason McClellan',
    author_email='jason@jasonmccllelan.net',
    packages=find_packages(),
    url='https://github.com/jmcclell/django-bootstrap-pagination',
    license='MIT licence, see LICENCE',
    description='Render Django Page objects as Bootstrap 3.x Pagination compatible HTML',
    #long_description=readme_text,
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ]
)
