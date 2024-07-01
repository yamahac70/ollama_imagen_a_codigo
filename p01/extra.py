import re
import os

# Lee el archivo Markdown
with open('p000.md', 'r', encoding='utf-8',errors='ignore') as file:
    markdown_content = file.read()

# Divide el contenido por bloques de código
code_blocks = re.findall(r'```[a-z]*\n[\s\S]*?\n```', markdown_content)

if code_blocks:
    for block in code_blocks:
        language_match = re.search(r'```([a-z]*)', block)
        if language_match:
            language = language_match.group(1)
            code = re.sub(r'```[a-z]*\n', '', block).replace('\n```', '')

            if language == 'html':
                file_name = 'index.html'
            elif language == 'javascript':
                file_name = 'script.js'
            elif language == 'css':
                file_name = 'styles.css'
            elif language == 'markdown':
                file_name = 'index.md'
            elif language == 'python':
                file_name = 'index.py'
            elif language == 'jsx':
                file_name = 'index.jsx'
            else:
                print(f'Lenguaje no soportado: {language}')
                continue

            with open(f"proyec/{file_name}", 'w', encoding='utf-8') as code_file:
                code_file.write(code)
                print(f'Archivo {language} guardado como {file_name}')
else:
    print('No se encontraron bloques de código.')