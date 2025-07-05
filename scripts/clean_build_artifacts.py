import shutil
import os


def clean_build_artifacts():
    for d in ["build", "dist"]:
        shutil.rmtree(d, ignore_errors=True)
    for f in ["StudyForge.spec"]:
        if os.path.exists(f):
            os.remove(f)

    print("Cleaned build artifacts")


if __name__ == "__main__":
    clean_build_artifacts()
