import src.external_modules.ssd1306 as ssd1306
import machine

# Display Settings
i2c = machine.I2C(0)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

font = {
    'A': [
        0b00100,
        0b01010,
        0b10001,
        0b11111,
        0b10001
    ],
    'B': [
        0b11110,
        0b10001,
        0b11110,
        0b10001,
        0b11110
    ],
    'C': [
        0b01110,
        0b10000,
        0b10000,
        0b10000,
        0b01110
    ],
    'D': [
        0b11100,
        0b10010,
        0b10001,
        0b10001,
        0b11110
    ],
    'E': [
        0b11111,
        0b10000,
        0b11100,
        0b10000,
        0b11111
    ],
    'F': [
        0b11111,
        0b10000,
        0b11100,
        0b10000,
        0b10000
    ],
    'G': [
        0b01110,
        0b10000,
        0b10011,
        0b10001,
        0b01110
    ],
    'H': [
        0b10001,
        0b10001,
        0b11111,
        0b10001,
        0b10001
    ],
    'I': [
        0b11100,
        0b01000,
        0b01000,
        0b01000,
        0b11100
    ],
    'J': [
        0b11110,
        0b00100,
        0b00100,
        0b10100,
        0b01000
    ],
    'K': [
        0b10001,
        0b10010,
        0b11100,
        0b10010,
        0b10001
    ],
    'L': [
        0b10000,
        0b10000,
        0b10000,
        0b10000,
        0b11111
    ],
    'M': [
        0b10001,
        0b11011,
        0b10101,
        0b10001,
        0b10001
    ],
    'N': [
        0b10001,
        0b11001,
        0b10101,
        0b10011,
        0b10001
    ],
    'O': [
        0b01110,
        0b10001,
        0b10001,
        0b10001,
        0b01110
    ],
    'P': [
        0b11110,
        0b10001,
        0b11110,
        0b10000,
        0b10000
    ],
    'Q': [
        0b01110,
        0b10001,
        0b10101,
        0b10011,
        0b01111
    ],
    'R': [
        0b11110,
        0b10001,
        0b11110,
        0b10010,
        0b10001
    ],
    'S': [
        0b01111,
        0b10000,
        0b01110,
        0b00001,
        0b11110
    ],
    'T': [
        0b11111,
        0b00100,
        0b00100,
        0b00100,
        0b00100
    ],
    'U': [
        0b10001,
        0b10001,
        0b10001,
        0b10001,
        0b01110
    ],
    'V': [
        0b10001,
        0b10001,
        0b10001,
        0b01010,
        0b00100
    ],
    'W': [
        0b10001,
        0b10001,
        0b10101,
        0b11011,
        0b10001
    ],
    'X': [
        0b10001,
        0b01010,
        0b00100,
        0b01010,
        0b10001
    ],
    'Y': [
        0b10001,
        0b01010,
        0b00100,
        0b00100,
        0b00100
    ],
    'Z': [
        0b11111,
        0b00010,
        0b00100,
        0b01000,
        0b11111
    ],
    ' ': [
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00000
    ],
    ':': [
        0b00000,
        0b01000,
        0b00000,
        0b01000,
        0b00000
    ],
    '?': [
        0b01110,
        0b10001,
        0b00010,
        0b00100,
        0b00000
    ],
    '.': [
        0b00000,
        0b00000,
        0b00000,
        0b00100,
        0b00000

    ], '0': [
        0b01110,
        0b10001,
        0b10001,
        0b10001,
        0b01110
    ],
    '1': [
        0b00100,
        0b01100,
        0b00100,
        0b00100,
        0b01110
    ],
    '2': [
        0b01110,
        0b10001,
        0b00001,
        0b00010,
        0b11111
    ],
    '3': [
        0b11111,
        0b00010,
        0b00100,
        0b00001,
        0b11110
    ],
    '4': [
        0b00010,
        0b00110,
        0b01010,
        0b11111,
        0b00010
    ],
    '5': [
        0b11111,
        0b10000,
        0b11110,
        0b00001,
        0b11110
    ],
    '6': [
        0b00110,
        0b01000,
        0b11110,
        0b10001,
        0b01110
    ],
    '7': [
        0b11111,
        0b00001,
        0b00010,
        0b00100,
        0b01000
    ],
    '8': [
        0b01110,
        0b10001,
        0b01110,
        0b10001,
        0b01110
    ],
    '9': [
        0b01110,
        0b10001,
        0b01111,
        0b00001,
        0b00110
    ],
}


def draw_text(oled, text, x, y, color):
    text = str(text).upper()

    # Largura e altura máximas de um caractere
    max_char_width = 5
    max_char_height = 5

    # Inicializa as coordenadas x e y iniciais
    current_x = x
    current_y = y

    # Percorre cada caractere na string
    for char in text:
        if char in font:
            # Obtém a matriz de pixels para o caractere
            char_pixels = font[char]

            # Desenha o caractere na tela
            for i in range(max_char_height):
                for j in range(max_char_width):
                    if (char_pixels[i] >> (max_char_width - 1 - j)) & 1:
                        oled.pixel(current_x + j, current_y + i, color)

            # Move as coordenadas para o próximo caractere
            current_x += max_char_width + 1  # Adiciona 1 pixel de espaço entre caracteres


draw_text(oled, 'Turbo: 1.2Kg', 0, 0, 1)
draw_text(oled, 'Oil Press.: 3.0Bar', 0, 15, 1)
draw_text(oled, 'Fuel Press.: 5.0 Bar', 0, 30, 1)
# oled.invert(1)
oled.show()
