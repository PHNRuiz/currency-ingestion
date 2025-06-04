# Dockerfile - A receita para nossa caixinha mágica!

# 1. Pegamos uma base pronta com Python (como uma caixa de LEGO já com peças de Python)
# Usaremos uma versão específica e "slim" (pequena) para economizar espaço
FROM python:3.11-slim

# 2. Dizemos onde vamos guardar as coisas dentro da caixinha
WORKDIR /app

# 3. Copiamos a lista de "brinquedos" (bibliotecas) que nosso projeto precisa
# Primeiro copiamos só a lista para o Docker ser mais rápido se a lista não mudar
COPY requirements.txt .

# 4. Mandamos o Docker instalar todos os "brinquedos" da lista
# "--no-cache-dir" é para não guardar lixo da instalação
RUN pip install --no-cache-dir -r requirements.txt

# 5. Agora copiamos o resto do nosso projeto para dentro da caixinha
# Copiamos a pasta 'app' com nosso código e o arquivo '.env' com os segredos
COPY ./app ./app
COPY .env .

# 6. Dizemos qual comando rodar quando a caixinha mágica for ligada
# É o mesmo comando que usamos no terminal!
CMD ["python", "-m", "app.main"]

