from reportlab.lib import colors
from reportlab.platypus import Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)
from datetime import datetime
import os


def generate_report(df, score, dataset_name):
    print("Inside generate_report()")
    os.makedirs("reports", exist_ok=True)

    pdf = SimpleDocTemplate(
        "reports/Data_Quality_Report.pdf"
    )

    styles = getSampleStyleSheet()

    story = []

    # ==========================================
    # Title
    # ==========================================

    title = Paragraph(
        "<font size=20><b>UNIVERSAL CSV DATA QUALITY REPORT</b></font>",
        styles["Title"]
    )

    story.append(title)
    story.append(Spacer(1, 20))

    # ==========================================
    # Dataset Information
    # ==========================================

    story.append(
        Paragraph("<b>Dataset Information</b>", styles["Heading2"])
    )

    info = [

        ["Metric", "Value"],

        ["Dataset Name", dataset_name],

        ["Rows", str(df.shape[0])],

        ["Columns", str(df.shape[1])],

        ["Memory Usage",
         f"{df.memory_usage(deep=True).sum()/1024:.2f} KB"],

        ["Generated On",
         datetime.now().strftime("%d-%m-%Y %H:%M:%S")]

    ]

    table = Table(info)

    table.setStyle(

        TableStyle([

            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),

            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),

            ("GRID", (0, 0), (-1, -1), 1, colors.black),

            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

            ("ALIGN", (0, 0), (-1, -1), "CENTER"),

            ("BOTTOMPADDING", (0, 0), (-1, 0), 10)

        ])

    )

    story.append(table)

    story.append(Spacer(1, 20))

    # ==========================================
    # Dataset Status
    # ==========================================

    if score >= 90:
        status = "Excellent"

    elif score >= 75:
        status = "Good"

    elif score >= 50:
        status = "Average"

    else:
        status = "Poor"

    # ==========================================
    # Quality Metrics
    # ==========================================

    story.append(
        Paragraph("<b>Quality Metrics</b>", styles["Heading2"])
    )

    metrics = [

        ["Metric", "Value"],

        ["Missing Values",
         str(df.isnull().sum().sum())],

        ["Duplicate Rows",
         str(df.duplicated().sum())],

        ["Empty Columns",
         str(len(df.columns[df.isnull().all()]))],

        ["Overall Score",
         f"{score:.2f}%"],

        ["Dataset Status",
         status]

    ]

    metric_table = Table(metrics)

    metric_table.setStyle(

        TableStyle([

            ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),

            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

            ("GRID", (0, 0), (-1, -1), 1, colors.black),

            ("BACKGROUND", (0, 1), (-1, -1), colors.lightgrey),

            ("ALIGN", (0, 0), (-1, -1), "CENTER"),

            ("BOTTOMPADDING", (0, 0), (-1, 0), 10)

        ])

    )

    story.append(metric_table)

    story.append(Spacer(1, 20))

    # ==========================================
    # Numeric Columns
    # ==========================================

    story.append(
        Paragraph("<b>Numeric Columns</b>", styles["Heading2"])
    )

    numeric_columns = df.select_dtypes(include="number").columns

    for col in numeric_columns:

        story.append(
            Paragraph(f"• {col}", styles["Normal"])
        )

    story.append(Spacer(1, 15))

    # ==========================================
    # Text Columns
    # ==========================================

    story.append(
        Paragraph("<b>Text Columns</b>", styles["Heading2"])
    )

    text_columns = df.select_dtypes(include="object").columns

    for col in text_columns:

        story.append(
            Paragraph(f"• {col}", styles["Normal"])
        )

    story.append(Spacer(1, 20))
    # ===========================
    #charts
    #==============
    story.append(
    Paragraph("<b>Charts</b>", styles["Heading2"])
    )

    if os.path.exists("charts/missing_values.png"):

        story.append(
            Paragraph("Missing Value Chart", styles["Heading3"])
        )

        img = Image(
            "charts/missing_values.png",
            width=400,
            height=250
        )

        story.append(img)

        story.append(Spacer(1,20))

    # -------------------------------
    # Missing Value Chart
    # -------------------------------

    if os.path.exists("charts/missing_values.png"):

        story.append(
            Paragraph("Missing Value Chart", styles["Heading3"])
        )

        img = Image(
            "charts/missing_values.png",
            width=400,
            height=250
        )

        story.append(img)

        story.append(Spacer(1,20))

    # -------------------------------
    # Histograms
    # -------------------------------

    for col in df.select_dtypes(include="number").columns:

        file = f"charts/{col}_histogram.png"

        if os.path.exists(file):

            story.append(
                Paragraph(f"{col} Histogram", styles["Heading3"])
            )

            story.append(
                Image(file, width=400, height=250)
            )

            story.append(Spacer(1,20))

    # -------------------------------
    # Boxplots
    # -------------------------------

    for col in df.select_dtypes(include="number").columns:

        file = f"charts/{col}_boxplot.png"

        if os.path.exists(file):

            story.append(
                Paragraph(f"{col} Boxplot", styles["Heading3"])
            )

            story.append(
                Image(file, width=400, height=250)
            )

            story.append(Spacer(1,20))
    # ==========================================
    # Recommendations
    # ==========================================

    story.append(
        Paragraph("<b>Recommendations</b>", styles["Heading2"])
    )

    recommendations = [

        "• Fill missing values.",

        "• Remove duplicate rows.",

        "• Review outliers.",

        "• Validate data types before analysis."

    ]

    for rec in recommendations:

        story.append(
            Paragraph(rec, styles["Normal"])
        )

    
    # ==========================================
    # Footer
    # ==========================================

    story.append(Spacer(1, 25))

    story.append(
        Paragraph(
            "<i>Report generated automatically by Universal CSV Data Quality Analyzer</i>",
            styles["Normal"]
        )
    )

    pdf.build(story)

    print("\n✅ PDF Report Generated Successfully!")