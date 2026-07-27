from multiprocessing import freeze_support
from pathlib import Path

from ultralytics import YOLO


def main():
    project_dir = Path(__file__).resolve().parent
    data_yaml = project_dir / "Dataset" / "data.yaml"
    output_dir = project_dir / "runs" / "aerial_detection"

    if not data_yaml.exists():
        raise FileNotFoundError(
            f"Dataset YAML file was not found:\n{data_yaml}"
        )

    model = YOLO("yolov8n.pt")

    results = model.train(
        data=str(data_yaml),
        epochs=5,
        imgsz=640,
        batch=8,
        device=0,
        workers=4,
        project=str(output_dir),
        name="baseline_v1",
        patience=20,
        exist_ok=True,
    )

    print("Training completed successfully.")
    print(f"Results saved in: {results.save_dir}")


if __name__ == "__main__":
    freeze_support()
    main()


# from ultralytics import YOLO

# model = YOLO("yolov8n.pt")

# results = model.train(
#     data=r"E:\VS Code Environment\VS code\Dataset\data.yaml",
#     epochs=10,
#     imgsz=640,
#     batch=8,
#     device=0,
#     workers=4,
#     project=r"E:\VS Code Environment\VS code\runs\aerial_detection",
#     name="baseline_v1",
#     patience=20,
# )