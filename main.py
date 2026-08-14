import glob
import img2pdf
import os
import zipfile

FolderPath = input("Please input the path to your folder: ")

for FileName in os.listdir(FolderPath):
    if FileName.endswith(".cbz"):
        OldName = os.path.join(FolderPath, FileName)
        NewName = os.path.join(FolderPath, FileName.replace(".cbz", ".zip"))
        os.rename(OldName, NewName)

for ZipFile in os.listdir(FolderPath):
    if ZipFile.endswith(".zip"):
        with zipfile.ZipFile(os.path.join(FolderPath, ZipFile), 'r') as ZipInst:
            ZipInst.extractall(os.path.join(FolderPath, ZipFile.replace(".zip", "")))
        
for FolderName in os.listdir(FolderPath):
    SubFolderPath = os.path.join(FolderPath, FolderName)
    if os.path.isdir(SubFolderPath):
        ImagePaths = glob.glob(f"{SubFolderPath}/*.jpg") + glob.glob(f"{SubFolderPath}/*.png") + glob.glob(f"{SubFolderPath}/*.jpeg")
        ImagePaths = sorted(ImagePaths)
        PdfOutput = os.path.join(os.path.dirname(SubFolderPath), f"{FolderName}.pdf")
        with open(PdfOutput, "wb") as WritePdf:
            WritePdf.write(img2pdf.convert([str(page) for page in ImagePaths]))

for ZipFile in os.listdir(FolderPath):
    if ZipFile.endswith(".zip"):
        os.rename(os.path.join(FolderPath, ZipFile), os.path.join(FolderPath, ZipFile.replace(".zip", ".cbz")))