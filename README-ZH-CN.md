
# Audio Converter Pro (.m4a 到 .mp3)

这个项目会用 **Python** 和 **pydub** 库 (该库依赖ffmpeg)把 `.m4a` 转换格式到 `.mp3` .

---

## Index
- [前置需求](#requirements)
- [安装](#installation)
  - [配置虚拟容器](#set-up-virtual-environment)
- [使用](#usage)
  - [单文件使用样例](#single-file-conversion-example)
  - [多文件使用样例](#multiple-files-conversion-example)
- [日志和进度条](#logs-and-progress-bar)
- [其他提醒](#other-notes)
- [贡献](#contributing)
- [许可](#license)

---

## 前置需求

- Python 3.8 或更新
- ffmpeg installed on your system:

### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

### Windows
- Download from the [official ffmpeg site](https://ffmpeg.org/) or use the **Chocolatey** package manager.
- Ensure the `ffmpeg` executable is in your PATH.

### macOS
```bash
brew install ffmpeg
```

---

## 安装

克隆仓库 (或下载 ZIP):
```bash
git clone https://github.com/user/audio-converter-pro.git
```

到项目文件夹:
```bash
cd audio-converter-pro
```

### Python 依赖

从 `requirements.txt` 安装依赖:
```bash
pip install -r requirements.txt
```

包含关键依赖（Key dependencies include）:
- **pydub** – A Python library for easy audio operations.
- Others listed in `requirements.txt`.

---

### 配置虚拟容器

建议在安装库之前设置虚拟环境 (用来保护全局库和其他依赖).

```bash
python -m venv venv
```

激活虚拟环境:

- **Linux/Mac**:
    ```bash
    source venv/bin/activate
    ```
- **Windows**:
    ```bash
    venv\Scripts\activate
    ```

然后，在虚拟环境里面安装依赖:
```bash
pip install -r requirements.txt
```

---

## 使用

主程序文件是 `convert_m4a_to_mp3.py`, 它能直接使用命令行启动.

It accepts the following arguments:
1. `<input_path>`: 包含`.m4a`的文件夹或文件路径.
2. `[output_directory]` (可选): 要让 `mp3` 文件存储在哪.

### 单文件使用样例

PS:翻译不下去了，明天再翻译
In the same location:
```bash
python convert_m4a_to_mp3.py "C:\music\track1.m4a"
```

To a specific output directory:
```bash
python convert_m4a_to_mp3.py "C:\music\track1.m4a" "C:\output_mp3"
```

### 多文件使用样例

In the same location:
```bash
python convert_m4a_to_mp3.py "C:\music"
```

To a different directory:
```bash
python convert_m4a_to_mp3.py "C:\music" "C:\output_mp3"
```

---

## 日志和进度条

The script displays:
- **Progress bar**: Shows the index of the current file, total files, and completion percentage.
- Input file name and the generated output file (or error in case of failure).
- Processing time for each file (in seconds).
- **Final summary**: Total successes, failures, and total execution time.

### Example Output:
```
Starting conversion of 3 .m4a file(s) in 'C:\music'...

[1/3] |█████--------------|  33.3%  track1.m4a -> track1.mp3 : OK | time: 2.37s
[2/3] |██████████---------|  66.7%  track2.m4a -> track2.mp3 : OK | time: 3.10s
[3/3] |██████████████████-| 100.0%  track3.m4a -> ERROR: ...

Conversion complete!
 - Successes : 2
 - Failures  : 1
 - Total     : 3
Total execution time: 12.45s.
```

---

## 其他提醒

- If you encounter issues with backslashes (`\`), use quotes for paths containing spaces or special characters.
- To support different extensions or output formats, modify the code to use:
    ```python
    AudioSegment.from_file(input_file, format="m4a").export(output_file, format="mp3")
    ```
    With other settings (bitrate, channels, etc.).

---

## 贡献

Contributions are welcome! Feel free to open **issues** or submit **pull requests**.

1. Fork the repository.
2. Create a branch for your contribution:
    ```bash
    git checkout -b feature/your-contribution
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add new feature"
    ```
4. Push the branch:
    ```bash
    git push origin feature/your-contribution
    ```
5. Open a **Pull Request** explaining your proposed changes.

---

## 许可

This project is distributed under the MIT License. Feel free to use, modify, and distribute.

**Author**: Lucas Albuquerque
**Contact**: lucas.albuquerque.gk@gmail.com

## 其它语言的文档
- [Portuguese](readme/pt/README.md)
- [Spanish](readme/es/README.md)
- [French](readme/fr/README.md)
