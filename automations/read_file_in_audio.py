import fitz  # PyMuPDF
import docx
import os
from gtts import gTTS

class ReadAudio:
    """
    Class ReadAudio wil implement reading of a text file into audio
    Packagaes: PyMuPDF (for PDFs), python-docx (for Word files), and gTTS (Google Text-to-Speech) to generate audio.
    """
    def __init__(self, file_path=None) -> None:
        self.file_path = file_path


    def extract_text_from_pdf(pdf_path):
        """Extract text from a PDF file."""
        text = ""
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text("text") + "\n"
        return text.strip()

    def extract_text_from_docx(docx_path):
        """Extract text from a Word file."""
        doc = docx.Document(docx_path)
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
