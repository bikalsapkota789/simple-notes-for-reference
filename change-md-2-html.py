import markdown 
import os 
import sys 

markdown_file = open(os.path.join(sys.path[0], "django.md"), "r")

#print(markdown_file.read())
new_html = markdown.markdown(markdown_file.read(), extensions=['md_in_html'])

with open('django.html', 'w') as html_file:
    html_file.write(new_html)

#print(new_html)

