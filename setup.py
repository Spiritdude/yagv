import setuptools

setuptools.setup(
    name = 'yagv',
    version = '0.5.8',        # -- check ./yagv & Makefile too
    description = 'Yet Another Gcode Viewer (3D Printing Format)',
    packages = setuptools.find_packages(),
    package_data = {'yagv': [ "data/icon.png", "data/hana_swimsuit_fv_solid_v1.gcode" ] },
    data_files = [
        ( "share/applications", [ "yagv.desktop" ] ),
        ( "share/icons/hicolor/scalable/apps", [ "yagv.svg" ] ),
    ],
    classifiers = [
      "Environment :: Console",
      "Topic :: Multimedia :: Graphics :: 3D Rendering",
      "Topic :: Multimedia :: Graphics :: Presentation",
      "Topic :: Multimedia :: Graphics :: Viewers"
    ],
    entry_points={
        'gui_scripts': [
            "yagv = yagv.__main__:main"
        ]
    },
    python_requires='>3.6',
    install_requires=[
        'setuptools',
        'pyglet>=1.4.10, <2'
    ]
)
