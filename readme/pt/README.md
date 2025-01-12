
# Conversor de Áudio Pro (.m4a para .mp3)

Este projeto tem como objetivo converter arquivos de áudio no formato `.m4a` para `.mp3` utilizando **Python** e a biblioteca **pydub** (que depende do ffmpeg).

---

## Índice
- [Requisitos](#requisitos)
- [Instalação](#instalação)
  - [Configurar Ambiente Virtual](#configurar-ambiente-virtual)
- [Uso](#uso)
  - [Exemplo de Conversão de Um Arquivo](#exemplo-de-conversão-de-um-arquivo)
  - [Exemplo de Conversão de Vários Arquivos em um Diretório](#exemplo-de-conversão-de-vários-arquivos-em-um-diretório)
- [Logs e Barra de Progresso](#logs-e-barra-de-progresso)
- [Outras Observações](#outras-observações)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

---

## Requisitos

- Python 3.8 ou superior
- ffmpeg instalado no sistema:

### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

### Windows
- Baixe do [site oficial do ffmpeg](https://ffmpeg.org/) ou use o gerenciador **Chocolatey**.
- Certifique-se de que o executável `ffmpeg` está no seu PATH.

### macOS
```bash
brew install ffmpeg
```

---

## Instalação

Clone o repositório (ou faça download do ZIP):
```bash
git clone https://github.com/usuario/audio-converter-pro-pro.git
```

Navegue até a pasta do projeto:
```bash
cd audio-converter-pro-pro
```

### Dependências Python

Instale as dependências do `requirements.txt`:
```bash
pip install -r requirements.txt
```

As principais dependências são:
- **pydub** – biblioteca Python que facilita operações de áudio.
- Outras listadas no `requirements.txt`.

---

### Configurar Ambiente Virtual

É recomendado criar e ativar um ambiente virtual antes de instalar as dependências (para evitar conflitos com outras bibliotecas instaladas globalmente).

```bash
python -m venv venv
```

Ative o ambiente virtual:

- **Linux/Mac**:
    ```bash
    source venv/bin/activate
    ```
- **Windows**:
    ```bash
    venv\Scripts\activate
    ```

Agora, instale as dependências dentro do ambiente virtual:
```bash
pip install -r requirements.txt
```

---

## Uso

O script principal deste projeto é `convert_m4a_to_mp3.py`, que pode ser executado diretamente via linha de comando.

Ele aceita como argumentos:
1. `<input_path>`: Caminho de um arquivo `.m4a` ou de um diretório contendo vários `.m4a`.
2. `[output_directory]` (opcional): Diretório onde serão gerados os arquivos `.mp3`.

### Exemplo de Conversão de Um Arquivo

No mesmo local:
```bash
python convert_m4a_to_mp3.py "C:\musicas\faixa1.m4a"
```

Para um diretório de destino específico:
```bash
python convert_m4a_to_mp3.py "C:\musicas\faixa1.m4a" "C:\saida_mp3"
```

### Exemplo de Conversão de Vários Arquivos em um Diretório

No mesmo local:
```bash
python convert_m4a_to_mp3.py "C:\musicas"
```

Para outro diretório:
```bash
python convert_m4a_to_mp3.py "C:\musicas" "C:\saida_mp3"
```

---

## Logs e Barra de Progresso

O script mostra:
- **Barra de progresso**: exibe o índice do arquivo atual, total de arquivos e porcentagem concluída.
- Nome do arquivo de entrada e arquivo de saída gerado (ou erro, em caso de falha).
- Tempo de processamento de cada arquivo (em segundos).
- **Resumo final**: total de sucessos, falhas e tempo total de execução.

### Exemplo de saída:
```
Iniciando conversão de 3 arquivo(s) .m4a em 'C:\musicas'...

[1/3] |█████--------------|  33.3%  faixa1.m4a -> faixa1.mp3 : OK | tempo: 2.37s
[2/3] |██████████---------|  66.7%  faixa2.m4a -> faixa2.mp3 : OK | tempo: 3.10s
[3/3] |██████████████████-| 100.0%  faixa3.m4a -> ERRO: ...

Conversão concluída!
 - Sucessos : 2
 - Falhas   : 1
 - Total    : 3
Tempo total de execução: 12.45s.
```

---

## Outras Observações

- Se você tiver problemas com barras invertidas (`\`), utilize aspas para caminhos que contenham espaços ou caracteres especiais.
- Caso queira extensões diferentes ou outro formato de saída, é possível adaptar o código para usar:
    ```python
    AudioSegment.from_file(input_file, format="m4a").export(output_file, format="mp3")
    ```
    Com outras configurações (bitrate, canais, etc.).

---

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** ou enviar **pull requests**.

1. Faça um fork do projeto.
2. Crie uma branch para sua contribuição:
    ```bash
    git checkout -b feature/sua-contribuicao
    ```
3. Faça commit das suas mudanças:
    ```bash
    git commit -m "Adiciona nova feature"
    ```
4. Faça push da branch:
    ```bash
    git push origin feature/sua-contribuicao
    ```
5. Abra um **Pull Request** explicando a mudança proposta.

---

## Licença

Este projeto é distribuído sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.

**Autor**: Lucas Albuquerque 
**Contato**: lucas.albuquerque.gk@gmail.com
