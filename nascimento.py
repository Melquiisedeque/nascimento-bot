from datetime import datetime


def formatar_data(data_nascimento):
    # Remover espaços e verificar se a data tem o tamanho correto
    data_nascimento = data_nascimento.replace(" ", "")

    # Verificar se a data tem 8 caracteres ou 7 caracteres (sem separadores)
    if len(data_nascimento) == 8 and data_nascimento.isdigit():
        try:
            # Formato DDMMYYYY
            data_formatada = datetime.strptime(data_nascimento, "%d%m%Y")
            return data_formatada.strftime("%Y-%m-%d")
        except ValueError:
            return "Formato de data inválido"
    elif len(data_nascimento) == 7 and data_nascimento.isdigit():
        try:
            # Formato DMMYYYY (com 1 dígito no dia)
            data_formatada = datetime.strptime(data_nascimento, "%d%m%Y")
            return data_formatada.strftime("%Y-%m-%d")
        except ValueError:
            return "Formato de data inválido"

    # Tentando os formatos com separadores
    try:
        # Tenta com o formato DD/MM/YYYY
        data_formatada = datetime.strptime(data_nascimento, "%d/%m/%Y")
        return data_formatada.strftime("%Y-%m-%d")
    except ValueError:
        try:
            # Tenta com o formato MM-DD-YYYY
            data_formatada = datetime.strptime(data_nascimento, "%m-%d-%Y")
            return data_formatada.strftime("%Y-%m-%d")
        except ValueError:
            try:
                # Tenta com o formato YYYY-MM-DD
                data_formatada = datetime.strptime(data_nascimento, "%Y-%m-%d")
                return data_formatada.strftime("%Y-%m-%d")
            except ValueError:
                try:
                    # Tenta com o formato DD.MM.YYYY (pontos como separadores)
                    data_formatada = datetime.strptime(data_nascimento, "%d.%m.%Y")
                    return data_formatada.strftime("%Y-%m-%d")
                except ValueError:
                    return "Formato de data inválido"


# Exemplo de uso
data_nascimento = input("Digite a data de nascimento: ")
print("Data formatada:", formatar_data(data_nascimento))
