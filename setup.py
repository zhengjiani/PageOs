# 项目可安装化
from setuptools import find_packages,setup

setup(
    name = 'pograph',
    version = '1.0.0',
    # 自动查找python所包含的文件夹，包含python文件
    packages = find_packages(),
    # 包含其他文件夹，包括静态文件和模版文件所在的文件夹
    include_package_data = True,
    zip_safe = False,
    install_requires=[
        'flask',
    ],
)
