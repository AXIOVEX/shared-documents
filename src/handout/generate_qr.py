from pathlib import Path
import qrcode
from qrcode.constants import ERROR_CORRECT_H

URL = "https://www.youtube.com/watch?v=CMFj75kBQlU"
OUT = Path(__file__).parent / "media" / "humans-need-not-apply-qr.png"
qr = qrcode.QRCode(version=None, error_correction=ERROR_CORRECT_H, box_size=18, border=4)
qr.add_data(URL)
qr.make(fit=True)
img = qr.make_image(fill_color="#0B1F33", back_color="#FFFFFF")
img.save(OUT)
print(OUT)
