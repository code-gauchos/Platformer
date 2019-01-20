@ECHO OFF

pip install --upgrade pip wheel setuptools

python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy.deps.gstreamer
python -m pip install kivy

pip install pyserial

pip install final_class

pip install pillow