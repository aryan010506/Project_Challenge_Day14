"""
Project 14 — QR Code Generator (GUI)
Authors: Aryan Sunil & Swara Gharat
Dependencies: pip install qrcode[pil]
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    data = text_entry.get().strip()
    if not data:
        messagebox.showerror("Error", "Please enter text or URL to generate QR code.")
        return

    try:
        # Create QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Save temporarily for preview
        img.save("temp_qr.png")
        qr_img = Image.open("temp_qr.png")
        qr_img = qr_img.resize((250, 250))
        qr_photo = ImageTk.PhotoImage(qr_img)

        qr_label.config(image=qr_photo)
        qr_label.image = qr_photo
        save_btn.config(state="normal")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate QR code.\n{e}")

def save_qr():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG Files", "*.png")])
    if file_path:
        try:
            # Save a fresh QR image with original size
            data = text_entry.get().strip()
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(file_path)
            messagebox.showinfo("Saved", f"QR Code saved at:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save QR code.\n{e}")

# ---------- GUI ---------- #
root = tk.Tk()
root.title("Project 14 - QR Code Generator")
root.geometry("400x500")
root.config(bg="#111")

title_label = tk.Label(root, text="QR Code Generator", font=("Arial", 16, "bold"), bg="#111", fg="#1DB954")
title_label.pack(pady=10)

instruction = tk.Label(root, text="Enter Text or URL:", bg="#111", fg="white", font=("Arial", 12))
instruction.pack(pady=5)

text_entry = tk.Entry(root, width=40, font=("Arial", 12))
text_entry.pack(pady=5)

generate_btn = tk.Button(root, text="Generate QR Code", command=generate_qr,
                         bg="#1DB954", fg="black", font=("Arial", 12, "bold"), padx=20, pady=5)
generate_btn.pack(pady=10)

qr_label = tk.Label(root, bg="#111")
qr_label.pack(pady=10)

save_btn = tk.Button(root, text="Save QR Code", command=save_qr,
                     bg="#1DB954", fg="black", font=("Arial", 12, "bold"), padx=20, pady=5, state="disabled")
save_btn.pack(pady=10)

footer = tk.Label(root, text="Day 14 of 30-Day Coding Challenge | Aryan Sunil & Swara Gharat",
                  font=("Arial", 9), bg="#111", fg="gray")
footer.pack(side="bottom", pady=5)

root.mainloop()
