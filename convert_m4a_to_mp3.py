import sys
import os
import time
from pydub import AudioSegment

def convert_m4a_to_mp3(input_file, output_file=None):
    """
    将m4a文件转换为mp3文件

    :param input_file: Caminho completo do arquivo .m4a.
    :param output_file: 输出路径（可选）。如果无,
                        将以相同目录和相同名称生成转换过的文件,
                        也就是（只从文件名角度看）只将扩展名变成mp3.
    :return: 生成的 .mp3 文件的完整路径.
    """
    if not output_file:
        output_file = os.path.splitext(input_file)[0] + '.mp3'

    audio = AudioSegment.from_file(input_file, format="m4a")
    audio.export(output_file, format="mp3")
    return output_file

def log_progress(index, total, filename, output_filename, status='OK', error_msg=None, elapsed_time=None):
    """
    显示带有计数器和进度条的进度信息

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
            print(f"输入的文件 {input_path} 不是.m4a文件")
            sys.exit(1)

        total_files = 1
        success_count = 0
        fail_count = 0

        print("开始单个文件转换...\n")

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
        print(f"\n转换完成！成功个数: {success_count}, 失败个数: {fail_count}, Total: {total_files}.")
        print(f"运行耗时: {elapsed_time_total:.2f}s.")

    # Se for um diretório
    elif os.path.isdir(input_path):
        files_m4a = [f for f in os.listdir(input_path) if f.lower().endswith('.m4a')]
        total_files = len(files_m4a)
        if total_files == 0:
            print(f"在 {input_path} 下未找到m4a文件")
            sys.exit(0)

        print(f"开始转换 {input_path} 中的 {total_files} 个m4a文件 arquivo(s) .m4a em...\n")

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
        print("\n转换完成！")
        print(f" - 成功数 : {success_count}")
        print(f" - 失败数   : {fail_count}")
        print(f" - 总计    : {total_files}")
        print(f"运行时间: {elapsed_time_total:.2f}s.")

    else:
        print(f"错误: {input_path} 不是有效文件或目录。")
        sys.exit(1)

if __name__ == '__main__':
    main()
