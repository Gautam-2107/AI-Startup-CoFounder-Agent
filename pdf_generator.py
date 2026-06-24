
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(report_text, filename):

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    for line in report_text.split("\n"):

        if line.strip():
            content.append(
                Paragraph(
                    line.replace("&", "&amp;")
                        .replace("<", "&lt;")
                        .replace(">", "&gt;"),
                    styles["BodyText"]
                )
            )

            content.append(Spacer(1, 6))

    pdf.build(content)

