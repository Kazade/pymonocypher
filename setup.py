"""
pymonocypher
"""

# See:
# https://packaging.python.org/en/latest/distributing.html
# https://github.com/pypa/sampleproject


import setuptools
import os

MYPATH = os.path.abspath(os.path.dirname(__file__))
VERSION = '3.1.1.0'  # also change c_monocypher.pyx


from Cython.Build import cythonize


ext = '.pyx'
extensions = [
    setuptools.Extension('monocypher',
        sources=['c_monocypher' + ext, 'monocypher.c'],
        include_dirs=['.'],
        extra_compile_args=['-DBLAKE2_NO_UNROLLING'],
    ),
]


from Cython.Build import cythonize
extensions = cythonize(
    extensions,
    compiler_directives={'language_level': '3'})


# Get the long description from the README file
with open(os.path.join(MYPATH, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    # also edit c_monocypher.pyx
    name='pymonocypher',
    version=VERSION,
    description='Python ctypes bindings to the Monocypher library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jetperch/pymonocypher',
    author='Jetperch LLC',
    author_email='joulescope-dev@jetperch.com',
    license='BSD 2-clause',

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Natural Language :: English',
        'Topic :: Security :: Cryptography',

        # Supported Python versions
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: C',
    ],

    keywords='cryto cryptography monocypher chacha blake2b 25519',
    install_requires = [
        'Cython'
    ],
    extras_require={
        'dev': ['check-manifest', 'Cython', 'coverage'],
    },
    ext_modules=extensions,

    project_urls={
        'Bug Reports': 'https://github.com/jetperch/pymonocypher/issues',
        'Source': 'https://github.com/jetperch/pymonocypher/',
    },
)
