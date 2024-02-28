import pathlib
from fastapi import File, UploadFile
from fastapi import FastAPI
from sel import SeleniumController

app = FastAPI()


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    # загрузить файл
    try:
        with open(file.filename, "wb") as f:
            while contents := file.file.read(1024 * 1024):
                f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    # Передать информацию из файла на сайт
    if file.filename is not None:
        msg = SeleniumController().input_data(file.filename)

    # Удалить файл
    pathlib.Path(file.filename).unlink()

    return {"message": msg}
