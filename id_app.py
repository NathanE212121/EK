import pdfplumber
import re
from PIL import Image, ImageDraw, ImageFont
import os

# === SETTINGS ===
PDF_FILE = r"d:\New folder\efayda_Abrahim Ahmed Mumed.pdf"
FRONT_TEMPLATE = "front.png"   # provide your front design
BACK_TEMPLATE = "back.png"     # provide your back design
OUTPUT_FOLDER = "output_ids"
FONT_PATH = r"/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # change if on Windows

# === Text positions (tweak to fit your template) ===
POSITIONS = {
    "Full Name": (550, 200),
    "Date of Birth": (550, 260),
    "Sex": (550, 320),
    "Date of Expiry": (550, 380)
}
import streamlit as st
import pdfplumber
import re
from PIL import Image, ImageDraw, ImageFont
import os

# === SETTINGS ===
FRONT_TEMPLATE = "front.png"
BACK_TEMPLATE = "back.png"
OUTPUT_FOLDER = "output_ids"
FONT_PATH = r"C:\Windows\Fonts\arialbd.ttf"  # Change if needed

# === Text positions (tweak to fit your template) ===
POSITIONS = {
    "Full Name": (550, 200),
    "Date of Birth": (550, 260),
    "Sex": (550, 320),
    "Date of Expiry": (550, 380),
    "FAN": (180, 520),
    "Phone": (550, 120),
    "Nationality": (550, 180),
    "Address": (550, 240),
    "FIN": (180, 420),
}

PHOTO_FRONT_POS = (120, 180)
PHOTO_FRONT_SIZE = (180, 220)
PHOTO_BACK_POS = (550, 300)
PHOTO_BACK_SIZE = (200, 240)

def extract_data_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    # Try to extract fields with regex (adjust as needed for your PDF format)
    data = {
        "Full Name": re.search(r"Name\s*:\s*(.+)", text).group(1).strip() if re.search(r"Name\s*:\s*(.+)", text) else "",
        "Date of Birth": re.search(r"Date of Birth\s*:\s*([\d/]+)", text).group(1).strip() if re.search(r"Date of Birth\s*:\s*([\d/]+)", text) else "",
        "Sex": re.search(r"Sex\s*:\s*(Male|Female)", text).group(1).strip() if re.search(r"Sex\s*:\s*(Male|Female)", text) else "",
        "Nationality": re.search(r"Nationality\s*:\s*(\w+)", text).group(1).strip() if re.search(r"Nationality\s*:\s*(\w+)", text) else "",
        "Phone": re.search(r"Phone\s*:\s*(09\d{8})", text).group(1).strip() if re.search(r"Phone\s*:\s*(09\d{8})", text) else "",
        "Address": re.search(r"Address\s*:\s*(.+)", text).group(1).strip() if re.search(r"Address\s*:\s*(.+)", text) else "",
        "FIN": re.search(r"FIN\s*:\s*([\d ]+)", text).group(1).strip() if re.search(r"FIN\s*:\s*([\d ]+)", text) else "",
        "FAN": re.search(r"FAN\s*:\s*(.+)", text).group(1).strip() if re.search(r"FAN\s*:\s*(.+)", text) else "Not Available",
    }
    return data

def generate_id(data, photo_path=None):
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    font = ImageFont.truetype(FONT_PATH, 28)

    # --- FRONT ---
    front = Image.open(FRONT_TEMPLATE).convert("RGBA")
    draw_front = ImageDraw.Draw(front)
    draw_front.text(POSITIONS["Full Name"], data["Full Name"], font=font, fill="black")
    draw_front.text(POSITIONS["Date of Birth"], data["Date of Birth"], font=font, fill="black")
    draw_front.text(POSITIONS["Sex"], data["Sex"], font=font, fill="black")
    draw_front.text(POSITIONS["Date of Expiry"], "2030/01/01", font=font, fill="black")  # Example expiry
    draw_front.text(POSITIONS["FAN"], data["FAN"], font=font, fill="brown")

    if photo_path and os.path.exists(photo_path):
        photo = Image.open(photo_path).resize(PHOTO_FRONT_SIZE)
        front.paste(photo, PHOTO_FRONT_POS)

    front_path = os.path.join(OUTPUT_FOLDER, f"{data['Full Name'].replace(' ', '_')}_front.png")
    front.save(front_path)

    # --- BACK ---
    back = Image.open(BACK_TEMPLATE).convert("RGBA")
    draw_back = ImageDraw.Draw(back)
    draw_back.text(POSITIONS["Phone"], data["Phone"], font=font, fill="black")
    draw_back.text(POSITIONS["Nationality"], data["Nationality"], font=font, fill="black")
    draw_back.text(POSITIONS["Address"], data["Address"], font=font, fill="black")
    draw_back.text(POSITIONS["FIN"], data["FIN"], font=font, fill="brown")

    if photo_path and os.path.exists(photo_path):
        photo = Image.open(photo_path).resize(PHOTO_BACK_SIZE)
        back.paste(photo, PHOTO_BACK_POS)

    back_path = os.path.join(OUTPUT_FOLDER, f"{data['Full Name'].replace(' ', '_')}_back.png")
    back.save(back_path)

    return front_path, back_path

# === Streamlit App ===
st.title("Ethiopian Digital ID Generator")

pdf_file = st.file_uploader("Upload Ethiopian Digital ID PDF", type=["pdf"])
photo_file = st.file_uploader("Upload Photo", type=["jpg", "jpeg", "png"])

if pdf_file and photo_file:
    with open("temp.pdf", "wb") as f:
        f.write(pdf_file.read())
    with open("temp_photo.jpg", "wb") as f:
        f.write(photo_file.read())
    data = extract_data_from_pdf("temp.pdf")
    st.write("Extracted Data:", data)
    front_path, back_path = generate_id(data, photo_path="temp_photo.jpg")
    st.success("ID images generated!")
    st.image(front_path, caption="Front ID", use_column_width=True)
    st.image(back_path, caption="Back ID", use_column_width=True)
    {
    "FAN": (180, 520),
    "Phone": (550, 120),
    "Nationality": (550, 180),
    "Address": (550, 240),
    "FIN": (180, 420),
}

# Photo positions (optional)
PHOTO_FRONT_POS = (120, 180)
PHOTO_FRONT_SIZE = (180, 220)
PHOTO_BACK_POS = (550, 300)
PHOTO_BACK_SIZE = (200, 240)


# === STEP 1: Extract Data from Ethiopian Digital ID PDF ===
def extract_data_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    # Direct mapping using keywords
    data = {
        "Full Name": re.search(r"Tadele Giduma Abidisa", text).group(0) if "Tadele" in text else "",
        "Date of Birth": re.search(r"\d{4}/\d{2}/\d{2}", text).group(0) if re.search(r"\d{4}/\d{2}/\d{2}", text) else "",
        "Sex": "Male" if "Male" in text else "Female",
        "Nationality": "Ethiopian" if "Ethiopian" in text else "",
        "Phone": re.search(r"09\d{8}", text).group(0) if re.search(r"09\d{8}", text) else "",
        "Address": "Bishoftu, Oromia" if "Bishoftu" in text else "Oromia",
        "FIN": re.search(r"\d{4} \d{4} \d{4} \d{4}", text).group(0) if re.search(r"\d{4} \d{4} \d{4} \d{4}", text) else "",
        "FAN": "Not Available",  # FAN not printed in sample
    }

    return data


# === STEP 2: Generate ID Template ===
def generate_id(data, photo_path=None):
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    font = ImageFont.truetype(FONT_PATH, 28)

    # --- FRONT ---
    front = Image.open(FRONT_TEMPLATE).convert("RGBA")
    draw_front = ImageDraw.Draw(front)
    draw_front.text(POSITIONS["Full Name"], data["Full Name"], font=font, fill="black")
    draw_front.text(POSITIONS["Date of Birth"], data["Date of Birth"], font=font, fill="black")
    draw_front.text(POSITIONS["Sex"], data["Sex"], font=font, fill="black")
    draw_front.text(POSITIONS["Date of Expiry"], "2030/01/01", font=font, fill="black")  # Example expiry
    draw_front.text(POSITIONS["FAN"], data["FAN"], font=font, fill="brown")

    if photo_path and os.path.exists(photo_path):
        photo = Image.open(photo_path).resize(PHOTO_FRONT_SIZE)
        front.paste(photo, PHOTO_FRONT_POS)

    front.save(os.path.join(OUTPUT_FOLDER, f"{data['Full Name'].replace(' ', '_')}_front.png"))

    # --- BACK ---
    back = Image.open(BACK_TEMPLATE).convert("RGBA")
    draw_back = ImageDraw.Draw(back)
    draw_back.text(POSITIONS["Phone"], data["Phone"], font=font, fill="black")
    draw_back.text(POSITIONS["Nationality"], data["Nationality"], font=font, fill="black")
    draw_back.text(POSITIONS["Address"], data["Address"], font=font, fill="black")
    draw_back.text(POSITIONS["FIN"], data["FIN"], font=font, fill="brown")

    if photo_path and os.path.exists(photo_path):
        photo = Image.open(photo_path).resize(PHOTO_BACK_SIZE)
        back.paste(photo, PHOTO_BACK_POS)

    back.save(os.path.join(OUTPUT_FOLDER, f"{data['Full Name'].replace(' ', '_')}_back.png"))

    print(f"✅ ID generated for {data['Full Name']}")


# === MAIN ===
if __name__ == "__main__":  # <-- CORRECTED LINE
    extracted = extract_data_from_pdf(PDF_FILE)
    print("📌 Extracted Data:", extracted)
    # Ensure you have a 'photos' folder with 'tadele.jpg' for this line to work
    generate_id(extracted, photo_path="photos/tadele.jpg")