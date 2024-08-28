import re
from django.db import transaction
from GPC.models.gestor import ElementConfiguration, PageConfiguration

def parse_css(file_path):
    elements = {}
    current_selector = None

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            # Identifica seletores (início de bloco CSS)
            if line and line.endswith('{'):
                current_selector = line[:-1].strip()
                if current_selector.startswith('.'):
                    current_selector = current_selector[1:]
                elements[current_selector] = {
                    'background_color': None,
                    'text_color': None
                }

            # Identifica propriedades CSS dentro do bloco
            elif current_selector:
                if line.startswith('background-color:'):
                    elements[current_selector]['background_color'] = line.split(':')[1].strip().rstrip(';')
                elif line.startswith('color:'):
                    elements[current_selector]['text_color'] = line.split(':')[1].strip().rstrip(';')

            # Identifica o fim do bloco CSS
            if line and line == '}':
                current_selector = None

    # Remove elementos sem background-color e color
    elements = {k: v for k, v in elements.items() if v['background_color'] or v['text_color']}

    return elements

@transaction.atomic
def parse_css_and_create_elements(file_path, page_name):
    elements = parse_css(file_path)

    # Obtém ou cria a configuração da página
    page_config, _ = PageConfiguration.objects.get_or_create(page_name=page_name)

    for selector, styles in elements.items():
        # Cria ou atualiza o elemento
        element, created = ElementConfiguration.objects.get_or_create(
            element_name=selector,
            defaults={
                'background_color': styles['background_color'] or None,
                'text_color': styles['text_color'] or None,
            }
        )

        if not created:
            if styles['background_color']:
                element.background_color = styles['background_color']
            if styles['text_color']:
                element.text_color = styles['text_color']
            element.save()

        # Adiciona o elemento à página
        page_config.elements.add(element)

    page_config.save()