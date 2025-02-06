import os
from fpdf import FPDF

PDF_STORAGE_PATH = "data"

def create_pdfs():
    """Generates 10 PDFs with meaningful one-line sentences."""
    os.makedirs(PDF_STORAGE_PATH, exist_ok=True)

    pdf_sentences = [
    "In the small town of Eldridge, the citizens were preparing for the annual Harvest Festival when an unexpected storm hit, forcing everyone to take shelter in the town hall, where they discovered an old map hidden inside a wooden chest, sparking rumors of a long-lost treasure buried beneath the town.",
    "Lena, a young scientist, stumbled upon a mysterious artifact during her expedition in the Amazon rainforest. The artifact emitted a faint glow and seemed to hold secrets of an ancient civilization long forgotten, and Lena vowed to unlock its mysteries, unaware of the dangers that awaited her.",
    "A team of explorers embarked on a journey to the North Pole to study the effects of climate change on the polar ice caps, but their mission took a strange turn when they discovered a hidden underground cave system, where they found ancient cave paintings depicting beings not of this world.",
    "In the year 2125, humanity had colonized Mars, and life on the red planet was flourishing. However, a series of unexplained malfunctions at the main colony caused widespread panic, leading a small group of astronauts to venture into the Martian wilderness to investigate the mysterious events and uncover the truth behind the disturbances.",
    "During a peaceful day at the village square, an old man named Victor arrived with a peculiar story of a parallel world existing just beyond the edge of the forest. His tale was met with skepticism, but as strange occurrences began to happen in the village, the townspeople started to question if there was more to his story than they initially believed."
  
   
    ]

    for i, sentence in enumerate(pdf_sentences, start=1):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=sentence, ln=True, align="C")
        pdf_file = os.path.join(PDF_STORAGE_PATH, f"doc_{i}.pdf")
        pdf.output(pdf_file)

    print(f"✅ Created {len(pdf_sentences)} PDFs in '{PDF_STORAGE_PATH}' folder.")
