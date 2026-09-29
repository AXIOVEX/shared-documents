from pathlib import Path
import base64

ROOT = Path(__file__).parent
html_path = ROOT / "index.html"
qr_path = ROOT / "media" / "humans-need-not-apply-qr.png"
html = html_path.read_text(encoding="utf-8")
if "QR_DATA" not in html:
    raise SystemExit("QR_DATA placeholder not found")
uri = base64.b64encode(qr_path.read_bytes()).decode("ascii")
html_path.write_text(html.replace("QR_DATA", uri), encoding="utf-8")
