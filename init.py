
import os

try: input = raw_input
except NameError: pass

name = input("Please enter the name of your project: ")

def template(name, target, **kwargs):
    f = open(name)
    text = f.read()
    f.close()
    for k, v in kwargs.items():
        text = text.replace('{{' + k + '}}', v)
    f = open(target, 'w')
    f.write(text)
    f.close()

if name.strip():
    template('cmake/template.txt', 'CMakeLists.txt', project_name=name)
    template('cmake/template_src.txt', 'src/CMakeLists.txt', project_name=name)

