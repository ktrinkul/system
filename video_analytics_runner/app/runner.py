import asyncio
import cv2

# Глобальные переменные для статистики
processed_frames = 0
detections_per_frame = {}

def detect_objects(frame):
    """
    Заглушка функции детекции объектов.
    Принимает кадр, возвращает список детекций.
    """
    # TODO: здесь позже вставим реальный алгоритм ML
    return [{'bbox': [50, 50, 150, 150], 'class': 'person', 'score': 0.6}]

async def process_video(video_path: str):
    global processed_frames, detections_per_frame

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Не удалось открыть видео: {video_path}")
        return

    frame_number = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Видео закончилось или ошибка чтения")
            break

        # Вызовем функцию детекции
        detections = detect_objects(frame)

        # Сохраняем данные для статистики
        detections_per_frame[frame_number] = detections

        print(f"Обработан кадр {frame_number}, обнаружения: {detections}")

        frame_number += 1
        processed_frames = frame_number

        await asyncio.sleep(0.04)  # ~25 FPS

    cap.release()
    print("Обработка видео завершена.")

def print_status():
    print(f"\nСтатистика на данный момент:")
    print(f"Обработано кадров: {processed_frames}")
    for frame_num, dets in detections_per_frame.items():
        print(f" Кадр {frame_num}, детекции: {dets}")

import asyncio

async def main():
    video_path = "/Users/ekaterinagoryacheva/Desktop/проект_бэк/video_analytics_runner/app/19.mp4"
    task = asyncio.create_task(process_video(video_path))

    try:
        while not task.done():
            try:
                await asyncio.sleep(2)
            except asyncio.CancelledError:
                # Когда прерывают sleep, ловим это, чтобы вывести статистику
                print("\nПрерывание во время ожидания. Текущая статистика:")
                print_status()
                # прерываем главный таск, чтобы программа завершилась
                task.cancel()
                break
            print_status()
        # Ждем, если таск еще не завершился (если не отменили)
        if not task.cancelled():
            await task
    except KeyboardInterrupt:
        # Дополнительный catch для Ctrl+C вне sleep
        print("\nПрерывание пользователем. Итоговая статистика:")
        print_status()
    except asyncio.CancelledError:
        # Если сам таск отменён
        print("\nОбработка видео отменена. Итоговая статистика:")
        print_status()

if __name__ == "__main__":
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())
