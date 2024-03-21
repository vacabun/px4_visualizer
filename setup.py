from setuptools import find_packages, setup

package_name = 'px4_visualizer'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/'+ package_name + '/launch', ['launch/' + 'position.launch.py'])
    ],
    install_requires=['setuptools','geometry_msgs'],
    zip_safe=True,
    maintainer='vacabun',
    maintainer_email='maguotong66@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'position = px4_visualizer.position:main'
        ],
    },
)
