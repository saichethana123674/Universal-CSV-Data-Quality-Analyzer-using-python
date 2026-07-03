import os
from datetime import datetime


def generate_dashboard(df, score, dataset_name):

    os.makedirs("reports", exist_ok=True)

    # -----------------------------------
    # Dataset Status
    # -----------------------------------

    if score >= 90:
        status = "🟢 Excellent"
    elif score >= 75:
        status = "🔵 Good"
    elif score >= 50:
        status = "🟡 Average"
    else:
        status = "🔴 Poor"

    # -----------------------------------
    # Display Dataset Name
    # -----------------------------------

    display_name = (
        dataset_name
        .replace(".csv", "")
        .replace("_", " ")
        .title()
    )

    # -----------------------------------
    # Generate Charts HTML
    # -----------------------------------

    charts_html = ""

    # Missing Value Chart
    if os.path.exists("charts/missing_values.png"):

        charts_html += """
        <h2 class="section-title">Missing Value Chart</h2>
        <img src="../charts/missing_values.png">
        """

    # Histograms
    for column in df.select_dtypes(include="number").columns:

        histogram = f"charts/{column}_histogram.png"

        if os.path.exists(histogram):

            charts_html += f"""
            <h2 class="section-title">{column} Histogram</h2>
            <img src="../{histogram}">
            """

    # Boxplots
    for column in df.select_dtypes(include="number").columns:

        boxplot = f"charts/{column}_boxplot.png"

        if os.path.exists(boxplot):

            charts_html += f"""
            <h2 class="section-title">{column} Box Plot</h2>
            <img src="../{boxplot}">
            """

    # -----------------------------------
    # HTML
    # -----------------------------------

    html = f"""
<!DOCTYPE html>

<html>

<head>

<title>Universal CSV Data Quality Dashboard</title>

<style>

body {{
    font-family: Arial, Helvetica, sans-serif;
    background:#eef3f8;
    margin:0;
}}

.header {{
    background:linear-gradient(90deg,#0f4c81,#1976d2);
    color:white;
    text-align:center;
    padding:30px;
}}

.container {{
    width:90%;
    margin:auto;
    padding:30px;
}}

.cards {{
    display:flex;
    flex-wrap:wrap;
    gap:20px;
    margin-bottom:30px;
}}

.card {{
    flex:1;
    min-width:220px;
    background:white;
    border-radius:12px;
    padding:25px;
    text-align:center;
    box-shadow:0px 5px 15px rgba(0,0,0,.15);
}}

.card h2 {{
    color:#1976d2;
}}

.card p {{
    font-size:26px;
    font-weight:bold;
}}

.score {{
    color:green;
}}

table {{
    width:100%;
    border-collapse:collapse;
    background:white;
    box-shadow:0px 5px 15px rgba(0,0,0,.15);
}}

th {{
    background:#1976d2;
    color:white;
    padding:12px;
}}

td {{
    padding:12px;
    text-align:center;
    border-bottom:1px solid #ddd;
}}

.section-title {{
    color:#0f4c81;
    margin-top:40px;
}}

img {{
    width:90%;
    max-width:900px;
    display:block;
    margin:auto;
    margin-top:20px;
    margin-bottom:30px;
    border-radius:10px;
    box-shadow:0px 5px 15px rgba(0,0,0,.2);
}}

.footer {{
    margin-top:60px;
    text-align:center;
    color:gray;
    padding:20px;
}}

</style>

</head>

<body>

<div class="header">

<h1>📊 Universal CSV Data Quality Dashboard</h1>

<p>Professional Dataset Analysis Report</p>

</div>

<div class="container">

<div class="cards">

<div class="card">
<h2>Dataset</h2>
<p>{display_name}</p>
</div>

<div class="card">
<h2>Rows</h2>
<p>{df.shape[0]}</p>
</div>

<div class="card">
<h2>Columns</h2>
<p>{df.shape[1]}</p>
</div>

<div class="card">
<h2>Quality Score</h2>
<p class="score">{score:.2f}/100</p>
</div>

<div class="card">
<h2>Status</h2>
<p>{status}</p>
</div>

</div>

<h2 class="section-title">Dataset Information</h2>

<table>

<tr>
<th>Metric</th>
<th>Value</th>
</tr>

<tr>
<td>Rows</td>
<td>{df.shape[0]}</td>
</tr>

<tr>
<td>Columns</td>
<td>{df.shape[1]}</td>
</tr>

<tr>
<td>Missing Values</td>
<td>{df.isnull().sum().sum()}</td>
</tr>

<tr>
<td>Duplicate Rows</td>
<td>{df.duplicated().sum()}</td>
</tr>

<tr>
<td>Memory Usage</td>
<td>{df.memory_usage(deep=True).sum()/1024:.2f} KB</td>
</tr>

<tr>
<td>Generated On</td>
<td>{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}</td>
</tr>

</table>

{charts_html}

<div class="footer">

<hr>

<h3>Developed By</h3>

<p><b>Universal CSV Data Quality Analyzer</b></p>

<p>Version 1.0</p>

<p>© 2026 All Rights Reserved</p>

</div>

</div>

</body>

</html>
"""

    with open(
        "reports/dashboard.html",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html)

    print("✅ HTML Dashboard Generated Successfully!")