class TextColor:
    def __init__(self, string):
        self.text = string

    def setColor(self, color: str) -> str:
        colors = {
            "red": "\33[0;49;31m",
            "green": "\33[0;49;32m",
            "yellow": "\33[0;49;33m",
            "blue": "\33[0;49;34m",
            "purple": "\33[0;49;35m",
            "light_blue": "\33[0;49;36m",
            "white": "\33[0;49;36m",
            "black": "\33[0;49;37m",
        }

        if colors.get(color):
            return f"{colors[color]}{self.text}\33[m"
        else:
            print(
                f"{colors['red']}A cor informada é inválida!\33[m\n\nCores disponíveis: {colors['green']}{', '.join(list(colors.keys()))}\33[m"
            )
            return self.text
