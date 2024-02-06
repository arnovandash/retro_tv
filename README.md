# Retro 90s TV

## Description

Retro 90s TV is a Python project designed to bring back the nostalgic experience of enjoying TV series in the 90s. Unlike modern streaming services, where autoplay tends to skip intros and jump straight to the next episode, this project aims to recreate the anticipation and joy of watching one episode at a time, with the added benefit of remembering exactly where you left off. Whether you're rewatching your favorite series or exploring classics for the first time, Retro 90s TV offers a unique viewing experience that mimics the simplicity and charm of '90s television.

## Features

- **Sequential Playback:** Automatically plays episodes from your stored TV series in succession, moving through each series one episode at a time.
- **State Memory:** Remembers the last watched episode and its playback position, so you can resume exactly where you left off.

## Folder Structure

To ensure the script functions correctly, organize your TV series in the following structure:
```
Videos/Series/Season/Episode.mp4
```
This structure helps the script to correctly identify and play episodes in sequence.

## Getting Started

### Prerequisites

- Python 3.x
- VLC Media Player
- `python-vlc` module (install via pip)

### Installation

1. Ensure VLC Media Player is installed on your system.
2. Clone this repository or download the source code.
3. Install the required Python module:

```bash
pip install python-vlc
```

4. Update the `PATH` variable in the script to point to the directory containing your TV series.

### Usage

Run the script from the command line:

```bash
python retro_tv.py
```

The script will automatically play episodes from your configured TV series directory, resuming from the last episode you watched.

## Known Issues

- **Work in Progress:** This project is currently under development, and users might encounter issues. Notably, the video window may not load correctly due to the error:
  ```
  [00007f9775705050] macosx vout display error: No drawable-nsobject nor vout_window_t found, passing over.
  [00007f97748a10f0] main video output error: video output creation failed
  [00007f97747478d0] main decoder error: failed to create video output
  ```
  Any contributions to address this and other issues are greatly appreciated.

## Contributing

Contributions to Retro 90s TV are welcome! Whether it's adding new features, improving existing ones, or reporting bugs, your input helps make this project better for everyone.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Thanks to the VLC Media Player team for providing the robust media playback engine used in this project.
