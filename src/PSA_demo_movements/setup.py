from setuptools import find_packages, setup

package_name = 'PSA_demo_movements'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='marmot',
    maintainer_email='2645885722@qq.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'main_demo = PSA_demo_movements.main_demo:main',
            'test_goto = PSA_demo_movements.test_goto:main',
            'main_keyboard = PSA_demo_movements.main_keyboard:main',
        ],
    },
)
