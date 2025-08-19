# main.py
from bokeh.plotting import figure, show, output_file
from datetime import datetime
import re
import webbrowser

# Baca file
with open("soal_chart_bokeh.txt", "r") as f:
    lines = f.readlines()

timestamps = []
speeds = []

current_time = None
for line in lines:
    # Cari timestamp
    if line.startswith("Timestamp:"):
        ts_str = line.replace("Timestamp:", "").strip()
        current_time = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S")
    
    # Cari baris rata-rata sender (bitrate)
    if "sender" in line and "sec" in line and "Mbits/sec" in line:
        parts = line.split()
        try:
            mbps = float(parts[6])  # kolom "bitrate" (Mbits/sec)
            timestamps.append(current_time)
            speeds.append(mbps)
        except:
            pass

# Buat grafik dengan Bokeh
output_file("line_chart.html")

p = figure(title="Testing Jaringan",
           x_axis_label="DATE TIME",
           y_axis_label="Speed (Mbps)",
           x_axis_type="datetime",
           width=800, height=400)

p.line(timestamps, speeds, line_width=2, legend_label="Sender Speed", color="blue")
p.scatter(timestamps, speeds, size=6, color="red", legend_label="Data Point")


p.legend.location = "top_left"

show(p)

webbrowser.open("line_chart.html")
