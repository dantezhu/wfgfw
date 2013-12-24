from setuptools import setup
import wfgfw

setup(
    name="wfgfw",
    version=wfgfw.__version__,
    zip_safe=False,
    platforms='any',
    py_modules=['wfgfw'],
    url="https://github.com/dantezhu/wfgfw",
    license="BSD",
    author="dantezhu",
    author_email="zny2008@gmail.com",
    description="word filter for gfw. download keywords: https://github.com/observerss/textfilter",
    )
