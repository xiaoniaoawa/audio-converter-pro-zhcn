
# Audio Converter Pro (.m4a to .mp3)

This project aims to convert audio files from the `.m4a` format to `.mp3` using **Python** and the **pydub** library (which depends on ffmpeg).

---

## Index
- [Requirements](#requirements)
- [Installation](#installation)
  - [Set Up Virtual Environment](#set-up-virtual-environment)
- [Usage](#usage)
  - [Single File Conversion Example](#single-file-conversion-example)
  - [Multiple Files Conversion Example](#multiple-files-conversion-example)
- [Logs and Progress Bar](#logs-and-progress-bar)
- [Other Notes](#other-notes)
- [Contributing](#contributing)
- [License](#license)

---

## Requirements

- Python 3.8 or later
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

## Installation

Clone the repository (or download the ZIP):
```bash
git clone https://github.com/user/audio-converter-pro.git
```

Navigate to the project folder:
```bash
cd audio-converter-pro
```

### Python Dependencies

Install dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```

Key dependencies include:
- **pydub** – A Python library for easy audio operations.
- Others listed in `requirements.txt`.

---

### Set Up Virtual Environment

It is recommended to create and activate a virtual environment before installing dependencies (to avoid conflicts with globally installed libraries).

```bash
python -m venv venv
```

Activate the virtual environment:

- **Linux/Mac**:
    ```bash
    source venv/bin/activate
    ```
- **Windows**:
    ```bash
    venv\Scripts\activate
    ```

Now, install the dependencies inside the virtual environment:
```bash
pip install -r requirements.txt
```

---

## Usage

The main script for this project is `convert_m4a_to_mp3.py`, which can be run directly from the command line.

It accepts the following arguments:
1. `<input_path>`: Path to a `.m4a` file or a directory containing `.m4a` files.
2. `[output_directory]` (optional): Directory where the `.mp3` files will be saved.

### Single File Conversion Example

In the same location:
```bash
python convert_m4a_to_mp3.py "C:\music\track1.m4a"
```

To a specific output directory:
```bash
python convert_m4a_to_mp3.py "C:\music\track1.m4a" "C:\output_mp3"
```

### Multiple Files Conversion Example

In the same location:
```bash
python convert_m4a_to_mp3.py "C:\music"
```

To a different directory:
```bash
python convert_m4a_to_mp3.py "C:\music" "C:\output_mp3"
```

---

## Logs and Progress Bar

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

## Other Notes

- If you encounter issues with backslashes (`\`), use quotes for paths containing spaces or special characters.
- To support different extensions or output formats, modify the code to use:
    ```python
    AudioSegment.from_file(input_file, format="m4a").export(output_file, format="mp3")
    ```
    With other settings (bitrate, channels, etc.).

---

## Contributing

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

## License

This project is distributed under the MIT License. Feel free to use, modify, and distribute.

**Author**: Lucas Albuquerque
**Contact**: lucas.albuquerque.gk@gmail.com

## Documentation in Other Languages
- [Portuguese](readme/pt/README.md)
- [Spanish](readme/es/README.md)
- [French](readme/fr/README.md)