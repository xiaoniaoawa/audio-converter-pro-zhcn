import sys
import os
import time
from pydub import AudioSegment

def convert_m4a_to_mp3(input_file, output_file=None):
    """
    Converte um arquivo .m4a para .mp3.

    :param input_file: Caminho completo do arquivo .m4a.
    :param output_file: Caminho de saída (opcional). Se None,
                        será gerado no mesmo local e nome do arquivo de entrada,
                        apenas mudando a extensão para .mp3.
    :return: Caminho completo do arquivo .mp3 gerado.
    """
    if not output_file:
        output_file = os.path.splitext(input_file)[0] + '.mp3'

    audio = AudioSegment.from_file(input_file, format="m4a")
    audio.export(output_file, format="mp3")
    return output_file

def log_progress(index, total, filename, output_filename, status='OK', error_msg=None, elapsed_time=None):
    """
    Exibe uma mensagem de progresso com contador e opcionalmente uma barra de progresso.

    :param index: Índice atual (1-based).
    :param total: Total de itens a processar.
    :param filename: Nome do arquivo de entrada.
    :param output_filename: Nome do arquivo de saída.
    :param status: 'OK' ou 'FALHA'.
    :param error_msg: Mensagem de erro caso status seja 'FALHA'.
    :param elapsed_time: Tempo decorrido, em segundos, para o processamento do arquivo (opcional).
    """
    # Exemplo de barra de progresso “criativa”
    progress_bar_length = 20  # tamanho “visual” da barra
    fraction = index / total
    filled = int(progress_bar_length * fraction)
    bar = '█' * filled + '-' * (progress_bar_length - filled)
    percent = fraction * 100

    time_str = ""
    if elapsed_time is not None:
        time_str = f" | tempo: {elapsed_time:.2f}s"

    if status == 'OK':
        print(f"[{index}/{total}] |{bar}| {percent:5.1f}%  {filename} -> {os.path.basename(output_filename)} : {status}{time_str}")
    else:
        # Em caso de falha, imprime a mensagem de erro
        print(f"[{index}/{total}] |{bar}| {percent:5.1f}%  {filename} -> ERRO: {error_msg}")

def main():
    """
    Modo de uso via linha de comando:
        python convert_m4a_to_mp3.py <input_path> [output_directory]

    - Se <input_path> for um arquivo .m4a, converte apenas esse arquivo.
    - Se <input_path> for um diretório, converte todos os arquivos .m4a encontrados nele.
    - Se [output_directory] for fornecido, os arquivos .mp3 serão gerados nesse diretório.
    - Exibe o tempo de conclusão para cada arquivo e o tempo total da conversão.
    """
    if len(sys.argv) < 2:
        print("Uso: python convert_m4a_to_mp3.py <input_path> [output_directory]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    # Marca o início do processo total
    start_time_total = time.time()

    # Se for um arquivo específico
    if os.path.isfile(input_path):
        if not input_path.lower().endswith('.m4a'):
            print(f"Entrada não é um arquivo .m4a: {input_path}")
            sys.exit(1)

        total_files = 1
        success_count = 0
        fail_count = 0

        print("Iniciando conversão de arquivo único...\n")

        try:
            start_time = time.time()  # tempo inicial do arquivo
            if output_dir is None:
                mp3_file = convert_m4a_to_mp3(input_path)
            else:
                base_name = os.path.splitext(os.path.basename(input_path))[0]
                mp3_file = os.path.join(output_dir, base_name + ".mp3")
                mp3_file = convert_m4a_to_mp3(input_path, mp3_file)
            elapsed_time_file = time.time() - start_time  # tempo final do arquivo

            success_count += 1
            log_progress(
                1, total_files,
                os.path.basename(input_path),
                mp3_file,
                status='OK',
                elapsed_time=elapsed_time_file
            )

        except Exception as e:
            fail_count += 1
            log_progress(
                1, total_files,
                os.path.basename(input_path),
                '',
                status='FALHA',
                error_msg=str(e)
            )

        # Resumo final
        elapsed_time_total = time.time() - start_time_total
        print(f"\nConversão concluída! Sucessos: {success_count}, Falhas: {fail_count}, Total: {total_files}.")
        print(f"Tempo total de execução: {elapsed_time_total:.2f}s.")

    # Se for um diretório
    elif os.path.isdir(input_path):
        files_m4a = [f for f in os.listdir(input_path) if f.lower().endswith('.m4a')]
        total_files = len(files_m4a)
        if total_files == 0:
            print(f"Nenhum arquivo .m4a encontrado em: {input_path}")
            sys.exit(0)

        print(f"Iniciando conversão de {total_files} arquivo(s) .m4a em '{input_path}'...\n")

        success_count = 0
        fail_count = 0

        for i, file_name in enumerate(files_m4a, start=1):
            full_input_file = os.path.join(input_path, file_name)
            base_name = os.path.splitext(file_name)[0]

            if output_dir is None:
                mp3_file = os.path.join(input_path, base_name + ".mp3")
            else:
                mp3_file = os.path.join(output_dir, base_name + ".mp3")

            try:
                start_time = time.time()  # tempo inicial do arquivo
                convert_m4a_to_mp3(full_input_file, mp3_file)
                elapsed_time_file = time.time() - start_time  # tempo final do arquivo

                success_count += 1
                log_progress(
                    i, total_files,
                    file_name,
                    mp3_file,
                    status='OK',
                    elapsed_time=elapsed_time_file
                )
            except Exception as e:
                fail_count += 1
                log_progress(
                    i, total_files,
                    file_name,
                    mp3_file,
                    status='FALHA',
                    error_msg=str(e)
                )

        # Resumo final
        elapsed_time_total = time.time() - start_time_total
        print("\nConversão concluída!")
        print(f" - Sucessos : {success_count}")
        print(f" - Falhas   : {fail_count}")
        print(f" - Total    : {total_files}")
        print(f"Tempo total de execução: {elapsed_time_total:.2f}s.")

    else:
        print(f"Erro: {input_path} não é um arquivo nem um diretório válido.")
        sys.exit(1)

if __name__ == '__main__':
    main()