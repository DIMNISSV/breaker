import tkinter as tk
import time


# Функция, которая блокирует экран
def block_screen(n_seconds):
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    label = tk.Label(root, text="Перерыв", font=("Arial", 100))
    label.pack(expand=True)

    # Отображаем таймер оставшегося времени
    time_remaining = n_seconds
    timer_label = tk.Label(root, text=str(time_remaining), font=("Arial", 50))
    timer_label.pack(expand=True)

    def update_timer():
        nonlocal time_remaining
        time_remaining -= 1
        timer_label.config(text=str(time_remaining))
        if time_remaining > 0:
            timer_label.after(1000, update_timer)
        else:
            root.destroy()

    update_timer()

    # Добавляем обработчик закрытия окна
    def on_closing():
        nonlocal n_seconds
        n_seconds += 10
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()


# Основной цикл программы
def main():
    # Параметры времени
    n_seconds = 10  # Длительность перерыва в секундах
    m_minutes = 1  # Интервал между перерывами в минутах

    while True:
        # Блокируем экран на n_seconds секунд
        block_screen(n_seconds)

        # Ждем m_minutes минут перед следующим перерывом
        time.sleep(m_minutes * 60)


if __name__ == '__main__':
    main()
