import os
import fitz  # PyMuPDF
import docx
from gtts import gTTS

class ReadAudio:
    """
    Class ReadAudio will implement reading of a text file into audio
    function extract_text_from_pdf & extract_text_from_docx: Extracts text from a PDF or Word document.
    function text_to_speech: Converts the extracted text into speech using gTTS.
    Saves the speech as an MP3 file.
    paramenters:
        Input: pdf_path or docx_path
        Output: Audio mp3 of the files
    Packagaes: PyMuPDF (for PDFs), python-docx (for Word files), and gTTS (Google Text-to-Speech) to generate audio.
    """
    def __init__(self, pdf_path=None, docx_path=None) -> None:
        self.pdf_path = pdf_path
        self.docx_path = docx_path

    def extract_text_from_pdf(self):
        """Extract text from a PDF file."""
        text = ""
        doc = fitz.open(self.pdf_path)
        for page in doc:
            text += page.get_text("text") + "\n"
        return text.strip()
    # utils?
    def extract_text_from_docx(self):
        """Extract text from a Word file."""
        doc = docx.Document(self.docx_path)
        return "\n".join([para.text for para in doc.paragraphs]).strip()

def text_to_speech(text, output_audio):
    """Convert text to speech and save as an audio file."""
    if not text:
        print("No text extracted.")
        return

    tts = gTTS(text=text, lang="en")
    tts.save(output_audio)
    print(f"Audio saved as {output_audio}")

def process_file(file_path):
    """Determine file type and process accordingly."""
    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    else:
        print("Unsupported file format.")
        return
    
    output_audio = os.path.splitext(file_path)[0] + ".mp3"
    text_to_speech(text, output_audio)

# Example usage
file_path = "example.pdf"  # Change this to your actual file path
process_file(file_path)


def run():
    directory_name = "pdf_docx_files"
    file_name = "1-introduction-bash-shell-linux-mac-os-m1-overview-slides"
    pdffile = os.path.join(directory_name, file_name)
    pdf_file_instance = ReadAudio(pdffile)
    docx_file_instance = ReadAudio()
    return text_to_speech(pdf_file_instance.extract_text_from_pdf, output_audio=None)