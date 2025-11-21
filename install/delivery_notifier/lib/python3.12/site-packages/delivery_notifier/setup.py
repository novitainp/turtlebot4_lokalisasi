from setuptools import setup

package_name = 'delivery_notifier'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='',
    description='Delivery notifier for TurtleBot4',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'delivery_notifier = delivery_notifier.delivery_notifier:main',
        ],
    },
)

