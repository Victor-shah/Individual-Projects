import io
from pypdf import PdfReader
from openai import OpenAI
from app.config import settings
from app.schemas import StructuredProjectBrief

class AIEngine:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def extract_text_from_pdf(self, pdf_bytes: bytes) -> str:
        """Parses raw bytes from an uploaded PDF and converts it into pure text."""
        pdf_file = io.BytesIO(pdf_bytes)
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text

    def analyze_brief(self, raw_text: str) -> StructuredProjectBrief:
        """Leverages OpenAI's Beta Structured Output engine to guarantee validation against our Pydantic scheme."""
        system_prompt = (
            "You are an expert AI Solutions Architect at Brainlake Agency. "
            "Analyze the following messy, unstructured client brief or inquiry. "
            "Extract operational targets, technical parameters, features, and map out a clean architecture structure."
        )

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Here is the unstructured client document:\n\n{raw_text}"}
            ],
            response_format=StructuredProjectBrief,
        )
        
        return completion.choices[0].message.parsed
