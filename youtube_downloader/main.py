from tkinter import *
from tkinter import messagebox, filedialog
from pytube import YouTube

class Downloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.geometry("400x150")

        self.url_label = Label(self.root, text="Enter YouTube Video URL:")
        self.url_label.pack(pady=10)

        self.url_entry = Entry(self.root, width=40)
        self.url_entry.pack(pady=5)

        self.download_button = Button(self.root, text="Download", command=self.download_video)
        self.download_button.pack(pady=10)

    def download_video(self):
        video_url = self.url_entry.get()
        if video_url:
            try:
                yt = YouTube(video_url)
                stream = yt.streams.get_highest_resolution()

                # Open a dialog for the user to select a folder
                save_path = filedialog.askdirectory()
                if save_path:  # Proceed only if a folder is selected
                    stream.download(output_path=save_path)
                    messagebox.showinfo("Success", "Video downloaded successfully!")
                else:
                    messagebox.showwarning("Cancelled", "Download cancelled by the user.")

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            messagebox.showwarning("Input Error", "Please enter a valid YouTube URL.")

if __name__ == '__main__':
    root = Tk()
    application = Downloader(root)
    root.mainloop()
