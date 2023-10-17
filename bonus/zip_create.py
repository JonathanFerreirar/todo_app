import zipfile
import pathlib


def make_archive(filepaths, dest_dit):
    dest = pathlib.Path(dest_dit, "compressed.zip")
    with zipfile.ZipFile(dest, 'w') as archive:
        for filepath in filepaths:
            filepath_trated = pathlib.Path(filepath)
            archive.write(filepath_trated, arcname=filepath_trated.name)
