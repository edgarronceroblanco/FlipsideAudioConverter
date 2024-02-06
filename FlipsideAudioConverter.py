import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from datetime import datetime

class FlipsideAudioConverter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Flipside Audio Converter")
        self.window.geometry("600x400")

        self.selected_directory_label = tk.Label(self.window, text="Select a directory containing audio files", wraplength=550)
        self.selected_directory_label.pack(pady=10)

        self.input_format_label = tk.Label(self.window, text="Select input audio format:")
        self.input_format_label.pack(pady=5)

        self.input_format_var = tk.StringVar()
        self.input_format_var.set(".flac")  # Set default input format to FLAC

        # Allow input format selection for FLAC, WAV, AIF, AIFF, M4A
        self.input_format_dropdown = ttk.Combobox(self.window, textvariable=self.input_format_var, values=(".flac", ".wav", ".aif", ".aiff", ".m4a"))
        self.input_format_dropdown.pack(pady=5)

        self.output_format_label = tk.Label(self.window, text="Select output audio format:")
        self.output_format_label.pack(pady=5)

        self.output_format_var = tk.StringVar()
        self.output_format_var.set(".m4a")  # Set default output format to M4A

        # Allow output format selection for M4A, MP3, FLAC
        self.output_format_dropdown = ttk.Combobox(self.window, textvariable=self.output_format_var, values=(".m4a", ".mp3", ".flac"))
        self.output_format_dropdown.pack(pady=5)

        self.dither_checkbox_var = tk.IntVar()
        self.dither_checkbox = tk.Checkbutton(self.window, text="Apply Dithering", variable=self.dither_checkbox_var)
        self.dither_checkbox.pack(pady=5)

        self.progress_label = tk.Label(self.window, text="")
        self.progress_label.pack(pady=5)

        select_directory_button = tk.Button(self.window, text="Select directory", command=self.open_directory_dialog)
        select_directory_button.pack(pady=5)

        convert_button = tk.Button(self.window, text="Convert", command=self.convert_files)
        convert_button.pack(pady=10)

        # Set initial values for cmd and output_file
        self.cmd = None

        self.window.mainloop()

    def open_directory_dialog(self):
        directory_path = filedialog.askdirectory(title="Select a directory containing audio files")
        if directory_path:
            self.selected_directory_label.config(text=directory_path)

    def create_output_folder(self, input_directory):
        output_folder = os.path.join(os.path.dirname(input_directory), '_' + os.path.basename(input_directory))
        os.makedirs(output_folder, exist_ok=True)
        return output_folder

    def update_progress(self, current, total):
        percentage = int((current / total) * 100)
        self.progress_label.config(text=f"Converting: {percentage}%")
        self.window.update_idletasks()

    def update_current_file_label(self, message):
        self.progress_label.config(text=message)
        self.window.update_idletasks()

    def convert_files(self):
        input_directory = self.selected_directory_label.cget("text")
        if not input_directory:
            messagebox.showerror(title="Error", message="Please select a directory.")
            return

        output_format = self.output_format_var.get()
        output_extension = ".mp3" if output_format == ".mp3" else ".flac" if output_format == ".flac" else ".m4a"

        output_folder = self.create_output_folder(input_directory)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        log_filename = f"{os.path.basename(output_folder)}_{timestamp}.log"
        log_filepath = os.path.join(output_folder, log_filename)

        use_dither = self.dither_checkbox_var.get() == 1
        input_format = self.input_format_var.get()

        input_files = [os.path.join(input_directory, f) for f in os.listdir(input_directory) if
                       os.path.isfile(os.path.join(input_directory, f)) and f.lower().endswith((input_format.lower()))]

        total_files = len(input_files)
        self.update_file_count_label(total_files)

        with open(log_filepath, 'w') as log_file:
            for i, input_file in enumerate(input_files, start=1):
                output_file = os.path.join(output_folder, os.path.basename(input_file))
                output_file = os.path.splitext(output_file)[0] + output_extension

                if output_format == ".mp3":
                    self.cmd = ['ffmpeg', '-i', input_file, '-vn', '-map_metadata', '0', '-c:a', 'mp3', '-b:a', '320k', '-y', output_file]
                elif output_format == ".flac":
                    self.cmd = ['ffmpeg', '-i', input_file, '-c:v', 'copy', '-map_metadata', '0', '-c:a', 'flac', '-y', output_file]
                else:
                    self.cmd = ['ffmpeg', '-i', input_file, '-c:v', 'copy', '-map_metadata', '0', '-c:a', 'alac', '-y', output_file]

                if use_dither:
                    self.cmd.extend(['-dither_method', 'triangular'])

                print(f"Executing command: {' '.join(self.cmd)}")

                try:
                    subprocess.run(self.cmd, stdout=log_file, stderr=log_file, check=True)
                except subprocess.CalledProcessError as e:
                    messagebox.showerror(title="Error", message=f"Error converting file: {input_file}\n{str(e)}")

                self.update_progress(i, total_files)
                self.update_current_file_label(os.path.basename(input_file))

        self.update_progress(total_files, total_files)
        self.update_current_file_label("Conversion completed.")
        messagebox.showinfo(title="Converted", message="Conversion completed successfully.")

    def update_file_count_label(self, message):
        self.progress_label.config(text=message)
        self.window.update_idletasks()

if __name__ == "__main__":
    app = FlipsideAudioConverter()

