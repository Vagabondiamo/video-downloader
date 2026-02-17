#!/usr/bin/env python3
"""
Video Downloader - Scarica video da YouTube e social media
Autore: AI Assistant
Versione: 1.0
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import urllib.request
import re
import os
from urllib.parse import urlparse

# Per il download da YouTube (installare yt-dlp)
# pip install yt-dlp

# Per social media (installare requirements)
# pip install requests

try:
    import yt_dlp
    YTDLP_AVAILABLE = True
except ImportError:
    YTDLP_AVAILABLE = False

class VideoDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Downloader - YouTube & Social")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Colori tema scuro
        self.bg_color = "#1e1e2e"
        self.fg_color = "#cdd6f4"
        self.accent_color = "#89b4fa"
        self.entry_bg = "#313244"
        
        self.root.configure(bg=self.bg_color)
        
        self.output_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        self.create_widgets()
        
    def create_widgets(self):
        # Titolo
        title = tk.Label(self.root, text="📥 Video Downloader",
                        font=("Helvetica", 20, "bold"),
                        bg=self.bg_color, fg=self.accent_color)
        title.pack(pady=20)
        
        # Label URL
        url_label = tk.Label(self.root, text="Incolla URL del video:",
                            font=("Helvetica", 12),
                            bg=self.bg_color, fg=self.fg_color)
        url_label.pack(anchor="w", padx=30)
        
        # Entry URL
        self.url_entry = tk.Entry(self.root, font=("Helvetica", 11),
                                  bg=self.entry_bg, fg=self.fg_color,
                                  insertbackground=self.fg_color,
                                  relief="flat", width=50)
        self.url_entry.pack(padx=30, pady=5)
        
        # Label piattaforma
        self.platform_label = tk.Label(self.root, text="",
                                       font=("Helvetica", 10, "italic"),
                                       bg=self.bg_color, fg="#a6adc8")
        self.platform_label.pack(pady=5)
        
        # Opzioni
        options_frame = tk.Frame(self.root, bg=self.bg_color)
        options_frame.pack(pady=15, padx=30, fill="x")
        
        # Formato
        tk.Label(options_frame, text="Formato:", bg=self.bg_color, fg=self.fg_color).pack(side="left")
        self.format_var = tk.StringVar(value="mp4")
        format_combo = ttk.Combobox(options_frame, textvariable=self.format_var,
                                    values=["mp4", "mp3", "webm"], state="readonly", width=8)
        format_combo.pack(side="left", padx=10)
        
        # Qualità
        tk.Label(options_frame, text="Qualità:", bg=self.bg_color, fg=self.fg_color).pack(side="left", padx=(20, 10))
        self.quality_var = tk.StringVar(value="best")
        quality_combo = ttk.Combobox(options_frame, textvariable=self.quality_var,
                                     values=["best", "1080p", "720p", "480p", "360p"], state="readonly", width=8)
        quality_combo.pack(side="left")
        
        # Cartella download
        folder_frame = tk.Frame(self.root, bg=self.bg_color)
        folder_frame.pack(pady=10, padx=30, fill="x")
        
        tk.Label(folder_frame, text="Salva in:", bg=self.bg_color, fg=self.fg_color).pack(side="left")
        self.folder_entry = tk.Entry(folder_frame, font=("Helvetica", 10),
                                      bg=self.entry_bg, fg=self.fg_color,
                                      insertbackground=self.fg_color,
                                      width=35)
        self.folder_entry.insert(0, self.output_dir)
        self.folder_entry.pack(side="left", padx=10)
        
        btn_folder = tk.Button(folder_frame, text="📁", command=self.choose_folder,
                               bg=self.entry_bg, fg=self.fg_color, relief="flat")
        btn_folder.pack(side="left")
        
        # Pulsante download
        self.download_btn = tk.Button(self.root, text="⬇️ SCARICA VIDEO",
                                       font=("Helvetica", 14, "bold"),
                                       bg=self.accent_color, fg=self.bg_color,
                                       relief="flat", padx=30, pady=10,
                                       command=self.start_download)
        self.download_btn.pack(pady=20)
        
        # Progress bar
        self.progress = ttk.Progressbar(self.root, mode='indeterminate', length=400)
        self.progress.pack(pady=10)
        
        # Status
        self.status_label = tk.Label(self.root, text="Pronto",
                                    font=("Helvetica", 10),
                                    bg=self.bg_color, fg="#a6adc8")
        self.status_label.pack(pady=5)
        
        # Piattaforme supportate
        platforms_frame = tk.Frame(self.root, bg=self.bg_color)
        platforms_frame.pack(side="bottom", pady=15)
        
        platforms = "YouTube • Instagram • TikTok • Twitter • Facebook • LinkedIn"
        tk.Label(platforms_frame, text=platforms, font=("Helvetica", 9),
                 bg=self.bg_color, fg="#6c7086").pack()
    
    def choose_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_dir = folder
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, folder)
    
    def detect_platform(self, url):
        url = url.lower()
        if "youtube.com" in url or "youtu.be" in url:
            return "YouTube"
        elif "instagram.com" in url:
            return "Instagram"
        elif "tiktok.com" in url:
            return "TikTok"
        elif "twitter.com" in url or "x.com" in url:
            return "Twitter/X"
        elif "facebook.com" in url:
            return "Facebook"
        elif "linkedin.com" in url:
            return "LinkedIn"
        else:
            return "Sito web"
    
    def start_download(self):
        url = self.url_entry.get().strip()
        
        if not url:
            messagebox.showerror("Errore", "Inserisci un URL!")
            return
        
        if not YTDLP_AVAILABLE:
            messagebox.showerror("Errore", "Installa yt-dlp: pip install yt-dlp")
            return
        
        self.platform_label.config(text=f"Piattaforma: {self.detect_platform(url)}")
        self.download_btn.config(state="disabled")
        self.progress.start()
        self.status_label.config(text="Download in corso...")
        
        # Avvia download in thread separato
        thread = threading.Thread(target=self.download_video, args=(url,))
        thread.daemon = True
        thread.start()
    
    def download_video(self, url):
        try:
            platform = self.detect_platform(url)
            
            ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join(self.output_dir, '%(title)s.%(ext)s'),
                'progress_hooks': [self.progress_hook],
                'nocheckcertificate': True,
            }
            
            # Opzioni specifiche per Instagram
            if platform == "Instagram":
                ydl_opts.update({
                    'extractor_retries': 3,
                    'fragment_retries': 3,
                    'no_warnings': False,
                    'username': 'cookie',
                    'password': 'dummy',  # Necessario per некоторые video
                })
            
            # Opzioni specifiche per TikTok
            elif platform == "TikTok":
                ydl_opts.update({
                    'nocheckcertificate': True,
                })
            
            quality = self.quality_var.get()
            if quality != "best":
                ydl_opts['format'] = f'bestvideo[height<={quality[:-1]}]+bestaudio/best[height<={quality[:-1]}]'
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                title = info.get('title', 'Video')
            
            self.root.after(0, self.download_complete, title)
            
        except Exception as e:
            self.root.after(0, self.download_error, str(e))
    
    def progress_hook(self, d):
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', '0%')
            self.root.after(0, self.status_label.config, 
                          (f"Download: {percent}",))
    
    def download_complete(self, title):
        self.progress.stop()
        self.download_btn.config(state="normal")
        self.status_label.config(text="Completato!")
        messagebox.showinfo("✓ Fatto!", f"Video scaricato:\n{title}")
        self.status_label.config(text="Pronto")
    
    def download_error(self, error):
        self.progress.stop()
        self.download_btn.config(state="normal")
        self.status_label.config(text="Errore")
        messagebox.showerror("Errore download", str(error))

def main():
    if not YTDLP_AVAILABLE:
        print("Installazione dipendenze...")
        os.system("pip install yt-dlp")
    
    root = tk.Tk()
    app = VideoDownloaderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
