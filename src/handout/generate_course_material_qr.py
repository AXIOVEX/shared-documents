from pathlib import Path
import qrcode
from qrcode.constants import ERROR_CORRECT_H

ROOT = Path(__file__).parent
MEDIA = ROOT / "media"
MEDIA.mkdir(parents=True, exist_ok=True)
ITEMS = {
    "course-slides-qr.png": "https://axiovex.github.io/shared-documents/docs/ai-101-beyond-the-chatbot-slides.pdf",
    "handout-qr.png": "https://axiovex.github.io/shared-documents/docs/ai-101-handout.pdf",
}
for filename, url in ITEMS.items():
    qr = qrcode.QRCode(version=None, error_correction=ERROR_CORRECT_H, box_size=20, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    image = qr.make_image(fill_color="#081F32", back_color="#FFFFFF")
    output = MEDIA / filename
    image.save(output)
    print(f"{output}\t{url}")
