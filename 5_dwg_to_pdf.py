import win32com.client
import os
import time 
# This code only works for simple dwg file drawings.
# Initialize AutoCAD application
acad = win32com.client.Dispatch("AutoCAD.Application")

# Set AutoCAD to be visible (optional, you can set it to False to run in the background)
acad.Visible = True

# Open the DWG file
dwg_file = r"Documents/autocad/1.bodrum kat yk- ky calisma.dwg"  #your file adress
doc = acad.Documents.Open(dwg_file)
time.sleep(4)  # Wait for 2 seconds to ensure AutoCAD is ready

# Set the PDF plotter (AutoCAD default PDF plotter)
plotter_name = "DWG To PDF.pc3"


# Check if the file exists
if not os.path.exists(dwg_file):
    print(f"Error: The DWG file at {dwg_file} does not exist.")
else:
    # Open the DWG file
    try:
        doc = acad.Documents.Open(dwg_file)
        print(f"Successfully opened the DWG file: {dwg_file}")

        # Set the PDF plotter (AutoCAD default PDF plotter)
        plotter_name = "DWG To PDF.pc3"

        # Set the output PDF path
        output_pdf_path = r"/Documents/autocad/OutputDrawing.pdf"  #The address you requested.

        # Set the plotter and page settings
        plot = doc.Plot
        #plot.PlotCentered = True  # Center the plot on the page
        #plot.ScaleMode = 0  # Fit to paper
        #plot.PlotRotation = 0  # Portrait orientation
        #plot.PlotWithLineweights = True  # Use lineweights for the plot

        # Select the plot configuration (PDF)
        #plot.ConfigurationName = plotter_name  # Set the plotter (DWG to PDF)

        # Set the output file for PDF plot
        plot.PlotToFile(output_pdf_path)
        time.sleep(20) 
        print(f"PDF plot was successful: {output_pdf_path}")

        # Close the document (optional, without saving)
        doc.Close(False)

    except Exception as e:
        print(f"Error opening or plotting the DWG file: {e}")

    # Quit AutoCAD (optional)
    acad.Quit()

print(f"DWG has been successfully converted to PDF.")