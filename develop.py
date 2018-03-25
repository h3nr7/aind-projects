from livereload import Server, shell

def develop():
    server = Server()
    server.watch('core/styles/*.less', shell('python core/generate_styles.py'))
    server.watch('core/*.py', shell('python core/generate_html.py'))
    server.watch('core/templates/*.html', shell('python core/generate_html.py'))
    server.serve(root='docs', port=5500)

if __name__ == '__main__':
    develop()
