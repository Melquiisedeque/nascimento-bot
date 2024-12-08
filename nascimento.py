from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


def formatar_data(data_nascimento):
    # Remover espaços e verificar se a data tem o tamanho correto
    data_nascimento = data_nascimento.replace(" ", "")

    # Verificar se a data tem o formato ISO 8601 (1995-09-29T00:00:00.000Z)
    try:
        if 'T' in data_nascimento and 'Z' in data_nascimento:
            # Formato: 1995-09-29T00:00:00.000Z
            data_formatada = datetime.strptime(data_nascimento, "%Y-%m-%dT%H:%M:%S.%fZ")
            return data_formatada.strftime("%Y-%m-%d")
    except ValueError:
        pass

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


@app.route('/webhook', methods=['POST'])
def webhook():
    # Recebe a data de nascimento do corpo da requisição
    data = request.json

    # Verifica se a chave 'data_nascimento' está presente
    if 'data_nascimento' in data:
        data_nascimento = data['data_nascimento']
        # Formata a data
        data_formatada = formatar_data(data_nascimento)
        # Retorna a resposta no formato esperado pelo BotConversa
        return jsonify({'data_formatada': data_formatada})
    else:
        return jsonify({'error': 'Data de nascimento não fornecida'}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)  # Porta 5003
