import lesscpy

def generate_styles():
    with open('docs/styles.css', 'w') as css_file:
        less = open('core/styles/main.less', 'r')
        css = lesscpy.compile(less, minify=True)
        css_file.write(css)


if __name__ == "__main__":
    generate_styles();
