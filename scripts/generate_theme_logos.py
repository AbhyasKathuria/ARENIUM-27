import re

def generate_logos():
    with open('images/logo.svg', 'r', encoding='utf-8') as f:
        content = f.read()

    # Dark logo
    dark_content = content
    dark_content = dark_content.replace('fill="#160d0d"', 'fill="#3B0E14"')
    dark_content = dark_content.replace('stroke="rgba(165, 42, 42, 0.45)"', 'stroke="rgba(184, 29, 66, 0.45)"')
    dark_content = dark_content.replace('fill="#ffffff"', 'fill="#F8E8EB"')
    dark_content = dark_content.replace('fill="#A52A2A"', 'fill="#B81D42"')
    dark_content = dark_content.replace('fill="#6C403E"', 'fill="#7A0026"')

    with open('images/logo.svg', 'w', encoding='utf-8') as f:
        f.write(dark_content)

    with open('images/logo-dark.svg', 'w', encoding='utf-8') as f:
        f.write(dark_content)

    # Light logo
    light_content = content
    light_content = light_content.replace('fill="#160d0d"', 'fill="#E3EEF8"')
    light_content = light_content.replace('stroke="rgba(165, 42, 42, 0.45)"', 'stroke="rgba(91, 127, 255, 0.45)"')
    light_content = light_content.replace('fill="#ffffff"', 'fill="#1B2342"')
    light_content = light_content.replace('fill="#A52A2A"', 'fill="#5B7FFF"')
    light_content = light_content.replace('fill="#6C403E"', 'fill="#5B7FFF"')

    with open('images/logo-light.svg', 'w', encoding='utf-8') as f:
        f.write(light_content)

    print("Theme logos generated successfully!")

if __name__ == '__main__':
    generate_logos()
